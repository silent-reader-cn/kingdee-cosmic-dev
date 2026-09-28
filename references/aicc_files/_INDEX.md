# aicc 模块表清单

> 本模块共收录 **17** 张表定义，来自 `aicc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope aicc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aicc_agent_service` | Agent服务-主表 | 21 | [aicc_agent_service.md](./aicc_agent_service.md) |
| 2 | `t_aicc_agent_service_l` | Agent服务-多语言表 | 4 | [aicc_agent_service.md](./aicc_agent_service.md) |
| 3 | `t_aicc_agent_service_u` | Agent服务-使用范围表 | 3 | [aicc_agent_service.md](./aicc_agent_service.md) |
| 4 | `t_aicc_config` | 配置信息-主表 | 14 | [aicc_config.md](./aicc_config.md) |
| 5 | `t_aicc_config_l` | 配置信息-多语言表 | 4 | [aicc_config.md](./aicc_config.md) |
| 6 | `t_aicc_instance` | 算法部署实例-主表 | 20 | [aicc_instance.md](./aicc_instance.md) |
| 7 | `t_aicc_instance_l` | 算法部署实例-多语言表 | 4 | [aicc_instance.md](./aicc_instance.md) |
| 8 | `t_aicc_llm` | 基础大模型-主表 | 22 | [aicc_llm.md](./aicc_llm.md) |
| 9 | `t_aicc_llm_l` | 基础大模型-多语言表 | 4 | [aicc_llm.md](./aicc_llm.md) |
| 10 | `t_aicc_service` | 算法服务-主表 | 20 | [aicc_service.md](./aicc_service.md) |
| 11 | `t_aicc_service_l` | 算法服务-多语言表 | 4 | [aicc_service.md](./aicc_service.md) |
| 12 | `t_aicc_servicetype` | 算法服务—类型-主表 | 10 | [aicc_servicetype.md](./aicc_servicetype.md) |
| 13 | `t_aicc_servicetype_l` | 算法服务—类型-多语言表 | 4 | [aicc_servicetype.md](./aicc_servicetype.md) |
| 14 | `t_aicc_task` | 算法任务-主表 | 16 | [aicc_task.md](./aicc_task.md) |
| 15 | `t_aicc_task_history` | 任务执行历史-主表 | 5 | [aicc_task_history.md](./aicc_task_history.md) |
| 16 | `t_aicc_tenant` | 服务租户-主表 | 14 | [aicc_tenant.md](./aicc_tenant.md) |
| 17 | `t_aicc_tenant_l` | 服务租户-多语言表 | 4 | [aicc_tenant.md](./aicc_tenant.md) |
