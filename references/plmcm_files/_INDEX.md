# plmcm 模块表清单

> 本模块共收录 **7** 张表定义，来自 `plmcm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope plmcm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_plm_pdm_relation` | 更改内容-主表 | 46 | [plm_plmcm_changereport.md](./plm_plmcm_changereport.md) |
| 2 | `t_plm_pdm_relation` | 影响对象-主表 | 46 | [plm_plmcm_effected_object.md](./plm_plmcm_effected_object.md) |
| 3 | `t_plmcm_bomchange` | 结构变更-子表 | 21 | [plm_plmcm_changereport.md](./plm_plmcm_changereport.md) |
| 4 | `t_plmcm_classifychange` | 分类属性-子表 | 7 | [plm_plmcm_changereport.md](./plm_plmcm_changereport.md) |
| 5 | `t_plmcm_effectedobject` | 单据体-子表 | 6 | [plm_plmcm_effected_object.md](./plm_plmcm_effected_object.md) |
| 6 | `t_plmcm_propertychange` | 基本属性-子表 | 7 | [plm_plmcm_changereport.md](./plm_plmcm_changereport.md) |
| 7 | `t_plmcm_viewchange` | 视图变更-子表 | 4 | [plm_plmcm_changereport.md](./plm_plmcm_changereport.md) |
