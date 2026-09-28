# modelm 模块表清单

> 本模块共收录 **7** 张表定义，来自 `modelm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category modelm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_dm_pdmmodelversion` | 数据模型操作日志-主表 | 13 | [bos_datamodel_log.md](./bos_datamodel_log.md) |
| 2 | `t_mast_statistics` | 模型资产统计-主表 | 16 | [statistics.md](./statistics.md) |
| 3 | `t_mast_statistics_l` | 模型资产统计-多语言表 | 4 | [statistics.md](./statistics.md) |
| 4 | `t_meta_dynplugin` | 动态插件定义-主表 | 21 | [bos_dynplugin.md](./bos_dynplugin.md) |
| 5 | `t_meta_dynplugin_l` | 动态插件定义-多语言表 | 4 | [bos_dynplugin.md](./bos_dynplugin.md) |
| 6 | `t_meta_dynpluginbind` | 动态插件注册-主表 | 19 | [bos_dynpluginbind.md](./bos_dynpluginbind.md) |
| 7 | `t_meta_dynpluginbind_l` | 动态插件注册-多语言表 | 4 | [bos_dynpluginbind.md](./bos_dynpluginbind.md) |
