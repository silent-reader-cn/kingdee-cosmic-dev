# 一般纳税人已开票数据尚未设定规则-tcvat_ybnsr_rule_invoice

## 一般纳税人已开票数据尚未设定规则-主表 t_tcvat_ybnsr_rule_invoic

- **表名称：** 一般纳税人已开票数据尚未设定规则-主表
- **表名：** t_tcvat_ybnsr_rule_invoic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | ftaxrate | 税率/征收率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率/征收率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 6 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 7 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 8 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 9 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 11 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 12 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 13 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 14 | ftotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 15 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 16 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybnsr_rule_invoic |  | fid |
| 2 | idx_tcvat_ybnsr_rule_invoic |  | forgid,fskssqq,fskssqz |
