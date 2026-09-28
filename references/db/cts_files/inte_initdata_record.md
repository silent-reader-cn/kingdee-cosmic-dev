# 初始库预置数据主键-inte_initdata_record

## 初始库预置数据主键-主表 t_int_initdata_record

- **表名称：** 初始库预置数据主键-主表
- **表名：** t_int_initdata_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappnumber | fappnumber | varchar | 32 |  | √ | ' ' |  |
| 3 | fenvconfig | 环境标识 | varchar | 64 |  | √ | ' ' | 环境标识 |
| 4 | ftablename | 表名 | varchar | 32 |  | √ | ' ' | 表名 |
| 5 | fmasterids | 主键内容 | varchar | 255 |  | √ | ' ' | 主键内容 |
| 6 | fproducttype | 产品标识 | varchar | 64 |  | √ | ' ' | 产品标识 |
| 7 | fmasterids_tag | 主键内容_详情 | text | 0 |  |  | null | 主键内容_详情 |
| 8 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_initdata_record |  | fid |
| 2 | idx_t_int_initdata_rec |  | ftablename |
