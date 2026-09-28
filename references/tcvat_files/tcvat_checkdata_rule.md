# 汇总一般企业重复取数的规则-tcvat_checkdata_rule

## 汇总一般企业重复取数的规则-主表 t_tcvat_checkdata_rule

- **表名称：** 汇总一般企业重复取数的规则-主表
- **表名：** t_tcvat_checkdata_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fname | 规则名称 | varchar | 2000 |  | √ | ' ' | 规则名称 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fruletype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: tcvat_rule_income :收入取数规则 tcvat_rule_rollout :进项转出取数规则 tcvat_rule_diff :差额扣除取数规则 |
| 7 | ffield | 重复类型 | varchar | 30 |  | √ | ' ' | 重复类型,枚举: invoice :开票金额 tcvat_rule_income :未开票金额 tcvat_rule_diff :本期发生额 tcvat_rule_rollout :转出税额 |
| 8 | finvoiceorg | 汇总方案组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 2 :汇总 3 :被汇总 |
| 10 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 11 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 12 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 13 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 |
| 14 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 15 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 17 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 18 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 19 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 20 | ftotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 21 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_checkdata_rule_pkey |  | fid |
| 2 | idx_tcvat_checkdata_rule |  | forgid,fskssqq,fskssqz |
