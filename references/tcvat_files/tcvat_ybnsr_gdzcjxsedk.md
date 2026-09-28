# 一般纳税人固定资产进项税额抵扣情况-tcvat_ybnsr_gdzcjxsedk

## 一般纳税人固定资产进项税额抵扣情况-主表 t_tcvat_ybnsr_gdzcjxsedk

- **表名称：** 一般纳税人固定资产进项税额抵扣情况-主表
- **表名：** t_tcvat_ybnsr_gdzcjxsedk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1-项目 2 :2-增值税专用发票 3 :3-海关进口增值税专用缴款书 4 :4-合计 |
| 3 | fdqdkgdzcjxse | 1-当期申报抵扣的固定资产进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 1-当期申报抵扣的固定资产进项税额 |
| 4 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 5 | fgdzcjxselj | 2-申报抵扣的固定资产进项税额累计 | numeric | 23 | 10 | √ | 0.0000000000 | 2-申报抵扣的固定资产进项税额累计 |
| 6 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ybnsr_gdzcjxsedk2 |  | fewblxh,fsbbid |
| 2 | t_tcvat_ybnsr_gdzcjxsedk_pkey |  | fid |
| 3 | idx_tcvat_ybnsr_gdzcjxsedk |  | fsbbid |
