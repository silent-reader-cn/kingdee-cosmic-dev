# 固定资产后台变量-fa_variables

## 固定资产后台变量-主表 t_fa_variables

- **表名称：** 固定资产后台变量-主表
- **表名：** t_fa_variables

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | value | varchar | 255 |  |  | ' ' | value |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fkey | key | varchar | 50 |  | √ | ' ' | key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_variables_fkey |  | fkey |
| 2 | t_fa_variables_pkey |  | fid |
