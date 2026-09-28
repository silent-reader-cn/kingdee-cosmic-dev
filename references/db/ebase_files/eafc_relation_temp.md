# 关系临时表-eafc_relation_temp

## 关系临时表-主表 tk_eafc_relation_temp

- **表名称：** 关系临时表-主表
- **表名：** tk_eafc_relation_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_src_uniqueid | 源唯一ID | varchar | 50 |  | √ | ' ' | 源唯一ID |
| 4 | fk_eafc_srcid | 源主键ID | int8 | 64 |  | √ | 0 | 源主键ID |
| 5 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fk_eafc_destid | 目标主键ID | int8 | 64 |  | √ | 0 | 目标主键ID |
| 7 | fk_eafc_relation_type | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: 1 :凭证关联单据 2 :凭证关联回单 3 :凭证关联发票 4 :单据关联发票 5 :单据上下游 |
| 8 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 9 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 10 | fk_eafc_dest_uniqueid | 目标唯一ID | varchar | 50 |  | √ | ' ' | 目标唯一ID |
| 11 | fk_eafc_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_relation_temp |  | fid |
