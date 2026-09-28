# devgptas 模块表清单

> 本模块共收录 **54** 张表定义，来自 `devgptas_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category devgptas
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `communityflow` | （废弃）用户流水-主表 | 0 | [community_user_flow.md](./community_user_flow.md) |
| 2 | `communityflowlist` | 单据体-子表 | 0 | [community_user_flow.md](./community_user_flow.md) |
| 3 | `communityuserlimit` | 用户额度表-主表 | 0 | [community_user_limit.md](./community_user_limit.md) |
| 4 | `communityuserlimit_l` | 用户额度表-多语言表 | 0 | [community_user_limit.md](./community_user_limit.md) |
| 5 | `t_article_segment` | 分块信息-子表 | 9 | [knl_corpus.md](./knl_corpus.md) |
| 6 | `t_comm_consume` | 消费记录-主表 | 15 | [bos_comm_consume.md](./bos_comm_consume.md) |
| 7 | `t_comm_consume_l` | 消费记录-多语言表 | 4 | [bos_comm_consume.md](./bos_comm_consume.md) |
| 8 | `t_comm_recharge_record` | 充值记录-主表 | 13 | [bos_comm_recharge_record.md](./bos_comm_recharge_record.md) |
| 9 | `t_comm_recharge_record_l` | 充值记录-多语言表 | 4 | [bos_comm_recharge_record.md](./bos_comm_recharge_record.md) |
| 10 | `t_comm_user` | 社区用户-主表 | 18 | [bos_comm_user.md](./bos_comm_user.md) |
| 11 | `t_comm_user_l` | 社区用户-多语言表 | 4 | [bos_comm_user.md](./bos_comm_user.md) |
| 12 | `t_community_user` | （废弃）社区用户-主表 | 0 | [community_user.md](./community_user.md) |
| 13 | `t_community_user_l` | （废弃）社区用户-多语言表 | 0 | [community_user.md](./community_user.md) |
| 14 | `t_corpus_assistant` | 开发助手-主表 | 17 | [bos_corpus_assistant.md](./bos_corpus_assistant.md) |
| 15 | `t_corpus_assistant_l` | 开发助手-多语言表 | 5 | [bos_corpus_assistant.md](./bos_corpus_assistant.md) |
| 16 | `t_corpus_assistant_libs` | 知识库-多选基础资料表 | 3 | [bos_corpus_assistant.md](./bos_corpus_assistant.md) |
| 17 | `t_corpus_libs` | 知识库设置-主表 | 50 | [bos_knl_kmconfig.md](./bos_knl_kmconfig.md) |
| 18 | `t_corpus_libs` | 知识管理-主表 | 50 | [corpus_libs.md](./corpus_libs.md) |
| 19 | `t_corpus_libs_l` | 知识库设置-多语言表 | 5 | [bos_knl_kmconfig.md](./bos_knl_kmconfig.md) |
| 20 | `t_corpus_libs_l` | 知识管理-多语言表 | 5 | [corpus_libs.md](./corpus_libs.md) |
| 21 | `t_corpus_question` | 预置问题分录-子表 | 5 | [bos_corpus_assistant.md](./bos_corpus_assistant.md) |
| 22 | `t_corpus_skill` | 技能管理-主表 | 17 | [bos_skillcorpus.md](./bos_skillcorpus.md) |
| 23 | `t_corpus_skill_l` | 技能管理-多语言表 | 5 | [bos_skillcorpus.md](./bos_skillcorpus.md) |
| 24 | `t_corpus_skillconf` | 技能配置-子表 | 5 | [bos_corpus_assistant.md](./bos_corpus_assistant.md) |
| 25 | `t_corpus_type` | 语料知识库类型-主表 | 10 | [corpus_lib_type.md](./corpus_lib_type.md) |
| 26 | `t_corpus_type_l` | 语料知识库类型-多语言表 | 4 | [corpus_lib_type.md](./corpus_lib_type.md) |
| 27 | `t_gptas_emedctlonfig` | 嵌入式控件技能组配置-主表 | 6 | [bos_emedctlconfig.md](./bos_emedctlconfig.md) |
| 28 | `t_gptas_ideaplugin` | IDEA插件版本管理-主表 | 13 | [bos_comm_ide_version.md](./bos_comm_ide_version.md) |
| 29 | `t_knl_corpus` | 知识语料-主表 | 28 | [knl_corpus.md](./knl_corpus.md) |
| 30 | `t_knl_corpus_l` | 知识语料-多语言表 | 4 | [knl_corpus.md](./knl_corpus.md) |
| 31 | `t_knl_datasource` | 数据来源-主表 | 10 | [knl_datasource.md](./knl_datasource.md) |
| 32 | `t_knl_datasource_l` | 数据来源-多语言表 | 4 | [knl_datasource.md](./knl_datasource.md) |
| 33 | `t_knl_embcache` | 嵌入向量缓存-主表 | 6 | [bos_knl_embcache.md](./bos_knl_embcache.md) |
| 34 | `t_knl_group` | 知识分组-主表 | 15 | [knl_group.md](./knl_group.md) |
| 35 | `t_knl_group_l` | 知识分组-多语言表 | 5 | [knl_group.md](./knl_group.md) |
| 36 | `t_knl_metadata_des` | 元数据描述-主表 | 17 | [bos_metadata_desc.md](./bos_metadata_desc.md) |
| 37 | `t_knl_metadata_des_l` | 元数据描述-多语言表 | 6 | [bos_metadata_desc.md](./bos_metadata_desc.md) |
| 38 | `t_knl_metadata_group` | 元数据描述分组-主表 | 14 | [bos_metadata_group.md](./bos_metadata_group.md) |
| 39 | `t_knl_metadata_group_l` | 元数据描述分组-多语言表 | 5 | [bos_metadata_group.md](./bos_metadata_group.md) |
| 40 | `t_knl_metadata_prop` | 元素信息-子表 | 16 | [bos_metadata_desc.md](./bos_metadata_desc.md) |
| 41 | `t_knl_metadata_prop_l` | 元素信息-多语言表 | 5 | [bos_metadata_desc.md](./bos_metadata_desc.md) |
| 42 | `t_knl_qaresult` | 问答反馈-主表 | 24 | [bos_qaresult.md](./bos_qaresult.md) |
| 43 | `t_knl_qaresultentry` | 单据体-子表 | 7 | [bos_qaresult.md](./bos_qaresult.md) |
| 44 | `t_knl_qarstanal` | 反馈分析类型-主表 | 11 | [bos_qaresultanalyse.md](./bos_qaresultanalyse.md) |
| 45 | `t_knl_qarstanal_l` | 反馈分析类型-多语言表 | 5 | [bos_qaresultanalyse.md](./bos_qaresultanalyse.md) |
| 46 | `t_knl_qarstanalgrp` | 反馈分析类型分组-主表 | 14 | [bos_qaresultanalyse_group.md](./bos_qaresultanalyse_group.md) |
| 47 | `t_knl_qarstanalgrp_l` | 反馈分析类型分组-多语言表 | 5 | [bos_qaresultanalyse_group.md](./bos_qaresultanalyse_group.md) |
| 48 | `t_knl_type` | 知识类型-主表 | 10 | [knl_type.md](./knl_type.md) |
| 49 | `t_knl_type_l` | 知识类型-多语言表 | 4 | [knl_type.md](./knl_type.md) |
| 50 | `t_qa_knl` | 单据体-子表 | 0 | [bos_qarecord.md](./bos_qarecord.md) |
| 51 | `t_qa_record` | 问答记录-主表 | 0 | [bos_qarecord.md](./bos_qarecord.md) |
| 52 | `t_skill_group` | 技能语料分组-主表 | 14 | [bos_skillcorpus_group.md](./bos_skillcorpus_group.md) |
| 53 | `t_skill_group_l` | 技能语料分组-多语言表 | 5 | [bos_skillcorpus_group.md](./bos_skillcorpus_group.md) |
| 54 | `t_userbehavior` | 用户行为数据-主表 | 0 | [bos_gptas_userbehavior.md](./bos_gptas_userbehavior.md) |
