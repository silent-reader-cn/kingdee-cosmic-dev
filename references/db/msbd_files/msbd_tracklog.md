# 跟踪日志-msbd_tracklog

## 跟踪日志-主表 t_msbd_tracklog

- **表名称：** 跟踪日志-主表
- **表名：** t_msbd_tracklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmethodname | 方法名 | varchar | 512 |  |  | null | 方法名 |
| 3 | ftracklog | ftracklog | varchar | 512 |  |  | null |  |
| 4 | ftraceid | traceId | varchar | 80 |  | √ | ' ' | traceId |
| 5 | fclassname | 类名 | varchar | 512 |  |  | null | 类名 |
| 6 | finvokedcodeposition | 调用服务代码位置 | varchar | 512 |  |  | null | 调用服务代码位置 |
| 7 | fmethodparam | 方法参数 | varchar | 512 |  |  | null | 方法参数 |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmethodparam_tag | 方法参数_详情 | text | 0 |  |  | null | 方法参数_详情 |
| 10 | fdatetime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 11 | ftracklogdetail_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 12 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 应用 |
| 13 | fcodeposition | 服务代码位置 | varchar | 512 |  |  | null | 服务代码位置 |
| 14 | flevel | 日志级别 | varchar | 5 |  | √ | ' ' | 日志级别,枚举: info :信息日志 warn :警告日志 error :错误日志 |
| 15 | ftype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: start :开始 mid :执行中 end :结束 |
| 16 | ftracklogdetail | 日志 | varchar | 512 |  |  | null | 日志 |
| 17 | fformid | fformid | varchar | 255 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msbd_tracklog_type |  | fdatetime,fuserid |
| 2 | pk_t_msbd_tracklog |  | fid |
