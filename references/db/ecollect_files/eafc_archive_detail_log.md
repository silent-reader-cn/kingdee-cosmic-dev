# 接收详细日志-eafc_archive_detail_log

## 接收详细日志-主表 tk_eafc_archive_detaillog

- **表名称：** 接收详细日志-主表
- **表名：** tk_eafc_archive_detaillog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_period_new | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间 |
| 3 | fk_eafc_book_type | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fk_eafc_file_sign | 文件题名 | varchar | 500 |  | √ | ' ' | 文件题名 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 7 | fk_eafc_main_differ | 主文件失败数 | int8 | 64 |  |  | null | 主文件失败数 |
| 8 | fk_eafc_file_code | 文件编码 | varchar | 500 |  | √ | ' ' | 文件编码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpy_refbill_status | fpy_refbill_status | varchar | 50 |  | √ | ' ' |  |
| 11 | fk_eafc_billid | 文件id | int8 | 64 |  |  | null | 文件id |
| 12 | fk_eafc_creator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 13 | fk_fpy_desc | 详情描述 | varchar | 255 |  | √ | ' ' | 详情描述 |
| 14 | fk_eafc_uniqueid | 唯一id | varchar | 100 |  | √ | ' ' | 唯一id |
| 15 | fk_eafc_append_differ | 附件失败数 | int8 | 64 |  |  | null | 附件失败数 |
| 16 | fk_eafc_refbill_count | 应归关联文件数 | int4 | 32 |  | √ | 0 | 应归关联文件数 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 19 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 20 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fk_eafc_period | 属期 | timestamp | 0 |  |  | null | 属期 |
| 25 | fk_fpy_refbill_status | 关联获取 | varchar | 50 |  | √ | ' ' | 关联获取,枚举: 1 :完整 2 :缺失 |
| 26 | fk_eafc_type | 接收类型 | varchar | 50 |  | √ | ' ' | 接收类型,枚举: 1 :新增 2 :修改 3 :删除 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fk_eafc_status | 接收状态 | varchar | 50 |  | √ | ' ' | 接收状态,枚举: 1 :入库中 2 :入库成功 3 :接收失败 4 :退回中 5 :退回成功 6 :退回失败 7 :检测中 8 :自动组卷中 9 :成功 |
| 29 | fk_fpy_desc_tag | 详情描述_详情 | text | 0 |  |  | null | 详情描述_详情 |
| 30 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 31 | fk_fpy_append_status | 附件获取 | varchar | 50 |  | √ | ' ' | 附件获取,枚举: 1 :完整 2 :缺失 |
| 32 | fk_eafc_refbill_differ | 关联文件失败数 | int8 | 64 |  |  | null | 关联文件失败数 |
| 33 | fk_eafc_orgid | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fk_eafc_desc | 状态描述 | varchar | 2000 |  | √ | ' ' | 状态描述 |
| 35 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_archive_detaillog_batchnum |  | fk_eafc_batch_num |
| 2 | pk__eafc_archive_detaillog |  | fid |
| 3 | idx_eafc_archive_detaillog_bs |  | fk_eafc_batch_num,fk_eafc_status |
| 4 | idx_eafc_archive_detaillog_brc |  | fk_eafc_batch_num,fk_eafc_refbill_count |
