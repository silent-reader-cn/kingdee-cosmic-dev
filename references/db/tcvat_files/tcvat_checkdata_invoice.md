# 汇总一般企业已开票数据尚未设定规则-tcvat_checkdata_invoice

## 汇总一般企业已开票数据尚未设定规则-主表 t_tcvat_checkdata_invoice

- **表名称：** 汇总一般企业已开票数据尚未设定规则-主表
- **表名：** t_tcvat_checkdata_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | ftaxrate | 税率/征收率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率/征收率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | finvoiceorg | 汇总方案组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 2 :汇总 3 :被汇总 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 9 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 10 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费发票 |
| 11 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 12 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 14 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 15 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 16 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 17 | ftotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 18 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 19 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_checkdata_invoice |  | forgid,fskssqq,fskssqz |
| 2 | t_tcvat_checkdata_invoice_pkey |  | fid |
