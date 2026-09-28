# 智能会计平台后台参数-ai_backgroundparam

## 智能会计平台后台参数-主表 t_ai_backgroundparam

- **表名称：** 智能会计平台后台参数-主表
- **表名：** t_ai_backgroundparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fvalue | 值 | varchar | 100 |  | √ | ' ' | 值 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fkey | key标识 | varchar | 100 |  | √ | ' ' | key标识 |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_backparam |  | forgid,fkey |
| 2 | pk_ai_backgroundparam |  | fid |
