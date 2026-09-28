# 入门必学事项-ipop_abc_reading_itemcfg

## 入门必学事项-主表 t_ipop_abc_item

- **表名称：** 入门必学事项-主表
- **表名：** t_ipop_abc_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemname | 子任务名称 | varchar | 200 |  | √ | ' ' | 子任务名称 |
| 3 | fitemicon | fitemicon | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_abc_item_name |  | fitemname |
| 2 | pk_t_ipop_abc_item |  | fid |
