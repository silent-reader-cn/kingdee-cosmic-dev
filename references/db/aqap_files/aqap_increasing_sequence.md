# 自增序列号-aqap_increasing_sequence

## 自增序列号-主表 t_aqap_increasing_sequenc

- **表名称：** 自增序列号-主表
- **表名：** t_aqap_increasing_sequenc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsequence_no | 当前序号 | int8 | 64 |  | √ | 0 | 当前序号 |
| 3 | fcreate_time | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fsequence_date | 序列号日期（天） | varchar | 10 |  | √ | ' ' | 序列号日期（天） |
| 5 | fsequence_key | 序列号关键字 | varchar | 200 |  | √ | ' ' | 序列号关键字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_increasing_sequenc |  | fid |
| 2 | idx_increasing_sequenc_quer |  | fsequence_key,fsequence_date |
