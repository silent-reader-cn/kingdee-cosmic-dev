# 单据关联关系-bos_ctbotp_billlk

## 单据关联关系-主表 t_ctbotp_billlk

- **表名称：** 单据关联关系-主表
- **表名：** t_ctbotp_billlk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funiquekey | 唯一标识 | varchar | 100 |  | √ | ' ' | 唯一标识 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fdeletetime | 删除时间 | timestamp | 0 |  |  | null | 删除时间 |
| 5 | fttableid | 目标单类型 | int8 | 64 |  | √ | 0 | 目标单类型 |
| 6 | fstableid | 源单类型 | int8 | 64 |  | √ | 0 | 源单类型 |
| 7 | fstenantcode | 源单租户编号 | varchar | 50 |  | √ | ' ' | 源单租户编号 |
| 8 | ftentitykey | 目标单标识 | varchar | 36 |  | √ | ' ' | 目标单标识 |
| 9 | fsaccountid | 源单数据中心 | varchar | 50 |  | √ | ' ' | 源单数据中心 |
| 10 | ftbillid | 目标单内码 | int8 | 64 |  | √ | 0 | 目标单内码 |
| 11 | fttenantcode | 目标单租户编号 | varchar | 50 |  | √ | ' ' | 目标单租户编号 |
| 12 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :目标单生成中 1 :目标单已保存 |
| 13 | fdelstatus | 删除状态 | bpchar | 1 |  | √ | '0' | 删除状态,枚举: 0 :正常使用 1 :待删除 2 :已删除 |
| 14 | fsentitykey | 源单标识 | varchar | 36 |  | √ | ' ' | 源单标识 |
| 15 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 16 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 17 | ftaccountid | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_billlk_delstatus |  | fdelstatus |
| 2 | idx_ctbotp_billlk_status |  | fstatus |
| 3 | pk_t_ctbotp_billlk |  | fid |
| 4 | idx_ctbotp_billlk_deletetime |  | fdeletetime |
| 5 | idx_ctbotp_billlk_createtime |  | fcreatetime |
| 6 | idx_ctbotp_billlk_uniquekey |  | funiquekey |
| 7 | idx_ctbotp_billlk_tbillid |  | ftbillid |
| 8 | idx_ctbotp_billlk_sbillid |  | fsbillid |
