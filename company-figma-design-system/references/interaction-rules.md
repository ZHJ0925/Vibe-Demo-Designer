# Interaction Rules

These rules cover observed states and behavior in component documentation and business pages.

## State Model

Observed common states:

- Default
- Hover
- Active
- Focus
- Disabled
- Loading
- Selected
- Error
- Warning
- Success
- Empty

Rules:

- Every interactive control should define hover and disabled behavior.
- Form controls should define focus behavior.
- Data components should define loading and empty/zero-value behavior.

## Hover

Observed rules:

- Input hover/focus border uses `#222222`.
- Table rows support hover.
- Close button hover uses a light background such as `#F5F7F9`.
- Tag hover exists for normal and selectable tags.

## Active

Observed rules:

- Button active state exists for button variants.
- Close button active background uses a stronger neutral such as `#DCDCDC`.
- Selectable Tag active/selected state uses `#222222`.

## Disabled

Observed rules:

- Disabled text uses `#BDBDBD`.
- Disabled background commonly uses `#F5F7F9`.
- Disabled border commonly uses `#DCDCDC`.
- Disabled controls should remain visible but clearly non-interactive.

## Loading

Observed rules:

- Button has loading state with 16px loading icon.
- Message has loading type.
- Table loading keeps the table shell/header and displays centered loading text such as “正在加载中，请稍等”.
- Loading can include a top loading indicator in table examples.

## Empty and Zero Values

Observed table docs include:

- Data presentation for zero/empty values.
- Empty or unavailable values should be intentionally displayed, not left ambiguous.

TODO: confirm exact placeholder text or symbol for empty table cells.

## Error and Validation

Observed rules:

- Required marker uses `#FF1432`.
- Error semantic color uses `#FF1432` or `#F54A45`.
- Error background uses `#FFE9E8` or `#FFE7EA`.
- Input has error state.
- Form has validation-related structure.

Rules:

- Keep validation messages near the related field.
- Use semantic color consistently across input state, message, and inline feedback.

TODO: confirm exact validation message typography and placement.

## Dialog

Observed rules:

- Dialog requires user response.
- Footer actions are right aligned.
- Close button can be omitted in specific variants.
- Dialog supports info, warning, error, and success icon themes.
- Fullscreen dialog exists for larger tasks.

## Drawer

Observed in task recommendation/form workflow.

Rules:

- Use Drawer for contextual side workflows.
- Keep form and business content visible within a structured side panel.

TODO: confirm drawer overlay, width, close behavior, and footer action rules.

## Notification and Toast

Observed Message component covers global lightweight feedback.

Rules:

- Use Message for lightweight global operation feedback.
- Use Alert for inline persistent notices.

TODO: confirm whether a separate Toast component exists or whether Message is the product's toast-equivalent.

## Table Interactions

Observed capabilities:

- Row hover
- Single select
- Multi select
- Sort ascending/descending
- Filter dropdown
- Active filter condition display
- Clear filter
- Column width adjustment
- Row drag sort
- Column drag sort
- Expand/collapse rows
- Custom column settings

Rules:

- Use visible sort and filter affordances in header cells.
- Show active filter state.
- Provide clear action for active filters.
- Use Tooltip for truncated content.

## Sidebar Navigation Interactions

Observed behavior:

- 一级菜单 can show a collapse arrow for expandable groups.
- Expanded group can reveal 二级菜单 items.
- Current 二级菜单 selection is indicated by a white rounded item surface and a 4px red dot marker.

Rules:

- Use selected state for the current page or module.
- Use collapse/expand arrow only when the menu item owns child items.
- Keep the selected marker visible even when the selected item text is short.
- For long labels, prefer adaptive sidebar width or a documented truncation + tooltip pattern over clipping.

TODO: confirm hover, active, disabled, and keyboard focus states for SidebarNavigation.

## Top Navigation Interactions

Rules:

- Top menu active item should be visibly distinct from hover/default states.
- Primary action in the topbar should use Button rules.
- User avatar/menu should not compete visually with the primary action.
- If a topbar contains horizontal menu items, do not duplicate the same navigation level in page tabs.

TODO: confirm Element Plus top menu active/hover styling from node `9304:177289`.
