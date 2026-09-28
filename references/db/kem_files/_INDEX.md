# kem 模块表清单

> 本模块共收录 **28** 张表定义，来自 `kem_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category kem
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_kem_actiontype` | 目标服务类型-主表 | 15 | [kem_actiontype.md](./kem_actiontype.md) |
| 2 | `t_kem_actiontype_l` | 目标服务类型-多语言表 | 5 | [kem_actiontype.md](./kem_actiontype.md) |
| 3 | `t_kem_event` | 事件-主表 | 28 | [kem_event.md](./kem_event.md) |
| 4 | `t_kem_event` | 开放事件-主表 | 28 | [kem_event_open.md](./kem_event_open.md) |
| 5 | `t_kem_event_l` | 事件-多语言表 | 5 | [kem_event.md](./kem_event.md) |
| 6 | `t_kem_event_l` | 开放事件-多语言表 | 5 | [kem_event_open.md](./kem_event_open.md) |
| 7 | `t_kem_eventbus` | 事件通道-主表 | 12 | [kem_eventbus.md](./kem_eventbus.md) |
| 8 | `t_kem_eventbus_l` | 事件通道-多语言表 | 4 | [kem_eventbus.md](./kem_eventbus.md) |
| 9 | `t_kem_eventgroup` | 事件分类-主表 | 17 | [kem_eventgroup.md](./kem_eventgroup.md) |
| 10 | `t_kem_eventgroup_l` | 事件分类-多语言表 | 5 | [kem_eventgroup.md](./kem_eventgroup.md) |
| 11 | `t_kem_eventpara` | Data单据体-子表 | 12 | [kem_event.md](./kem_event.md) |
| 12 | `t_kem_eventpara` | Data单据体-子表 | 12 | [kem_event_open.md](./kem_event_open.md) |
| 13 | `t_kem_eventpara_l` | Data单据体-多语言表 | 5 | [kem_event.md](./kem_event.md) |
| 14 | `t_kem_eventpara_l` | Data单据体-多语言表 | 5 | [kem_event_open.md](./kem_event_open.md) |
| 15 | `t_kem_openeventsub` | 事件推送订阅-主表 | 21 | [kem_sub_open.md](./kem_sub_open.md) |
| 16 | `t_kem_openeventsub_l` | 事件推送订阅-多语言表 | 6 | [kem_sub_open.md](./kem_sub_open.md) |
| 17 | `t_kem_openeventsubdetl` | 单据体-子表 | 6 | [kem_sub_open.md](./kem_sub_open.md) |
| 18 | `t_kem_queue` | 事件消息监控-主表 | 18 | [kem_msg_queue.md](./kem_msg_queue.md) |
| 19 | `t_kem_sub` | 事件订阅-主表 | 32 | [kem_subscribe.md](./kem_subscribe.md) |
| 20 | `t_kem_sub` | 订阅详情-主表 | 32 | [kem_subscribe_inh.md](./kem_subscribe_inh.md) |
| 21 | `t_kem_sub_l` | 事件订阅-多语言表 | 6 | [kem_subscribe.md](./kem_subscribe.md) |
| 22 | `t_kem_sub_l` | 订阅详情-多语言表 | 6 | [kem_subscribe_inh.md](./kem_subscribe_inh.md) |
| 23 | `t_kem_subcond` | 订阅规则-子表 | 11 | [kem_subscribe.md](./kem_subscribe.md) |
| 24 | `t_kem_subcond` | 订阅规则-子表 | 11 | [kem_subscribe_inh.md](./kem_subscribe_inh.md) |
| 25 | `t_kem_subcond_l` | 订阅规则-多语言表 | 4 | [kem_subscribe.md](./kem_subscribe.md) |
| 26 | `t_kem_subcond_l` | 订阅规则-多语言表 | 4 | [kem_subscribe_inh.md](./kem_subscribe_inh.md) |
| 27 | `t_kem_subtarget` | 事件目标-子表 | 12 | [kem_subscribe.md](./kem_subscribe.md) |
| 28 | `t_kem_subtarget` | 事件目标-子表 | 12 | [kem_subscribe_inh.md](./kem_subscribe_inh.md) |
