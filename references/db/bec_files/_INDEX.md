# bec 模块表清单

> 本模块共收录 **36** 张表定义，来自 `bec_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category bec
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_evt_abnormalinstance` | 异常订阅实例-主表 | 32 | [evt_abnormalinstance.md](./evt_abnormalinstance.md) |
| 2 | `t_evt_abnormalsubs` | 异常订阅-主表 | 21 | [evt_abnormalsubs.md](./evt_abnormalsubs.md) |
| 3 | `t_evt_abnormalsubs_l` | 异常订阅-多语言表 | 8 | [evt_abnormalsubs.md](./evt_abnormalsubs.md) |
| 4 | `t_evt_deadletterjob` | 异常信息-主表 | 31 | [evt_deadletterjob.md](./evt_deadletterjob.md) |
| 5 | `t_evt_deadletterjob_l` | 异常信息-多语言表 | 7 | [evt_deadletterjob.md](./evt_deadletterjob.md) |
| 6 | `t_evt_devopstask` | 运维任务表-主表 | 6 | [evt_devops_task.md](./evt_devops_task.md) |
| 7 | `t_evt_event` | 事件定义-主表 | 19 | [evt_event.md](./evt_event.md) |
| 8 | `t_evt_event_l` | 事件定义-多语言表 | 6 | [evt_event.md](./evt_event.md) |
| 9 | `t_evt_eventconfig` | 事件参数-子表 | 9 | [evt_event.md](./evt_event.md) |
| 10 | `t_evt_eventconfig_l` | 事件参数-多语言表 | 6 | [evt_event.md](./evt_event.md) |
| 11 | `t_evt_hiabnormalsubs` | 历史异常订阅-主表 | 21 | [evt_hiabnormalsubs.md](./evt_hiabnormalsubs.md) |
| 12 | `t_evt_hiabnormalsubs_l` | 历史异常订阅-多语言表 | 8 | [evt_hiabnormalsubs.md](./evt_hiabnormalsubs.md) |
| 13 | `t_evt_hijobrecord` | 历史事件日志-主表 | 32 | [evt_hijob.md](./evt_hijob.md) |
| 14 | `t_evt_jobrecord` | 事件日志-主表 | 32 | [evt_job.md](./evt_job.md) |
| 15 | `t_evt_jobstatistics` | 事件日志统计-主表 | 16 | [evt_jobstatistics.md](./evt_jobstatistics.md) |
| 16 | `t_evt_jobstatistics_l` | 事件日志统计-多语言表 | 4 | [evt_jobstatistics.md](./evt_jobstatistics.md) |
| 17 | `t_evt_log` | 事件日志（内部）-主表 | 11 | [evt_log.md](./evt_log.md) |
| 18 | `t_evt_queueconfig` | 队列资源管理-主表 | 5 | [evt_queue_config.md](./evt_queue_config.md) |
| 19 | `t_evt_queueconfig_l` | 队列资源管理-多语言表 | 4 | [evt_queue_config.md](./evt_queue_config.md) |
| 20 | `t_evt_queueconfigdetail` | 单据体-子表 | 7 | [evt_queue_config.md](./evt_queue_config.md) |
| 21 | `t_evt_regulation` | 自动处理策略-主表 | 14 | [evt_rule.md](./evt_rule.md) |
| 22 | `t_evt_regulation_l` | 自动处理策略-多语言表 | 5 | [evt_rule.md](./evt_rule.md) |
| 23 | `t_evt_ruleshieldsubs` | 屏蔽规则的订阅-子表 | 4 | [evt_rule.md](./evt_rule.md) |
| 24 | `t_evt_service` | 服务目录-主表 | 14 | [evt_service.md](./evt_service.md) |
| 25 | `t_evt_service_l` | 服务目录-多语言表 | 4 | [evt_service.md](./evt_service.md) |
| 26 | `t_evt_subscription` | 事件订阅-主表 | 28 | [evt_subscription.md](./evt_subscription.md) |
| 27 | `t_evt_subscription` | 业务异常白名单-主表 | 28 | [evt_whitelist_config.md](./evt_whitelist_config.md) |
| 28 | `t_evt_subscription_l` | 事件订阅-多语言表 | 5 | [evt_subscription.md](./evt_subscription.md) |
| 29 | `t_evt_subscription_l` | 业务异常白名单-多语言表 | 5 | [evt_whitelist_config.md](./evt_whitelist_config.md) |
| 30 | `t_evt_timerjob` | 定时工作-主表 | 25 | [evt_timerjob.md](./evt_timerjob.md) |
| 31 | `t_evt_whitelist` | 单据体-子表 | 10 | [evt_whitelist_config.md](./evt_whitelist_config.md) |
| 32 | `t_evt_whitelist_l` | 单据体-多语言表 | 4 | [evt_whitelist_config.md](./evt_whitelist_config.md) |
| 33 | `t_wf_alarmmsgsendlog` | 报警消息发送日志-主表 | 17 | [evt_alarmmessagesendlog.md](./evt_alarmmessagesendlog.md) |
| 34 | `t_wf_alarmmsgsendlog_l` | 报警消息发送日志-多语言表 | 7 | [evt_alarmmessagesendlog.md](./evt_alarmmessagesendlog.md) |
| 35 | `t_wf_alarmrule` | 报警消息设置-主表 | 15 | [evt_alarmrulesetting.md](./evt_alarmrulesetting.md) |
| 36 | `t_wf_alarmrule_l` | 报警消息设置-多语言表 | 6 | [evt_alarmrulesetting.md](./evt_alarmrulesetting.md) |
