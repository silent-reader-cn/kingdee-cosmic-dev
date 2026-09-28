# md 模块表清单

> 本模块共收录 **60** 张表定义，来自 `md_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category md
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_md_apphome_setting` | 市场数据主页设置-主表 | 19 | [md_apphome_setting.md](./md_apphome_setting.md) |
| 2 | `t_md_apphome_setting_l` | 市场数据主页设置-多语言表 | 5 | [md_apphome_setting.md](./md_apphome_setting.md) |
| 3 | `t_md_blpfield` | 彭博字段-主表 | 0 | [md_blpfield.md](./md_blpfield.md) |
| 4 | `t_md_blpfield_l` | 彭博字段-多语言表 | 0 | [md_blpfield.md](./md_blpfield.md) |
| 5 | `t_md_blprequest` | 彭博请求-主表 | 0 | [md_blprequest.md](./md_blprequest.md) |
| 6 | `t_md_bondvol` | 债券波动率曲面-主表 | 21 | [md_bondvol.md](./md_bondvol.md) |
| 7 | `t_md_bondvol` | 债券波动率曲面-主表 | 21 | [md_bondvol_f7.md](./md_bondvol_f7.md) |
| 8 | `t_md_bondvol_bi` | 债券发行-多选基础资料表 | 3 | [md_bondvol.md](./md_bondvol.md) |
| 9 | `t_md_bondvol_entrys` | 金融工具单据体-子表 | 20 | [md_bondvol.md](./md_bondvol.md) |
| 10 | `t_md_bondvol_l` | 债券波动率曲面-多语言表 | 5 | [md_bondvol.md](./md_bondvol.md) |
| 11 | `t_md_bondvol_l` | 债券波动率曲面-多语言表 | 5 | [md_bondvol_f7.md](./md_bondvol_f7.md) |
| 12 | `t_md_datagoods` | 商品数据-主表 | 21 | [md_datagoods.md](./md_datagoods.md) |
| 13 | `t_md_datagoods_l` | 商品数据-多语言表 | 5 | [md_datagoods.md](./md_datagoods.md) |
| 14 | `t_md_dataindex` | 指数数据-主表 | 21 | [md_dataindex.md](./md_dataindex.md) |
| 15 | `t_md_dataindex_l` | 指数数据-多语言表 | 5 | [md_dataindex.md](./md_dataindex.md) |
| 16 | `t_md_dataratederic` | 利率衍生品数据-主表 | 20 | [md_dataratederic.md](./md_dataratederic.md) |
| 17 | `t_md_dataratederic_l` | 利率衍生品数据-多语言表 | 5 | [md_dataratederic.md](./md_dataratederic.md) |
| 18 | `t_md_forexquote` | 外汇报价-主表 | 19 | [md_forexquote.md](./md_forexquote.md) |
| 19 | `t_md_forexquote` | 外汇报价-主表 | 19 | [md_forexquote_f7.md](./md_forexquote_f7.md) |
| 20 | `t_md_forexquote_define` | 定义-子表 | 20 | [md_forexquote.md](./md_forexquote.md) |
| 21 | `t_md_forexquote_define_h` | 定义-子表 | 20 | [md_forexquote_h.md](./md_forexquote_h.md) |
| 22 | `t_md_forexquote_h` | 历史外汇报价-主表 | 21 | [md_forexquote_h.md](./md_forexquote_h.md) |
| 23 | `t_md_forexquote_h_l` | 历史外汇报价-多语言表 | 5 | [md_forexquote_h.md](./md_forexquote_h.md) |
| 24 | `t_md_forexquote_input` | 报价录入-子表 | 12 | [md_forexquote.md](./md_forexquote.md) |
| 25 | `t_md_forexquote_input_h` | 报价录入-子表 | 12 | [md_forexquote_h.md](./md_forexquote_h.md) |
| 26 | `t_md_forexquote_l` | 外汇报价-多语言表 | 5 | [md_forexquote.md](./md_forexquote.md) |
| 27 | `t_md_forexquote_l` | 外汇报价-多语言表 | 5 | [md_forexquote_f7.md](./md_forexquote_f7.md) |
| 28 | `t_md_forexquote_output` | 报价输出-子表 | 9 | [md_forexquote.md](./md_forexquote.md) |
| 29 | `t_md_forexquote_output_h` | 报价输出-子表 | 9 | [md_forexquote_h.md](./md_forexquote_h.md) |
| 30 | `t_md_forexvol` | 外汇波动率曲面-主表 | 30 | [md_forexvol.md](./md_forexvol.md) |
| 31 | `t_md_forexvol` | 外汇波动率曲面-主表 | 30 | [md_forexvol_f7.md](./md_forexvol_f7.md) |
| 32 | `t_md_forexvol_entrys` | 单据体-子表 | 24 | [md_forexvol.md](./md_forexvol.md) |
| 33 | `t_md_forexvol_l` | 外汇波动率曲面-多语言表 | 5 | [md_forexvol.md](./md_forexvol.md) |
| 34 | `t_md_forexvol_l` | 外汇波动率曲面-多语言表 | 5 | [md_forexvol_f7.md](./md_forexvol_f7.md) |
| 35 | `t_md_interface` | 接口配置-主表 | 0 | [md_interface.md](./md_interface.md) |
| 36 | `t_md_interface_l` | 接口配置-多语言表 | 0 | [md_interface.md](./md_interface.md) |
| 37 | `t_md_intratevol` | 利率上限波动率曲面-主表 | 36 | [md_intratevol.md](./md_intratevol.md) |
| 38 | `t_md_intratevol` | 利率上限波动率曲面-主表 | 36 | [md_intratevol_f7.md](./md_intratevol_f7.md) |
| 39 | `t_md_intratevol_l` | 利率上限波动率曲面-多语言表 | 5 | [md_intratevol.md](./md_intratevol.md) |
| 40 | `t_md_intratevol_l` | 利率上限波动率曲面-多语言表 | 5 | [md_intratevol_f7.md](./md_intratevol_f7.md) |
| 41 | `t_md_intratevol_wc` | 日历-多选基础资料表 | 3 | [md_intratevol.md](./md_intratevol.md) |
| 42 | `t_md_quote_wc` | 日历-多选基础资料表 | 3 | [md_forexquote.md](./md_forexquote.md) |
| 43 | `t_md_quote_wc_h` | 日历-多选基础资料表 | 3 | [md_forexquote_h.md](./md_forexquote_h.md) |
| 44 | `t_md_ratevol_ft` | 金融工具-子表 | 16 | [md_intratevol.md](./md_intratevol.md) |
| 45 | `t_md_ratevol_st` | 结构-子表 | 7 | [md_intratevol.md](./md_intratevol.md) |
| 46 | `t_md_scheduleplan` | 调度计划-主表 | 17 | [md_scheduleplan.md](./md_scheduleplan.md) |
| 47 | `t_md_setblpfield` | 彭博field初始化-主表 | 0 | [md_setblpfield.md](./md_setblpfield.md) |
| 48 | `t_md_setblpfield_entry` | 单据体-子表 | 0 | [md_setblpfield.md](./md_setblpfield.md) |
| 49 | `t_md_setblpfield_l` | 彭博field初始化-多语言表 | 0 | [md_setblpfield.md](./md_setblpfield.md) |
| 50 | `t_md_setblpuniverse` | 彭博universe初始化-主表 | 0 | [md_setblpuniverse.md](./md_setblpuniverse.md) |
| 51 | `t_md_setblpuniverse_entry` | 单据体-子表 | 0 | [md_setblpuniverse.md](./md_setblpuniverse.md) |
| 52 | `t_md_setblpuniverse_l` | 彭博universe初始化-多语言表 | 0 | [md_setblpuniverse.md](./md_setblpuniverse.md) |
| 53 | `t_md_yieldline` | 收益率曲线-主表 | 27 | [md_yieldcurve_f7.md](./md_yieldcurve_f7.md) |
| 54 | `t_md_yieldline` | 收益率曲线-主表 | 27 | [md_yieldline.md](./md_yieldline.md) |
| 55 | `t_md_yieldline_fintool` | 单据体-子表 | 21 | [md_yieldcurve_f7.md](./md_yieldcurve_f7.md) |
| 56 | `t_md_yieldline_fintool` | 金融工具单据体-子表 | 21 | [md_yieldline.md](./md_yieldline.md) |
| 57 | `t_md_yieldline_l` | 收益率曲线-多语言表 | 5 | [md_yieldcurve_f7.md](./md_yieldcurve_f7.md) |
| 58 | `t_md_yieldline_l` | 收益率曲线-多语言表 | 5 | [md_yieldline.md](./md_yieldline.md) |
| 59 | `t_md_yieldline_wc` | 日历-多选基础资料表 | 3 | [md_yieldcurve_f7.md](./md_yieldcurve_f7.md) |
| 60 | `t_md_yieldline_wc` | 日历-多选基础资料表 | 3 | [md_yieldline.md](./md_yieldline.md) |
