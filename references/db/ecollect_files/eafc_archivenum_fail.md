# 编目失败-eafc_archivenum_fail

## 编目失败-主表 tk_eafc_archivenum_fail

- **表名称：** 编目失败-主表
- **表名：** tk_eafc_archivenum_fail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fk_eafc_archive_user | 编目人 | varchar | 50 |  | √ | ' ' | 编目人 |
| 5 | fcreatetime | 编码时间 | timestamp | 0 |  |  | null | 编码时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_eafc_result_desc | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 8 | fk_eafc_file_sign | 文件标识 | varchar | 50 |  | √ | ' ' | 文件标识 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_eafc_batchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fk_eafc_archivenum | 档案号 | varchar | 50 |  | √ | ' ' | 档案号 |
| 14 | fk_eafc_combofield | 编码结果 | varchar | 50 |  | √ | ' ' | 编码结果,枚举: 1 :编码成功 2 :编目失败 |
| 15 | fk_eafc_uniqueid | 唯一编号 | varchar | 64 |  | √ | ' ' | 唯一编号 |
| 16 | fk_eafc_textfield | 文本5 | varchar | 50 |  | √ | ' ' | 文本5 |
| 17 | fk_eafc_file_cod | 文件编码 | varchar | 50 |  | √ | ' ' | 文件编码 |
| 18 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_archivenum_fail |  | fid |
