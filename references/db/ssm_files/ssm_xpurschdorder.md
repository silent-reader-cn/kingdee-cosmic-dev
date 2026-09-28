# 采购计划协议变更单-ssm_xpurschdorder

## 单据体-分表 t_ssm_xpurorderentry_r

- **表名称：** 单据体-分表
- **表名：** t_ssm_xpurorderentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceivedqty | 累计已入库数量 | numeric | 23 | 10 | √ | 0 | 累计已入库数量 |
| 3 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 4 | freceivedbaseqty | 累计已入库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已入库基本数量 |
| 5 | freceivedretbaseqty | 累计库存可退基本数量 | numeric | 23 | 10 | √ | 0 | 累计库存可退基本数量 |
| 6 | fasnretbaseqty | 累计收货可退基本数量 | numeric | 23 | 10 | √ | 0 | 累计收货可退基本数量 |
| 7 | faccumstartdate | 累计数起始日 | timestamp | 0 |  |  | null | 累计数起始日 |
| 8 | freturnqty | 累计已退库数量 | numeric | 23 | 10 | √ | 0 | 累计已退库数量 |
| 9 | fasnqty | 累计收货通知数量 | numeric | 23 | 10 | √ | 0 | 累计收货通知数量 |
| 10 | freturnbaseqty | 累计已退库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已退库基本数量 |
| 11 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 12 | fasnbaseqty | 累计收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 累计收货通知基本数量 |
| 13 | freceivedretqty | 累计库存可退数量 | numeric | 23 | 10 | √ | 0 | 累计库存可退数量 |
| 14 | fcarryoverqty | 累计结转已入库数量 | numeric | 23 | 10 | √ | 0 | 累计结转已入库数量 |
| 15 | fasnretqty | 累计收货可退数量 | numeric | 23 | 10 | √ | 0 | 累计收货可退数量 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ssm_xpurorderentry_r |  | fentryid |
| 2 | idx_t_ssm_xpcurorderentry_r |  | fid,fentryid |

---

## 采购计划协议变更单-主表 t_ssm_xpurschdorder

- **表名称：** 采购计划协议变更单-主表
- **表名：** t_ssm_xpurschdorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillentity | 源单实体 | varchar | 50 |  | √ | ' ' | 源单实体 |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fschedmonths | 计划月数 | int8 | 64 |  | √ | 0 | 计划月数 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fenddate | 订单截止日期 | timestamp | 0 |  |  | null | 订单截止日期 |
| 8 | fsrcbillstatus | 订单状态 | bpchar | 1 |  | √ | ' ' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 13 | fbillno | 采购计划协议编号 | varchar | 50 |  | √ | ' ' | 采购计划协议编号 |
| 14 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 17 | freason | 变更原因 | varchar | 510 |  | √ | ' ' | 变更原因 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fchangebillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 21 | fvalidstatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 22 | fstartdate | 订单起始日期 | timestamp | 0 |  |  | null | 订单起始日期 |
| 23 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | fshipsdp | SDP代码 | int8 | 64 |  | √ | 0 | [SDP代码 amccsa_sdpcode](../amccsa_files/amccsa_sdpcode.md) |
| 30 | fexchangemethod | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 31 | fschedweeks | 计划周数 | int8 | 64 |  | √ | 0 | 计划周数 |
| 32 | fscheddays | 计划日数 | int8 | 64 |  | √ | 0 | 计划日数 |
| 33 | fpaymenttermid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 34 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 35 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [采购价目表 pm_purpricelist](../pm_files/pm_purpricelist.md) |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fsdpedigroup | EDI报文标准 | varchar | 50 |  | √ | ' ' | EDI报文标准,枚举: 0 :EDIFACT 1 :X12 2 :其他 |
| 38 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 39 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 40 | ffirmdays | 计划固定日数 | int8 | 64 |  | √ | 0 | 计划固定日数 |
| 41 | fincludetax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 42 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fsafetydays | 安全日数 | int8 | 64 |  | √ | 0 | 安全日数 |
| 48 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 49 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 50 | fsettlementmethodid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 51 | fpaymode | 付款方式 | varchar | 50 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 52 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 53 | fbizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 54 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 55 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 56 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 57 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 58 | fprocureorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ssm_xpurschdorder_billno |  | fbillno,fid |
| 2 | pk_ssm_xpurschdorder |  | fid |

---

## 采购计划协议变更单-分表 t_ssm_xpurschdorder_s

- **表名称：** 采购计划协议变更单-分表
- **表名：** t_ssm_xpurschdorder_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffullfillsupplieraddr | 供货联系地址 | varchar | 512 |  | √ | ' ' | 供货联系地址 |
| 3 | faddress | 联系地址 | varchar | 512 |  | √ | ' ' | 联系地址 |
| 4 | ffullfillcontactid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 5 | ffullfillsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 6 | fcontactid | 联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 7 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 8 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ssm_xpurschdorder_s |  | fid |
| 2 | idx_t_xpurschdorder_s |  | ffullfillsupplierid |

---

## 单据体-子表 t_ssm_xpurorderentry

- **表名称：** 单据体-子表
- **表名：** t_ssm_xpurorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 单位折扣(率) | numeric | 23 | 2 | √ | 0 | 单位折扣(率) |
| 3 | frssrlsid | 滚动收货计划发放号 | int8 | 64 |  | √ | 0 | 滚动收货计划 ssm_require_schedule |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 5 | fsourceentryid | 订单物料分录ID | int8 | 64 |  | √ | 0 | 订单物料分录ID |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fplanschdrlsid | 供应商预测计划发放号 | int8 | 64 |  | √ | 0 | 供应商预测计划 ssm_plan_schedule |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmaterielmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 11 | fumid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | ftracknoid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fminorderqty | 单次起送量 | int8 | 64 |  | √ | 0 | 单次起送量 |
| 15 | flineremark | 行备注 | varchar | 50 |  | √ | ' ' | 行备注 |
| 16 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 19 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 20 | fshipschid | 最新供应商交货计划 | int8 | 64 |  | √ | 0 | 最新供应商交货计划 |
| 21 | fstdpackqty | 标准包装数量 | int8 | 64 |  | √ | 0 | 标准包装数量 |
| 22 | fbaseumid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fdemandorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | ftaxedprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 25 | fqcpflg | 来料检验 | bpchar | 1 |  | √ | '0' | 来料检验 |
| 26 | fdeliveraddress | 交货地址 | varchar | 512 |  | √ | ' ' | 交货地址 |
| 27 | fplanschid | 最新供应商预测计划 | int8 | 64 |  | √ | 0 | 最新供应商预测计划 |
| 28 | fdiscounttype | 折扣方式 | varchar | 8 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 29 | fshipschdrlsid | 供应商交货计划发放号 | int8 | 64 |  | √ | 0 | 供应商交货计划 ssm_ship_schedule |
| 30 | flinestartdate | 行起始日期 | timestamp | 0 |  |  | null | 行起始日期 |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | frequireschid | 最新滚动收货计划 | int8 | 64 |  | √ | 0 | 最新滚动收货计划 |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 36 | finvoiceorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 38 | flineenddate | 行截止日期 | timestamp | 0 |  |  | null | 行截止日期 |
| 39 | freceiveorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 41 | flineclosestatus | 行关闭状态 | bpchar | 1 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ssm_xpcurorderentry |  | flineno,fentryid |
| 2 | pk_ssm_xpurorderentry |  | fentryid |
| 3 | idx_ssm_xpurorderentry_fk |  | fid |
