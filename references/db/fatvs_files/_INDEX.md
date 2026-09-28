# fatvs 模块表清单

> 本模块共收录 **27** 张表定义，来自 `fatvs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fatvs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fatvs_alarmmessage` | 告警信息-主表 | 7 | [fatvs_alarmmessage.md](./fatvs_alarmmessage.md) |
| 2 | `t_fatvs_employee` | 形象库-主表 | 25 | [fatvs_employee.md](./fatvs_employee.md) |
| 3 | `t_fatvs_employee_l` | 形象库-多语言表 | 5 | [fatvs_employee.md](./fatvs_employee.md) |
| 4 | `t_fatvs_office` | 办公室-主表 | 12 | [fatvs_office.md](./fatvs_office.md) |
| 5 | `t_fatvs_office_l` | 办公室-多语言表 | 4 | [fatvs_office.md](./fatvs_office.md) |
| 6 | `t_fatvs_pos_refskill` | 关联技能-多选基础资料表 | 3 | [fatvs_position.md](./fatvs_position.md) |
| 7 | `t_fatvs_position` | 虚拟职位-主表 | 12 | [fatvs_position.md](./fatvs_position.md) |
| 8 | `t_fatvs_position_l` | 虚拟职位-多语言表 | 4 | [fatvs_position.md](./fatvs_position.md) |
| 9 | `t_fatvs_runtimedataentry` | 运行数据-子表 | 5 | [fatvs_skill_runtimedata.md](./fatvs_skill_runtimedata.md) |
| 10 | `t_fatvs_skill` | 技能-主表 | 26 | [fatvs_skill.md](./fatvs_skill.md) |
| 11 | `t_fatvs_skill_l` | 技能-多语言表 | 6 | [fatvs_skill.md](./fatvs_skill.md) |
| 12 | `t_fatvs_skill_relatedflag` | 技能标签-多选基础资料表 | 3 | [fatvs_skill.md](./fatvs_skill.md) |
| 13 | `t_fatvs_skillflag` | 技能标签-主表 | 10 | [fatvs_skillflag.md](./fatvs_skillflag.md) |
| 14 | `t_fatvs_skillflag_l` | 技能标签-多语言表 | 4 | [fatvs_skillflag.md](./fatvs_skillflag.md) |
| 15 | `t_fatvs_skillindex` | 技能指标-主表 | 12 | [fatvs_skill_index.md](./fatvs_skill_index.md) |
| 16 | `t_fatvs_skillindex_l` | 技能指标-多语言表 | 4 | [fatvs_skill_index.md](./fatvs_skill_index.md) |
| 17 | `t_fatvs_skilllatestime` | 技能取数最新时间记录-主表 | 12 | [fatvs_skillruntimeflag.md](./fatvs_skillruntimeflag.md) |
| 18 | `t_fatvs_skilllatestime_l` | 技能取数最新时间记录-多语言表 | 4 | [fatvs_skillruntimeflag.md](./fatvs_skillruntimeflag.md) |
| 19 | `t_fatvs_skillruntimedata` | 技能运行数据-主表 | 23 | [fatvs_skill_runtimedata.md](./fatvs_skill_runtimedata.md) |
| 20 | `t_fatvs_skillruntimedata_l` | 技能运行数据-多语言表 | 4 | [fatvs_skill_runtimedata.md](./fatvs_skill_runtimedata.md) |
| 21 | `t_fatvs_userinformstatus` | 用户消息通知接收状态-主表 | 4 | [fatvs_userinformstatus.md](./fatvs_userinformstatus.md) |
| 22 | `t_fatvs_warndetail` | 技能预警详情-主表 | 21 | [fatvs_warndetail.md](./fatvs_warndetail.md) |
| 23 | `t_fatvs_warndetail_l` | 技能预警详情-多语言表 | 6 | [fatvs_warndetail.md](./fatvs_warndetail.md) |
| 24 | `t_fatvs_warnuserentry` | 用户信息-子表 | 5 | [fatvs_warnusergroup.md](./fatvs_warnusergroup.md) |
| 25 | `t_fatvs_warnusergroup` | 预警用户组-主表 | 10 | [fatvs_warnusergroup.md](./fatvs_warnusergroup.md) |
| 26 | `t_fatvs_warnusergroup_l` | 预警用户组-多语言表 | 4 | [fatvs_warnusergroup.md](./fatvs_warnusergroup.md) |
| 27 | `t_fatvs_warnusers` | 预警用户组-多选基础资料表 | 3 | [fatvs_warndetail.md](./fatvs_warndetail.md) |
