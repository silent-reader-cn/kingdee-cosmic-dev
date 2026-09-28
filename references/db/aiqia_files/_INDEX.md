# aiqia 模块表清单

> 本模块共收录 **21** 张表定义，来自 `aiqia_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category aiqia
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aiqa_avgprice_cusmats` | 客户物料均值价格-主表 | 13 | [aiqa_avgprice_cusmats.md](./aiqa_avgprice_cusmats.md) |
| 2 | `t_aiqa_config` | 配置页面-主表 | 18 | [aiqa_config.md](./aiqa_config.md) |
| 3 | `t_aiqa_conversation` | AI报价会话-主表 | 17 | [aiqa_conversation.md](./aiqa_conversation.md) |
| 4 | `t_aiqa_conversation_me` | 单据体-子表 | 18 | [aiqa_conversation.md](./aiqa_conversation.md) |
| 5 | `t_aiqa_goodsentry` | 单据体-子表 | 5 | [aiqa_goodsinfo.md](./aiqa_goodsinfo.md) |
| 6 | `t_aiqa_goodsinfo` | 物料商品信息-主表 | 14 | [aiqa_goodsinfo.md](./aiqa_goodsinfo.md) |
| 7 | `t_aiqa_goodsinfo_l` | 物料商品信息-多语言表 | 4 | [aiqa_goodsinfo.md](./aiqa_goodsinfo.md) |
| 8 | `t_aiqa_his_price_task_log` | 历史价格计算任务跟进表-主表 | 18 | [aiqa_his_price_task_log.md](./aiqa_his_price_task_log.md) |
| 9 | `t_aiqa_prequote` | 预报价单-主表 | 17 | [aiqa_prequote.md](./aiqa_prequote.md) |
| 10 | `t_aiqa_prequoteentry` | 物料明细-子表 | 21 | [aiqa_prequote.md](./aiqa_prequote.md) |
| 11 | `t_aiqa_rag_sync_config` | 向量同步配置-主表 | 23 | [aiqa_sync_config.md](./aiqa_sync_config.md) |
| 12 | `t_aiqa_rag_sync_config_l` | 向量同步配置-多语言表 | 4 | [aiqa_sync_config.md](./aiqa_sync_config.md) |
| 13 | `t_aiqa_ragconfig` | RAG配置-主表 | 21 | [aiqa_ragconfig.md](./aiqa_ragconfig.md) |
| 14 | `t_aiqa_ragconfig_l` | RAG配置-多语言表 | 4 | [aiqa_ragconfig.md](./aiqa_ragconfig.md) |
| 15 | `t_aiqa_synclog` | 多模态同步日志-主表 | 16 | [aiqa_synclog.md](./aiqa_synclog.md) |
| 16 | `t_aiqa_tenant` | 租户地址-主表 | 13 | [aiqa_tenant_url.md](./aiqa_tenant_url.md) |
| 17 | `t_aiqa_vector_sync` | 多模态向量同步-主表 | 17 | [aiqa_vector_sync.md](./aiqa_vector_sync.md) |
| 18 | `t_aiqa_vector_sync_l` | 多模态向量同步-多语言表 | 5 | [aiqa_vector_sync.md](./aiqa_vector_sync.md) |
| 19 | `t_knowledge_chunk` | 知识库分块-主表 | 0 | [aiqa_knowledge_chunk.md](./aiqa_knowledge_chunk.md) |
| 20 | `t_knowledge_file` | 知识库文件-主表 | 0 | [aiqa_knowledge_file.md](./aiqa_knowledge_file.md) |
| 21 | `t_knowledge_info` | 知识库基础信息-主表 | 0 | [aiqa_knowledge_info.md](./aiqa_knowledge_info.md) |
