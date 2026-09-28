# fircm 模块表清单

> 本模块共收录 **41** 张表定义，来自 `fircm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fircm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fircm_creditappeal` | 信用申诉单-主表 | 16 | [fircm_creditappeal.md](./fircm_creditappeal.md) |
| 2 | `t_fircm_creditappeal_l` | 信用申诉单-多语言表 | 4 | [fircm_creditappeal.md](./fircm_creditappeal.md) |
| 3 | `t_fircm_creditarg` | 信用参数-主表 | 10 | [fircm_creditarg.md](./fircm_creditarg.md) |
| 4 | `t_fircm_creditarg_l` | 信用参数-多语言表 | 5 | [fircm_creditarg.md](./fircm_creditarg.md) |
| 5 | `t_fircm_creditsetting` | 我的信用页面设置-主表 | 17 | [fircm_creditsetting.md](./fircm_creditsetting.md) |
| 6 | `t_fircm_creditsetting_l` | 我的信用页面设置-多语言表 | 5 | [fircm_creditsetting.md](./fircm_creditsetting.md) |
| 7 | `t_fircm_creditsetting_m` | 我的信用页面设置-使用范围位图表 | 2 | [fircm_creditsetting.md](./fircm_creditsetting.md) |
| 8 | `t_fircm_creditsetting_u` | 我的信用页面设置-使用范围表 | 3 | [fircm_creditsetting.md](./fircm_creditsetting.md) |
| 9 | `t_fircm_equitysetting` | 单据体-子表 | 5 | [my_creditsetting.md](./my_creditsetting.md) |
| 10 | `t_fircm_equitysetting_l` | 单据体-多语言表 | 4 | [my_creditsetting.md](./my_creditsetting.md) |
| 11 | `t_fircm_mycreditsetting` | 我的信用配置-主表 | 19 | [my_creditsetting.md](./my_creditsetting.md) |
| 12 | `t_fircm_mycreditsetting_l` | 我的信用配置-多语言表 | 5 | [my_creditsetting.md](./my_creditsetting.md) |
| 13 | `t_fircm_mycreditsetting_m` | 我的信用配置-使用范围位图表 | 2 | [my_creditsetting.md](./my_creditsetting.md) |
| 14 | `t_fircm_mycreditsetting_u` | 我的信用配置-使用范围表 | 3 | [my_creditsetting.md](./my_creditsetting.md) |
| 15 | `t_fircm_rightssetting` | 单据体-子表 | 4 | [fircm_creditsetting.md](./fircm_creditsetting.md) |
| 16 | `t_fircm_rightssetting_l` | 单据体-多语言表 | 4 | [fircm_creditsetting.md](./fircm_creditsetting.md) |
| 17 | `t_fircm_subscorerule` | 审核扣分规则-主表 | 18 | [fircm_subscorerule.md](./fircm_subscorerule.md) |
| 18 | `t_fircm_subscorerule_l` | 审核扣分规则-多语言表 | 5 | [fircm_subscorerule.md](./fircm_subscorerule.md) |
| 19 | `t_fircm_subscorerulebill` | 关联单据查询-主表 | 12 | [fircm_subscoredisquery.md](./fircm_subscoredisquery.md) |
| 20 | `t_fircm_subscorerulebill_l` | 关联单据查询-多语言表 | 4 | [fircm_subscoredisquery.md](./fircm_subscoredisquery.md) |
| 21 | `t_fircm_subscorerulegroup` | 审核扣分规则分组-主表 | 17 | [fircm_subscorerulegroup.md](./fircm_subscorerulegroup.md) |
| 22 | `t_fircm_subscorerulegroup_l` | 审核扣分规则分组-多语言表 | 6 | [fircm_subscorerulegroup.md](./fircm_subscorerulegroup.md) |
| 23 | `t_tk_crebreakrulerecord` | 信用--任务审批违规记录-主表 | 4 | [task_crebreakrulerecord.md](./task_crebreakrulerecord.md) |
| 24 | `t_tk_creditbyimage` | 减分规则--影像超期-主表 | 18 | [task_creditbyimagenew.md](./task_creditbyimagenew.md) |
| 25 | `t_tk_creditbyimage_l` | 减分规则--影像超期-多语言表 | 4 | [task_creditbyimagenew.md](./task_creditbyimagenew.md) |
| 26 | `t_tk_creditbyimage_m` | 减分规则--影像超期-使用范围位图表 | 2 | [task_creditbyimagenew.md](./task_creditbyimagenew.md) |
| 27 | `t_tk_creditbyimage_u` | 减分规则--影像超期-使用范围表 | 3 | [task_creditbyimagenew.md](./task_creditbyimagenew.md) |
| 28 | `t_tk_creditcommrule` | 通用加分规则-主表 | 23 | [task_credit_commonrule.md](./task_credit_commonrule.md) |
| 29 | `t_tk_creditcommrule_l` | 通用加分规则-多语言表 | 6 | [task_credit_commonrule.md](./task_credit_commonrule.md) |
| 30 | `t_tk_creditcommrule_m` | 通用加分规则-使用范围位图表 | 2 | [task_credit_commonrule.md](./task_credit_commonrule.md) |
| 31 | `t_tk_creditcommrule_u` | 通用加分规则-使用范围表 | 3 | [task_credit_commonrule.md](./task_credit_commonrule.md) |
| 32 | `t_tk_creditfiles` | 信用档案-主表 | 24 | [task_creditfiles.md](./task_creditfiles.md) |
| 33 | `t_tk_creditfiles_l` | 信用档案-多语言表 | 5 | [task_creditfiles.md](./task_creditfiles.md) |
| 34 | `t_tk_creditlevel` | 信用等级-主表 | 19 | [task_creditlevel.md](./task_creditlevel.md) |
| 35 | `t_tk_creditlevel_l` | 信用等级-多语言表 | 5 | [task_creditlevel.md](./task_creditlevel.md) |
| 36 | `t_tk_creditmodifylog` | 信用变更日志-主表 | 34 | [task_creditmodifylog.md](./task_creditmodifylog.md) |
| 37 | `t_tk_creditmodifylog_l` | 信用变更日志-多语言表 | 4 | [task_creditmodifylog.md](./task_creditmodifylog.md) |
| 38 | `t_tk_creditscorelimit` | 每单加减分限制-主表 | 18 | [task_creditscorelimit.md](./task_creditscorelimit.md) |
| 39 | `t_tk_creditscorelimit_l` | 每单加减分限制-多语言表 | 4 | [task_creditscorelimit.md](./task_creditscorelimit.md) |
| 40 | `t_tk_creditscorelimit_m` | 每单加减分限制-使用范围位图表 | 2 | [task_creditscorelimit.md](./task_creditscorelimit.md) |
| 41 | `t_tk_creditscorelimit_u` | 每单加减分限制-使用范围表 | 3 | [task_creditscorelimit.md](./task_creditscorelimit.md) |
