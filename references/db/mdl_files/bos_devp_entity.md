# 卡片实体-bos_devp_entity

## 卡片实体-多语言表 t_meta_cardrepository_l

- **表名称：** 卡片实体-多语言表
- **表名：** t_meta_cardrepository_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_cardrepo_localeid |  | fid,flocaleid |
| 2 | t_meta_cardrepository_l_pkey |  | fpkid |

---

## 卡片实体-主表 t_meta_cardrepository

- **表名称：** 卡片实体-主表
- **表名：** t_meta_cardrepository

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 3 | fappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 4 | fcardconfig | 卡片配置 | text | 0 |  |  | null | 卡片配置 |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | frefcount | 引用次数 | int8 | 64 |  | √ | 0 | 引用次数 |
| 9 | fplugin | 插件 | varchar | 500 |  | √ | ' ' | 插件 |
| 10 | fentityid | 实体id | varchar | 36 |  | √ | ' ' | 实体id |
| 11 | fformid | 卡片模板 | varchar | 36 |  | √ | ' ' | 卡片模板 |
| 12 | ftitleimg | 标题图标 | varchar | 500 |  |  | null | 标题图标 |
| 13 | fconfigpagename | 配置页面名称 | varchar | 36 |  | √ | ' ' | 配置页面名称 |
| 14 | fwidgetnumber | 小部件编码 | varchar | 36 |  | √ | ' ' | 小部件编码 |
| 15 | fbizunitid | 功能分组 | varchar | 36 |  | √ | ' ' | 功能分组 |
| 16 | flabel | 标签 | varchar | 500 |  |  | null | 标签 |
| 17 | fisrefresh | 是否刷新 | bpchar | 1 |  | √ | '0' | 是否刷新,枚举: 1 :是 0 :否 |
| 18 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fwidgetname | 小部件名称 | varchar | 36 |  | √ | ' ' | 小部件名称 |
| 20 | fstate | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: 1 :未发布 2 :已发布 |
| 21 | fisshowtitlearea | 是否显示标题区 | bpchar | 1 |  | √ | ' ' | 是否显示标题区,枚举: 0 :否 1 :是 |
| 22 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: LinkCard :链接卡片 YunZhiJiaCard :云之家卡片 BillDigestCard :单据摘要卡片 ListStatisticsCard :列表统计卡片 StatementCard :报表卡片 WorkflowCard :工作流卡片 CustomCard :自定义卡片 |
| 23 | fconfigpagenumber | 配置页面编码 | varchar | 36 |  | √ | ' ' | 配置页面编码 |
| 24 | fscene | 使用场景 | varchar | 5 |  | √ | '0' | 使用场景,枚举: 0 :不限 1 :首页 2 :应用首页 |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 26 | fformname | 卡片模板名称 | varchar | 100 |  | √ | ' ' | 卡片模板名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_cardrepository_pkey |  | fid |
| 2 | t_meta_cardrepository_fnumber_key |  | fnumber |
