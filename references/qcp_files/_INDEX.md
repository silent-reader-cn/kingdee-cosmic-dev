# qcp 模块表清单

> 本模块共收录 **70** 张表定义，来自 `qcp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope qcp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_qcp_applypromatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 2 | `t_qcp_baddeal_lk` | 关联子实体-子表 | 6 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 3 | `t_qcp_baddeal_tc` | 来料不良品处理单-关联追踪表 | 7 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 4 | `t_qcp_baddeal_wb` | 来料不良品处理单-反写记录表 | 10 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 5 | `t_qcp_baddealent_lk` | 关联子实体-子表 | 6 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 6 | `t_qcp_baddealn` | 来料不良品处理单-主表 | 19 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 7 | `t_qcp_baddealn_l` | 来料不良品处理单-多语言表 | 4 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 8 | `t_qcp_baddealnentry` | 不良处理信息-子表 | 82 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 9 | `t_qcp_baddealnentry_a` | 不良处理信息-分表 | 6 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 10 | `t_qcp_badserialnumber` | 序列号分录-子表 | 10 | [qcp_baddeal.md](./qcp_baddeal.md) |
| 11 | `t_qcp_insappnentry` | 物料信息-子表 | 54 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 12 | `t_qcp_inspapplyproj` | 检验项目-子表 | 23 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 13 | `t_qcp_inspapplyproj_lk` | 关联子实体-子表 | 6 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 14 | `t_qcp_inspbill` | 来料检验单-主表 | 20 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 15 | `t_qcp_inspbill_l` | 来料检验单-多语言表 | 4 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 16 | `t_qcp_inspctdef` | 缺陷记录-子表 | 10 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 17 | `t_qcp_inspctdef_l` | 缺陷记录-多语言表 | 4 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 18 | `t_qcp_inspctdefsn` | 序列号-多选基础资料表 | 3 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 19 | `t_qcp_inspecapply_lk` | 关联子实体-子表 | 6 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 20 | `t_qcp_inspecapply_tc` | 来料检验申请单-关联追踪表 | 7 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 21 | `t_qcp_inspecapply_wb` | 来料检验申请单-反写记录表 | 10 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 22 | `t_qcp_inspecapplyentry_lk` | 关联子实体-子表 | 6 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 23 | `t_qcp_inspecapplyn` | 来料检验申请单-主表 | 21 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 24 | `t_qcp_inspecapplyn_l` | 来料检验申请单-多语言表 | 4 | [qcp_inspecapply.md](./qcp_inspecapply.md) |
| 25 | `t_qcp_inspecbill_lk` | 关联子实体-子表 | 6 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 26 | `t_qcp_inspecbill_tc` | 来料检验单-关联追踪表 | 7 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 27 | `t_qcp_inspecbill_wb` | 来料检验单-反写记录表 | 10 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 28 | `t_qcp_inspentry` | 物料信息-子表 | 99 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 29 | `t_qcp_inspentry_a` | 物料信息-分表 | 7 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 30 | `t_qcp_inspentry_l` | 物料信息-多语言表 | 4 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 31 | `t_qcp_inspresult` | 来料检验结果-主表 | 33 | [qcp_inspresult.md](./qcp_inspresult.md) |
| 32 | `t_qcp_inspresult_lk` | 关联子实体-子表 | 6 | [qcp_inspresult.md](./qcp_inspresult.md) |
| 33 | `t_qcp_inspresult_tc` | 来料检验结果-关联追踪表 | 7 | [qcp_inspresult.md](./qcp_inspresult.md) |
| 34 | `t_qcp_inspresult_wb` | 来料检验结果-反写记录表 | 10 | [qcp_inspresult.md](./qcp_inspresult.md) |
| 35 | `t_qcp_inspsubbaddeal` | 不良处理信息-子表 | 40 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 36 | `t_qcp_inspsubbaddeal_l` | 不良处理信息-多语言表 | 4 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 37 | `t_qcp_inspsubresproj` | 检验明细-子表 | 41 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 38 | `t_qcp_inspsubresproj_l` | 检验明细-多语言表 | 4 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 39 | `t_qcp_inspsubresrela` | 样本检验结果_项目样本关系-子表 | 10 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 40 | `t_qcp_inspsubressamp` | 检验结果_样本-子表 | 7 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 41 | `t_qcp_joininspect` | 来料联合检验单-主表 | 14 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 42 | `t_qcp_joininspect_lk` | 关联子实体-子表 | 6 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 43 | `t_qcp_joininspect_tc` | 来料联合检验单-关联追踪表 | 7 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 44 | `t_qcp_joininspect_wb` | 来料联合检验单-反写记录表 | 10 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 45 | `t_qcp_joininspentry` | 物料信息-子表 | 34 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 46 | `t_qcp_joininspentry_lk` | 关联子实体-子表 | 6 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 47 | `t_qcp_joininspproj` | 检验信息-子表 | 33 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 48 | `t_qcp_joininspproj_lk` | 关联子实体-子表 | 6 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 49 | `t_qcp_joininsprela_n` | 项目样本关系-子表 | 10 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 50 | `t_qcp_joininspsamp_n` | 检验样本-子表 | 7 | [qcp_joininspect.md](./qcp_joininspect.md) |
| 51 | `t_qcp_matintoentity_lk` | 关联子实体-子表 | 10 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 52 | `t_qcp_mrb` | 来料MRB评审单-主表 | 43 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 53 | `t_qcp_mrb_l` | 来料MRB评审单-多语言表 | 5 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 54 | `t_qcp_mrb_s` | 来料MRB评审单-分表 | 17 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 55 | `t_qcp_mrb_tc` | 来料MRB评审单-关联追踪表 | 7 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 56 | `t_qcp_mrb_wb` | 来料MRB评审单-反写记录表 | 10 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 57 | `t_qcp_mrbentry` | 评审明细-子表 | 31 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 58 | `t_qcp_mrbentry_lk` | 关联子实体-子表 | 8 | [qcp_mrbbill.md](./qcp_mrbbill.md) |
| 59 | `t_qcp_promatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 60 | `t_qcp_resultentry` | 分批信息-单据体-子表 | 25 | [qcp_inspresult.md](./qcp_inspresult.md) |
| 61 | `t_qcp_resultentry_lk` | 关联子实体-子表 | 6 | [qcp_inspresult.md](./qcp_inspresult.md) |
| 62 | `t_qcp_samplecheck` | 样本检测-无检验项目时显示-子表 | 8 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 63 | `t_qcp_samplecheck_l` | 样本检测-无检验项目时显示-多语言表 | 4 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 64 | `t_qcp_serialnumber` | 序列号分录-子表 | 10 | [qcp_incominginspct.md](./qcp_incominginspct.md) |
| 65 | `t_qcp_ycbill_bad` | 单据体-子表 | 33 | [qcp_yieldreceivebill.md](./qcp_yieldreceivebill.md) |
| 66 | `t_qcp_ycbill_bad_lk` | 关联子实体-子表 | 8 | [qcp_yieldreceivebill.md](./qcp_yieldreceivebill.md) |
| 67 | `t_qcp_yieldrecbill` | 来料让步接收申请单-主表 | 16 | [qcp_yieldreceivebill.md](./qcp_yieldreceivebill.md) |
| 68 | `t_qcp_yieldrecbill_l` | 来料让步接收申请单-多语言表 | 4 | [qcp_yieldreceivebill.md](./qcp_yieldreceivebill.md) |
| 69 | `t_qcp_yieldrecbill_tc` | 来料让步接收申请单-关联追踪表 | 7 | [qcp_yieldreceivebill.md](./qcp_yieldreceivebill.md) |
| 70 | `t_qcp_yieldrecbill_wb` | 来料让步接收申请单-反写记录表 | 10 | [qcp_yieldreceivebill.md](./qcp_yieldreceivebill.md) |
