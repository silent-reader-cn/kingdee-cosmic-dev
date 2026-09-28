# 组员关系同步规则-perm_usrgrprel_rules

## 组员关系同步规则-主表 t_perm_usrgrprel_rules

- **表名称：** 组员关系同步规则-主表
- **表名：** t_perm_usrgrprel_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 组员关系同步规则-多语言表 t_perm_usrgrprel_rules_l

- **表名称：** 组员关系同步规则-多语言表
- **表名：** t_perm_usrgrprel_rules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 单据体-子表 t_perm_usrgrprel_ruleent

- **表名称：** 单据体-子表
- **表名：** t_perm_usrgrprel_ruleent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fruleconftype | fruleconftype | varchar | 50 |  | √ | ' ' |  |
| 4 | fuserfieldkey | fuserfieldkey | varchar | 50 |  | √ | ' ' |  |
| 5 | foper | foper | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fsrcentity | fsrcentity | varchar | 36 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | frule | 规则 | text | 0 |  |  | null | 规则 |
| 10 | fusrgrpid | fusrgrpid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fgrprefbdtype | fgrprefbdtype | varchar | 50 |  | √ | ' ' |  |
| 13 | fgrpreffieldkey | fgrpreffieldkey | varchar | 50 |  | √ | ' ' |  |
| 14 | frule_tag | 规则_详情 | text | 0 |  |  | null | 规则_详情 |
| 15 | fiscomplexrule | 使用复杂规则 | bpchar | 1 |  | √ | '0' | 使用复杂规则 |
| 16 | fgrprefvalue | fgrprefvalue | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_usrgrprel_ruleent |  | fid |
| 2 | idx_perm_usrgrprel_ruent |  | fusrgrpid |
