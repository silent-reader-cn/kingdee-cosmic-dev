# mai 模块表清单

> 本模块共收录 **26** 张表定义，来自 `mai_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category mai
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mai_bizreport` | 经营报告-主表 | 10 | [mai_bizreport.md](./mai_bizreport.md) |
| 2 | `t_mai_bizreportcfg` | 经营报告配置-主表 | 13 | [mai_bizreportcfg.md](./mai_bizreportcfg.md) |
| 3 | `t_mai_bizreportcfg_new` | 经营报告配置-主表 | 17 | [mai_bizreportcfg_new.md](./mai_bizreportcfg_new.md) |
| 4 | `t_mai_bizreportcfg_new_l` | 经营报告配置-多语言表 | 4 | [mai_bizreportcfg_new.md](./mai_bizreportcfg_new.md) |
| 5 | `t_mai_chapter_entry` | 单据体-子表 | 6 | [mai_bizreportcfg_new.md](./mai_bizreportcfg_new.md) |
| 6 | `t_mai_chathistory` | 历史对话-主表 | 5 | [mai_chathistory.md](./mai_chathistory.md) |
| 7 | `t_mai_chathistory_attach` | 历史对话附加详情-主表 | 4 | [mai_chathistory_attach.md](./mai_chathistory_attach.md) |
| 8 | `t_mai_chathistory_d` | 单据体-子表 | 14 | [mai_chathistory.md](./mai_chathistory.md) |
| 9 | `t_mai_favoriteiac` | 企业信息收藏-主表 | 5 | [mai_favoriteiac.md](./mai_favoriteiac.md) |
| 10 | `t_mai_globalconfig` | 全局配置-主表 | 10 | [mai_globalconfig.md](./mai_globalconfig.md) |
| 11 | `t_mai_guideconfig` | 引导语配置-主表 | 12 | [mai_guideconfig.md](./mai_guideconfig.md) |
| 12 | `t_mai_guideconfig_detail` | 单据体-子表 | 8 | [mai_guideconfig.md](./mai_guideconfig.md) |
| 13 | `t_mai_guideconfig_detail_l` | 单据体-多语言表 | 4 | [mai_guideconfig.md](./mai_guideconfig.md) |
| 14 | `t_mai_guideconfig_l` | 引导语配置-多语言表 | 4 | [mai_guideconfig.md](./mai_guideconfig.md) |
| 15 | `t_mai_index_quote_entry` | 指标引用单据体-子表 | 14 | [mai_bizreportcfg_new.md](./mai_bizreportcfg_new.md) |
| 16 | `t_mai_indexanalysis` | 指标分析配置-主表 | 30 | [mai_indexanalysis.md](./mai_indexanalysis.md) |
| 17 | `t_mai_indexanalysis_l` | 指标分析配置-多语言表 | 6 | [mai_indexanalysis.md](./mai_indexanalysis.md) |
| 18 | `t_mai_indextreecfg` | 指标树配置-主表 | 16 | [mai_indextreecfg.md](./mai_indextreecfg.md) |
| 19 | `t_mai_indextype` | 指标分类-主表 | 17 | [mai_indextype.md](./mai_indextype.md) |
| 20 | `t_mai_indextype_l` | 指标分类-多语言表 | 6 | [mai_indextype.md](./mai_indextype.md) |
| 21 | `t_mai_recommend` | 推荐问题-主表 | 4 | [mai_recommend.md](./mai_recommend.md) |
| 22 | `t_mai_reportuser` | 接收用户-多选基础资料表 | 3 | [mai_bizreportcfg_new.md](./mai_bizreportcfg_new.md) |
| 23 | `t_mai_req_entry` | 分析要求-子表 | 6 | [mai_bizreportcfg_new.md](./mai_bizreportcfg_new.md) |
| 24 | `t_mai_sercfg` | 语义规则配置-主表 | 13 | [mai_sercfg.md](./mai_sercfg.md) |
| 25 | `t_mai_sercfg_l` | 语义规则配置-多语言表 | 4 | [mai_sercfg.md](./mai_sercfg.md) |
| 26 | `t_mai_userlang` | 用户语言-主表 | 4 | [mai_userlang.md](./mai_userlang.md) |
