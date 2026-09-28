# 单据同步路线-bos_ctbotp_billroute

## 单据同步路线-主表 t_ctbotp_billroute

- **表名称：** 单据同步路线-主表
- **表名：** t_ctbotp_billroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftbillid | 目标单内码 | int8 | 64 |  | √ | 0 | 目标单内码 |
| 3 | fttenantcode | 目标单租户编号 | varchar | 50 |  | √ | ' ' | 目标单租户编号 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fsentitykey | 源单标识 | varchar | 36 |  | √ | ' ' | 源单标识 |
| 6 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 7 | ftaccountid | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |
| 8 | fstenantcode | 源单租户编号 | varchar | 50 |  | √ | ' ' | 源单租户编号 |
| 9 | ftentitykey | 目标单标识 | varchar | 36 |  | √ | ' ' | 目标单标识 |
| 10 | fsaccountid | 源单数据中心 | varchar | 50 |  | √ | ' ' | 源单数据中心 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbr_tbillid |  | ftbillid |
| 2 | pk_ctbotp_billroute |  | fid |
| 3 | idx_cbr_sbillid |  | fsbillid |
