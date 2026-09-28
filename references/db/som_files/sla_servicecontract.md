# 共享服务合同-sla_servicecontract

## 共享服务合同-主表 t_tk_sla_sercontract

- **表名称：** 共享服务合同-主表
- **表名：** t_tk_sla_sercontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 4 | frelationtype | 委托关系类型 | bpchar | 1 |  | √ | '0' | 委托关系类型,枚举: 1 :核算组织委托共享中心 |
| 5 | forgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fenddate | 合同截止日期 | timestamp | 0 |  |  | null | 合同截止日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbillamtsum | 累计账单金额 | numeric | 23 | 10 | √ | 0 | 累计账单金额 |
| 10 | ftaxsum | 累计账单税额 | numeric | 23 | 10 | √ | 0 | 累计账单税额 |
| 11 | fbillamtinvsum | 累计账单已开票金额 | numeric | 23 | 10 | √ | 0 | 累计账单已开票金额 |
| 12 | frelationorg | 共享服务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbillno | 合同编码 | varchar | 30 |  | √ | ' ' | 合同编码 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcustomer | 共享服务客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | ftallyorg | 共享中心所属核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsigningdate | 签约日期 | timestamp | 0 |  |  | null | 签约日期 |
| 21 | fcurrency | 合同币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbillamtsumstd | 累计账单金额折本币 | numeric | 23 | 10 | √ | 0 | 累计账单金额折本币 |
| 24 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 26 | fbillamtrecsum | 累计账单已收款金额 | numeric | 23 | 10 | √ | 0 | 累计账单已收款金额 |
| 27 | fstartdate | 合同起始日期 | timestamp | 0 |  |  | null | 合同起始日期 |
| 28 | fcontractdetails | 合同明细 | int8 | 64 |  | √ | 0 | [合同明细 sla_contractdetails](../som_files/sla_contractdetails.md) |
| 29 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fisperiod | 期初标识 | bpchar | 1 |  | √ | ' ' | 期初标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_sercontract |  | fid |
| 2 | idx_ssc_sla_sercontract |  | fbillno |

---

## 共享服务合同-多语言表 t_tk_sla_sercontract_l

- **表名称：** 共享服务合同-多语言表
- **表名：** t_tk_sla_sercontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 共享服务合同名称 | varchar | 50 |  | √ | ' ' | 共享服务合同名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_sercontract_l |  | fpkid |
| 2 | idx_ssc_sla_sercontract_l |  | fid,flocaleid |

---

## 合同明细-子表 t_tk_sla_scdetails

- **表名称：** 合同明细-子表
- **表名：** t_tk_sla_scdetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourceentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 3 | fserviceproject | 服务项目 | int8 | 64 |  | √ | 0 | [服务项目 sla_serviceproject](../som_files/sla_serviceproject.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fprice | 暂估单价 | numeric | 23 | 10 | √ | 0 | 暂估单价 |
| 6 | fcdremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fnorfixedamount | 结算固定价格 | numeric | 23 | 10 | √ | 0 | 结算固定价格 |
| 8 | fserviceclassify | 服务类别 | int8 | 64 |  | √ | 0 | [服务项目分类 sla_serviceclassify](../som_files/sla_serviceclassify.md) |
| 9 | fservicestandard | 服务标准 | int8 | 64 |  | √ | 0 | [服务标准 sla_servicelevel](../som_files/sla_servicelevel.md) |
| 10 | fbilling | 计费方式 | varchar | 10 |  | √ | ' ' | 计费方式,枚举: qty :数量单价 fixed :固定价格 |
| 11 | ffixedamount | 暂估固定价格 | numeric | 23 | 10 | √ | 0 | 暂估固定价格 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsettlementperiod | 结算周期 | varchar | 10 |  | √ | ' ' | 结算周期,枚举: MM :月度 QQ :季度 YY :年度 EL :其他 |
| 14 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fnorprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_sla_scdetails |  | fid |
| 2 | pk_tk_sla_scdetails |  | fentryid |
