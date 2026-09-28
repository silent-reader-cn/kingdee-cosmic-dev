# 执行冲销详情日志-pa_offexecdetail

## 执行冲销详情日志-主表 t_pa_offexecdetail

- **表名称：** 执行冲销详情日志-主表
- **表名：** t_pa_offexecdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftarget_id | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 3 | fexecution_logid | 执行日志id | int8 | 64 |  | √ | 0 | 执行日志id |
| 4 | fsource_id | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_offexecdetail_1 |  | fexecution_logid |
| 2 | pk_t_pa_offexecdetail |  | fid |
