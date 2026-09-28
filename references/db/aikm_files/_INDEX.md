# aikm 模块表清单

> 本模块共收录 **24** 张表定义，来自 `aikm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category aikm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aikm_evaluationtask` | 评测任务单据-主表 | 22 | [aikm_evaluationbill.md](./aikm_evaluationbill.md) |
| 2 | `t_aikm_evaluationtaske` | 单据体-子表 | 22 | [aikm_evaluationbill.md](./aikm_evaluationbill.md) |
| 3 | `t_aikm_genqa_scheme` | 生成QA对方案-主表 | 18 | [aikm_genqa_scheme.md](./aikm_genqa_scheme.md) |
| 4 | `t_aikm_genqa_scheme_l` | 生成QA对方案-多语言表 | 4 | [aikm_genqa_scheme.md](./aikm_genqa_scheme.md) |
| 5 | `t_aikm_knl_manager` | 知识库管理-主表 | 43 | [aikm_knl_manager.md](./aikm_knl_manager.md) |
| 6 | `t_aikm_knl_manager_group` | 知识库分组-主表 | 11 | [aikm_knl_manager_group.md](./aikm_knl_manager_group.md) |
| 7 | `t_aikm_knl_manager_group_l` | 知识库分组-多语言表 | 4 | [aikm_knl_manager_group.md](./aikm_knl_manager_group.md) |
| 8 | `t_aikm_knl_manager_l` | 知识库管理-多语言表 | 4 | [aikm_knl_manager.md](./aikm_knl_manager.md) |
| 9 | `t_aikm_knl_manager_u` | 知识库管理-使用范围表 | 3 | [aikm_knl_manager.md](./aikm_knl_manager.md) |
| 10 | `t_aikm_labelconfig` | 知识库标签设置-主表 | 2 | [aikm_labelconfig.md](./aikm_labelconfig.md) |
| 11 | `t_aikm_labelconfigentry` | 单据体-子表 | 8 | [aikm_labelconfig.md](./aikm_labelconfig.md) |
| 12 | `t_aikm_labeldefine` | 标签定义-主表 | 12 | [aikm_labeldefine.md](./aikm_labeldefine.md) |
| 13 | `t_aikm_labeldefine_l` | 标签定义-多语言表 | 4 | [aikm_labeldefine.md](./aikm_labeldefine.md) |
| 14 | `t_aikm_labelscheme` | 标签方案-主表 | 10 | [aikm_labelscheme.md](./aikm_labelscheme.md) |
| 15 | `t_aikm_labelscheme_l` | 标签方案-多语言表 | 4 | [aikm_labelscheme.md](./aikm_labelscheme.md) |
| 16 | `t_aikm_labelschemeentry` | 单据体-子表 | 4 | [aikm_labelscheme.md](./aikm_labelscheme.md) |
| 17 | `t_aikm_noun_manager` | 名词知识库管理-主表 | 42 | [aikm_nounknl_manager.md](./aikm_nounknl_manager.md) |
| 18 | `t_aikm_noun_manager_l` | 名词知识库管理-多语言表 | 4 | [aikm_nounknl_manager.md](./aikm_nounknl_manager.md) |
| 19 | `t_aikm_noun_manager_u` | 名词知识库管理-使用范围表 | 3 | [aikm_nounknl_manager.md](./aikm_nounknl_manager.md) |
| 20 | `t_aikm_similar_setting` | 检测配置-主表 | 3 | [aikm_similar_setting.md](./aikm_similar_setting.md) |
| 21 | `t_noun_manager_group` | 名词知识库管理分组-主表 | 11 | [aikm_noun_manager_group.md](./aikm_noun_manager_group.md) |
| 22 | `t_noun_manager_group_l` | 名词知识库管理分组-多语言表 | 4 | [aikm_noun_manager_group.md](./aikm_noun_manager_group.md) |
| 23 | `t_repo_configscheme` | 知识库配置方案-主表 | 37 | [aikm_repo_scheme.md](./aikm_repo_scheme.md) |
| 24 | `t_repo_configscheme_l` | 知识库配置方案-多语言表 | 5 | [aikm_repo_scheme.md](./aikm_repo_scheme.md) |
