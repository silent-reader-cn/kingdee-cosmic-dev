# 无代码分享-bos_nocode_share

## 无代码分享-主表 t_nocode_share

- **表名称：** 无代码分享-主表
- **表名：** t_nocode_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 3 | ficon | 应用图标 | varchar | 255 |  | √ | ' ' | 应用图标 |
| 4 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | furl | 分享链接 | varchar | 255 |  | √ | ' ' | 分享链接 |
| 6 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fshareid | 分享id | varchar | 50 |  | √ | ' ' | 分享id |
| 8 | fimage | 背景图 | varchar | 255 |  | √ | ' ' | 背景图 |
| 9 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_nocode_share |  | fid |
| 2 | idx_nc_ns_fappid |  | fappid |
