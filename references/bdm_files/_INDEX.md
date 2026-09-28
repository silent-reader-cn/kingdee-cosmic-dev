# bdm 模块表清单

> 本模块共收录 **80** 张表定义，来自 `bdm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope bdm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bdm_attach_type` | 附件类型基础资料-主表 | 13 | [bdm_attach_type.md](./bdm_attach_type.md) |
| 2 | `t_bdm_attach_type_l` | 附件类型基础资料-多语言表 | 4 | [bdm_attach_type.md](./bdm_attach_type.md) |
| 3 | `t_bdm_blacklist_config` | 新增自定义黑名单-主表 | 10 | [bdm_blacklist_config.md](./bdm_blacklist_config.md) |
| 4 | `t_bdm_blacklist_config_l` | 新增自定义黑名单-多语言表 | 4 | [bdm_blacklist_config.md](./bdm_blacklist_config.md) |
| 5 | `t_bdm_download_center` | 下载中心-主表 | 17 | [bdm_download_center.md](./bdm_download_center.md) |
| 6 | `t_bdm_download_center` | 发票数据下载-主表 | 17 | [bdm_download_center_v1.md](./bdm_download_center_v1.md) |
| 7 | `t_bdm_download_detail1` | 发票信息-子表 | 5 | [bdm_download_center.md](./bdm_download_center.md) |
| 8 | `t_bdm_download_detail1` | 发票信息-子表 | 5 | [bdm_download_center_v1.md](./bdm_download_center_v1.md) |
| 9 | `t_bdm_download_detail2` | 文件信息-子表 | 5 | [bdm_download_center.md](./bdm_download_center.md) |
| 10 | `t_bdm_download_detail2` | 文件信息-子表 | 5 | [bdm_download_center_v1.md](./bdm_download_center_v1.md) |
| 11 | `t_bdm_download_item` | 下载记录（实体）-主表 | 5 | [bdm_download_item.md](./bdm_download_item.md) |
| 12 | `t_bdm_drawer_item` | 单据体-子表 | 4 | [bdm_drawer_strategy.md](./bdm_drawer_strategy.md) |
| 13 | `t_bdm_drawer_strategy` | 开票人设置-主表 | 17 | [bdm_drawer_strategy.md](./bdm_drawer_strategy.md) |
| 14 | `t_bdm_einvoice_account` | 电子发票服务平台信息-主表 | 15 | [bdm_einvoice_account.md](./bdm_einvoice_account.md) |
| 15 | `t_bdm_einvoice_account_l` | 电子发票服务平台信息-多语言表 | 4 | [bdm_einvoice_account.md](./bdm_einvoice_account.md) |
| 16 | `t_bdm_einvoice_items` | 组织-子表 | 4 | [bdm_einvoice_account.md](./bdm_einvoice_account.md) |
| 17 | `t_bdm_enterprise_baseinfo` | 企业基础信息-主表 | 44 | [bdm_enterprise_baseinfo.md](./bdm_enterprise_baseinfo.md) |
| 18 | `t_bdm_enterprise_info` | 企业信息-主表 | 28 | [bdm_enterprise_info.md](./bdm_enterprise_info.md) |
| 19 | `t_bdm_ep_checked_tax` | 核定税率-子表 | 9 | [bdm_enterprise_info.md](./bdm_enterprise_info.md) |
| 20 | `t_bdm_ep_monitor_info` | 监控信息-子表 | 24 | [bdm_enterprise_info.md](./bdm_enterprise_info.md) |
| 21 | `t_bdm_equip_stock_item` | 单据体-子表 | 4 | [bdm_stock_manage.md](./bdm_stock_manage.md) |
| 22 | `t_bdm_equip_stock_manage` | 设备库存管理-主表 | 18 | [bdm_equip_stock_manage.md](./bdm_equip_stock_manage.md) |
| 23 | `t_bdm_equip_stock_manage` | 设备库存-主表 | 18 | [bdm_stock_manage.md](./bdm_stock_manage.md) |
| 24 | `t_bdm_goods_info` | 开票项管理-主表 | 41 | [bdm_goods_info.md](./bdm_goods_info.md) |
| 25 | `t_bdm_goods_info_group` | 开票项分类-主表 | 17 | [bdm_goods_info_group.md](./bdm_goods_info_group.md) |
| 26 | `t_bdm_goods_info_group_l` | 开票项分类-多语言表 | 5 | [bdm_goods_info_group.md](./bdm_goods_info_group.md) |
| 27 | `t_bdm_goods_info_item` | 单据体-子表 | 13 | [bdm_goods_info.md](./bdm_goods_info.md) |
| 28 | `t_bdm_goods_info_l` | 开票项管理-多语言表 | 4 | [bdm_goods_info.md](./bdm_goods_info.md) |
| 29 | `t_bdm_goods_info_m` | 开票项管理-使用范围位图表 | 3 | [bdm_goods_info.md](./bdm_goods_info.md) |
| 30 | `t_bdm_goods_info_u` | 开票项管理-使用范围表 | 3 | [bdm_goods_info.md](./bdm_goods_info.md) |
| 31 | `t_bdm_goods_mapping` | 商品映射（弃用）-主表 | 13 | [bdm_goods_mapping.md](./bdm_goods_mapping.md) |
| 32 | `t_bdm_inv_issue_title` | 开票抬头管理-主表 | 17 | [bdm_inv_issue_title.md](./bdm_inv_issue_title.md) |
| 33 | `t_bdm_inv_item_setting` | 开票项设置-主表 | 13 | [bdm_inv_item_setting.md](./bdm_inv_item_setting.md) |
| 34 | `t_bdm_inv_merge_rule` | 单据合并规则-主表 | 23 | [bdm_inv_merge_rule.md](./bdm_inv_merge_rule.md) |
| 35 | `t_bdm_inv_merge_rule` | 合并配置-主表 | 23 | [bdm_merge_rule.md](./bdm_merge_rule.md) |
| 36 | `t_bdm_inv_merge_rule_l` | 单据合并规则-多语言表 | 4 | [bdm_inv_merge_rule.md](./bdm_inv_merge_rule.md) |
| 37 | `t_bdm_inv_merge_rule_l` | 合并配置-多语言表 | 4 | [bdm_merge_rule.md](./bdm_merge_rule.md) |
| 38 | `t_bdm_inv_split_rule` | 拆分配置-主表 | 37 | [bdm_inv_split_rule.md](./bdm_inv_split_rule.md) |
| 39 | `t_bdm_inv_title_setting` | 开票抬头设置-主表 | 13 | [bdm_inv_title_setting.md](./bdm_inv_title_setting.md) |
| 40 | `t_bdm_invoice_apply_agent` | 发票申领经办人-子表 | 8 | [bdm_enterprise_info.md](./bdm_enterprise_info.md) |
| 41 | `t_bdm_invoice_permission` | 许可授权-主表 | 16 | [bdm_invoice_permission.md](./bdm_invoice_permission.md) |
| 42 | `t_bdm_issue_inv_setttting` | 批量开票设置-主表 | 5 | [bdm_issue_inv_setting.md](./bdm_issue_inv_setting.md) |
| 43 | `t_bdm_issue_title_cust` | 客户信息单据体-子表 | 7 | [bdm_inv_issue_title.md](./bdm_inv_issue_title.md) |
| 44 | `t_bdm_issue_title_items` | 开户行单据体-子表 | 13 | [bdm_inv_issue_title.md](./bdm_inv_issue_title.md) |
| 45 | `t_bdm_issue_title_mapping` | 开票抬头映射（弃用）-主表 | 11 | [bdm_issue_title_mapping.md](./bdm_issue_title_mapping.md) |
| 46 | `t_bdm_mail_items` | 企业信息-子表 | 4 | [bdm_mail.md](./bdm_mail.md) |
| 47 | `t_bdm_mail_setting` | 邮箱设置-主表 | 21 | [bdm_mail.md](./bdm_mail.md) |
| 48 | `t_bdm_msg_auth_setting` | 短信推送权限控制设置-主表 | 6 | [bdm_msg_auth_setting.md](./bdm_msg_auth_setting.md) |
| 49 | `t_bdm_operator_info` | 经办人信息-主表 | 22 | [bdm_operator_info.md](./bdm_operator_info.md) |
| 50 | `t_bdm_operator_info_l` | 经办人信息-多语言表 | 4 | [bdm_operator_info.md](./bdm_operator_info.md) |
| 51 | `t_bdm_operator_info_u` | 经办人信息-使用范围表 | 3 | [bdm_operator_info.md](./bdm_operator_info.md) |
| 52 | `t_bdm_org` | 企业管理-主表 | 27 | [bdm_org.md](./bdm_org.md) |
| 53 | `t_bdm_org` | 非组织树企业-主表 | 27 | [bdm_org_nottree_list.md](./bdm_org_nottree_list.md) |
| 54 | `t_bdm_org` | 分配组织树形列表-主表 | 27 | [bdm_org_tree_allocation.md](./bdm_org_tree_allocation.md) |
| 55 | `t_bdm_org` | 树形组织列表-主表 | 27 | [bdm_org_tree_list.md](./bdm_org_tree_list.md) |
| 56 | `t_bdm_org` | 静态二维码设置-主表 | 27 | [bdm_qr_code_manage.md](./bdm_qr_code_manage.md) |
| 57 | `t_bdm_org_l` | 非组织树企业-多语言表 | 6 | [bdm_org_nottree_list.md](./bdm_org_nottree_list.md) |
| 58 | `t_bdm_org_l` | 分配组织树形列表-多语言表 | 6 | [bdm_org_tree_allocation.md](./bdm_org_tree_allocation.md) |
| 59 | `t_bdm_org_l` | 树形组织列表-多语言表 | 6 | [bdm_org_tree_list.md](./bdm_org_tree_list.md) |
| 60 | `t_bdm_pdf_download_rename` | pdf文件下载命名-主表 | 14 | [bdm_pdf_download_rename.md](./bdm_pdf_download_rename.md) |
| 61 | `t_bdm_premission_info` | 发票许可信息-主表 | 8 | [bdm_premission_info.md](./bdm_premission_info.md) |
| 62 | `t_bdm_redinfo_setting` | 审批配置单据(弃用)-主表 | 14 | [bdm_redinfo_setting.md](./bdm_redinfo_setting.md) |
| 63 | `t_bdm_remark_select_set` | 已选备注设置-主表 | 9 | [bdm_remark_select_setting.md](./bdm_remark_select_setting.md) |
| 64 | `t_bdm_remark_setting` | 备注设置-主表 | 13 | [bdm_remark.md](./bdm_remark.md) |
| 65 | `t_bdm_scaninvoice_setting` | 扫码开票设置（原默认开票项）-主表 | 17 | [bdm_scaninvoice_setting.md](./bdm_scaninvoice_setting.md) |
| 66 | `t_bdm_scheme_setting` | 方案配置-主表 | 17 | [bdm_scheme_setting.md](./bdm_scheme_setting.md) |
| 67 | `t_bdm_send_epinfo_setting` | 短信发送企业设置-主表 | 2 | [bdm_send_epinfo_setting.md](./bdm_send_epinfo_setting.md) |
| 68 | `t_bdm_sensitive_wordlist` | 新增敏感词-主表 | 10 | [bdm_sensitive_wordlist.md](./bdm_sensitive_wordlist.md) |
| 69 | `t_bdm_sensitive_wordlist_l` | 新增敏感词-多语言表 | 4 | [bdm_sensitive_wordlist.md](./bdm_sensitive_wordlist.md) |
| 70 | `t_bdm_sms_setting` | 短信设置-主表 | 22 | [bdm_sms_setting.md](./bdm_sms_setting.md) |
| 71 | `t_bdm_split_hs_config` | 含税拆分-主表 | 16 | [bdm_split_hs_config.md](./bdm_split_hs_config.md) |
| 72 | `t_bdm_system_setting` | 系统设置（当前只有二维码过期时间）-主表 | 3 | [bdm_system_setting.md](./bdm_system_setting.md) |
| 73 | `t_bdm_tax_equipment` | 开票设备-主表 | 35 | [bdm_tax_equipment.md](./bdm_tax_equipment.md) |
| 74 | `t_bdm_taxrate_code` | 税收分类编码(废弃)-主表 | 28 | [bdm_taxrate_code.md](./bdm_taxrate_code.md) |
| 75 | `t_bdm_taxrate_code_l` | 税收分类编码(废弃)-多语言表 | 5 | [bdm_taxrate_code.md](./bdm_taxrate_code.md) |
| 76 | `t_bdm_terminal` | 终端单据体-子表 | 12 | [bdm_tax_equipment.md](./bdm_tax_equipment.md) |
| 77 | `t_bdm_terminal_invoice` | 终端发票号段-主表 | 7 | [bdm_terminal_invoice.md](./bdm_terminal_invoice.md) |
| 78 | `t_bdm_third_org` | 外部系统组织-主表 | 9 | [bdm_third_org.md](./bdm_third_org.md) |
| 79 | `t_bdm_vehicle_info` | 车辆信息管理-主表 | 16 | [bdm_vehicle_info.md](./bdm_vehicle_info.md) |
| 80 | `t_rim_his_sync_log` | 公有云数据同步-主表 | 18 | [bdm_his_sync_log.md](./bdm_his_sync_log.md) |
