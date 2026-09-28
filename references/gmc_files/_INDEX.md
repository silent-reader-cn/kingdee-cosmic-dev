# gmc 模块表清单

> 本模块共收录 **16** 张表定义，来自 `gmc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope gmc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bd_classstandard` | 商品分类标准-主表 | 23 | [bd_goodsclassstandard.md](./bd_goodsclassstandard.md) |
| 2 | `t_bd_classstandard_l` | 商品分类标准-多语言表 | 5 | [bd_goodsclassstandard.md](./bd_goodsclassstandard.md) |
| 3 | `t_bd_classstandard_m` | 商品分类标准-使用范围位图表 | 2 | [bd_goodsclassstandard.md](./bd_goodsclassstandard.md) |
| 4 | `t_bd_classstandard_u` | 商品分类标准-使用范围表 | 3 | [bd_goodsclassstandard.md](./bd_goodsclassstandard.md) |
| 5 | `t_bd_itemtype` | 商品类型-主表 | 14 | [bd_itemtype.md](./bd_itemtype.md) |
| 6 | `t_bd_itemtype_l` | 商品类型-多语言表 | 5 | [bd_itemtype.md](./bd_itemtype.md) |
| 7 | `t_mdr_itembrand` | 商品品牌-主表 | 22 | [mdr_item_brand.md](./mdr_item_brand.md) |
| 8 | `t_mdr_itembrand_classes` | 关联商品分类-多选基础资料表 | 3 | [mdr_item_brand.md](./mdr_item_brand.md) |
| 9 | `t_mdr_itembrand_l` | 商品品牌-多语言表 | 5 | [mdr_item_brand.md](./mdr_item_brand.md) |
| 10 | `t_mdr_itembrand_m` | 商品品牌-使用范围位图表 | 2 | [mdr_item_brand.md](./mdr_item_brand.md) |
| 11 | `t_mdr_itembrand_u` | 商品品牌-使用范围表 | 3 | [mdr_item_brand.md](./mdr_item_brand.md) |
| 12 | `t_mdr_itemclass` | 商品分类-主表 | 26 | [mdr_goodsclass.md](./mdr_goodsclass.md) |
| 13 | `t_mdr_itemclass` | 商品分类-主表 | 26 | [mdr_item_class.md](./mdr_item_class.md) |
| 14 | `t_mdr_itemclass_l` | 商品分类-多语言表 | 5 | [mdr_goodsclass.md](./mdr_goodsclass.md) |
| 15 | `t_mdr_itemclass_l` | 商品分类-多语言表 | 5 | [mdr_item_class.md](./mdr_item_class.md) |
| 16 | `t_mdr_itemclass_p` | 商品分类-分表 | 4 | [mdr_goodsclass.md](./mdr_goodsclass.md) |
