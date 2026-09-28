# qcas 模块表清单

> 本模块共收录 **60** 张表定义，来自 `qcas_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category qcas
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_qcas_appinsentry` | 物料信息-子表 | 84 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 2 | `t_qcas_appinsentry_lk` | 关联子实体-子表 | 6 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 3 | `t_qcas_applyinssub` | 检验信息-子表 | 13 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 4 | `t_qcas_baddeal` | 销售不良品处理单-主表 | 18 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 5 | `t_qcas_baddeal_l` | 销售不良品处理单-多语言表 | 4 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 6 | `t_qcas_baddeal_lk` | 关联子实体-子表 | 6 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 7 | `t_qcas_baddeal_tc` | 销售不良品处理单-关联追踪表 | 7 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 8 | `t_qcas_baddeal_wb` | 销售不良品处理单-反写记录表 | 10 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 9 | `t_qcas_baddealentry` | 不良处理信息-子表 | 74 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 10 | `t_qcas_baddealentry_lk` | 关联子实体-子表 | 6 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 11 | `t_qcas_badserialnumber` | 序列号分录-子表 | 10 | [qcas_salebaddeal.md](./qcas_salebaddeal.md) |
| 12 | `t_qcas_inspbill` | 销售检验单-主表 | 21 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 13 | `t_qcas_inspbill_l` | 销售检验单-多语言表 | 4 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 14 | `t_qcas_inspbill_lk` | 关联子实体-子表 | 6 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 15 | `t_qcas_inspbill_tc` | 销售检验单-关联追踪表 | 7 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 16 | `t_qcas_inspbill_wb` | 销售检验单-反写记录表 | 10 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 17 | `t_qcas_inspctdef` | 缺陷记录-子表 | 10 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 18 | `t_qcas_inspctdef_l` | 缺陷记录-多语言表 | 4 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 19 | `t_qcas_inspctdefsn` | 序列号-多选基础资料表 | 3 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 20 | `t_qcas_inspentry` | 物料信息-子表 | 85 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 21 | `t_qcas_inspentry_l` | 物料信息-多语言表 | 4 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 22 | `t_qcas_inspentry_lk` | 关联子实体-子表 | 6 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 23 | `t_qcas_inspresult` | 销售检验结果-主表 | 32 | [qcas_inspresult.md](./qcas_inspresult.md) |
| 24 | `t_qcas_inspresult_lk` | 关联子实体-子表 | 6 | [qcas_inspresult.md](./qcas_inspresult.md) |
| 25 | `t_qcas_inspresult_tc` | 销售检验结果-关联追踪表 | 7 | [qcas_inspresult.md](./qcas_inspresult.md) |
| 26 | `t_qcas_inspresult_wb` | 销售检验结果-反写记录表 | 10 | [qcas_inspresult.md](./qcas_inspresult.md) |
| 27 | `t_qcas_inspsubbaddeal` | 不良处理信息-子表 | 34 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 28 | `t_qcas_inspsubbaddeal_l` | 不良处理信息-多语言表 | 4 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 29 | `t_qcas_inspsubresproj` | 检验明细-子表 | 41 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 30 | `t_qcas_inspsubresproj_l` | 检验明细-多语言表 | 4 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 31 | `t_qcas_inspsubresrela` | 样本检验结果_项目样本关系-子表 | 10 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 32 | `t_qcas_inspsubressamp` | 检验结果_样本-子表 | 7 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 33 | `t_qcas_invapplyins` | 发货请检单-主表 | 22 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 34 | `t_qcas_invapplyins_l` | 发货请检单-多语言表 | 4 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 35 | `t_qcas_invapplyins_lk` | 关联子实体-子表 | 6 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 36 | `t_qcas_invapplyins_tc` | 发货请检单-关联追踪表 | 7 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 37 | `t_qcas_invapplyins_wb` | 发货请检单-反写记录表 | 10 | [qcas_invinspectplan.md](./qcas_invinspectplan.md) |
| 38 | `t_qcas_joininspect` | 销售联合检验单-主表 | 14 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 39 | `t_qcas_joininspect_lk` | 关联子实体-子表 | 6 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 40 | `t_qcas_joininspect_tc` | 销售联合检验单-关联追踪表 | 7 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 41 | `t_qcas_joininspect_wb` | 销售联合检验单-反写记录表 | 10 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 42 | `t_qcas_joininspentry` | 物料信息-子表 | 33 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 43 | `t_qcas_joininspentry_lk` | 关联子实体-子表 | 6 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 44 | `t_qcas_joininspproj` | 检验信息-子表 | 33 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 45 | `t_qcas_joininspproj_lk` | 关联子实体-子表 | 6 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 46 | `t_qcas_joininsprela_n` | 样本检验结果_项目样本关系-子表 | 10 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 47 | `t_qcas_joininspsamp_n` | 检验结果_样本-子表 | 7 | [qcas_joininspect.md](./qcas_joininspect.md) |
| 48 | `t_qcas_mrb` | 销售MRB评审单-主表 | 38 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 49 | `t_qcas_mrb_l` | 销售MRB评审单-多语言表 | 5 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 50 | `t_qcas_mrb_s` | 销售MRB评审单-分表 | 17 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 51 | `t_qcas_mrb_tc` | 销售MRB评审单-关联追踪表 | 7 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 52 | `t_qcas_mrb_wb` | 销售MRB评审单-反写记录表 | 10 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 53 | `t_qcas_mrbentry` | 评审明细-子表 | 23 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 54 | `t_qcas_mrbentry_lk` | 关联子实体-子表 | 8 | [qcas_mrbbill.md](./qcas_mrbbill.md) |
| 55 | `t_qcas_promatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 56 | `t_qcas_resultentry` | 分批信息-单据体-子表 | 25 | [qcas_inspresult.md](./qcas_inspresult.md) |
| 57 | `t_qcas_resultentry_lk` | 关联子实体-子表 | 6 | [qcas_inspresult.md](./qcas_inspresult.md) |
| 58 | `t_qcas_samplecheck` | 样本检测-无检验项目时显示-子表 | 8 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 59 | `t_qcas_samplecheck_l` | 样本检测-无检验项目时显示-多语言表 | 4 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
| 60 | `t_qcas_serialnumber` | 序列号分录-子表 | 10 | [qcas_saleinspec.md](./qcas_saleinspec.md) |
