# mscm 模块表清单

> 本模块共收录 **13** 张表定义，来自 `mscm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category mscm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mscm_favorites` | 移动供应链_用户收藏夹-主表 | 10 | [mscm_favoritesconfig.md](./mscm_favoritesconfig.md) |
| 2 | `t_mscm_imcfgfilter` | 筛选条件-子表 | 5 | [mscm_iminventorycfg.md](./mscm_iminventorycfg.md) |
| 3 | `t_mscm_imcfgshowlist` | 库存明细-子表 | 5 | [mscm_iminventorycfg.md](./mscm_iminventorycfg.md) |
| 4 | `t_mscm_imcfgsummary` | 汇总方式-子表 | 6 | [mscm_iminventorycfg.md](./mscm_iminventorycfg.md) |
| 5 | `t_mscm_imfilterplan` | 库存查询_筛选方案-主表 | 13 | [mscm_imfilterplan.md](./mscm_imfilterplan.md) |
| 6 | `t_mscm_iminventorycfg` | 库存查询显示设置-主表 | 15 | [mscm_iminventorycfg.md](./mscm_iminventorycfg.md) |
| 7 | `t_mscm_iminventorycfg_l` | 库存查询显示设置-多语言表 | 5 | [mscm_iminventorycfg.md](./mscm_iminventorycfg.md) |
| 8 | `t_mscm_smbillcfg` | 移动销售显示设置-主表 | 16 | [mscm_smbillcfg.md](./mscm_smbillcfg.md) |
| 9 | `t_mscm_smbillcfg_l` | 移动销售显示设置-多语言表 | 5 | [mscm_smbillcfg.md](./mscm_smbillcfg.md) |
| 10 | `t_mscm_smbillcfgeentity` | 单据体字段信息-子表 | 13 | [mscm_smbillcfg.md](./mscm_smbillcfg.md) |
| 11 | `t_mscm_smbillcfgeentity_l` | 单据体字段信息-多语言表 | 4 | [mscm_smbillcfg.md](./mscm_smbillcfg.md) |
| 12 | `t_mscm_smbillcfghentity` | 单据头字段信息-子表 | 13 | [mscm_smbillcfg.md](./mscm_smbillcfg.md) |
| 13 | `t_mscm_smbillcfghentity_l` | 单据头字段信息-多语言表 | 4 | [mscm_smbillcfg.md](./mscm_smbillcfg.md) |
