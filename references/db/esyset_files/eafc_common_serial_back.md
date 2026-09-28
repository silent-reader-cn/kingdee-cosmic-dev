# 流水号表_备份表-eafc_common_serial_back

## 流水号表_备份表-主表 tk_eafc_comm_serial_bak

- **表名称：** 流水号表_备份表-主表
- **表名：** tk_eafc_comm_serial_bak

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_serial_field | 流水号字段 | varchar | 50 |  | √ | ' ' | 流水号字段 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_eafc_data_pk | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 7 | fk_eafc_bak_time | 备份时间 | timestamp | 0 |  |  | null | 备份时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_eafc_feature_md5 | 特征码(md5) | varchar | 100 |  | √ | ' ' | 特征码(md5) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_eafc_feature_code | 特征码 | varchar | 1000 |  | √ | ' ' | 特征码 |
| 13 | fk_eafc_form_type | 表单类型 | varchar | 50 |  | √ | ' ' | 表单类型 |
| 14 | fk_eafc_bak_batch | 备份批次 | varchar | 50 |  | √ | ' ' | 备份批次 |
| 15 | fk_fpy_source_code | 原号段字段 | varchar | 50 |  | √ | ' ' | 原号段字段 |
| 16 | fbillno | 流水号 | varchar | 200 |  | √ | ' ' | 流水号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_comm_serial_bak |  | fid |
