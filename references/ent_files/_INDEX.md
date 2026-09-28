# ent 模块表清单

> 本模块共收录 **45** 张表定义，来自 `ent_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope ent
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mal_freight` | 运费方案-主表 | 26 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 2 | `t_mal_freight_l` | 运费方案-多语言表 | 5 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 3 | `t_mal_freight_m` | 运费方案-使用范围位图表 | 2 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 4 | `t_mal_freight_u` | 运费方案-使用范围表 | 3 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 5 | `t_mal_freightentry` | 单据体-子表 | 7 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 6 | `t_mal_freightentry_city` | 市-多选基础资料表 | 4 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 7 | `t_mal_freightentry_pro` | 省-多选基础资料表 | 4 | [ent_freightscheme.md](./ent_freightscheme.md) |
| 8 | `t_mal_instock` | 库存调整-主表 | 12 | [ent_instock.md](./ent_instock.md) |
| 9 | `t_mal_instock_a` | 库存调整-分表 | 10 | [ent_instock.md](./ent_instock.md) |
| 10 | `t_mal_instock_l` | 库存调整-多语言表 | 4 | [ent_instock.md](./ent_instock.md) |
| 11 | `t_mal_instockentry` | 商品分录-子表 | 11 | [ent_instock.md](./ent_instock.md) |
| 12 | `t_mal_inventory` | 库存查询-主表 | 10 | [ent_inventory.md](./ent_inventory.md) |
| 13 | `t_mal_order` | 商城订单-主表 | 46 | [ent_order.md](./ent_order.md) |
| 14 | `t_mal_order_a` | 商城订单-分表 | 16 | [ent_order.md](./ent_order.md) |
| 15 | `t_mal_order_l` | 商城订单-多语言表 | 4 | [ent_order.md](./ent_order.md) |
| 16 | `t_mal_orderentry` | 商品分录-子表 | 40 | [ent_order.md](./ent_order.md) |
| 17 | `t_mal_priceadjust` | 调价申请-主表 | 13 | [ent_pricerequest.md](./ent_pricerequest.md) |
| 18 | `t_mal_priceadjust_a` | 调价申请-分表 | 11 | [ent_pricerequest.md](./ent_pricerequest.md) |
| 19 | `t_mal_priceadjust_l` | 调价申请-多语言表 | 4 | [ent_pricerequest.md](./ent_pricerequest.md) |
| 20 | `t_mal_priceadjustentry` | 商品明细-子表 | 16 | [ent_pricerequest.md](./ent_pricerequest.md) |
| 21 | `t_mal_prod` | 价格管理-主表 | 52 | [ent_price.md](./ent_price.md) |
| 22 | `t_mal_prod` | 商品管理-主表 | 52 | [ent_prodmanage.md](./ent_prodmanage.md) |
| 23 | `t_mal_prod_a` | 价格管理-分表 | 28 | [ent_price.md](./ent_price.md) |
| 24 | `t_mal_prod_a` | 商品管理-分表 | 28 | [ent_prodmanage.md](./ent_prodmanage.md) |
| 25 | `t_mal_prod_l` | 价格管理-多语言表 | 8 | [ent_price.md](./ent_price.md) |
| 26 | `t_mal_prod_l` | 商品管理-多语言表 | 8 | [ent_prodmanage.md](./ent_prodmanage.md) |
| 27 | `t_mal_prod_m` | 价格管理-使用范围位图表 | 2 | [ent_price.md](./ent_price.md) |
| 28 | `t_mal_prod_m` | 商品管理-使用范围位图表 | 2 | [ent_prodmanage.md](./ent_prodmanage.md) |
| 29 | `t_mal_prod_u` | 价格管理-使用范围表 | 3 | [ent_price.md](./ent_price.md) |
| 30 | `t_mal_prod_u` | 商品管理-使用范围表 | 3 | [ent_prodmanage.md](./ent_prodmanage.md) |
| 31 | `t_mal_prodenter` | 上架申请-主表 | 13 | [ent_prodrequest.md](./ent_prodrequest.md) |
| 32 | `t_mal_prodenter_a` | 上架申请-分表 | 11 | [ent_prodrequest.md](./ent_prodrequest.md) |
| 33 | `t_mal_prodenter_l` | 上架申请-多语言表 | 4 | [ent_prodrequest.md](./ent_prodrequest.md) |
| 34 | `t_mal_prodenterentry` | 商品分录-子表 | 12 | [ent_prodrequest.md](./ent_prodrequest.md) |
| 35 | `t_mal_returnreq` | 售后确认-主表 | 0 | [ent_returnaudit.md](./ent_returnaudit.md) |
| 36 | `t_mal_returnreq_a` | 售后确认-分表 | 0 | [ent_returnaudit.md](./ent_returnaudit.md) |
| 37 | `t_mal_returnreq_l` | 售后确认-多语言表 | 0 | [ent_returnaudit.md](./ent_returnaudit.md) |
| 38 | `t_mal_returnreqentry` | 单据体-子表 | 0 | [ent_returnaudit.md](./ent_returnaudit.md) |
| 39 | `t_mal_supaptitude` | 资质分录-子表 | 12 | [ent_suprequest.md](./ent_suprequest.md) |
| 40 | `t_mal_supenter` | 入驻申请-主表 | 28 | [ent_suprequest.md](./ent_suprequest.md) |
| 41 | `t_mal_supenter_a` | 入驻申请-分表 | 10 | [ent_suprequest.md](./ent_suprequest.md) |
| 42 | `t_mal_supenter_l` | 入驻申请-多语言表 | 6 | [ent_suprequest.md](./ent_suprequest.md) |
| 43 | `t_mal_supenter_mat` | 入驻商品类别-多选基础资料表 | 3 | [ent_suprequest.md](./ent_suprequest.md) |
| 44 | `t_mal_surcharge` | 附加费方案-主表 | 17 | [ent_surcharge.md](./ent_surcharge.md) |
| 45 | `t_mal_surcharge_l` | 附加费方案-多语言表 | 5 | [ent_surcharge.md](./ent_surcharge.md) |
