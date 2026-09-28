# 集成云后台任务-isc_job_inst

## 集成云后台任务-主表 t_isc_job_inst

- **表名称：** 集成云后台任务-主表
- **表名：** t_isc_job_inst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fcreator | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fhost | 服务器IP | varchar | 150 |  | √ | ' ' | 服务器IP |
| 5 | fparam | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 6 | fscheduled_time | 计划时间 | timestamp | 0 |  |  | null | 计划时间 |
| 7 | fjob_owner | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 8 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 9 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | ftitle | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 11 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: CREATED :新建 WAITING :等待中 READY :就绪 RUNNING :执行中 FAILED :已失败 COMPLETE :已完成 TERMINATED :已撤销 |
| 13 | fstarted_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 14 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: DATA_COPY_RUNNER :集成任务 DATA_COPY_STAGE :任务分批 SF_PROC_EXEC :服务流程执行 SF_TIMER_WAITING :服务流程时间等待 SF_TIMER_STARTER :服务流程定时触发 SF_PROC_ABORT :撤销服务流程 SF_EVENT_WAITING :服务流程事件等待 SF_PROC_SIGNAL :服务流程唤醒 MAP_DATA :参照数据映射 SYNC_META :元数据同步 SYNC_DATA :参照数据同步 RES_IMP :资源导入 IMPORT_DATA_FILE :文件集成导入任务 EXPORT_DATA_FILE :文件集成导出任务 DataCopyJob :数据集成任务 DC_LOG_REDO :数据日志重做 RES_PARSE :文件资源解析 RES_IMP2 :文件资源导入 DATA_COMP :数据对比 SOLUTION_DEPLOY :解决方案部署 CHECK_SF_BIGLOGS :流程日志监测 ISC_HUB_EVT :集成HUB事件 SOLUTION_COMPARE :资源对比 SOLUTION_UPDATE :资源更新 SOLUTION_IMPORT :导入资源包 UPDATE_REF :更新引用资源 ISC_HEALTH_CHECK :健康度检测 UPDATE_CLOUD_CN_TYPE :云更新连接类型 UPDATE_CLOUD_SOLUTION :云更新解决方案 TRIGGER_CRON :定时启动方案 FLOW_CRON :定时服务流程 API_CRON :定时API调度 EVENT_REFRESH :定时更新事件触发 DELETE_LOG :清理日志任务 QUERY_LOG :检测日志任务 DatabaseCopySubJob :数据库复制 DatabaseCompSubJob :数据库比较 sync_isc_article :同步集成云帖子 TABLECOPY_CRON :定时数据表复制 DBC_TABLECOPY :数据表复制 update_white_list :更新云端白名单 RES_IMP_WHITE_LIST :文件资源导入(白名单) MService_IMP :微服务导入 |
| 15 | fmodified_time | 最近修改时间 | timestamp | 0 |  |  | null | 最近修改时间 |
| 16 | ftype2 | 任务类型 | varchar | 30 |  | √ | ' ' | 集成云后台任务类型 isc_job_type |
| 17 | flang | 语言编码 | varchar | 50 |  | √ | 'zh_CN' | 语言编码 |
| 18 | fparam_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_job_inst_1 |  | ftitle |
| 2 | idx_isc_job_inst_2 |  | fscheduled_time |
| 3 | t_isc_job_inst_pkey |  | fid |
| 4 | idx_isc_job_inst_3 |  | fmodified_time |
| 5 | idx_isc_job_inst_4 |  | fjob_owner |
