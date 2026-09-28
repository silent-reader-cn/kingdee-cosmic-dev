# 工具-gai_tool

## 工具-多语言表 t_gai_tool_l

- **表名称：** 工具-多语言表
- **表名：** t_gai_tool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fillustrate | 使用说明 | varchar | 2000 |  | √ | ' ' | 使用说明 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_tool_l |  | fpkid |
| 2 | idx_gai_tool_l_fid |  | fid |

---

## 工具-使用范围表 t_gai_tool_u

- **表名称：** 工具-使用范围表
- **表名：** t_gai_tool_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_tool_u_uo |  | fuseorgid |
| 2 | pk_t_gai_tool_u |  | fdataid,fuseorgid |

---

## 工具-主表 t_gai_tool

- **表名称：** 工具-主表
- **表名：** t_gai_tool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [工具分组 gai_tool_group](../gai_files/gai_tool_group.md) |
| 3 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fagentcount | 关联智能体数量 | int8 | 64 |  | √ | 0 | 关联智能体数量 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsource | 工具来源 | varchar | 50 |  | √ | 'customize' | 工具来源,枚举: kingdee :金蝶官方 customize :自定义工具 |
| 8 | fispreset | 是否预置 | varchar | 1 |  | √ | '0' | 是否预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fpicture | 工具头像 | varchar | 499 |  | √ | ' ' | 工具头像 |
| 12 | fconfig | 工具配置 | varchar | 255 |  | √ | ' ' | 工具配置 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fprocesscount | 关联任务流数量 | int8 | 64 |  | √ | 0 | 关联任务流数量 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: internal_mcp :系统OpenAPI mcp_tool :外部MCP restful_api :RESTful API cosmic_action :自定义操作 third_openapi :OpenAPI |
| 25 | fcloudid | 业务云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 26 | fconfig_tag | 工具配置_详情 | text | 0 |  |  | null | 工具配置_详情 |
| 27 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fillustrate | 使用说明 | varchar | 2000 |  | √ | ' ' | 使用说明 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 31 | ftest_status | 测试状态 | varchar | 1 |  | √ | '0' | 测试状态,枚举: 0 :未通过测试 1 :已通过测试 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_tool_fname |  | fname |
| 2 | pk_t_gai_tool |  | fid |
| 3 | idx_t_gai_tool_createorg |  | fcreateorgid |
| 4 | idx_t_gai_tool_master |  | fmasterid |
