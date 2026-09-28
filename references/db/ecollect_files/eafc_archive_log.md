# 在线接收日志-eafc_archive_log

## 在线接收日志-主表 tk_eafc_archive_log

- **表名称：** 在线接收日志-主表
- **表名：** tk_eafc_archive_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 3 | fk_eafc_ref_ok_count | 实归关联文件数 | int8 | 64 |  |  | null | 实归关联文件数 |
| 4 | fk_eafc_fail | 失败数 | int8 | 64 |  |  | null | 失败数 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fk_eafc_append_ok_count | 实归附件数 | int8 | 64 |  |  | null | 实归附件数 |
| 7 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_eafc_ref_fail_count | 关联文件失败数 | int8 | 64 |  |  | null | 关联文件失败数 |
| 10 | fk_eafc_main_count | 应归主文件数 | int8 | 64 |  |  | null | 应归主文件数 |
| 11 | fk_eafc_creator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 12 | fk_eafc_main_fail_count | 主文件失败数 | int8 | 64 |  |  | null | 主文件失败数 |
| 13 | fk_eafc_refbill_count | 应归关联文件数 | int8 | 64 |  |  | null | 应归关联文件数 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统,枚举: 1 :ERP 2 :异构 3 :手工 |
| 16 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fk_eafc_period | 期属 | timestamp | 0 |  |  | null | 期属 |
| 21 | fk_eafc_bytediffer_count | 电子文件字节差异 | int8 | 64 |  |  | null | 电子文件字节差异 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fk_eafc_status | 接收状态 | varchar | 50 |  | √ | ' ' | 接收状态,枚举: 1 :入库中 2 :入库成功 3 :入库失败 4 :退回中 5 :退回成功 6 :退回失败 7 :检测中 8 :自动组卷中 9 :已完成 10 :待入库 11 :已终止 |
| 24 | fk_eafc_append_fail_count | 附件失败数 | int8 | 64 |  |  | null | 附件失败数 |
| 25 | fk_eafc_append_count | 应归附件数 | int8 | 64 |  |  | null | 应归附件数 |
| 26 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 27 | fk_eafc_total | 总数 | int8 | 64 |  |  | null | 总数 |
| 28 | fk_eafc_orgid | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fk_eafc_progress | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 30 | fk_eafc_main_ok_count | 实归主文件数 | int8 | 64 |  |  | null | 实归主文件数 |
| 31 | fk_eafc_desc | 接收描述 | varchar | 2000 |  | √ | ' ' | 接收描述 |
| 32 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_archive_log_batchnum |  | fk_eafc_batch_num |
| 2 | pk__eafc_archive_log |  | fid |
