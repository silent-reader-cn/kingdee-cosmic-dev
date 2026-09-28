# 数据同步日志查询-rim_down_log

## 数据同步日志查询-主表 t_rim_down_log

- **表名称：** 数据同步日志查询-主表
- **表名：** t_rim_down_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvoice_enddate | 下载结束时间 | timestamp | 0 |  |  | null | 下载结束时间 |
| 3 | fsync_gov_status | 同步状态 | varchar | 2 |  | √ | ' ' | 同步状态,枚举: 1 :成功 2 :数据不全 3 :已下载表头 4 :表头下载失败 5 :进销项下载失败 6 :进销项下载处理中 7 :进销项下载申请失败 8 :进销项已下载 9 :没有发票 |
| 4 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 5 | frequest_id | 进销项申请id | varchar | 50 |  | √ | ' ' | 进销项申请id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsync_type | 同步类型 | varchar | 2 |  | √ | ' ' | 同步类型,枚举: 1 :进项采集 2 :当前月进销项下载 3 :历史月进销项下载 4 :当前属期进项下载 5 :手工导入 |
| 8 | fbatch_no | 发票云同步批次号 | varchar | 36 |  | √ | ' ' | 发票云同步批次号 |
| 9 | ftax_no | 税号 | varchar | 30 |  | √ | ' ' | 税号 |
| 10 | finout | 进销项 | varchar | 2 |  | √ | ' ' | 进销项,枚举: 1 :进项 2 :销项 3 :进项状态更新 |
| 11 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fapply_step | 进销项申请页数 | int4 | 32 |  | √ | 0 | 进销项申请页数 |
| 14 | fsync_task_no | 增量同步任务号 | varchar | 50 |  | √ | ' ' | 增量同步任务号 |
| 15 | ftax_batch_no | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 16 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 17 | ftaskno | 进销项下载任务号 | varchar | 50 |  | √ | ' ' | 进销项下载任务号 |
| 18 | finvoice_startdate | 下载开始时间 | timestamp | 0 |  |  | null | 下载开始时间 |
| 19 | fsuccess_total_num | 处理成功的份数 | int4 | 32 |  | √ | 0 | 处理成功的份数 |
| 20 | ftotal_num | 下载的发票份数 | int4 | 32 |  | √ | 0 | 下载的发票份数 |
| 21 | fdownload_errcode | 申请状态 | varchar | 10 |  | √ | ' ' | 申请状态,枚举: 0 :申请中 1 :申请失败 2 :申请成功税局未完成 3 :申请成功 4 :没有发票 5 :下载失败 6 :文件处理失败 7 :归集申请提交失败 8 :税盘登录失败 9 :更新为正在处理中 10 :无申请记录 11 :进度查询失败 12 :登录失败 13 :全电企业,不支持 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_down_log_type |  | finvoicetype |
| 2 | idx_rim_down_log_govstatus |  | fsync_gov_status |
| 3 | idx_rim_down_log_batch_no |  | fbatch_no |
| 4 | pk_rim_down_log |  | fid |
| 5 | idx_rim_down_log_org |  | forg |
| 6 | idx_rim_down_log_tax_no |  | ftax_no |
