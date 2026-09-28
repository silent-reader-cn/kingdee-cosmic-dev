# 问询率分布-inquiry_rate_distribution

## 问询率分布-主表 t_inquiry_rate_distributi

- **表名称：** 问询率分布-主表
- **表名：** t_inquiry_rate_distributi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fquestion_type | 问题类型 | varchar | 50 |  | √ | ' ' | 问题类型 |
| 3 | finquiry_rate | 问询率 | numeric | 10 | 4 |  | null | 问询率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_inquiry_rate_distributi |  | fid |
| 2 | idx_inquiry_rate_type |  | fquestion_type |
