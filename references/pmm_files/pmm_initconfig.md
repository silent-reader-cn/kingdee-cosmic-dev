# 电商初始化配置-pmm_initconfig

## 电商初始化配置-主表 t_mal_initconfig

- **表名称：** 电商初始化配置-主表
- **表名：** t_mal_initconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fconnecttypeid | 连接类型 | varchar | 36 |  | √ | ' ' | 连接类型 isc_connection_type |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsourcename | 电商标志 | varchar | 50 |  | √ | ' ' | 电商标志 |
| 7 | fdatasourceid | 连接配置 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 8 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fplatform | 电商类型 | bpchar | 1 |  | √ | ' ' | 电商类型,枚举: 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_initconfig_fnumber |  | fnumber |
| 2 | pk_t_mal_initconfig |  | fid |

---

## 单据体-子表 t_mal_initconfigentry

- **表名称：** 单据体-子表
- **表名：** t_mal_initconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsort | 任务执行顺序 | int4 | 32 |  | √ | 0 | 任务执行顺序 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftaskid | 任务明细 | int8 | 64 |  | √ | 0 | 电商初始化任务 pmm_inittask |
| 5 | fvalid | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_initconfigentry |  | fentryid |
| 2 | idx_mal_initconfigentry_fid |  | fid,ftaskid |

---

## 电商初始化配置-多语言表 t_mal_initconfig_l

- **表名称：** 电商初始化配置-多语言表
- **表名：** t_mal_initconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_initconfig_l |  | fpkid |
| 2 | idx_mal_initconfig_l_fid |  | fid,flocaleid |
