# wftask 模块表清单

> 本模块共收录 **62** 张表定义，来自 `wftask_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category wftask
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_msg_archive` | 归档服务-主表 | 27 | [wf_archiveservice.md](./wf_archiveservice.md) |
| 2 | `t_msg_archive_l` | 归档服务-多语言表 | 5 | [wf_archiveservice.md](./wf_archiveservice.md) |
| 3 | `t_msg_archivedetail` | 归档数据详情-子表 | 8 | [wf_archiveservice.md](./wf_archiveservice.md) |
| 4 | `t_msg_archivedetail_l` | 归档数据详情-多语言表 | 4 | [wf_archiveservice.md](./wf_archiveservice.md) |
| 5 | `t_msg_archivelog` | 归档调度日志-主表 | 14 | [wf_archivelog.md](./wf_archivelog.md) |
| 6 | `t_msg_channel` | 消息渠道-主表 | 31 | [msg_channel.md](./msg_channel.md) |
| 7 | `t_msg_channel_l` | 消息渠道-多语言表 | 5 | [msg_channel.md](./msg_channel.md) |
| 8 | `t_msg_event` | 事件模型-主表 | 0 | [msg_event.md](./msg_event.md) |
| 9 | `t_msg_event_l` | 事件模型-多语言表 | 0 | [msg_event.md](./msg_event.md) |
| 10 | `t_msg_eventlisteners` | 消息监听事件-主表 | 10 | [msg_eventlisteners.md](./msg_eventlisteners.md) |
| 11 | `t_msg_eventlisteners_l` | 消息监听事件-多语言表 | 5 | [msg_eventlisteners.md](./msg_eventlisteners.md) |
| 12 | `t_msg_eventlog` | 事件订阅日志-主表 | 0 | [msg_eventlog.md](./msg_eventlog.md) |
| 13 | `t_msg_eventlog_l` | 事件订阅日志-多语言表 | 0 | [msg_eventlog.md](./msg_eventlog.md) |
| 14 | `t_msg_pubacc` | 公共号-主表 | 6 | [msg_pubacc.md](./msg_pubacc.md) |
| 15 | `t_msg_pubacc_l` | 公共号-多语言表 | 5 | [msg_pubacc.md](./msg_pubacc.md) |
| 16 | `t_msg_quantitysum` | 消息数量统计-主表 | 6 | [msg_quantitysum.md](./msg_quantitysum.md) |
| 17 | `t_msg_selectscene` | 适用场景-多选基础资料表 | 3 | [msg_template.md](./msg_template.md) |
| 18 | `t_msg_srvcfg` | 消息服务配置-主表 | 13 | [msg_srvcfg.md](./msg_srvcfg.md) |
| 19 | `t_msg_srvcfg_l` | 消息服务配置-多语言表 | 4 | [msg_srvcfg.md](./msg_srvcfg.md) |
| 20 | `t_msg_template` | 消息模板-主表 | 13 | [msg_template.md](./msg_template.md) |
| 21 | `t_msg_template_l` | 消息模板-多语言表 | 6 | [msg_template.md](./msg_template.md) |
| 22 | `t_msg_tplscene` | 消息场景-主表 | 7 | [msg_tplscene.md](./msg_tplscene.md) |
| 23 | `t_msg_tplscene_l` | 消息场景-多语言表 | 4 | [msg_tplscene.md](./msg_tplscene.md) |
| 24 | `t_msg_type` | 消息类型-主表 | 10 | [msg_type.md](./msg_type.md) |
| 25 | `t_msg_type_l` | 消息类型-多语言表 | 6 | [msg_type.md](./msg_type.md) |
| 26 | `t_msg_usercorrectlog` | 用户登录校正日志-主表 | 5 | [msg_usercorrectlog.md](./msg_usercorrectlog.md) |
| 27 | `t_msg_welinktodo` | welink待办-主表 | 14 | [msg_welinktodo.md](./msg_welinktodo.md) |
| 28 | `t_msg_yzjtpl` | 云之家模板-主表 | 6 | [msg_yzjtpl.md](./msg_yzjtpl.md) |
| 29 | `t_msg_yzjtpl_l` | 云之家模板-多语言表 | 4 | [msg_yzjtpl.md](./msg_yzjtpl.md) |
| 30 | `t_wf_concurrentdata` | 并发数据池-主表 | 8 | [wf_concurrentdata.md](./wf_concurrentdata.md) |
| 31 | `t_wf_dingtodo` | 钉钉待办-主表 | 15 | [wf_msg_dingtodo.md](./wf_msg_dingtodo.md) |
| 32 | `t_wf_dingtpl` | 钉钉模板-主表 | 8 | [wf_msg_dingtpl.md](./wf_msg_dingtpl.md) |
| 33 | `t_wf_dingtpl_l` | 钉钉模板-多语言表 | 6 | [wf_msg_dingtpl.md](./wf_msg_dingtpl.md) |
| 34 | `t_wf_himessage` | 历史消息-主表 | 30 | [wf_msg_himessage.md](./wf_msg_himessage.md) |
| 35 | `t_wf_himessage_l` | 历史消息-多语言表 | 9 | [wf_msg_himessage.md](./wf_msg_himessage.md) |
| 36 | `t_wf_himsgfail` | 历史消息日志-主表 | 23 | [wf_msg_hifailmessage.md](./wf_msg_hifailmessage.md) |
| 37 | `t_wf_himsgfail_l` | 历史消息日志-多语言表 | 8 | [wf_msg_hifailmessage.md](./wf_msg_hifailmessage.md) |
| 38 | `t_wf_himsgreceiver` | 历史消息接受者-主表 | 29 | [wf_msg_hireceiver.md](./wf_msg_hireceiver.md) |
| 39 | `t_wf_himsgreceiver_l` | 历史消息接受者-多语言表 | 7 | [wf_msg_hireceiver.md](./wf_msg_hireceiver.md) |
| 40 | `t_wf_hitaskjob` | 历史渠道待办日志-主表 | 45 | [wf_hitaskjob.md](./wf_hitaskjob.md) |
| 41 | `t_wf_hitaskjob_l` | 历史渠道待办日志-多语言表 | 7 | [wf_hitaskjob.md](./wf_hitaskjob.md) |
| 42 | `t_wf_hitaskjobretrylog` | 历史渠道待办重试日志-主表 | 7 | [wf_hitaskjobretrylog.md](./wf_hitaskjobretrylog.md) |
| 43 | `t_wf_hitaskjobretrylog_l` | 历史渠道待办重试日志-多语言表 | 4 | [wf_hitaskjobretrylog.md](./wf_hitaskjobretrylog.md) |
| 44 | `t_wf_message` | 消息模型-主表 | 28 | [wf_msg_message.md](./wf_msg_message.md) |
| 45 | `t_wf_message_l` | 消息模型-多语言表 | 9 | [wf_msg_message.md](./wf_msg_message.md) |
| 46 | `t_wf_msgfail` | 消息日志-主表 | 21 | [wf_msg_failmessage.md](./wf_msg_failmessage.md) |
| 47 | `t_wf_msgfail_l` | 消息日志-多语言表 | 8 | [wf_msg_failmessage.md](./wf_msg_failmessage.md) |
| 48 | `t_wf_msgreceiver` | 消息接收者-主表 | 27 | [wf_msg_receiver.md](./wf_msg_receiver.md) |
| 49 | `t_wf_msgreceiver_l` | 消息接收者-多语言表 | 7 | [wf_msg_receiver.md](./wf_msg_receiver.md) |
| 50 | `t_wf_nocode_taskjob` | 无代码渠道待办日志-主表 | 44 | [wf_nocode_taskjob.md](./wf_nocode_taskjob.md) |
| 51 | `t_wf_nocode_taskjob_l` | 无代码渠道待办日志-多语言表 | 7 | [wf_nocode_taskjob.md](./wf_nocode_taskjob.md) |
| 52 | `t_wf_relatetaskid` | 第三方关联任务ID-主表 | 5 | [wf_msg_relatetask.md](./wf_msg_relatetask.md) |
| 53 | `t_wf_smsinfo` | 短信id记录-主表 | 13 | [wf_smsinfo.md](./wf_smsinfo.md) |
| 54 | `t_wf_smsinfo_l` | 短信id记录-多语言表 | 5 | [wf_smsinfo.md](./wf_smsinfo.md) |
| 55 | `t_wf_smsusingquantity` | 短信使用数量-主表 | 3 | [wf_smsusingquantity.md](./wf_smsusingquantity.md) |
| 56 | `t_wf_taskjob` | 渠道待办日志-主表 | 44 | [wf_taskjob.md](./wf_taskjob.md) |
| 57 | `t_wf_taskjob_l` | 渠道待办日志-多语言表 | 7 | [wf_taskjob.md](./wf_taskjob.md) |
| 58 | `t_wf_taskjobretrylog` | 渠道待办重试日志-主表 | 6 | [wf_taskjobretrylog.md](./wf_taskjobretrylog.md) |
| 59 | `t_wf_taskjobretrylog_l` | 渠道待办重试日志-多语言表 | 4 | [wf_taskjobretrylog.md](./wf_taskjobretrylog.md) |
| 60 | `t_wf_yzjtodo` | 云之家待办-主表 | 20 | [msg_yzjtodo.md](./msg_yzjtodo.md) |
| 61 | `t_wf_yzjtodo_l` | 云之家待办-多语言表 | 4 | [msg_yzjtodo.md](./msg_yzjtodo.md) |
| 62 | `t_wftask_eiduser` | 单租户配置信息-主表 | 6 | [wf_mobile_usereid.md](./wf_mobile_usereid.md) |
