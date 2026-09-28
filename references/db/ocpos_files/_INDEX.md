# ocpos 模块表清单

> 本模块共收录 **53** 张表定义，来自 `ocpos_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ocpos
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ocdbd_b2cchannelonline` | 线上门店信息-子表 | 10 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 2 | `t_ocdbd_b2cchannelonline_l` | 线上门店信息-多语言表 | 4 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 3 | `t_ocdbd_channel` | 店铺档案-主表 | 56 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 4 | `t_ocdbd_channel_auth` | 供货关系-主表 | 42 | [ocdbd_channel_author_b2c.md](./ocdbd_channel_author_b2c.md) |
| 5 | `t_ocdbd_channel_auth_l` | 供货关系-多语言表 | 5 | [ocdbd_channel_author_b2c.md](./ocdbd_channel_author_b2c.md) |
| 6 | `t_ocdbd_channel_auth_u` | 供货关系-使用范围表 | 3 | [ocdbd_channel_author_b2c.md](./ocdbd_channel_author_b2c.md) |
| 7 | `t_ocdbd_channel_e` | 店铺档案-分表 | 24 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 8 | `t_ocdbd_channel_l` | 店铺档案-多语言表 | 5 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 9 | `t_ocdbd_channel_lk` | 关联子实体-子表 | 6 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 10 | `t_ocdbd_channel_rp` | 相关负责人-多选基础资料表 | 3 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 11 | `t_ocdbd_channel_stockrec` | 店铺仓库-子表 | 17 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 12 | `t_ocdbd_channel_u` | 店铺档案-使用范围表 | 3 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 13 | `t_ocdbd_channel_x` | 店铺档案-分表 | 37 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 14 | `t_ocdbd_channelclasses` | 渠道分类单据体-子表 | 5 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 15 | `t_ocdbd_channelfuncs` | 渠道职能-多选基础资料表 | 3 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 16 | `t_ocdbd_channellabel` | 渠道标签单据体-子表 | 6 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 17 | `t_ocdbd_channelorginfo` | 供货关系-子表 | 9 | [ocdbd_b2c_channel.md](./ocdbd_b2c_channel.md) |
| 18 | `t_ocdbd_chl_address` | 店铺收货地址-主表 | 23 | [ocdbd_channel_address_inh.md](./ocdbd_channel_address_inh.md) |
| 19 | `t_ocdbd_chl_address_l` | 店铺收货地址-多语言表 | 4 | [ocdbd_channel_address_inh.md](./ocdbd_channel_address_inh.md) |
| 20 | `t_ocdbd_chl_type` | 店铺经营类型-主表 | 22 | [ocdbd_b2c_channel_type.md](./ocdbd_b2c_channel_type.md) |
| 21 | `t_ocdbd_chl_type_l` | 店铺经营类型-多语言表 | 4 | [ocdbd_b2c_channel_type.md](./ocdbd_b2c_channel_type.md) |
| 22 | `t_ocdbd_chl_type_u` | 店铺经营类型-使用范围表 | 3 | [ocdbd_b2c_channel_type.md](./ocdbd_b2c_channel_type.md) |
| 23 | `t_ocdbd_platformtype` | 平台类型-主表 | 14 | [rtbd_platformtype.md](./rtbd_platformtype.md) |
| 24 | `t_ocdbd_platformtype_l` | 平台类型-多语言表 | 4 | [rtbd_platformtype.md](./rtbd_platformtype.md) |
| 25 | `t_rtecs_omssys_branchs` | 店铺档案单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 26 | `t_rtecs_omssys_combine` | 组合商品单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 27 | `t_rtecs_omssys_items` | 商品档案单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 28 | `t_rtecs_omssys_kjorder` | 跨境销售订单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 29 | `t_rtecs_omssys_kjreturn` | 跨境售后单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 30 | `t_rtecs_omssys_origorder` | 原始订单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 31 | `t_rtecs_omssys_pd` | 盘点单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 32 | `t_rtecs_omssys_purchase` | 采购订单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 33 | `t_rtecs_omssys_purin` | 入库(采购)单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 34 | `t_rtecs_omssys_purout` | 出库(采购)单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 35 | `t_rtecs_omssys_return` | 售后退货单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 36 | `t_rtecs_omssys_returnin` | 退货入库单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 37 | `t_rtecs_omssys_sales` | 销售订单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 38 | `t_rtecs_omssys_salesout` | 销售出库单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 39 | `t_rtecs_omssys_stockin` | 入库(其他,调拨,盘盈)单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 40 | `t_rtecs_omssys_stockout` | 出库(其他,调拨,盘亏)单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 41 | `t_rtecs_omssys_supplier` | 供货商单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 42 | `t_rtecs_omssys_surplusin` | 盘盈单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 43 | `t_rtecs_omssys_surplusout` | 盘亏单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 44 | `t_rtecs_omssys_trans` | 调拨单单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 45 | `t_rtecs_omssys_transin` | 调拨人单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 46 | `t_rtecs_omssys_transout` | 调拨出单据体-子表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 47 | `t_rtecs_omssystem` | OMS系统配置-主表 | 43 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 48 | `t_rtecs_omssystem_a` | OMS系统配置-分表 | 23 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 49 | `t_rtecs_omssystem_g` | OMS系统配置-分表 | 5 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 50 | `t_rtecs_omssystem_j` | OMS系统配置-分表 | 11 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 51 | `t_rtecs_omssystem_k` | OMS系统配置-分表 | 5 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 52 | `t_rtecs_omssystem_l` | OMS系统配置-多语言表 | 4 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
| 53 | `t_rtecs_omssystem_w` | OMS系统配置-分表 | 4 | [rtecs_omssystem.md](./rtecs_omssystem.md) |
