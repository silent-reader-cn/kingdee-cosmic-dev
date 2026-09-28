# 结算判定配置-ism_interorgsettlecfg

## 结算判定配置-主表 t_ism_interorgsettlecfg

- **表名称：** 结算判定配置-主表
- **表名：** t_ism_interorgsettlecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fsettlerelationname | fsettlerelationname | varchar | 100 |  | √ | ' ' |  |
| 4 | fsettlerelation | 结算关系标识 | varchar | 80 |  | √ | ' ' | 结算关系标识 |
| 5 | fbill | 单据对象 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 6 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fbillfilterstr_tag | 单据过滤条件_详情 | text | 0 |  |  | null | 单据过滤条件_详情 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fbalanceorgname | fbalanceorgname | varchar | 100 |  | √ | ' ' |  |
| 11 | fownerorg | 需求方结算组织标识 | varchar | 80 |  | √ | ' ' | 需求方结算组织标识 |
| 12 | fisenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 13 | fbalanceorg | 供应方结算组织标识 | varchar | 80 |  | √ | ' ' | 供应方结算组织标识 |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fownerorgname | fownerorgname | varchar | 100 |  | √ | ' ' |  |
| 17 | fbillfilterstr | 单据过滤条件 | varchar | 255 |  | √ | ' ' | 单据过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_intorgcf_fno |  | fnumber |
| 2 | t_ism_interorgsettlecfg_pkey |  | fid |

---

## 结算判定配置-多语言表 t_ism_interorgsettlecfg_l

- **表名称：** 结算判定配置-多语言表
- **表名：** t_ism_interorgsettlecfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_interorgsettlecfg_l_pkey |  | fpkid |
| 2 | idx_ism_int_l_flid |  | fid,flocaleid |
