# plmmm 模块表清单

> 本模块共收录 **24** 张表定义，来自 `plmmm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category plmmm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_plm_mtldocmatch_log` | 物料文档自动匹配日志-主表 | 14 | [plm_plmmm_mtldocmatch_log.md](./plm_plmmm_mtldocmatch_log.md) |
| 2 | `t_plm_pdm_basic` | 物料_单据参数-主表 | 38 | [plm_pdm_material_conf.md](./plm_pdm_material_conf.md) |
| 3 | `t_plm_pdm_basic` | 物料版本_参数预置-主表 | 38 | [plm_pdm_material_rev_conf.md](./plm_pdm_material_rev_conf.md) |
| 4 | `t_plm_pdm_basic` | 技术资料导出审核单-主表 | 38 | [plm_plmmm_export_audit.md](./plm_plmmm_export_audit.md) |
| 5 | `t_plm_pdm_basic_l` | 物料_单据参数-多语言表 | 10 | [plm_pdm_material_conf.md](./plm_pdm_material_conf.md) |
| 6 | `t_plm_pdm_basic_l` | 物料版本_参数预置-多语言表 | 10 | [plm_pdm_material_rev_conf.md](./plm_pdm_material_rev_conf.md) |
| 7 | `t_plm_pdm_basic_l` | 技术资料导出审核单-多语言表 | 10 | [plm_plmmm_export_audit.md](./plm_plmmm_export_audit.md) |
| 8 | `t_plm_pdm_basic_mb` | 物料_单据参数-分表 | 104 | [plm_pdm_material_conf.md](./plm_pdm_material_conf.md) |
| 9 | `t_plm_pdm_basic_mb` | 物料版本_参数预置-分表 | 104 | [plm_pdm_material_rev_conf.md](./plm_pdm_material_rev_conf.md) |
| 10 | `t_plm_pdm_basic_mb` | 技术资料导出审核单-分表 | 104 | [plm_plmmm_export_audit.md](./plm_plmmm_export_audit.md) |
| 11 | `t_plm_pdm_basic_mm` | 物料_单据参数-分表 | 5 | [plm_pdm_material_conf.md](./plm_pdm_material_conf.md) |
| 12 | `t_plm_pdm_basic_mr` | 物料_单据参数-分表 | 48 | [plm_pdm_material_conf.md](./plm_pdm_material_conf.md) |
| 13 | `t_plm_pdm_basic_mr` | 物料版本_参数预置-分表 | 48 | [plm_pdm_material_rev_conf.md](./plm_pdm_material_rev_conf.md) |
| 14 | `t_plm_pdm_basic_mr` | 技术资料导出审核单-分表 | 48 | [plm_plmmm_export_audit.md](./plm_plmmm_export_audit.md) |
| 15 | `t_plm_pdm_basic_u` | 物料_单据参数-使用范围表 | 3 | [plm_pdm_material_conf.md](./plm_pdm_material_conf.md) |
| 16 | `t_plm_pdm_basic_u` | 物料版本_参数预置-使用范围表 | 3 | [plm_pdm_material_rev_conf.md](./plm_pdm_material_rev_conf.md) |
| 17 | `t_plm_pdm_basic_u` | 技术资料导出审核单-使用范围表 | 3 | [plm_plmmm_export_audit.md](./plm_plmmm_export_audit.md) |
| 18 | `t_plm_pdm_relation` | 目标关系单据体-子表 | 79 | [plm_plmmm_export_audit.md](./plm_plmmm_export_audit.md) |
| 19 | `t_plmmm_integrity_classif` | 分类-多选基础资料表 | 3 | [plm_plmmm_integrity_pro.md](./plm_plmmm_integrity_pro.md) |
| 20 | `t_plmmm_integrity_entry` | 单据体-子表 | 8 | [plm_plmmm_integrity_pro.md](./plm_plmmm_integrity_pro.md) |
| 21 | `t_plmmm_integrity_flow` | 流程启动时校验模板-多选基础资料表 | 3 | [plm_plmmm_integrity_pro.md](./plm_plmmm_integrity_pro.md) |
| 22 | `t_plmmm_integrity_life` | 流程状态-多选基础资料表 | 3 | [plm_plmmm_integrity_pro.md](./plm_plmmm_integrity_pro.md) |
| 23 | `t_plmmm_integrity_project` | 完整性检查方案-主表 | 14 | [plm_plmmm_integrity_pro.md](./plm_plmmm_integrity_pro.md) |
| 24 | `t_plmmm_integrity_project_l` | 完整性检查方案-多语言表 | 5 | [plm_plmmm_integrity_pro.md](./plm_plmmm_integrity_pro.md) |
