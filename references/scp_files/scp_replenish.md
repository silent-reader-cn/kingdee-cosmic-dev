# 补货申请-scp_replenish

## 补货申请分录-子表 t_pur_replenishentry

- **表名称：** 补货申请分录-子表
- **表名：** t_pur_replenishentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallotqty | 分配数量 | numeric | 19 | 6 | √ | 0.000000 | 分配数量 |
| 3 | fmaterialid | 商品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fneedqty | 需求数量 | numeric | 19 | 6 | √ | 0.000000 | 需求数量 |
| 5 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: null :null null :null |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fsafeqty | 安全库存 | numeric | 19 | 6 | √ | 0.000000 | 安全库存 |
| 9 | fonwayqty | 在途数量 | numeric | 19 | 6 | √ | 0.000000 | 在途数量 |
| 10 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 11 | fqty | 实际数量 | numeric | 19 | 6 | √ | 0.000000 | 实际数量 |
| 12 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 13 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 14 | fbatqty | 订货批量 | numeric | 19 | 6 | √ | 0.000000 | 订货批量 |
| 15 | finvqty | 库存数量 | numeric | 19 | 6 | √ | 0.000000 | 库存数量 |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 18 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 19 | flotid | 批号 | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 20 | fadvqty | 建议补货 | numeric | 19 | 6 | √ | 0.000000 | 建议补货 |
| 21 | freqqty | 净需求量 | numeric | 19 | 6 | √ | 0.000000 | 净需求量 |
| 22 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 23 | fmaterialdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_replenishentry_pkey |  | fentryid |
| 2 | idx_pur_replenish_fid_fseq |  | fid,fseq |
| 3 | idx_pur_replenish_fmatid |  | fmaterialid |

---

## 补货申请分录-分表 t_pur_replenishentry_a

- **表名称：** 补货申请分录-分表
- **表名：** t_pur_replenishentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 3 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 4 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 5 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 9 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 15 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_replenishentry_a_pkey |  | fentryid |
| 2 | idx_pur_replenishentry_a_fid |  | fid |

---

## 补货申请-主表 t_pur_replenish

- **表名称：** 补货申请-主表
- **表名：** t_pur_replenish

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 3 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 6 | forgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 9 | fbillno | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 10 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_replenish_fbilldate |  | fbilldate |
| 2 | idx_pur_replenish_fbillno |  | fbillno |
| 3 | t_pur_replenish_pkey |  | fid |
| 4 | idx_pur_replenish_fbizid |  | fbizpartnerid |

---

## 补货申请-分表 t_pur_replenish_a

- **表名称：** 补货申请-分表
- **表名：** t_pur_replenish_a

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
| 1 | idx_pur_replenish_a_ftime |  | fcreatetime |
| 2 | t_pur_replenish_a_pkey |  | fid |

---

## 补货申请-多语言表 t_pur_replenish_l

- **表名称：** 补货申请-多语言表
- **表名：** t_pur_replenish_l

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
| 1 | t_pur_replenish_l_pkey |  | fpkid |
| 2 | idx_pur_replenish_l_fid |  | fid,flocaleid |
