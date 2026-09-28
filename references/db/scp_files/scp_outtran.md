# 委外调拨-scp_outtran

## 委外调拨-多语言表 t_pur_outtran_l

- **表名称：** 委外调拨-多语言表
- **表名：** t_pur_outtran_l

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
| 1 | idx_pur_outtran_l_fid |  | fid,flocaleid |
| 2 | t_pur_outtran_l_pkey |  | fpkid |

---

## 委外调拨-分表 t_pur_outtran_a

- **表名称：** 委外调拨-分表
- **表名：** t_pur_outtran_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
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
| 1 | t_pur_outtran_a_pkey |  | fid |
| 2 | idx_pur_outtran_a_fcreatetime |  | fcreatetime |

---

## 委外调拨分录-分表 t_pur_outtranentry_a

- **表名称：** 委外调拨分录-分表
- **表名：** t_pur_outtranentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 本位币税额 | numeric | 19 | 6 | √ | 0.000000 | 本位币税额 |
| 3 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 4 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 5 | fgoodsid | 供方商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 7 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fgoodsdesc | 供方商品描述 | varchar | 255 |  | √ | ' ' | 供方商品描述 |
| 11 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 12 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 13 | flocamount | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 14 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 16 | floctaxamount | 本位币价税合计 | numeric | 19 | 6 | √ | 0.000000 | 本位币价税合计 |
| 17 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 20 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_outtranentry_a_pkey |  | fentryid |
| 2 | idx_pur_outtranentry_a_fid |  | fid |

---

## 委外调拨分录-子表 t_pur_outtranentry

- **表名称：** 委外调拨分录-子表
- **表名：** t_pur_outtranentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 3 | fmaterialid | 商品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 8 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 11 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 12 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 13 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 14 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 15 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 16 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 19 | flotid | 批号 | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 20 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 21 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 22 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 23 | fmaterialdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_outtranentry_pkey |  | fentryid |
| 2 | idx_pur_outtranentry_fmatid |  | fmaterialid |
| 3 | idx_pur_outtranentry_fid_fseq |  | fid,fseq |

---

## 委外调拨-主表 t_pur_outtran

- **表名称：** 委外调拨-主表
- **表名：** t_pur_outtran

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 6 | forgid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 10 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 11 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | finvorgid | 调入库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 15 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 16 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :委外直接调拨 |
| 17 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 18 | fpersonid | 仓管员 | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 19 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 20 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 21 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 22 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 23 | fbillno | 调拨单号 | varchar | 80 |  | √ | ' ' | 调拨单号 |
| 24 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_outtran_fbillno |  | fbillno |
| 2 | idx_pur_outtran_fbilldate |  | fbilldate |
| 3 | t_pur_outtran_pkey |  | fid |
| 4 | idx_pur_outtran_fbizpartnerid |  | fbizpartnerid |
