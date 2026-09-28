# 物料供应-psw_itemsupply

## 物料供应-主表 t_psw_itemsupply

- **表名称：** 物料供应-主表
- **表名：** t_psw_itemsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 8 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_item_suply |  | fbillno,fid |
| 2 | pk_t_psw_itemsupply |  | fid |

---

## 单据体-子表 t_psw_supplydetail

- **表名称：** 单据体-子表
- **表名：** t_psw_supplydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 3 | fsupplytype | 供应类型 | bpchar | 1 |  | √ | '0' | 供应类型,枚举: 0 :重复生产工单 1 :即时库存 |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freleasedate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 7 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | 物料版本 bd_bomversion_new |
| 8 | fmaterialauxprop | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 9 | fbaseunitid | 基本单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 10 | fdemandorgid | 需求组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 11 | fbaseqtytosupply | 供应基本数量 | numeric | 23 | 10 |  | null | 供应基本数量 |
| 12 | fbizunitid | 业务单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 13 | fqtytosupply | 供应数量 | numeric | 23 | 10 |  | null | 供应数量 |
| 14 | fwarehouseid | 仓库 | int8 | 64 |  |  | null | 仓库 bd_warehouse |
| 15 | fqtycompleted | 已完工数量 | numeric | 23 | 10 |  | null | 已完工数量 |
| 16 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 17 | fmaterialmasterid | 物料编码 | int8 | 64 |  |  | null | 物料 bd_material |
| 18 | fproductionlineid | 生产线 | int8 | 64 |  |  | null | 生产线 arm_linecapacity |
| 19 | fduedate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 20 | fyieldpercent | 成品率% | numeric | 23 | 10 |  | null | 成品率% |
| 21 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 22 | flocationid | 仓位 | int8 | 64 |  |  | null | 仓位 bd_location |
| 23 | fqtytostart | 订单数量 | numeric | 23 | 10 |  | null | 订单数量 |
| 24 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 25 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 26 | fsupplyorgid | 供应组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_supplydetail |  | fentryid |
| 2 | idx_t_psw_suply_detail |  | fid |
