# 销售计划协议-amccsa_custschdorder

## 销售计划协议-分表 t_amccsa_custschdorder_c

- **表名称：** 销售计划协议-分表
- **表名：** t_amccsa_custschdorder_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiptplace | 收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 3 | fpaidbyid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 4 | fshippingaddress | 收货地址 | varchar | 300 |  |  | null | 收货地址 |
| 5 | fexchangemethod | 换算方式 | varchar | 8 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fsettlementmethodid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 8 | fsoldtoid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 9 | fcollectiontermid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 10 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 11 | fcontactid | 联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 12 | fshiptoid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 13 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 14 | fpaymentmethod | 付款方式 | varchar | 8 |  | √ | ' ' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 15 | fconsigneeid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 16 | fbilltoid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 18 | fincludetax | 含税 | bpchar | 1 |  | √ | ' ' | 含税 |
| 19 | fcontactaddress | 联系地址 | varchar | 300 |  |  | null | 联系地址 |
| 20 | fdeliverytype | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 21 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_custschdorder_c |  | fid |
| 2 | idx_t_amccsa_csorder_c_shp |  | fshiptoid |

---

## 订单明细-分表 t_amccsa_csorderentry_r

- **表名称：** 订单明细-分表
- **表名：** t_amccsa_csorderentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 3 | freplenishmentqty | 待补货数量 | numeric | 23 | 10 | √ | 0 | 待补货数量 |
| 4 | fsalesagencybaseqty | 委托代销已结算基本数量 | numeric | 23 | 10 | √ | 0 | 委托代销已结算基本数量 |
| 5 | fpredemandbaseqty | 预计总需求基本数量 | numeric | 23 | 10 | √ | 0 | 预计总需求基本数量 |
| 6 | faccumstartdate | 累计数起始日 | timestamp | 0 |  |  | null | 累计数起始日 |
| 7 | faccumconfirmamount | 累计已确认金额 | numeric | 23 | 10 | √ | 0 | 累计已确认金额 |
| 8 | faccumdeliqty | 累计已发货通知数量 | numeric | 23 | 10 | √ | 0 | 累计已发货通知数量 |
| 9 | faccumbackqty | 累计已退库数量 | numeric | 23 | 10 | √ | 0 | 累计已退库数量 |
| 10 | faccumconfirmqty | 累计已确认数量 | numeric | 23 | 10 | √ | 0 | 累计已确认数量 |
| 11 | faccumrebackbaseqty | 累计售出可退基本数量 | numeric | 23 | 10 | √ | 0 | 累计售出可退基本数量 |
| 12 | faccumbackbaseqty | 累计已退库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已退库基本数量 |
| 13 | faccumaramount | 累计应收金额 | numeric | 23 | 10 | √ | 0 | 累计应收金额 |
| 14 | faccumconfirmbaseqty | 累计已确认基本数量 | numeric | 23 | 10 | √ | 0 | 累计已确认基本数量 |
| 15 | faccumjoinpriceqty | 累计应收数量 | numeric | 23 | 10 | √ | 0 | 累计应收数量 |
| 16 | faccumbasearqty | 累计应收基本数量 | numeric | 23 | 10 | √ | 0 | 累计应收基本数量 |
| 17 | faccumclosqty | 累计结转已出库数量 | numeric | 23 | 10 | √ | 0 | 累计结转已出库数量 |
| 18 | faccuminvbaseqty | 累计已出库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已出库基本数量 |
| 19 | freplenishbaseqty | 待补货基本数量 | numeric | 23 | 10 | √ | 0 | 待补货基本数量 |
| 20 | faccuminvqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0 | 累计已出库数量 |
| 21 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 22 | fsalesagencyqty | 委托代销已结算数量 | numeric | 23 | 10 | √ | 0 | 委托代销已结算数量 |
| 23 | faccumrebackqty | 累计售出可退数量 | numeric | 23 | 10 | √ | 0 | 累计售出可退数量 |
| 24 | fpredemandqty | 预计总需求数量 | numeric | 23 | 10 | √ | 0 | 预计总需求数量 |
| 25 | faccumdelibaseqty | 累计已发货通知基本数量 | numeric | 23 | 10 | √ | 0 | 累计已发货通知基本数量 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_csorderentry_r |  | fentryid |
| 2 | idx_t_amccsa_csordentry_r_fid |  | fid |

---

## 销售计划协议-主表 t_amccsa_custschdorder

- **表名称：** 销售计划协议-主表
- **表名：** t_amccsa_custschdorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fdeliverycalendar | 发货计划日历选项 | varchar | 8 |  | √ | ' ' | 发货计划日历选项,枚举: 0 :使用客户日历 1 :不使用客户日历 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 8 | fenddate | 订单截止日期 | timestamp | 0 |  |  | null | 订单截止日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsdpedigroup | EDI报文标准 | varchar | 8 |  | √ | ' ' | EDI报文标准,枚举: 0 :EDIFACT 1 :X12 2 :其他 |
| 11 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 12 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 13 | fdefaultqtymethod | 默认数量录入方式 | varchar | 8 |  | √ | ' ' | 默认数量录入方式,枚举: 0 :累计值 1 :净值 |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 17 | fremark | 备注 | varchar | 510 |  |  | null | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | ' ' | 初始化单据 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 25 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 26 | fstartdate | 订单起始日期 | timestamp | 0 |  |  | null | 订单起始日期 |
| 27 | fisaccumulation | 累计制 | bpchar | 1 |  | √ | '0' | 累计制 |
| 28 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fplandatetype | 计划日期类型 | varchar | 8 |  | √ | ' ' | 计划日期类型,枚举: 0 :以到货日期为准 1 :以发货日期为准 |
| 30 | fdaysdelivery | 运输天数 | int4 | 32 |  | √ | 0 | 运输天数 |
| 31 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_custschdorder_org |  | forgid |
| 2 | pk_t_amccsa_custschdorder |  | fid |

---

## 销售计划协议-反写记录表 t_amccsa_custschdorder_wb

- **表名称：** 销售计划协议-反写记录表
- **表名：** t_amccsa_custschdorder_wb

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
| 1 | pk_amccsa_custschdorder_wb |  | fentryid |
| 2 | idx_amccsa_custschdorder_wb_fk |  | fid |

---

## 销售计划协议-关联追踪表 t_amccsa_custschdorder_tc

- **表名称：** 销售计划协议-关联追踪表
- **表名：** t_amccsa_custschdorder_tc

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
| 1 | idx_amccsa_custschdorder_tc_tbill |  | ftbillid |
| 2 | pk_amccsa_custschdorder_tc |  | fid |
| 3 | idx_amccsa_custschdorder_tc_tid |  | ftid |

---

## 关联子实体-子表 t_amccsa_csorderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_amccsa_csorderentry_lk

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
| 1 | pk_amccsa_csorderentry_lk |  | fpkid |
| 2 | idx_amccsa_csorderentry_lk_fk |  | fentryid |

---

## 订单明细-子表 t_amccsa_csorderentry

- **表名称：** 订单明细-子表
- **表名：** t_amccsa_csorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freferencecode | 客户参考值 | varchar | 50 |  | √ | ' ' | 客户参考值 |
| 3 | frssrls | 滚动发货计划发放号 | varchar | 50 |  | √ | ' ' | 滚动发货计划发放号 |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdiscountmode | 折扣方式 | varchar | 8 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 8 | fplansdpid | 预测SDP代码 | int8 | 64 |  | √ | 0 | [SDP代码 amccsa_sdpcode](../amccsa_files/amccsa_sdpcode.md) |
| 9 | fmaterielmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 11 | ftracknoid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 12 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 13 | fsecondaryattrv | 辅助属性值 | varchar | 512 |  |  | null | 辅助属性值 |
| 14 | flineremark | 行备注 | varchar | 50 |  | √ | ' ' | 行备注 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 |
| 17 | fcusmaterialid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 18 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fstdpackqty | 标准包装数量 | int4 | 32 |  | √ | 0 | 标准包装数量 |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fcustpurorder | 客户采购订单号 | varchar | 50 |  | √ | ' ' | 客户采购订单号 |
| 23 | ftaxedprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 24 | fprodorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | frsslogic | 合并逻辑 | varchar | 8 |  | √ | ' ' | 合并逻辑,枚举: 0 :取交货计划 1 :取预测计划 2 :交货计划冲销预测计划 |
| 27 | flinemodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | flinestartdate | 行起始日期 | timestamp | 0 |  |  | null | 行起始日期 |
| 30 | flinemodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 31 | fsecondaryattr | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 32 | fdocker | 交货地点 | varchar | 50 |  | √ | ' ' | 交货地点 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fshipsdpid | 交货SDP代码 | int8 | 64 |  | √ | 0 | [SDP代码 amccsa_sdpcode](../amccsa_files/amccsa_sdpcode.md) |
| 35 | flineenddate | 行截止日期 | timestamp | 0 |  |  | null | 行截止日期 |
| 36 | fplanschdrls | 客户预测计划发放号 | varchar | 50 |  | √ | ' ' | 客户预测计划发放号 |
| 37 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fmodelyear | 年份型号 | varchar | 50 |  | √ | ' ' | 年份型号 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 41 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | flineclosestatus | 行关闭状态 | bpchar | 1 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 43 | fshipschdrls | 客户交货计划发放号 | varchar | 50 |  | √ | ' ' | 客户交货计划发放号 |
| 44 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_csorderentry_fid |  | fid,flineno |
| 2 | pk_t_amccsa_csorderentry |  | fentryid |
