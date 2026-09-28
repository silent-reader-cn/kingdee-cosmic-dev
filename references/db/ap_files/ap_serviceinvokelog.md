# 服务调用日志-ap_serviceinvokelog

## 服务调用日志-主表 t_ap_serviceinvokelog

- **表名称：** 服务调用日志-主表
- **表名：** t_ap_serviceinvokelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmethodname | methodName | varchar | 50 |  | √ | ' ' | methodName |
| 3 | fparam | param | varchar | 255 |  | √ | ' ' | param |
| 4 | fissuccess | 成功 | bpchar | 1 |  | √ | ' ' | 成功 |
| 5 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 6 | fexceptioninfo | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 7 | fdescription | 服务类型 | varchar | 50 |  | √ | ' ' | 服务类型,枚举: apverify-cal :应付核销-调用存货 arverify-cal :应收核销-调用存货 costrecord-cal :反写核算成本记录-调用存货 |
| 8 | fexectime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 9 | fappid | appId | varchar | 50 |  | √ | ' ' | appId |
| 10 | ftype | 调用类型 | varchar | 30 |  | √ | ' ' | 调用类型,枚举: mservice :微服务调用 |
| 11 | fcloudid | cloudId | varchar | 50 |  | √ | ' ' | cloudId |
| 12 | fsuccesstime | 成功时间 | timestamp | 0 |  |  | null | 成功时间 |
| 13 | fservicename | serviceName | varchar | 50 |  | √ | ' ' | serviceName |
| 14 | fcount | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 15 | fparam_tag | param_详情 | text | 0 |  |  | null | param_详情 |
| 16 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_serviceinvokelog |  | fid |
| 2 | idx_ap_serlog_date |  | fexectime |
