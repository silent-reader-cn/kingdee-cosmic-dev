# 订单变更-scp_ordchange

## 订单变更-多语言表 t_pur_ordchange_l

- **表名称：** 订单变更-多语言表
- **表名：** t_pur_ordchange_l

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
| 1 | t_pur_ordchange_l_pkey |  | fpkid |
| 2 | idx_pur_ordchange_l_fid |  | fid,flocaleid |

---

## 关联子实体-子表 t_pur_ordchangentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_ordchangentry_lk

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
| 1 | t_pur_ordchangentry_lk_pkey |  | fpkid |

---

## 订单变更-主表 t_pur_ordchange

- **表名称：** 订单变更-主表
- **表名：** t_pur_ordchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | forgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fpayeesupid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 11 | fcentersettle | 集中结算 | bpchar | 1 |  | √ | ' ' | 集中结算 |
| 12 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 13 | fchgreasonid | 变更原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 14 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 15 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 19 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 21 | finvoicesupid | 开票供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fdelisupid | 送货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | freason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |
| 26 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 28 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 29 | fsupplierid | 销售方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 32 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 33 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 34 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 35 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 37 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 38 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 39 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 40 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 41 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_ordchange_fbizid |  | fbizpartnerid |
| 2 | t_pur_ordchange_pkey |  | fid |
| 3 | idx_pur_ordchange_fbilldate |  | fbilldate |
| 4 | idx_pur_ordchange_fbillno |  | fbillno |

---

## 订单变更-反写记录表 t_pur_ordchange_wb

- **表名称：** 订单变更-反写记录表
- **表名：** t_pur_ordchange_wb

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
| 1 | t_pur_ordchange_wb_pkey |  | fentryid |

---

## 订单变更-分表 t_pur_ordchange_a

- **表名称：** 订单变更-分表
- **表名：** t_pur_ordchange_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 2 :采购方 1 :供应商 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 13 | fsourcebillid | fsourcebillid | varchar | 50 |  | √ | ' ' |  |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_ordchange_a_pkey |  | fid |
| 2 | idx_pur_ordchange_a_ftime |  | fcreatetime |

---

## 订单变更-关联追踪表 t_pur_ordchange_tc

- **表名称：** 订单变更-关联追踪表
- **表名：** t_pur_ordchange_tc

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
| 1 | idx_pur_ordchange_tc_tid |  | ftid |
| 2 | idx_pur_ordchange_tc_tbill |  | ftbillid |
| 3 | t_pur_ordchange_tc_pkey |  | fid |

---

## 变更单分录-子表 t_pur_ordchangentry

- **表名称：** 变更单分录-子表
- **表名：** t_pur_ordchangentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 确认交货日期 | timestamp | 0 |  |  | null | 确认交货日期 |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fpromiseday | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 12 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 14 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 15 | fqty | 确认数量 | numeric | 19 | 6 | √ | 0.000000 | 确认数量 |
| 16 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 17 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 19 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 22 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 23 | fchgtype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :更改 2 :追加 3 :冻结 4 :终止 |
| 24 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 26 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 27 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 28 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 29 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 33 | fpromisedayold | 原承诺日期 | timestamp | 0 |  |  | null | 原承诺日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_ordchang_fmatid |  | fmaterialid |
| 2 | t_pur_ordchangentry_pkey |  | fentryid |
| 3 | idx_pur_ordchang_fid_fseq |  | fid,fseq |

---

## 变更单分录-分表 t_pur_ordchangentry_a

- **表名称：** 变更单分录-分表
- **表名：** t_pur_ordchangentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 3 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 4 | fsaloutbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0 | 发货上限基本数量 |
| 5 | fsaloutqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0 | 发货上限数量 |
| 6 | fdelidateold | 原交货日期 | timestamp | 0 |  |  | null | 原交货日期 |
| 7 | fsaloutratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0 | 发货欠发比率(%) |
| 8 | ftaxrateidold | 原税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 9 | fdctrateold | 原单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 原单位折扣(率) |
| 10 | fsaloutqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0 | 发货下限数量 |
| 11 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fiscontrolamountup | 控制上限金额 | bpchar | 1 |  | √ | '0' | 控制上限金额 |
| 13 | fdeliaddrold | 原交货地址 | varchar | 255 |  | √ | ' ' | 原交货地址 |
| 14 | ftaxrateold | 原税率(%) | numeric | 19 | 6 | √ | 0.000000 | 原税率(%) |
| 15 | fsourcebillentryid | fsourcebillentryid | varchar | 50 |  | √ | ' ' |  |
| 16 | ftaxpriceold | 原含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原含税单价 |
| 17 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 18 | fsrcbillentryid | fsrcbillentryid | varchar | 50 |  | √ | ' ' |  |
| 19 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 20 | fsaloutrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0 | 发货超发比率(%) |
| 21 | famountup | 上限金额 | numeric | 23 | 10 | √ | 0 | 上限金额 |
| 22 | fpriceold | 原单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原单价 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fqtyold | 原数量 | numeric | 19 | 6 | √ | 0.000000 | 原数量 |
| 25 | fpromisedayold | fpromisedayold | timestamp | 0 |  |  | null |  |
| 26 | fsaloutbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0 | 发货下限基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_ordchang_a_fpoid |  | fpoentryid |
| 2 | t_pur_ordchangentry_a_pkey |  | fentryid |
| 3 | idx_pur_ordchang_a_fid |  | fid |

---

## 关联子实体-子表 t_pur_ordchange_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_ordchange_lk

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
| 1 | t_pur_ordchange_lk_pkey |  | fpkid |
