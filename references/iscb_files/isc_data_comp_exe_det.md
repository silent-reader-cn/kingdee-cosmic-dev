# 对比详细结果-isc_data_comp_exe_det

## 对比详细结果-主表 t_isc_data_comp_exe_det

- **表名称：** 对比详细结果-主表
- **表名：** t_isc_data_comp_exe_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | freal_data | 目标单实际数据 | varchar | 255 |  | √ | ' ' | 目标单实际数据 |
| 4 | fmessage | 执行结果 | varchar | 255 |  | √ | ' ' | 执行结果 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fdata_comp_exe | 执行实例 | varchar | 50 |  | √ | ' ' | 执行实例 |
| 7 | fauditdatetime | fauditdatetime | timestamp | 0 |  |  | null |  |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fcompensate_log | 补偿日志 | varchar | 255 |  |  | ' ' | 补偿日志 |
| 10 | fcompensate_state | 补偿状态 | varchar | 10 |  | √ | ' ' | 补偿状态,枚举: N :未补偿 S :补偿成功 F :补偿失败 |
| 11 | fresult | 补偿日志(废弃) | varchar | 50 |  | √ | ' ' | 补偿日志(废弃) |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fsource_data_tag | 源单数据_详情 | text | 0 |  |  | null | 源单数据_详情 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fsrc_pk | 源单主键 | varchar | 50 |  | √ | ' ' | 源单主键 |
| 16 | ftarget_data | 目标单预期数据 | varchar | 255 |  | √ | ' ' | 目标单预期数据 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcompensate_log_tag | 补偿日志_详情 | text | 0 |  |  | null | 补偿日志_详情 |
| 19 | ftarget_data_tag | 目标单预期数据_详情 | text | 0 |  |  | null | 目标单预期数据_详情 |
| 20 | fsource_data | 源单数据 | varchar | 255 |  | √ | ' ' | 源单数据 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | freal_data_tag | 目标单实际数据_详情 | text | 0 |  |  | null | 目标单实际数据_详情 |
| 24 | fmessage_tag | 执行结果_详情 | text | 0 |  |  | null | 执行结果_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp_exe_det |  | fid |
| 2 | idx_isc_data_comp_exe_det2 |  | fdata_comp_exe |
| 3 | idx_isc_data_copy_exe_det_c |  | fcreatetime |
