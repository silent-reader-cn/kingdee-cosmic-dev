# 销售订单变更单-sm_xssalorder

## 销售订单变更单-主表 t_sm_xsalorder

- **表名称：** 销售订单变更单-主表
- **表名：** t_sm_xsalorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprereceiptamount | 已预收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预收金额 |
| 3 | fsrcbiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :正常 B :已作废 |
| 7 | fchangecanceler | 变更单作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fconsigngencrossorg | 委托代销生成跨组织发出 | bpchar | 1 |  | √ | '0' | 委托代销生成跨组织发出 |
| 11 | fsrcbillstatus | 订单单据状态 | varchar | 5 |  | √ | ' ' | 订单单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | forderstatus | 订单状态 | bpchar | 1 |  | √ | 'A' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货通知 E :已发货通知 F :部分出库 G :已出库 H :部分退货 I :已退货 J :部分应收 K :已应收 |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 15 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fversion | 版本号 | varchar | 20 |  | √ | ' ' | 版本号 |
| 19 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmarginlevel | 保证金比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 保证金比例(%) |
| 21 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 22 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 23 | fdiscountlistid | 折扣表 | int8 | 64 |  | √ | 0 | [销售折扣表 sm_salediscountlist](../sm_files/sm_salediscountlist.md) |
| 24 | freason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |
| 25 | ftraderouteid | 贸易路线 | int8 | 64 |  | √ | 0 | [贸易路线 sbs_traderoute](../sbs_files/sbs_traderoute.md) |
| 26 | freceiptamount | 已收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收金额 |
| 27 | fk_bj73_assistantfield1 | 业务活动 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 28 | fk_bj73_assistantfield2 | fk_bj73_assistantfield2 | int8 | 64 |  | √ | 0 |  |
| 29 | fbillsource | 单据来源 | bpchar | 1 |  | √ | 'A' | 单据来源,枚举: A :普通销售 B :移动销售 |
| 30 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 31 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 36 | fprojinvctrltype | 项目开票控制方式 | varchar | 50 |  | √ | ' ' | 项目开票控制方式,枚举: A :按数量控制 B :按金额控制 |
| 37 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 D :原始源单 |
| 38 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fisvirtualbill | 是否虚单 | bpchar | 1 |  | √ | '0' | 是否虚单 |
| 42 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 43 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 44 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 45 | funreceiptamount | 未收金额 | numeric | 23 | 10 | √ | 0 | 未收金额 |
| 46 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 47 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | factivestatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 50 | fcomment | 物流备注 | varchar | 512 |  |  | null | 物流备注 |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 53 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 54 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 56 | fdeliverywayid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 57 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 58 | fchangecancelstatus | 变更单作废状态 | varchar | 5 |  | √ | ' ' | 变更单作废状态,枚举: A :正常 B :已作废 |
| 59 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 60 | foutmargin | 转出保证金 | numeric | 23 | 10 | √ | 0 | 转出保证金 |
| 61 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 62 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 63 | favailablemargin | 可用保证金 | numeric | 23 | 10 | √ | 0 | 可用保证金 |
| 64 | frelatemargin | 关联保证金 | numeric | 23 | 10 | √ | 0 | 关联保证金 |
| 65 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 66 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 67 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 68 | freceiveaddress | 收货地址 | varchar | 512 |  |  | null | 收货地址 |
| 69 | fcarrierid | 承运方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 70 | faddress | 客户联系地址 | varchar | 512 |  |  | null | 客户联系地址 |
| 71 | fsourcebillentity | 源单实体 | varchar | 36 |  | √ | ' ' | 源单实体 |
| 72 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 73 | flocation | 交货地点 | varchar | 255 |  |  | null | 交货地点 |
| 74 | fassociatemargin | 已收保证金 | numeric | 23 | 10 | √ | 0.0000000000 | 已收保证金 |
| 75 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 76 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 77 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 78 | ftradestatus | 贸易转换状态 | bpchar | 1 |  | √ | ' ' | 贸易转换状态,枚举: 0 :未完成 1 :已完成 |
| 79 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 80 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 81 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 82 | fmpmrecmethod | 项目收入确认方式 | varchar | 50 |  | √ | ' ' | 项目收入确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 83 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 84 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 85 | fdescountryid | 目的国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 86 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 87 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 88 | flinkmanid | 联系人（弃用） | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 89 | fk_bj73_assistantfield | 订单类型 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 90 | flinkaddressf7 | 客户联系地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 91 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 92 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 93 | fk_bj73_datetimefield | fk_bj73_datetimefield | timestamp | 0 |  |  | null |  |
| 94 | fk_bj73_textfield4 | 考核大区 | varchar | 50 |  | √ | ' ' | 考核大区 |
| 95 | fsrcbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 96 | fk_bj73_textfield5 | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 97 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 98 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 99 | fk_bj73_textfield2 | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 100 | fendbill | 尾单 | bpchar | 1 |  | √ | '0' | 尾单 |
| 101 | fk_bj73_textfield3 | 考核省区 | varchar | 50 |  | √ | ' ' | 考核省区 |
| 102 | fbiztime | 订单日期(封存) | timestamp | 0 |  |  | null | 订单日期(封存) |
| 103 | fk_bj73_textfield1 | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 104 | factiverid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 105 | fsrccountryid | 装运国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 106 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 107 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 108 | fmargin | 应收保证金 | numeric | 23 | 10 | √ | 0.0000000000 | 应收保证金 |
| 109 | fassrefundmargin | 已退保证金 | numeric | 23 | 10 | √ | 0.0000000000 | 已退保证金 |
| 110 | fstep | 当前步骤 | int4 | 32 |  | √ | 0 | 当前步骤 |
| 111 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 112 | fchangecanceldate | 变更单作废日期 | timestamp | 0 |  |  | null | 变更单作废日期 |
| 113 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 114 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 115 | fclosemanual | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 116 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 117 | fisexport | 出口 | bpchar | 1 |  | √ | '0' | 出口 |
| 118 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 119 | fbizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 120 | ftransportmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 121 | fk_bj73_textfield | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 122 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 123 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 124 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_uniq_xsalorder_billnoorg |  | fbillno,forgid |
| 2 | t_sm_xsalorder_pkey |  | fid |

---

## 销售订单变更单-多语言表 t_sm_xsalorder_l

- **表名称：** 销售订单变更单-多语言表
- **表名：** t_sm_xsalorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 物流备注 | varchar | 512 |  |  | ' ' | 物流备注 |
| 3 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_xsalorder_l_pkey |  | fpkid |
| 2 | idx_sm_xsalesorder_l |  | fid,flocaleid |

---

## 销售订单变更单-分表 t_sm_xsalorder_m

- **表名称：** 销售订单变更单-分表
- **表名：** t_sm_xsalorder_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccmexcessamount | 预估信用超标额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标额度 |
| 3 | fccmexcessdays | 预估信用超标天数 | numeric | 23 | 10 | √ | 0 | 预估信用超标天数 |
| 4 | fccmexcessoveramount | 预估信用超标逾期额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标逾期额度 |
| 5 | fccmexcessbillamount | 预估信用超标单笔限额 | numeric | 23 | 10 | √ | 0 | 预估信用超标单笔限额 |
| 6 | fccmupdatetime | 预估信用超标时点 | timestamp | 0 |  |  | null | 预估信用超标时点 |
| 7 | fccmunsettlecount | 信用未结批数 | int4 | 32 |  | √ | 0 | 信用未结批数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_xsalorder_m |  | fid |
| 2 | idx_sm_xsalorder_m_t |  | fccmupdatetime |

---

## 销售订单变更单-分表 t_sm_xsalorder_c

- **表名称：** 销售订单变更单-分表
- **表名：** t_sm_xsalorder_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | faddress | varchar | 512 |  |  | null |  |
| 3 | fk_bj73_datetimefield | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 4 | fk_bj73_datetimefield1 | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 5 | flocation | flocation | varchar | 255 |  |  | null |  |
| 6 | fdeliverywayid | fdeliverywayid | int8 | 64 |  | √ | 0 |  |
| 7 | freclinkmanid | freclinkmanid | int8 | 64 |  | √ | 0 |  |
| 8 | fk_bj73_timefield | fk_bj73_timefield | int4 | 32 |  | √ | '-1' |  |
| 9 | fpayingcustomerid | fpayingcustomerid | int8 | 64 |  | √ | 0 |  |
| 10 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 11 | fsettlecustomerid | fsettlecustomerid | int8 | 64 |  | √ | 0 |  |
| 12 | freccustomerid | freccustomerid | int8 | 64 |  | √ | 0 |  |
| 13 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 14 | freceiveaddress | freceiveaddress | varchar | 512 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xsalesorder_c_cusid |  | fcustomerid |
| 2 | t_sm_xsalorder_c_pkey |  | fid |

---

## 关联子实体-子表 t_sm_salorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_salorder_lk

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
| 1 | idx_sm_salorder_lk_fk |  | fid |
| 2 | t_sm_salorder_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_sm_salorderrpentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_salorderrpentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salorderrpentry_lk_fk |  | fentryid |
| 2 | t_sm_salorderrpentry_lk_pkey |  | fpkid |

---

## 物料明细-子表 t_sm_xsalorderentry

- **表名称：** 物料明细-子表
- **表名：** t_sm_xsalorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货超发比率(%) |
| 3 | fexpectqtydate | 获取可发量日期 | timestamp | 0 |  |  | null | 获取可发量日期 |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdeliverratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货欠发比率(%) |
| 8 | fprojectconfqty | 已确认项目服务数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务数量 |
| 9 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 11 | fmpmopportno | 商机号 | int8 | 64 |  | √ | 0 | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 12 | foldcusmaterialname | 历史客户物料名称 | varchar | 255 |  | √ | ' ' | 历史客户物料名称 |
| 13 | foldcusmaterialmod | 历史客户物料规格型号 | varchar | 255 |  | √ | ' ' | 历史客户物料规格型号 |
| 14 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 15 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 17 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 18 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fmaterialmasterid |  | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 23 | fmaterialinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 24 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 26 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 31 | fprojassinvoicebaseqty | 关联项目开票申请基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请基本数量 |
| 32 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 33 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 34 | fmaterialgroup | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 35 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 36 | fprojectinvoicedbaseqty | 项目已申请开票基本数量 | numeric | 23 | 10 | √ | 0 | 项目已申请开票基本数量 |
| 37 | fprojassinvoiceqty | 关联项目开票申请数量 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请数量 |
| 38 | fk_bj73_qtyfield1 | 未出库数量 | numeric | 23 | 10 |  | null | 未出库数量 |
| 39 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 40 | fdeliverqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限数量 |
| 41 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 42 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 43 | fk_bj73_custombasedatafield | fk_bj73_custombasedatafield | int8 | 64 |  | √ | 0 |  |
| 44 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 45 | fdeliverdelaydays | 允许延迟天数 | int4 | 32 |  | √ | 0 | 允许延迟天数 |
| 46 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fsettledeptid | 结算部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 49 | fcorebillrowno | 核心单据行号(封存) | int8 | 64 |  | √ | 0 | 核心单据行号(封存) |
| 50 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 51 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 52 | fprojectinvoicedqty | 项目已申请开票数量 | numeric | 23 | 10 | √ | 0 | 项目已申请开票数量 |
| 53 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 54 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 55 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 56 | flogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 57 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 58 | fdeliverqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限数量 |
| 59 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 60 | fmatchdiscountlistid | 行折扣表 | int8 | 64 |  | √ | 0 | [销售折扣表 sm_salediscountlist](../sm_files/sm_salediscountlist.md) |
| 61 | fk_bj73_pricefield | 销售参考价 | numeric | 23 | 10 |  | null | 销售参考价 |
| 62 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 63 | fprojectconfbaseqty | 已确认项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务基本数量 |
| 64 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 |
| 65 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 66 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 67 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 68 | fdeliveradvdays | 允许提前天数 | int4 | 32 |  | √ | 0 | 允许提前天数 |
| 69 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 70 | fdeliverbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限基本数量 |
| 71 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 72 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 73 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 74 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 75 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 76 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 77 | foldcusmaterialnum | 历史客户物料编码 | varchar | 255 |  | √ | ' ' | 历史客户物料编码 |
| 78 | fexpectqty | 预计可发量 | numeric | 23 | 10 | √ | 0 | 预计可发量 |
| 79 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 80 | fprojectassqty | 关联项目服务数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务数量 |
| 81 | fprojectassbaseqty | 关联项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务基本数量 |
| 82 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  | √ | ' ' | 尾差调整日志 |
| 83 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 84 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 85 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 86 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 87 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 88 | fcusmaterialmod | fcusmaterialmod | varchar | 50 |  | √ | ' ' |  |
| 89 | fk_bj73_materielfield1 | fk_bj73_materielfield1 | int8 | 64 |  | √ | 0 |  |
| 90 | fisprojassociated | 是否关联立项 | bpchar | 1 |  | √ | '0' | 是否关联立项 |
| 91 | freturntype | 退补类型 | varchar | 5 |  | √ | ' ' | 退补类型,枚举: 1 :退回 2 :补货 |
| 92 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 93 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 94 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 95 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 96 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 97 | fminorderbaseqty | 起销量(基本) | numeric | 23 | 10 | √ | 0.0000000000 | 起销量(基本) |
| 98 | fmatchpricelist | 行价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 99 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 100 | fmaterialname | 物料名称(历史) | varchar | 800 |  | √ | ' ' | 物料名称(历史) |
| 101 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 102 | fk_bj73_textfield6 | fk_bj73_textfield6 | varchar | 50 |  | √ | ' ' |  |
| 103 | fishidden | 隐藏标识 | bpchar | 1 |  | √ | '0' | 隐藏标识 |
| 104 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 105 | fk_bj73_materielfield | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 106 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 107 | fentrystatus | fentrystatus | varchar | 5 |  | √ | ' ' |  |
| 108 | fk_bj73_qtyfield | 未发货数量 | numeric | 23 | 10 |  | null | 未发货数量 |
| 109 | fissuedqty | fissuedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 110 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 111 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 112 | fcorebillno | 核心单据编号(封存) | varchar | 80 |  | √ | ' ' | 核心单据编号(封存) |
| 113 | fproorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 114 | fk_bj73_materialmasterid | fk_bj73_materialmasterid | int8 | 64 |  | √ | 0 |  |
| 115 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 116 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 117 | frowterminatemanual | 行手工终止 | bpchar | 1 |  | √ | '0' | 行手工终止 |
| 118 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 119 | fdeliverbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限基本数量 |
| 120 | fsettleamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 121 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 122 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 123 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 124 | fdeliverydate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 125 | fcusmaterialname | fcusmaterialname | varchar | 50 |  | √ | ' ' |  |
| 126 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 127 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 128 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xsalesorderentry_fid |  | fid |
| 2 | t_sm_xsalorderentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_sm_salorderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_salorderentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_salorderentry_lk_pkey |  | fpkid |
| 2 | idx_sm_salorderentry_lk_fk |  | fentryid |

---

## 收款计划-子表 t_sm_xsalorderrpentry

- **表名称：** 收款计划-子表
- **表名：** t_sm_xsalorderrpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 3 | fneedrecadvance | 是否预收 | bpchar | 1 |  | √ | '0' | 是否预收 |
| 4 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 5 | frpbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frpmilestone | 里程碑 | varchar | 50 |  | √ | ' ' | 里程碑 |
| 8 | frecsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | frpmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 10 | frpcontract | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 11 | frelbillno | 关联单号 | varchar | 50 |  | √ | ' ' | 关联单号 |
| 12 | frecadvancerate | 应收比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应收比例(%) |
| 13 | frecamount | 已收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收金额 |
| 14 | frpexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 15 | funremainamount | 未关联收款金额 | numeric | 23 | 10 | √ | 0 | 未关联收款金额 |
| 16 | frpmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 17 | frpprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 18 | fcontrolbyactualprerec | 按实际预收控制发货 | bpchar | 1 |  | √ | '0' | 按实际预收控制发货 |
| 19 | fcontrolsend | fcontrolsend | varchar | 5 |  | √ | ' ' |  |
| 20 | fpreallowoverrate | 预收允超比例(%) | numeric | 23 | 10 | √ | 0 | 预收允超比例(%) |
| 21 | fremainamount | 关联收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联收款金额 |
| 22 | fcontrolnode | 控制环节 | varchar | 50 |  | √ | ' ' | 控制环节,枚举: delivernotice :发货通知 salout :销售出库 mftorder :生产工单 |
| 23 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 24 | frpprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 25 | fsrcbillrecentryid | 订单收款计划分录ID | int8 | 64 |  | √ | 0 | 订单收款计划分录ID |
| 26 | frpprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | frecadvanceamount | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 29 | frplicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xorderrecplety_fid |  | fid |
| 2 | t_sm_xsalorderrpentry_pkey |  | fentryid |

---

## 收款计划-多语言表 t_sm_xsalorderrpentry_l

- **表名称：** 收款计划-多语言表
- **表名：** t_sm_xsalorderrpentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frpmilestone | 里程碑 | varchar | 255 |  | √ | ' ' | 里程碑 |
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
| 1 | idx_t_xsm_salorderrpentry_l |  | fentryid,flocaleid |
| 2 | pk_t_sm_xsalorderrpentry_l |  | fpkid |

---

## 销售订单变更单-反写记录表 t_sm_salorder_wb

- **表名称：** 销售订单变更单-反写记录表
- **表名：** t_sm_salorder_wb

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
| 1 | t_sm_salorder_wb_pkey |  | fentryid |
| 2 | idx_sm_salorder_wb_fk |  | fid |

---

## 销售条款-子表 t_sm_xsalordertermentry

- **表名称：** 销售条款-子表
- **表名：** t_sm_xsalordertermentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillclauseentryid | fsrcbillclauseentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fclauseid | 条款编码 | int8 | 64 |  | √ | 0 | [销售条款 sm_salterm](../sm_files/sm_salterm.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fclausedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fclauseentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xsalescalentry_fid |  | fid |
| 2 | t_sm_xsalordertermentry_pkey |  | fentryid |

---

## 物流跟踪-子表 t_sm_xsalordertraceentry

- **表名称：** 物流跟踪-子表
- **表名：** t_sm_xsalordertraceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftracestatus | 物流状态 | varchar | 5 |  | √ | ' ' | 物流状态,枚举: |
| 3 | fphonenumber | 寄件人手机号 | varchar | 80 |  | √ | ' ' | 寄件人手机号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdelitime | 发货时间 | timestamp | 0 |  |  | null | 发货时间 |
| 6 | fsrcbilltraceentryid | fsrcbilltraceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | ftraceentrychangetype | ftraceentrychangetype | varchar | 5 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcarrybillno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 10 | flogcomid | 物流公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_xsalordertraceentry_pkey |  | fentryid |
| 2 | idx_sm_xordertraceentry_fid |  | fid |

---

## 物料明细-分表 t_sm_xsalorderentry_r

- **表名称：** 物料明细-分表
- **表名：** t_sm_xsalorderentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | fpurjoinqty | 关联采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联采购数量 |
| 5 | fmftorderqty | 关联生产数量 | numeric | 23 | 10 | √ | 0 | 关联生产数量 |
| 6 | fcfmjoinbaseqty | 关联确认基本数量 | numeric | 23 | 10 | √ | 0 | 关联确认基本数量 |
| 7 | fremaininvoicedbaseqty | 应收未关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票基本数量 |
| 8 | fsignedqty | 已签收数量 | numeric | 23 | 10 | √ | 0 | 已签收数量 |
| 9 | finvbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库基本数量 |
| 10 | fsourceentryid | 订单物料分录ID | int8 | 64 |  | √ | 0 | 订单物料分录ID |
| 11 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 12 | ftransitlossbaseqty | 途损基本数量 | numeric | 23 | 10 | √ | 0 | 途损基本数量 |
| 13 | fbasedeliqty | 已发货通知基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已发货通知基本数量 |
| 14 | fconfirmqty | 已确认数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已确认数量 |
| 15 | foversignedqty | 多签数量 | numeric | 23 | 10 | √ | 0 | 多签数量 |
| 16 | fremaininvqty | fremaininvqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 18 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 19 | fjoinpriceqty | 应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收数量 |
| 20 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 21 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 22 | fremaininvoicedqty | 应收未关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票数量 |
| 23 | fbasearqty | 应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收基本数量 |
| 24 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 25 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 26 | funbasedeliqty | 未发货通知基本数量 | numeric | 23 | 10 | √ | 0 | 未发货通知基本数量 |
| 27 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 28 | fdelijoinqty | fdelijoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 30 | finvqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 31 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 32 | ftransapplyqty | 已调拨申请数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调拨申请数量 |
| 33 | fprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 34 | fdeliqty | 已发货通知数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已发货通知数量 |
| 35 | fsrcsysbillentryid | 来源系统单据分录id | varchar | 100 |  | √ | ' ' | 来源系统单据分录id |
| 36 | fremainjoinpriceqty | fremainjoinpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | finvoicedqty | 关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票数量 |
| 38 | fbasetransjoinqty | fbasetransjoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 41 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 42 | fconfirmamount | 已确认金额 | numeric | 23 | 10 | √ | 0 | 已确认金额 |
| 43 | finvoicedbaseqty | 关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票基本数量 |
| 44 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 45 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 46 | fsignedbaseqty | 已签收基本数量 | numeric | 23 | 10 | √ | 0 | 已签收基本数量 |
| 47 | ftransapplybaseqty | 已调拨申请基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调拨申请基本数量 |
| 48 | fbackqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 49 | fbaseinvoicejoinqty | fbaseinvoicejoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | fbasebackqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 51 | ftransportbaseqty | 已运输基本数量 | numeric | 23 | 10 | √ | 0 | 已运输基本数量 |
| 52 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 53 | funinvbaseqty | 未出库基本数量 | numeric | 23 | 10 | √ | 0 | 未出库基本数量 |
| 54 | fbasemftorderqty | 关联生产基本数量 | numeric | 23 | 10 | √ | 0 | 关联生产基本数量 |
| 55 | ftransportqty | 已运输数量 | numeric | 23 | 10 | √ | 0 | 已运输数量 |
| 56 | fbasearjoinqty | 关联应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应收基本数量 |
| 57 | fconbillentryseq | 合同分录序号 | int8 | 64 |  | √ | 0 | 合同分录序号 |
| 58 | fprojassinvoiceamtandtax | 关联项目开票申请价税合计 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请价税合计 |
| 59 | ftransitlossqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 60 | farjoinqty | 关联应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应收数量 |
| 61 | funinvqty | 未出库数量 | numeric | 23 | 10 | √ | 0 | 未出库数量 |
| 62 | foversignedbaseqty | 多签基本数量 | numeric | 23 | 10 | √ | 0 | 多签基本数量 |
| 63 | fbasedelijoinqty | fbasedelijoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 64 | fbasepurqty | 已采购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购基本数量 |
| 65 | fcfmjoinqty | 关联确认数量 | numeric | 23 | 10 | √ | 0 | 关联确认数量 |
| 66 | fremaininvbaseqty | fremaininvbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 67 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 68 | fentrustverifyqty | 委托代销已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算数量 |
| 69 | fundeliqty | 未发货通知数量 | numeric | 23 | 10 | √ | 0 | 未发货通知数量 |
| 70 | fpurqty | 已采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购数量 |
| 71 | fentrustverifybaseqty | 委托代销已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算基本数量 |
| 72 | fremainbasebackqty | 售出可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 售出可退基本数量 |
| 73 | fconfirmbaseqty | 已确认基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已确认基本数量 |
| 74 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 75 | fprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 76 | finvoicedamountandtax | 关联销售发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计 |
| 77 | faramount | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 78 | fbasepurjoinqty | 关联采购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联采购基本数量 |
| 79 | fremainbackqty | 售出可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 售出可退数量 |
| 80 | fsrcsysbillid | 来源系统单据id | varchar | 100 |  | √ | ' ' | 来源系统单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_xsalorderentry_r_pkey |  | fentryid |
| 2 | idx_sm_xsalorderentry_r_fid |  | fid |

---

## 物料明细-多语言表 t_sm_xsalorderentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_sm_xsalorderentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | foldcusmaterialname | 历史客户物料名称 | varchar | 255 |  | √ | ' ' | 历史客户物料名称 |
| 5 | foldcusmaterialmod | 历史客户物料规格型号 | varchar | 255 |  | √ | ' ' | 历史客户物料规格型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xsalorderentry_l |  | fentryid,flocaleid |
| 2 | pk_t_sm_xsalorderentry_l |  | fpkid |

---

## 销售订单变更单-关联追踪表 t_sm_salorder_tc

- **表名称：** 销售订单变更单-关联追踪表
- **表名：** t_sm_salorder_tc

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
| 1 | idx_sm_salorder_tc_tbill |  | ftbillid |
| 2 | t_sm_salorder_tc_pkey |  | fid |
| 3 | idx_sm_salorder_tc_tid |  | ftid |

---

## 发货计划-子表 t_sm_xsalorderdeliventry

- **表名称：** 发货计划-子表
- **表名：** t_sm_xsalorderdeliventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanqty | 计划数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计划数量 |
| 2 | factbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdelentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 5 | fplandate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 6 | flastdeliverydate | 最近通知日期 | timestamp | 0 |  |  | null | 最近通知日期 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | factdeliverydate | 最近出库日期 | timestamp | 0 |  |  | null | 最近出库日期 |
| 10 | fdelibaseqty | 已通知基本数量 | numeric | 23 | 10 | √ | 0 | 已通知基本数量 |
| 11 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 12 | factqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 13 | fplandeliverydate | 计划发货日期 | timestamp | 0 |  |  | null | 计划发货日期 |
| 14 | fundelibaseqty | 剩余未通知基本数量 | numeric | 23 | 10 | √ | 0 | 剩余未通知基本数量 |
| 15 | freceiveaddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 16 | fplanunitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fsrcbilldeliventryid | 订单发货计划分录ID | int8 | 64 |  | √ | 0 | 订单发货计划分录ID |
| 18 | fundeliqty | 剩余未通知数量 | numeric | 23 | 10 | √ | 0 | 剩余未通知数量 |
| 19 | ftransportleadtime | 运输提前期（天） | numeric | 23 | 10 | √ | 0.0000000000 | 运输提前期（天） |
| 20 | funstockbaseqty | 剩余未出库基本数量 | numeric | 23 | 10 | √ | 0 | 剩余未出库基本数量 |
| 21 | fdeliqty | 已通知数量 | numeric | 23 | 10 | √ | 0 | 已通知数量 |
| 22 | fplanbaseqty | 计划基本数量 | numeric | 23 | 10 | √ | 0 | 计划基本数量 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | freceiveaddress | 收货地址 | varchar | 300 |  | √ | ' ' | 收货地址 |
| 25 | funstockqty | 剩余未出库数量 | numeric | 23 | 10 | √ | 0 | 剩余未出库数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xorderdelientry_feid |  | fentryid |
| 2 | t_sm_xsalorderdeliventry_pkey |  | fdetailid |

---

## 合同条款-子表 t_sm_xsalordertentry

- **表名称：** 合同条款-子表
- **表名：** t_sm_xsalordertentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同条款分组 conm_termgroup](../conm_files/conm_termgroup.md) |
| 3 | ftermentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | ftermcontent | 条款内容 | varchar | 2000 |  | √ | ' ' | 条款内容 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftermid | 合同条款 | int8 | 64 |  | √ | 0 | [合同条款 conm_term](../conm_files/conm_term.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_xsalordertentry |  | fid |
| 2 | pk_t_sm_xsalordertentry |  | fentryid |
