# 标准成本差异余额快照表（分片用）-cal_standcost_bal_sp

## 标准成本差异余额快照表（分片用）-主表 t_cal_standcost_bal_sp

- **表名称：** 标准成本差异余额快照表（分片用）-主表
- **表名：** t_cal_standcost_bal_sp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiff_c_sp | fdiff_c_sp | numeric | 23 | 10 | √ | 0 |  |
| 3 | fdiff_w_in_sp | fdiff_w_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 4 | fcostdiff_sp | fcostdiff_sp | numeric | 23 | 10 | √ | 0 |  |
| 5 | fdiff_g_bal_sp | fdiff_g_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 6 | fdiff_h_bal_sp | fdiff_h_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 7 | fdiff_c_bal_sp | fdiff_c_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 8 | fdiff_g_sp | fdiff_g_sp | numeric | 23 | 10 | √ | 0 |  |
| 9 | fdiff_r_sp | fdiff_r_sp | numeric | 23 | 10 | √ | 0 |  |
| 10 | fdiff_m_in_sp | fdiff_m_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 11 | fcostdiff_bal_sp | fcostdiff_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 12 | fdiff_k_sp | fdiff_k_sp | numeric | 23 | 10 | √ | 0 |  |
| 13 | fdiff_s_in_sp | fdiff_s_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 14 | fdiff_p_in_sp | fdiff_p_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 15 | fdiff_c_in_sp | fdiff_c_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 16 | fisnew | fisnew | bpchar | 1 |  | √ | ' ' |  |
| 17 | fupdateruleid | fupdateruleid | varchar | 36 |  | √ | ' ' |  |
| 18 | fmovetime | fmovetime | timestamp | 0 |  |  | null |  |
| 19 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 20 | fdiff_q_in_sp | fdiff_q_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 21 | fdiff_y_sp | fdiff_y_sp | numeric | 23 | 10 | √ | 0 |  |
| 22 | fdiff_t_bal_sp | fdiff_t_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 23 | fdiff_q_sp | fdiff_q_sp | numeric | 23 | 10 | √ | 0 |  |
| 24 | fbillname | fbillname | varchar | 50 |  | √ | ' ' |  |
| 25 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 26 | fperiod | fperiod | int4 | 32 |  | √ | 0 |  |
| 27 | fdiff_x_bal_sp | fdiff_x_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 28 | fcostdiff_out_sp | fcostdiff_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 29 | fdiff_p_bal_sp | fdiff_p_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 30 | fdiff_r_bal_sp | fdiff_r_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fdiff_g_in_sp | fdiff_g_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 33 | fkeycol | fkeycol | varchar | 50 |  | √ | ' ' |  |
| 34 | fdiff_t_in_sp | fdiff_t_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 35 | fdiff_k_in_sp | fdiff_k_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 36 | fdiff_p_out_sp | fdiff_p_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 37 | fdiff_q_out_sp | fdiff_q_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 38 | fdiff_m_out_sp | fdiff_m_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 39 | fdiff_t_sp | fdiff_t_sp | numeric | 23 | 10 | √ | 0 |  |
| 40 | fcostdiff_in_sp | fcostdiff_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 41 | fdiff_r_in_sp | fdiff_r_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 42 | fdiff_x_sp | fdiff_x_sp | numeric | 23 | 10 | √ | 0 |  |
| 43 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 44 | fdiff_h_in_sp | fdiff_h_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 45 | fdiff_g_out_sp | fdiff_g_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 46 | fdiff_m_sp | fdiff_m_sp | numeric | 23 | 10 | √ | 0 |  |
| 47 | fdiff_h_out_sp | fdiff_h_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 48 | fdiff_x_out_sp | fdiff_x_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 49 | fdiff_r_out_sp | fdiff_r_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 50 | fdiff_s_out_sp | fdiff_s_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 51 | fdiff_t_out_sp | fdiff_t_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 52 | fdiff_w_out_sp | fdiff_w_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 53 | fdiff_c_out_sp | fdiff_c_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 54 | fdiff_k_out_sp | fdiff_k_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 55 | fdiff_x_in_sp | fdiff_x_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 56 | fupdatetype | fupdatetype | int4 | 32 |  | √ | 0 |  |
| 57 | fdiff_s_bal_sp | fdiff_s_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 58 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 59 | fdiff_h_sp | fdiff_h_sp | numeric | 23 | 10 | √ | 0 |  |
| 60 | fdiff_y_out_sp | fdiff_y_out_sp | numeric | 23 | 10 | √ | 0 |  |
| 61 | fdiff_s_sp | fdiff_s_sp | numeric | 23 | 10 | √ | 0 |  |
| 62 | fentryseq | fentryseq | int4 | 32 |  | √ | 0 |  |
| 63 | fdiff_w_sp | fdiff_w_sp | numeric | 23 | 10 | √ | 0 |  |
| 64 | fdiff_m_bal_sp | fdiff_m_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 65 | fdiff_p_sp | fdiff_p_sp | numeric | 23 | 10 | √ | 0 |  |
| 66 | fdiff_k_bal_sp | fdiff_k_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 67 | fupdatetime | 更新标识 | int8 | 64 |  | √ | 0 | 更新标识 |
| 68 | fdiff_w_bal_sp | fdiff_w_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 69 | fdiff_y_bal_sp | fdiff_y_bal_sp | numeric | 23 | 10 | √ | 0 |  |
| 70 | fdiff_y_in_sp | fdiff_y_in_sp | numeric | 23 | 10 | √ | 0 |  |
| 71 | fdiff_q_bal_sp | fdiff_q_bal_sp | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_sdbalsp_fut |  | fupdatetime |
| 2 | idx_cal_sdbalsp_fbeid |  | fentryid |
| 3 | idx_cal_sdbalsp_fbid |  | fbillid |
| 4 | idx_cal_sdbalsp_fk |  | fkeycol |
| 5 | idx_cal_sdbalsp_fbno |  | fbillno |
| 6 | pk_cal_standcost_bal_sp |  | fid |
