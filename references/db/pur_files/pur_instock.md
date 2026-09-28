# 入库查询-pur_instock

## 入库查询-反写记录表 t_pur_instock_wb

- **表名称：** 入库查询-反写记录表
- **表名：** t_pur_instock_wb

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
| 1 | t_pur_instock_wb_pkey |  | fentryid |

---

## 入库查询-多语言表 t_pur_instock_l

- **表名称：** 入库查询-多语言表
- **表名：** t_pur_instock_l

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
| 1 | idx_pur_instock_l_fid |  | fid,flocaleid |
| 2 | t_pur_instock_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_pur_instockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_instockentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_instockentry_lk_pkey |  | fpkid |
| 2 | idx_pur_instock_lk_fentryid |  | fentryid |

---

## 入库查询-分表 t_pur_instock_a

- **表名称：** 入库查询-分表
- **表名：** t_pur_instock_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fisinitial | 期初入库单（废弃） | bpchar | 1 |  | √ | ' ' | 期初入库单（废弃） |
| 5 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 7 | fchkbillno | 对账单号 | varchar | 80 |  | √ | ' ' | 对账单号 |
| 8 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fiscentersettle | 集中结算 | bpchar | 1 |  | √ | ' ' | 集中结算 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fischeck | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |
| 15 | fisvirtual | fisvirtual | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_instock_a_pkey |  | fid |
| 2 | idx_pur_instock_a_fcreatetime |  | fcreatetime |

---

## 入库查询-主表 t_pur_instock

- **表名称：** 入库查询-主表
- **表名：** t_pur_instock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 6 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | freplenishtype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货需补 2 :新补货订单 3 :退货不补 |
| 10 | fpayeesupid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 12 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 13 | fbusinessdirect | 业务方向 | varchar | 50 |  | √ | 'normal' | 业务方向,枚举: normal :普通 return :退货 |
| 14 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 21 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 22 | finvoicesupid | 开票供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 24 | fvmisettle | VMI结算 | bpchar | 1 |  | √ | '0' | VMI结算 |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fdelisupid | 送货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 32 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 33 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 34 | fpersonid | 收货人员（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 35 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 36 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 38 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 39 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |
| 40 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_instock_pkey |  | fid |
| 2 | idx_pur_instock_fbillno |  | fbillno |
| 3 | idx_pur_instock_fsupplierid |  | fsupplierid |
| 4 | idx_pur_instock_fbizpartnerid |  | fbilldate,fbizpartnerid |

---

## 入库单分录-分表 t_pur_instockentry_o

- **表名称：** 入库单分录-分表
- **表名：** t_pur_instockentry_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foproperation | 工序编码 | varchar | 80 |  | √ | ' ' | 工序编码 |
| 3 | fmftorderid | 委外工单ID | varchar | 50 |  | √ | ' ' | 委外工单ID |
| 4 | fmftorderentryid | 委外工单行ID | varchar | 50 |  | √ | ' ' | 委外工单行ID |
| 5 | foprdescription | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | fpayentrychangetype | fpayentrychangetype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 9 | foproperationname | 工序名称 | varchar | 100 |  | √ | ' ' | 工序名称 |
| 10 | foprentryid | 工序计划工序号ID | varchar | 50 |  | √ | ' ' | 工序计划工序号ID |
| 11 | ftechno | 工序计划编码 | varchar | 80 |  | √ | ' ' | 工序计划编码 |
| 12 | foproperationid | 工序ID | varchar | 50 |  | √ | ' ' | 工序ID |
| 13 | foprentryseq | 工序计划工序号 | varchar | 20 |  | √ | ' ' | 工序计划工序号 |
| 14 | fmftorderentryseq | 委外工单分录序号 | varchar | 20 |  | √ | ' ' | 委外工单分录序号 |
| 15 | ftechid | 工序计划ID | varchar | 50 |  | √ | ' ' | 工序计划ID |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 18 | fprocessseq | 工序计划序列号 | varchar | 50 |  | √ | ' ' | 工序计划序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_instockentry_o_fid |  | fid |
| 2 | pk_pur_instockentry_o |  | fentryid |

---

## 入库单分录-分表 t_pur_instockentry_a

- **表名称：** 入库单分录-分表
- **表名：** t_pur_instockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 23 | 10 | √ | 0.000000 | 关联对账数量 |
| 4 | fmatchqty | 已核销数量 | numeric | 23 | 10 | √ | 0.000000 | 已核销数量 |
| 5 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 6 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 7 | fsrcinsentryid | 源单入库分录ID | varchar | 50 |  | √ | ' ' | 源单入库分录ID |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 11 | fsettlesupid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 14 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 15 | funmatchbaseqty | 未核销基本数量 | numeric | 23 | 10 | √ | 0 | 未核销基本数量 |
| 16 | funmatchqty | 未核销数量 | numeric | 23 | 10 | √ | 0.000000 | 未核销数量 |
| 17 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 18 | fsuminvoiceamt | fsuminvoiceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 20 | frelateinvoiceamt | 关联开票金额 | numeric | 23 | 10 | √ | 0 | 关联开票金额 |
| 21 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 22 | fsrcinsbillid | 源单入库ID | varchar | 50 |  | √ | ' ' | 源单入库ID |
| 23 | fischeckorinvoice | 对账/开票 | bpchar | 1 |  | √ | '0' | 对账/开票 |
| 24 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 25 | funmatchamt | 未核销金额 | numeric | 23 | 10 | √ | 0.000000 | 未核销金额 |
| 26 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 27 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 28 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 29 | fsuminvoiceqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 30 | frelateinvoiceqty | 关联开票数量 | numeric | 23 | 10 | √ | 0 | 关联开票数量 |
| 31 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 金额(本位币) |
| 32 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 33 | fsaloutnum | 销售发货单编码 | varchar | 80 |  | √ | ' ' | 销售发货单编码 |
| 34 | fsumcheckamt | 关联对账金额 | numeric | 23 | 10 | √ | 0.000000 | 关联对账金额 |
| 35 | fsaloutid | 销售发货单id | int8 | 64 |  | √ | 0 | 销售发货单id |
| 36 | fsaloutentryid | 销售发货单行id | int8 | 64 |  | √ | 0 | 销售发货单行id |
| 37 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 40 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |
| 41 | fmatchamt | 已核销金额 | numeric | 23 | 10 | √ | 0.000000 | 已核销金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_instockentry_a_fid |  | fid |
| 2 | idx_pur_isentry_a_fsrcentryid |  | fsrcentryid |
| 3 | t_pur_instockentry_a_pkey |  | fentryid |
| 4 | idx_pur_instockentry_a_fpobiid |  | fpobillid |
| 5 | idx_t_pur_instockentry_a_srcinsentryid |  | fsrcinsentryid |
| 6 | idx_pur_instockentry_a_fpoid |  | fpoentryid |

---

## 入库查询-关联追踪表 t_pur_instock_tc

- **表名称：** 入库查询-关联追踪表
- **表名：** t_pur_instock_tc

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
| 1 | idx_pur_instock_tc_tbill |  | ftbillid |
| 2 | t_pur_instock_tc_pkey |  | fid |
| 3 | idx_pur_instock_tc_tid |  | ftid |

---

## 入库单分录-子表 t_pur_instockentry

- **表名称：** 入库单分录-子表
- **表名：** t_pur_instockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 5 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 14 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fcheckfreeze | 对账冻结 | bpchar | 1 |  | √ | '0' | 对账冻结 |
| 17 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 18 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 19 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 21 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 23 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 C :折扣额 NULL :无 |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 27 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 31 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 32 | flotid | 批号（废弃） | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 33 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 34 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 35 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 36 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 37 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 38 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 39 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 43 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_instockentry_pkey |  | fentryid |
| 2 | idx_pur_instockentry_fmatid |  | fmaterialid |
| 3 | idx_pur_instockentry_fid_fseq |  | fid,fseq |
| 4 | idx_pur_instockentry_fpurorgid |  | fpurorgid |
