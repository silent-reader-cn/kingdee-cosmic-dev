# 总机构信息-tccit_qysds_zjgxx

## 总机构信息-主表 t_tccit_qysds_zjgxx

- **表名称：** 总机构信息-主表
- **表名：** t_tccit_qysds_zjgxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzjgnsrsbh | 2.总机构纳税人识别号 | varchar | 100 |  | √ | ' ' | 2.总机构纳税人识别号 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :本年累计 |
| 4 | fynsdse | 3.应纳所得税额 | numeric | 23 | 10 | √ | 0.0000000000 | 3.应纳所得税额 |
| 5 | fzjgftsdse | 4.总机构分摊所得税额 | numeric | 23 | 10 | √ | 0.0000000000 | 4.总机构分摊所得税额 |
| 6 | fsfxsdfjm | 是否享受地方减免 | bpchar | 1 |  | √ | ' ' | 是否享受地方减免 |
| 7 | fzjgzjglyfsdse | 总机构直接管理建筑项目部预分所得税额 | numeric | 23 | 10 | √ | 0 | 总机构直接管理建筑项目部预分所得税额 |
| 8 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 9 | fzjgczjzfpsdse | 5.总机构财政集中分配所得税额 | numeric | 23 | 10 | √ | 0.0000000000 | 5.总机构财政集中分配所得税额 |
| 10 | fzjgmc | 1.总机构名称 | varchar | 600 |  | √ | ' ' | 1.总机构名称 |
| 11 | fljyftsdse | fljyftsdse | numeric | 23 | 10 | √ | 0 |  |
| 12 | fxsdfjmfd | 享受地方减免幅度 | numeric | 23 | 10 | √ | 0.0000000000 | 享受地方减免幅度 |
| 13 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 14 | ffzjgftdsdse | 6.分支机构分摊的所得税额 | numeric | 23 | 10 | √ | 0.0000000000 | 6.分支机构分摊的所得税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qysds_zjgxx |  | fsbbid |
| 2 | idx_tccit_qysds_zjgxx_1 |  | fewblxh,fsbbid |
| 3 | t_tccit_qysds_zjgxx_pkey |  | fid |
