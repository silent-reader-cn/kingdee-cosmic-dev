# 企业所得税A06779列表-tccit_qysds_a06779_bill

## 企业所得税A06779列表-主表 t_tccit_qysds_a06779_bill

- **表名称：** 企业所得税A06779列表-主表
- **表名：** t_tccit_qysds_a06779_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdysd | 递延所得合计 | numeric | 23 | 10 | √ | 0 | 递延所得合计 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计 |
| 4 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 5 | fdeclareyear | 申报年份 | varchar | 50 |  | √ | ' ' | 申报年份 |
| 6 | ffairvalue | 公允价值合计 | numeric | 23 | 10 | √ | 0 | 公允价值合计 |
| 7 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 8 | ftaxbase | 计税基础合计 | numeric | 23 | 10 | √ | 0 | 计税基础合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_qysds_a06779_bill |  | fid |
| 2 | idx_tccit_a06779_bill_fsbbid |  | fsbbid |
