# mbase 模块表清单

> 本模块共收录 **42** 张表定义，来自 `mbase_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category mbase
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mbase_bcfgadvfentry` | 高级过滤单据体-子表 | 9 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 2 | `t_mbase_bcfgadvfentry_l` | 高级过滤单据体-多语言表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 3 | `t_mbase_bcfgbtentry` | 单据类型多模板单据体-子表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 4 | `t_mbase_bcfgbtnentry` | 单据体-子表 | 6 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 5 | `t_mbase_bcfgbtnentry_l` | 单据体-多语言表 | 4 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 6 | `t_mbase_bcfgfieldentry` | 单据体-子表 | 8 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 7 | `t_mbase_bcfgfieldentry_l` | 单据体-多语言表 | 4 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 8 | `t_mbase_bcfgpicentry` | 单据体-子表 | 6 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 9 | `t_mbase_bcfgpicentry_l` | 单据体-多语言表 | 4 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 10 | `t_mbase_billcfg` | 业务审批显示设置-主表 | 30 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 11 | `t_mbase_billcfg_l` | 业务审批显示设置-多语言表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 12 | `t_mbase_billcfgabentry` | 基本信息单据体-子表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 13 | `t_mbase_billcfgabentry_l` | 基本信息单据体-多语言表 | 4 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 14 | `t_mbase_billcfgapentry` | 关键要素单据体-子表 | 6 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 15 | `t_mbase_billcfgapentry_l` | 关键要素单据体-多语言表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 16 | `t_mbase_billcfgentry` | 单据体-子表 | 20 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 17 | `t_mbase_billcfgentry_l` | 单据体-多语言表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 18 | `t_mbase_billcfgextentry` | 单据体1-子表 | 8 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 19 | `t_mbase_billcfgextentry_l` | 单据体1-多语言表 | 5 | [mbase_billcfg.md](./mbase_billcfg.md) |
| 20 | `t_mbase_bzjclog` | 标准集成消息日志-主表 | 19 | [mbase_bzjclog.md](./mbase_bzjclog.md) |
| 21 | `t_mbase_bzjclogentry` | 单据体-子表 | 11 | [mbase_bzjclog.md](./mbase_bzjclog.md) |
| 22 | `t_mbase_bzjclogretryentry` | 重发单据体-子表 | 12 | [mbase_bzjclog.md](./mbase_bzjclog.md) |
| 23 | `t_mbase_ctrltest` | 控件示例_来源单据-主表 | 11 | [mbase_ctrlsrcbill_test.md](./mbase_ctrlsrcbill_test.md) |
| 24 | `t_mbase_ctrltestentry` | 单据体-子表 | 10 | [mbase_ctrlsrcbill_test.md](./mbase_ctrlsrcbill_test.md) |
| 25 | `t_mbase_ctrltestsubentry` | 子单据体-子表 | 11 | [mbase_ctrlsrcbill_test.md](./mbase_ctrlsrcbill_test.md) |
| 26 | `t_mbase_interfaceconfig` | 业务接口配置-主表 | 12 | [mbase_interfaceconfig.md](./mbase_interfaceconfig.md) |
| 27 | `t_mbase_lightapp` | 轻应用-主表 | 15 | [mbase_lightapp.md](./mbase_lightapp.md) |
| 28 | `t_mbase_lightapp_l` | 轻应用-多语言表 | 4 | [mbase_lightapp.md](./mbase_lightapp.md) |
| 29 | `t_mbase_miniapp` | 微信小程序集成-主表 | 14 | [mbase_miniapp.md](./mbase_miniapp.md) |
| 30 | `t_mbase_miniapp_l` | 微信小程序集成-多语言表 | 4 | [mbase_miniapp.md](./mbase_miniapp.md) |
| 31 | `t_mbase_mobentity` | 移动实体-主表 | 20 | [mbase_mobentity.md](./mbase_mobentity.md) |
| 32 | `t_mbase_mobentity_l` | 移动实体-多语言表 | 7 | [mbase_mobentity.md](./mbase_mobentity.md) |
| 33 | `t_mbase_mobentityuser` | 可见用户-子表 | 4 | [mbase_mobentity.md](./mbase_mobentity.md) |
| 34 | `t_mbase_mobentityusrgrp` | 可见用户组-子表 | 4 | [mbase_mobentity.md](./mbase_mobentity.md) |
| 35 | `t_mbase_msgbot` | 群消息机器人-主表 | 13 | [mbase_msgbot.md](./mbase_msgbot.md) |
| 36 | `t_mbase_msgbotbasedata` | 群组消息机器人-多选基础资料表 | 3 | [mbase_msgtask.md](./mbase_msgtask.md) |
| 37 | `t_mbase_msgbotbaseuser` | 消息接收人-多选基础资料表 | 3 | [mbase_msgtask.md](./mbase_msgtask.md) |
| 38 | `t_mbase_msgbotlog` | 群消息日志-主表 | 13 | [mbase_msgbotlog.md](./mbase_msgbotlog.md) |
| 39 | `t_mbase_msgtask` | 定时消息任务-主表 | 27 | [mbase_msgtask.md](./mbase_msgtask.md) |
| 40 | `t_mbase_msgtasklogdetail` | 执行计划日志详情-主表 | 9 | [mbase_msgtasklogdetail.md](./mbase_msgtasklogdetail.md) |
| 41 | `t_mbase_userconfig` | 用户设置-主表 | 10 | [mbase_userconfig.md](./mbase_userconfig.md) |
| 42 | `t_mbase_userconfig_l` | 用户设置-多语言表 | 4 | [mbase_userconfig.md](./mbase_userconfig.md) |
