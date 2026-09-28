# 旧销售订单变更单（废弃）-sm_xsalorder

## 销售条款-子表 t_sm_xsalordertermentry

- **表名称：** 销售条款-子表
- **表名：** t_sm_xsalordertermentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillclauseentryid | fsrcbillclauseentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fclauseid | 条款编码 | int8 | 64 |  | √ | 0 | 销售条款 sm_salterm |
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

## 旧销售订单变更单（废弃）-主表 t_sm_xsalorder

- **表名称：** 旧销售订单变更单（废弃）-主表
- **表名：** t_sm_xsalorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 512 |  |  | null | 联系地址 |
| 3 | fprereceiptamount | 已预收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预收金额 |
| 4 | fsourcebillentity | fsourcebillentity | varchar | 36 |  | √ | ' ' |  |
| 5 | fsrcbiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 6 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 8 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 9 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :正常 B :已作废 |
| 10 | flocation | 交货地点 | varchar | 255 |  |  | null | 交货地点 |
| 11 | fassociatemargin | 关联保证金 | numeric | 23 | 10 | √ | 0.0000000000 | 关联保证金 |
| 12 | fchangecanceler | fchangecanceler | int8 | 64 |  | √ | 0 |  |
| 13 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 14 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 17 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 18 | fsrcbillstatus | 订单状态 | varchar | 5 |  | √ | ' ' | 订单状态,枚举: |
| 19 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 20 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 21 | forderstatus | 订单状态 | bpchar | 1 |  | √ | 'A' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货通知 E :已发货通知 F :部分出库 G :已出库 H :部分退货 I :已退货 J :部分应收 K :已应收 |
| 22 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 23 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 26 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 27 | fversion | 版本号 | varchar | 20 |  | √ | ' ' | 版本号 |
| 28 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fmarginlevel | 保证金比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 保证金比例(%) |
| 30 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 31 | fsrcbillid | 订单ID | int8 | 64 |  | √ | 0 | 订单ID |
| 32 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 33 | fdiscountlistid | 折扣表 | int8 | 64 |  | √ | 0 | 销售折扣表 sm_salediscountlist |
| 34 | fmpmrecmethod | 项目收入确认方式 | varchar | 50 |  | √ | ' ' | 项目收入确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | freason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |
| 37 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 38 | freceiptamount | 已收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收金额 |
| 39 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 40 | fbillsource | 单据来源 | bpchar | 1 |  | √ | 'A' | 单据来源,枚举: A :普通销售 B :移动销售 |
| 41 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 44 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 46 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 49 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 50 | fsrcbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 51 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 52 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 53 | fbiztime | 订单日期(封存) | timestamp | 0 |  |  | null | 订单日期(封存) |
| 54 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 55 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | factiverid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 57 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 58 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 59 | fisvirtualbill | 是否虚单 | bpchar | 1 |  | √ | '0' | 是否虚单 |
| 60 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 61 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 62 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 63 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 64 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 65 | fmargin | 保证金 | numeric | 23 | 10 | √ | 0.0000000000 | 保证金 |
| 66 | fassrefundmargin | 关联退款保证金 | numeric | 23 | 10 | √ | 0.0000000000 | 关联退款保证金 |
| 67 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 68 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 69 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 70 | factivestatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 71 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 72 | fchangecanceldate | fchangecanceldate | timestamp | 0 |  |  | null |  |
| 73 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 74 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 75 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 76 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 77 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 78 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 79 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 80 | fdeliverywayid | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 81 | fchangecancelstatus | fchangecancelstatus | varchar | 5 |  | √ | ' ' |  |
| 82 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 83 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 84 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 85 | fclosemanual | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 86 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 87 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 88 | fbizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 89 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 90 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 91 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 92 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 93 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 94 | freceiveaddress | 收货地址 | varchar | 512 |  |  | null | 收货地址 |

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

## 旧销售订单变更单（废弃）-多语言表 t_sm_xsalorder_l

- **表名称：** 旧销售订单变更单（废弃）-多语言表
- **表名：** t_sm_xsalorder_l

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
| 1 | t_sm_xsalorder_l_pkey |  | fpkid |
| 2 | idx_sm_xsalesorder_l |  | fid,flocaleid |

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
| 10 | flogcomid | 物流公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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
| 8 | finvbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库基本数量 |
| 9 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fmainbillentity | fmainbillentity | varchar | 36 |  | √ | ' ' |  |
| 11 | fbasedeliqty | 已发货通知基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已发货通知基本数量 |
| 12 | fconfirmqty | 已确认数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已确认数量 |
| 13 | fremaininvqty | fremaininvqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 15 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 16 | fjoinpriceqty | 应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收数量 |
| 17 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 18 | fmainbillid | fmainbillid | int8 | 64 |  | √ | 0 |  |
| 19 | fremaininvoicedqty | 应收未关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票数量 |
| 20 | fbasearqty | 应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收基本数量 |
| 21 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 22 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 23 | fsrcbillnumber | fsrcbillnumber | varchar | 80 |  | √ | ' ' |  |
| 24 | fdelijoinqty | fdelijoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 26 | finvqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 27 | fmainbillnumber | fmainbillnumber | varchar | 80 |  | √ | ' ' |  |
| 28 | ftransapplyqty | 已调拨申请数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调拨申请数量 |
| 29 | fdeliqty | 已发货通知数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已发货通知数量 |
| 30 | fsrcsysbillentryid | 来源系统单据分录id | varchar | 100 |  | √ | ' ' | 来源系统单据分录id |
| 31 | fremainjoinpriceqty | fremainjoinpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | finvoicedqty | 关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票数量 |
| 33 | fbasetransjoinqty | fbasetransjoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 36 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 37 | fconfirmamount | 已确认金额 | numeric | 23 | 10 | √ | 0 | 已确认金额 |
| 38 | finvoicedbaseqty | 关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票基本数量 |
| 39 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 40 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 41 | ftransapplybaseqty | 已调拨申请基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调拨申请基本数量 |
| 42 | fbackqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 43 | fbaseinvoicejoinqty | fbaseinvoicejoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fbasebackqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 45 | fsrcbillentity | fsrcbillentity | varchar | 36 |  | √ | ' ' |  |
| 46 | fbasemftorderqty | 关联生产基本数量 | numeric | 23 | 10 | √ | 0 | 关联生产基本数量 |
| 47 | fbasearjoinqty | 关联应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应收基本数量 |
| 48 | fconbillentryseq | 合同分录序号 | int8 | 64 |  | √ | 0 | 合同分录序号 |
| 49 | farjoinqty | 关联应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应收数量 |
| 50 | fbasedelijoinqty | fbasedelijoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 51 | fbasepurqty | 已采购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购基本数量 |
| 52 | fcfmjoinqty | 关联确认数量 | numeric | 23 | 10 | √ | 0 | 关联确认数量 |
| 53 | fremaininvbaseqty | fremaininvbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 55 | fentrustverifyqty | 委托代销已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算数量 |
| 56 | fpurqty | 已采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购数量 |
| 57 | fentrustverifybaseqty | 委托代销已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算基本数量 |
| 58 | fremainbasebackqty | 售出可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 售出可退基本数量 |
| 59 | fconfirmbaseqty | 已确认基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已确认基本数量 |
| 60 | fmainbillentryid | fmainbillentryid | int8 | 64 |  | √ | 0 |  |
| 61 | finvoicedamountandtax | 关联销售发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计 |
| 62 | faramount | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 63 | fbasepurjoinqty | 关联采购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联采购基本数量 |
| 64 | fremainbackqty | 售出可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 售出可退数量 |
| 65 | fsrcsysbillid | 来源系统单据id | varchar | 100 |  | √ | ' ' | 来源系统单据id |

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
| 11 | fmpmopportno | 商机号 | int8 | 64 |  | √ | 0 | 商机登记F7 mpm_bizopregf7 |
| 12 | foldcusmaterialname | 历史客户物料名称 | varchar | 255 |  | √ | ' ' | 历史客户物料名称 |
| 13 | foldcusmaterialmod | 历史客户物料规格型号 | varchar | 255 |  | √ | ' ' | 历史客户物料规格型号 |
| 14 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 15 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 17 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 18 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 21 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 24 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 28 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 29 | fprojassinvoicebaseqty | 关联项目开票申请基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请基本数量 |
| 30 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 31 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 32 | fprojectinvoicedbaseqty | 项目已申请开票基本数量 | numeric | 23 | 10 | √ | 0 | 项目已申请开票基本数量 |
| 33 | fprojassinvoiceqty | 关联项目开票申请数量 | numeric | 23 | 10 | √ | 0 | 关联项目开票申请数量 |
| 34 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 35 | fdeliverqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限数量 |
| 36 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 37 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 38 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 39 | fdeliverdelaydays | 允许延迟天数 | int4 | 32 |  | √ | 0 | 允许延迟天数 |
| 40 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | fsettledeptid | 结算部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 43 | fcorebillrowno | 核心单据行号(封存) | int8 | 64 |  | √ | 0 | 核心单据行号(封存) |
| 44 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 45 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 46 | fprojectinvoicedqty | 项目已申请开票数量 | numeric | 23 | 10 | √ | 0 | 项目已申请开票数量 |
| 47 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 48 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 49 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 50 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 51 | fdeliverqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限数量 |
| 52 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 53 | fmatchdiscountlistid | 行折扣表 | int8 | 64 |  | √ | 0 | 销售折扣表 sm_salediscountlist |
| 54 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 55 | fprojectconfbaseqty | 已确认项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务基本数量 |
| 56 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 |
| 57 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 58 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 59 | fdeliveradvdays | 允许提前天数 | int4 | 32 |  | √ | 0 | 允许提前天数 |
| 60 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 61 | fdeliverbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限基本数量 |
| 62 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 63 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 64 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 65 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 66 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 67 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 68 | foldcusmaterialnum | 历史客户物料编码 | varchar | 255 |  | √ | ' ' | 历史客户物料编码 |
| 69 | fexpectqty | 预计可发量 | numeric | 23 | 10 | √ | 0 | 预计可发量 |
| 70 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 71 | fprojectassqty | 关联项目服务数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务数量 |
| 72 | fprojectassbaseqty | 关联项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务基本数量 |
| 73 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 74 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 75 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 76 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 77 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 78 | fisprojassociated | 是否关联立项 | bpchar | 1 |  | √ | '0' | 是否关联立项 |
| 79 | freturntype | 退补类型 | varchar | 5 |  | √ | ' ' | 退补类型,枚举: 1 :退回 2 :补货 |
| 80 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 81 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 82 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 83 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 84 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 85 | fminorderbaseqty | 起销量(基本) | numeric | 23 | 10 | √ | 0.0000000000 | 起销量(基本) |
| 86 | fmatchpricelist | 行价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 87 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 88 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 89 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 90 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 91 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 92 | fentrystatus | fentrystatus | varchar | 5 |  | √ | ' ' |  |
| 93 | fissuedqty | fissuedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 94 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 95 | fcorebillno | 核心单据编号(封存) | varchar | 80 |  | √ | ' ' | 核心单据编号(封存) |
| 96 | fproorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 97 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 98 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 99 | frowterminatemanual | 行手工终止 | bpchar | 1 |  | √ | '0' | 行手工终止 |
| 100 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 101 | fdeliverbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限基本数量 |
| 102 | fsettleamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 103 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 104 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 105 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 106 | fdeliverydate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 107 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 108 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 109 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

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

## 旧销售订单变更单（废弃）-关联追踪表 t_sm_salorder_tc

- **表名称：** 旧销售订单变更单（废弃）-关联追踪表
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
| 8 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | factdeliverydate | 最近出库日期 | timestamp | 0 |  |  | null | 最近出库日期 |
| 10 | fdelibaseqty | 已通知基本数量 | numeric | 23 | 10 | √ | 0 | 已通知基本数量 |
| 11 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 12 | factqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 13 | fplandeliverydate | 计划发货日期 | timestamp | 0 |  |  | null | 计划发货日期 |
| 14 | fundelibaseqty | 剩余未通知基本数量 | numeric | 23 | 10 | √ | 0 | 剩余未通知基本数量 |
| 15 | freceiveaddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 16 | fplanunitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fsrcbilldeliventryid | 订单发货计划ID | int8 | 64 |  | √ | 0 | 订单发货计划ID |
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
| 4 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | frpmilestone | 里程碑 | varchar | 50 |  | √ | ' ' | 里程碑 |
| 7 | frecsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | frpmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 9 | frpcontract | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 10 | frelbillno | 关联单号 | varchar | 50 |  | √ | ' ' | 关联单号 |
| 11 | frecadvancerate | 应收比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应收比例(%) |
| 12 | frecamount | 已收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收金额 |
| 13 | frpexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | funremainamount | 未关联收款金额 | numeric | 23 | 10 | √ | 0 | 未关联收款金额 |
| 15 | frpmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 16 | frpprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 17 | fcontrolbyactualprerec | 按实际预收控制发货 | bpchar | 1 |  | √ | '0' | 按实际预收控制发货 |
| 18 | fcontrolsend | fcontrolsend | varchar | 5 |  | √ | ' ' |  |
| 19 | fpreallowoverrate | 预收允超比例(%) | numeric | 23 | 10 | √ | 0 | 预收允超比例(%) |
| 20 | fremainamount | 关联收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联收款金额 |
| 21 | fcontrolnode | 控制环节 | varchar | 50 |  | √ | ' ' | 控制环节,枚举: delivernotice :发货通知 salout :销售出库 mftorder :生产工单 |
| 22 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 23 | frpprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 24 | fsrcbillrecentryid | 订单收款计划ID | int8 | 64 |  | √ | 0 | 订单收款计划ID |
| 25 | frpprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | frecadvanceamount | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |

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

## 旧销售订单变更单（废弃）-反写记录表 t_sm_salorder_wb

- **表名称：** 旧销售订单变更单（废弃）-反写记录表
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
