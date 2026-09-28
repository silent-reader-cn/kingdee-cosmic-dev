# 从库检测事件-rw_split_check_event

## 从库检测事件-主表 t_rw_split_check_event

- **表名称：** 从库检测事件-主表
- **表名：** t_rw_split_check_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevent | 事件 | varchar | 50 |  | √ | ' ' | 事件 |
| 3 | fcomment | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 4 | fresult_code | 结果码 | varchar | 50 |  | √ | ' ' | 结果码 |
| 5 | fresult | 结果 | varchar | 50 |  | √ | ' ' | 结果 |
| 6 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rw_split_check_event |  | fid |
| 2 | idx_rw_split_check_fevent |  | fevent |
