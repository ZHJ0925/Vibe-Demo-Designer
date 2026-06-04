# Naming Rules

These naming rules reflect observed Figma node names and component documentation naming patterns.

## General

- Use clear bilingual or Chinese business names when the source design uses Chinese product terminology.
- Use English component names for component library demos when the source component uses English names.
- Keep component names stable across pages.
- Use `/` to express component hierarchy or variant grouping when appropriate.

## Page Naming

Observed examples:

- `RB商机`
- `看板工作台UI改版`
- `Welcome 欢迎使用`

Rules:

- Use business domain names for product pages.
- Use “模块 / 页面功能” style for business pages when needed.
- Use explicit component/demo page names for component documentation.

TODO: confirm final page naming convention for production Figma files.

## Frame Naming

Observed examples:

- `商机详情`
- `任务推荐1.0-沟通跟进`
- `车辆管理看板`
- `Button-demo 按钮示例`
- `Input-demo 输入框示例`
- `search-demo 搜索示例`
- `Form-demo 表单示例`
- `Alert-demo 警告示例`
- `Message-demo 全局提示示例`
- `Dialog-demo 对话框示例`
- `Table表格示例`
- `Tag-demo 标签示例`
- `导航栏`

Rules:

- Business frames should use the business page/module name.
- Component documentation frames should use `ComponentName-demo 中文说明`.
- Keep version text only when the design itself represents a versioned workflow, such as `任务推荐1.0-沟通跟进`.

## Section Naming

Observed section topics:

- 基础按钮
- 组件状态
- 组件大小
- 不同主题
- 基础表格
- 可展开表格
- 固定表头
- 筛选
- 加载态

Rules:

- Use purpose-based section names.
- For component docs, group by variant, state, size, theme, and usage scenario.
- For business pages, group by business information block.

## Component Naming

Observed components:

- Button
- Input
- Search
- Form
- Alert
- Message
- Dialog
- Table
- Tag
- Drawer
- Descriptions
- Sidebar/Menu
- Steps
- Popover
- DatePicker
- Checkbox
- Badge
- Scrollbar
- SidebarNavigation

Rules:

- Use singular component names.
- Use PascalCase for English component names.
- Use business-specific names only for composed modules.

## Variant Naming

Observed variant dimensions:

- Type
- State
- Size
- Theme
- Shape
- Disabled
- Loading
- Selected

Rules:

- Prefer explicit variant property names such as `type`, `state`, `size`, `theme`, `shape`.
- Use values like `default`, `primary`, `success`, `warning`, `danger`, `disabled`, `loading`.
- Use `dark`, `light`, `outline`, `light-outline` for Tag theme style variants.

TODO: confirm exact Figma component property names for all published components.

## Layer Naming

Rules:

- Use semantic names for meaningful layers: `Header`, `Content`, `Footer`, `Label`, `Control`, `Icon`, `Close`, `Pagination`.
- Avoid leaving production component layers as generic `Frame 1`, `Group 2`, or duplicated copy names.
- Keep repeated table structures named by role: `Table/Header`, `Table/Row`, `Table/Cell`.
- Keep sidebar navigation layers named by role: `SidebarNavigation`, `MenuGroup`, `MenuItem`, `SubMenuItem`, `Icon`, `Label`, `CollapseArrow`, `ActiveMarker`.
- Use semantic icon layer names or confirmed published icon names. If the icon is not confirmed, mark it as `TODO: confirm icon` instead of creating a new arbitrary icon name.

TODO: confirm whether the source library enforces a strict layer naming plugin or lint rule.
