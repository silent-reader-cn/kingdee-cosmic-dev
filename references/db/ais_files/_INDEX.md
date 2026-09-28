# ais 模块表清单

> 本模块共收录 **6** 张表定义，来自 `ais_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ais
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ais_entity_cfg` | 全局搜索对象-主表 | 12 | [ais_entity_cfg.md](./ais_entity_cfg.md) |
| 2 | `t_ais_entity_cfg_ref` | 被引用的实体-主表 | 10 | [ais_entity_cfg_ref.md](./ais_entity_cfg_ref.md) |
| 3 | `t_ais_entity_relation` | 实体配置引用关系-主表 | 3 | [ais_entity_relation.md](./ais_entity_relation.md) |
| 4 | `t_ais_guidewords` | 单据体-子表 | 6 | [ais_search_config.md](./ais_search_config.md) |
| 5 | `t_ais_guidewords_l` | 单据体-多语言表 | 4 | [ais_search_config.md](./ais_search_config.md) |
| 6 | `t_ais_search_config` | 搜索参数配置-主表 | 13 | [ais_search_config.md](./ais_search_config.md) |
