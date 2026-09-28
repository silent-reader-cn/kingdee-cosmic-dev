# xkda 模块表清单

> 本模块共收录 **14** 张表定义，来自 `xkda_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category xkda
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fa_data_asset` | 数据资产-主表 | 25 | [fa_data_asset.md](./fa_data_asset.md) |
| 2 | `t_fa_data_asset_l` | 数据资产-多语言表 | 5 | [fa_data_asset.md](./fa_data_asset.md) |
| 3 | `t_fa_data_asset_lk` | 关联子实体-子表 | 6 | [fa_data_asset.md](./fa_data_asset.md) |
| 4 | `t_fa_data_asset_tc` | 数据资产-关联追踪表 | 7 | [fa_data_asset.md](./fa_data_asset.md) |
| 5 | `t_fa_data_asset_wb` | 数据资产-反写记录表 | 10 | [fa_data_asset.md](./fa_data_asset.md) |
| 6 | `t_fa_data_detail` | 单据体-子表 | 12 | [fa_data_asset.md](./fa_data_asset.md) |
| 7 | `t_fa_data_detail` | 数据资产明细-主表 | 12 | [fa_data_asset_detail.md](./fa_data_asset_detail.md) |
| 8 | `t_fa_data_detail_l` | 单据体-多语言表 | 5 | [fa_data_asset.md](./fa_data_asset.md) |
| 9 | `t_fa_data_detail_l` | 数据资产明细-多语言表 | 5 | [fa_data_asset_detail.md](./fa_data_asset_detail.md) |
| 10 | `t_fa_data_resource` | 数据资源-主表 | 19 | [fa_data_resource.md](./fa_data_resource.md) |
| 11 | `t_fa_data_resource_l` | 数据资源-多语言表 | 5 | [fa_data_resource.md](./fa_data_resource.md) |
| 12 | `t_fa_data_resource_lk` | 关联子实体-子表 | 6 | [fa_data_resource.md](./fa_data_resource.md) |
| 13 | `t_fa_data_resource_tc` | 数据资源-关联追踪表 | 7 | [fa_data_resource.md](./fa_data_resource.md) |
| 14 | `t_fa_data_resource_wb` | 数据资源-反写记录表 | 10 | [fa_data_resource.md](./fa_data_resource.md) |
