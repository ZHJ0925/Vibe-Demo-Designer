# Auto Layout Rules

Use these rules to keep generated Figma designs editable and consistent with the observed system.

## Must Use Auto Layout

Use Auto Layout for:

- Buttons
- Tags
- Form rows
- Form groups
- Alert content
- Message content
- Dialog header/content/footer
- Table toolbar
- Table rows and cells where practical
- Pagination
- Sidebar menu items
- Sidebar navigation column
- Top navigation bar
- Metric card content
- Drawer sections

## Direction

Horizontal Auto Layout:

- Button icon + text
- Tag icon + text + close icon
- Form label + control row
- Dialog footer actions
- Table toolbar
- Pagination controls
- Sidebar menu item icon + text
- Sidebar menu item content + collapse arrow
- Top navigation left region + right action/user region

Vertical Auto Layout:

- Form item stacks
- Dialog overall structure
- Drawer content
- Dashboard page content
- Detail page sections
- Alert with title + description
- Table region with table + pagination
- Sidebar navigation column
- Shell layout: topbar + main region when top navigation is present

## Gap Rules

Observed gaps:

- 4px: tag icon/text gap
- 8px: button icon/text gap, alert inner gap, message content gap
- 12px: sidebar navigation vertical item gap
- 13px: selected sidebar marker/text gap
- 16px: form label-control gap, common control group gap
- 24px: form item vertical gap, dialog content/footer spacing
- 32px: dialog basic padding

Use the observed scale before introducing new gaps.

## Padding Rules

Observed padding:

- Small button: `2px 8px`
- Medium button: `5px 16px`
- Large button: `8px 24px`
- Medium tag: `2px 8px`
- Large tag: `5px 12px`
- Alert: approximately `24px 16px`
- Message: approximately `16px 13px`
- Sidebar top-level menu item: `10px 14px`
- Sidebar selected sub-item: `10px 16px`
- Sidebar plain sub-item: `10px 39px`
- Basic dialog: 32px
- Separator dialog header/footer: approximately `24px 32px`

## Alignment

Rules:

- Button and Tag content should be center aligned.
- Form labels can be right, left, or top aligned depending on layout variant.
- Default enterprise form layout should use consistent label width.
- Dialog footer actions align to the right.
- Table cell content should align consistently by data type.

TODO: confirm numeric table alignment rules.

## Constraints and Resize

Rules:

- Buttons and tags should hug content unless block/full-width variant is used.
- Dialog normal width should stay between 480px and 960px.
- Table columns may be fixed, resizable, or flexible depending on variant.
- Sidebar uses 160px as a historical narrow reference only; generated desktop pages should prefer 200-256px and high-resolution pages should use 240px+ when useful.
- Sidebar navigation content column fills available sidebar width minus padding; 148px is a historical reference, not a hard lock.
- Selected sidebar sub-item uses 140px as an observed reference, not a hard lock.
- Sidebar labels must not be clipped by fixed constraints; use adaptive width, collapsed mode, or documented truncation with tooltip.
- Main content gap from the sidebar should be adaptive: 24px on desktop and up to 32px on high-resolution pages when space allows.
- Top navigation should use fill-width horizontal Auto Layout with left context, flexible spacer, and right action/user cluster.
- Main content should resize with the viewport while preserving left alignment.
- Form controls should use stable widths within a form section.

TODO: confirm exact responsive breakpoints.

## Component Properties

Use Figma component properties for:

- Button: type, state, size, loading, icon visibility, block, disabled
- Input: size, state, clearable, password, borderless, disabled
- Search: icon position, clearable, popup, history, disabled
- Tag: type, theme, size, state, icon, closable, selected
- Alert: type, icon, closable, action, description, collapsible
- Message: type, closable
- Dialog: type, icon, close button, separator, fullscreen
- Table: density, border, zebra, selection, sortable, filterable, loading, empty
- SidebarNavigation: level, selected, expanded, collapsed, icon, arrow, active marker

TODO: confirm exact published component property names from Figma component sets.
