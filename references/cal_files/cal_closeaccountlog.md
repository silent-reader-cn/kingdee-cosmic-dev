# 关账日志表-cal_closeaccountlog

## 关账日志表-主表 t_cal_closelog

- **表名称：** 关账日志表-主表
- **表名：** t_cal_closelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclosetype | 类型 | varchar | 10 |  | √ | ' ' | 类型,枚举: A :关账 B :反关账 |
| 3 | flastdate | 上次关账日期 | timestamp | 0 |  |  | null | 上次关账日期 |
| 4 | foperationtime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fexpectdate | 期望日期 | timestamp | 0 |  |  | null | 期望日期 |
| 7 | fsuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 8 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdatemsg | 日期流转 | varchar | 80 |  | √ | ' ' | 日期流转 |
| 10 | fcheckresult | 检查结果 | varchar | 255 |  | √ | ' ' | 检查结果 |
| 11 | fqueryschemeid | 查询方案 | int8 | 64 |  | √ | 0 | 查询方案 cal_query_scheme |
| 12 | foperationuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ftaskid | 后台任务id | int8 | 64 |  | √ | 0 | 后台任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_closelog |  | fid |
| 2 | idx_cal_calorg |  | forgid |
| 3 | idx_cal_op_time |  | foperationtime |
