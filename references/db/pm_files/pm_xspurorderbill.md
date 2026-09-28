# 采购订单变更单-pm_xspurorderbill

## 物料明细-分表 t_pm_xpurorderbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_pm_xpurorderbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | funjoinpricebaseqty | 未关联应付基本数量 | numeric | 23 | 10 | √ | 0 | 未关联应付基本数量 |
| 4 | finvretqty | 库存可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可退数量 |
| 5 | fsoubillid | 协同单据ID | int8 | 64 |  | √ | 0 | 协同单据ID |
| 6 | freceiptnoticeqty | 已收货通知数量 | numeric | 23 | 10 | √ | 0 | 已收货通知数量 |
| 7 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库基本数量 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 9 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | freleasedupqty | 已释放上游单据数量 | numeric | 23 | 10 | √ | 0 | 已释放上游单据数量 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | fjoinpriceqty | 关联应付数量 | numeric | 23 | 10 | √ | 0 | 关联应付数量 |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 16 | funreceiveqty | 未收货数量 | numeric | 23 | 10 | √ | 0 | 未收货数量 |
| 17 | funjoinpurinvoiceqty | 应付未关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票数量 |
| 18 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货基本数量 |
| 19 | fjoinbusqty | 暂估应付数量 | numeric | 23 | 10 | √ | 0 | 暂估应付数量 |
| 20 | fsrcsysbillno | 来源系统编号 | varchar | 100 |  | √ | ' ' | 来源系统编号 |
| 21 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 22 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 23 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 24 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 25 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 26 | fsoubillnumber | 协同单据编号 | varchar | 80 |  | √ | ' ' | 协同单据编号 |
| 27 | freceiptnoticbaseqty | 已收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 已收货通知基本数量 |
| 28 | fjoinbusunwoffqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 29 | freleasedupbaseqty | 已释放上游单据基本数量 | numeric | 23 | 10 | √ | 0 | 已释放上游单据基本数量 |
| 30 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 31 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 32 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 33 | frecretqty | 收货可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货可退数量 |
| 34 | freturnreceiptqty | 已退验数量 | numeric | 23 | 10 | √ | 0 | 已退验数量 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | fsoubillentryseq | 协同单据分录序号 | int8 | 64 |  | √ | 0 | 协同单据分录序号 |
| 37 | fjoinbusbaseqty | 暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量 |
| 38 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |
| 39 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货数量 |
| 40 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 41 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 42 | fjoinpurinvoicebaseqty | 关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票基本数量 |
| 43 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 44 | frecretbaseqty | 收货可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货可退基本数量 |
| 45 | fperformamount | 执行金额 | numeric | 23 | 10 | √ | 0 | 执行金额 |
| 46 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 47 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 48 | fjoinpricebaseqty | 关联应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联应付基本数量 |
| 49 | fjoinpayablebaseqty | 关联验收应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联验收应付基本数量 |
| 50 | finvretbaseqty | 库存可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可退基本数量 |
| 51 | fpayablebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0 | 应付基本数量 |
| 52 | funjoinpurinvoicebaseqty | 应付未关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票基本数量 |
| 53 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 54 | funjoinpriceqty | 未关联应付数量 | numeric | 23 | 10 | √ | 0 | 未关联应付数量 |
| 55 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 56 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 57 | funinvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0 | 未入库基本数量 |
| 58 | fconbillentryseq | 合同分录序号 | varchar | 50 |  | √ | ' ' | 合同分录序号 |
| 59 | fjoinamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 60 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 61 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 62 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 63 | fjoinpurinvoiceamount | 关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联采购发票价税合计 |
| 64 | fsoubillentryid | 协同单据行ID | int8 | 64 |  | √ | 0 | 协同单据行ID |
| 65 | funinvqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 66 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 67 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 68 | fpayablepriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 69 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 70 | fmftorderentrypid | 委外工单行父id | int8 | 64 |  | √ | 0 | 委外工单行父id |
| 71 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 72 | fsoubillentity | 协同单据实体 | varchar | 36 |  | √ | ' ' | 协同单据实体 |
| 73 | funreceivebaseqty | 未收货基本数量 | numeric | 23 | 10 | √ | 0 | 未收货基本数量 |
| 74 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 75 | fjoinpayablepriceqty | 关联验收应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联验收应付数量 |
| 76 | fjoinpurinvoiceqty | 关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票数量 |
| 77 | freturnreceiptbaseqty | 已退验基本数量 | numeric | 23 | 10 | √ | 0 | 已退验基本数量 |
| 78 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |
| 79 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_xpurorderbillentry_r_pkey |  | fentryid |
| 2 | idx_pm_xpobillentry_r |  | fid |

---

## 采购订单变更单-多语言表 t_pm_xpurorderbill_l

- **表名称：** 采购订单变更单-多语言表
- **表名：** t_pm_xpurorderbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_xpurorderbill_l_pkey |  | fpkid |
| 2 | idx_pm_xpurorderbill_l |  | fid,flocaleid |

---

## 回款依据-子表 t_pm_purorderpayrefentry

- **表名称：** 回款依据-子表
- **表名：** t_pm_purorderpayrefentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtbpraentprojectid | 父项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fbtbprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fbtblinkedphaseid | 关联阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 5 | fbtbispraent | 按父项目回款 | bpchar | 1 |  | √ | '0' | 按父项目回款 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbtblinkedmilestoneid | 关联里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorderpayrefentry |  | fid |
| 2 | pk_t_pm_purorderpayrefentry |  | fentryid |

---

## 采购订单变更单-主表 t_pm_xpurorderbill

- **表名称：** 采购订单变更单-主表
- **表名：** t_pm_xpurorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmpmpaymethod | 项目支出确认方式 | varchar | 5 |  | √ | ' ' | 项目支出确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 3 | fpaidallamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 4 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 8 | fchangecanceler | 变更单作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 10 | fsplitschemeid | 付款计划方案 | int8 | 64 |  | √ | 0 | [付款计划方案 ap_plansplit_scheme](../ap_files/ap_plansplit_scheme.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 15 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 18 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmarginlevel | 保证金比例(%) | numeric | 23 | 10 | √ | 0 | 保证金比例(%) |
| 20 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 21 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 22 | fbtbpayrateset | 付款比例设置 | varchar | 30 |  | √ | ' ' | 付款比例设置,枚举: ZDY :自定义 TBL :收支同步 |
| 23 | freason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |
| 24 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 25 | ftraderouteid | 贸易路线 | int8 | 64 |  | √ | 0 | [贸易路线 sbs_traderoute](../sbs_files/sbs_traderoute.md) |
| 26 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpaidpreallamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 28 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 29 | fsourcebiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 30 | fsettleorgid | 结算组织(废弃) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 35 | flogisticsstatus | 物流状态 | varchar | 5 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 36 | fk_bj73_operator | fk_bj73_operator | int8 | 64 |  | √ | 0 |  |
| 37 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 D :原始源单 |
| 38 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 39 | fprovideraddress | 供货联系地址 | varchar | 512 |  |  | ' ' | 供货联系地址 |
| 40 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [采购价目表 pm_purpricelist](../pm_files/pm_purpricelist.md) |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 44 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 45 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 46 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |
| 47 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 48 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | factivestatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 51 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 54 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 56 | fchangecancelstatus | 变更单作废状态 | varchar | 5 |  | √ | ' ' | 变更单作废状态,枚举: A :正常 B :变更中 C :已变更 |
| 57 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 58 | foutmargin | 转出保证金 | numeric | 23 | 10 | √ | 0 | 转出保证金 |
| 59 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 60 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 61 | favailablemargin | 可用保证金 | numeric | 23 | 10 | √ | 0 | 可用保证金 |
| 62 | frelatemargin | 关联保证金 | numeric | 23 | 10 | √ | 0 | 关联保证金 |
| 63 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 64 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 65 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 66 | fcarrierid | 承运方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 67 | faddress | 联系地址 | varchar | 512 |  | √ | ' ' | 联系地址 |
| 68 | fk_bj73_basedatafield | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 69 | fsourcebillentity | 订单实体标识 | varchar | 36 |  | √ | ' ' | 订单实体标识 |
| 70 | fsourceid | 订单ID | int8 | 64 |  | √ | 0 | 订单ID |
| 71 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 72 | fassociatemargin | 已付保证金 | numeric | 23 | 10 | √ | 0 | 已付保证金 |
| 73 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 74 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 75 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 76 | ftradestatus | 贸易转换状态 | bpchar | 1 |  | √ | ' ' | 贸易转换状态,枚举: 0 :未完成 1 :已完成 |
| 77 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 78 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 79 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 80 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 81 | fdescountryid | 目的国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 82 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 83 | fmanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 84 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 85 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 86 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 87 | fk_bj73_textfield4 | 发货地址 | varchar | 50 |  | √ | ' ' | 发货地址 |
| 88 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 89 | fdiscountlist | 折扣表 | int8 | 64 |  | √ | 0 | [采购折扣表 pm_purdiscountlist](../pm_files/pm_purdiscountlist.md) |
| 90 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :自动确认 |
| 91 | fk_bj73_textfield2 | foperatorid | varchar | 50 |  | √ | ' ' | foperatorid |
| 92 | fendbill | 尾单 | bpchar | 1 |  | √ | '0' | 尾单 |
| 93 | fbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 94 | fk_bj73_textfield1 | 采购订单 | varchar | 50 |  | √ | ' ' | 采购订单 |
| 95 | fpaystatus | 付款状态 | varchar | 5 |  | √ | ' ' | 付款状态,枚举: A :待付款 B :部分付款 C :已付款 |
| 96 | factiverid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 97 | fsrccountryid | 装运国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 98 | fisimport | 进口 | bpchar | 1 |  | √ | '0' | 进口 |
| 99 | fsourceno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 100 | fbtbpayref | 付款参考 | varchar | 30 |  | √ | ' ' | 付款参考,枚举: FKCK01 :项目收款 FKCK02 :阶段收款 FKCK03 :单个里程碑 FKCK04 :截止至固定里程碑 |
| 101 | fmargin | 应付保证金 | numeric | 23 | 10 | √ | 0 | 应付保证金 |
| 102 | fassrefundmargin | 已退保证金 | numeric | 23 | 10 | √ | 0 | 已退保证金 |
| 103 | fsourcestatus | 订单状态 | varchar | 5 |  | √ | ' ' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 |
| 104 | fstep | 当前步骤 | int4 | 32 |  | √ | 0 | 当前步骤 |
| 105 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 106 | fchangecanceldate | 变更单作废日期 | timestamp | 0 |  |  | null | 变更单作废日期 |
| 107 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 108 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 109 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 110 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 111 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 112 | ftransportmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 113 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 114 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpurorder_billno_org |  | fbillno,forgid |
| 2 | idx_pm_xpurorderbill_time |  | fbiztime |
| 3 | idx_pm_xpurorderbill_org |  | forgid,fbiztime,fbillno |
| 4 | t_pm_xpurorderbill_pkey |  | fid |

---

## 物料明细-子表 t_pm_xpurorderbillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_xpurorderbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqtyup | 收货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货上限数量 |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fdeliverlocationid | 交货地点 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fsourceentryid | 订单行ID | int8 | 64 |  | √ | 0 | 订单行ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | frootdemandentryseq | 根需求单据分录行号 | int4 | 32 |  | √ | 0 | 根需求单据分录行号 |
| 9 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fprojectconfqty | 已确认项目服务数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务数量 |
| 11 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 14 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | freceivebaseqtydown | 收货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货下限基本数量 |
| 16 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fdeliveraddress | 交货地址 | varchar | 512 |  |  | ' ' | 交货地址 |
| 19 | freceivebaseqtyup | 收货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货上限基本数量 |
| 20 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 22 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 24 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fmatchtype | 匹配类型 | bpchar | 1 |  | √ | ' ' | 匹配类型,枚举: A :订单匹配合同 |
| 28 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 31 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 32 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 33 | freceiveqtydown | 收货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货下限数量 |
| 34 | fsupplierlot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 35 | frootdemandentity | 根需求单据实体 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 36 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 37 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 38 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 39 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | ftransportbaseqty | 已运输基本数量 | numeric | 23 | 10 |  | null | 已运输基本数量 |
| 42 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 43 | fiscontrolamountup | 控制上限金额 | bpchar | 1 |  | √ | '0' | 控制上限金额 |
| 44 | frootdemandbillno | 根需求单据编码 | varchar | 120 |  | √ | ' ' | 根需求单据编码 |
| 45 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 46 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | freceivingtype | 代收料组织类型 | varchar | 36 |  | √ | ' ' | 代收料组织类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 49 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 50 | fislogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 51 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 52 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 53 | fentrypurorgid | 分录采购组织(封存) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 55 | fprojectconfbaseqty | 已确认项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务基本数量 |
| 56 | freceivedaydown | 允许延迟天数 | int4 | 32 |  | √ | 0 | 允许延迟天数 |
| 57 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 58 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 59 | fiscontrolqty | 控制收货数量 | bpchar | 1 |  | √ | '0' | 控制收货数量 |
| 60 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 61 | freceiverateup | 收货超收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货超收比率(%) |
| 62 | fentrysettledeptid | 结算部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 65 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 66 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 67 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 68 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 69 | fprojectassqty | 关联项目服务数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务数量 |
| 70 | fprojectassbaseqty | 关联项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务基本数量 |
| 71 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 72 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 73 | fentrymanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 74 | fjointransportbaseqty | 关联运输基本数量 | numeric | 23 | 10 | √ | 0 | 关联运输基本数量 |
| 75 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 76 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 77 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 78 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 79 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 80 | fjointransportqty | 关联运输数量 | numeric | 23 | 10 | √ | 0 | 关联运输数量 |
| 81 | fisdirectdelivery | 是否直送 | bpchar | 1 |  | √ | '0' | 是否直送 |
| 82 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 83 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 84 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 85 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 86 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 87 | fentrypayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 88 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 89 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 90 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 91 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 92 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 93 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 94 | fk_bj73_textfield3 | requid | varchar | 50 |  | √ | ' ' | requid |
| 95 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 96 | freceiving | 代收料组织 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 97 | freceiveratedown | 收货欠收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货欠收比率(%) |
| 98 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 99 | ftransportqty | 已运输数量 | numeric | 23 | 10 |  | null | 已运输数量 |
| 100 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 101 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 102 | ffloatingconversion | 浮动换算 | bpchar | 1 |  | √ | '0' | 浮动换算 |
| 103 | freceivedayup | 允许提前天数 | int4 | 32 |  | √ | 0 | 允许提前天数 |
| 104 | famountup | 上限金额 | numeric | 23 | 10 | √ | 0 | 上限金额 |
| 105 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 106 | fprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 107 | fk_bj73_textfield | TZID | varchar | 50 |  | √ | ' ' | TZID |
| 108 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 109 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpurorderbillentry |  | fid |
| 2 | t_pm_xpurorderbillentry_pkey |  | fentryid |

---

## 付款计划-子表 t_pm_xpurorderpayentry

- **表名称：** 付款计划-子表
- **表名：** t_pm_xpurorderpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 3 | finvoicedamount | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 4 | fplanprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fplanmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 6 | fk_bj73_qtyfield | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpayamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 9 | fplanprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 10 | fpayentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 12 | fplanmainbillnumber | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 13 | fisprepay | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 14 | fplanentrysettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fplanbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 16 | fpayentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fpayprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 18 | fprepaybillno | 预付款单编号 | varchar | 80 |  | √ | ' ' | 预付款单编号 |
| 19 | fplanexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fplanmilestone | 里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 21 | fjoinpayamount | 关联付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联付款金额 |
| 22 | fpayentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fpaypriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 24 | fplanconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 25 | fplanentrycomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fplanlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 27 | fpayentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 28 | fpayentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fpayrate | 应付比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应付比例(%) |
| 30 | fpaidamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 31 | fk_bj73_unitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | fsourcepayentryid | 订单付款计划ID | int8 | 64 |  | √ | 0 | 订单付款计划ID |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 35 | fpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_xpurorderpayentry_pkey |  | fentryid |
| 2 | idx_pm_xpurorderpayentry |  | fid |

---

## 合同条款-子表 t_pm_xpurorderbilltentry

- **表名称：** 合同条款-子表
- **表名：** t_pm_xpurorderbilltentry

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
| 1 | idx_pm_xpurorderbilltentry |  | fid |
| 2 | pk_t_pm_xpurorderbilltentry |  | fentryid |

---

## 交货计划-子表 t_pm_xporderdeliverentry

- **表名称：** 交货计划-子表
- **表名：** t_pm_xporderdeliverentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanqty | 计划交货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计划交货数量 |
| 2 | fdeliveryaddress | 交货地址 | varchar | 512 |  | √ | ' ' | 交货地址 |
| 3 | fplandeliverdate | 计划交货日期 | timestamp | 0 |  |  | null | 计划交货日期 |
| 4 | fplanuninvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0 | 未入库基本数量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fconfirmdeliverydate | 确认交货日期 | timestamp | 0 |  |  | null | 确认交货日期 |
| 7 | fplanreceiveqty | 已交货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已交货数量 |
| 8 | fdelentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 9 | fplaninvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 10 | fbaseconfirmdeliveryqty | 确认交货基本数量 | numeric | 23 | 10 | √ | 0 | 确认交货基本数量 |
| 11 | fdeliveryplace | 交货地点 | varchar | 512 |  | √ | ' ' | 交货地点 |
| 12 | fdelentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fplancomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fbaseplanunitid | 交货计划基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbaseplanqty | 计划交货基本数量 | numeric | 23 | 10 | √ | 0 | 计划交货基本数量 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fdelentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbaseplanreceiveqty | 已交货基本数量 | numeric | 23 | 10 | √ | 0 | 已交货基本数量 |
| 19 | fplanuninvqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 20 | fplaninvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 21 | fdelentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsurplusqty | 未交货数量 | numeric | 23 | 10 | √ | 0 | 未交货数量 |
| 23 | fplanunitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fconfirmdeliveryqty | 确认交货数量 | numeric | 23 | 10 | √ | 0 | 确认交货数量 |
| 25 | fplanreceivedate | 收货日期（废弃） | timestamp | 0 |  |  | null | 收货日期（废弃） |
| 26 | flatestdeliverydate | 最近交货日期 | timestamp | 0 |  |  | null | 最近交货日期 |
| 27 | fsourcedeliverentryid | 订单交货计划ID | int8 | 64 |  | √ | 0 | 订单交货计划ID |
| 28 | fbasesurplusqty | 未交货基本数量 | numeric | 23 | 10 | √ | 0 | 未交货基本数量 |
| 29 | fmaterialtrackingdate | 追料到货日期 | timestamp | 0 |  |  | null | 追料到货日期 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 31 | fdelentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpodeliverentry |  | fentryid |
| 2 | t_pm_xporderdeliverentry_pkey |  | fdetailid |

---

## 付款比例约束-子表 t_pm_purorderpayrateentry

- **表名称：** 付款比例约束-子表
- **表名：** t_pm_purorderpayrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtbpayratio | 累计付款比例(%) | numeric | 23 | 10 | √ | 0 | 累计付款比例(%) |
| 3 | fbtbpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 4 | fbtbrecratio | 累计收款比例(%) | numeric | 23 | 10 | √ | 0 | 累计收款比例(%) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbtbispre | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 8 | fbtbpayrate | 付款比例(%) | numeric | 23 | 10 | √ | 0 | 付款比例(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorderpayrateentry |  | fid |
| 2 | pk_t_pm_purorderpayrateentry |  | fentryid |
