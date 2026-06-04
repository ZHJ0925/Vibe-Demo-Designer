# Layout Rules

These rules are extracted from observed business pages, dashboard pages, detail pages, drawers, forms, and tables.

## Shell Layout

Observed dashboard/workbench layout and updated generation rule:

- Left sidebar historical observed reference width: 160px.
- Generated desktop workbench sidebar should usually be wider than the historical 160px reference.
- Recommended generated sidebar width: adaptive, with 192px minimum and 200-256px preferred desktop range.
- High-resolution pages should use 240px or more when labels, hierarchy, and spacing benefit.
- Main content begins after a horizontal gap from the sidebar; observed reference gap is 20px.
- Generated desktop content/sidebar gap should usually be at least 24px; high-resolution pages may use 32px.
- Example content x-position: 180px when sidebar starts at 0.
- Page background uses `#F5F7F9` or `#F2F5FA`.
- Main surfaces are white or near-white cards/panels.
- Sidebar and topbar should read as separate surfaces from the page background.

Rules:

- Use a persistent left navigation for workbench-style pages, but do not hard-code the sidebar width when content or viewport requires adaptive sizing.
- Use the observed sidebar navigation component for workbench pages when a vertical menu is required.
- Treat 160px as a historical narrow reference, not the default for new generated workbench pages.
- The sidebar should support adaptive width, collapsed mode, and content-safe label rendering.
- The sidebar width should be content-aware: calculate from label length, icon width, arrow width, marker width, and horizontal padding.
- The sidebar must have enough visual separation from the right content: preferred treatment is white surface plus subtle right-side shadow; a divider or clear spacing is acceptable when shadow is not available.
- Top navigation should provide a separate horizontal surface for page title, global actions, and user identity when those elements exist.
- Keep content aligned to a consistent left edge.
- Avoid centered marketing-style layouts for operational pages.
- Use compact page headers and dense content regions.

## Sidebar Navigation Pattern

Observed structure from 看板工作台 navigation:

- Navigation content column historical reference width: 148px inside the 160px sidebar area.
- Navigation content is vertically stacked with 12px gap.
- Top offset in the observed frame: 72px.
- 一级菜单 items use icon + 12px label + optional collapse arrow.
- 二级菜单 default items are text-only and centered by horizontal padding.
- Selected 二级菜单 uses a 140px white rounded rectangle with a 4px red dot marker.

Rules:

- Sidebar page area uses `#F5F7F9`.
- Sidebar navigation surface should use `#FFFFFF` when the main page background is gray.
- Use `sidebar_elevated` shadow or a clear divider on the sidebar edge to distinguish the navigation from the content region.
- Sidebar width must be responsive to product needs. Use 160px/148px only as historical narrow references.
- For generated desktop pages, prefer `clamp(200px, 14vw, 256px)` or an equivalent adaptive rule.
- On high-resolution pages, widen the sidebar to 240px or more when it improves menu readability and page hierarchy.
- Use at least 24px gap between sidebar and content on normal desktop pages; use 32px on high-resolution pages when space allows.
- Do not clip or force-wrap Chinese menu labels just to preserve the observed reference width.
- If labels are longer than the observed 62px text area, allow the navigation content to widen, use a supported collapsed mode, or use a documented truncation pattern with tooltip.
- Selected navigation item background uses `#FFFFFF`.
- Selected sub-item marker uses `#FF1432`.
- Item radius is 4px.
- 一级菜单 item padding is `10px 16px` by default; `10px 14px` is compact mode only.
- Selected 二级菜单 padding is `10px 16px`.
- Plain 二级菜单 padding is approximately `10px 40px`; `10px 39px` is compact historical reference.
- Use 12px labels by default.
- Use 16px icons for navigation items.
- Use 10px arrow wrapper and 4px by 8px arrow glyph for collapsible groups.

TODO: confirm hover state, collapsed sidebar width, exact responsive min/max sidebar range, and whether selected top-level items use the same white background treatment.
TODO: confirm Element Plus menu references from nodes `9178:169254` and `9181:170196` when Figma MCP is available.

## Top Navigation Pattern

Observed/requested structure:

- Left side: page title, logo, breadcrumb, or horizontal menu.
- Right side: primary action, secondary actions, user name, avatar.
- Topbar sits above the main content and reinforces page hierarchy.

Rules:

- Use a white or clearly separated topbar surface.
- Use a subtle bottom divider or `topbar_subtle` shadow.
- Keep the page title or active menu on the left.
- Keep global actions and user identity on the right.
- Use the primary brand button `#222222` for the main topbar action.
- Use adaptive horizontal padding; `24px 32px` is a reference, not a hard lock.

TODO: confirm exact top menu state, height, and spacing from IS RB node `932:27490` and Element Plus node `9304:177289`.

## Dashboard Pattern

Observed structure:

- Sidebar navigation
- Top metric cards or indicator blocks
- Business section title
- Filter tabs or status chips
- Data table
- Pagination area

Rules:

- Place high-level metrics above the main table.
- Use compact metric labels around 12px.
- Use larger numbers for primary metric values; observed dashboard metrics use approximately 34px.
- Keep table and pagination visually connected.
- Pagination sits at the bottom of the table region.

## List Pattern

Observed structure:

- Optional page title or business module title
- Search/filter row
- Table toolbar or tabs
- Table
- Pagination

Rules:

- Table header height defaults to 40px.
- Table row height defaults to 40px.
- Use row hover state for scanability.
- Use single-line truncation for long table values by default.
- Use Tooltip for truncated content.
- Use filter dropdowns for column filtering.
- Use selected/filter condition display when active filters exist.

## Detail Pattern

Observed structure:

- Business title/header
- Sectioned description blocks
- Status tags
- Related business panels
- Optional timeline/steps
- Optional action area

Rules:

- Use section titles at 14px or 16px depending on hierarchy.
- Use description/list rows with compact vertical rhythm.
- Use tags for business status and classification.
- Keep related information grouped into bordered or white panels.
- TODO: confirm the final detail-page section spacing scale.

## Form Pattern

Observed structure:

- Label + control rows
- Optional required marker
- Help tooltip beside label
- Validation message near control
- Action buttons at form bottom

Rules:

- Default label width: 80px.
- Default label-control gap: 16px.
- Default form item vertical gap: 24px.
- Required marker uses `#FF1432`.
- Support right-aligned labels, left-aligned labels, top-aligned labels, vertical layout, and inline layout.
- Inline form demos show large horizontal item gaps around 120px.
- TODO: confirm whether 120px inline gap is a demo-only value or production rule.

## Settings Pattern

No complete settings page was directly observed.

Use inferred enterprise pattern only when needed:

- Left or top category navigation
- Form-like grouped settings content
- Save/cancel footer for editable settings

TODO: confirm with a real Settings page.

## Modal Pattern

Observed Dialog structure:

- Overlay/mask
- Dialog surface
- Header
- Content
- Footer

Rules:

- Default dialog width: 480px.
- Custom normal dialog width range: min 480px, max 960px.
- Dialog padding: 32px in basic dialog examples.
- Dialog radius: 9px.
- Footer buttons are right aligned.
- Footer button gap: 8px.
- Separator dialog uses header/footer padding around `24px 32px`.
- Separator lines use `#E7E7E7`.

## Drawer Pattern

Observed in business task/form flow.

Rules:

- Use Drawer for side workflows that keep the user in context.
- Drawer content can contain form fields, descriptions, alerts, and task recommendation content.
- Use sectioned content with clear title hierarchy.
- TODO: confirm drawer width, header height, footer behavior, and mask color from a dedicated Drawer component page.

## Spacing Rules

Observed scale:

- 2px: small button vertical padding
- 4px: tag icon/text gap, small tag horizontal padding
- 8px: button icon/text gap, common inner gap
- 12px: large tag horizontal padding, filter/dropdown inner padding
- 13px: selected sidebar marker/text gap
- 14px: sidebar top-level horizontal padding
- 16px: label-control gap, medium button horizontal padding, alert side padding
- 24px: large button horizontal padding, form row vertical spacing, dialog footer/content spacing
- 39px: plain sidebar sub-item horizontal padding
- 32px: basic dialog padding
- 40px: table default row/header height
- 64px: table pagination area height

Use this observed scale before inventing new spacing values.

Responsive note:

- Values such as sidebar 160px, navigation content 148px, selected item 140px, and label width 62px are observed reference values. They must not override readability or responsive layout requirements.
- For new generated pages, do not default to the narrow 160px sidebar on broad desktop or high-resolution canvases.
