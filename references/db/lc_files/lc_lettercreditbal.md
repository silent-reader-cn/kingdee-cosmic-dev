# 开证余额表-lc_lettercreditbal

## 开证余额表-主表 t_lc_lettercreditbal

- **表名称：** 开证余额表-主表
- **表名：** t_lc_lettercreditbal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | fvalibalance | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 5 | famount | 当前余额 | numeric | 23 | 10 | √ | 0 | 当前余额 |
| 6 | fcreditamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 7 | flstbalance | 上日余额 | numeric | 23 | 10 | √ | 0 | 上日余额 |
| 8 | fdebitamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 9 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | faccountbankid | 开证 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 11 | fcompanyid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercreditbal_comp |  | fbizdate,fcompanyid,fcurrencyid |
| 2 | pk_t_lc_lettercreditbal |  | fid |
