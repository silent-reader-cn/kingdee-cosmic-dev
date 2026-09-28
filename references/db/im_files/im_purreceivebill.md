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
| 3 | ftaxrate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 5 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 6 | fentryinvschemeid | fentryinvschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fexpectcompletedate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 11 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 13 | fleftinspqty | 未送检数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未送检数量 |
| 14 | fentrydc | fentrydc | varchar | 5 |  | √ | ' ' |  |
| 15 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 16 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 18 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fleftinspbaseqty | 未送检基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未送检基本数量 |
| 23 | femrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 24 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 25 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 27 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 28 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fleftunqualreturnqty | 不合格未退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格未退货数量 |
| 31 | fleftunqualreturnbaseqty | 不合格未退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格未退货基本数量 |
| 32 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 34 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 35 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 36 | fisinspect | 来料检验 | bpchar | 1 |  | √ | '0' | 来料检验 |
| 37 | ftotalinspbaseqty | 已送检基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已送检基本数量 |
| 38 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 39 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 40 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 41 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 42 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 43 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: A :合格退货 B :不合格退货 |
| 44 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 46 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 47 | freturnmaterialtype | 退料类型 | bpchar | 1 |  | √ | '0' | 退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 48 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 49 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 50 | fhasgenapbusbill | 已生成暂估应付单 | bpchar | 1 |  | √ | '0' | 已生成暂估应付单 |
| 51 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 52 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 53 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 54 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | frowclosestatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 56 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 57 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 58 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 59 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 60 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 61 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 62 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 63 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 64 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 65 | fpurunitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 66 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 67 | fprovideraddress | 供货地址 | varchar | 512 |  | √ | ' ' | 供货地址 |
| 68 | finsporg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 69 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 70 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 71 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 72 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 73 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 74 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 75 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 76 | ftotalunqualreturnqty | 不合格已退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格已退货数量 |
| 77 | ftotalinspqty | 已送检数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已送检数量 |
| 78 | fprovidersupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 79 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 80 | fpurqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 81 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 82 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 83 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 84 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 85 | ftotalunqualreturnbaseqty | 不合格已退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格已退货基本数量 |
| 86 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 87 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 88 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 89 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 90 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 91 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 92 | furgent | 是否加急 | bpchar | 1 |  | √ | '0' | 是否加急 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purrecbillentry_pkey |  | fentryid |
| 2 | idx_im_purrecbill_e_mmt |  | fmaterialmasterid |
| 3 | idx_im_purrecbill_e_ow |  | fownerid |
| 4 | idx_im_purrecbillentry |  | fid |
| 5 | idx_im_purrecbill_e_wh |  | fwarehouseid |

---

## 收料通知单-主表 t_im_purrecbill

- **表名称：** 收料通知单-主表
- **表名：** t_im_purrecbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | forgid | 收料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 10 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 13 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 16 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 17 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 18 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 21 | fbizdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 25 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 26 | fhasapbusbill | 是否生成暂估应付单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应付单 |
| 27 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fbizoperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 29 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 30 | fquotation | 换算方式 | varchar | 50 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 34 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 35 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 36 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 39 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 43 | fbizoperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 44 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 45 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 46 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :已关闭 |
| 47 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 48 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 49 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 50 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | facceptancestatus | 验收状态 | bpchar | 1 |  | √ | '0' | 验收状态,枚举: 0 :待验收 1 :已验收 |

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
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库基本数量 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 7 | funqualifiedunit3rd | funqualifiedunit3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽基本数量 |
| 9 | ftotalreturnqty | 合格已退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格已退货数量 |
| 10 | fqualifiedunit2nd | 合格数量(主辅单位) | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量(主辅单位) |
| 11 | fjoinstockdamageqty | 关联入库采购损耗数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗数量 |
| 12 | fremaininvqty | 未入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未入库数量 |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 14 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 15 | fjoinpriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 16 | fremainpurqty | 未转固数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未转固数量 |
| 17 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 18 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 19 | facceptanceentrystatus | 验收状态 | bpchar | 1 |  | √ | '0' | 验收状态,枚举: 0 :待验收 1 :已验收 |
| 20 | frejectdiscountamount | 不良品折让金额 | numeric | 23 | 10 | √ | 0 | 不良品折让金额 |
| 21 | fjoinbusqty | 暂估应付数量 | numeric | 23 | 10 | √ | 0 | 暂估应付数量 |
| 22 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 23 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 24 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量 |
| 25 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 26 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 27 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 28 | fjoinstockdamagebaseqty | 关联入库采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗基本数量 |
| 29 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 30 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽基本数量 |
| 31 | fremainpurbaseqty | 未转固基本数量 | numeric | 23 | 10 | √ | 0 | 未转固基本数量 |
| 32 | fjoinbusunwoffqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 33 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 34 | fremainjoinpricebaseqty | 剩余应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付基本数量 |
| 35 | fremainjoinpriceqty | 剩余应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付数量 |
| 36 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 38 | fjoinbusbaseqty | 暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量 |
| 39 | fpurbillentryid | 采购订单行号 | int8 | 64 |  | √ | 0 | 采购订单行号 |
| 40 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 41 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 42 | funqualifiedunit2nd | 不合格数量(主辅单位) | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量(主辅单位) |
| 43 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 44 | fjoinrejectdiscountamount | 关联不良品折让金额 | numeric | 23 | 10 | √ | 0 | 关联不良品折让金额 |
| 45 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 46 | fjoinpricebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付基本数量 |
| 47 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 48 | fconcessionbaseqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收基本数量 |
| 49 | fdamagebaseqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 50 | ftotalreturnbaseqty | 合格已退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格已退货基本数量 |
| 51 | fqualifiedunit3rd | fqualifiedunit3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fremainreturnbaseqty | 合格未退货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格未退货基本数量 |
| 53 | fpurbillnumber | fpurbillnumber | int8 | 64 |  | √ | 0 |  |
| 54 | fverifyqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 55 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 56 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 57 | fjoininvqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 58 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 59 | fpurchasedbaseqty | 已转固基本数量 | numeric | 23 | 10 | √ | 0 | 已转固基本数量 |
| 60 | fpurchasedqty | 已转固数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已转固数量 |
| 61 | fqualifiedbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格基本数量 |
| 62 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 63 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 64 | funqualifiedbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格基本数量 |
| 65 | fremaininvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未入库基本数量 |
| 66 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 67 | fpurorderbillnumber | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 68 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 69 | facceptancedate | 验收日期 | timestamp | 0 |  |  | null | 验收日期 |
| 70 | fpurchasedamount | 已转固价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已转固价税合计(本位币) |
| 71 | fjoininvbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 72 | fremainpuramount | 未转固价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未转固价税合计(本位币) |
| 73 | fremainreturnqty | 合格未退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格未退货数量 |
| 74 | fdamageqty | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 75 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |
| 76 | fmftordernumber | 委外工单编号 | varchar | 100 |  | √ | ' ' | 委外工单编号 |

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
