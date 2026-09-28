# 组件日志记录-fpy_relation_log

## 组件日志记录-主表 tk_fpy_relation_log

- **表名称：** 组件日志记录-主表
- **表名：** tk_fpy_relation_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_file_code_tar | 目标单据-文件编码 | varchar | 100 |  | √ | ' ' | 目标单据-文件编码 |
| 3 | fk_fpy_file_sign | 来源单据-文件题名 | varchar | 200 |  | √ | ' ' | 来源单据-文件题名 |
| 4 | fk_fpy_id | 来源单据-id | int8 | 64 |  | √ | 0 | 来源单据-id |
| 5 | fk_fpy_task_no | 组件批次号 | varchar | 50 |  | √ | ' ' | 组件批次号 |
| 6 | fk_fpy_createdate | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 7 | fk_fpy_file_sign_tar | 目标单据-文件题名 | varchar | 200 |  | √ | ' ' | 目标单据-文件题名 |
| 8 | fk_fpy_file_code | 来源单据-文件编码 | varchar | 100 |  | √ | ' ' | 来源单据-文件编码 |
| 9 | fk_fpy_arcorg_tar | 目标单据-归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 10 | fk_fpy_book_type_tar | 目标单据-机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 11 | fk_fpy_business_tar | 目标单据-三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 12 | fk_fpy_id_tar | 目标单据-id | int8 | 64 |  | √ | 0 | 目标单据-id |
| 13 | fk_fpy_operator | 操作人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_fpy_relation_status | 组件状态 | varchar | 50 |  | √ | ' ' | 组件状态,枚举: 1 :关联成功 2 :关联失败 |
| 15 | fk_fpy_relation_mode | 组件方式 | varchar | 50 |  | √ | ' ' | 组件方式,枚举: 1 :智能方案组件 2 :在线接收组件 3 :手动组件 |
| 16 | fk_fpy_description | 组件结果描述 | varchar | 50 |  | √ | ' ' | 组件结果描述 |
| 17 | fk_fpy_rule_name | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 18 | fk_fpy_relation_conf | 组件方案 | int8 | 64 |  |  | null | [组件方案配置 fpy_match_relation_conf](../ecollect_files/fpy_match_relation_conf.md) |
| 19 | fk_fpy_book_type | 来源单据-机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 20 | fk_eafc_arcorg | 来源单据-归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 21 | fk_fpy_business | 来源单据-三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_relation_src_id |  | fk_fpy_id |
| 2 | idx_relation_task_no |  | fk_fpy_task_no |
| 3 | pk_fpy_relation_log |  | fid |
| 4 | idx_relation_arcorg |  | fk_eafc_arcorg |
| 5 | idx_relation_tar_id |  | fk_fpy_id_tar |
