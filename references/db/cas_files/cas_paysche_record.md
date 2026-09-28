# 付款排程付款记录-cas_paysche_record

## 付款排程付款记录-主表 t_cas_paysche_record

- **表名称：** 付款排程付款记录-主表
- **表名：** t_cas_paysche_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayscheid | 排程单ID | int8 | 64 |  | √ | 0 | 排程单ID |
| 3 | fpayentryid | 付款单分录ID | int8 | 64 |  | √ | 0 | 付款单分录ID |
| 4 | fpaybatchid | 付款批次号 | varchar | 60 |  | √ | ' ' | 付款批次号 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | foptype | 操作类型 | varchar | 30 |  | √ | ' ' | 操作类型,枚举: pay :付款 back :退单 delete :删除 |
| 7 | fpayid | 付款单ID | int8 | 64 |  | √ | 0 | 付款单ID |
| 8 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 9 | famountbefore | 操作前付款分录金额 | numeric | 19 | 6 | √ | 0 | 操作前付款分录金额 |
| 10 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | famountafter | 操作后付款分录金额 | numeric | 19 | 6 | √ | 0 | 操作后付款分录金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_paysche_record |  | fid |
| 2 | idx_t_cas_paysche_recordbatch |  | fpaybatchid |
