# note 模块表清单

> 本模块共收录 **48** 张表定义，来自 `note_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category note
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aqap_code_less` | 银行接口配置管理-主表 | 30 | [ebg_code_less.md](./ebg_code_less.md) |
| 2 | `t_aqap_code_less_l` | 银行接口配置管理-多语言表 | 4 | [ebg_code_less.md](./ebg_code_less.md) |
| 3 | `t_ebg_page_entity` | 分页方案单据体-子表 | 6 | [ebg_page_scheme.md](./ebg_page_scheme.md) |
| 4 | `t_ebg_page_param` | 分页参数类型-主表 | 10 | [ebg_page_param.md](./ebg_page_param.md) |
| 5 | `t_ebg_page_param_l` | 分页参数类型-多语言表 | 4 | [ebg_page_param.md](./ebg_page_param.md) |
| 6 | `t_ebg_page_scheme` | 分页方案-主表 | 14 | [ebg_page_scheme.md](./ebg_page_scheme.md) |
| 7 | `t_ebg_page_scheme_l` | 分页方案-多语言表 | 4 | [ebg_page_scheme.md](./ebg_page_scheme.md) |
| 8 | `t_lastpage_entity` | 最后一页单据体-子表 | 5 | [ebg_code_less.md](./ebg_code_less.md) |
| 9 | `t_nextpage_entity` | 下一页设置单据体-子表 | 4 | [ebg_code_less.md](./ebg_code_less.md) |
| 10 | `t_note_bank_app_list` | 银行应用列表-主表 | 14 | [note_bank_app_list.md](./note_bank_app_list.md) |
| 11 | `t_note_bank_app_list_l` | 银行应用列表-多语言表 | 5 | [note_bank_app_list.md](./note_bank_app_list.md) |
| 12 | `t_note_codeless_bodyentry` | 请求体单据体-子表 | 17 | [ebg_code_less.md](./ebg_code_less.md) |
| 13 | `t_note_codeless_filecont` | 文件上传内容单据体-子表 | 13 | [ebg_code_less.md](./ebg_code_less.md) |
| 14 | `t_note_codeless_fileentry` | 文件上传请求体单据体-子表 | 16 | [ebg_code_less.md](./ebg_code_less.md) |
| 15 | `t_note_codeless_filename` | 文件名组成单据体-子表 | 12 | [ebg_code_less.md](./ebg_code_less.md) |
| 16 | `t_note_codeless_headerent` | 请求头单据体-子表 | 6 | [ebg_code_less.md](./ebg_code_less.md) |
| 17 | `t_note_codeless_rspbody` | 响应体单据体-子表 | 13 | [ebg_code_less.md](./ebg_code_less.md) |
| 18 | `t_note_codeless_type` | 低代码业务类型-主表 | 11 | [note_codeless_type.md](./note_codeless_type.md) |
| 19 | `t_note_codeless_type_l` | 低代码业务类型-多语言表 | 4 | [note_codeless_type.md](./note_codeless_type.md) |
| 20 | `t_note_ebg_field` | 银企属性-主表 | 12 | [note_ebg_field.md](./note_ebg_field.md) |
| 21 | `t_note_ebg_field_l` | 银企属性-多语言表 | 4 | [note_ebg_field.md](./note_ebg_field.md) |
| 22 | `t_note_ebg_field_type` | 银企属性类型-主表 | 10 | [note_ebg_field_type.md](./note_ebg_field_type.md) |
| 23 | `t_note_ebg_field_type_l` | 银企属性类型-多语言表 | 4 | [note_ebg_field_type.md](./note_ebg_field_type.md) |
| 24 | `t_note_inner_rspcode` | 内层响应码单据体-子表 | 6 | [ebg_code_less.md](./ebg_code_less.md) |
| 25 | `t_note_judging_body` | 单据体-子表 | 14 | [ebg_judging_condition.md](./ebg_judging_condition.md) |
| 26 | `t_note_judging_condition` | 匹配规则-主表 | 17 | [ebg_judging_condition.md](./ebg_judging_condition.md) |
| 27 | `t_note_judging_condition_l` | 匹配规则-多语言表 | 4 | [ebg_judging_condition.md](./ebg_judging_condition.md) |
| 28 | `t_note_judging_conditions` | 匹配规则集合-主表 | 14 | [ebg_judging_conditions.md](./ebg_judging_conditions.md) |
| 29 | `t_note_judging_conditions_l` | 匹配规则集合-多语言表 | 4 | [ebg_judging_conditions.md](./ebg_judging_conditions.md) |
| 30 | `t_note_judgings` | 规则集合匹配时取值单据体-子表 | 13 | [ebg_judging_conditions.md](./ebg_judging_conditions.md) |
| 31 | `t_note_judgings_n` | 规则集合不匹配时取值单据体-子表 | 10 | [ebg_judging_conditions.md](./ebg_judging_conditions.md) |
| 32 | `t_note_out_rspcode` | 外层响应码单据体-子表 | 6 | [ebg_code_less.md](./ebg_code_less.md) |
| 33 | `t_note_payable` | 应付票据交易记录-主表 | 144 | [note_payable.md](./note_payable.md) |
| 34 | `t_note_payable_l` | 应付票据交易记录-多语言表 | 4 | [note_payable.md](./note_payable.md) |
| 35 | `t_note_receivable` | 应收票据交易记录-主表 | 155 | [note_receivable.md](./note_receivable.md) |
| 36 | `t_note_receivable_l` | 应收票据交易记录-多语言表 | 4 | [note_receivable.md](./note_receivable.md) |
| 37 | `t_note_route_manage` | 银行接口路由-主表 | 14 | [note_route_manage.md](./note_route_manage.md) |
| 38 | `t_note_route_manage_l` | 银行接口路由-多语言表 | 4 | [note_route_manage.md](./note_route_manage.md) |
| 39 | `t_note_route_type` | 路由类型-主表 | 12 | [note_route_type.md](./note_route_type.md) |
| 40 | `t_note_route_type_l` | 路由类型-多语言表 | 4 | [note_route_type.md](./note_route_type.md) |
| 41 | `t_note_routes` | 业务接口调用集合单据体-子表 | 9 | [note_route_manage.md](./note_route_manage.md) |
| 42 | `t_note_routes_query` | 同步接口调用集合单据体-子表 | 9 | [note_route_manage.md](./note_route_manage.md) |
| 43 | `t_note_sim_endorse` | 背面信息-主表 | 19 | [note_sim_endorse.md](./note_sim_endorse.md) |
| 44 | `t_note_sim_endorse_l` | 背面信息-多语言表 | 4 | [note_sim_endorse.md](./note_sim_endorse.md) |
| 45 | `t_note_sim_hold` | 持票信息-主表 | 17 | [note_sim_hold.md](./note_sim_hold.md) |
| 46 | `t_note_sim_hold_l` | 持票信息-多语言表 | 4 | [note_sim_hold.md](./note_sim_hold.md) |
| 47 | `t_note_sim_reply` | 待签收信息-主表 | 18 | [note_sim_reply.md](./note_sim_reply.md) |
| 48 | `t_note_sim_reply_l` | 待签收信息-多语言表 | 4 | [note_sim_reply.md](./note_sim_reply.md) |
