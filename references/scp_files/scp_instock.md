# 入库查询-scp_instock

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

## 入库查询-分表 t_pur_instock_a

- **表名称：** 入库查询-分表
- **表名：** t_pur_instock_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fisinitial | fisinitial | bpchar | 1 |  | √ | ' ' |  |
| 5 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 7 | fchkbillno | 对账单号 | varchar | 80 |  | √ | ' ' | 对账单号 |
| 8 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fiscentersettle | 集中结算 | bpchar | 1 |  | √ | ' ' | 集中结算 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foperatorid | 联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 6 | forgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 11 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 12 | fbusinessdirect | 业务方向 | varchar | 50 |  | √ | 'normal' | 业务方向,枚举: normal :普通 return :退货 |
| 13 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 16 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 19 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 21 | fvmisettle | VMI结算 | bpchar | 1 |  | √ | '0' | VMI结算 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 26 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 29 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 30 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 31 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 32 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 33 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 35 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 36 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 37 | fcontacterid | 销售员 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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

## 入库查询分录-分表 t_pur_instockentry_a

- **表名称：** 入库查询分录-分表
- **表名：** t_pur_instockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 19 | 6 | √ | 0.000000 | 关联对账数量 |
| 4 | fmatchqty | fmatchqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 5 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 6 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 7 | fsrcinsentryid | 来源单据入库行ID | varchar | 50 |  | √ | ' ' | 来源单据入库行ID |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 11 | fsettlesupid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 14 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 15 | funmatchbaseqty | 未核销基本数量 | numeric | 23 | 10 | √ | 0 | 未核销基本数量 |
| 16 | funmatchqty | 未核销数量 | numeric | 19 | 6 | √ | 0.000000 | 未核销数量 |
| 17 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 18 | fsuminvoiceamt | fsuminvoiceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 20 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 21 | fsrcinsbillid | 来源单据入库ID | varchar | 50 |  | √ | ' ' | 来源单据入库ID |
| 22 | fischeckorinvoice | 对账/开票 | bpchar | 1 |  | √ | '0' | 对账/开票 |
| 23 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 24 | funmatchamt | funmatchamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 25 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 26 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 27 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 28 | fsuminvoiceqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 29 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 30 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 31 | fsaloutnum | fsaloutnum | varchar | 80 |  | √ | ' ' |  |
| 32 | fsumcheckamt | 关联对账金额 | numeric | 19 | 6 | √ | 0.000000 | 关联对账金额 |
| 33 | fsaloutid | fsaloutid | int8 | 64 |  | √ | 0 |  |
| 34 | fsaloutentryid | fsaloutentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 38 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |
| 39 | fmatchamt | fmatchamt | numeric | 19 | 6 | √ | 0.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_instockentry_a_fid |  | fid |
| 2 | t_pur_instockentry_a_pkey |  | fentryid |
| 3 | idx_t_pur_instockentry_a_srcinsentryid |  | fsrcinsentryid |
| 4 | idx_pur_instockentry_a_fpoid |  | fpoentryid |

---

## 入库查询分录-子表 t_pur_instockentry

- **表名称：** 入库查询分录-子表
- **表名：** t_pur_instockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 11 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 15 | fqty | 入库数量 | numeric | 19 | 6 | √ | 0.000000 | 入库数量 |
| 16 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 17 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 19 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 23 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 25 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 27 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 29 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 30 | flotid | 批号（废弃） | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 31 | flocationid | 库位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 32 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 33 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 34 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 35 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 36 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 40 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

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
