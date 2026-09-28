# 分支机构税额分摊表分录-tccit_seft_fzjg_entry

## 分支机构税额分摊表分录-主表 t_tccit_seft_fzjg_entry

- **表名称：** 分支机构税额分摊表分录-主表
- **表名：** t_tccit_seft_fzjg_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :动态行 count :合计 |
| 4 | ftyshxydm | 统一社会信用代码 | varchar | 50 |  | √ | ' ' | 统一社会信用代码 |
| 5 | fzgxc | 职工薪酬 | numeric | 23 | 10 | √ | 0.0000000000 | 职工薪酬 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fzcze | 资产总额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产总额 |
| 8 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 9 | fyysr | 营业收入 | numeric | 23 | 10 | √ | 0.0000000000 | 营业收入 |
| 10 | ffpbl | 分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 分配比例 |
| 11 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 12 | ffpsdse | 分配所得额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配所得额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffzjgmc | 分支机构名称 | varchar | 50 |  | √ | ' ' | 分支机构名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_seft_fzjg_entry |  | fentryid |
| 2 | idx_tccit_seft_fzjg_entry_fk |  | fid |
