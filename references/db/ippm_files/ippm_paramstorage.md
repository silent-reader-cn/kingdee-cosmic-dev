# 参数数据存储-ippm_paramstorage

## 参数数据存储-主表 t_ippm_paramstorage

- **表名称：** 参数数据存储-主表
- **表名：** t_ippm_paramstorage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamdata | 参数数据 | varchar | 255 |  | √ | ' ' | 参数数据 |
| 3 | frecorddate | 参数记录日期 | timestamp | 0 |  |  | null | 参数记录日期 |
| 4 | fparamtype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: sys-sys :系统参数-系统 sys-app :系统参数-应用 bill :单据参数 |
| 5 | fparamdata_tag | 参数数据_详情 | text | 0 |  |  | null | 参数数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_paramstorage |  | fid |
| 2 | idx_ippm_paramstorage_type |  | fparamtype |
| 3 | idx_ippm_paramstorage_date |  | frecorddate |
