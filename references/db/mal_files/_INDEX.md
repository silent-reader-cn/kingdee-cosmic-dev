# mal 模块表清单

> 本模块共收录 **89** 张表定义，来自 `mal_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category mal
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mal_attention` | 我的关注单-主表 | 21 | [mal_attentionbill.md](./mal_attentionbill.md) |
| 2 | `t_mal_billentry` | 受控业务单据-子表 | 0 | [mal_pricemonitorstrategy.md](./mal_pricemonitorstrategy.md) |
| 3 | `t_mal_browsinghistory` | 浏览记录-主表 | 9 | [mal_browsinghistory.md](./mal_browsinghistory.md) |
| 4 | `t_mal_compareprice` | 比价记录-主表 | 12 | [mal_compareprice.md](./mal_compareprice.md) |
| 5 | `t_mal_comparepriceentry` | 比价分录-子表 | 13 | [mal_compareprice.md](./mal_compareprice.md) |
| 6 | `t_mal_comparerecord` | 商城对比记录-主表 | 9 | [mal_compare_record.md](./mal_compare_record.md) |
| 7 | `t_mal_goodsclasssubentry` | 子单据体-子表 | 0 | [mal_salepricestrategy.md](./mal_salepricestrategy.md) |
| 8 | `t_mal_menuclass` | 菜单分类-主表 | 12 | [mal_menuclass.md](./mal_menuclass.md) |
| 9 | `t_mal_menuclass_l` | 菜单分类-多语言表 | 4 | [mal_menuclass.md](./mal_menuclass.md) |
| 10 | `t_mal_menus` | 菜单-主表 | 15 | [mal_menu.md](./mal_menu.md) |
| 11 | `t_mal_menus_l` | 菜单-多语言表 | 4 | [mal_menu.md](./mal_menu.md) |
| 12 | `t_mal_oftenbuy` | 我的常买单-主表 | 24 | [mal_oftenbuybill.md](./mal_oftenbuybill.md) |
| 13 | `t_mal_order` | 商城订单-主表 | 46 | [mal_order.md](./mal_order.md) |
| 14 | `t_mal_order` | 商城订单-主表 | 46 | [mal_order_bd.md](./mal_order_bd.md) |
| 15 | `t_mal_order` | 订单评价-主表 | 46 | [mal_order_comment.md](./mal_order_comment.md) |
| 16 | `t_mal_order_a` | 商城订单-分表 | 16 | [mal_order.md](./mal_order.md) |
| 17 | `t_mal_order_a` | 商城订单-分表 | 16 | [mal_order_bd.md](./mal_order_bd.md) |
| 18 | `t_mal_order_a` | 订单评价-分表 | 16 | [mal_order_comment.md](./mal_order_comment.md) |
| 19 | `t_mal_order_l` | 商城订单-多语言表 | 4 | [mal_order.md](./mal_order.md) |
| 20 | `t_mal_order_l` | 订单评价-多语言表 | 4 | [mal_order_comment.md](./mal_order_comment.md) |
| 21 | `t_mal_order_lk` | 关联子实体-子表 | 6 | [mal_order.md](./mal_order.md) |
| 22 | `t_mal_order_lk` | 关联子实体-子表 | 6 | [mal_order_comment.md](./mal_order_comment.md) |
| 23 | `t_mal_order_tc` | 商城订单-关联追踪表 | 7 | [mal_order.md](./mal_order.md) |
| 24 | `t_mal_order_tc` | 订单评价-关联追踪表 | 7 | [mal_order_comment.md](./mal_order_comment.md) |
| 25 | `t_mal_order_wb` | 商城订单-反写记录表 | 10 | [mal_order.md](./mal_order.md) |
| 26 | `t_mal_order_wb` | 订单评价-反写记录表 | 10 | [mal_order_comment.md](./mal_order_comment.md) |
| 27 | `t_mal_orderentry` | 商品分录-子表 | 47 | [mal_order.md](./mal_order.md) |
| 28 | `t_mal_orderentry` | 单据体-子表 | 47 | [mal_order_bd.md](./mal_order_bd.md) |
| 29 | `t_mal_orderentry` | 商品分录-子表 | 47 | [mal_order_comment.md](./mal_order_comment.md) |
| 30 | `t_mal_orderentry_a` | 商品分录-分表 | 13 | [mal_order.md](./mal_order.md) |
| 31 | `t_mal_orderentry_a` | 商品分录-分表 | 13 | [mal_order_comment.md](./mal_order_comment.md) |
| 32 | `t_mal_orderentry_lk` | 关联子实体-子表 | 8 | [mal_order.md](./mal_order.md) |
| 33 | `t_mal_orderentry_lk` | 关联子实体-子表 | 8 | [mal_order_comment.md](./mal_order_comment.md) |
| 34 | `t_mal_orderrequest` | 商城采购申请-主表 | 29 | [mal_orderrequest.md](./mal_orderrequest.md) |
| 35 | `t_mal_orderrequest_l` | 商城采购申请-多语言表 | 4 | [mal_orderrequest.md](./mal_orderrequest.md) |
| 36 | `t_mal_orderrequestentry` | 单据体-子表 | 45 | [mal_orderrequest.md](./mal_orderrequest.md) |
| 37 | `t_mal_plan` | 采购计划-主表 | 15 | [mal_plan.md](./mal_plan.md) |
| 38 | `t_mal_plan_l` | 采购计划-多语言表 | 4 | [mal_plan.md](./mal_plan.md) |
| 39 | `t_mal_plan_tc` | 采购计划-关联追踪表 | 7 | [mal_plan.md](./mal_plan.md) |
| 40 | `t_mal_plan_wb` | 采购计划-反写记录表 | 10 | [mal_plan.md](./mal_plan.md) |
| 41 | `t_mal_planentry` | 单据体-子表 | 24 | [mal_plan.md](./mal_plan.md) |
| 42 | `t_mal_planentry_lk` | 关联子实体-子表 | 10 | [mal_plan.md](./mal_plan.md) |
| 43 | `t_mal_pricemonitor1` | 价格监控策略-主表 | 0 | [mal_pricemonitorstrategy.md](./mal_pricemonitorstrategy.md) |
| 44 | `t_mal_purscheme` | 个人套餐-主表 | 12 | [mal_purscheme.md](./mal_purscheme.md) |
| 45 | `t_mal_purscheme_l` | 个人套餐-多语言表 | 5 | [mal_purscheme.md](./mal_purscheme.md) |
| 46 | `t_mal_purschemeentry` | 商品分录-子表 | 7 | [mal_purscheme.md](./mal_purscheme.md) |
| 47 | `t_mal_receiptinfo` | 收货地址-主表 | 36 | [mal_address.md](./mal_address.md) |
| 48 | `t_mal_receiptinfo_l` | 收货地址-多语言表 | 7 | [mal_address.md](./mal_address.md) |
| 49 | `t_mal_receiptinfo_m` | 收货地址-使用范围位图表 | 2 | [mal_address.md](./mal_address.md) |
| 50 | `t_mal_receiptinfo_u` | 收货地址-使用范围表 | 3 | [mal_address.md](./mal_address.md) |
| 51 | `t_mal_ruleentry1` | 触发规则-子表 | 0 | [mal_pricemonitorstrategy.md](./mal_pricemonitorstrategy.md) |
| 52 | `t_mal_saleentryentity` | 销售单据体-子表 | 0 | [mal_salepricestrategy.md](./mal_salepricestrategy.md) |
| 53 | `t_mal_salepricestrategy` | 销售价格策略-主表 | 0 | [mal_salepricestrategy.md](./mal_salepricestrategy.md) |
| 54 | `t_mal_salepricestrategy_l` | 销售价格策略-多语言表 | 0 | [mal_salepricestrategy.md](./mal_salepricestrategy.md) |
| 55 | `t_mal_shopcart` | 我的购物车单-主表 | 24 | [mal_shopcartbill.md](./mal_shopcartbill.md) |
| 56 | `t_mal_statementdata` | 对账数据-主表 | 60 | [mal_statement_data.md](./mal_statement_data.md) |
| 57 | `t_mal_statementdata` | 开票中（废弃）-主表 | 60 | [mal_statement_invoicing.md](./mal_statement_invoicing.md) |
| 58 | `t_mal_statementdata` | 收货入库明细-主表 | 60 | [mal_statement_recinstock.md](./mal_statement_recinstock.md) |
| 59 | `t_mal_statementdata_a` | 对账数据-分表 | 0 | [mal_statement_data.md](./mal_statement_data.md) |
| 60 | `t_mal_statementdata_a` | 开票中（废弃）-分表 | 0 | [mal_statement_invoicing.md](./mal_statement_invoicing.md) |
| 61 | `t_mal_statementdata_l` | 对账数据-多语言表 | 4 | [mal_statement_data.md](./mal_statement_data.md) |
| 62 | `t_mal_statementdata_l` | 开票中（废弃）-多语言表 | 4 | [mal_statement_invoicing.md](./mal_statement_invoicing.md) |
| 63 | `t_mal_statementdataentry` | 明细数据-子表 | 18 | [mal_statement_data.md](./mal_statement_data.md) |
| 64 | `t_mal_statementdataentry` | 明细数据-子表 | 18 | [mal_statement_invoicing.md](./mal_statement_invoicing.md) |
| 65 | `t_mal_statementdataentry` | 明细数据-子表 | 18 | [mal_statement_recinstock.md](./mal_statement_recinstock.md) |
| 66 | `t_mal_statementrule` | 电商对账规则-主表 | 23 | [mal_statement_rule.md](./mal_statement_rule.md) |
| 67 | `t_mal_statementrule_l` | 电商对账规则-多语言表 | 4 | [mal_statement_rule.md](./mal_statement_rule.md) |
| 68 | `t_mal_tab` | 页签-主表 | 19 | [mal_tab.md](./mal_tab.md) |
| 69 | `t_mal_tab_l` | 页签-多语言表 | 4 | [mal_tab.md](./mal_tab.md) |
| 70 | `t_pur_order` | 售后申请（暂时弃用）-主表 | 51 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 71 | `t_pur_order` | 订单执行跟踪-主表 | 51 | [mal_purorder.md](./mal_purorder.md) |
| 72 | `t_pur_order_a` | 售后申请（暂时弃用）-分表 | 32 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 73 | `t_pur_order_a` | 订单执行跟踪-分表 | 32 | [mal_purorder.md](./mal_purorder.md) |
| 74 | `t_pur_order_l` | 售后申请（暂时弃用）-多语言表 | 4 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 75 | `t_pur_order_l` | 订单执行跟踪-多语言表 | 4 | [mal_purorder.md](./mal_purorder.md) |
| 76 | `t_pur_orderentry` | 订单分录-子表 | 46 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 77 | `t_pur_orderentry` | 订单分录-子表 | 46 | [mal_purorder.md](./mal_purorder.md) |
| 78 | `t_pur_orderentry_a` | 订单分录-分表 | 72 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 79 | `t_pur_orderentry_a` | 订单分录-分表 | 72 | [mal_purorder.md](./mal_purorder.md) |
| 80 | `t_pur_request` | 售后申请单-主表 | 53 | [mal_returnreq.md](./mal_returnreq.md) |
| 81 | `t_pur_request_a` | 售后申请单-分表 | 15 | [mal_returnreq.md](./mal_returnreq.md) |
| 82 | `t_pur_request_l` | 售后申请单-多语言表 | 5 | [mal_returnreq.md](./mal_returnreq.md) |
| 83 | `t_pur_request_lk` | 关联子实体-子表 | 6 | [mal_returnreq.md](./mal_returnreq.md) |
| 84 | `t_pur_request_tc` | 售后申请单-关联追踪表 | 7 | [mal_returnreq.md](./mal_returnreq.md) |
| 85 | `t_pur_request_wb` | 售后申请单-反写记录表 | 10 | [mal_returnreq.md](./mal_returnreq.md) |
| 86 | `t_pur_requestasentry` | 电商服务分录-子表 | 4 | [mal_returnreq.md](./mal_returnreq.md) |
| 87 | `t_pur_requestentry` | 商品详情分录-子表 | 44 | [mal_returnreq.md](./mal_returnreq.md) |
| 88 | `t_pur_requestentry_a` | 商品详情分录-分表 | 28 | [mal_returnreq.md](./mal_returnreq.md) |
| 89 | `t_pur_requestentry_lk` | 关联子实体-子表 | 8 | [mal_returnreq.md](./mal_returnreq.md) |
