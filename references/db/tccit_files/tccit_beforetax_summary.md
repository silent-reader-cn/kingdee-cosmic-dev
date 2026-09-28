# 不可抵扣单据列表-tccit_beforetax_summary

## 不可抵扣单据列表-主表 t_tccit_beforetax_summary

- **表名称：** 不可抵扣单据列表-主表
- **表名：** t_tccit_beforetax_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 001 :罚金、罚款和被没收财物的损失 002 :税收滞纳金、加收利息 003 :赞助支出 004 :与取得收入无关的支出 005 :不合规票据支出 006 :母子公司间的管理费 007 :其他 008 :合计 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 8 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 9 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_beforetax_summary |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_beforetax_summary |  | fid |
