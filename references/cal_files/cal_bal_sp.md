# 核算余额快照表（分片用）-cal_bal_sp

## 核算余额快照表（分片用）-主表 t_cal_bal_sp

- **表名称：** 核算余额快照表（分片用）-主表
- **表名：** t_cal_bal_sp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostdiff_sp | fcostdiff_sp | numeric | 23 | 10 | √ | 0 |  |
| 3 | factualcost_bal_sp | factualcost_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 4 | fcaldimensionid | fcaldimensionid | int8 | 64 |  | √ | 0 |  |
| 5 | factualcost_sp | factualcost_sp | numeric | 23 | 10 | √ | 0 |  |
| 6 | fcostdiff_in_sp | fcostdiff_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 7 | fcalrangeid | fcalrangeid | int8 | 64 |  | √ | 0 |  |
| 8 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbaseqty_out_sp | fbaseqty_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 10 | fstandardcost_bal_sp | fstandardcost_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 11 | fcostdiff_bal_sp | fcostdiff_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 12 | fisnew | fisnew | bpchar | 1 |  | √ | ' ' |  |
| 13 | fupdateruleid | fupdateruleid | varchar | 36 |  | √ | ' ' |  |
| 14 | fmovetime | fmovetime | timestamp | 0 |  |  | null |  |
| 15 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 16 | fupdatetype | fupdatetype | int4 | 32 |  | √ | 0 |  |
| 17 | fbaseqty_in_sp | fbaseqty_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fstandardcost_in_sp | fstandardcost_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 20 | factualcost_in_sp | factualcost_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 21 | fbaseqty_sp | fbaseqty_sp | numeric | 23 | 10 | √ | 0 |  |
| 22 | fentryseq | fentryseq | int4 | 32 |  | √ | 0 |  |
| 23 | fstandardcost_out_sp | fstandardcost_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 24 | fbillname | fbillname | varchar | 50 |  | √ | ' ' |  |
| 25 | fstandardcost_sp | fstandardcost_sp | numeric | 23 | 10 | √ | 0 |  |
| 26 | fupdatetime | 更新标识 | int8 | 64 |  | √ | 0 | 更新标识 |
| 27 | faccounttype | faccounttype | bpchar | 1 |  | √ | ' ' |  |
| 28 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 29 | fperiod | fperiod | int4 | 32 |  | √ | 0 |  |
| 30 | fcostdiff_out_sp | fcostdiff_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 31 | factualcost_out_sp | factualcost_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fkeycol | fkeycol | varchar | 50 |  | √ | ' ' |  |
| 34 | fbaseqty_bal_sp | fbaseqty_bal_sp | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_balsp_fbid |  | fbillid |
| 2 | idx_cal_balsp_fbeid |  | fentryid |
| 3 | idx_cal_balsp_fbno |  | fbillno |
| 4 | idx_cal_balsp_fut |  | fupdatetime |
| 5 | idx_cal_balsp_fk |  | fkeycol |
| 6 | pk_cal_bal_sp |  | fid |
