# 银行回单匹配规则-receipt_bd_match_rule

## 银行回单匹配规则-主表 t_receipt_bd_match_rule

- **表名称：** 银行回单匹配规则-主表
- **表名：** t_receipt_bd_match_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmatch_rule | 路由规则 | varchar | 500 |  | √ | ' ' | 路由规则 |
| 3 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 4 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | ftrans_type | 交易类型 | varchar | 50 |  | √ | '0' | 交易类型,枚举: 0 :收付款交易 1 :银行结息 2 :资金归集 |
| 11 | fnumber | 模板名称 | varchar | 30 |  | √ | ' ' | 模板名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_bd_match_rule_pkey |  | fid |

---

## 银行回单匹配规则-多语言表 t_receipt_bd_match_rule_l

- **表名称：** 银行回单匹配规则-多语言表
- **表名：** t_receipt_bd_match_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_bd_match_rule_l_pkey |  | fpkid |
| 2 | idx_receipt_bd_match_rule_l_0 |  | fid,flocaleid |
