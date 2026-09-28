# 对账规则配置-cas_reconciliationrule

## 单据体-子表 t_cas_reconciliation_e

- **表名称：** 单据体-子表
- **表名：** t_cas_reconciliation_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatafilterdesc_real | 适用条件2 | text | 0 |  |  | null | 适用条件2 |
| 3 | frulesname | 对账规则 | varchar | 100 |  | √ | ' ' | 对账规则 |
| 4 | fdatafilterdesc_real_tag | 适用条件2_详情 | text | 0 |  |  | null | 适用条件2_详情 |
| 5 | fdatafilterdesc | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_reconciliation_e_pkey |  | fentryid |
| 2 | index_cas_rule_fid |  | fid |

---

## 组织-多选基础资料表 t_cas_reconciliation_b

- **表名称：** 组织-多选基础资料表
- **表名：** t_cas_reconciliation_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cas_rec_fid |  | fid |
| 2 | t_cas_reconciliation_b_pkey |  | fpkid |

---

## 对账规则配置-多语言表 t_cas_reconciliationrule_l

- **表名称：** 对账规则配置-多语言表
- **表名：** t_cas_reconciliationrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_reconciliationrule_l_pkey |  | fpkid |
| 2 | idx_cas_recciliation_l_fid |  | fid,flocaleid |

---

## 对账规则配置-主表 t_cas_reconciliationrule

- **表名称：** 对账规则配置-主表
- **表名：** t_cas_reconciliationrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgfield | 隐藏组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_rule_fnumber |  | fnumber |
| 2 | index_cas_rule_orgfield |  | forgfield |
| 3 | t_cas_reconciliationrule_pkey |  | fid |
| 4 | idx_cas_rule_fname |  | fname,fenable |
