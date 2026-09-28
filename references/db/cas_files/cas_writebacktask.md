# 反写任务-cas_writebacktask

## 反写任务-主表 t_cas_writebacktask

- **表名称：** 反写任务-主表
- **表名：** t_cas_writebacktask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 参数 | varchar | 255 |  |  | null | 参数 |
| 3 | flastexecutetime | 最后执行时间 | timestamp | 0 |  |  | null | 最后执行时间 |
| 4 | fsourceentitykey | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识 |
| 5 | fexception_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 6 | fbillpk | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 7 | fentitykey | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 8 | fresult | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果,枚举: 1 :成功 0 :失败 -1 :未执行 |
| 9 | ftaskexecuteclass | 执行类 | varchar | 100 |  | √ | ' ' | 执行类 |
| 10 | fexception | 异常信息 | varchar | 500 |  |  | null | 异常信息 |
| 11 | foperation | 反写操作 | varchar | 50 |  | √ | ' ' | 反写操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_wb_result |  | fresult |
| 2 | t_cas_writebacktask_pkey |  | fid |
