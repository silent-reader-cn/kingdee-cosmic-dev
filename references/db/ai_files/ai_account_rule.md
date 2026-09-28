# 科目核算规则-ai_account_rule

## 科目核算规则-多语言表 t_ai_account_rule_l

- **表名称：** 科目核算规则-多语言表
- **表名：** t_ai_account_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | fnote | 备注 | varchar | 1500 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_account_rule_l_lid |  | fid,flocaleid |
| 2 | pk_ai_account_rule_l |  | fpkid |

---

## 规则描述-多语言表 t_ai_account_rule_info_l

- **表名称：** 规则描述-多语言表
- **表名：** t_ai_account_rule_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountruledescription | 科目核算规则描述 | varchar | 255 |  | √ | ' ' | 科目核算规则描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_account_rule_info_l |  | fpkid |
| 2 | idx_ai_account_rule_info_l_lid |  | fentryid,flocaleid |

---

## 科目字段映射-子表 t_ai_ruleacctentry

- **表名称：** 科目字段映射-子表
- **表名：** t_ai_ruleacctentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctfieldkey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryaccttable | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_ruleacctentry |  | fid |
| 2 | pk_t_ai_ruleacctentry |  | fentryid |

---

## 字段映射-子表 t_ai_rulefactorentry

- **表名称：** 字段映射-子表
- **表名：** t_ai_rulefactorentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentityid | 实体类型 | varchar | 100 |  | √ | ' ' | 实体类型 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdatatype | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 7 | ffieldkey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_rulefactorentry |  | fentryid |
| 2 | idx_ai_rulefactorentry |  | fid |

---

## 科目核算规则-主表 t_ai_account_rule

- **表名称：** 科目核算规则-主表
- **表名：** t_ai_account_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fnote | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | ffactorvalue_basedata | 影响因素_基础资料 | varchar | 200 |  | √ | ' ' | 影响因素_基础资料 |
| 7 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 8 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ffactorvalue_asstdata | 影响因素_辅助资料 | varchar | 200 |  | √ | ' ' | 影响因素_辅助资料 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | ffactorname | 影响因素 | varchar | 50 |  | √ | ' ' | 影响因素 |
| 18 | ffactorvalue | 影响因素值 | varchar | 200 |  | √ | ' ' | 影响因素值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_acc_rule_accounttable |  | faccounttableid |
| 2 | pk_ai_account_rule |  | fid |

---

## 规则描述-子表 t_ai_account_rule_info

- **表名称：** 规则描述-子表
- **表名：** t_ai_account_rule_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | faccountruledescription | 科目核算规则描述 | varchar | 255 |  | √ | ' ' | 科目核算规则描述 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | faccountid | 科目编码 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_account_rule_info |  | fentryid |
| 2 | idx_ai_account_rule_info_fk |  | fid |
