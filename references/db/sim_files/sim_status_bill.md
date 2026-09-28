# 发票状态统计单据-sim_status_bill

## 发票状态统计单据-主表 t_sim_status_bill

- **表名称：** 发票状态统计单据-主表
- **表名：** t_sim_status_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcancelbluetotalamount | 已作废蓝票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已作废蓝票金额 |
| 3 | fblueinvoicenum | 未作废蓝票数量 | int8 | 64 |  | √ | 0 | 未作废蓝票数量 |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 5 | fbluetotalamount | 未作废蓝票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未作废蓝票金额 |
| 6 | fissuedevice | 开票设备编号 | varchar | 50 |  | √ | ' ' | 开票设备编号 |
| 7 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 026 :电子普票 028 :电子专票 |
| 8 | fsalername | 销方名称 | varchar | 50 |  | √ | ' ' | 销方名称 |
| 9 | ftaxno | 销方税号 | varchar | 50 |  | √ | ' ' | 销方税号 |
| 10 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 11 | fredinvoicenum | 未作废红票数量 | int8 | 64 |  | √ | 0 | 未作废红票数量 |
| 12 | fbluetotaltax | 未作废蓝票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 未作废蓝票税额 |
| 13 | fredtotaltax | 未作废红票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 未作废红票税额 |
| 14 | fcancelbluenum | 已作废蓝票数量 | int8 | 64 |  | √ | 0 | 已作废蓝票数量 |
| 15 | fredtotalamount | 未作废红票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未作废红票金额 |
| 16 | fcancelbluetotaltax | 已作废蓝票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已作废蓝票税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_status_bill |  | fid |
| 2 | idx_sim_status_bill |  | fdate |
