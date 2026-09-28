# mal 模块表清单

> 本模块共收录 **48** 张表定义，来自 `mal_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope mal
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mal_attention` | 我的关注单-主表 | 21 | [mal_attentionbill.md](./mal_attentionbill.md) |
| 2 | `t_mal_comparerecord` | 商城对比记录-主表 | 9 | [mal_compare_record.md](./mal_compare_record.md) |
| 3 | `t_mal_oftenbuy` | 我的常买单-主表 | 24 | [mal_oftenbuybill.md](./mal_oftenbuybill.md) |
| 4 | `t_mal_order` | 商城订单-主表 | 46 | [mal_order.md](./mal_order.md) |
| 5 | `t_mal_order` | 商城订单基础资料-主表 | 46 | [mal_order_bd.md](./mal_order_bd.md) |
| 6 | `t_mal_order_a` | 商城订单-分表 | 16 | [mal_order.md](./mal_order.md) |
| 7 | `t_mal_order_a` | 商城订单基础资料-分表 | 16 | [mal_order_bd.md](./mal_order_bd.md) |
| 8 | `t_mal_order_l` | 商城订单-多语言表 | 4 | [mal_order.md](./mal_order.md) |
| 9 | `t_mal_order_tc` | 商城订单-关联追踪表 | 7 | [mal_order.md](./mal_order.md) |
| 10 | `t_mal_order_wb` | 商城订单-反写记录表 | 10 | [mal_order.md](./mal_order.md) |
| 11 | `t_mal_orderentry` | 商品分录-子表 | 40 | [mal_order.md](./mal_order.md) |
| 12 | `t_mal_orderentry` | 单据体-子表 | 40 | [mal_order_bd.md](./mal_order_bd.md) |
| 13 | `t_mal_orderentry_a` | 商品分录-分表 | 10 | [mal_order.md](./mal_order.md) |
| 14 | `t_mal_orderentry_lk` | 关联子实体-子表 | 8 | [mal_order.md](./mal_order.md) |
| 15 | `t_mal_plan` | 采购计划-主表 | 15 | [mal_plan.md](./mal_plan.md) |
| 16 | `t_mal_plan_l` | 采购计划-多语言表 | 4 | [mal_plan.md](./mal_plan.md) |
| 17 | `t_mal_plan_tc` | 采购计划-关联追踪表 | 7 | [mal_plan.md](./mal_plan.md) |
| 18 | `t_mal_plan_wb` | 采购计划-反写记录表 | 10 | [mal_plan.md](./mal_plan.md) |
| 19 | `t_mal_planentry` | 单据体-子表 | 24 | [mal_plan.md](./mal_plan.md) |
| 20 | `t_mal_planentry_lk` | 关联子实体-子表 | 10 | [mal_plan.md](./mal_plan.md) |
| 21 | `t_mal_purscheme` | 采购方案-主表 | 12 | [mal_purscheme.md](./mal_purscheme.md) |
| 22 | `t_mal_purscheme_l` | 采购方案-多语言表 | 5 | [mal_purscheme.md](./mal_purscheme.md) |
| 23 | `t_mal_purschemeentry` | 商品分录-子表 | 7 | [mal_purscheme.md](./mal_purscheme.md) |
| 24 | `t_mal_receiptinfo` | 收货地址-主表 | 35 | [mal_address.md](./mal_address.md) |
| 25 | `t_mal_receiptinfo_l` | 收货地址-多语言表 | 7 | [mal_address.md](./mal_address.md) |
| 26 | `t_mal_receiptinfo_m` | 收货地址-使用范围位图表 | 2 | [mal_address.md](./mal_address.md) |
| 27 | `t_mal_receiptinfo_u` | 收货地址-使用范围表 | 3 | [mal_address.md](./mal_address.md) |
| 28 | `t_mal_shopcart` | 我的购物车单-主表 | 24 | [mal_shopcartbill.md](./mal_shopcartbill.md) |
| 29 | `t_pur_order` | 售后申请（暂时弃用）-主表 | 48 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 30 | `t_pur_order` | 订单执行跟踪-主表 | 48 | [mal_purorder.md](./mal_purorder.md) |
| 31 | `t_pur_order_a` | 售后申请（暂时弃用）-分表 | 27 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 32 | `t_pur_order_a` | 订单执行跟踪-分表 | 27 | [mal_purorder.md](./mal_purorder.md) |
| 33 | `t_pur_order_l` | 售后申请（暂时弃用）-多语言表 | 4 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 34 | `t_pur_order_l` | 订单执行跟踪-多语言表 | 4 | [mal_purorder.md](./mal_purorder.md) |
| 35 | `t_pur_orderentry` | 订单分录-子表 | 44 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 36 | `t_pur_orderentry` | 订单分录-子表 | 44 | [mal_purorder.md](./mal_purorder.md) |
| 37 | `t_pur_orderentry_a` | 订单分录-分表 | 70 | [mal_aftersalereq.md](./mal_aftersalereq.md) |
| 38 | `t_pur_orderentry_a` | 订单分录-分表 | 70 | [mal_purorder.md](./mal_purorder.md) |
| 39 | `t_pur_request` | 售后申请单-主表 | 51 | [mal_returnreq.md](./mal_returnreq.md) |
| 40 | `t_pur_request_a` | 售后申请单-分表 | 15 | [mal_returnreq.md](./mal_returnreq.md) |
| 41 | `t_pur_request_l` | 售后申请单-多语言表 | 5 | [mal_returnreq.md](./mal_returnreq.md) |
| 42 | `t_pur_request_lk` | 关联子实体-子表 | 6 | [mal_returnreq.md](./mal_returnreq.md) |
| 43 | `t_pur_request_tc` | 售后申请单-关联追踪表 | 7 | [mal_returnreq.md](./mal_returnreq.md) |
| 44 | `t_pur_request_wb` | 售后申请单-反写记录表 | 10 | [mal_returnreq.md](./mal_returnreq.md) |
| 45 | `t_pur_requestasentry` | 电商服务分录-子表 | 4 | [mal_returnreq.md](./mal_returnreq.md) |
| 46 | `t_pur_requestentry` | 商品详情分录-子表 | 43 | [mal_returnreq.md](./mal_returnreq.md) |
| 47 | `t_pur_requestentry_a` | 商品详情分录-分表 | 28 | [mal_returnreq.md](./mal_returnreq.md) |
| 48 | `t_pur_requestentry_lk` | 关联子实体-子表 | 8 | [mal_returnreq.md](./mal_returnreq.md) |
