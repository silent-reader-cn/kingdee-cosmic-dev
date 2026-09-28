# 并行计算参数-sco_parparam

## 并行计算参数-主表 t_sco_parparam

- **表名称：** 并行计算参数-主表
- **表名：** t_sco_parparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 后台参数 | varchar | 255 |  | √ | ' ' | 后台参数 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fparam_tag | 后台参数_详情 | text | 0 |  |  | null | 后台参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_parparam |  | fid |
| 2 | idx_sco_parparam |  | fparam |
