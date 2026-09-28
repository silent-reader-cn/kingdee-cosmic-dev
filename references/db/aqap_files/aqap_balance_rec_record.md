# 余额对账查询记录表-aqap_balance_rec_record

## 余额对账查询记录表-主表 t_aqap_balance_rec_record

- **表名称：** 余额对账查询记录表-主表
- **表名：** t_aqap_balance_rec_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | facc_no | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 6 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 10 | fsync_count | 联机查询次数 | int4 | 32 |  | √ | 0 | 联机查询次数 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fenable | 使用状态 | int4 | 32 |  | √ | 0 | 使用状态 |
| 13 | fsync_date | 交易月份 | timestamp | 0 |  |  | null | 交易月份 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | unidx_balance_rec_record |  | facc_no,fcurrency,fsync_date |
| 2 | pk_t_aqap_balance_rec_record |  | fid |
