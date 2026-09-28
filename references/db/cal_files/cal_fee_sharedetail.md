# 费用分摊明细-cal_fee_sharedetail

## 费用分摊明细-主表 t_cal_sharedetailentry

- **表名称：** 费用分摊明细-主表
- **表名：** t_cal_sharedetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 2 | fsharercdid | 费用分摊记录id | int8 | 64 |  | √ | 0 | 费用分摊记录id |
| 3 | fasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fasstacttype | 往来类型 | varchar | 30 |  | √ | 'bd_supplier' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 |
| 6 | fshareamount | 差额分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 差额分摊金额 |
| 7 | ffeeupdatetype | 费用更新成本类型 | varchar | 30 |  | √ | ' ' | 费用更新成本类型,枚举: |
| 8 | fcostrecordid | 核算成本记录id | int8 | 64 |  | √ | 0 | 核算成本记录id |
| 9 | frealshareamount | 页面分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 页面分摊金额 |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fentryid | 核算成本记录行id | int8 | 64 |  | √ | 0 | 核算成本记录行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_sharedetailentry_pkey |  | fdetailid |
| 2 | idx_cal_sharede_cre |  | fentryid |
