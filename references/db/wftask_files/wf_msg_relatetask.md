# 第三方关联任务ID-wf_msg_relatetask

## 第三方关联任务ID-主表 t_wf_relatetaskid

- **表名称：** 第三方关联任务ID-主表
- **表名：** t_wf_relatetaskid

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkey | 键Key | varchar | 100 |  | √ | ' ' | 键Key |
| 3 | ftaskid | 苍穹任务id | int8 | 64 |  | √ | 0 | 苍穹任务id |
| 4 | fsetting | 值value | varchar | 500 |  | √ | ' ' | 值value |
| 5 | fchannel | 第三方渠道 | varchar | 100 |  | √ | ' ' | 第三方渠道 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_relatetaskid_pkey |  | fid |
| 2 | idx_wf_relatetaskid |  | ftaskid |
