# 核算成本记录（委外）-cal_costrecordom

## 成本要素明细-子表 t_cal_costrecordomentry

- **表名称：** 成本要素明细-子表
- **表名：** t_cal_costrecordomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 3 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_costrecordomentry |  | fentryid |
| 2 | idx_cal_costrecordomentry_id |  | fid |

---

## 核算成本记录（委外）-主表 t_cal_costrecordom

- **表名称：** 核算成本记录（委外）-主表
- **表名：** t_cal_costrecordom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizentryid | 业务单据分录内码 | int8 | 64 |  | √ | 0 | 业务单据分录内码 |
| 3 | fmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 4 | fbizid | 业务单据内码 | int8 | 64 |  | √ | 0 | 业务单据内码 |
| 5 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0 | 采购成本 |
| 6 | frecordid | 核算成本记录内码 | int8 | 64 |  | √ | 0 | 核算成本记录内码 |
| 7 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 9 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0 | 委外费用 |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 11 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0 | 材料成本 |
| 12 | fresource | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 13 | frecordentryid | 核算成本记录分录内码 | int8 | 64 |  | √ | 0 | 核算成本记录分录内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costrecordom_b |  | fbizentryid,fcostaccountid |
| 2 | idx_cal_costrecordom_r |  | frecordentryid |
| 3 | pk_cal_costrecordom |  | fid |
