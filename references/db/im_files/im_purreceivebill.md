# 收料通知单-im_purreceivebill

## 收料通知单-关联追踪表 t_im_purrecbill_tc

- **表名称：** 收料通知单-关联追踪表
- **表名：** t_im_purrecbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purrec_tc_ftbidtid |  | ftbillid,ftid |
| 2 | idx_im_purrecbill_tc_tid |  | ftid |
| 3 | idx_im_purrecbill_tc_tbill |  | ftbillid |
| 4 | t_im_purrecbill_tc_pkey |  | fid |

---

## 物料明细-子表 t_im_purrecbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_purrecbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fexpectcompletedate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 9 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 10 | fleftinspqty | 未送检数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未送检数量 |
| 11 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 12 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 13 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 19 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fisinspect | 来料检验 | bpchar | 1 |  | √ | '0' | 来料检验 |
| 22 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 23 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 24 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 25 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 26 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 30 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 32 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 35 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 36 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 37 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 38 | fprovideraddress | 供货地址 | varchar | 512 |  | √ | ' ' | 供货地址 |
| 39 | finsporg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 41 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 42 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 43 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 44 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 45 | ftotalinspqty | 已送检数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已送检数量 |
| 46 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 47 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 48 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 49 | ftotalunqualreturnbaseqty | 不合格已退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格已退货基本数量 |
| 50 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 51 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 53 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 54 | ftaxrate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 55 | fentryinvschemeid | fentryinvschemeid | int8 | 64 |  | √ | 0 |  |
| 56 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 57 | fentrydc | fentrydc | varchar | 5 |  | √ | ' ' |  |
| 58 | fbasictransquantity | 关联运输基本数量 | numeric | 23 | 10 |  | null | 关联运输基本数量 |
| 59 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 60 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 61 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 62 | fleftinspbaseqty | 未送检基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未送检基本数量 |
| 63 | femrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 64 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 65 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 66 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 67 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 68 | fleftunqualreturnqty | 不合格未退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格未退货数量 |
| 69 | fleftunqualreturnbaseqty | 不合格未退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格未退货基本数量 |
| 70 | ftotalinspbaseqty | 已送检基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已送检基本数量 |
| 71 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 72 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: A :合格退货 B :不合格退货 |
| 73 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 74 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 75 | freturnmaterialtype | 退料类型 | bpchar | 1 |  | √ | '0' | 退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 76 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 77 | ftransquantity | 关联运输数量 | numeric | 23 | 10 |  | null | 关联运输数量 |
| 78 | fhasgenapbusbill | 已生成暂估应付单 | bpchar | 1 |  | √ | '0' | 已生成暂估应付单 |
| 79 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 80 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 81 | frowclosestatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 82 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 83 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 84 | fpurunitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 85 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 86 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 87 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 88 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 89 | ftotalunqualreturnqty | 不合格已退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格已退货数量 |
| 90 | fprovidersupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 91 | ffloatingconversion | 浮动换算 | bpchar | 1 |  | √ | '0' | 浮动换算 |
| 92 | fpurqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 93 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 94 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 95 | fk_bj73_textfield | requid | varchar | 50 |  | √ | ' ' | requid |
| 96 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 97 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 98 | furgent | 是否加急 | bpchar | 1 |  | √ | '0' | 是否加急 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purrecbillentry_pkey |  | fentryid |
| 2 | idx_im_purrecbill_e_mmt |  | fmaterialmasterid |
| 3 | idx_im_purrecbillentry |  | fid |
| 4 | idx_im_purrecbill_e_ow |  | fownerid |
| 5 | idx_im_purrecbill_e_wh |  | fwarehouseid |

---

## 收料通知单-主表 t_im_purrecbill

- **表名称：** 收料通知单-主表
- **表名：** t_im_purrecbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fk_bj73_basedatafield | 使用部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 4 | forgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 10 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 11 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 14 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 17 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 20 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | ftraderouteid | 贸易路线 | int8 | 64 |  | √ | 0 | [贸易路线 sbs_traderoute](../sbs_files/sbs_traderoute.md) |
| 22 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 25 | fbizdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 30 | fhasapbusbill | 是否生成暂估应付单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应付单 |
| 31 | fendbill | 尾单 | bpchar | 1 |  | √ | '0' | 尾单 |
| 32 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | fbizoperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 34 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 35 | fquotation | 换算方式 | varchar | 50 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 39 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 40 | fisimport | 进口 | bpchar | 1 |  | √ | '0' | 进口 |
| 41 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 42 | fdeclareformed | 已生成报关单 | bpchar | 1 |  | √ | '0' | 已生成报关单 |
| 43 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fstep | 当前步骤 | int4 | 32 |  | √ | 0 | 当前步骤 |
| 46 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 51 | fbizoperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 52 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 53 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 54 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :已关闭 |
| 55 | flogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 56 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 57 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 58 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 59 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | facceptancestatus | 验收状态 | bpchar | 1 |  | √ | '0' | 验收状态,枚举: 0 :待验收 1 :已验收 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purrecbill_pkey |  | fid |
| 2 | idx_im_purrecbill_forgbillno |  | fbillno,forgid |
| 3 | idx_im_purrecbill_supp |  | fsupplierid |
| 4 | idx_im_purrecbill_org |  | forgid |
| 5 | idx_im_purrecbill_biztorgno |  | fbiztime,forgid,fbillno |
| 6 | idx_im_prbill_bktorgno |  | fbookdate,forgid,fbillno |

---

## 收料通知单-反写记录表 t_im_purrecbill_wb

- **表名称：** 收料通知单-反写记录表
- **表名：** t_im_purrecbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purrecbill_wb_pkey |  | fentryid |
| 2 | idx_im_purrecbill_wb_fk |  | fid |

---

## 收料通知单-多语言表 t_im_purrecbill_l

- **表名称：** 收料通知单-多语言表
- **表名：** t_im_purrecbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purrecbill_l |  | fid,flocaleid |
| 2 | t_im_purrecbill_l_pkey |  | fpkid |

---

## 物料明细-多语言表 t_im_purrecbillentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_im_purrecbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprovideraddress | 供货地址 | varchar | 512 |  | √ | ' ' | 供货地址 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purrecbille_l_id_local |  | fentryid,flocaleid |
| 2 | t_im_purrecbillentry_l_pkey |  | fpkid |

---

## 物料明细-分表 t_im_purrecbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_purrecbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconcessionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | furgentjoinbaseqty | 紧急放行关联基本数量 | numeric | 23 | 10 | √ | 0 | 紧急放行关联基本数量 |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库基本数量 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 8 | funqualifiedunit3rd | funqualifiedunit3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽基本数量 |
| 10 | ftotalreturnqty | 合格已退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格已退货数量 |
| 11 | fqualifiedunit2nd | 合格数量(主辅单位) | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量(主辅单位) |
| 12 | fjoinstockdamageqty | 关联入库采购损耗数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗数量 |
| 13 | fremaininvqty | 未入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未入库数量 |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 15 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 16 | fjoinpriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 17 | fremainpurqty | 未转固数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未转固数量 |
| 18 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 19 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 20 | facceptanceentrystatus | 验收状态 | bpchar | 1 |  | √ | '0' | 验收状态,枚举: 0 :待验收 1 :已验收 |
| 21 | frejectdiscountamount | 不良品折让金额 | numeric | 23 | 10 | √ | 0 | 不良品折让金额 |
| 22 | fjoinbusqty | 暂估应付数量 | numeric | 23 | 10 | √ | 0 | 暂估应付数量 |
| 23 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 25 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量 |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 28 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 29 | fjoinstockdamagebaseqty | 关联入库采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗基本数量 |
| 30 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 31 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽基本数量 |
| 32 | fremainpurbaseqty | 未转固基本数量 | numeric | 23 | 10 | √ | 0 | 未转固基本数量 |
| 33 | fjoinbusunwoffqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 34 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 35 | fremainjoinpricebaseqty | 剩余应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付基本数量 |
| 36 | fremainjoinpriceqty | 剩余应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付数量 |
| 37 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fjoinbusbaseqty | 暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量 |
| 40 | fpurbillentryid | 采购订单行号 | int8 | 64 |  | √ | 0 | 采购订单行号 |
| 41 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 42 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 43 | funqualifiedunit2nd | 不合格数量(主辅单位) | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量(主辅单位) |
| 44 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 45 | furgentjoinqty | 紧急放行关联数量 | numeric | 23 | 10 | √ | 0 | 紧急放行关联数量 |
| 46 | fjoinrejectdiscountamount | 关联不良品折让金额 | numeric | 23 | 10 | √ | 0 | 关联不良品折让金额 |
| 47 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 48 | fjoinpricebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付基本数量 |
| 49 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 50 | fconcessionbaseqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收基本数量 |
| 51 | fdamagebaseqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 52 | ftotalreturnbaseqty | 合格已退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格已退货基本数量 |
| 53 | fqualifiedunit3rd | fqualifiedunit3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | fremainreturnbaseqty | 合格未退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格未退货基本数量 |
| 55 | fpurbillnumber | fpurbillnumber | int8 | 64 |  | √ | 0 |  |
| 56 | fverifyqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 57 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 58 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 59 | fjoininvqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 60 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 61 | fpurchasedbaseqty | 已转固基本数量 | numeric | 23 | 10 | √ | 0 | 已转固基本数量 |
| 62 | fpurchasedqty | 已转固数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已转固数量 |
| 63 | fqualifiedbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格基本数量 |
| 64 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 65 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 66 | funqualifiedbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格基本数量 |
| 67 | fremaininvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未入库基本数量 |
| 68 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 69 | fpurorderbillnumber | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 70 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 71 | facceptancedate | 验收日期 | timestamp | 0 |  |  | null | 验收日期 |
| 72 | fpurchasedamount | 已转固价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已转固价税合计(本位币) |
| 73 | fjoininvbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 74 | fremainpuramount | 未转固价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未转固价税合计(本位币) |
| 75 | fremainreturnqty | 合格未退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格未退货数量 |
| 76 | fdamageqty | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 77 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |
| 78 | fmftordernumber | 委外工单编号 | varchar | 100 |  | √ | ' ' | 委外工单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purrecbillentry_r_pkey |  | fentryid |
| 2 | idx_pm_purrecbillentry_r |  | fid |

---

## 关联子实体-子表 t_im_purrecbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_purrecbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purrecbill_lk_fk |  | fid |
| 2 | t_im_purrecbill_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_im_purrecbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_purrecbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purrecbillentry_lk_fk |  | fentryid |
| 2 | t_im_purrecbillentry_lk_pkey |  | fpkid |
