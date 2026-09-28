# 共享异常收集平台-task_exceptionplatform

## 共享异常收集平台-主表 t_tk_exceptionplatform

- **表名称：** 共享异常收集平台-主表
- **表名：** t_tk_exceptionplatform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 3 | fmethodname | 方法名 | varchar | 50 |  | √ | ' ' | 方法名 |
| 4 | fkeyinfo | 业务关键信息 | varchar | 2000 |  | √ | ' ' | 业务关键信息 |
| 5 | ftraceid | traceId | varchar | 50 |  | √ | ' ' | traceId |
| 6 | ftype | 异常类型 | varchar | 50 |  | √ | ' ' | 异常类型,枚举: 0 :方法类 |
| 7 | fclassname | 全类名 | varchar | 200 |  | √ | ' ' | 全类名 |
| 8 | fexceptioninfo | 异常信息 | varchar | 500 |  | √ | ' ' | 异常信息 |
| 9 | fuserid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fstacktrace | 异常堆栈 | varchar | 200 |  | √ | ' ' | 异常堆栈 |
| 11 | fstacktrace_tag | 异常堆栈_详情 | text | 0 |  |  | null | 异常堆栈_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ssc_excepplatform_idx |  | ftraceid |
| 2 | pk_t_tk_exceptionplatform |  | fid |
