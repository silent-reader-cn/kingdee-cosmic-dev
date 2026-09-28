# qcop 模块表清单

> 本模块共收录 **49** 张表定义，来自 `qcop_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category qcop
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_qcop_baddeal` | 其他不良品处理单-主表 | 18 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 2 | `t_qcop_baddeal_l` | 其他不良品处理单-多语言表 | 4 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 3 | `t_qcop_baddeal_lk` | 关联子实体-子表 | 6 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 4 | `t_qcop_baddeal_tc` | 其他不良品处理单-关联追踪表 | 7 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 5 | `t_qcop_baddeal_wb` | 其他不良品处理单-反写记录表 | 10 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 6 | `t_qcop_baddealentry` | 不良处理信息-子表 | 91 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 7 | `t_qcop_baddealentry_a` | 不良处理信息-分表 | 6 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 8 | `t_qcop_baddealentry_lk` | 关联子实体-子表 | 6 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 9 | `t_qcop_badserialnumber` | 序列号分录-子表 | 10 | [qcop_otherbaddeal.md](./qcop_otherbaddeal.md) |
| 10 | `t_qcop_insappentry` | 物料信息-子表 | 74 | [qcop_otherinspecapply.md](./qcop_otherinspecapply.md) |
| 11 | `t_qcop_insappentry_q` | 物料信息-分表 | 6 | [qcop_otherinspecapply.md](./qcop_otherinspecapply.md) |
| 12 | `t_qcop_inspapplyproj` | 联合检验信息-子表 | 23 | [qcop_otherinspecapply.md](./qcop_otherinspecapply.md) |
| 13 | `t_qcop_inspbill` | 其他检验单-主表 | 19 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 14 | `t_qcop_inspbill_l` | 其他检验单-多语言表 | 4 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 15 | `t_qcop_inspbill_lk` | 关联子实体-子表 | 6 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 16 | `t_qcop_inspbill_tc` | 其他检验单-关联追踪表 | 7 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 17 | `t_qcop_inspbill_wb` | 其他检验单-反写记录表 | 10 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 18 | `t_qcop_inspctdef` | 缺陷记录-子表 | 10 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 19 | `t_qcop_inspctdef_l` | 缺陷记录-多语言表 | 4 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 20 | `t_qcop_inspctdefsn` | 序列号-多选基础资料表 | 3 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 21 | `t_qcop_inspecapply` | 其他请检单-主表 | 18 | [qcop_otherinspecapply.md](./qcop_otherinspecapply.md) |
| 22 | `t_qcop_inspecapply_l` | 其他请检单-多语言表 | 4 | [qcop_otherinspecapply.md](./qcop_otherinspecapply.md) |
| 23 | `t_qcop_inspentry` | 物料信息-子表 | 102 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 24 | `t_qcop_inspentry_a` | 物料信息-分表 | 6 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 25 | `t_qcop_inspentry_l` | 物料信息-多语言表 | 4 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 26 | `t_qcop_inspentry_lk` | 关联子实体-子表 | 10 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 27 | `t_qcop_inspresult` | 其他检验检验结果-主表 | 32 | [qcop_inspresult.md](./qcop_inspresult.md) |
| 28 | `t_qcop_inspresult_lk` | 关联子实体-子表 | 6 | [qcop_inspresult.md](./qcop_inspresult.md) |
| 29 | `t_qcop_inspresult_tc` | 其他检验检验结果-关联追踪表 | 7 | [qcop_inspresult.md](./qcop_inspresult.md) |
| 30 | `t_qcop_inspresult_wb` | 其他检验检验结果-反写记录表 | 10 | [qcop_inspresult.md](./qcop_inspresult.md) |
| 31 | `t_qcop_inspsubbaddeal` | 不良处理信息-子表 | 41 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 32 | `t_qcop_inspsubbaddeal_l` | 不良处理信息-多语言表 | 4 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 33 | `t_qcop_inspsubresproj` | 检验明细-子表 | 42 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 34 | `t_qcop_inspsubresproj_l` | 检验明细-多语言表 | 4 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 35 | `t_qcop_inspsubresrela` | 样本检验结果_项目样本关系-子表 | 10 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 36 | `t_qcop_inspsubressamp` | 检验结果_样本-子表 | 7 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 37 | `t_qcop_mrb` | 其他MRB评审单-主表 | 37 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 38 | `t_qcop_mrb_l` | 其他MRB评审单-多语言表 | 5 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 39 | `t_qcop_mrb_s` | 其他MRB评审单-分表 | 21 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 40 | `t_qcop_mrb_tc` | 其他MRB评审单-关联追踪表 | 7 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 41 | `t_qcop_mrb_wb` | 其他MRB评审单-反写记录表 | 10 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 42 | `t_qcop_mrbentry` | 评审明细-子表 | 23 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 43 | `t_qcop_mrbentry_lk` | 关联子实体-子表 | 8 | [qcop_mrbbill.md](./qcop_mrbbill.md) |
| 44 | `t_qcop_promatchdimo` | 检验方案匹配维度-多选基础资料表 | 3 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 45 | `t_qcop_resultentry` | 分批信息-单据体-子表 | 23 | [qcop_inspresult.md](./qcop_inspresult.md) |
| 46 | `t_qcop_resultentry_lk` | 关联子实体-子表 | 6 | [qcop_inspresult.md](./qcop_inspresult.md) |
| 47 | `t_qcop_samplecheck` | 样本检测-无检验项目时显示-子表 | 8 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 48 | `t_qcop_samplecheck_l` | 样本检测-无检验项目时显示-多语言表 | 4 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
| 49 | `t_qcop_serialnumber` | 序列号分录-子表 | 10 | [qcop_otherinspec.md](./qcop_otherinspec.md) |
