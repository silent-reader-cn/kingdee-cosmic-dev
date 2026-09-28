# 采购订单-scp_order

## 采购订单-主表 t_pur_order

- **表名称：** 采购订单-主表
- **表名：** t_pur_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 最早交货日期 | timestamp | 0 |  |  | null | 最早交货日期 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fprepayrate | 预付比例(%) | numeric | 19 | 2 | √ | 0.00 | 预付比例(%) |
| 6 | foperatorid | 联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 7 | forgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 10 | fsumpayableamt | 应付金额 | numeric | 19 | 6 | √ | 0.000000 | 应付金额 |
| 11 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 13 | fpaystatus | 收款状态 | bpchar | 1 |  | √ | ' ' | 收款状态,枚举: A :待开票 B :部分开票 C :待收款 D :部分收款 E :已收款 |
| 14 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 15 | fcentersettle | 集中结算 | bpchar | 1 |  | √ | ' ' | 集中结算 |
| 16 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 17 | fsupgroupid | fsupgroupid | int8 | 64 |  | √ | 0 |  |
| 18 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 19 | fsumpayamt | 已付款金额 | numeric | 19 | 6 | √ | 0.000000 | 已付款金额 |
| 20 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fsuminvoiceamt | 已开票金额 | numeric | 19 | 6 | √ | 0.000000 | 已开票金额 |
| 23 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 25 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 E :变更中 |
| 27 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 28 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 30 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fdelisupid | 发货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 32 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 34 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 35 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 37 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 38 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 E :自动确认 |
| 39 | fissyn | fissyn | bpchar | 1 |  | √ | ' ' |  |
| 40 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 41 | fsumprepayamt | 预付金额 | numeric | 19 | 6 | √ | 0.000000 | 预付金额 |
| 42 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 43 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 45 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 46 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 47 | fcontacterid | 业务员 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 48 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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

## 采购订单-分表 t_pur_order_a

- **表名称：** 采购订单-分表
- **表名：** t_pur_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumsaloutamount | fsumsaloutamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 5 | fbillversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 8 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | ' ' |  |
| 11 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 12 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 16 | frejectreason | 打回原因 | varchar | 512 |  |  | ' ' | 打回原因 |
| 17 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | freason | 关闭原因 | varchar | 255 |  | √ | ' ' | 关闭原因 |
| 20 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | ' ' |  |
| 22 | fcloseid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fsumdiffamount | fsumdiffamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 24 | fsrcbilltype | 来源单据类型 | bpchar | 1 |  | √ | ' ' | 来源单据类型,枚举: 1 :自建商城 2 :京东商城 3 :ERP系统 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fsumsettleamount | fsumsettleamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 27 | fcheckstatus | fcheckstatus | bpchar | 1 |  | √ | ' ' |  |

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

## 采购订单-多语言表 t_pur_order_l

- **表名称：** 采购订单-多语言表
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
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 E :变更中 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 10 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 11 | frowlogstatus | 行物流状态 | bpchar | 1 |  | √ | ' ' | 行物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fpromiseday | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 14 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 16 | fdeliaddr | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 17 | fscheduledetail | 进度详情 | varchar | 512 |  | √ | ' ' | 进度详情 |
| 18 | fexecuteschedule | 执行进度 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 19 | fscheduleqty | 关联交货计划数量 | numeric | 23 | 10 | √ | 0 | 关联交货计划数量 |
| 20 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 21 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 22 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 24 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 26 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 28 | fschedulebaseqty | 关联交货计划基本数量 | numeric | 23 | 10 | √ | 0 | 关联交货计划基本数量 |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 31 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 32 | freqbillno | freqbillno | varchar | 80 |  | √ | ' ' |  |
| 33 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 34 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 36 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 37 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 38 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 39 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fexecutesdate | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 41 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 44 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

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

---

## 附件-附件表 t_pur_orderejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_orderejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orderrejectatt_fbasedataid |  | fbasedataid |
| 2 | pk_t_pur_orderejectreasonatt |  | fpkid |

---

## 物流信息-子表 t_pur_order_log

- **表名称：** 物流信息-子表
- **表名：** t_pur_order_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 3 | fdelidate | 预计到货日期 | timestamp | 0 |  |  | null | 预计到货日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flogbillno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 8 | fsupplierid | 物流公司 | int8 | 64 |  | √ | 0 | 物流公司 pur_logsupplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_order_log_flogbillno |  | flogbillno |
| 2 | t_pur_order_log_pkey |  | fentryid |
| 3 | idx_pur_order_log_fid_fseq |  | fid,fseq |

---

## 订单分录-分表 t_pur_orderentry_a

- **表名称：** 订单分录-分表
- **表名：** t_pur_orderentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumrefundqty | 已退补数量 | numeric | 23 | 10 | √ | 0 | 已退补数量 |
| 4 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '1' | 控制发货数量 |
| 5 | fsaloutqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0 | 发货上限数量 |
| 6 | fcostitemid | 费用类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 7 | fsuminstockretqty | 已退库数量 | numeric | 19 | 6 | √ | 0.000000 | 已退库数量 |
| 8 | fsaloutratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0 | 发货欠发比率(%) |
| 9 | frcvpersonname | 收货人 | varchar | 200 |  | √ | ' ' | 收货人 |
| 10 | ferpsourceid | ferpsourceid | varchar | 255 |  | √ | ' ' |  |
| 11 | frowcloseid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 13 | frowclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 14 | fsumreturnqty | fsumreturnqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | frcvpersonid | 收货人 | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 16 | fsumreceiptqty | 已收货数量 | numeric | 19 | 6 | √ | 0.000000 | 已收货数量 |
| 17 | fsaloutqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0 | 发货下限数量 |
| 18 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fsumreturnreqqty | 已退货申请数量 | numeric | 19 | 6 | √ | 0.000000 | 已退货申请数量 |
| 20 | flockprepayamt | 已锁定付款金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定付款金额 |
| 21 | fsumreceiveqty | 已通知数量 | numeric | 19 | 6 | √ | 0.000000 | 已通知数量 |
| 22 | fsumrejqty | 已拒收数量 | numeric | 19 | 6 | √ | 0.000000 | 已拒收数量 |
| 23 | fprepayamt | 预付金额 | numeric | 19 | 6 | √ | 0.000000 | 预付金额 |
| 24 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 25 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 26 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 27 | fsuminstockbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 28 | frelateoutstockqty | 关联发货数量 | numeric | 23 | 10 | √ | 0 | 关联发货数量 |
| 29 | fgoodsdesc | 供方商品描述 | varchar | 255 |  | √ | ' ' | 供方商品描述 |
| 30 | fjdorder | fjdorder | int8 | 64 |  | √ | 0 |  |
| 31 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 32 | fsumoutstockqty | 已发货数量 | numeric | 19 | 6 | √ | 0.000000 | 已发货数量 |
| 33 | frcvpersontel | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 34 | fsuminstockqty | 已入库数量 | numeric | 19 | 6 | √ | 0.000000 | 已入库数量 |
| 35 | fsaloutrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0 | 发货超发比率(%) |
| 36 | fsumrecretbaseqty | 已退货基本数量 | numeric | 23 | 10 | √ | 0 | 已退货基本数量 |
| 37 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fsaloutbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0 | 发货下限基本数量 |
| 40 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 41 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 42 | fpayprepayamt | 已付预付金额 | numeric | 19 | 6 | √ | 0.000000 | 已付预付金额 |
| 43 | fsaloutbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0 | 发货上限基本数量 |
| 44 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 45 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 46 | frelateoutstockbaseqty | 关联发货基本数量 | numeric | 23 | 10 | √ | 0 | 关联发货基本数量 |
| 47 | fsumaccepttaxamount | 已验收金额 | numeric | 23 | 10 | √ | 0 | 已验收金额 |
| 48 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 49 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 50 | fpayableamt | 关联对账金额 | numeric | 19 | 6 | √ | 0.000000 | 关联对账金额 |
| 51 | fiscontrolamountup | 控制上限金额 | bpchar | 1 |  | √ | '0' | 控制上限金额 |
| 52 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 53 | fsumrefundbaseqty | 已退补基本数量 | numeric | 23 | 10 | √ | 0 | 已退补基本数量 |
| 54 | fsuminstockretbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 55 | fvmistockqty | VMI在库数量 | numeric | 19 | 6 | √ | 0.000000 | VMI在库数量 |
| 56 | fsumreceiptbaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0 | 已收货基本数量 |
| 57 | frowclosereason | 关闭原因 | varchar | 255 |  | √ | ' ' | 关闭原因 |
| 58 | fsumoutstockbaseqty | 已发货基本数量 | numeric | 23 | 10 | √ | 0 | 已发货基本数量 |
| 59 | fsumapaccepttaxamount | 已申请验收金额 | numeric | 23 | 10 | √ | 0 | 已申请验收金额 |
| 60 | fpayableqty | 关联对账数量 | numeric | 19 | 6 | √ | 0.000000 | 关联对账数量 |
| 61 | fpayamt | 已付款金额 | numeric | 19 | 6 | √ | 0.000000 | 已付款金额 |
| 62 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 63 | ferpsourceentryid | ferpsourceentryid | varchar | 255 |  | √ | ' ' |  |
| 64 | frelateapaccepttaxamount | 关联验收申请金额 | numeric | 23 | 10 | √ | 0 | 关联验收申请金额 |
| 65 | famountup | 上限金额 | numeric | 23 | 10 | √ | 0 | 上限金额 |
| 66 | fsumrecretqty | 已退货数量 | numeric | 19 | 6 | √ | 0.000000 | 已退货数量 |
| 67 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 68 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 69 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 70 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

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
