---
name: company-figma-design-system
description: Use this skill whenever the user asks Codex to create, modify, regenerate, review, audit, or align Figma designs for the company's web product UI. It enforces the observed AiOMP / IS RB design system tokens, component rules, page patterns, naming conventions, interaction states, and Auto Layout rules from the bundled references and assets. Trigger this skill for Figma design generation, Figma design edits, design-system compliance reviews, UI consistency checks, component/page reconstruction, or any request that mentions matching the company's existing Figma style, tokens, components, layouts, or interaction patterns.
---

# Company Figma Design System

This skill applies the company web design system extracted from the observed Figma files:

- IS RB UI改版 Copy
- AiOMP Design for web组件
- 看板工作台 UI改版 Copy

Use it to keep new or modified Figma designs aligned with the existing system. The skill is based on structured tokens, component rules, layout rules, interaction rules, naming rules, and Auto Layout rules. It should not depend on screenshots as the source of truth.

## 使用场景

Use this skill when the user asks to:

- Create a new Figma design, page, component, module, dialog, drawer, dashboard, table page, form, detail page, or settings page.
- Modify an existing Figma design while preserving the company design system.
- Review or audit a Figma file for design-system compliance.
- Convert a design idea into a Figma screen that should match the existing AiOMP / IS RB UI style.
- Check whether tokens, components, spacing, naming, states, or Auto Layout match the company system.
- Produce implementation guidance based on the company Figma design system.

Do not use this skill for unrelated brands or visual systems unless the user explicitly asks to apply this company design language.

## 必须读取的 References 和 Assets

Before creating, modifying, or reviewing a Figma design, read the relevant bundled resources.

Always read:

- `assets/tokens.json`
- `assets/components.json`
- `assets/page-patterns.json`
- `assets/icons.json`
- `references/design-system-overview.md`
- `references/figma-generation-checklist.md`

For creation or modification, also read as needed:

- `references/layout-rules.md`
- `references/component-rules.md`
- `references/interaction-rules.md`
- `references/auto-layout-rules.md`
- `references/naming-rules.md`

For reviews, read all reference files unless the review scope is explicitly narrow.

If a needed rule is missing or marked `TODO: confirm`, report the gap. Do not invent a new rule silently.

## 工作流程

1. Identify the task type:
   - Generation
   - Modification
   - Review/audit
   - Gap analysis

2. Load the required resources:
   - Start with `tokens.json`, `components.json`, and `page-patterns.json`.
   - Load Markdown references that match the task area.

3. Determine the relevant pattern:
   - Dashboard
   - List
   - Detail
   - Form
   - Settings
   - Modal/Dialog
   - Drawer
   - Sidebar navigation
   - Table module
   - Component library item

4. Apply the system constraints:
   - Tokens
   - Component variants and states
   - Layout structure
   - Interaction states
   - Naming rules
   - Auto Layout rules

5. Report gaps:
   - If a token, component, state, or layout rule is missing, mark it as a gap.
   - Use `TODO: confirm` for unresolved design decisions.
   - Ask for confirmation only when the missing rule materially affects the requested output.

6. Verify output:
   - Run through the QA checklist below.
   - For Figma edits, prefer reusable variables, styles, and component-like structure over hardcoded one-off visuals when possible.

## 生成 Figma 文件时的规则

When generating a Figma design:

- Use `#222222` as the primary brand color.
- Use blue colors such as `#0052D9`, `#295FD8`, and `#3370FF` only for links, info states, and auxiliary emphasis unless the user confirms otherwise.
- Use `PingFang SC` typography.
- Use observed type levels:
  - 16px / 24px semibold for compact titles and dialog titles.
  - 14px / 22px for controls, forms, and normal body content.
  - 12px / 20px for dense labels, table metadata, and tags.
- Use observed radius values:
  - 3px for Tag.
  - 4px for Button and Input.
  - 6px for Alert and Message.
  - 9px for Dialog.
  - 16px for pill controls.
- Use the observed spacing scale from `tokens.json`.
- Use 40px as the default table header height and table row height.
- Use 160px sidebar width only as a historical narrow reference for workbench/dashboard layouts, not as the generated default.
- For generated desktop workbench pages, prefer adaptive sidebar width with 192px minimum and 200-256px normal range. On high-resolution layouts, use 240px or more when it improves menu readability and page hierarchy.
- Use the observed SidebarNavigation style for vertical workbench menus: 12px labels, 16px icons, compact padding, white selected sub-item surface, and 4px red selected marker. Widths such as 160px, 148px, and 140px are reference values and must adapt to labels and viewport.
- Use at least 24px content/sidebar gap on desktop workbench layouts; high-resolution layouts may use 32px when the page still reads as connected.
- Left sidebar navigation must be visually separated from the right content. Prefer a white navigation surface plus `sidebar_elevated` shadow; a clear divider or sufficient spacing is acceptable when shadow is not possible.
- Use TopNavigation when a page includes global actions, user identity, page title controls, or a horizontal menu. Separate the topbar from content with `topbar_subtle` shadow or a divider.
- Use confirmed icon library rules from `assets/icons.json`. If an icon is missing or unconfirmed, report `TODO: confirm icon` instead of inventing one.
- Use Dialog for temporary focused decisions.
- Use Drawer for contextual side workflows.
- Use Message for lightweight global feedback.
- Use Alert for inline persistent notices.
- Use Table patterns from `components.json` and `page-patterns.json` for data-heavy screens.
- Use Auto Layout for buttons, tags, form rows, dialog sections, alert/message content, table toolbars, pagination, sidebar navigation/menu items, dashboard cards, and drawer sections.
- Name pages, frames, sections, components, variants, and layers according to `references/naming-rules.md`.

If the requested design requires a component or pattern not present in the references, create only the minimum necessary structure and clearly report the missing design-system gap.

## 审查 Figma 文件时的规则

When reviewing a Figma design:

- Compare the design against `tokens.json`, `components.json`, and `page-patterns.json`.
- Check whether the primary brand color is correctly applied as `#222222`.
- Check whether blue is limited to links, info states, or auxiliary emphasis.
- Check table row/header height against the 40px default.
- Check that sidebar width is adaptive and labels are not clipped by hard-coded reference widths.
- Check that generated desktop sidebars are not unnecessarily narrow; 160px should be treated as compact/historical, not default.
- Check that the sidebar has clear visual hierarchy against the right content, using surface, shadow, divider, or spacing.
- Check that top navigation exists and is clearly separated when the page has global actions or user identity.
- Check that icons come from the confirmed icon rules or are reported as gaps.
- Check typography against the observed PingFang SC levels.
- Check radii against the observed radius scale.
- Check spacing against the observed spacing scale.
- Check component variants, states, and sizes against `components.json`.
- Check page structure against `page-patterns.json`.
- Check naming against `references/naming-rules.md`.
- Check Auto Layout usage against `references/auto-layout-rules.md`.
- Check interaction states against `references/interaction-rules.md`.
- Separate confirmed violations from gaps that require human confirmation.

Do not treat undocumented preferences as violations. If the system lacks a rule, report a gap.

## 禁止事项

- Do not invent new tokens when a rule is missing.
- Do not silently substitute another brand color for `#222222`.
- Do not use blue as the default primary action color without explicit confirmation.
- Do not rely on screenshots as the main source of design-system truth.
- Do not create ornamental marketing-style layouts for operational product screens.
- Do not use arbitrary table row heights outside the observed density scale.
- Do not ignore missing hover, active, disabled, loading, empty, or error states.
- Do not create one-off component structures when an observed component rule exists.
- Do not invent icons, draw arbitrary SVG icons, or mix icon styles when the icon library does not provide a confirmed match.
- Do not hard-code sidebar/navigation widths when adaptive sizing is required.
- Do not leave left navigation and right page content at the same visual layer when the layout needs a shell/sidebar hierarchy.
- Do not modify Figma files during a review-only request.
- Do not generate implementation code unless the user explicitly asks for code.

## 输出格式

For generation or modification tasks, respond with:

- What was created or changed.
- Which tokens, components, and page patterns were used.
- Any `TODO: confirm` gaps.
- QA checklist result.

For review tasks, respond with:

- Findings first, ordered by severity.
- File/node references when available.
- Confirmed violations.
- Gaps or ambiguous rules marked with `TODO: confirm`.
- Short recommended fixes.
- QA checklist result.

For gap-analysis tasks, respond with:

- Missing tokens.
- Missing components.
- Missing states.
- Missing page patterns.
- Conflicting rules.
- Recommended Figma pages or component docs to inspect next.

## QA Checklist

Before finishing, verify:

- Primary brand color is `#222222`.
- Blue is used only for links, info states, or auxiliary emphasis unless confirmed otherwise.
- Typography uses PingFang SC and observed size/line-height levels.
- Table default header and row height is 40px.
- Spacing follows the observed scale in `tokens.json`.
- Radius follows the observed radius scale.
- Shadows use observed `Shadow-3` for upper-layer floating surfaces and `sidebar_elevated`/`topbar_subtle` for app shell hierarchy.
- Buttons, Inputs, Forms, Alerts, Messages, Dialogs, Tables, Tags, SidebarNavigation, TopNavigation, and Drawers follow `components.json`.
- Dashboard, List, Detail, Form, Settings, Modal, Drawer, TopNavigation, SidebarNavigation, and Table module patterns follow `page-patterns.json`.
- Hover, active, focus, disabled, loading, empty, error, warning, and success states are included where relevant.
- Auto Layout is used for required structures.
- Names follow the naming rules.
- All unresolved or missing rules are reported as `TODO: confirm`.
