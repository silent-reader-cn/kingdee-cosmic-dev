# 调用日志-aicc_task

## 调用日志-主表 t_aicc_task

- **表名称：** 调用日志-主表
- **表名：** t_aicc_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 4 | ferrcode | 错误代码 | varchar | 50 |  | √ | ' ' | 错误代码 |
| 5 | ftenantid | 租户 | int8 | 64 |  | √ | 0 | [服务租户 aicc_tenant](../aicc_files/aicc_tenant.md) |
| 6 | fresult | 结果 | varchar | 255 |  | √ | ' ' | 结果 |
| 7 | fcompletiontokens | 输出token | varchar | 50 |  | √ | ' ' | 输出token |
| 8 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | ftotaltokens | 总token | varchar | 50 |  | √ | ' ' | 总token |
| 10 | ftasksourcecode | 任务来源标识 | varchar | 100 |  | √ | ' ' | 任务来源标识 |
| 11 | fresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 12 | frequestbody | 请求体 | varchar | 255 |  | √ | ' ' | 请求体 |
| 13 | frequestbody_tag | 请求体_详情 | text | 0 |  |  | null | 请求体_详情 |
| 14 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: create :新增 running :执行中 failed :执行失败 success :执行成功 timeout :执行超时 response :首token响应 stopped :停止 waiting :队列等待中 outlimit :超出队列限制 |
| 15 | fisstream | 流式任务 | bpchar | 1 |  | √ | '0' | 流式任务 |
| 16 | fprompttokens | 输入token | varchar | 50 |  | √ | ' ' | 输入token |
| 17 | ferrmsg | 错误信息 | varchar | 1024 |  | √ | ' ' | 错误信息 |
| 18 | fkddatapackage | 使用金蝶大模型流量包 | bpchar | 1 |  | √ | '0' | 使用金蝶大模型流量包 |
| 19 | finstanceid | 执行实例 | int8 | 64 |  | √ | 0 | [算法部署实例 aicc_instance](../aicc_files/aicc_instance.md) |
| 20 | fserviceid | 服务 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 21 | fisasync | 异步任务 | bpchar | 1 |  | √ | '0' | 异步任务 |
| 22 | fformatcontent_tag | 流式格式化_详情 | text | 0 |  |  | ' ' | 流式格式化_详情 |
| 23 | fformatcontent | 流式格式化 | varchar | 255 |  | √ | ' ' | 流式格式化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aicc_task |  | fid |
| 2 | idx_aicc_task_tenant_id |  | ftenantid |
| 3 | idx_aicc_task_service_id |  | fserviceid |
| 4 | idx_aicc_task_createtime |  | fcreatetime |
| 5 | idx_aicc_task_instance_id |  | finstanceid |
