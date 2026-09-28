# 成本还原结果-cal_cr_costrcyresult

## 成本还原结果-主表 t_cal_cr_costrcyresult

- **表名称：** 成本还原结果-主表
- **表名：** t_cal_cr_costrcyresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fcfientryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 5 | fcfiid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fcfiqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | frtpperiodid | 追溯期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 9 | frtpplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 10 | frangetype | 计算类型 | varchar | 50 |  | √ | ' ' | 计算类型,枚举: 1 :期末结存 2 :出库 3 :入库 |
| 11 | fsourcetype | 数据来源类型 | varchar | 50 |  | √ | ' ' | 数据来源类型,枚举: 0 :余额表 1 :核算成本记录 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | frecoveryamount | 还原金额 | numeric | 23 | 10 | √ | 0 | 还原金额 |
| 14 | fcfibillno | 源单编码 | varchar | 50 |  | √ | ' ' | 源单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_cr_costrcyresult |  | fid |
| 2 | idx_cal_cr_costrcyresult_m0 |  | frtpplanid,fcostaccountid,frtpperiodid,fmaterialid |
