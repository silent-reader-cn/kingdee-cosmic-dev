# 计提来源-ar_accrualsource

## 计提来源-多语言表 t_ar_accrualsource_l

- **表名称：** 计提来源-多语言表
- **表名：** t_ar_accrualsource_l

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
| 1 | idx_ar_asr_fid |  | fid,flocaleid |
| 2 | pk_t_ar_accrualsource_l |  | fpkid |

---

## 计提来源-主表 t_ar_accrualsource

- **表名称：** 计提来源-主表
- **表名：** t_ar_accrualsource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fentityobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 5 | fdatefield | 日期字段 | varchar | 50 |  | √ | ' ' | 日期字段 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdatefielddesc | 账龄起算日 | varchar | 50 |  | √ | ' ' | 账龄起算日 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | famttype | 计提主体类型 | varchar | 30 |  | √ | ' ' | 计提主体类型,枚举: 1 :计提主体 2 :冲减主体 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fwofffilterdesc | 计提冲回条件 | varchar | 2000 |  | √ | ' ' | 计提冲回条件 |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ffilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | ffilterdesc | 参与计提条件 | varchar | 2000 |  | √ | ' ' | 参与计提条件 |
| 17 | fwofffilter | 冲回过滤条件 | varchar | 2000 |  | √ | ' ' | 冲回过滤条件 |
| 18 | fisdefault | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 19 | fbaseamfielddesc | 基准金额 | varchar | 50 |  | √ | ' ' | 基准金额 |
| 20 | fbaseamfield | 金额字段 | varchar | 50 |  | √ | ' ' | 金额字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_asr_fnumber |  | fnumber |
| 2 | pk_t_ar_accrualsource |  | fid |
