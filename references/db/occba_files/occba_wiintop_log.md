# 冬储结息日志-occba_wiintop_log

## 冬储结息日志-主表 t_occba_wiintop_log

- **表名称：** 冬储结息日志-主表
- **表名：** t_occba_wiintop_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopamount | 更新金额 | numeric | 23 | 10 | √ | 0 | 更新金额 |
| 3 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fintacctid | 结息账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 5 | fmyentryid | 资金收入单行ID | int8 | 64 |  | √ | 0 | 资金收入单行ID |
| 6 | foperate | 操作 | bpchar | 1 |  | √ | 'A' | 操作,枚举: A :保存 B :关闭 C :反关闭 D :变更 E :撤销 F :反审核 G :行关闭 H :行反关闭 I :提交 T :退货审核 Z :退货反审核 |
| 7 | fmybillno | 资金收入单编号 | varchar | 80 |  | √ | ' ' | 资金收入单编号 |
| 8 | fopintamt | 更新结息金额 | numeric | 23 | 10 | √ | 0 | 更新结息金额 |
| 9 | fwinteracctid | 冬储账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | finterest | 利息（%） | numeric | 23 | 10 | √ | 0 | 利息（%） |
| 12 | fbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 13 | fbillentityid | 业务单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fdirection | 更新方向 | bpchar | 1 |  | √ | 'A' | 更新方向,枚举: A :正向 B :逆向 |
| 15 | fbillno | 业务单据编号 | varchar | 80 |  | √ | ' ' | 业务单据编号 |
| 16 | fmybillid | 资金收入单ID | int8 | 64 |  | √ | 0 | 资金收入单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_wiintop_log |  | fid |
| 2 | idx_occba_wiintop_bid |  | fbillid |
