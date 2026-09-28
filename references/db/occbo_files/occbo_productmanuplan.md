# 产品运作计划-occbo_productmanuplan

## 计划明细-子表 t_occbo_prodmanuplan_ee

- **表名称：** 计划明细-子表
- **表名：** t_occbo_prodmanuplan_ee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 销售计划数量 | numeric | 23 | 10 | √ | 0 | 销售计划数量 |
| 3 | frequireqty | 运作计划数量 | numeric | 23 | 10 | √ | 0 | 运作计划数量 |
| 4 | fsrcbillno | 来源产品计划编码 | varchar | 80 |  | √ | ' ' | 来源产品计划编码 |
| 5 | fsrcbillid | 来源产品计划主键 | int8 | 64 |  | √ | 0 | 来源产品计划主键 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsaleunitid | 销售计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fmanufactureorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsrcbillname | 来源产品计划名称 | varchar | 80 |  | √ | ' ' | 来源产品计划名称 |
| 11 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fbaseqty | 基本计划数量 | numeric | 23 | 10 | √ | 0 | 基本计划数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | frequireqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_prodmanuplanee_fid |  | fid |
| 2 | pk_occbo_prodmanuplan_ee |  | fentryid |

---

## 产品运作计划-主表 t_occbo_prodmanuplan

- **表名称：** 产品运作计划-主表
- **表名：** t_occbo_prodmanuplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fassessentityid | 计划月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillno | 计划编号 | varchar | 80 |  | √ | ' ' | 计划编号 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbilltypeid | 计划方案 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_prodmanuplan |  | fid |
| 2 | idx_occbo_prodmanuplan_billno |  | fbillno |
