# 业务员首页赞-task_fabulous

## 业务员首页赞-主表 t_tk_fabulous

- **表名称：** 业务员首页赞-主表
- **表名：** t_tk_fabulous

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskproperty | 任务属性 | varchar | 10 |  | √ | '0' | 任务属性,枚举: 0 :审单任务 5 :质检任务 |
| 3 | fthumbupuser | 点赞用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdate | 点赞日期 | timestamp | 0 |  |  | null | 点赞日期 |
| 5 | fbythumbupuser | 被点赞用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_fabulous |  | fthumbupuser |
| 2 | t_tk_fabulous_pkey |  | fid |
