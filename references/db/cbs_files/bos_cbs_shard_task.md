# 分片任务-bos_cbs_shard_task

## 分片任务-主表 t_cbs_shard_task

- **表名称：** 分片任务-主表
- **表名：** t_cbs_shard_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frunnode | 执行节点信息 | varchar | 200 |  | √ | ' ' | 执行节点信息 |
| 3 | fhost | 任务执行ip | varchar | 50 |  | √ | ' ' | 任务执行ip |
| 4 | ftasktype | 任务类型 | varchar | 100 |  | √ | ' ' | 任务类型,枚举: shardenable :分片启用 sharddisable :分片还原 moveindex :索引迁移 shardarchive :分表归档 |
| 5 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 6 | fprogress | 迁移进度 | varchar | 2000 |  | √ | ' ' | 迁移进度 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fstrategyparams | 分片策略参数 | varchar | 1000 |  | √ | ' ' | 分片策略参数 |
| 9 | flastfastindex | 变更前索引 | varchar | 1000 |  | √ | ' ' | 变更前索引 |
| 10 | fmoving_record | 已迁移数量 | int8 | 64 |  | √ | 0 | 已迁移数量 |
| 11 | fruninstance | 执行节点instance | varchar | 50 |  | √ | ' ' | 执行节点instance |
| 12 | ftotal_record | 总数据量 | int8 | 64 |  | √ | 0 | 总数据量 |
| 13 | fwarningstatus | 警告状态 | bpchar | 1 |  | √ | ' ' | 警告状态,枚举: 0 :正常 1 :超时异常 |
| 14 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 15 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: 0 :等待 1 :执行中 2 :成功 3 :失败 4 :已终止 5 :暂停中 6 :已暂停 |
| 16 | fcount | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 17 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 18 | fstrategyzh_cn | 分片策略属性 | varchar | 100 |  | √ | ' ' | 分片策略属性 |
| 19 | ffastindex | 变更后索引 | varchar | 1000 |  | √ | ' ' | 变更后索引 |
| 20 | fprogressdesc | 进度描述 | varchar | 2000 |  | √ | ' ' | 进度描述 |
| 21 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 22 | frunhost | 执行节点ip | varchar | 50 |  | √ | ' ' | 执行节点ip |
| 23 | farchivefield | 归档属性 | varchar | 50 |  | √ | ' ' | 归档属性 |
| 24 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 25 | ftasknode | 任务节点 | varchar | 100 |  | √ | ' ' | 任务节点,枚举: clustertblock :集群锁表 sliceanalysis :分片分析 datamove :数据迁移 clustertbunlock :集群解锁 indexmove :索引迁移 archivemove :归档迁移 |
| 26 | fconfigid | 配置ID | int8 | 64 |  | √ | 0 | 配置ID |
| 27 | fshardingfields | 分片属性 | varchar | 200 |  | √ | ' ' | 分片属性 |
| 28 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_task |  | fid |
| 2 | idx_cbs_shard_task_status |  | ftaskstatus |
| 3 | idx_cbs_shard_task |  | fentitynumber |
