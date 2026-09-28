# 成本调整单结转明细-cal_costadjust_detail

## 成本调整单结转明细-主表 t_cal_costadjust_detail

- **表名称：** 成本调整单结转明细-主表
- **表名：** t_cal_costadjust_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 2 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | 成本调整单分录ID | int8 | 64 |  | √ | 0 | 成本调整单分录ID |
| 6 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costadjust_detail_pkey |  | fdetailid |
| 2 | idx_cal_costadjust_detail_sub |  | fentryid,fcostsubelementid |
| 3 | idx_cal_cadetail_entryid |  | fentryid |
