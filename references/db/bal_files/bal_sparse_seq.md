# 稀疏序列-bal_sparse_seq

## 稀疏序列-主表 t_bal_sparse_seq

- **表名称：** 稀疏序列-主表
- **表名：** t_bal_sparse_seq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fentity | 实体对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fstoretb | 存储表 | varchar | 30 |  | √ | ' ' | 存储表 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdbkey | 库标识 | varchar | 20 |  | √ | ' ' | 库标识 |
| 6 | fsparsecol | 稀疏字段 | varchar | 20 |  | √ | ' ' | 稀疏字段 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 8 | factualtb | 实际物理表 | varchar | 30 |  | √ | ' ' | 实际物理表 |
| 9 | fentitytb | 物理表 | varchar | 30 |  | √ | ' ' | 物理表 |
| 10 | fsparsesize | 稀疏大小 | int4 | 32 |  | √ | 10000 | 稀疏大小 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_seq_atb |  | factualtb |
| 2 | pk_bal_sparse_seq |  | fid |
| 3 | idx_bal_seq_mt |  | fmodifydate |
