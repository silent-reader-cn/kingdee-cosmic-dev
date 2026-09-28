# 会计事件索引-ai_event_index

## 会计事件索引-主表 t_ai_event_index

- **表名称：** 会计事件索引-主表
- **表名：** t_ai_event_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffieldvalue | 字段值 | varchar | 80 |  | √ | ' ' | 字段值 |
| 3 | feventid | 会计事件id | int8 | 64 |  | √ | 0 | 会计事件id |
| 4 | ffieldname | 字段名 | varchar | 80 |  | √ | ' ' | 字段名 |
| 5 | feventclassid | 会计事件类型id | int8 | 64 |  | √ | 0 | 会计事件类型id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_event_index |  | feventclassid,ffieldname,ffieldvalue,feventid |
| 2 | pk_t_ai_event_index |  | fid |
