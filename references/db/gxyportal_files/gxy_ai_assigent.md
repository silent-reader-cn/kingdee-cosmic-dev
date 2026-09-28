# 首页AI助手配置-gxy_ai_assigent

## 首页AI助手配置-多语言表 t_gxy_ai_assigent_l

- **表名称：** 首页AI助手配置-多语言表
- **表名：** t_gxy_ai_assigent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gxy_ai_assigent_l |  | fid,flocaleid |
| 2 | pk_gxy_ai_assigent_l |  | fpkid |

---

## 首页AI助手配置-主表 t_gxy_ai_assigent

- **表名称：** 首页AI助手配置-主表
- **表名：** t_gxy_ai_assigent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 6 | fagent | 会话智能体 | int8 | 64 |  | √ | 0 | 智能体 gai_agent |
| 7 | fpermbizobjid | 鉴权表单 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpicture | 头像 | varchar | 255 |  | √ | ' ' | 头像 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fopentype | 打开方式 | varchar | 50 |  | √ | ' ' | 打开方式,枚举: menu :菜单 agent :会话 customize :自定义 url :外部链接 |
| 14 | fagenttype | 会话智能体类型 | varchar | 50 |  | √ | ' ' | 会话智能体类型,枚举: gai_agent :智能体 gai_process :任务流 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | flicencekey | 许可key | varchar | 50 |  | √ | ' ' | 许可key |
| 17 | furl | 跳转URL | varchar | 255 |  | √ | ' ' | 跳转URL |
| 18 | fplugin | 自定义插件 | varchar | 100 |  | √ | ' ' | 自定义插件 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fdesc | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 21 | fbgcolor | 背景颜色 | varchar | 50 |  | √ | ' ' | 背景颜色 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gxy_ai_assigent |  | fid |

---

## 单据体-子表 t_gxy_ai_assigentlink

- **表名称：** 单据体-子表
- **表名：** t_gxy_ai_assigentlink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 智能体 | int8 | 64 |  | √ | 0 | 智能体 gai_agent |
| 3 | fmenuparams | 菜单自定义参数 | varchar | 255 |  | √ | ' ' | 菜单自定义参数 |
| 4 | fagenttype | 智能体类型 | varchar | 50 |  | √ | ' ' | 智能体类型,枚举: gai_agent :智能体 gai_process :任务流 |
| 5 | fopenappid | 打开应用 | varchar | 50 |  | √ | ' ' | 打开应用 |
| 6 | fopenmenuid | 打开菜单id | varchar | 50 |  | √ | ' ' | 打开菜单id |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gxy_ai_assigentlink_fk |  | fid |
| 2 | pk_gxy_ai_assigentlink |  | fentryid |
