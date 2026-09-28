# plmpsm 模块表清单

> 本模块共收录 **7** 张表定义，来自 `plmpsm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category plmpsm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bd_replaceplan` | 物料替代方案-主表 | 30 | [plm_plmpsm_replaceplan.md](./plm_plmpsm_replaceplan.md) |
| 2 | `t_bd_replaceplan_l` | 物料替代方案-多语言表 | 4 | [plm_plmpsm_replaceplan.md](./plm_plmpsm_replaceplan.md) |
| 3 | `t_bd_replaceplan_u` | 物料替代方案-使用范围表 | 3 | [plm_plmpsm_replaceplan.md](./plm_plmpsm_replaceplan.md) |
| 4 | `t_bd_replaceplanentry_m` | 主物料-子表 | 12 | [plm_plmpsm_replaceplan.md](./plm_plmpsm_replaceplan.md) |
| 5 | `t_bd_replaceplanentry_r` | 替代物料-子表 | 14 | [plm_plmpsm_replaceplan.md](./plm_plmpsm_replaceplan.md) |
| 6 | `t_plm_plmpsm_bomview` | BOM视图-主表 | 14 | [plm_plmpsm_newbomview.md](./plm_plmpsm_newbomview.md) |
| 7 | `t_plm_plmpsm_bomview_l` | BOM视图-多语言表 | 5 | [plm_plmpsm_newbomview.md](./plm_plmpsm_newbomview.md) |
