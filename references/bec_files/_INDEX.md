# bec 模块表清单

> 本模块共收录 **16** 张表定义，来自 `bec_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope bec
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_evt_deadletterjob` | 异常信息-主表 | 31 | [evt_deadletterjob.md](./evt_deadletterjob.md) |
| 2 | `t_evt_deadletterjob_l` | 异常信息-多语言表 | 7 | [evt_deadletterjob.md](./evt_deadletterjob.md) |
| 3 | `t_evt_event` | 事件定义-主表 | 19 | [evt_event.md](./evt_event.md) |
| 4 | `t_evt_event_l` | 事件定义-多语言表 | 6 | [evt_event.md](./evt_event.md) |
| 5 | `t_evt_eventconfig` | 事件参数-子表 | 9 | [evt_event.md](./evt_event.md) |
| 6 | `t_evt_eventconfig_l` | 事件参数-多语言表 | 6 | [evt_event.md](./evt_event.md) |
| 7 | `t_evt_hijobrecord` | 历史事件日志-主表 | 32 | [evt_hijob.md](./evt_hijob.md) |
| 8 | `t_evt_jobrecord` | 事件日志-主表 | 32 | [evt_job.md](./evt_job.md) |
| 9 | `t_evt_jobstatistics` | 事件日志统计-主表 | 16 | [evt_jobstatistics.md](./evt_jobstatistics.md) |
| 10 | `t_evt_jobstatistics_l` | 事件日志统计-多语言表 | 4 | [evt_jobstatistics.md](./evt_jobstatistics.md) |
| 11 | `t_evt_log` | 事件日志（内部）-主表 | 11 | [evt_log.md](./evt_log.md) |
| 12 | `t_evt_service` | 服务目录-主表 | 14 | [evt_service.md](./evt_service.md) |
| 13 | `t_evt_service_l` | 服务目录-多语言表 | 4 | [evt_service.md](./evt_service.md) |
| 14 | `t_evt_subscription` | 事件订阅-主表 | 28 | [evt_subscription.md](./evt_subscription.md) |
| 15 | `t_evt_subscription_l` | 事件订阅-多语言表 | 5 | [evt_subscription.md](./evt_subscription.md) |
| 16 | `t_evt_timerjob` | 定时工作-主表 | 25 | [evt_timerjob.md](./evt_timerjob.md) |
