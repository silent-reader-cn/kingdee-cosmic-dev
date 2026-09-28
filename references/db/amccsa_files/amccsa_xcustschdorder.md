# 销售计划协议变更单-amccsa_xcustschdorder

## 销售计划协议变更单-关联追踪表 t_amccsa_custschdorder_tc

- **表名称：** 销售计划协议变更单-关联追踪表
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

## 销售计划协议变更单-分表 t_amccsa_xcustschdorder_c

- **表名称：** 销售计划协议变更单-分表
- **表名：** t_amccsa_xcustschdorder_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiptplace | 收货地点 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 3 | fpaidbyid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fshippingaddress | 收货地址 | varchar | 300 |  |  | null | 收货地址 |
| 5 | fexchangemethod | 换算方式 | varchar | 8 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fsettlementmethodid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 8 | fsoldtoid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 9 | fcollectiontermid | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 10 | fcontactid | 联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 11 | fshiptoid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 13 | fpaymentmethod | 付款方式 | varchar | 8 |  | √ | ' ' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 14 | fconsigneeid | 收货联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 15 | fbilltoid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 17 | fincludetax | 含税 | bpchar | 1 |  | √ | ' ' | 含税 |
| 18 | fcontactaddress | 联系地址 | varchar | 300 |  |  | null | 联系地址 |
| 19 | fdeliverytype | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 20 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_xcustschdorder_c |  | fid |
| 2 | idx_t_amccsa_xcsorder_c_shp |  | fshiptoid |

---

## 订单明细-子表 t_amccsa_xcsorderentry

- **表名称：** 订单明细-子表
- **表名：** t_amccsa_xcsorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freferencecode | 客户参考值 | varchar | 50 |  | √ | ' ' | 客户参考值 |
| 3 | frssrls | 交货计划发放号 | varchar | 50 |  | √ | ' ' | 交货计划发放号 |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 6 | fsourceentryid | 订单物料分录ID | int8 | 64 |  | √ | 0 | 订单物料分录ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdiscountmode | 折扣方式 | varchar | 8 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 9 | fplansdpid | 预测SDP代码 | int8 | 64 |  | √ | 0 | SDP代码 amccsa_sdpcode |
| 10 | fmaterielmasterid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | ftracknoid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | fsecondaryattrv | 辅助属性值 | varchar | 512 |  |  | null | 辅助属性值 |
| 14 | flineremark | 行备注 | varchar | 50 |  | √ | ' ' | 行备注 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 16 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 |
| 17 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | fstdpackqty | 标准包装数量 | int4 | 32 |  | √ | 0 | 标准包装数量 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fcustpurorder | 客户采购订单号 | varchar | 50 |  | √ | ' ' | 客户采购订单号 |
| 22 | ftaxedprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 23 | fprodorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | frsslogic | 合并逻辑 | varchar | 8 |  | √ | ' ' | 合并逻辑,枚举: 0 :取要货计划 1 :取预测计划 2 :要货计划冲销预测计划 |
| 26 | flinemodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 28 | flinestartdate | 行起始日期 | timestamp | 0 |  |  | null | 行起始日期 |
| 29 | flinemodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 30 | fsecondaryattr | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 31 | fdocker | 交货地点 | varchar | 50 |  | √ | ' ' | 交货地点 |
| 32 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fshipsdpid | 要货SDP代码 | int8 | 64 |  | √ | 0 | SDP代码 amccsa_sdpcode |
| 34 | flineenddate | 行截止日期 | timestamp | 0 |  |  | null | 行截止日期 |
| 35 | fplanschdrls | 预测计划发放号 | varchar | 50 |  | √ | ' ' | 预测计划发放号 |
| 36 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fmodelyear | 年份型号 | varchar | 50 |  | √ | ' ' | 年份型号 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 40 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | flineclosestatus | 行关闭状态 | bpchar | 1 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 42 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 43 | fshipschdrls | 要货计划发放号 | varchar | 50 |  | √ | ' ' | 要货计划发放号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_xcsorderentry |  | fentryid |
| 2 | idx_t_amccsa_xcsorderentry_fid |  | fid,flineno |

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

## 订单明细-分表 t_amccsa_xcsorderentry_r

- **表名称：** 订单明细-分表
- **表名：** t_amccsa_xcsorderentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 3 | freplenishmentqty | 待补货数量 | numeric | 23 | 10 | √ | 0 | 待补货数量 |
| 4 | fsalesagencybaseqty | 委托代销已结算基本数量 | numeric | 23 | 10 | √ | 0 | 委托代销已结算基本数量 |
| 5 | faccuminvbaseqty | 累计已出库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已出库基本数量 |
| 6 | faccumstartdate | 累计数起始日 | timestamp | 0 |  |  | null | 累计数起始日 |
| 7 | freplenishbaseqty | 待补货基本数量 | numeric | 23 | 10 | √ | 0 | 待补货基本数量 |
| 8 | faccuminvqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0 | 累计已出库数量 |
| 9 | faccumconfirmamount | 累计已确认金额 | numeric | 23 | 10 | √ | 0 | 累计已确认金额 |
| 10 | faccumdeliqty | 累计已发货通知数量 | numeric | 23 | 10 | √ | 0 | 累计已发货通知数量 |
| 11 | faccumbackqty | 累计已退库数量 | numeric | 23 | 10 | √ | 0 | 累计已退库数量 |
| 12 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 13 | faccumconfirmqty | 累计已确认数量 | numeric | 23 | 10 | √ | 0 | 累计已确认数量 |
| 14 | fsalesagencyqty | 委托代销已结算数量 | numeric | 23 | 10 | √ | 0 | 委托代销已结算数量 |
| 15 | faccumrebackbaseqty | 累计售出可退基本数量 | numeric | 23 | 10 | √ | 0 | 累计售出可退基本数量 |
| 16 | faccumbackbaseqty | 累计已退库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已退库基本数量 |
| 17 | faccumaramount | 累计应收金额 | numeric | 23 | 10 | √ | 0 | 累计应收金额 |
| 18 | faccumconfirmbaseqty | 累计已确认基本数量 | numeric | 23 | 10 | √ | 0 | 累计已确认基本数量 |
| 19 | faccumrebackqty | 累计售出可退数量 | numeric | 23 | 10 | √ | 0 | 累计售出可退数量 |
| 20 | faccumjoinpriceqty | 累计应收数量 | numeric | 23 | 10 | √ | 0 | 累计应收数量 |
| 21 | faccumbasearqty | 累计应收基本数量 | numeric | 23 | 10 | √ | 0 | 累计应收基本数量 |
| 22 | faccumdelibaseqty | 累计已发货通知基本数量 | numeric | 23 | 10 | √ | 0 | 累计已发货通知基本数量 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | faccumclosqty | 累计结转已出库数量 | numeric | 23 | 10 | √ | 0 | 累计结转已出库数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_xcsorderentry_r |  | fentryid |
| 2 | idx_t_amccsa_xcsordentry_r_fid |  | fid |

---

## 销售计划协议变更单-反写记录表 t_amccsa_custschdorder_wb

- **表名称：** 销售计划协议变更单-反写记录表
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

## 销售计划协议变更单-主表 t_amccsa_xcustschdorder

- **表名称：** 销售计划协议变更单-主表
- **表名：** t_amccsa_xcustschdorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsourcebillentity | 源单实体 | varchar | 50 |  | √ | ' ' | 源单实体 |
| 4 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fdeliverycalendar | 交货计划日历选项 | varchar | 8 |  | √ | ' ' | 交货计划日历选项,枚举: 0 :使用客户日历 1 :不使用客户日历 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 D :原始源单 |
| 10 | fenddate | 订单截止日期 | timestamp | 0 |  |  | null | 订单截止日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsrcbillstatus | 订单状态 | bpchar | 1 |  | √ | ' ' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fsdpedigroup | EDI报文标准 | varchar | 8 |  | √ | ' ' | EDI报文标准,枚举: 0 :EDIFACT 1 :X12 2 :其他 |
| 14 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fdefaultqtymethod | 默认数量录入方式 | varchar | 8 |  | √ | ' ' | 默认数量录入方式,枚举: 0 :累计值 1 :净值 |
| 17 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 18 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillno | 销售计划协议编号 | varchar | 50 |  | √ | ' ' | 销售计划协议编号 |
| 20 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 21 | fremark | 备注 | varchar | 510 |  |  | null | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | ' ' | 初始化单据 |
| 27 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | freason | 变更原因 | varchar | 510 |  | √ | ' ' | 变更原因 |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 32 | fchangebillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 33 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 34 | fstartdate | 订单起始日期 | timestamp | 0 |  |  | null | 订单起始日期 |
| 35 | fvalidstatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 36 | fbizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 37 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 39 | fplandatetype | 计划日期类型 | varchar | 8 |  | √ | ' ' | 计划日期类型,枚举: 0 :以到货日期为准 1 :以发货日期为准 |
| 40 | fdaysdelivery | 运输天数 | int4 | 32 |  | √ | 0 | 运输天数 |
| 41 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_xcsorder_org |  | forgid |
| 2 | pk_t_amccsa_xcustschdorder |  | fid |
