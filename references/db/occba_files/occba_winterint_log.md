# 冬储结息明细-occba_winterint_log

## 冬储结息明细-主表 t_occba_wiint_log

- **表名称：** 冬储结息明细-主表
- **表名：** t_occba_wiint_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcloseusedrealintamt | 本次更新利息 | numeric | 23 | 10 | √ | 0 | 本次更新利息 |
| 3 | factualusedamount | 实际使用金额 | numeric | 23 | 10 | √ | 0 | 实际使用金额 |
| 4 | fsettledintamt | 结算利息（废弃） | numeric | 23 | 10 | √ | 0 | 结算利息（废弃） |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcloseusedamount | 关闭退回金额（废弃） | numeric | 23 | 10 | √ | 0 | 关闭退回金额（废弃） |
| 7 | factualintamt | 实际结算利息 | numeric | 23 | 10 | √ | 0 | 实际结算利息 |
| 8 | fmyentryid | 资金收入单行ID | int8 | 64 |  | √ | 0 | 资金收入单行ID |
| 9 | fdiffrealintamt | 变更结息差额（废弃） | numeric | 23 | 10 | √ | 0 | 变更结息差额（废弃） |
| 10 | fcloserealintamt | 关闭退回结息金额（废弃） | numeric | 23 | 10 | √ | 0 | 关闭退回结息金额（废弃） |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | finterest | 利息（%） | numeric | 23 | 10 | √ | 0 | 利息（%） |
| 13 | fisupdate | 是否更新单据 | bpchar | 1 |  | √ | '0' | 是否更新单据 |
| 14 | fusedamount | 使用金额（废弃） | numeric | 23 | 10 | √ | 0 | 使用金额（废弃） |
| 15 | fdate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 16 | fdiffuseamount | 变更差额（废弃） | numeric | 23 | 10 | √ | 0 | 变更差额（废弃） |
| 17 | fbillno | 业务单据编号 | varchar | 80 |  | √ | ' ' | 业务单据编号 |
| 18 | fpaycustid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 19 | fmybillid | 资金收入单ID | int8 | 64 |  | √ | 0 | 资金收入单ID |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 21 | fintacctid | 结息账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 22 | foperate | 操作 | bpchar | 1 |  | √ | 'A' | 操作,枚举: A :保存 B :关闭 C :反关闭 D :变更 E :撤销 F :反审核 G :行关闭 H :行反关闭 I :提交 |
| 23 | fmybillno | 资金收入单编号 | varchar | 80 |  | √ | ' ' | 资金收入单编号 |
| 24 | fwinteracctid | 冬储账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 25 | fcalcintway | 计息方式 | bpchar | 1 |  | √ | 'A' | 计息方式,枚举: A :一次性计息 |
| 26 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 27 | fbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 28 | fbillentityid | 业务单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fcloserefundamount | 本次更新金额 | numeric | 23 | 10 | √ | 0 | 本次更新金额 |
| 30 | fdirection | 本次更新方向 | bpchar | 1 |  | √ | 'A' | 本次更新方向,枚举: A :正向 B :逆向 |
| 31 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | frecptchannelid | 收款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_wiint_log_bid |  | fbillid |
| 2 | pk_t_occba_wiint_log |  | fid |
