# 坏账插件注册-ar_accrreserveconfig

## 坏账插件注册-主表 t_ar_accrreserveconfig

- **表名称：** 坏账插件注册-主表
- **表名：** t_ar_accrreserveconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fservice | 坏账计提类 | varchar | 200 |  | √ | ' ' | 坏账计提类 |
| 3 | fentityid | 单据标识 | varchar | 36 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_accrreserveconfig |  | fid |
| 2 | idx_ar_arc_fentityid |  | fentityid |
