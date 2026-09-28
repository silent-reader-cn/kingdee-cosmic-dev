# fap 模块表清单

> 本模块共收录 **7** 张表定义，来自 `fap_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fap
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fa_card_barcode` | 资产条码-多选基础资料表 | 3 | [fap_card_real.md](./fap_card_real.md) |
| 2 | `t_fa_card_real` | 个人负责资产-主表 | 57 | [fap_card_real.md](./fap_card_real.md) |
| 3 | `t_fa_card_real_l` | 个人负责资产-多语言表 | 4 | [fap_card_real.md](./fap_card_real.md) |
| 4 | `t_fa_card_real_lk` | 关联子实体-子表 | 8 | [fap_card_real.md](./fap_card_real.md) |
| 5 | `t_fa_card_real_tc` | 个人负责资产-关联追踪表 | 7 | [fap_card_real.md](./fap_card_real.md) |
| 6 | `t_fa_card_real_wb` | 个人负责资产-反写记录表 | 10 | [fap_card_real.md](./fap_card_real.md) |
| 7 | `t_fa_facility` | 附属设备分录-子表 | 13 | [fap_card_real.md](./fap_card_real.md) |
