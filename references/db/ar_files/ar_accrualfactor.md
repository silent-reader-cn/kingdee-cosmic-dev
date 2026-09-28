# 计提因素-ar_accrualfactor

## 计提因素-多语言表 t_ar_accrualfactor_l

- **表名称：** 计提因素-多语言表
- **表名：** t_ar_accrualfactor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 计提因素名称 | varchar | 100 |  | √ | ' ' | 计提因素名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_afl_fid |  | fid,flocaleid |
| 2 | pk_t_ar_accrualfactor_l |  | fpkid |

---

## 计提因素数据映射-子表 t_ar_accrualfactor_entry

- **表名称：** 计提因素数据映射-子表
- **表名：** t_ar_accrualfactor_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freservefield | 映射坏账字段 | varchar | 50 |  | √ | ' ' | 映射坏账字段 |
| 3 | freservefieldname | 映射坏账字段 | varchar | 50 |  | √ | ' ' | 映射坏账字段 |
| 4 | fmappingfieldname | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |
| 5 | fbizmain | 业务主体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fentrytisdefault | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 9 | fmappingfield | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_afentry_fid |  | fid |
| 2 | pk_t_ar_accrualfactor_entry |  | fentryid |

---

## 计提因素-主表 t_ar_accrualfactor

- **表名称：** 计提因素-主表
- **表名：** t_ar_accrualfactor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffactortype | 因素字段类型 | varchar | 30 |  | √ | ' ' | 因素字段类型,枚举: F7 :基础资料 TEXT :文本 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fbasedatamain | 基础资料主体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fisdefault | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_af_fnumber |  | fnumber |
| 2 | pk_t_ar_accrualfactor |  | fid |
