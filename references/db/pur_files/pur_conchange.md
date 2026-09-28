# 合同变更-pur_conchange

## 合同变更-反写记录表 t_pur_conchange_wb

- **表名称：** 合同变更-反写记录表
- **表名：** t_pur_conchange_wb

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
| 1 | t_pur_conchange_wb_pkey |  | fentryid |

---

## 合同变更-主表 t_pur_conchange

- **表名称：** 合同变更-主表
- **表名：** t_pur_conchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fdateto | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 4 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 8 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 pur_paycond](../basedata_files/pur_paycond.md) |
| 9 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 13 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 14 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 15 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 16 | fdatefrom | 有效期从 | timestamp | 0 |  |  | null | 有效期从 |
| 17 | fchgreasonid | 变更原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 18 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 19 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_conchange_pkey |  | fid |
| 2 | idx_pur_conchange_fbillno |  | fbillno |
| 3 | idx_pur_conchange_fbilldate |  | fbilldate |

---

## 合同变更-关联追踪表 t_pur_conchange_tc

- **表名称：** 合同变更-关联追踪表
- **表名：** t_pur_conchange_tc

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
| 1 | idx_pur_conchange_tc_tid |  | ftid |
| 2 | idx_pur_conchange_tc_tbill |  | ftbillid |
| 3 | t_pur_conchange_tc_pkey |  | fid |

---

## 物料变更分录-子表 t_pur_conchangentry

- **表名称：** 物料变更分录-子表
- **表名：** t_pur_conchangentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 3 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 折扣率(%) |
| 4 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fmatclassid | 物料分类 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: null :null null :null |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 13 | fchgtype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :修改 2 :取消 3 :新增 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 16 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 17 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_conchangentry_fmatid |  | fmaterialid |
| 2 | t_pur_conchangentry_pkey |  | fentryid |
| 3 | idx_pur_conchangentry_fid_fseq |  | fid,fseq |

---

## 计划变更分录-子表 t_pur_conchangepay

- **表名称：** 计划变更分录-子表
- **表名：** t_pur_conchangepay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpayamount | 应付金额 | numeric | 19 | 6 | √ | 0.000000 | 应付金额 |
| 6 | fchgtype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :修改 2 :取消 3 :新增 |
| 7 | fpaydateold | 原应付日期 | timestamp | 0 |  |  | null | 原应付日期 |
| 8 | fpayrate | 应付比例(%) | numeric | 19 | 6 | √ | 0.000000 | 应付比例(%) |
| 9 | fpayamountold | 原应付金额 | numeric | 19 | 6 | √ | 0.000000 | 原应付金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fpayrateold | 原应付比例(%) | numeric | 19 | 6 | √ | 0.000000 | 原应付比例(%) |
| 12 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |
| 13 | fpaydate | 应付日期 | timestamp | 0 |  |  | null | 应付日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_conchangepay_pkey |  | fentryid |
| 2 | idx_pur_conchangepay_fid_fseq |  | fid,fseq |

---

## 条款变更分录-子表 t_pur_conchangeitem

- **表名称：** 条款变更分录-子表
- **表名：** t_pur_conchangeitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 条款名称 | varchar | 255 |  | √ | ' ' | 条款名称 |
| 3 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 4 | fitemoldid | 原条款编码 | int8 | 64 |  | √ | 0 | [采购条款 pur_item](../pbd_files/pur_item.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 条款备注 | varchar | 255 |  | √ | ' ' | 条款备注 |
| 7 | fchgtype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :修改 2 :取消 3 :新增 |
| 8 | fnameold | 原条款名称 | varchar | 255 |  | √ | ' ' | 原条款名称 |
| 9 | fitemid | 条款编码 | int8 | 64 |  | √ | 0 | [采购条款 pur_item](../pbd_files/pur_item.md) |
| 10 | fnoteold | 原条款备注 | varchar | 255 |  | √ | ' ' | 原条款备注 |
| 11 | ftypeid | 条款类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 12 | fcontentold | 原条款内容 | varchar | 500 |  | √ | ' ' | 原条款内容 |
| 13 | ftypeoldid | 原条款类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 14 | fcontent | 条款内容 | varchar | 500 |  | √ | ' ' | 条款内容 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_conchangeitem_pkey |  | fentryid |
| 2 | idx_pur_conchangeitem_fid_fseq |  | fid,fseq |

---

## 费用变更分录-子表 t_pur_conchangecost

- **表名称：** 费用变更分录-子表
- **表名：** t_pur_conchangecost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrateold | 原税率(%) | numeric | 19 | 6 | √ | 0.000000 | 原税率(%) |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | fcostoldid | 原费用项目 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 9 | fchgtype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :修改 2 :取消 3 :新增 |
| 10 | fcostid | 费用项目 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | famountold | 原金额 | numeric | 19 | 6 | √ | 0.000000 | 原金额 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_conchangecost_pkey |  | fentryid |
| 2 | idx_pur_conchangecost_fid_fseq |  | fid,fseq |

---

## 合同变更-分表 t_pur_conchange_a

- **表名称：** 合同变更-分表
- **表名：** t_pur_conchange_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_conchange_a_ftime |  | fcreatetime |
| 2 | t_pur_conchange_a_pkey |  | fid |

---

## 物料变更分录-分表 t_pur_conchangentry_a

- **表名称：** 物料变更分录-分表
- **表名：** t_pur_conchangentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrateold | 原税率(%) | numeric | 19 | 6 | √ | 0.000000 | 原税率(%) |
| 3 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 4 | fdctrateold | 原折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 原折扣率(%) |
| 5 | fpriceold | 原单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原单价 |
| 6 | ftaxpriceold | 原含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原含税单价 |
| 7 | fdeliaddrold | 原交货地址 | varchar | 255 |  | √ | ' ' | 原交货地址 |
| 8 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 9 | fdelidateold | 原交货日期 | timestamp | 0 |  |  | null | 原交货日期 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fqtyold | 原数量 | numeric | 19 | 6 | √ | 0.000000 | 原数量 |
| 12 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_conchangentry_a_fid |  | fid |
| 2 | t_pur_conchangentry_a_pkey |  | fentryid |
| 3 | idx_pur_conchangentry_a_fpcid |  | fpcentryid |

---

## 合同变更-多语言表 t_pur_conchange_l

- **表名称：** 合同变更-多语言表
- **表名：** t_pur_conchange_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_conchange_l_fid |  | fid,flocaleid |
| 2 | t_pur_conchange_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_pur_conchangentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_conchangentry_lk

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
| 1 | t_pur_conchangentry_lk_pkey |  | fpkid |
