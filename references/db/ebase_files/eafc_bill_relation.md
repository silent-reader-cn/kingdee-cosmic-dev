# 上下游单据关系表-eafc_bill_relation

## 上下游单据关系表-主表 tk_eafc_bill_relation

- **表名称：** 上下游单据关系表-主表
- **表名：** tk_eafc_bill_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_upper_billid | 上游单据主键ID | int8 | 64 |  |  | null | 上游单据主键ID |
| 4 | fk_eafc_upper_uniqueid | 上游单据唯一ID | varchar | 50 |  | √ | ' ' | 上游单据唯一ID |
| 5 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fk_eafc_billid | 单据主键ID | int8 | 64 |  |  | null | 单据主键ID |
| 7 | fk_eafc_uniqueid | 单据唯一ID | varchar | 50 |  | √ | ' ' | 单据唯一ID |
| 8 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 9 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 10 | fk_eafc_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_bill_relation |  | fid |
| 2 | idx_eafc_bill_rela_uid |  | fk_eafc_uniqueid,fk_eafc_upper_uniqueid |
