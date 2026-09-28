# 航空运输企业分支机构传递单-已缴纳增值税情况-tcvat_fzjg_taxpay_state

## 航空运输企业分支机构传递单-已缴纳增值税情况-主表 t_tcvat_fzjg_taxpay_state

- **表名称：** 航空运输企业分支机构传递单-已缴纳增值税情况-主表
- **表名：** t_tcvat_fzjg_taxpay_state

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :分支机构 2 :交通运输服务 3 :有形动产租赁服务 4 :其他《应税服务范围注释》所列业务 5 :小计 |
| 4 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 5 | fyzl | 预征率 | numeric | 23 | 10 | √ | 0.0000000000 | 预征率 |
| 6 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 7 | fbjse | 补缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 补缴税额 |
| 8 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 9 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 10 | ffzjgmc | 分支机构名称 | varchar | 50 |  | √ | ' ' | 分支机构名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fzjg_taxpay_state |  | fsbbid |
| 2 | pk_tcvat_fzjg_taxpay_state |  | fid |
| 3 | idx_tcvat_fzjg_taxpay_state2 |  | fewblxh,fsbbid |
