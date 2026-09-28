# 进项数据看板明细-rim_idb_detail

## 进项数据看板明细-主表 t_rim_idb_detail

- **表名称：** 进项数据看板明细-主表
- **表名：** t_rim_idb_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forg_id | 组织id | varchar | 50 |  | √ | ' ' | 组织id |
| 3 | fcategory_sum | 类型对应数量 | int8 | 64 |  | √ | 0 | 类型对应数量 |
| 4 | fdeal_time | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 5 | fparent_category | 父类型 | varchar | 50 |  | √ | ' ' | 父类型 |
| 6 | fcategory_amount | 类型对应金额 | numeric | 23 | 10 | √ | 0 | 类型对应金额 |
| 7 | fquery_type | 查询类型 | varchar | 50 |  | √ | ' ' | 查询类型 |
| 8 | fsub_category | 子类型 | varchar | 50 |  | √ | ' ' | 子类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_idb_detail |  | forg_id,fdeal_time |
| 2 | pk_t_rim_idb_detail |  | fid |
