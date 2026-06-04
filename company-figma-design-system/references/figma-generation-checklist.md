# Figma Generation Checklist

Use this checklist before delivering generated or reviewed Figma screens for this design system.

## Token Check

- Primary brand color is `#222222`.
- Blue is used for info, links, or auxiliary emphasis, not default primary actions.
- Text uses observed neutral scale: `#1A1A1A`, `#494C4F`, `#999999`, `#BDBDBD`.
- Borders use observed neutral border colors, especially `#DCDCDC` and `#E7E7E7`.
- Semantic colors match observed info/success/warning/error tokens.
- Radius uses observed scale: 3, 4, 6, 9, 12, 16.
- Shadow uses observed `Shadow-3` for upper-layer floating surfaces.

## Typography Check

- Product UI uses PingFang SC.
- Dialog/compact title uses 16px / 24px semibold.
- Normal controls and body use 14px / 22px.
- Dense labels and table metadata use 12px / 20px.
- Letter spacing is 0.

## Layout Check

- Workbench sidebar does not default to the historical 160px width on broad desktop pages.
- Sidebar generated width follows adaptive guidance: 192px minimum, 200-256px preferred desktop range, 240px+ when high-resolution pages need better hierarchy.
- Sidebar navigation content fills available width; 148px is only a historical reference.
- Sidebar selected sub-item uses a white rounded surface and 4px red marker; its 140px width is an observed reference, not a hard lock.
- Long sidebar labels are not clipped; use adaptive width, collapsed mode, or documented truncation with tooltip.
- Content/sidebar gap is at least 24px on desktop and may grow to 32px on high-resolution pages.
- Sidebar is visually separated from the right content using a white navigation surface plus `sidebar_elevated` shadow, divider, or sufficient spacing.
- Top navigation is used when the page has global actions, user identity, or horizontal menu.
- Top navigation is separated from content by `topbar_subtle` shadow or a divider.
- Main content aligns consistently after sidebar.
- Dashboard pages put metrics above the table.
- List pages include search/filter, table, and pagination.
- Detail pages use sectioned information blocks.
- Forms use consistent label width and spacing.
- Table default header and row height is 40px.

## Component Check

- Buttons use observed sizes and states.
- Inputs use observed 40/32/24 height scale.
- Forms use 80px label width where applicable.
- Alerts use semantic backgrounds and optional icon/close/action.
- Messages use white floating surface, border, radius, and shadow.
- Dialog footer actions are right aligned with 8px gap.
- Tables include hover, loading, filtering, sorting, empty, and pagination states when relevant.
- Tags use observed size/theme/state rules.
- SidebarNavigation uses 12px labels, 16px icons, compact padding, and the observed selected sub-item treatment.
- TopNavigation uses clear left context and right action/user clusters.
- Icons come from the confirmed icon library or are reported as `TODO: confirm icon`.

## Interaction Check

- Interactive controls have hover and disabled states.
- Form controls have focus and validation states.
- Loading states do not collapse layout.
- Empty values are intentionally displayed.
- Truncated table content has Tooltip behavior.
- Active filters can be cleared.

## Auto Layout Check

- Buttons, tags, forms, alerts, messages, dialogs, table toolbars, pagination, sidebar navigation, and sidebar items use Auto Layout.
- Content hugging is used for buttons/tags unless block variant is intended.
- Dialog width stays in the observed range.
- Sidebar remains fixed width in workbench layouts.

## Open TODOs

- TODO: confirm exact Drawer component width and footer rules.
- TODO: confirm whether Message fully replaces Toast.
- TODO: confirm production Settings page pattern.
- TODO: confirm exact component property names in published Figma component sets.
- TODO: confirm responsive breakpoints.
