# 归档请求-eafc_archive_request

## 归档请求-主表 tk_eafc_archive_request

- **表名称：** 归档请求-主表
- **表名：** tk_eafc_archive_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_request_param | 请求参数 | varchar | 500 |  | √ | ' ' | 请求参数 |
| 3 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fk_eafc_request_type | 请求类型 | varchar | 50 |  | √ | ' ' | 请求类型,枚举: 1 :归档 2 :反归档 |
| 5 | fk_eafc_modifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fk_eafc_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :执行完成 |
| 7 | fk_eafc_createuser | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_archive_request |  | fid |
