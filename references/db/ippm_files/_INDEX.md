# ippm 模块表清单

> 本模块共收录 **13** 张表定义，来自 `ippm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ippm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ippm_problem_knownuser` | 首页问题反馈与建议不提示人员-主表 | 4 | [ippm_problem_knownuser.md](./ippm_problem_knownuser.md) |
| 2 | `t_ippm_problemlist` | 问题列表-主表 | 26 | [ippm_problemlist.md](./ippm_problemlist.md) |
| 3 | `t_ippm_problemlist` | 反馈问题-主表 | 26 | [ippm_problemlist_home.md](./ippm_problemlist_home.md) |
| 4 | `t_ippm_problemlist` | 反馈建议-主表 | 26 | [ippm_suggest_home.md](./ippm_suggest_home.md) |
| 5 | `t_ippm_problemlist` | AI记账申请记录-主表 | 26 | [tc_aiaccapplyrecord.md](./tc_aiaccapplyrecord.md) |
| 6 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [ippm_problemlist.md](./ippm_problemlist.md) |
| 7 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [ippm_problemlist_home.md](./ippm_problemlist_home.md) |
| 8 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [ippm_suggest_home.md](./ippm_suggest_home.md) |
| 9 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [tc_aiaccapplyrecord.md](./tc_aiaccapplyrecord.md) |
| 10 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [ippm_problemlist.md](./ippm_problemlist.md) |
| 11 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [ippm_problemlist_home.md](./ippm_problemlist_home.md) |
| 12 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [ippm_suggest_home.md](./ippm_suggest_home.md) |
| 13 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [tc_aiaccapplyrecord.md](./tc_aiaccapplyrecord.md) |
