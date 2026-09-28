# 同步路线-bos_ctbotp_syncroute

## 同步路线-主表 t_ctbotp_syncroute

- **表名称：** 同步路线-主表
- **表名：** t_ctbotp_syncroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fttenantcode | 目标单租户 | varchar | 50 |  | √ | ' ' | 目标单租户 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fsentitykey | 源单标识 | varchar | 36 |  | √ | ' ' | 源单标识 |
| 5 | ftaccountid | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |
| 6 | fstenantcode | 源单租户 | varchar | 50 |  | √ | ' ' | 源单租户 |
| 7 | ftentitykey | 目标单标识 | varchar | 36 |  | √ | ' ' | 目标单标识 |
| 8 | fsaccountid | 源单数据中心 | varchar | 50 |  | √ | ' ' | 源单数据中心 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_syncroute_tentitykey |  | ftentitykey |
| 2 | pk_t_ctbotp_syncroute |  | fid |
| 3 | idx_ctbotp_syncroute_sentitykey |  | fsentitykey |
