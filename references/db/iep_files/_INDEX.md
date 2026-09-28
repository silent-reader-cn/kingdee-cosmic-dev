# iep 模块表清单

> 本模块共收录 **18** 张表定义，来自 `iep_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category iep
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gl_businesstask` | 智能核算业务单据任务-主表 | 4 | [iep_businesstask.md](./iep_businesstask.md) |
| 2 | `t_gl_filingdata` | 凭证归档数据-主表 | 10 | [gl_filingdata.md](./gl_filingdata.md) |
| 3 | `t_gl_intellaccountschema` | 智能执行方案-主表 | 22 | [gl_intellexecschema.md](./gl_intellexecschema.md) |
| 4 | `t_gl_intellaccountschema_l` | 智能执行方案-多语言表 | 5 | [gl_intellexecschema.md](./gl_intellexecschema.md) |
| 5 | `t_gl_intellexecoperentry` | 操作单据体-子表 | 15 | [gl_intellexecschema.md](./gl_intellexecschema.md) |
| 6 | `t_gl_intellexecorgentry` | 组织单据体-子表 | 4 | [gl_intellexecschema.md](./gl_intellexecschema.md) |
| 7 | `t_gl_intellexecparam` | 智能执行方案操作参数-主表 | 5 | [gl_intellexecparam.md](./gl_intellexecparam.md) |
| 8 | `t_gl_intellexecparam_l` | 智能执行方案操作参数-多语言表 | 5 | [gl_intellexecparam.md](./gl_intellexecparam.md) |
| 9 | `t_gl_intellexecparamentry` | 单据体-子表 | 7 | [gl_intellexecparam.md](./gl_intellexecparam.md) |
| 10 | `t_gl_intellexecparamentry_l` | 单据体-多语言表 | 6 | [gl_intellexecparam.md](./gl_intellexecparam.md) |
| 11 | `t_gl_intellnotifyusers` | 消息接收人-多选基础资料表 | 3 | [gl_intellexecschema.md](./gl_intellexecschema.md) |
| 12 | `t_gl_intelloper_filter` | 智能方案预置过滤-主表 | 7 | [gl_intelloper_filter.md](./gl_intelloper_filter.md) |
| 13 | `t_gl_intellopersumlog` | 智能核算操作汇总日志-主表 | 14 | [gl_intellopersumlog.md](./gl_intellopersumlog.md) |
| 14 | `t_gl_intellschemalog` | 智能方案详细日志-主表 | 21 | [gl_intellexecdetaillog.md](./gl_intellexecdetaillog.md) |
| 15 | `t_gl_intellschemasumlog` | 智能方案日志-主表 | 11 | [gl_intelschemasumlog.md](./gl_intelschemasumlog.md) |
| 16 | `t_gl_intellwhitelist` | 智能核算白名单-主表 | 2 | [gl_intellwhitelist.md](./gl_intellwhitelist.md) |
| 17 | `t_gl_intellwhitelistentry` | 单据体-子表 | 4 | [gl_intellwhitelist.md](./gl_intellwhitelist.md) |
| 18 | `t_gl_intellwhitelistsub` | 子单据体-子表 | 4 | [gl_intellwhitelist.md](./gl_intellwhitelist.md) |
