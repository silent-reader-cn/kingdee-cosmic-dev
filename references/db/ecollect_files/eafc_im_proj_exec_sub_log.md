# 方案执行详细日志-eafc_im_proj_exec_sub_log

## 方案执行详细日志-主表 tk_eafc_im_proj_sub_log

- **表名称：** 方案执行详细日志-主表
- **表名：** tk_eafc_im_proj_sub_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  | √ | 0 | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fpy_refbill_status | fpy_refbill_status | varchar | 50 |  | √ | ' ' |  |
| 7 | fk_eafc_billid | 唯一id | varchar | 100 |  | √ | ' ' | 唯一id |
| 8 | fk_fpy_desc | 详情描述 | varchar | 255 |  | √ | ' ' | 详情描述 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fk_eafc_pro_logid | 方案执行日志id | int8 | 64 |  |  | null | 方案执行日志id |
| 11 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 12 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fk_eafc_data_json_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fk_eafc_period | 归档期间 | varchar | 50 |  | √ | ' ' | 归档期间 |
| 17 | fk_fpy_refbill_status | 关联获取 | varchar | 50 |  | √ | ' ' | 关联获取,枚举: 1 :完整 2 :缺失 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fk_eafc_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :成功 1 :失败 |
| 20 | fk_fpy_desc_tag | 详情描述_详情 | text | 0 |  |  | null | 详情描述_详情 |
| 21 | fk_eafc_content | 归档内容 | int8 | 64 |  |  | null | [集成内容 eafc_im_content](../ecollect_files/eafc_im_content.md) |
| 22 | fk_eafc_data_json | 数据 | varchar | 255 |  | √ | ' ' | 数据 |
| 23 | fk_fpy_append_status | 附件获取 | varchar | 50 |  | √ | ' ' | 附件获取,枚举: 1 :完整 2 :缺失 |
| 24 | fk_eafc_file_name | 文件名 | varchar | 100 |  |  | null | 文件名 |
| 25 | fk_eafc_project | 方案 | int8 | 64 |  |  | null | [集成方案 eafc_im_project](../ecollect_files/eafc_im_project.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_proj_sub_log |  | fid |
| 2 | idx_eafc_im_proj_sub_log_pid |  | fk_eafc_pro_logid |
