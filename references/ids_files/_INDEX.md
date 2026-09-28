# ids 模块表清单

> 本模块共收录 **45** 张表定义，来自 `ids_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope ids
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ids_associate_scheme` | 业务关联方案-主表 | 21 | [ids_biz_associate_scheme.md](./ids_biz_associate_scheme.md) |
| 2 | `t_ids_associate_scheme_l` | 业务关联方案-多语言表 | 4 | [ids_biz_associate_scheme.md](./ids_biz_associate_scheme.md) |
| 3 | `t_ids_entity_field` | 业务对象字段-主表 | 6 | [ids_entity_field.md](./ids_entity_field.md) |
| 4 | `t_ids_field_mapping_entry` | 单据体-子表 | 6 | [ids_biz_associate_scheme.md](./ids_biz_associate_scheme.md) |
| 5 | `t_ids_gpe_attachment` | 附件-主表 | 13 | [ids_gpe_attachment.md](./ids_gpe_attachment.md) |
| 6 | `t_ids_gpe_attachment_l` | 附件-多语言表 | 4 | [ids_gpe_attachment.md](./ids_gpe_attachment.md) |
| 7 | `t_ids_gpe_biz_request` | 业务请求记录-主表 | 15 | [ids_gpe_biz_request.md](./ids_gpe_biz_request.md) |
| 8 | `t_ids_gpe_biztrans_field` | 单据体-子表 | 5 | [ids_gpe_biz_trans_scheme.md](./ids_gpe_biz_trans_scheme.md) |
| 9 | `t_ids_gpe_biztrans_scheme` | 结果下推方案-主表 | 14 | [ids_gpe_biz_trans_scheme.md](./ids_gpe_biz_trans_scheme.md) |
| 10 | `t_ids_gpe_biztrans_scheme_l` | 结果下推方案-多语言表 | 4 | [ids_gpe_biz_trans_scheme.md](./ids_gpe_biz_trans_scheme.md) |
| 11 | `t_ids_gpe_dataset` | 数据集-主表 | 27 | [ids_gpe_dataset.md](./ids_gpe_dataset.md) |
| 12 | `t_ids_gpe_dataset_l` | 数据集-多语言表 | 4 | [ids_gpe_dataset.md](./ids_gpe_dataset.md) |
| 13 | `t_ids_gpe_datasource` | 数据源-主表 | 17 | [ids_gpe_datasource.md](./ids_gpe_datasource.md) |
| 14 | `t_ids_gpe_datasource_l` | 数据源-多语言表 | 4 | [ids_gpe_datasource.md](./ids_gpe_datasource.md) |
| 15 | `t_ids_gpe_predict_record` | 预测结果-主表 | 18 | [ids_gpe_predict_record.md](./ids_gpe_predict_record.md) |
| 16 | `t_ids_gpe_predict_record_l` | 预测结果-多语言表 | 4 | [ids_gpe_predict_record.md](./ids_gpe_predict_record.md) |
| 17 | `t_ids_gpe_scheme` | 预测模型方案-主表 | 29 | [ids_gpe_scheme.md](./ids_gpe_scheme.md) |
| 18 | `t_ids_gpe_scheme_l` | 预测模型方案-多语言表 | 4 | [ids_gpe_scheme.md](./ids_gpe_scheme.md) |
| 19 | `t_ids_mark_outlier_tag` | 数据标签-主表 | 12 | [ids_mark_outlier_tag.md](./ids_mark_outlier_tag.md) |
| 20 | `t_ids_mark_outlier_tag_l` | 数据标签-多语言表 | 4 | [ids_mark_outlier_tag.md](./ids_mark_outlier_tag.md) |
| 21 | `t_ids_mservice_method` | 微服务方法-主表 | 0 | [ids_mservice_method.md](./ids_mservice_method.md) |
| 22 | `t_ids_mservice_method_l` | 微服务方法-多语言表 | 0 | [ids_mservice_method.md](./ids_mservice_method.md) |
| 23 | `t_ids_mservice_method_par` | 单据体-方法入参-子表 | 0 | [ids_mservice_method.md](./ids_mservice_method.md) |
| 24 | `t_ids_mservice_paras` | 子单据体-方法入参-子表 | 0 | [ids_mservice_test_case.md](./ids_mservice_test_case.md) |
| 25 | `t_ids_mservice_scene` | 单据体-调用场景-子表 | 0 | [ids_mservice_test_case.md](./ids_mservice_test_case.md) |
| 26 | `t_ids_mservice_service` | 微服务-主表 | 0 | [ids_mservice_service.md](./ids_mservice_service.md) |
| 27 | `t_ids_mservice_service_l` | 微服务-多语言表 | 0 | [ids_mservice_service.md](./ids_mservice_service.md) |
| 28 | `t_ids_mservice_test_case` | 微服务测试用例-主表 | 0 | [ids_mservice_test_case.md](./ids_mservice_test_case.md) |
| 29 | `t_ids_new_product` | 新品对应表-主表 | 20 | [ids_new_product.md](./ids_new_product.md) |
| 30 | `t_ids_new_product_exit` | 退出新品表-主表 | 5 | [ids_new_product_exit.md](./ids_new_product_exit.md) |
| 31 | `t_ids_ns_predict_scheme` | 新品实时预测-主表 | 18 | [ids_ns_predict_scheme.md](./ids_ns_predict_scheme.md) |
| 32 | `t_ids_perm_org` | 预测明细（数据权限使用）-主表 | 2 | [ids_predict_detail_l_perm.md](./ids_predict_detail_l_perm.md) |
| 33 | `t_ids_predict_detail` | 预测明细（废弃）-主表 | 14 | [ids_predict_detail.md](./ids_predict_detail.md) |
| 34 | `t_ids_req_indicator_entry` | 统计指标单据体-子表 | 30 | [ids_requireplan_entry.md](./ids_requireplan_entry.md) |
| 35 | `t_ids_requireplan` | 需求计划单-主表 | 16 | [ids_requireplan.md](./ids_requireplan.md) |
| 36 | `t_ids_requireplan_entry` | 需求计划单明细-主表 | 14 | [ids_requireplan_entry.md](./ids_requireplan_entry.md) |
| 37 | `t_ids_result` | 智能销售预测-预测数据-主表 | 14 | [ids_result_all.md](./ids_result_all.md) |
| 38 | `t_ids_salesplan` | 销售计划单-主表 | 19 | [ids_salesplan.md](./ids_salesplan.md) |
| 39 | `t_ids_salesplan_entry` | 明细信息-子表 | 12 | [ids_salesplan.md](./ids_salesplan.md) |
| 40 | `t_ids_salesplan_indicator` | 预测信息-子表 | 16 | [ids_salesplan.md](./ids_salesplan.md) |
| 41 | `t_ids_salesplan_period` | 销售计划周期-主表 | 12 | [ids_salesplan_period.md](./ids_salesplan_period.md) |
| 42 | `t_ids_salesplan_period_l` | 销售计划周期-多语言表 | 4 | [ids_salesplan_period.md](./ids_salesplan_period.md) |
| 43 | `t_ids_salesplan_push_his` | 销售计划单下推记录-主表 | 5 | [ids_salesplan_push_his.md](./ids_salesplan_push_his.md) |
| 44 | `t_ids_sf_scheme` | 预测方案-主表 | 12 | [ids_sf_scheme.md](./ids_sf_scheme.md) |
| 45 | `t_ids_sf_scheme_l` | 预测方案-多语言表 | 4 | [ids_sf_scheme.md](./ids_sf_scheme.md) |
