# 组卷/拆卷日志-fpy_volume_operation

## 组卷/拆卷日志-主表 tk_fpy_volume_operate

- **表名称：** 组卷/拆卷日志-主表
- **表名：** tk_fpy_volume_operate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_creater_arcorg | 操作人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fk_fpy_volume_mode | 组卷方式 | varchar | 50 |  | √ | ' ' | 组卷方式,枚举: 1 :自动组卷 2 :手动组卷 3 :扫码组卷 |
| 5 | fk_fpy_createdate | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 6 | fk_fpy_creater | 操作人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fk_fpy_operation_type | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: 1 :组卷 2 :拆卷 |
| 8 | fk_fpy_volume | 卷号 | varchar | 100 |  | √ | ' ' | 卷号 |
| 9 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 10 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 11 | fk_fpy_volume_name | 案卷题名 | varchar | 200 |  | √ | ' ' | 案卷题名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_volume_op_creater |  | fk_fpy_creater |
| 2 | idx_volume_op_arcorg |  | fk_eafc_arcorg |
| 3 | idx_volume_op_volume |  | fk_fpy_volume |
| 4 | pk_fpy_volume_operate |  | fid |
| 5 | idx_volume_op_createdate |  | fk_fpy_createdate |
