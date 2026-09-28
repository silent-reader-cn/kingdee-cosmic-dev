# 流程会话数据-gai_flow_session_store

## 流程会话数据-主表 t_gai_flow_session_store

- **表名称：** 流程会话数据-主表
- **表名：** t_gai_flow_session_store

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 3 | fvalue_tag | 值_详情 | text | 0 |  |  | null | 值_详情 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fkey | 键 | varchar | 500 |  | √ | ' ' | 键 |
| 6 | fchatsessionid | 会话Id | varchar | 150 |  | √ | ' ' | 会话Id |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_flow_session_store |  | fid |
| 2 | idx_session |  | fchatsessionid |
