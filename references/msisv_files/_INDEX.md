# msisv 模块表清单

> 本模块共收录 **17** 张表定义，来自 `msisv_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope msisv
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_msisv_actionentry` | 监听行为-子表 | 11 | [msisv_ecologicmonitor.md](./msisv_ecologicmonitor.md) |
| 2 | `t_msisv_ecologicmonitor` | 生态接入监听-主表 | 21 | [msisv_ecologicmonitor.md](./msisv_ecologicmonitor.md) |
| 3 | `t_msisv_ecologicmonitor_l` | 生态接入监听-多语言表 | 5 | [msisv_ecologicmonitor.md](./msisv_ecologicmonitor.md) |
| 4 | `t_msisv_monitorlog` | 监听日志-主表 | 19 | [msisv_monitorlog.md](./msisv_monitorlog.md) |
| 5 | `t_msisv_monitorlog_l` | 监听日志-多语言表 | 5 | [msisv_monitorlog.md](./msisv_monitorlog.md) |
| 6 | `t_msisv_monitortype` | 生态接入监听分类-主表 | 15 | [msisv_monitortype.md](./msisv_monitortype.md) |
| 7 | `t_msisv_monitortype_l` | 生态接入监听分类-多语言表 | 5 | [msisv_monitortype.md](./msisv_monitortype.md) |
| 8 | `t_msisv_puassignentry` | 对目标单据赋值-子表 | 9 | [msisv_unionpush.md](./msisv_unionpush.md) |
| 9 | `t_msisv_pumatchentry` | 与来源单据的匹配关系-子表 | 7 | [msisv_unionpush.md](./msisv_unionpush.md) |
| 10 | `t_msisv_puoperateentry` | 下推后执行目标单的操作-子表 | 4 | [msisv_unionpush.md](./msisv_unionpush.md) |
| 11 | `t_msisv_relateupdate` | 关联更新-主表 | 29 | [msisv_relateupdate.md](./msisv_relateupdate.md) |
| 12 | `t_msisv_relateupdate_l` | 关联更新-多语言表 | 4 | [msisv_relateupdate.md](./msisv_relateupdate.md) |
| 13 | `t_msisv_unionpush` | 联合下推-主表 | 34 | [msisv_unionpush.md](./msisv_unionpush.md) |
| 14 | `t_msisv_unionpush_l` | 联合下推-多语言表 | 4 | [msisv_unionpush.md](./msisv_unionpush.md) |
| 15 | `t_msisv_upassignentry` | 对目标单据赋值-子表 | 9 | [msisv_relateupdate.md](./msisv_relateupdate.md) |
| 16 | `t_msisv_upmatchentry` | 与目标单据的匹配关系-子表 | 7 | [msisv_relateupdate.md](./msisv_relateupdate.md) |
| 17 | `t_msisv_upoperateentry` | 更新目标单后执行的操作-子表 | 9 | [msisv_relateupdate.md](./msisv_relateupdate.md) |
