# 出口报关单-tdm_export_declaration

## 出口报关单-主表 t_tdm_ep_declaration

- **表名称：** 出口报关单-主表
- **表名：** t_tdm_ep_declaration

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpremiumcurrency | 保费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fpremiumamount | 保费金额 | numeric | 23 | 10 | √ | 0 | 保费金额 |
| 4 | fconsignor | 境内发货人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmylajcurrency | 美元离岸价币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | ftransport | 运输工具 | varchar | 50 |  | √ | ' ' | 运输工具 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsupervision | 监管方式代码 | int8 | 64 |  | √ | 0 | [监管方式 bastax_supervision](../bastax_files/bastax_supervision.md) |
| 9 | fconsignee | 境外收货人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | fremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 11 | ffreightmark | 运费标志 | varchar | 50 |  | √ | ' ' | 运费标志,枚举: 1 :1-运费率 2 :2-运费单价 3 :3-运费总价 |
| 12 | fpremiummark | 保费标志 | varchar | 50 |  | √ | ' ' | 保费标志,枚举: 1 :1-保费率 3 :3-保费总价 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fexportdate | 出口日期 | timestamp | 0 |  |  | null | 出口日期 |
| 16 | frecordno | 备案号 | varchar | 50 |  | √ | ' ' | 备案号 |
| 17 | fdeclarationdate | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 18 | fbillno | 出口报关单号 | varchar | 30 |  | √ | ' ' | 出口报关单号 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fwriteoff | 核销单号 | varchar | 50 |  | √ | ' ' | 核销单号 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fsundrycurrency | 杂费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fsundryex | 杂费美元汇率 | numeric | 23 | 10 | √ | 0 | 杂费美元汇率 |
| 25 | fpremiumex | 保费美元汇率 | numeric | 23 | 10 | √ | 0 | 保费美元汇率 |
| 26 | fsundrymark | 杂费标志 | varchar | 50 |  | √ | ' ' | 杂费标志,枚举: 1 :1-杂费率 2 :2-杂费单价 3 :3-杂费总价 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | ffreightcurrency | 运费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fcontractno | 合同协议号 | varchar | 50 |  | √ | ' ' | 合同协议号 |
| 30 | ffreightamount | 运费金额 | numeric | 23 | 10 | √ | 0 | 运费金额 |
| 31 | ftradeway | 成交方式 | varchar | 50 |  | √ | ' ' | 成交方式,枚举: fob :FOB cif :CIF cf :C&F fcr :FCR exw :EXW |
| 32 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :模板导入 3 :直连下载 |
| 33 | ffreightex | 运费美元汇率 | numeric | 23 | 10 | √ | 0 | 运费美元汇率 |
| 34 | fclearancestatus | 结关状态 | varchar | 50 |  | √ | ' ' | 结关状态 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fsundryamount | 杂费金额 | numeric | 23 | 10 | √ | 0 | 杂费金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_ep_declaration |  | fid |
| 2 | idx_tdm_ep_declaration |  | fbillno |

---

## 商品明细-子表 t_tdm_ep_entry

- **表名称：** 商品明细-子表
- **表名：** t_tdm_ep_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemno | 项号 | varchar | 50 |  | √ | ' ' | 项号 |
| 3 | fmylaj | 美元离岸价 | numeric | 23 | 10 | √ | 0 | 美元离岸价 |
| 4 | ftradeamount | 成交金额 | numeric | 23 | 10 | √ | 0 | 成交金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdcountry | 目的国(地区) | varchar | 50 |  | √ | ' ' | 目的国(地区) |
| 7 | ftradeprice | 成交单价 | numeric | 23 | 10 | √ | 0 | 成交单价 |
| 8 | fwriteoffqty | 已核销数量 | numeric | 23 | 10 | √ | 0 | 已核销数量 |
| 9 | fspecification | 规格型号 | varchar | 300 |  | √ | ' ' | 规格型号 |
| 10 | ffirstunitqty | 法定第一单位数量 | numeric | 23 | 10 | √ | 0 | 法定第一单位数量 |
| 11 | funwriteoffqty | 未核销数量 | numeric | 23 | 10 | √ | 0 | 未核销数量 |
| 12 | fyfamount | 运费金额 | numeric | 23 | 10 | √ | 0 | 运费金额 |
| 13 | fzfamount | 杂费金额 | numeric | 23 | 10 | √ | 0 | 杂费金额 |
| 14 | fexemption | 征免 | varchar | 50 |  | √ | ' ' | 征免 |
| 15 | fhscode | 商品编码 | int8 | 64 |  | √ | 0 | [海关商品编码 bastax_hscode](../bastax_files/bastax_hscode.md) |
| 16 | ftradeex | 成交价美元汇率 | numeric | 23 | 10 | √ | 0 | 成交价美元汇率 |
| 17 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsecondunit | 法定第二单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fbfamount | 保费金额 | numeric | 23 | 10 | √ | 0 | 保费金额 |
| 20 | ftradeunit | 成交单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | ffirstunit | 法定第一单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | ftradeqty | 成交数量 | numeric | 23 | 10 | √ | 0 | 成交数量 |
| 23 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 24 | ftradecurrency | 成交币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fhstag | 商品品名 | varchar | 200 |  | √ | ' ' | 商品品名 |
| 26 | fsecondunitqty | 法定第二单位数量 | numeric | 23 | 10 | √ | 0 | 法定第二单位数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ep_entry_fk |  | fid |
| 2 | pk_tdm_ep_entry |  | fentryid |
