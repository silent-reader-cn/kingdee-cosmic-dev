# qcnp 模块表清单

> 本模块共收录 **65** 张表定义，来自 `qcnp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category qcnp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_qcnp_appinsentry` | 物料信息-子表 | 84 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 2 | `t_qcnp_appinsentry_lk` | 关联子实体-子表 | 6 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 3 | `t_qcnp_applyinssub` | 检验信息-子表 | 13 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 4 | `t_qcnp_baddeal` | 库存不良品处理单-主表 | 18 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 5 | `t_qcnp_baddeal_l` | 库存不良品处理单-多语言表 | 4 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 6 | `t_qcnp_baddeal_lk` | 关联子实体-子表 | 6 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 7 | `t_qcnp_baddeal_tc` | 库存不良品处理单-关联追踪表 | 7 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 8 | `t_qcnp_baddeal_wb` | 库存不良品处理单-反写记录表 | 10 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 9 | `t_qcnp_baddealentry` | 不良处理信息-子表 | 82 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 10 | `t_qcnp_baddealentry_lk` | 关联子实体-子表 | 6 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 11 | `t_qcnp_badserialnumber` | 序列号分录-子表 | 10 | [qcnp_invbalbaddeal.md](./qcnp_invbalbaddeal.md) |
| 12 | `t_qcnp_iminv_entry` | 执行明细-子表 | 42 | [qcnp_imminv_model.md](./qcnp_imminv_model.md) |
| 13 | `t_qcnp_imminv` | 执行明细-主表 | 14 | [qcnp_imminv_model.md](./qcnp_imminv_model.md) |
| 14 | `t_qcnp_inspbill` | 库存检验单-主表 | 21 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 15 | `t_qcnp_inspbill_l` | 库存检验单-多语言表 | 4 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 16 | `t_qcnp_inspbill_lk` | 关联子实体-子表 | 6 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 17 | `t_qcnp_inspbill_tc` | 库存检验单-关联追踪表 | 7 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 18 | `t_qcnp_inspbill_wb` | 库存检验单-反写记录表 | 10 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 19 | `t_qcnp_inspctdef` | 缺陷记录-子表 | 10 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 20 | `t_qcnp_inspctdef_l` | 缺陷记录-多语言表 | 4 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 21 | `t_qcnp_inspctdefsn` | 序列号-多选基础资料表 | 3 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 22 | `t_qcnp_inspentry` | 物料信息-子表 | 93 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 23 | `t_qcnp_inspentry_l` | 物料信息-多语言表 | 4 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 24 | `t_qcnp_inspentry_lk` | 关联子实体-子表 | 6 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 25 | `t_qcnp_inspresult` | 库存检验结果-主表 | 29 | [qcnp_inspresult.md](./qcnp_inspresult.md) |
| 26 | `t_qcnp_inspresult_lk` | 关联子实体-子表 | 6 | [qcnp_inspresult.md](./qcnp_inspresult.md) |
| 27 | `t_qcnp_inspresult_tc` | 库存检验结果-关联追踪表 | 7 | [qcnp_inspresult.md](./qcnp_inspresult.md) |
| 28 | `t_qcnp_inspresult_wb` | 库存检验结果-反写记录表 | 10 | [qcnp_inspresult.md](./qcnp_inspresult.md) |
| 29 | `t_qcnp_inspsubbaddeal` | 不良处理信息-子表 | 32 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 30 | `t_qcnp_inspsubbaddeal_l` | 不良处理信息-多语言表 | 4 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 31 | `t_qcnp_inspsubbaddeal_lk` | 关联子实体-子表 | 6 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 32 | `t_qcnp_inspsubresproj` | 检验明细-子表 | 41 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 33 | `t_qcnp_inspsubresproj_l` | 检验明细-多语言表 | 4 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 34 | `t_qcnp_inspsubresrela` | 样本检验结果_项目样本关系-子表 | 10 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 35 | `t_qcnp_inspsubressamp` | 检验结果_样本-子表 | 7 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 36 | `t_qcnp_inv_ip_mod` | 库存检验计划过滤条件模型-主表 | 0 | [qcnp_invinsp_filtermodel.md](./qcnp_invinsp_filtermodel.md) |
| 37 | `t_qcnp_invapplyins` | 库存请检单-主表 | 18 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 38 | `t_qcnp_invapplyins_l` | 库存请检单-多语言表 | 4 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 39 | `t_qcnp_invapplyins_lk` | 关联子实体-子表 | 6 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 40 | `t_qcnp_invapplyins_tc` | 库存请检单-关联追踪表 | 7 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 41 | `t_qcnp_invapplyins_wb` | 库存请检单-反写记录表 | 10 | [qcnp_invinspectplan.md](./qcnp_invinspectplan.md) |
| 42 | `t_qcnp_invinsp_inf` | 库存检验信息-主表 | 8 | [qcnp_invinsp_info.md](./qcnp_invinsp_info.md) |
| 43 | `t_qcnp_joininspect` | 库存联合检验单-主表 | 14 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 44 | `t_qcnp_joininspect_lk` | 关联子实体-子表 | 6 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 45 | `t_qcnp_joininspect_tc` | 库存联合检验单-关联追踪表 | 7 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 46 | `t_qcnp_joininspect_wb` | 库存联合检验单-反写记录表 | 10 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 47 | `t_qcnp_joininspentry` | 物料信息-子表 | 33 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 48 | `t_qcnp_joininspentry_lk` | 关联子实体-子表 | 6 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 49 | `t_qcnp_joininspproj` | 检验信息-子表 | 33 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 50 | `t_qcnp_joininspproj_lk` | 关联子实体-子表 | 6 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 51 | `t_qcnp_joininsprela_n` | 样本检验结果_项目样本关系-子表 | 10 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 52 | `t_qcnp_joininspsamp_n` | 检验结果_样本-子表 | 7 | [qcnp_joininspect.md](./qcnp_joininspect.md) |
| 53 | `t_qcnp_mrb` | 库存MRB评审单-主表 | 37 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 54 | `t_qcnp_mrb_l` | 库存MRB评审单-多语言表 | 5 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 55 | `t_qcnp_mrb_s` | 库存MRB评审单-分表 | 17 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 56 | `t_qcnp_mrb_tc` | 库存MRB评审单-关联追踪表 | 7 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 57 | `t_qcnp_mrb_wb` | 库存MRB评审单-反写记录表 | 10 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 58 | `t_qcnp_mrbentry` | 评审明细-子表 | 23 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 59 | `t_qcnp_mrbentry_lk` | 关联子实体-子表 | 8 | [qcnp_mrbbill.md](./qcnp_mrbbill.md) |
| 60 | `t_qcnp_promatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 61 | `t_qcnp_resultentry` | 分批信息-单据体-子表 | 25 | [qcnp_inspresult.md](./qcnp_inspresult.md) |
| 62 | `t_qcnp_resultentry_lk` | 关联子实体-子表 | 6 | [qcnp_inspresult.md](./qcnp_inspresult.md) |
| 63 | `t_qcnp_samplecheck` | 样本检测-无检验项目时显示-子表 | 8 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 64 | `t_qcnp_samplecheck_l` | 样本检测-无检验项目时显示-多语言表 | 4 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
| 65 | `t_qcnp_serialnumber` | 序列号分录-子表 | 10 | [qcnp_invbalinspec.md](./qcnp_invbalinspec.md) |
