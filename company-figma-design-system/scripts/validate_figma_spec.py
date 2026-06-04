#!/usr/bin/env python3
"""Basic static validator for company Figma design-system specs.

Input:
  A JSON export or normalized node tree from Figma.

This script is intentionally conservative. It reports likely issues and TODO
gaps instead of pretending every Figma rule can be validated from arbitrary
JSON exports.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
TOKENS_PATH = ROOT / "assets" / "tokens.json"
COMPONENTS_PATH = ROOT / "assets" / "components.json"

HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")
GENERIC_LAYER_RE = re.compile(
    r"^(Frame|Group|Rectangle|Vector|Instance|Component|Text|Line|Ellipse|"
    r"Star|Polygon)\s*\d*(\s*copy\s*\d*)?$",
    re.IGNORECASE,
)
FRAME_TYPE_VALUES = {"FRAME", "Frame", "frame"}
COMPONENTISH_TYPES = {"COMPONENT", "COMPONENT_SET", "INSTANCE", "Component", "Instance"}
HANDMADE_COMPONENT_RE = re.compile(r"\b(button|btn|input|table|card|按钮|输入框|表格|卡片)\b", re.IGNORECASE)
STATE_RE = {
    "empty": re.compile(r"\b(empty|no data|空|暂无|无数据)\b", re.IGNORECASE),
    "loading": re.compile(r"\b(loading|加载|载入|spinner)\b", re.IGNORECASE),
    "error": re.compile(r"\b(error|danger|错误|失败|异常)\b", re.IGNORECASE),
}


@dataclass
class Finding:
    severity: str
    check: str
    message: str
    path: str = ""
    node_name: str = ""
    value: Any = None


@dataclass
class ValidationContext:
    allowed_colors: set[str]
    allowed_font_sizes: set[float]
    allowed_spacing: set[float]
    component_names: set[str]
    findings: list[Finding] = field(default_factory=list)

    def add(self, severity: str, check: str, message: str, path: str = "", node_name: str = "", value: Any = None) -> None:
        self.findings.append(Finding(severity, check, message, path, node_name, value))


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def collect_token_values(tokens: dict[str, Any]) -> tuple[set[str], set[float], set[float]]:
    colors: set[str] = set()
    font_sizes: set[float] = set()
    spacing: set[float] = set()

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for k, v in value.items():
                if k == "font_size" and isinstance(v, (int, float)):
                    font_sizes.add(float(v))
                elif isinstance(v, str):
                    for match in HEX_RE.findall(v):
                        colors.add(match.upper())
                elif isinstance(v, (int, float)):
                    # Numeric token values outside typography are usually spacing,
                    # radius, icon size, or layout dimensions. Spacing is checked
                    # against tokens["spacing"]["scale"] below instead of all nums.
                    pass
                walk(v)
        elif isinstance(value, list):
            for item in value:
                walk(item)
        elif isinstance(value, str):
            for match in HEX_RE.findall(value):
                colors.add(match.upper())

    walk(tokens.get("color", {}))
    walk(tokens.get("typography", {}))

    def walk_spacing(value: Any) -> None:
        if isinstance(value, dict):
            for item in value.values():
                walk_spacing(item)
        elif isinstance(value, list):
            for item in value:
                walk_spacing(item)
        elif isinstance(value, (int, float)):
            spacing.add(float(value))
        elif isinstance(value, str):
            for match in re.findall(r"(?<![\w.])(\d+(?:\.\d+)?)px\b", value):
                spacing.add(float(match))

    walk_spacing(tokens.get("spacing", {}))

    return colors, font_sizes, spacing


def collect_component_names(components: dict[str, Any]) -> set[str]:
    names = set()
    for component in components.get("components", []):
        name = component.get("name")
        if isinstance(name, str):
            names.add(name.lower())
    return names


def node_children(node: Any) -> Iterable[Any]:
    if not isinstance(node, dict):
        return []
    for key in ("children", "nodes", "layers"):
        children = node.get(key)
        if isinstance(children, list):
            return children
    return []


def node_type(node: dict[str, Any]) -> str:
    return str(node.get("type") or node.get("nodeType") or "")


def node_name(node: dict[str, Any]) -> str:
    name = node.get("name")
    return name if isinstance(name, str) else ""


def is_component_instance(node: dict[str, Any]) -> bool:
    ntype = node_type(node)
    if ntype in COMPONENTISH_TYPES:
        return True
    if node.get("componentId") or node.get("component_id") or node.get("mainComponent"):
        return True
    return False


def iter_nodes(root: Any, path: str = "$") -> Iterable[tuple[dict[str, Any], str]]:
    if isinstance(root, dict):
        yield root, path
        for index, child in enumerate(node_children(root)):
            yield from iter_nodes(child, f"{path}.children[{index}]")
    elif isinstance(root, list):
        for index, item in enumerate(root):
            yield from iter_nodes(item, f"{path}[{index}]")


def extract_hex_colors(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, str):
        found.update(match.upper() for match in HEX_RE.findall(value))
    elif isinstance(value, dict):
        # Common normalized format: {"r": 1, "g": 1, "b": 1}
        if all(k in value for k in ("r", "g", "b")):
            try:
                r = round(float(value["r"]) * 255)
                g = round(float(value["g"]) * 255)
                b = round(float(value["b"]) * 255)
                if all(0 <= x <= 255 for x in (r, g, b)):
                    found.add(f"#{r:02X}{g:02X}{b:02X}")
            except (TypeError, ValueError):
                pass
        for item in value.values():
            found.update(extract_hex_colors(item))
    elif isinstance(value, list):
        for item in value:
            found.update(extract_hex_colors(item))
    return found


def check_unknown_colors(ctx: ValidationContext, node: dict[str, Any], path: str) -> None:
    for color in extract_hex_colors(node):
        if color not in ctx.allowed_colors:
            ctx.add("warning", "unknown_color", "Color is not present in tokens.json.", path, node_name(node), color)


def check_unknown_font_sizes(ctx: ValidationContext, node: dict[str, Any], path: str) -> None:
    for key in ("fontSize", "font_size", "font-size"):
        value = node.get(key)
        if isinstance(value, (int, float)) and float(value) not in ctx.allowed_font_sizes:
            ctx.add("warning", "unknown_font_size", "Font size is not present in typography tokens.", path, node_name(node), value)
    style = node.get("style")
    if isinstance(style, dict):
        value = style.get("fontSize")
        if isinstance(value, (int, float)) and float(value) not in ctx.allowed_font_sizes:
            ctx.add("warning", "unknown_font_size", "Font size is not present in typography tokens.", path, node_name(node), value)


def check_unnamed_frame(ctx: ValidationContext, node: dict[str, Any], path: str) -> None:
    name = node_name(node).strip()
    if node_type(node) in FRAME_TYPE_VALUES and (not name or GENERIC_LAYER_RE.match(name)):
        ctx.add("error", "unnamed_frame", "Frame appears unnamed or generically named.", path, name)


def check_layer_naming(ctx: ValidationContext, node: dict[str, Any], path: str) -> None:
    name = node_name(node).strip()
    if not name:
        ctx.add("warning", "layer_naming", "Layer has no name.", path)
        return
    if GENERIC_LAYER_RE.match(name):
        ctx.add("warning", "layer_naming", "Layer name looks generic and may violate naming-rules.md.", path, name)
    if " copy" in name.lower():
        ctx.add("warning", "layer_naming", "Layer name contains copy suffix.", path, name)


def check_handmade_components(ctx: ValidationContext, node: dict[str, Any], path: str) -> None:
    name = node_name(node)
    if not HANDMADE_COMPONENT_RE.search(name):
        return
    if is_component_instance(node):
        return
    ctx.add(
        "warning",
        "handmade_component",
        "Node name suggests Button/Input/Table/Card but it is not clearly a component or instance.",
        path,
        name,
    )


def check_spacing(ctx: ValidationContext, node: dict[str, Any], path: str) -> None:
    spacing_keys = (
        "itemSpacing",
        "gap",
        "paddingLeft",
        "paddingRight",
        "paddingTop",
        "paddingBottom",
        "counterAxisSpacing",
        "horizontalPadding",
        "verticalPadding",
    )
    for key in spacing_keys:
        value = node.get(key)
        if isinstance(value, (int, float)) and float(value) not in ctx.allowed_spacing:
            ctx.add("warning", "unknown_spacing", f"{key} is not in spacing token scale.", path, node_name(node), value)


def check_missing_states(ctx: ValidationContext, root: Any) -> None:
    all_names = " ".join(name for node, _ in iter_nodes(root) for name in [node_name(node)] if name)

    for component in ("Table", "Input", "Button"):
        component_present = re.search(component, all_names, re.IGNORECASE)
        if not component_present:
            continue
        for state, pattern in STATE_RE.items():
            if not pattern.search(all_names):
                ctx.add(
                    "info",
                    "missing_state",
                    f"{component} appears in the file, but no {state} state was found by name. TODO: confirm by inspecting component variants, because arbitrary Figma JSON may not expose states consistently.",
                    value={"component": component, "state": state},
                )

    # TODO: Directly validating component variant coverage requires a normalized
    # component-set export with variant properties. This script currently uses
    # layer-name heuristics only.


def validate(figma_json: Any) -> list[Finding]:
    tokens = load_json(TOKENS_PATH)
    components = load_json(COMPONENTS_PATH)
    allowed_colors, allowed_font_sizes, allowed_spacing = collect_token_values(tokens)
    component_names = collect_component_names(components)

    ctx = ValidationContext(
        allowed_colors=allowed_colors,
        allowed_font_sizes=allowed_font_sizes,
        allowed_spacing=allowed_spacing,
        component_names=component_names,
    )

    for node, path in iter_nodes(figma_json):
        check_unknown_colors(ctx, node, path)
        check_unknown_font_sizes(ctx, node, path)
        check_unnamed_frame(ctx, node, path)
        check_layer_naming(ctx, node, path)
        check_handmade_components(ctx, node, path)
        check_spacing(ctx, node, path)

    check_missing_states(ctx, figma_json)

    ctx.add(
        "info",
        "validator_scope",
        "TODO: confirm validations that need live Figma component metadata: published component binding, exact Auto Layout constraints, variant property completeness, and interaction prototype states.",
    )

    return ctx.findings


def print_text(findings: list[Finding]) -> None:
    if not findings:
        print("No findings.")
        return
    for finding in findings:
        parts = [f"[{finding.severity.upper()}]", finding.check, "-", finding.message]
        if finding.node_name:
            parts.append(f"name={finding.node_name!r}")
        if finding.path:
            parts.append(f"path={finding.path}")
        if finding.value is not None:
            parts.append(f"value={finding.value!r}")
        print(" ".join(parts))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate a Figma JSON export against the company design-system spec.")
    parser.add_argument("figma_json", type=Path, help="Path to a Figma JSON export or normalized node tree.")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format.")
    args = parser.parse_args(argv)

    if not args.figma_json.exists():
        print(f"Input file not found: {args.figma_json}", file=sys.stderr)
        return 2

    figma_json = load_json(args.figma_json)
    findings = validate(figma_json)

    if args.format == "json":
        print(json.dumps([finding.__dict__ for finding in findings], ensure_ascii=False, indent=2))
    else:
        print_text(findings)

    return 1 if any(f.severity == "error" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
