# 元数据管理-eafc_archive_metadata

## 元数据管理-主表 tk_eafc_archive_metadata

- **表名称：** 元数据管理-主表
- **表名：** tk_eafc_archive_metadata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_sign | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 3 | fk_eafc_createrfield | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_eafc_filed_len | 长度 | int4 | 32 |  | √ | 0 | 长度 |
| 5 | fk_eafc_data_type | 元数据类型 | varchar | 50 |  | √ | ' ' | 元数据类型,枚举: 1 :业务元数据 2 :档案元数据 |
| 6 | fk_eafc_createdatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fk_eafc_status | 是否禁用 | varchar | 50 |  | √ | ' ' | 是否禁用,枚举: 1 :启用 2 :禁用 |
| 8 | fk_eafc_bus_type | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 9 | fk_eafc_field_tpye | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :文本 2 :数字 3 :日期 4 :基础资料 5 :金额 6 :小数 |
| 10 | fk_eafc_auto_volume_sel | 是否作为自动组卷字段 | bpchar | 1 |  | √ | '0' | 是否作为自动组卷字段 |
| 11 | fk_eafc_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 12 | fk_eafc_code | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fk_eafc_is_need | 是否必填 | varchar | 50 |  | √ | ' ' | 是否必填,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_archive_metadata |  | fid |
