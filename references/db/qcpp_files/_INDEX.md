# qcpp 模块表清单

> 本模块共收录 **69** 张表定义，来自 `qcpp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category qcpp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_qcp_baddeal_lk` | 关联子实体-子表 | 6 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 2 | `t_qcp_baddeal_tc` | 生产不良品处理单-关联追踪表 | 7 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 3 | `t_qcp_baddeal_wb` | 生产不良品处理单-反写记录表 | 10 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 4 | `t_qcp_baddealent_lk` | 关联子实体-子表 | 6 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 5 | `t_qcp_inspecapply_lk` | 关联子实体-子表 | 6 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 6 | `t_qcp_inspecapply_tc` | 生产退料请检单-关联追踪表 | 7 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 7 | `t_qcp_inspecapply_wb` | 生产退料请检单-反写记录表 | 10 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 8 | `t_qcp_inspecapplyentry_lk` | 关联子实体-子表 | 6 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 9 | `t_qcp_joininspproj_lk` | 关联子实体-子表 | 6 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 10 | `t_qcpp_applypromatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 11 | `t_qcpp_baddeal` | 生产不良品处理单-主表 | 19 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 12 | `t_qcpp_baddeal_l` | 生产不良品处理单-多语言表 | 4 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 13 | `t_qcpp_baddealentry` | 不良处理信息-子表 | 89 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 14 | `t_qcpp_baddealentry_a` | 不良处理信息-分表 | 3 | [qcpp_manubaddeal.md](./qcpp_manubaddeal.md) |
| 15 | `t_qcpp_insappentry` | 物料信息-子表 | 65 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 16 | `t_qcpp_insappentry_q` | 物料信息-分表 | 16 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 17 | `t_qcpp_inspapplyproj` | 联合检验信息-子表 | 23 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 18 | `t_qcpp_inspapplyproj_lk` | 关联子实体-子表 | 6 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 19 | `t_qcpp_inspbill` | 生产检验单-主表 | 21 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 20 | `t_qcpp_inspbill_l` | 生产检验单-多语言表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 21 | `t_qcpp_inspbill_lk` | 关联子实体-子表 | 6 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 22 | `t_qcpp_inspctdef` | 缺陷记录-子表 | 10 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 23 | `t_qcpp_inspctdef_l` | 缺陷记录-多语言表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 24 | `t_qcpp_inspctdefsn` | 序列号-多选基础资料表 | 3 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 25 | `t_qcpp_inspecapply` | 生产退料请检单-主表 | 21 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 26 | `t_qcpp_inspecapply_l` | 生产退料请检单-多语言表 | 4 | [qcpp_manuinspecapply.md](./qcpp_manuinspecapply.md) |
| 27 | `t_qcpp_inspecbill_tc` | 生产检验单-关联追踪表 | 7 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 28 | `t_qcpp_inspecbill_wb` | 生产检验单-反写记录表 | 10 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 29 | `t_qcpp_inspentry` | 物料信息-子表 | 106 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 30 | `t_qcpp_inspentry_a` | 物料信息-分表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 31 | `t_qcpp_inspentry_l` | 物料信息-多语言表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 32 | `t_qcpp_inspentry_lk` | 关联子实体-子表 | 8 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 33 | `t_qcpp_inspresult` | 生产检验结果-主表 | 34 | [qcpp_inspresult.md](./qcpp_inspresult.md) |
| 34 | `t_qcpp_inspresult_lk` | 关联子实体-子表 | 6 | [qcpp_inspresult.md](./qcpp_inspresult.md) |
| 35 | `t_qcpp_inspresult_tc` | 生产检验结果-关联追踪表 | 7 | [qcpp_inspresult.md](./qcpp_inspresult.md) |
| 36 | `t_qcpp_inspresult_wb` | 生产检验结果-反写记录表 | 10 | [qcpp_inspresult.md](./qcpp_inspresult.md) |
| 37 | `t_qcpp_inspsubbaddeal` | 不良处理信息-子表 | 40 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 38 | `t_qcpp_inspsubbaddeal_l` | 不良处理信息-多语言表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 39 | `t_qcpp_inspsubresproj` | 检验明细-子表 | 41 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 40 | `t_qcpp_inspsubresproj_l` | 检验明细-多语言表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 41 | `t_qcpp_inspsubresrela` | 样本检验结果_项目样本关系-子表 | 10 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 42 | `t_qcpp_inspsubressamp` | 检验结果_样本-子表 | 7 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 43 | `t_qcpp_joininspect` | 生产联合检验单-主表 | 14 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 44 | `t_qcpp_joininspect_lk` | 关联子实体-子表 | 6 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 45 | `t_qcpp_joininspect_tc` | 生产联合检验单-关联追踪表 | 7 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 46 | `t_qcpp_joininspect_wb` | 生产联合检验单-反写记录表 | 10 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 47 | `t_qcpp_joininspentry` | 物料信息-子表 | 40 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 48 | `t_qcpp_joininspentry_lk` | 关联子实体-子表 | 6 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 49 | `t_qcpp_joininspproj` | 检验信息-子表 | 33 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 50 | `t_qcpp_joininsprela_n` | 样本检验结果_项目样本关系-子表 | 10 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 51 | `t_qcpp_joininspsamp_n` | 检验结果_样本-子表 | 7 | [qcpp_joininspect.md](./qcpp_joininspect.md) |
| 52 | `t_qcpp_mrb` | 生产MRB评审单-主表 | 47 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 53 | `t_qcpp_mrb_l` | 生产MRB评审单-多语言表 | 5 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 54 | `t_qcpp_mrb_s` | 生产MRB评审单-分表 | 17 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 55 | `t_qcpp_mrb_tc` | 生产MRB评审单-关联追踪表 | 7 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 56 | `t_qcpp_mrb_wb` | 生产MRB评审单-反写记录表 | 10 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 57 | `t_qcpp_mrbentry` | 评审明细-子表 | 28 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 58 | `t_qcpp_mrbentry_lk` | 关联子实体-子表 | 8 | [qcpp_mrbbill.md](./qcpp_mrbbill.md) |
| 59 | `t_qcpp_promatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 60 | `t_qcpp_resultentry` | 分批信息-单据体-子表 | 25 | [qcpp_inspresult.md](./qcpp_inspresult.md) |
| 61 | `t_qcpp_resultentry_lk` | 关联子实体-子表 | 6 | [qcpp_inspresult.md](./qcpp_inspresult.md) |
| 62 | `t_qcpp_samplecheck` | 样本检测-无检验项目时显示-子表 | 8 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 63 | `t_qcpp_samplecheck_l` | 样本检测-无检验项目时显示-多语言表 | 4 | [qcpp_manuinspec.md](./qcpp_manuinspec.md) |
| 64 | `t_qcpp_ycbill_bad` | 单据体-子表 | 29 | [qcpp_yieldreceivebill.md](./qcpp_yieldreceivebill.md) |
| 65 | `t_qcpp_ycbill_bad_lk` | 关联子实体-子表 | 8 | [qcpp_yieldreceivebill.md](./qcpp_yieldreceivebill.md) |
| 66 | `t_qcpp_yieldrecbill` | 生产让步接收申请单-主表 | 16 | [qcpp_yieldreceivebill.md](./qcpp_yieldreceivebill.md) |
| 67 | `t_qcpp_yieldrecbill_l` | 生产让步接收申请单-多语言表 | 4 | [qcpp_yieldreceivebill.md](./qcpp_yieldreceivebill.md) |
| 68 | `t_qcpp_yieldrecbill_tc` | 生产让步接收申请单-关联追踪表 | 7 | [qcpp_yieldreceivebill.md](./qcpp_yieldreceivebill.md) |
| 69 | `t_qcpp_yieldrecbill_wb` | 生产让步接收申请单-反写记录表 | 10 | [qcpp_yieldreceivebill.md](./qcpp_yieldreceivebill.md) |
