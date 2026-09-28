# cca 模块表清单

> 本模块共收录 **33** 张表定义，来自 `cca_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category cca
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cca_allocreport` | 分配报告-主表 | 16 | [cca_allocreport.md](./cca_allocreport.md) |
| 2 | `t_cca_allocreportdtl` | 步骤明细-子表 | 9 | [cca_allocreport.md](./cca_allocreport.md) |
| 3 | `t_cca_allocreportentry` | 单据体-子表 | 6 | [cca_allocreport.md](./cca_allocreport.md) |
| 4 | `t_cca_allocreporterc` | 发送方成本中心-多选基础资料表 | 3 | [cca_allocreport.md](./cca_allocreport.md) |
| 5 | `t_cca_allocreportesc` | 接收方成本中心-多选基础资料表 | 3 | [cca_allocreport.md](./cca_allocreport.md) |
| 6 | `t_cca_allocreportrule` | 分配规则-多选基础资料表 | 3 | [cca_allocreport.md](./cca_allocreport.md) |
| 7 | `t_cca_costcenterbal` | 成本中心余额-主表 | 17 | [cca_costcenterbal.md](./cca_costcenterbal.md) |
| 8 | `t_cca_costcenterbalentry` | 单据体-子表 | 8 | [cca_costcenterbal.md](./cca_costcenterbal.md) |
| 9 | `t_cca_feeallocresult` | 费用分配结果-主表 | 15 | [cca_feeallocresult.md](./cca_feeallocresult.md) |
| 10 | `t_cca_feeallocresulte` | 单据体-子表 | 22 | [cca_feeallocresult.md](./cca_feeallocresult.md) |
| 11 | `t_cca_feeallocresulte_l` | 单据体-多语言表 | 4 | [cca_feeallocresult.md](./cca_feeallocresult.md) |
| 12 | `t_cca_feeallocrule` | 费用分配规则-主表 | 21 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 13 | `t_cca_feeallocrule_l` | 费用分配规则-多语言表 | 5 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 14 | `t_cca_feeallocruleav` | 会计科目-多选基础资料表 | 3 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 15 | `t_cca_feeallocruleei` | 费用项目-多选基础资料表 | 3 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 16 | `t_cca_feeallocruleentry` | 单据体-子表 | 13 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 17 | `t_cca_feeallocruleentry_l` | 单据体-多语言表 | 4 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 18 | `t_cca_feeallocrulerc` | 接收方成本中心-多选基础资料表 | 3 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 19 | `t_cca_feeallocrulesc` | 发送方成本中心-多选基础资料表 | 3 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 20 | `t_cca_feeallocruleweight` | 子单据体-子表 | 5 | [cca_feeallocrule.md](./cca_feeallocrule.md) |
| 21 | `t_cca_keyindicator` | 关键指标-主表 | 16 | [cca_keyindicator.md](./cca_keyindicator.md) |
| 22 | `t_cca_keyindicator_l` | 关键指标-多语言表 | 4 | [cca_keyindicator.md](./cca_keyindicator.md) |
| 23 | `t_cca_keyindicatoracct` | 指标记账-主表 | 15 | [cca_keyindicatoracct.md](./cca_keyindicatoracct.md) |
| 24 | `t_cca_keyindicatoracct_l` | 指标记账-多语言表 | 4 | [cca_keyindicatoracct.md](./cca_keyindicatoracct.md) |
| 25 | `t_cca_keyindicatoracctent` | 单据体-子表 | 8 | [cca_keyindicatoracct.md](./cca_keyindicatoracct.md) |
| 26 | `t_cca_mfgfeecollc` | 费用归集-主表 | 25 | [cca_mfgfeebill.md](./cca_mfgfeebill.md) |
| 27 | `t_cca_mfgfeecollc_l` | 费用归集-多语言表 | 4 | [cca_mfgfeebill.md](./cca_mfgfeebill.md) |
| 28 | `t_cca_mfgfeeimpsch` | 费用归集方案-主表 | 15 | [cca_mfgfeeimpsch.md](./cca_mfgfeeimpsch.md) |
| 29 | `t_cca_mfgfeeimpsch_l` | 费用归集方案-多语言表 | 5 | [cca_mfgfeeimpsch.md](./cca_mfgfeeimpsch.md) |
| 30 | `t_cca_mfgfeeimpschentry` | 单据体-子表 | 8 | [cca_mfgfeeimpsch.md](./cca_mfgfeeimpsch.md) |
| 31 | `t_cca_mfgimp_accountviews` | 来源科目-多选基础资料表 | 3 | [cca_mfgfeeimpsch.md](./cca_mfgfeeimpsch.md) |
| 32 | `t_cca_query_scheme` | 查询方案-主表 | 15 | [cca_query_scheme.md](./cca_query_scheme.md) |
| 33 | `t_cca_query_scheme_l` | 查询方案-多语言表 | 4 | [cca_query_scheme.md](./cca_query_scheme.md) |
