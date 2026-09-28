# 数据源请求日志-eafc_im_ds_request_log

## 数据源请求日志-主表 tk_eafc_im_ds_request_log

- **表名称：** 数据源请求日志-主表
- **表名：** tk_eafc_im_ds_request_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_request_param_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_eafc_request_status | 请求状态 | varchar | 50 |  | √ | ' ' | 请求状态,枚举: 0 :成功 1 :失败 |
| 7 | fk_eafc_system_name | 系统名称 | varchar | 50 |  | √ | ' ' | 系统名称 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fk_eafc_fail_info | 失败原因 | varchar | 503 |  | √ | ' ' | 失败原因 |
| 10 | fk_eafc_request_url | 请求地址 | varchar | 500 |  | √ | ' ' | 请求地址 |
| 11 | fk_eafc_ds_name | 数据源名称 | varchar | 50 |  | √ | ' ' | 数据源名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fk_eafc_project_name | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 14 | fk_eafc_request_param | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |
| 15 | fk_eafc_request_result | 请求结果 | varchar | 255 |  | √ | ' ' | 请求结果 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fk_eafc_request_time | 请求耗时(毫秒) | int8 | 64 |  |  | null | 请求耗时(毫秒) |
| 18 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 19 | fk_eafc_project | 方案 | int8 | 64 |  |  | 0 | [集成方案 eafc_im_project](../ecollect_files/eafc_im_project.md) |
| 20 | fk_eafc_request_result_tag | 请求结果_详情 | text | 0 |  |  | null | 请求结果_详情 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_request_log_dsname |  | fk_eafc_ds_name |
| 2 | idx_eafc_request_log_batch |  | fk_eafc_batch_num |
| 3 | idx_eafc_request_log_proj |  | fk_eafc_project |
| 4 | pk__eafc_im_ds_request_log |  | fid |
