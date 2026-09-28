# 计划管理视图缓存-mrp_schemecache

## 计划管理视图缓存-主表 t_mrp_schemecache

- **表名称：** 计划管理视图缓存-主表
- **表名：** t_mrp_schemecache

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :提交 C :审核 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fnumber | 视图编码 | varchar | 30 |  | √ | ' ' | 视图编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_schemecache |  | forgid |
| 2 | pk_t_mrp_schemecache |  | fid |
