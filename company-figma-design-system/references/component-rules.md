# Component Rules

Only use rules observed from the Figma component pages and business screens. Mark uncertain behavior with `TODO: confirm`.

## Button

Purpose:

- Trigger primary, secondary, text, icon-only, block, and loading actions.

Variants:

- Primary dark
- Default fill
- Outline
- Dashed
- Text
- Icon-only
- Block
- Loading
- Error theme

States:

- Default
- Hover
- Active
- Disabled
- Loading

Sizes:

- Small: 12px / 20px text, padding `2px 8px`
- Medium: 14px / 22px text, padding `5px 16px`
- Large: 16px / 24px text, padding `8px 24px`
- Icon button: commonly 32px square/circle

Rules:

- Primary action color is `#222222`.
- Button radius is commonly 4px.
- Pill button radius is 16px.
- Icon/text gap is 8px.
- Loading icon size is 16px.
- Use disabled text `#BDBDBD`.

Anti-patterns:

- Do not use blue as the default primary button unless the action is specifically info/link oriented.
- Do not mix too many primary buttons in the same action group.

## Input

Purpose:

- Text input, password input, textarea, grouped input, addon input, searchable input.

Variants:

- Basic input
- Textarea
- Addon
- Group
- Clearable
- Password
- Borderless

States:

- Default
- Hover
- Focus
- Disabled
- Success
- Warning
- Error

Sizes:

- Large: 40px
- Medium: 32px
- Small: 24px

Rules:

- Default border: `#DCDCDC`.
- Hover/focus border: `#222222`.
- Focus shadow: `#EEEEEE`.
- Disabled background: `#F5F7F9`.
- Placeholder and disabled text use muted neutral colors.

Anti-patterns:

- Do not remove validation state color when the field is invalid.
- Do not use borderless inputs in dense forms unless the surrounding container provides clear structure.

## Search

Purpose:

- Search input with optional clear, batch behavior, autocomplete, and history.

Variants:

- Basic search
- Borderless search
- Clearable search
- Batch search
- Autocomplete
- Custom popup
- History
- Search icon left
- Search icon right

States:

- Default
- Hover
- Focus
- Disabled
- Popup open

Rules:

- Follow Input sizing and border behavior.
- Use upper-layer shadow for popup/autocomplete surfaces.
- Search icon may appear on either side depending on variant.

Anti-patterns:

- Do not show popup content without clear connection to the search input.

## Form

Purpose:

- Structured data entry and validation.

Variants:

- Right-aligned label
- Left-aligned label
- Top-aligned label
- Vertical layout
- Inline layout

Properties:

- Label width
- Required marker
- Help tooltip
- Validation message
- Control width

Rules:

- Default label width: 80px.
- Label-control gap: 16px.
- Form item vertical gap: 24px.
- Required marker color: `#FF1432`.
- Controls include Input, Select, RadioButtonGroup, Checkbox, Switch, Textarea, Tooltip, and Button.

Anti-patterns:

- Do not use inconsistent label widths inside the same form section.
- Do not separate validation messages far from their related control.

## Alert

Purpose:

- Inline warning or notice block for information that needs user attention.

Variants:

- Basic
- With icon
- Closable
- Custom close action
- Related action link
- With description
- Collapsible

States:

- Info
- Success
- Warning
- Error

Rules:

- Radius: 6px.
- Icon size: 20px.
- Close icon: 16px.
- Main gap: 8px.
- Info uses `#F2F3FF` background and `#0052D9` action/link color.
- Success uses `#E8FFEF` background and `#3BD183`.
- Warning uses `#FFF4E8` background and `#FE8744`.
- Error uses `#FFE9E8` background and `#FF1432`.

Anti-patterns:

- Do not use Alert as a floating notification; use Message for global feedback.

## Message

Purpose:

- Lightweight global feedback after user operation.

Variants:

- Info
- Question/help
- Success
- Warning
- Error
- Loading
- Closable

Rules:

- Size adapts to content.
- Background: `#FFFFFF`.
- Border: 0.5px `#DCDCDC`.
- Radius: 6px.
- Padding: approximately `16px 13px`.
- Icon size: 20px.
- Content gap: 8px.
- Use `Shadow-3` upper-layer shadow.

Anti-patterns:

- Do not use Message for persistent content or complex actions.

## Dialog

Purpose:

- Temporary focused window requiring user response without replacing the full task flow.

Variants:

- Basic
- With separator lines
- With icon
- Without close button
- Fullscreen
- Info
- Warning
- Error
- Success

States:

- Open
- Close button normal
- Close button hover
- Close button active

Rules:

- Default width: 480px.
- Custom normal width range: 480px to 960px.
- Radius: 9px.
- Basic padding: 32px.
- Title: 16px / 24px semibold.
- Content: 14px / 22px.
- Footer is right aligned.
- Footer button gap: 8px.
- Separator line: `#E7E7E7`.

Anti-patterns:

- Do not use Dialog for large side workflows that should remain contextual; use Drawer.

## Table

Purpose:

- Display structured same-type data for organization, comparison, search, filter, sort, and analysis.

Variants:

- Basic
- Border table
- Zebra table
- Fixed header
- Fixed column
- Fixed footer
- Fixed header and footer
- Expandable rows
- Merged rows/columns
- Adjustable column width
- Multi-level header
- Row drag sort
- Column drag sort
- Custom column settings
- Single select
- Multi select
- Sortable
- Filterable
- Loading

States:

- Default
- Row hover
- Selected
- Sorted ascending
- Sorted descending
- Filter active
- Loading
- Empty or zero-value display

Sizes:

- Default header height: 40px.
- Default row height: 40px.
- Density variants observed: 36px, 46px, 54px.
- Pagination area: approximately 64px.

Rules:

- Default production table height is 40px for header and rows.
- Use Tooltip for truncated cell content.
- Use filter dropdowns for column filters.
- Keep pagination connected to the table.
- Show total count in pagination, such as “共 101 项数据”.

Anti-patterns:

- Do not use arbitrary row heights outside the observed density scale.
- Do not hide active filters without a visible clear or condition display.

## Tag

Purpose:

- Mark, classify, select, or show lightweight business status.

Variants:

- Basic
- Icon tag
- Deletable tag
- Addable tag
- Selectable CheckTag
- Dark
- Light
- Outline
- Light-outline

States:

- Normal
- Hover
- Active
- Disabled
- Selected
- Deletable disabled

Sizes:

- Small: 12px / 20px text, horizontal padding 4px.
- Medium: 12px / 20px text, padding `2px 8px`.
- Large: 14px / 22px text, padding `5px 12px`.

Rules:

- Radius: 3px.
- Icon size: 14px.
- Icon/text gap: 4px.
- Text/close gap: 8px.
- Default background: `#F3F3F4`.
- Disabled background: `#F5F7F9`.
- Disabled border: `#DCDCDC`.
- Disabled text: `#BDBDBD`.
- Selected CheckTag uses `#222222`.
- Success uses `#3BD183` and `#E8FFEF`.
- Warning uses `#FE8744` and `#FFF4E8`.
- Danger uses `#FF1432` and `#FFE9E8`.

Anti-patterns:

- Do not use tags as primary action buttons.
- Do not create new semantic colors when existing tag themes cover the status.

## Sidebar Navigation

Purpose:

- Provide persistent left-side navigation for dashboard/workbench pages.

Observed structure:

- Outer page background: `#F5F7F9`.
- Navigation content column reference width: 148px.
- Top offset in observed frame: 72px.
- Menu group vertical gap: 12px.
- 一级菜单 item: icon + label + optional collapse arrow.
- 二级菜单 item: text-only or selected item with active marker.

Variants:

- 一级菜单 with icon and collapse arrow
- 一级菜单 with icon only
- 二级菜单 default
- 二级菜单 selected
- Expanded group
- Collapsed group

States:

- Default
- Selected
- Expanded
- Collapsed
- TODO: confirm hover and disabled states from component source.

Sizes:

- Sidebar area historical reference width: 160px; do not use this as the generated default on broad desktop pages.
- Sidebar generated minimum: 192px.
- Sidebar generated preferred desktop range: 200-256px.
- Sidebar high-resolution recommended width: 240px or more when labels and hierarchy benefit.
- Sidebar collapsed width: 64px; TODO: confirm exact collapsed variant.
- Navigation content reference width: 148px.
- Selected sub-item reference width: 140px.
- 一级菜单 padding: `10px 16px` by default; `10px 14px` is compact mode only.
- 一级菜单 icon size: 16px; one observed icon uses 17px.
- Collapse arrow wrapper: 10px; arrow glyph: 4px by 8px.
- 一级菜单 icon/text gap: 8px.
- 一级菜单 text width should fill remaining space; 62px is a historical narrow reference only.
- 一级菜单 arrow gap: 24px.
- 二级菜单 selected padding: `10px 16px`.
- 二级菜单 selected marker: 4px dot, radius 3px.
- Selected marker/text gap: 13px.
- Plain 二级菜单 padding: approximately `10px 40px`; `10px 39px` is compact historical reference.
- Item radius: 4px.

Rules:

- Use `#FFFFFF` as the sidebar navigation surface when the page background is `#F5F7F9` or when the content area uses light cards.
- Add sidebar elevation using `sidebar_elevated` shadow, a clear divider, or enough spacing so the navigation and right content hierarchy do not merge.
- Use 12px label text.
- Use `PingFang SC` regular or light depending on hierarchy; selected item uses regular.
- Keep the observed compact rhythm, but do not hard-code widths if labels need more room.
- For new generated workbench pages, prefer a 200-256px sidebar range instead of the historical 160px reference.
- On high-resolution canvases, increase sidebar width and content gap before adding decorative whitespace inside cards.
- The menu must support adaptive width, collapsed mode, or documented truncation with tooltip for long labels.
- Use `#000000` for navigation text in observed frame.
- Use `#383838` for neutral icon color when icons are drawn as vectors.
- Use `#FFFFFF` for selected item background.
- Use `#FF1432` for selected sub-item marker.
- Keep menu items compact and vertically stacked.
- Use Auto Layout for every menu item and the menu column.

Anti-patterns:

- Do not leave the sidebar as flat gray-on-gray when the content area is also gray.
- Do not default to a 160px sidebar on high-resolution pages.
- Do not force every future sidebar to 160px or every navigation column to 148px.
- Do not keep only a 20px content/sidebar gap on wide pages if the layout feels cramped.
- Do not clip Chinese labels to preserve the observed 62px label area.
- Do not use the primary brand fill `#222222` as the selected navigation background for this sidebar style.
- Do not replace the 4px red selected marker with a full-height bar unless a future Figma source confirms that variant.
- Do not use oversized icons or 14px body labels in this sidebar navigation style.

## Top Navigation

Purpose:

- Provide page identity, horizontal menu when needed, global actions, and user account access.

Observed/requested structure:

- Left region: page title, logo, breadcrumb, or horizontal menu.
- Right region: primary action, secondary actions, user name, avatar.
- Surface should be visually distinct from the page background.

Variants:

- Page title with right-side actions
- Horizontal menu
- User account area
- TODO: confirm exact IS RB and Element Plus top menu variants from Figma MCP.

States:

- Default
- Active menu item
- Hover
- Disabled
- TODO: confirm exact top-menu state styling.

Sizes:

- Topbar height reference: 64px.
- Horizontal padding reference: `24px 32px`.
- Action gap reference: 16px.
- Title text: 16px / 24px semibold.

Rules:

- Use a white or clearly separated topbar surface.
- Use a subtle bottom divider or `topbar_subtle` shadow to separate it from content.
- Keep global actions and user identity right-aligned.
- Use `#222222` for the primary action button in the topbar.
- Top navigation dimensions are reference values and may adapt to page density.

Anti-patterns:

- Do not let a workbench page with global actions start directly on a gray background without a topbar.
- Do not mix horizontal top menu, page tabs, and table tabs at the same visual level.
- Do not make the topbar heavier than the main content surfaces.

## Icon

Purpose:

- Provide consistent symbolic navigation, action, state, and component affordances without ad-hoc AI-generated shapes.

Observed icon usage:

- Sidebar navigation icons are 16px by default.
- One sidebar icon was observed at 17px; treat this as an exception, not the default.
- Sidebar collapse arrow uses a 10px wrapper and an approximately 4px by 8px arrow glyph.
- Alert and Message status icons use 20px.
- Dialog status icons use 24px.
- Tag icons use 14px.

Rules:

- Use icons from the confirmed Figma component/icon library whenever possible.
- Keep icon sizes aligned to `assets/tokens.json`.
- Use neutral icon color `#383838` in sidebar/navigation contexts unless a semantic state requires another observed token.
- Do not invent new icon metaphors, custom decorative icons, or arbitrary SVG paths when a matching library icon is unavailable.
- If the requested icon is not present in the confirmed icon library, report `TODO: confirm icon` and ask for the icon source or mapping.
- Icons must be named semantically, such as `Icon/Order`, `Icon/Workbench`, `Icon/CollapseArrow`, or by the published component-library name when known.

Anti-patterns:

- Do not create random AI-styled icons to fill gaps.
- Do not mix icon visual styles in the same navigation or toolbar.
- Do not resize icons outside observed sizes unless a specific component rule requires it.
