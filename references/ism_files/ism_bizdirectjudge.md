# 业务方向配置-ism_bizdirectjudge

## 业务方向配置-主表 t_ism_bizdirectjudge

- **表名称：** 业务方向配置-主表
- **表名：** t_ism_bizdirectjudge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdirect | 业务方向 | bpchar | 1 |  | √ | '0' | 业务方向,枚举: 0 :正向业务 1 :反向业务 |
| 3 | fsysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fbill | 单据对象 | varchar | 72 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 6 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fbillfilterstr | 单据过滤条件 | varchar | 255 |  | √ | ' ' | 单据过滤条件 |
| 9 | fbillfilterstr_tag | 单据过滤条件_详情 | text | 0 |  |  | null | 单据过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_bizdirectjudge_fnum |  | fnumber |
| 2 | t_ism_bizdirectjudge_pkey |  | fid |
| 3 | idx_ism_bizdirectjudge_fbill |  | fbill |

---

## 业务方向配置-多语言表 t_ism_bizdirectjudge_l

- **表名称：** 业务方向配置-多语言表
- **表名：** t_ism_bizdirectjudge_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_bdirejudge_l_id_local |  | fid,flocaleid |
| 2 | t_ism_bizdirectjudge_l_pkey |  | fpkid |
