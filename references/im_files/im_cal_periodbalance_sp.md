# 库存核算期间余额快照表（分片用）-im_cal_periodbalance_sp

## 库存核算期间余额快照表（分片用）-主表 t_im_cal_per_bal_sp

- **表名称：** 库存核算期间余额快照表（分片用）-主表
- **表名：** t_im_cal_per_bal_sp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty3rd_out_sp | fqty3rd_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 3 | fqty2nd_sp | fqty2nd_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fqty_sp | fqty_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fqty_out_sp | fqty_out_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fqty3rd_sp | fqty3rd_sp | numeric | 23 | 10 | √ | 0 |  |
| 7 | fqty2nd_in_sp | fqty2nd_in_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbaseqty_out_sp | fbaseqty_out_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fisnew | fisnew | bpchar | 1 |  | √ | ' ' |  |
| 11 | fupdateruleid | fupdateruleid | varchar | 36 |  | √ | ' ' |  |
| 12 | fmovetime | fmovetime | timestamp | 0 |  |  | null |  |
| 13 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 14 | fqty_in_sp | fqty_in_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fupdatetype | fupdatetype | int4 | 32 |  | √ | 0 |  |
| 16 | fbaseqty_in_sp | fbaseqty_in_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 18 | fbaseqty_sp | fbaseqty_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fqty3rd_in_sp | fqty3rd_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 20 | fentryseq | fentryseq | int4 | 32 |  | √ | 0 |  |
| 21 | fbillname | fbillname | varchar | 50 |  | √ | ' ' |  |
| 22 | fqty2nd_out_sp | fqty2nd_out_sp | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fupdatetime | 更新流水号 | int8 | 64 |  | √ | 0 | 更新流水号 |
| 24 | fperiod | fperiod | int4 | 32 |  | √ | 0 |  |
| 25 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fkeycol | fkeycol | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_cal_per_bal_sp |  | fid |
| 2 | idx_im_cal_spbal_utime |  | fupdatetime |
| 3 | idx_im_cal_spbal_bno |  | fbillno |
| 4 | idx_im_cal_spbal_enid |  | fentryid |
| 5 | idx_im_cal_spbal_bid |  | fbillid |
| 6 | idx_im_cal_spbal_key |  | fkeycol |
