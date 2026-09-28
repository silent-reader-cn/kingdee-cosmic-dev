# 物料供应-ssm_itemsupply

## 单据体-子表 t_ssm_supplydetail

- **表名称：** 单据体-子表
- **表名：** t_ssm_supplydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 3 | fsupplytype | 供应类型 | varchar | 50 |  | √ | ' ' | 供应类型,枚举: 0 :重复生产工单 1 :即时库存 3 :生产工单 4 :委外工单 5 :采购订单 6 :滚动采购交货计划 7 :滚动采购预测计划 |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | freleasedate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcbill | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 8 | ffullfillsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fmaterialauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fdemandorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbaseqtytosupply | 供应基本数量 | numeric | 23 | 10 | √ | 0 | 供应基本数量 |
| 14 | fqtytosupply | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 15 | fbizunitid | 业务单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 17 | fqtycompleted | 已收货数量 | numeric | 23 | 10 | √ | 0 | 已收货数量 |
| 18 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fmaterialmasterid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | fduedate | 收货日期 | timestamp | 0 |  |  | null | 收货日期 |
| 22 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 23 | fyieldpercent | 成品率% | numeric | 23 | 2 | √ | 0 | 成品率% |
| 24 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 25 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 26 | freceiveorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fqtytostart | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 28 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 29 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 30 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_supplydetail |  | fentryid |
| 2 | idx_ssm_supplydetail_fk |  | fid |

---

## 物料供应-主表 t_ssm_itemsupply

- **表名称：** 物料供应-主表
- **表名：** t_ssm_itemsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_itemsupply |  | fid |
| 2 | idx_ssm_itemsupply_m0 |  | fbillno |
