# 航空运输企业分支机构传递单-取得进项税额情况-tcvat_fzjg_inputtax_state

## 航空运输企业分支机构传递单-取得进项税额情况-主表 t_tcvat_fzjg_input_state

- **表名称：** 航空运输企业分支机构传递单-取得进项税额情况-主表
- **表名：** t_tcvat_fzjg_input_state

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fje | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 4 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 |
| 5 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 6 | fdate | 认证/稽核月份 | timestamp | 0 |  |  | null | 认证/稽核月份 |
| 7 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 8 | finvoicecodeno | 发票代码及号码/缴款书号码 | varchar | 50 |  | √ | ' ' | 发票代码及号码/缴款书号码 |
| 9 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fzjg_input_state |  | fsbbid |
| 2 | idx_tcvat_fzjg_input_state2 |  | fewblxh,fsbbid |
| 3 | pk_tcvat_fzjg_input_state |  | fid |
