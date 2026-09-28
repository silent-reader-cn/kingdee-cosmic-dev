# gai 模块表清单

> 本模块共收录 **69** 张表定义，来自 `gai_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category gai
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gai_agent` | 智能体-主表 | 31 | [gai_agent.md](./gai_agent.md) |
| 2 | `t_gai_agent_app` | 应用-多选基础资料表 | 3 | [gai_agent.md](./gai_agent.md) |
| 3 | `t_gai_agent_l` | 智能体-多语言表 | 6 | [gai_agent.md](./gai_agent.md) |
| 4 | `t_gai_agent_process` | 单据体-GPT任务-子表 | 4 | [gai_agent.md](./gai_agent.md) |
| 5 | `t_gai_agent_prompt` | 单据体-GPT提示-子表 | 4 | [gai_agent.md](./gai_agent.md) |
| 6 | `t_gai_agent_repo` | 单据体-知识库-子表 | 4 | [gai_agent.md](./gai_agent.md) |
| 7 | `t_gai_agent_start` | 开场推荐问法-子表 | 4 | [gai_agent.md](./gai_agent.md) |
| 8 | `t_gai_agent_start_l` | 开场推荐问法-多语言表 | 4 | [gai_agent.md](./gai_agent.md) |
| 9 | `t_gai_agent_tool` | 单据体-工具-子表 | 4 | [gai_agent.md](./gai_agent.md) |
| 10 | `t_gai_agent_u` | 智能体-使用范围表 | 3 | [gai_agent.md](./gai_agent.md) |
| 11 | `t_gai_assistant_config` | cosmic助手-主表 | 10 | [gai_gpt_assistant_config.md](./gai_gpt_assistant_config.md) |
| 12 | `t_gai_chat_info` | 历史记录-主表 | 5 | [gai_chat_info.md](./gai_chat_info.md) |
| 13 | `t_gai_chat_info_old` | chat相关信息-主表 | 0 | [gai_chat_info_old.md](./gai_chat_info_old.md) |
| 14 | `t_gai_chat_item` | 历史记录详情-主表 | 6 | [gai_chat_item.md](./gai_chat_item.md) |
| 15 | `t_gai_chat_item_old` | 用户对话历史记录-主表 | 0 | [gai_chat_item_old.md](./gai_chat_item_old.md) |
| 16 | `t_gai_chat_message` | 消息-主表 | 18 | [gai_chat_message.md](./gai_chat_message.md) |
| 17 | `t_gai_chat_msg_feedback` | 消息反馈-主表 | 6 | [gai_chat_msg_feedback.md](./gai_chat_msg_feedback.md) |
| 18 | `t_gai_chat_session` | 会话-主表 | 20 | [gai_chat_session.md](./gai_chat_session.md) |
| 19 | `t_gai_chat_session_l` | 会话-多语言表 | 4 | [gai_chat_session.md](./gai_chat_session.md) |
| 20 | `t_gai_chat_session_u` | 会话-使用范围表 | 3 | [gai_chat_session.md](./gai_chat_session.md) |
| 21 | `t_gai_file` | 文件管理-主表 | 22 | [gai_file.md](./gai_file.md) |
| 22 | `t_gai_file_l` | 文件管理-多语言表 | 4 | [gai_file.md](./gai_file.md) |
| 23 | `t_gai_file_u` | 文件管理-使用范围表 | 3 | [gai_file.md](./gai_file.md) |
| 24 | `t_gai_log` | 监控日志-主表 | 28 | [gai_log.md](./gai_log.md) |
| 25 | `t_gai_log` | 监控日志单据-主表 | 28 | [gai_log_bak.md](./gai_log_bak.md) |
| 26 | `t_gai_log_l` | 监控日志-多语言表 | 4 | [gai_log.md](./gai_log.md) |
| 27 | `t_gai_log_step` | 单据体-子表 | 26 | [gai_log.md](./gai_log.md) |
| 28 | `t_gai_log_step` | 步骤单据体-子表 | 26 | [gai_log_bak.md](./gai_log_bak.md) |
| 29 | `t_gai_log_step_event` | 子单据体-子表 | 20 | [gai_log.md](./gai_log.md) |
| 30 | `t_gai_log_step_event` | 子单据体-子表 | 20 | [gai_log_bak.md](./gai_log_bak.md) |
| 31 | `t_gai_log_u` | 监控日志-使用范围表 | 3 | [gai_log.md](./gai_log.md) |
| 32 | `t_gai_operation` | GPT操作-主表 | 17 | [gai_operation.md](./gai_operation.md) |
| 33 | `t_gai_operation_input` | 输入-子表 | 6 | [gai_operation.md](./gai_operation.md) |
| 34 | `t_gai_operation_l` | GPT操作-多语言表 | 4 | [gai_operation.md](./gai_operation.md) |
| 35 | `t_gai_operation_output` | 输出-子表 | 6 | [gai_operation.md](./gai_operation.md) |
| 36 | `t_gai_piisetting` | PII脱敏配置-主表 | 19 | [gai_piisetting.md](./gai_piisetting.md) |
| 37 | `t_gai_piisetting_l` | PII脱敏配置-多语言表 | 4 | [gai_piisetting.md](./gai_piisetting.md) |
| 38 | `t_gai_piisetting_u` | PII脱敏配置-使用范围表 | 3 | [gai_piisetting.md](./gai_piisetting.md) |
| 39 | `t_gai_preset_var` | 预置变量-主表 | 0 | [gai_preset_var.md](./gai_preset_var.md) |
| 40 | `t_gai_preset_var_l` | 预置变量-多语言表 | 0 | [gai_preset_var.md](./gai_preset_var.md) |
| 41 | `t_gai_process` | 任务流-主表 | 25 | [gai_process.md](./gai_process.md) |
| 42 | `t_gai_process_app` | 应用-多选基础资料表 | 3 | [gai_process.md](./gai_process.md) |
| 43 | `t_gai_process_group` | GPT任务分组-主表 | 22 | [gai_process_group.md](./gai_process_group.md) |
| 44 | `t_gai_process_group_l` | GPT任务分组-多语言表 | 5 | [gai_process_group.md](./gai_process_group.md) |
| 45 | `t_gai_process_group_u` | GPT任务分组-使用范围表 | 3 | [gai_process_group.md](./gai_process_group.md) |
| 46 | `t_gai_process_l` | 任务流-多语言表 | 4 | [gai_process.md](./gai_process.md) |
| 47 | `t_gai_process_u` | 任务流-使用范围表 | 3 | [gai_process.md](./gai_process.md) |
| 48 | `t_gai_prompt` | GPT提示-主表 | 30 | [gai_prompt.md](./gai_prompt.md) |
| 49 | `t_gai_prompt_in_var` | 自定义变量-子表 | 6 | [gai_prompt.md](./gai_prompt.md) |
| 50 | `t_gai_prompt_l` | GPT提示-多语言表 | 4 | [gai_prompt.md](./gai_prompt.md) |
| 51 | `t_gai_prompt_out_var` | 输出变量-子表 | 7 | [gai_prompt.md](./gai_prompt.md) |
| 52 | `t_gai_prompt_repo_config` | 知识库配置-子表 | 7 | [gai_prompt.md](./gai_prompt.md) |
| 53 | `t_gai_prompt_u` | GPT提示-使用范围表 | 3 | [gai_prompt.md](./gai_prompt.md) |
| 54 | `t_gai_repo_doc_manage` | 文档管理-子表 | 16 | [gai_repo_info.md](./gai_repo_info.md) |
| 55 | `t_gai_repo_info` | 知识库-主表 | 18 | [gai_repo_info.md](./gai_repo_info.md) |
| 56 | `t_gai_repo_info_l` | 知识库-多语言表 | 4 | [gai_repo_info.md](./gai_repo_info.md) |
| 57 | `t_gai_run` | 执行-主表 | 27 | [gai_run.md](./gai_run.md) |
| 58 | `t_gai_run_step_entry` | 单据体-执行步骤-子表 | 20 | [gai_run.md](./gai_run.md) |
| 59 | `t_gai_sensitivewords` | 敏感词库-主表 | 21 | [gai_sensitivewords.md](./gai_sensitivewords.md) |
| 60 | `t_gai_sensitivewords_l` | 敏感词库-多语言表 | 4 | [gai_sensitivewords.md](./gai_sensitivewords.md) |
| 61 | `t_gai_sensitivewords_u` | 敏感词库-使用范围表 | 3 | [gai_sensitivewords.md](./gai_sensitivewords.md) |
| 62 | `t_gai_skill` | gai_skill-主表 | 6 | [gai_skill.md](./gai_skill.md) |
| 63 | `t_gai_suggestedask` | 推荐问法-子表 | 4 | [gai_process.md](./gai_process.md) |
| 64 | `t_gai_tenant_agreement` | 租户隐私协议签署状态-主表 | 7 | [gai_tenant_agreement.md](./gai_tenant_agreement.md) |
| 65 | `t_gai_text_chunk` | 文本分块信息-主表 | 16 | [gai_text_chunk.md](./gai_text_chunk.md) |
| 66 | `t_gai_tool` | 插件-主表 | 21 | [gai_tool.md](./gai_tool.md) |
| 67 | `t_gai_tool_l` | 插件-多语言表 | 5 | [gai_tool.md](./gai_tool.md) |
| 68 | `t_gai_tool_u` | 插件-使用范围表 | 3 | [gai_tool.md](./gai_tool.md) |
| 69 | `t_gai_user_agreement` | 用户隐私协议签署状态-主表 | 6 | [gai_user_agreement.md](./gai_user_agreement.md) |
