# 交易明细同步记录-aqap_detail_sync_record

## 交易明细同步记录-主表 t_aqap_detail_sync_record

- **表名称：** 交易明细同步记录-主表
- **表名：** t_aqap_detail_sync_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcompensation_detail | 补偿详情 | varchar | 256 |  |  | null | 补偿详情 |
| 6 | facc_no | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 7 | fcurrency | 币别 | varchar | 50 |  | √ | 'CNY' | 币别 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fcompensation_count | 补偿次数 | int8 | 64 |  |  | null | 补偿次数 |
| 10 | fdetail_count | 交易明细数量 | int8 | 64 |  |  | null | 交易明细数量 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbank_name | 银行名称 | varchar | 50 |  | √ | ' ' | 银行名称 |
| 13 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 14 | fsync_count | 联机查询次数 | int8 | 64 |  | √ | 1 | 联机查询次数 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fis_completed | 是否完整 | int8 | 64 |  |  | null | 是否完整 |
| 17 | fenable | 使用状态 | int8 | 64 |  | √ | 1 | 使用状态 |
| 18 | fsync_date | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_detail_sync_record_pkey |  | fid |
| 2 | idx_aqap_detail_sr1 |  | facc_no,fsync_date,fcurrency |
