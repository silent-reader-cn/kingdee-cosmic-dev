# 一般纳税人重复取数的发票-tcvat_ybnsr_repeat_invoic

## 一般纳税人重复取数的发票-主表 t_tcvat_ybnsr_repeat_inv

- **表名称：** 一般纳税人重复取数的发票-主表
- **表名：** t_tcvat_ybnsr_repeat_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fname | 规则名称 | varchar | 1000 |  | √ | ' ' | 规则名称 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: tcvat_rule_income :收入取数规则 tcvat_rule_rollout :进项转出取数规则 tcvat_rule_diff :差额扣除取数规则 |
| 7 | ffield | 重复类型 | varchar | 50 |  | √ | ' ' | 重复类型,枚举: invoice :开票金额 tcvat_rule_income :未开票金额 tcvat_rule_diff :本期发生额 tcvat_rule_rollout :转出税额 |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 9 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 10 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 11 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 12 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 14 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 15 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 16 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 17 | ftotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 18 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybnsr_repeat_inv |  | fid |
| 2 | idx_tcvat_ybnsr_repeat_inv |  | forgid,fskssqq,fskssqz |
