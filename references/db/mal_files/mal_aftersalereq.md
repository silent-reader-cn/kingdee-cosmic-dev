# 售后申请（暂时弃用）-mal_aftersalereq

## 售后申请（暂时弃用）-主表 t_pur_order

- **表名称：** 售后申请（暂时弃用）-主表
- **表名：** t_pur_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 7 | fsumpayableamt | 累计应付金额 | numeric | 23 | 10 | √ | 0.000000 | 累计应付金额 |
| 8 | freqpersonid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 10 | fsumpayamt | 已付款金额 | numeric | 23 | 10 | √ | 0.000000 | 已付款金额 |
| 11 | fbillno | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 12 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: B :已提交 C :已审核 Z :已作废 D :已关闭 |
| 14 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :待收货 D :部分收货 E :待入库 F :部分入库 G :已入库 |
| 15 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 16 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 17 | fissyn | fissyn | bpchar | 1 |  | √ | ' ' |  |
| 18 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 19 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbusinesstypeid | fbusinesstypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 22 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fprepayrate | 预付比例(%) | numeric | 23 | 6 | √ | 0.00 | 预付比例(%) |
| 24 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 25 | fbilldate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 26 | fpayeesupid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpaystatus | 付款状态 | bpchar | 1 |  | √ | ' ' | 付款状态,枚举: A :待开票 B :部分开票 C :待付款 D :部分付款 E :已付款 |
| 28 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 29 | fcentersettle | 集中结算 | bpchar | 1 |  | √ | ' ' | 集中结算 |
| 30 | fsupgroupid | 供应商分组 | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 31 | fplatform | fplatform | bpchar | 1 |  | √ | ' ' |  |
| 32 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 33 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 34 | fsuminvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.000000 | 已开票金额 |
| 35 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 37 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 39 | finvoicesupid | 开票供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 40 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 41 | fdelisupid | 送货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 42 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 44 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 45 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 46 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 47 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 48 | fsumprepayamt | 预付金额 | numeric | 23 | 10 | √ | 0.000000 | 预付金额 |
| 49 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 50 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 51 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_order_pkey |  | fid |
| 2 | idx_pur_order_fbillno |  | fbillno |
| 3 | idx_pur_order_frcvorgid |  | frcvorgid |
| 4 | idx_pur_order_fsupplierid |  | fsupplierid |
| 5 | idx_pur_order_fbizpartnerid |  | fbilldate,fbizpartnerid |

---

## 售后申请（暂时弃用）-分表 t_pur_order_a

- **表名称：** 售后申请（暂时弃用）-分表
- **表名：** t_pur_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumsaloutamount | fsumsaloutamount | numeric | 23 | 10 | √ | 0.000000 |  |
| 3 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 4 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 5 | fbillversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchangestatus | fchangestatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 9 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | frejectdate | frejectdate | timestamp | 0 |  |  | null |  |
| 13 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 14 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 15 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 19 | frejectreason | frejectreason | varchar | 512 |  |  | ' ' |  |
| 20 | frejecterid | frejecterid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 23 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | ' ' |  |
| 25 | fsubversion | fsubversion | varchar | 50 |  | √ | ' ' |  |
| 26 | fcloseid | fcloseid | int8 | 64 |  | √ | 0 |  |
| 27 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 28 | fsumdiffamount | fsumdiffamount | numeric | 23 | 10 | √ | 0.000000 |  |
| 29 | fsrcbilltype | 源单类型 | bpchar | 1 |  | √ | ' ' | 源单类型,枚举: 1 :自建商城 2 :京东商城 3 :ERP系统 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fsumsettleamount | fsumsettleamount | numeric | 23 | 10 | √ | 0.000000 |  |
| 32 | fcheckstatus | fcheckstatus | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_order_a_pkey |  | fid |
| 2 | idx_pur_order_a_fcreatetime |  | fcreatetime |

---

## 订单分录-分表 t_pur_orderentry_a

- **表名称：** 订单分录-分表
- **表名：** t_pur_orderentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumrefundqty | fsumrefundqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '1' |  |
| 5 | fsaloutqtyup | fsaloutqtyup | numeric | 23 | 10 | √ | 0 |  |
| 6 | fcostitemid | 费用类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 7 | fsuminstockretqty | fsuminstockretqty | numeric | 23 | 10 | √ | 0.000000 |  |
| 8 | fsaloutratedown | fsaloutratedown | numeric | 23 | 10 | √ | 0 |  |
| 9 | frcvpersonname | frcvpersonname | varchar | 200 |  | √ | ' ' |  |
| 10 | ferpsourceid | ferpsourceid | varchar | 255 |  | √ | ' ' |  |
| 11 | frowcloseid | frowcloseid | int8 | 64 |  | √ | 0 |  |
| 12 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 13 | frowclosedate | frowclosedate | timestamp | 0 |  |  | null |  |
| 14 | fsumreturnqty | fsumreturnqty | numeric | 23 | 10 | √ | 0.000000 |  |
| 15 | frcvpersonid | 收货人 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 16 | fsumreceiptqty | 关联收货数量 | numeric | 23 | 10 | √ | 0.000000 | 关联收货数量 |
| 17 | fsaloutqtydown | fsaloutqtydown | numeric | 23 | 10 | √ | 0 |  |
| 18 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fsumreturnreqqty | 关联退货申请数量 | numeric | 23 | 10 | √ | 0.000000 | 关联退货申请数量 |
| 20 | flockprepayamt | 已锁定付款金额 | numeric | 23 | 10 | √ | 0.000000 | 已锁定付款金额 |
| 21 | fsumreceiveqty | 关联通知数量 | numeric | 23 | 10 | √ | 0.000000 | 关联通知数量 |
| 22 | fsumrejqty | fsumrejqty | numeric | 23 | 10 | √ | 0.000000 |  |
| 23 | fprepayamt | 预付金额 | numeric | 23 | 10 | √ | 0.000000 | 预付金额 |
| 24 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 25 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 26 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 27 | fsuminstockbaseqty | fsuminstockbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | frelateoutstockqty | frelateoutstockqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 30 | fjdorder | fjdorder | int8 | 64 |  | √ | 0 |  |
| 31 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 32 | fsumoutstockqty | 关联发货数量 | numeric | 23 | 10 | √ | 0.000000 | 关联发货数量 |
| 33 | frcvpersontel | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 34 | fsuminstockqty | 关联入库数量 | numeric | 23 | 10 | √ | 0.000000 | 关联入库数量 |
| 35 | fsaloutrateup | fsaloutrateup | numeric | 23 | 10 | √ | 0 |  |
| 36 | fsumrecretbaseqty | fsumrecretbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fsaloutbaseqtydown | fsaloutbaseqtydown | numeric | 23 | 10 | √ | 0 |  |
| 40 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 41 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 42 | fpayprepayamt | 已付预付金额 | numeric | 23 | 10 | √ | 0.000000 | 已付预付金额 |
| 43 | fsaloutbaseqtyup | fsaloutbaseqtyup | numeric | 23 | 10 | √ | 0 |  |
| 44 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 45 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 46 | frelateoutstockbaseqty | frelateoutstockbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsumaccepttaxamount | fsumaccepttaxamount | numeric | 23 | 10 | √ | 0 |  |
| 48 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 49 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 50 | fpayableamt | 累计应付金额 | numeric | 23 | 10 | √ | 0.000000 | 累计应付金额 |
| 51 | fiscontrolamountup | fiscontrolamountup | bpchar | 1 |  | √ | '0' |  |
| 52 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 53 | fsumrefundbaseqty | fsumrefundbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | fsuminstockretbaseqty | fsuminstockretbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fvmistockqty | VMI在库数量 | numeric | 23 | 10 | √ | 0.000000 | VMI在库数量 |
| 56 | fsumreceiptbaseqty | fsumreceiptbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 57 | frelateinvoiceamt | frelateinvoiceamt | numeric | 23 | 10 | √ | 0 |  |
| 58 | frowclosereason | frowclosereason | varchar | 255 |  | √ | ' ' |  |
| 59 | fsumoutstockbaseqty | fsumoutstockbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 60 | fsumapaccepttaxamount | fsumapaccepttaxamount | numeric | 23 | 10 | √ | 0 |  |
| 61 | fpayableqty | 累计应付数量 | numeric | 23 | 10 | √ | 0.000000 | 累计应付数量 |
| 62 | fpayamt | 已付款金额 | numeric | 23 | 10 | √ | 0.000000 | 已付款金额 |
| 63 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 64 | ferpsourceentryid | ferpsourceentryid | varchar | 255 |  | √ | ' ' |  |
| 65 | frelateapaccepttaxamount | frelateapaccepttaxamount | numeric | 23 | 10 | √ | 0 |  |
| 66 | frelateinvoiceqty | frelateinvoiceqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | famountup | famountup | numeric | 23 | 10 | √ | 0 |  |
| 68 | fsumrecretqty | fsumrecretqty | numeric | 23 | 10 | √ | 0.000000 |  |
| 69 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 金额(本位币) |
| 70 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 71 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 72 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_orderen_a_fpobid |  | fpobillid |
| 2 | t_pur_orderentry_a_pkey |  | fentryid |
| 3 | idx_pur_orderentry_a_fid |  | fid |
| 4 | idx_pur_orderentry_a_fpoid |  | fpoentryid |

---

## 售后申请（暂时弃用）-多语言表 t_pur_order_l

- **表名称：** 售后申请（暂时弃用）-多语言表
- **表名：** t_pur_order_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_order_l_fid_flocaleid |  | fid,flocaleid |
| 2 | t_pur_order_l_pkey |  | fpkid |

---

## 订单分录-子表 t_pur_orderentry

- **表名称：** 订单分录-子表
- **表名：** t_pur_orderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 11 | frowlogstatus | frowlogstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fpromiseday | fpromiseday | timestamp | 0 |  |  | null |  |
| 14 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 16 | fdeliaddr | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |
| 17 | fscheduledetail | fscheduledetail | varchar | 512 |  | √ | ' ' |  |
| 18 | fexecuteschedule | fexecuteschedule | int8 | 64 |  | √ | 0 |  |
| 19 | fscheduleqty | fscheduleqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 21 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 22 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 24 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 26 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | 'NULL' |  |
| 28 | fschedulebaseqty | fschedulebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 31 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 32 | freqbillno | freqbillno | varchar | 80 |  | √ | ' ' |  |
| 33 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 pur_warehouse](../pbd_files/pur_warehouse.md) |
| 34 | fpayentrychangetype | fpayentrychangetype | bpchar | 1 |  | √ | ' ' |  |
| 35 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fjointdatachannelid | fjointdatachannelid | varchar | 80 |  | √ | ' ' |  |
| 37 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 38 | fmaterialnametext | fmaterialnametext | varchar | 255 |  | √ | ' ' |  |
| 39 | ftraceno | ftraceno | int8 | 64 |  | √ | 0 |  |
| 40 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 41 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fexecutesdate | fexecutesdate | timestamp | 0 |  |  | null |  |
| 43 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 46 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_orderentry_fmaterialid |  | fmaterialid |
| 2 | idx_pur_orderentry_fid_fseq |  | fid,fseq |
| 3 | t_pur_orderentry_pkey |  | fentryid |
