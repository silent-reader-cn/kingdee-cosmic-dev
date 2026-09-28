# 外部系统API组-pbd_extsys_apiset

## 单据体-子表 t_mal_ext_apisetentry

- **表名称：** 单据体-子表
- **表名：** t_mal_ext_apisetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextsysapi | 外部系统API | int8 | 64 |  | √ | 0 | [外部系统API pbd_extsys_api](../pbd_files/pbd_extsys_api.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fhandleclass | 接口处理类 | varchar | 100 |  | √ | ' ' | 接口处理类 |
| 5 | fsystype | 系统类型 | bpchar | 1 |  | √ | ' ' | 系统类型,枚举: 1 :自建 2 :京东 3 :苏宁 4 :得力 5 :西域 6 :晨光 7 :京东工业品 8 :鑫方盛 9 :震坤行 |
| 6 | fvalid | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_apisetentry_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_ext_apisetentry |  | fentryid |

---

## 外部系统API组-多语言表 t_mal_extapiset_l

- **表名称：** 外部系统API组-多语言表
- **表名：** t_mal_extapiset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_extapiset_l |  | fpkid |
| 2 | idx_mal_extapiset_l_fid |  | flocaleid,fid |

---

## 外部系统API组-主表 t_mal_extapiset

- **表名称：** 外部系统API组-主表
- **表名：** t_mal_extapiset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fispreset | 预置 | bpchar | 1 |  | √ | ' ' | 预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_extapiset_fnumber |  | fnumber |
| 2 | pk_t_mal_extapiset |  | fid |
