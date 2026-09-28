# 收款查询-scp_pay

## 关联子实体-子表 t_pur_payentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_payentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | famount_old | 应收金额_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | famount | 应收金额_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_payentry_lk_pkey |  | fpkid |

---

## 收款查询-关联追踪表 t_pur_pay_tc

- **表名称：** 收款查询-关联追踪表
- **表名：** t_pur_pay_tc

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
| 1 | idx_pur_pay_tc_tid |  | ftid |
| 2 | t_pur_pay_tc_pkey |  | fid |
| 3 | idx_pur_pay_tc_tbill |  | ftbillid |

---

## 收款单分录-子表 t_pur_payentry

- **表名称：** 收款单分录-子表
- **表名：** t_pur_payentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 5 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 7 | fmaterialid | 商品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 9 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 12 | famount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 13 | fpayamount | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 14 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | ffeeamount | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 16 | fdctamount | 折扣金额 | numeric | 19 | 6 | √ | 0.000000 | 折扣金额 |
| 17 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 18 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_payentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_payentry_fmaterialid |  | fmaterialid |
| 3 | t_pur_payentry_pkey |  | fentryid |

---

## 收款查询-反写记录表 t_pur_pay_wb

- **表名称：** 收款查询-反写记录表
- **表名：** t_pur_pay_wb

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
| 1 | t_pur_pay_wb_pkey |  | fentryid |

---

## 收款查询-多语言表 t_pur_pay_l

- **表名称：** 收款查询-多语言表
- **表名：** t_pur_pay_l

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
| 1 | idx_pur_pay_l_fid_flocaleid |  | fid,flocaleid |
| 2 | t_pur_pay_l_pkey |  | fpkid |

---

## 收款查询-分表 t_pur_pay_a

- **表名称：** 收款查询-分表
- **表名：** t_pur_pay_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_pay_a_fcreatetime |  | fcreatetime |
| 2 | t_pur_pay_a_pkey |  | fid |

---

## 收款单分录-分表 t_pur_payentry_a

- **表名称：** 收款单分录-分表
- **表名：** t_pur_payentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocdctamount | 折扣金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 折扣金额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | flocpayamount | 实付金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 实付金额(本位币) |
| 5 | fgoodsid | 供方商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | flocfeeamount | 手续费(本位币) | numeric | 19 | 6 | √ | 0.000000 | 手续费(本位币) |
| 7 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 8 | fgoodsdesc | 供方商品描述 | varchar | 255 |  | √ | ' ' | 供方商品描述 |
| 9 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 10 | flocamount | 应付金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 应付金额(本位币) |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 13 | fmaterialdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 16 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_payentry_a_fid |  | fid |
| 2 | t_pur_payentry_a_pkey |  | fentryid |

---

## 收款查询-主表 t_pur_pay

- **表名称：** 收款查询-主表
- **表名：** t_pur_pay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumdctamount | 折扣金额 | numeric | 19 | 6 | √ | 0.000000 | 折扣金额 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fpaybankid | fpaybankid | int8 | 64 |  | √ | 0 |  |
| 5 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | foperatorid | 客户联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 7 | forgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fpayeebankid | fpayeebankid | int8 | 64 |  | √ | 0 |  |
| 10 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 11 | ffee | 坐扣手续费 | numeric | 23 | 10 | √ | 0 | 坐扣手续费 |
| 12 | fpayeesupid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fbiztype | 收款类型 | bpchar | 1 |  | √ | ' ' | 收款类型,枚举: 1 :销售收款 2 :预收款 3 :退销售收款 4 :退预收款 5 :代收款 6 :退代收款 |
| 14 | fsumamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 15 | fpayacc | 付款账号 | varchar | 50 |  | √ | ' ' | 付款账号 |
| 16 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fpayaccid | fpayaccid | int8 | 64 |  | √ | 0 |  |
| 19 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fsumpayamount | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 21 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fpayeeacc | 收款账号 | varchar | 50 |  | √ | ' ' | 收款账号 |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 26 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 pur_paycond |
| 28 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | fpayeeaccid | fpayeeaccid | int8 | 64 |  | √ | 0 |  |
| 31 | fsumqty | fsumqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 32 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 33 | fsupplierid | 销售方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 34 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 35 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 36 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 37 | fpayeebank | 收款银行 | varchar | 100 |  | √ | ' ' | 收款银行 |
| 38 | fpaybank | 付款银行 | varchar | 100 |  | √ | ' ' | 付款银行 |
| 39 | fpersonid | 客户联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 40 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fsettleno | 结算号 | varchar | 50 |  | √ | ' ' | 结算号 |
| 42 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 43 | fcontacterid | 业务员 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 44 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_pay_fbillno |  | fbillno |
| 2 | idx_pur_pay_fbilldate |  | fbilldate |
| 3 | t_pur_pay_pkey |  | fid |
| 4 | idx_pur_pay_fbizpartnerid |  | fbizpartnerid |
