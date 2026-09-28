# 封面关系-rim_cover_relation

## 封面关系-主表 t_rim_cover_relation

- **表名称：** 封面关系-主表
- **表名：** t_rim_cover_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcover_id | 封面id | varchar | 50 |  | √ | ' ' | 封面id |
| 3 | fexpense_id | 报销单id | varchar | 50 |  | √ | ' ' | 报销单id |
| 4 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fresource | 报销单来源 | varchar | 50 |  | √ | ' ' | 报销单来源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_cover_relation |  | fid |
| 2 | idx_rim_cover_relation |  | fexpense_id,fresource |
