# 手工批量采集-eafc_archive_info

## 手工批量采集-主表 tk_eafc_archive_info

- **表名称：** 手工批量采集-主表
- **表名：** tk_eafc_archive_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_store_form | 采集默认存储形式 | varchar | 50 |  | √ | ' ' | 采集默认存储形式,枚举: 1 :电子 2 :纸质/电子 |
| 4 | fk_eafc_batch_no | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 5 | fk_eafc_data_period_str | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 6 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 9 | fcreatorid | 采集人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fk_eafc_basedatafield | 分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 11 | fk_eafc_data_period | 期间 | timestamp | 0 |  |  | null | 期间 |
| 12 | fk_eafc_rootid | 树结构根节点的id | varchar | 50 |  | √ | ' ' | 树结构根节点的id |
| 13 | fk_eafc_task_status | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: 1 :待提交 2 :暂存 3 :已完成 0 :待采集 4 :采集中 5 :采集异常 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fk_eafc_end_date | 采集结束时间 | timestamp | 0 |  |  | null | 采集结束时间 |
| 16 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 17 | fk_eafc_status_describe | 采集状态描述 | varchar | 200 |  | √ | ' ' | 采集状态描述 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_task_name | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fk_eafc_collect_progress | 采集进度 | numeric | 23 | 10 |  | null | 采集进度 |
| 23 | fk_eafc_source_in_out | 销方/购方 | varchar | 50 |  | √ | ' ' | 销方/购方,枚举: 1 :购方 2 :销方 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fk_eafc_enable_recog | 启用识别 | bpchar | 1 |  | √ | '0' | 启用识别 |
| 26 | fk_eafc_collect_type | 采集方式 | varchar | 50 |  | √ | ' ' | 采集方式,枚举: 1 :本地上传 2 :扫描 3 :同步 |
| 27 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fk_eafc_collect_dimension | 采集维度 | varchar | 50 |  | √ | ' ' | 采集维度,枚举: 1 :整册 2 :单件 3 :文件名称挂接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_archive_info |  | fid |

---

## 凭证册信息-子表 tk_eafc_archive_info_ent

- **表名称：** 凭证册信息-子表
- **表名：** tk_eafc_archive_info_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_book_total | 册数 | int8 | 64 |  |  | null | 册数 |
| 3 | fk_eafc_case_number | 案卷号(id) | varchar | 50 |  | √ | ' ' | 案卷号(id) |
| 4 | fk_eafc_account_year | 会计年度 | timestamp | 0 |  |  | null | 会计年度 |
| 5 | fk_eafc_voucher_no_end | 凭证号(结束) | varchar | 50 |  | √ | ' ' | 凭证号(结束) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fk_eafc_voucher_word | 凭证字 | varchar | 50 |  | √ | ' ' | 凭证字 |
| 8 | fk_eafc_book_no | 册号 | int8 | 64 |  |  | null | 册号 |
| 9 | fk_eafc_account_month | 会计月份 | varchar | 50 |  | √ | ' ' | 会计月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 10 | fk_eafc_volume_no | 册次号 | varchar | 30 |  | √ | ' ' | 册次号 |
| 11 | fk_eafc_collect_status | 采集状态 | varchar | 50 |  | √ | ' ' | 采集状态,枚举: 0 :待采集 1 :已采集 |
| 12 | fk_eafc_box_no | 盒号 | varchar | 30 |  | √ | ' ' | 盒号 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 14 | fk_eafc_case_no | 案卷号 | varchar | 30 |  | √ | ' ' | 案卷号 |
| 15 | fk_eafc_voucher_no_start | 凭证号(起始) | varchar | 50 |  | √ | ' ' | 凭证号(起始) |
| 16 | fk_eafc_volume_number | 册次号(id) | varchar | 50 |  | √ | ' ' | 册次号(id) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_archive_info_ent |  | fentryid |
