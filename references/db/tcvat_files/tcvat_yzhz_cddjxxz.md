# 纳税企业通用传递单进项-tcvat_yzhz_cddjxxz

## 纳税企业通用传递单进项-主表 t_tcvat_yzhz_cddjxxz

- **表名称：** 纳税企业通用传递单进项-主表
- **表名：** t_tcvat_yzhz_cddjxxz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计 2 :2 |
| 3 | fbqsjdke | 本期实际抵扣额 | numeric | 20 | 2 | √ | 0 | 本期实际抵扣额 |
| 4 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 5 | fqt | 其它 | numeric | 20 | 2 | √ | 0 | 其它 |
| 6 | fxj | 小计 | numeric | 20 | 2 | √ | 0 | 小计 |
| 7 | fmshwy | 免税货物用 | numeric | 20 | 2 | √ | 0 | 免税货物用 |
| 8 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 9 | ffzcss | 非正常损失 | numeric | 20 | 2 | √ | 0 | 非正常损失 |
| 10 | fbqfsjx | 本期发生进项 | numeric | 20 | 2 | √ | 0 | 本期发生进项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdd_sbbid |  | fsbbid,fewblxh |
| 2 | pk_tcvat_yzhz_cddjxxz |  | fid |
