# 结账日志表-cal_settleaccountlog

## 结账日志表-主表 t_cal_settlelog

- **表名称：** 结账日志表-主表
- **表名：** t_cal_settlelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 3 | fsettletype | 类型 | varchar | 10 |  | √ | ' ' | 类型,枚举: A :结账 B :反结账 C :关账 D :结账检查 |
| 4 | foperationtime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fexpectperiodid | 期望期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 7 | fsuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 8 | fperiodmsg | 期间流转 | varchar | 80 |  | √ | ' ' | 期间流转 |
| 9 | fcheckresult | 检查结果 | varchar | 255 |  | √ | ' ' | 检查结果 |
| 10 | fqueryschemeid | 查询方案 | int8 | 64 |  | √ | 0 | 查询方案 cal_query_scheme |
| 11 | foperationuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | ftaskid | 后台任务id | int8 | 64 |  | √ | 0 | 后台任务id |
| 14 | fcurrentperiodid | 当前期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_settlelog_pkey |  | fid |
| 2 | idx_cal_setlog_crid |  | fcostaccountid |
