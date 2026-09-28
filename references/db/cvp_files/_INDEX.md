# cvp 模块表清单

> 本模块共收录 **37** 张表定义，来自 `cvp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category cvp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cvp_api_invoke_info` | ocr识别API调用详情-主表 | 13 | [cvp_api_invoke_info.md](./cvp_api_invoke_info.md) |
| 2 | `t_cvp_classifier_config` | 单据体-子表 | 7 | [cvp_cls_info.md](./cvp_cls_info.md) |
| 3 | `t_cvp_classifier_files` | 图片集-附件表 | 3 | [cvp_cls_info.md](./cvp_cls_info.md) |
| 4 | `t_cvp_classifier_info` | 组合识别器-主表 | 14 | [cvp_cls_info.md](./cvp_cls_info.md) |
| 5 | `t_cvp_classifier_info_l` | 组合识别器-多语言表 | 4 | [cvp_cls_info.md](./cvp_cls_info.md) |
| 6 | `t_cvp_cls_push_config` | 组合识别器已发布模版-主表 | 4 | [cvp_cls_push_template.md](./cvp_cls_push_template.md) |
| 7 | `t_cvp_ctie_history` | 复杂文档提取历史记录-主表 | 21 | [cvp_ctie_history.md](./cvp_ctie_history.md) |
| 8 | `t_cvp_deliv_cargo_details` | 货物明细-子表 | 0 | [cvp_delivery_note.md](./cvp_delivery_note.md) |
| 9 | `t_cvp_delivery_note` | 测试供应链-主表 | 0 | [cvp_delivery_note.md](./cvp_delivery_note.md) |
| 10 | `t_cvp_demo` | 识别演示-主表 | 0 | [cvp_demo.md](./cvp_demo.md) |
| 11 | `t_cvp_demo_l` | 识别演示-多语言表 | 0 | [cvp_demo.md](./cvp_demo.md) |
| 12 | `t_cvp_goods` | 商品单据-主表 | 0 | [cvp_goods.md](./cvp_goods.md) |
| 13 | `t_cvp_ie_extracfield` | -子表 | 9 | [cvp_ie_mouldplan.md](./cvp_ie_mouldplan.md) |
| 14 | `t_cvp_ie_fieldtype` | 提取字段类型-主表 | 11 | [cvp_field_types.md](./cvp_field_types.md) |
| 15 | `t_cvp_ie_fieldtype_l` | 提取字段类型-多语言表 | 4 | [cvp_field_types.md](./cvp_field_types.md) |
| 16 | `t_cvp_ie_history` | 文档提取历史-主表 | 27 | [cvp_ie_history.md](./cvp_ie_history.md) |
| 17 | `t_cvp_ie_mould` | 信息提取方案-主表 | 13 | [cvp_ie_mouldplan.md](./cvp_ie_mouldplan.md) |
| 18 | `t_cvp_ie_mould_l` | 信息提取方案-多语言表 | 4 | [cvp_ie_mouldplan.md](./cvp_ie_mouldplan.md) |
| 19 | `t_cvp_ie_moulds` | 信息提取方案名称-多选基础资料表 | 3 | [cvp_ie_relateconfig.md](./cvp_ie_relateconfig.md) |
| 20 | `t_cvp_ie_relateconfig` | 提取关联设置-主表 | 14 | [cvp_ie_relateconfig.md](./cvp_ie_relateconfig.md) |
| 21 | `t_cvp_order` | 订单-主表 | 0 | [cvp_order.md](./cvp_order.md) |
| 22 | `t_cvp_plan` | 识别关联设置-主表 | 12 | [cvp_plan.md](./cvp_plan.md) |
| 23 | `t_cvp_plan_config` | 方案模板映射配置-主表 | 4 | [cvp_plan_config.md](./cvp_plan_config.md) |
| 24 | `t_cvp_plan_syn_business` | 基础资料同步信息-主表 | 5 | [cvp_plan_syn_business.md](./cvp_plan_syn_business.md) |
| 25 | `t_cvp_plan_template` | 模板名称-多选基础资料表 | 3 | [cvp_plan.md](./cvp_plan.md) |
| 26 | `t_cvp_service_auth_config` | 视觉识别服务配置-主表 | 3 | [cvp_service_auth_config.md](./cvp_service_auth_config.md) |
| 27 | `t_cvp_tda_comparison_task` | 历史对比任务-主表 | 25 | [cvp_tda_task_history.md](./cvp_tda_task_history.md) |
| 28 | `t_cvp_tda_plan` | 差异分析方案-主表 | 15 | [cvp_tda_plan.md](./cvp_tda_plan.md) |
| 29 | `t_cvp_tda_task_image` | 差异分析图片存储-主表 | 9 | [cvp_tda_task_image.md](./cvp_tda_task_image.md) |
| 30 | `t_cvp_tdaplan_diffname` | 单据体-子表 | 5 | [cvp_tda_plan.md](./cvp_tda_plan.md) |
| 31 | `t_cvp_template` | 自定义模板-主表 | 19 | [cvp_template.md](./cvp_template.md) |
| 32 | `t_cvp_template` | 模板基础资料-主表 | 19 | [cvp_template_base.md](./cvp_template_base.md) |
| 33 | `t_cvp_template` | 模版基础资料F7-主表 | 19 | [cvp_template_base_f7.md](./cvp_template_base_f7.md) |
| 34 | `t_cvp_template_config` | OCR模板配置-主表 | 5 | [cvp_template_config.md](./cvp_template_config.md) |
| 35 | `t_cvp_template_l` | 自定义模板-多语言表 | 4 | [cvp_template.md](./cvp_template.md) |
| 36 | `t_cvp_template_l` | 模板基础资料-多语言表 | 4 | [cvp_template_base.md](./cvp_template_base.md) |
| 37 | `t_cvp_template_l` | 模版基础资料F7-多语言表 | 4 | [cvp_template_base_f7.md](./cvp_template_base_f7.md) |
