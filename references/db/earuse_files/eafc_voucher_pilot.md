# 财政局-电子凭证试点-eafc_voucher_pilot

## 财政局-电子凭证试点-主表 tk_eafc_voucher_pilot

- **表名称：** 财政局-电子凭证试点-主表
- **表名：** tk_eafc_voucher_pilot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_opt_date | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fk_eafc_data_lasttime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fk_eafc_download_count | 下载次数 | int8 | 64 |  |  | null | 下载次数 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fk_eafc_period | 期间 | timestamp | 0 |  |  | null | 期间 |
| 9 | forgid | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fk_eafc_attachmentnum | 附件数 | int8 | 64 |  |  | null | 附件数 |
| 11 | fk_eafc_download_lasttime | 最后下载时间 | timestamp | 0 |  |  | null | 最后下载时间 |
| 12 | fk_eafc_book_type | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fk_eafc_number | 数量 | int8 | 64 |  |  | null | 数量 |
| 15 | fk_eafc_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :已报送 2 :待报送 |
| 16 | fk_eafc_opt_user | 操作人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_fileurl | 附件地址 | varchar | 50 |  | √ | ' ' | 附件地址 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_voucher_pilot |  | fid |
