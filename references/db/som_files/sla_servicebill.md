# 共享服务账单-sla_servicebill

## 关联子实体-子表 t_tk_sla_serbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_tk_sla_serbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_serbill_lk |  | fpkid |
| 2 | idx_tk_sla_serbill_lk_fk |  | fid |

---

## 共享服务账单-反写记录表 t_tk_sla_serbill_wb

- **表名称：** 共享服务账单-反写记录表
- **表名：** t_tk_sla_serbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_sla_serbill_wb_fk |  | fid |
| 2 | pk_tk_sla_serbill_wb |  | fentryid |

---

## 关联子实体-子表 t_tk_sla_sbsteridetails_lk

- **表名称：** 关联子实体-子表
- **表名：** t_tk_sla_sbsteridetails_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_sbsteridetails_lk |  | fpkid |
| 2 | idx_tk_sla_sbsteridetails_lk_fk |  | fentryid |

---

## 账单明细-子表 t_tk_sla_sbbilldetails

- **表名称：** 账单明细-子表
- **表名：** t_tk_sla_sbbilldetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvouchnotaxamt | 核定金额不含税 | numeric | 23 | 10 | √ | 0 | 核定金额不含税 |
| 3 | fdeducamtstd | 扣减金额折本币 | numeric | 23 | 10 | √ | 0 | 扣减金额折本币 |
| 4 | fsourceentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 7 | fservicelevel | 服务标准 | int8 | 64 |  | √ | 0 | [服务标准 sla_servicelevel](../som_files/sla_servicelevel.md) |
| 8 | fbdremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fvouchamtstd | 核定金额折本币 | numeric | 23 | 10 | √ | 0 | 核定金额折本币 |
| 10 | fbdamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fvouchamt | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 12 | fqty | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 13 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 14 | fserviceproject | 服务项目 | int8 | 64 |  | √ | 0 | [服务项目 sla_serviceproject](../som_files/sla_serviceproject.md) |
| 15 | fbdservicepriod | 服务结算期间 | int8 | 64 |  | √ | 0 | [服务结算期间 sla_serviceperiod](../som_files/sla_serviceperiod.md) |
| 16 | fdeducamt | 扣减金额 | numeric | 23 | 10 | √ | 0 | 扣减金额 |
| 17 | fdeduremark | 扣减说明 | varchar | 255 |  | √ | ' ' | 扣减说明 |
| 18 | fvouchnotaxamtstd | 核定金额不含税折本币 | numeric | 23 | 10 | √ | 0 | 核定金额不含税折本币 |
| 19 | fbdamountstd | 金额折本币 | numeric | 23 | 10 | √ | 0 | 金额折本币 |
| 20 | ftaxamountstd | 税额折本币 | numeric | 23 | 10 | √ | 0 | 税额折本币 |
| 21 | fnorfixedamount | 结算固定价格 | numeric | 23 | 10 | √ | 0 | 结算固定价格 |
| 22 | fserviceclassify | 服务类别 | int8 | 64 |  | √ | 0 | [服务项目分类 sla_serviceclassify](../som_files/sla_serviceclassify.md) |
| 23 | fbilling | 计费方式 | varchar | 10 |  | √ | ' ' | 计费方式,枚举: qty :数量单价 fixed :固定价格 |
| 24 | ffixedamount | 固定价格 | numeric | 23 | 10 | √ | 0 | 固定价格 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fnorprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_sbbilldetails |  | fentryid |
| 2 | idx_ssc_sla_sbbilldetails |  | fid |

---

## 冲暂估账单-子表 t_tk_sla_sbsteridetails

- **表名称：** 冲暂估账单-子表
- **表名：** t_tk_sla_sbsteridetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsdamountleft | 可冲销余额 | numeric | 23 | 10 | √ | 0 | 可冲销余额 |
| 3 | fsdapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 4 | fsdsteriamt | 冲销暂估金额 | numeric | 23 | 10 | √ | 0 | 冲销暂估金额 |
| 5 | fsdsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsdtaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 8 | fsdsteriamtstd | 冲销暂估金额折本币 | numeric | 23 | 10 | √ | 0 | 冲销暂估金额折本币 |
| 9 | fsdserpriod | 服务结算期间 | int8 | 64 |  | √ | 0 | [服务结算期间 sla_serviceperiod](../som_files/sla_serviceperiod.md) |
| 10 | fsdtaxamt | 税额余额 | numeric | 23 | 10 | √ | 0 | 税额余额 |
| 11 | fsdbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fsdremark | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 13 | fsdsteritaxamt | 冲销税额 | numeric | 23 | 10 | √ | 0 | 冲销税额 |
| 14 | fsdsteritaxamtstd | 冲销税额折本币 | numeric | 23 | 10 | √ | 0 | 冲销税额折本币 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_sbsteridetails |  | fentryid |
| 2 | idx_ssc_sla_sbsteridetails |  | fid |

---

## 共享服务账单-主表 t_tk_sla_serbill

- **表名称：** 共享服务账单-主表
- **表名：** t_tk_sla_serbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 4 | forgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsteriableoccamt | 回写已冲销金额 | numeric | 23 | 10 | √ | 0 | 回写已冲销金额 |
| 6 | famount | 暂估账单金额 | numeric | 23 | 10 | √ | 0 | 暂估账单金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbillamt | 结算账单金额 | numeric | 23 | 10 | √ | 0 | 结算账单金额 |
| 9 | fbillrecamt | 结算账单应收款金额 | numeric | 23 | 10 | √ | 0 | 结算账单应收款金额 |
| 10 | frecedamt | 已收款金额 | numeric | 23 | 10 | √ | 0 | 已收款金额 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsteriableamt | 可冲销余额 | numeric | 23 | 10 | √ | 0 | 可冲销余额 |
| 13 | fservicepriod | 服务结算期间 | int8 | 64 |  | √ | 0 | [服务结算期间 sla_serviceperiod](../som_files/sla_serviceperiod.md) |
| 14 | frecfreamt | 财务应收单冻结金额 | numeric | 23 | 10 | √ | 0 | 财务应收单冻结金额 |
| 15 | frelationorg | 共享服务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 17 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 18 | ftaxamt | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | fremark | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | ftallyorg | 共享中心所属核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fcustomer | 账单客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | fbillamtstd | 结算账单金额折本币 | numeric | 23 | 10 | √ | 0 | 结算账单金额折本币 |
| 24 | finvfreamt | 开票单冻结金额 | numeric | 23 | 10 | √ | 0 | 开票单冻结金额 |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 27 | frecoccamt | 财务应收单占用金额 | numeric | 23 | 10 | √ | 0 | 财务应收单占用金额 |
| 28 | finvoccamt | 开票单占用金额 | numeric | 23 | 10 | √ | 0 | 开票单占用金额 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fcurrency | 账单币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fcontractno | 合同编码 | varchar | 30 |  | √ | ' ' | 合同编码 |
| 33 | fbillrecamtstd | 结算账单应收款金额折本币 | numeric | 23 | 10 | √ | 0 | 结算账单应收款金额折本币 |
| 34 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 36 | fpayment | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 37 | famountstd | 暂估账单金额折本币 | numeric | 23 | 10 | √ | 0 | 暂估账单金额折本币 |
| 38 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 39 | finvedamt | 已开票金额 | numeric | 23 | 10 | √ | 0 | 已开票金额 |
| 40 | fsteriablefreamt | 回写冻结冲销金额 | numeric | 23 | 10 | √ | 0 | 回写冻结冲销金额 |
| 41 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 44 | fisperiod | 期初标识 | bpchar | 1 |  | √ | ' ' | 期初标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_sla_serbill |  | fbillno,fbilltype |
| 2 | pk_tk_sla_serbill |  | fid |

---

## 共享服务账单-多语言表 t_tk_sla_serbill_l

- **表名称：** 共享服务账单-多语言表
- **表名：** t_tk_sla_serbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 账单名称 | varchar | 50 |  | √ | ' ' | 账单名称 |
| 3 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_serbill_l |  | fpkid |
| 2 | idx_ssc_sla_serbill_l |  | fid,flocaleid |

---

## 共享服务账单-关联追踪表 t_tk_sla_serbill_tc

- **表名称：** 共享服务账单-关联追踪表
- **表名：** t_tk_sla_serbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sla_serbill_tc |  | fid |
| 2 | idx_tk_sla_serbill_tc_tid |  | ftid |
| 3 | idx_tk_sla_serbill_tc_tbill |  | ftbillid |
