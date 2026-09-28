# 成本记录结转明细-cal_costrecord_detail

## 成本记录结转明细-主表 t_cal_costrecord_detail

- **表名称：** 成本记录结转明细-主表
- **表名：** t_cal_costrecord_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fstepamt | 标准成本本阶金额 | numeric | 23 | 10 | √ | 0 | 标准成本本阶金额 |
| 6 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 7 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 8 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 12 | fentryid | 成本记录分录ID | int8 | 64 |  | √ | 0 | 成本记录分录ID |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | funitstandardcost | 单位标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costrecord_detail_pkey |  | fdetailid |
| 2 | idx_cal_crddetail_elementid |  | fcostelementid |
| 3 | idx_cal_costrecord_detail_sub |  | fentryid,fcostsubelementid |
| 4 | idx_cal_crddetail_entryid |  | fentryid,fdetailid,fstandardcost,factualcost |
| 5 | idx_cal_crddetail_subelementid |  | fcostsubelementid |
