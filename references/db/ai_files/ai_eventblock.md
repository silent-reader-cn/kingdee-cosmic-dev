# 会计事件阻塞-ai_eventblock

## 会计事件阻塞-主表 t_ai_eventblock

- **表名称：** 会计事件阻塞-主表
- **表名：** t_ai_eventblock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffieldvalue | 字段值 | varchar | 100 |  | √ | ' ' | 字段值 |
| 3 | feventid | 会计事件id | int8 | 64 |  | √ | 0 | 会计事件id |
| 4 | feventclass | 会计事件类型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |
| 5 | ffieldname | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 6 | ftextfield | 扩展列 | varchar | 100 |  | √ | ' ' | 扩展列 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_eventblock |  | feventclass,feventid |
| 2 | pk_t_ai_eventblock |  | fid |
