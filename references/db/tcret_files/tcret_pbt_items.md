# 财行税待申报项目单据-tcret_pbt_items

## 财行税待申报项目单据-主表 t_tcret_declare_entry

- **表名称：** 财行税待申报项目单据-主表
- **表名：** t_tcret_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsm | fsm | varchar | 50 |  | √ | ' ' |  |
| 3 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :按月申报 season :按季申报 halfyear :半年申报 year :按年申报 |
| 4 | ftaxstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 7 | fbqybtse | fbqybtse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fjmse | fjmse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 10 | fynse | fynse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fyjse | fyjse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: yhsaq :印花税（按期） yhsac :印花税（按次） fcscj :房产税（从价） fcscz :房产税（从租） cztdsys :城镇土地使用税 hbsaq :环保税（按期） ccscl :车船税（车辆） ccscb :车船税（船舶） qs :契税 tdzzs :土地增值税（尾盘） tdzzsyj :土地增值税（预征） tdzzsqs :土地增值税（清算） |
| 14 | ftaxtypebrief | ftaxtypebrief | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_declare_entry_fk |  | fid |
| 2 | pk_tcret_declare_entry |  | fentryid |
