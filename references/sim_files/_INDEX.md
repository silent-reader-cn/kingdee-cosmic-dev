# sim 模块表清单

> 本模块共收录 **87** 张表定义，来自 `sim_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope sim
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bdm_tax_equipment` | 库存管理-主表 | 35 | [sim_stock_management_list.md](./sim_stock_management_list.md) |
| 2 | `t_sim_apply_result` | 申领结果-子表 | 7 | [sim_inv_apply_log.md](./sim_inv_apply_log.md) |
| 3 | `t_sim_async_issue_invoice` | 异步开票临时表-主表 | 5 | [sim_async_issue_invoice.md](./sim_async_issue_invoice.md) |
| 4 | `t_sim_auto_issue_config` | 自动开票单据-主表 | 7 | [sim_auto_issue_config.md](./sim_auto_issue_config.md) |
| 5 | `t_sim_batch` | 待开发票(旧)-主表 | 44 | [sim_batch.md](./sim_batch.md) |
| 6 | `t_sim_batch_e` | 待开发票(旧)-分表 | 16 | [sim_batch.md](./sim_batch.md) |
| 7 | `t_sim_batch_item` | 明细单据体-子表 | 27 | [sim_batch.md](./sim_batch.md) |
| 8 | `t_sim_bill_add_invoice` | 开票申请单回填发票-主表 | 23 | [sim_bill_add_invoice.md](./sim_bill_add_invoice.md) |
| 9 | `t_sim_bill_inv_relation` | 单据发票关系-主表 | 15 | [sim_bill_inv_relation.md](./sim_bill_inv_relation.md) |
| 10 | `t_sim_bill_relation` | 单据关系表-主表 | 5 | [sim_bill_relation.md](./sim_bill_relation.md) |
| 11 | `t_sim_bill_trans` | 转换单据明细(旧)-主表 | 3 | [sim_bill_trans.md](./sim_bill_trans.md) |
| 12 | `t_sim_bill_trans_item` | 单据体-子表 | 8 | [sim_bill_trans.md](./sim_bill_trans.md) |
| 13 | `t_sim_bill_trans_relax` | 单据转换关系实体(旧)-主表 | 5 | [sim_bill_trans_relax.md](./sim_bill_trans_relax.md) |
| 14 | `t_sim_bill_type` | 单据商品类型-主表 | 3 | [sim_bill_type.md](./sim_bill_type.md) |
| 15 | `t_sim_block_chain_config` | 区块链第三方配置-主表 | 12 | [sim_block_chain_config.md](./sim_block_chain_config.md) |
| 16 | `t_sim_bueyer_bill` | 发票购方统计单据-主表 | 9 | [sim_bueyer_bill.md](./sim_bueyer_bill.md) |
| 17 | `t_sim_component_mock` | 组件mock接口-主表 | 0 | [sim_component_mock.md](./sim_component_mock.md) |
| 18 | `t_sim_confirm_bill` | 已确认单据(废弃)-主表 | 50 | [sim_confirm_bill.md](./sim_confirm_bill.md) |
| 19 | `t_sim_confirm_bill_e` | 已确认单据(废弃)-分表 | 5 | [sim_confirm_bill.md](./sim_confirm_bill.md) |
| 20 | `t_sim_confirm_bill_item` | 单据体-子表 | 24 | [sim_confirm_bill.md](./sim_confirm_bill.md) |
| 21 | `t_sim_confirm_bill_item_lk` | 关联子实体-子表 | 14 | [sim_confirm_bill.md](./sim_confirm_bill.md) |
| 22 | `t_sim_confirm_bill_tc` | 已确认单据(废弃)-关联追踪表 | 7 | [sim_confirm_bill.md](./sim_confirm_bill.md) |
| 23 | `t_sim_confirm_bill_wb` | 已确认单据(废弃)-反写记录表 | 10 | [sim_confirm_bill.md](./sim_confirm_bill.md) |
| 24 | `t_sim_confirm_detail_tc` | 单据发票关系(废弃)-主表 | 13 | [sim_confirm_detail_tc.md](./sim_confirm_detail_tc.md) |
| 25 | `t_sim_copy_tax_return` | 抄报税管理-主表 | 10 | [sim_copy_tax_returns.md](./sim_copy_tax_returns.md) |
| 26 | `t_sim_count_check` | 对账汇总-主表 | 16 | [sim_split_count_check.md](./sim_split_count_check.md) |
| 27 | `t_sim_count_check_items` | 单据体-子表 | 9 | [sim_split_count_check.md](./sim_split_count_check.md) |
| 28 | `t_sim_delivery_msg` | 配送信息盒子-子表 | 9 | [sim_inv_apply_log.md](./sim_inv_apply_log.md) |
| 29 | `t_sim_drawer_setting` | 开票方实体-主表 | 9 | [sim_drawer_setting.md](./sim_drawer_setting.md) |
| 30 | `t_sim_fail_auto_issue` | 失败自动重开记录-主表 | 4 | [sim_fail_auto_issue.md](./sim_fail_auto_issue.md) |
| 31 | `t_sim_goods_bill` | 商品统计单据-主表 | 11 | [sim_goods_bill.md](./sim_goods_bill.md) |
| 32 | `t_sim_inv_apply` | 发票领购-主表 | 8 | [sim_inv_apply.md](./sim_inv_apply.md) |
| 33 | `t_sim_inv_apply_detail` | 发票领购详情-主表 | 21 | [sim_inv_apply_detail.md](./sim_inv_apply_detail.md) |
| 34 | `t_sim_inv_apply_log` | 发票申领-主表 | 22 | [sim_inv_apply_log.md](./sim_inv_apply_log.md) |
| 35 | `t_sim_invoice_call_back` | 回调配置-主表 | 7 | [sim_invoice_call_back.md](./sim_invoice_call_back.md) |
| 36 | `t_sim_invoice_setting` | 销方地址电话-主表 | 12 | [sim_invoice_setting.md](./sim_invoice_setting.md) |
| 37 | `t_sim_invoice_sum_data` | 销项发票汇总数据-主表 | 19 | [sim_invoice_sum_data.md](./sim_invoice_sum_data.md) |
| 38 | `t_sim_original_bill` | 开票申请单-主表 | 65 | [sim_original_bill.md](./sim_original_bill.md) |
| 39 | `t_sim_original_bill_e` | 开票申请单-分表 | 73 | [sim_original_bill.md](./sim_original_bill.md) |
| 40 | `t_sim_original_bill_item` | 单据体-子表 | 77 | [sim_original_bill.md](./sim_original_bill.md) |
| 41 | `t_sim_original_bill_item_lk` | 关联子实体-子表 | 10 | [sim_original_bill.md](./sim_original_bill.md) |
| 42 | `t_sim_original_bill_lk` | 关联子实体-子表 | 6 | [sim_original_bill.md](./sim_original_bill.md) |
| 43 | `t_sim_original_bill_tc` | 开票申请单-关联追踪表 | 7 | [sim_original_bill.md](./sim_original_bill.md) |
| 44 | `t_sim_original_bill_wb` | 开票申请单-反写记录表 | 10 | [sim_original_bill.md](./sim_original_bill.md) |
| 45 | `t_sim_reconciliation_item` | 发票信息-子表 | 10 | [sim_reconciliation_sum.md](./sim_reconciliation_sum.md) |
| 46 | `t_sim_reconciliation_sum` | 单据对账-主表 | 16 | [sim_reconciliation_sum.md](./sim_reconciliation_sum.md) |
| 47 | `t_sim_recycle_log` | 发票回收-主表 | 10 | [sim_recycle_log.md](./sim_recycle_log.md) |
| 48 | `t_sim_red_confirm_bill` | 红字确认单（全电发票）-主表 | 43 | [sim_red_confirm_bill.md](./sim_red_confirm_bill.md) |
| 49 | `t_sim_red_confirm_bill_l` | 红字确认单（全电发票）-多语言表 | 4 | [sim_red_confirm_bill.md](./sim_red_confirm_bill.md) |
| 50 | `t_sim_red_confirm_bill_u` | 红字确认单（全电发票）-使用范围表 | 3 | [sim_red_confirm_bill.md](./sim_red_confirm_bill.md) |
| 51 | `t_sim_red_confirm_items` | 单据体-子表 | 16 | [sim_red_confirm_bill.md](./sim_red_confirm_bill.md) |
| 52 | `t_sim_red_info` | 红字信息表-主表 | 65 | [sim_red_info.md](./sim_red_info.md) |
| 53 | `t_sim_red_info_item` | 红字信息表明细-子表 | 21 | [sim_red_info.md](./sim_red_info.md) |
| 54 | `t_sim_redinfo_wf` | 发票审批-主表 | 13 | [sim_redinfo_workflow.md](./sim_redinfo_workflow.md) |
| 55 | `t_sim_redinfo_wf_item` | 单据体-子表 | 20 | [sim_redinfo_workflow.md](./sim_redinfo_workflow.md) |
| 56 | `t_sim_repair_invoice` | 待修复的发票数据-主表 | 6 | [sim_repair_invoice.md](./sim_repair_invoice.md) |
| 57 | `t_sim_rollback_log` | 发票回退-主表 | 11 | [sim_rollback_log.md](./sim_rollback_log.md) |
| 58 | `t_sim_scan_invoice` | 扫码开票-主表 | 16 | [sim_scan_invoice.md](./sim_scan_invoice.md) |
| 59 | `t_sim_split_use` | 拆分方案调用统计-主表 | 5 | [sim_split_use.md](./sim_split_use.md) |
| 60 | `t_sim_status_bill` | 发票状态统计单据-主表 | 16 | [sim_status_bill.md](./sim_status_bill.md) |
| 61 | `t_sim_sync_aws_record` | 公有云数据迁移记录（弃用）-主表 | 13 | [sim_sync_aws_record.md](./sim_sync_aws_record.md) |
| 62 | `t_sim_taxrate_bill` | 税率统计单据-主表 | 8 | [sim_taxrate_bill.md](./sim_taxrate_bill.md) |
| 63 | `t_sim_taxrate_bill_item` | 单据体-子表 | 14 | [sim_taxrate_bill.md](./sim_taxrate_bill.md) |
| 64 | `t_sim_vatinvoice` | 作废重开-主表 | 57 | [sim_invoice_invalid.md](./sim_invoice_invalid.md) |
| 65 | `t_sim_vatinvoice` | 发票作废-主表 | 57 | [sim_invoice_valid_list.md](./sim_invoice_valid_list.md) |
| 66 | `t_sim_vatinvoice` | 待开发票-主表 | 57 | [sim_invoice_wait.md](./sim_invoice_wait.md) |
| 67 | `t_sim_vatinvoice` | 发票红冲(废弃)-主表 | 57 | [sim_red_invoice_list.md](./sim_red_invoice_list.md) |
| 68 | `t_sim_vatinvoice` | 发票查询-主表 | 57 | [sim_vatinvoice.md](./sim_vatinvoice.md) |
| 69 | `t_sim_vatinvoice` | 发票红冲-主表 | 57 | [sim_vatinvoice_inh_red.md](./sim_vatinvoice_inh_red.md) |
| 70 | `t_sim_vatinvoice_e` | 作废重开-分表 | 57 | [sim_invoice_invalid.md](./sim_invoice_invalid.md) |
| 71 | `t_sim_vatinvoice_e` | 发票作废-分表 | 57 | [sim_invoice_valid_list.md](./sim_invoice_valid_list.md) |
| 72 | `t_sim_vatinvoice_e` | 待开发票-分表 | 57 | [sim_invoice_wait.md](./sim_invoice_wait.md) |
| 73 | `t_sim_vatinvoice_e` | 发票红冲(废弃)-分表 | 57 | [sim_red_invoice_list.md](./sim_red_invoice_list.md) |
| 74 | `t_sim_vatinvoice_e` | 发票查询-分表 | 57 | [sim_vatinvoice.md](./sim_vatinvoice.md) |
| 75 | `t_sim_vatinvoice_e` | 发票红冲-分表 | 57 | [sim_vatinvoice_inh_red.md](./sim_vatinvoice_inh_red.md) |
| 76 | `t_sim_vatinvoice_f` | 作废重开-分表 | 2 | [sim_invoice_invalid.md](./sim_invoice_invalid.md) |
| 77 | `t_sim_vatinvoice_f` | 待开发票-分表 | 2 | [sim_invoice_wait.md](./sim_invoice_wait.md) |
| 78 | `t_sim_vatinvoice_f` | 发票查询-分表 | 2 | [sim_vatinvoice.md](./sim_vatinvoice.md) |
| 79 | `t_sim_vatinvoice_f` | 发票红冲-分表 | 2 | [sim_vatinvoice_inh_red.md](./sim_vatinvoice_inh_red.md) |
| 80 | `t_sim_vatinvoice_item` | 明细单据体-子表 | 34 | [sim_invoice_invalid.md](./sim_invoice_invalid.md) |
| 81 | `t_sim_vatinvoice_item` | 单据体-子表 | 34 | [sim_invoice_valid_list.md](./sim_invoice_valid_list.md) |
| 82 | `t_sim_vatinvoice_item` | 明细单据体-子表 | 34 | [sim_invoice_wait.md](./sim_invoice_wait.md) |
| 83 | `t_sim_vatinvoice_item` | 明细单据体-子表 | 34 | [sim_vatinvoice.md](./sim_vatinvoice.md) |
| 84 | `t_sim_vatinvoice_item` | 明细单据体-子表 | 34 | [sim_vatinvoice_inh_red.md](./sim_vatinvoice_inh_red.md) |
| 85 | `t_sim_vatinvoice_vehicles` | 机动车销售发票查询-主表 | 68 | [sim_vatinvoice_vehicles.md](./sim_vatinvoice_vehicles.md) |
| 86 | `t_sim_vatinvoice_vehicles` | 机动车销售发票批量开具-主表 | 68 | [sim_vehicles_wait.md](./sim_vehicles_wait.md) |
| 87 | `t_sim_vatinvoice_wf_item` | 单据体-子表 | 13 | [sim_redinfo_workflow.md](./sim_redinfo_workflow.md) |
