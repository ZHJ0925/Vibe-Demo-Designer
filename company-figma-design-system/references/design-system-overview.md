# Design System Overview

This reference captures rules observed from the Figma files:

- IS RB UI改版 Copy
- AiOMP Design for web组件
- 看板工作台 UI改版 Copy

Use these rules when generating or reviewing web UI for this product family. Keep the visual language close to the observed Figma system.

## Source Scope

Observed component and page areas:

- Business detail pages
- Drawer-based task/form workflows
- Dashboard and table-heavy workbench pages
- Button, Input, Search, Form, Alert, Message, Dialog, Table, Tag component demos

## Brand

- Primary brand color is `#222222`.
- Use `#222222` for primary actions, selected states, key emphasis, and dark filled controls.
- Blue colors such as `#0052D9`, `#295FD8`, and `#3370FF` are secondary system colors for links, info states, and auxiliary emphasis.
- TODO: confirm whether blue is allowed for product-level navigation selection outside info/link contexts.

## Color Tokens

Observed neutral colors:

- Primary text: `#1A1A1A`
- Navigation text: `#000000`
- Navigation icon neutral: `#383838`
- Dark text / title alternative: `#1C1F23`, `#171A1F`
- Secondary text: `#494C4F`
- Tertiary text: `#999999`
- Disabled text: `#BDBDBD`
- White surface: `#FFFFFF`
- Page background: `#F5F7F9`, `#F2F5FA`
- Light surface: `#FAFBFC`, `#F3F3F4`
- Border: `#DCDCDC`, `#DEE0E3`, `#E7E7E7`, `#EAEEF5`

Observed semantic colors:

- Info: `#0052D9`
- Info background: `#F2F3FF`, `#F0F4FF`
- Success: `#3BD183`, `#19C573`
- Success background: `#E8FFEF`, `#E8F9F1`
- Warning: `#FE8744`
- Warning background: `#FFF4E8`
- Error: `#FF1432`, `#F54A45`
- Error background: `#FFE9E8`, `#FFE7EA`

## Typography

Observed font family:

- `PingFang SC`

Observed type levels:

- Component demo display title: 48px / 56px
- Dialog title and compact page title: 16px / 24px, semibold
- Form and table body: 14px / 22px
- Section or compact heading: 14px / 22px or 14px / 28px
- Business body and labels: 12px / 20px
- Small tag or dense label: 10px to 12px

Rules:

- Use letter spacing `0`.
- Use 16px titles for dialogs and compact business page headers.
- Use 14px for normal controls and form content.
- Use 12px for dense table labels, status chips, and secondary business metadata.
- TODO: confirm whether 48px / 56px is only for component documentation pages and never for product screens.

## Shape

Observed radius scale:

- Tag: 3px
- Button and input controls: 4px
- Alert and Message: 6px
- Dialog: 9px
- Large overlay mask/container examples: 12px
- Pill button/tag: 16px

## Elevation

Observed shadow:

- `Shadow-3` upper-layer shadow:
  - `0 8px 10px -5px rgba(0,0,0,0.08)`
  - `0 16px 24px 2px rgba(0,0,0,0.04)`
  - `0 6px 30px 5px rgba(0,0,0,0.05)`

Use this shadow for Message, dropdowns, popovers, and similar upper-layer floating surfaces.

## Density

- Table default header height: 40px.
- Table default row height: 40px.
- Component library also shows 36px, 46px, and 54px row-height options for density variants.
- Form item vertical gap is commonly 24px.
- Form label width is commonly 80px.
- Button text/icon gap is commonly 8px.

## Design Language

- This is a dense enterprise web system.
- Prefer restrained surfaces, compact spacing, clear hierarchy, and data-first layouts.
- Do not use decorative hero sections, oversized marketing cards, or ornamental gradients for business screens.
- Cards are functional containers for metrics, tables, and grouped content.
- Workbench pages use a compact left sidebar navigation with 12px labels, 16px icons, and a white selected sub-item surface with a 4px red marker.
- Left sidebar navigation must not visually merge with the right page content. Use a white navigation surface plus subtle shadow, divider, or enough separation.
- Top navigation should be used for page identity, global actions, and user identity when those elements exist.
- Sidebar widths observed in Figma are reference values, not hard constraints. Future page generation must adapt sidebar width to labels, viewport, collapsed mode, and readability.
- Icons must come from the confirmed Figma icon library or be reported as `TODO: confirm icon`; do not invent icons.
