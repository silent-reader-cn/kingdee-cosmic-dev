# til 模块表清单

> 本模块共收录 **25** 张表定义，来自 `til_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope til
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_rim_inv_collect_org` | 采集组织单据体-子表 | 6 | [til_invoice_list.md](./til_invoice_list.md) |
| 2 | `t_rim_inv_collect_user` | 采集用户单据体-子表 | 7 | [til_invoice_list.md](./til_invoice_list.md) |
| 3 | `t_rim_invoice` | 进项转出发票登记列表-主表 | 75 | [til_invoice_list.md](./til_invoice_list.md) |
| 4 | `t_rim_invoice_a` | 进项转出发票登记列表-分表 | 4 | [til_invoice_list.md](./til_invoice_list.md) |
| 5 | `t_rim_reim_vouch_relation` | 单据和凭证-子表 | 15 | [til_invoice_list.md](./til_invoice_list.md) |
| 6 | `t_tdm_customs_pay_item` | 海关专用缴款书子表明细-子表 | 10 | [til_customs_payment.md](./til_customs_payment.md) |
| 7 | `t_tdm_customs_payment` | 海关专用缴款书单据-主表 | 34 | [til_customs_payment.md](./til_customs_payment.md) |
| 8 | `t_tdm_withholding_items` | 代扣代缴子表明细-子表 | 11 | [til_withholding_tax.md](./til_withholding_tax.md) |
| 9 | `t_tdm_withholding_tax` | 代扣代缴税收缴款凭证单据-主表 | 23 | [til_withholding_tax.md](./til_withholding_tax.md) |
| 10 | `t_til_devide_detail` | 分摊明细-主表 | 16 | [til_devide_detail.md](./til_devide_detail.md) |
| 11 | `t_til_devide_entity` | 单据体-子表 | 7 | [til_devide_detail.md](./til_devide_detail.md) |
| 12 | `t_til_in_transfer_out` | 进项转出手工登记-主表 | 25 | [til_in_transfer_out_bill.md](./til_in_transfer_out_bill.md) |
| 13 | `t_til_in_transfer_out_ent` | 单据体-子表 | 7 | [til_in_transfer_out_bill.md](./til_in_transfer_out_bill.md) |
| 14 | `t_til_invoice_project` | 进项发票项目关系-主表 | 6 | [til_in_invoice_project.md](./til_in_invoice_project.md) |
| 15 | `t_til_jxdk_ncpjsdk` | 农产品计算抵扣单据-主表 | 17 | [til_jxdk_ncpjsdk_bill.md](./til_jxdk_ncpjsdk_bill.md) |
| 16 | `t_til_jxdk_ncpjsdk_entry` | 单据体-子表 | 7 | [til_jxdk_ncpjsdk_bill.md](./til_jxdk_ncpjsdk_bill.md) |
| 17 | `t_til_proportion_bill` | 进项转出比例分摊-主表 | 22 | [til_proportion_bill.md](./til_proportion_bill.md) |
| 18 | `t_til_query_condition_pla` | 查询方案基础资料-主表 | 16 | [til_query_condition_plan.md](./til_query_condition_plan.md) |
| 19 | `t_til_query_condition_pla_l` | 查询方案基础资料-多语言表 | 4 | [til_query_condition_plan.md](./til_query_condition_plan.md) |
| 20 | `t_til_rollout_type_config` | 进项转出映射配置-主表 | 23 | [til_rollout_type_config.md](./til_rollout_type_config.md) |
| 21 | `t_til_rollout_type_config_l` | 进项转出映射配置-多语言表 | 4 | [til_rollout_type_config.md](./til_rollout_type_config.md) |
| 22 | `t_til_rollout_type_config_m` | 进项转出映射配置-使用范围位图表 | 2 | [til_rollout_type_config.md](./til_rollout_type_config.md) |
| 23 | `t_til_rollout_type_config_u` | 进项转出映射配置-使用范围表 | 3 | [til_rollout_type_config.md](./til_rollout_type_config.md) |
| 24 | `t_til_sale` | 视同销售-主表 | 19 | [til_sale.md](./til_sale.md) |
| 25 | `t_til_sale_l` | 视同销售-多语言表 | 5 | [til_sale.md](./til_sale.md) |
