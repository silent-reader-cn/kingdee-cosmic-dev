# ocrpos 模块表清单

> 本模块共收录 **16** 张表定义，来自 `ocrpos_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope ocrpos
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ocrpos_fx_define` | 商城框架模板-主表 | 16 | [ocrpos_framework_define.md](./ocrpos_framework_define.md) |
| 2 | `t_ocrpos_fx_define_l` | 商城框架模板-多语言表 | 4 | [ocrpos_framework_define.md](./ocrpos_framework_define.md) |
| 3 | `t_ocrpos_ltpageset` | B2B商城微页面配置-主表 | 10 | [ocrpos_lightpageset.md](./ocrpos_lightpageset.md) |
| 4 | `t_ocrpos_ltpageset_e` | 组件类型明细-子表 | 8 | [ocrpos_lightpageset.md](./ocrpos_lightpageset.md) |
| 5 | `t_ocrpos_ltpageset_e_l` | 组件类型明细-多语言表 | 4 | [ocrpos_lightpageset.md](./ocrpos_lightpageset.md) |
| 6 | `t_ocrpos_ltpageset_l` | B2B商城微页面配置-多语言表 | 4 | [ocrpos_lightpageset.md](./ocrpos_lightpageset.md) |
| 7 | `t_ocrpos_ltpageset_p` | 发布组件类型明细-子表 | 8 | [ocrpos_lightpageset.md](./ocrpos_lightpageset.md) |
| 8 | `t_ocrpos_ltpageset_p_l` | 发布组件类型明细-多语言表 | 4 | [ocrpos_lightpageset.md](./ocrpos_lightpageset.md) |
| 9 | `t_ocrpos_moduledata` | 商城组件数据规则-主表 | 11 | [ocrpos_moduledata.md](./ocrpos_moduledata.md) |
| 10 | `t_ocrpos_moduledata_l` | 商城组件数据规则-多语言表 | 4 | [ocrpos_moduledata.md](./ocrpos_moduledata.md) |
| 11 | `t_ocrpos_moduledata_mt` | 组件类型-多选基础资料表 | 3 | [ocrpos_moduledata.md](./ocrpos_moduledata.md) |
| 12 | `t_ocrpos_moduletype` | 商城组件类型-主表 | 14 | [ocrpos_moduletype.md](./ocrpos_moduletype.md) |
| 13 | `t_ocrpos_moduletype_l` | 商城组件类型-多语言表 | 4 | [ocrpos_moduletype.md](./ocrpos_moduletype.md) |
| 14 | `t_ocrpos_navbar` | B2B商城导航设置-主表 | 22 | [ocrpos_mall_navbar.md](./ocrpos_mall_navbar.md) |
| 15 | `t_ocrpos_navbar_l` | B2B商城导航设置-多语言表 | 5 | [ocrpos_mall_navbar.md](./ocrpos_mall_navbar.md) |
| 16 | `t_ocrpos_navbar_p` | 自定义参数单据体-子表 | 5 | [ocrpos_mall_navbar.md](./ocrpos_mall_navbar.md) |
