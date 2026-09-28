# er 模块表清单

> 本模块共收录 **35** 张表定义，来自 `er_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope er
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ep_praiserecord` | 点赞记录实体-主表 | 13 | [er_praiserecord.md](./er_praiserecord.md) |
| 2 | `t_ep_praiserecord_l` | 点赞记录实体-多语言表 | 4 | [er_praiserecord.md](./er_praiserecord.md) |
| 3 | `t_ep_userscore` | 低碳积分单据-主表 | 18 | [er_integralboradbill.md](./er_integralboradbill.md) |
| 4 | `t_ep_userscore` | 我的实体-主表 | 18 | [er_view.md](./er_view.md) |
| 5 | `t_ep_userscore_l` | 我的实体-多语言表 | 5 | [er_view.md](./er_view.md) |
| 6 | `t_er_accountinfo` | 单据体-子表 | 40 | [er_dailyloanbilldata.md](./er_dailyloanbilldata.md) |
| 7 | `t_er_citypicture` | 城市图片-主表 | 20 | [er_citypicture.md](./er_citypicture.md) |
| 8 | `t_er_citypicture_l` | 城市图片-多语言表 | 7 | [er_citypicture.md](./er_citypicture.md) |
| 9 | `t_er_citypicture_m` | 城市图片-使用范围位图表 | 2 | [er_citypicture.md](./er_citypicture.md) |
| 10 | `t_er_citypicture_u` | 城市图片-使用范围表 | 3 | [er_citypicture.md](./er_citypicture.md) |
| 11 | `t_er_dailyloanbill` | 借款单基础资料-主表 | 54 | [er_dailyloanbilldata.md](./er_dailyloanbilldata.md) |
| 12 | `t_er_exceptioninfo` | 业务异常信息-主表 | 10 | [er_exceptioninfo.md](./er_exceptioninfo.md) |
| 13 | `t_er_functionpermsetting` | 功能权限设置-主表 | 20 | [er_functionpermsetting.md](./er_functionpermsetting.md) |
| 14 | `t_er_functionpermsetting_l` | 功能权限设置-多语言表 | 4 | [er_functionpermsetting.md](./er_functionpermsetting.md) |
| 15 | `t_er_functionpermsetting_m` | 功能权限设置-使用范围位图表 | 2 | [er_functionpermsetting.md](./er_functionpermsetting.md) |
| 16 | `t_er_functionpermsetting_u` | 功能权限设置-使用范围表 | 3 | [er_functionpermsetting.md](./er_functionpermsetting.md) |
| 17 | `t_er_futureweather` | 未来七天天气-子表 | 8 | [er_tripweather.md](./er_tripweather.md) |
| 18 | `t_er_hotelbill` | 员工酒店订单-主表 | 70 | [er_staffhotelbill.md](./er_staffhotelbill.md) |
| 19 | `t_er_integralrecord` | 累计积分记录-主表 | 31 | [er_integralrecord.md](./er_integralrecord.md) |
| 20 | `t_er_integralrecord_l` | 累计积分记录-多语言表 | 4 | [er_integralrecord.md](./er_integralrecord.md) |
| 21 | `t_er_integralrecord_m` | 累计积分记录-使用范围位图表 | 2 | [er_integralrecord.md](./er_integralrecord.md) |
| 22 | `t_er_integralrecord_u` | 累计积分记录-使用范围表 | 3 | [er_integralrecord.md](./er_integralrecord.md) |
| 23 | `t_er_integralrecordentry` | 单据体-子表 | 7 | [er_integralrecord.md](./er_integralrecord.md) |
| 24 | `t_er_mannualpay` | 手动付款记录表-主表 | 4 | [er_manualpay.md](./er_manualpay.md) |
| 25 | `t_er_manualrepay` | 手动收款记录表-主表 | 4 | [er_manualrepay.md](./er_manualrepay.md) |
| 26 | `t_er_planebill` | 员工机票订单-主表 | 102 | [er_staffplanebill.md](./er_staffplanebill.md) |
| 27 | `t_er_planebill_a` | 员工机票订单-分表 | 5 | [er_staffplanebill.md](./er_staffplanebill.md) |
| 28 | `t_er_stdconfig` | 费用全局配置-主表 | 4 | [er_stdconfig.md](./er_stdconfig.md) |
| 29 | `t_er_timelinedata` | 我的足迹中城市对应描述数据-主表 | 5 | [er_timelinedata.md](./er_timelinedata.md) |
| 30 | `t_er_timelinedata_l` | 我的足迹中城市对应描述数据-多语言表 | 6 | [er_timelinedata.md](./er_timelinedata.md) |
| 31 | `t_er_tripsettingdata` | 个人设置-主表 | 10 | [er_tripsettingdata.md](./er_tripsettingdata.md) |
| 32 | `t_er_tripweather` | 天气贴士天气数据-主表 | 4 | [er_tripweather.md](./er_tripweather.md) |
| 33 | `t_er_weathercitycode` | 天气贴士城市天气链接-主表 | 6 | [er_tripweathercity.md](./er_tripweathercity.md) |
| 34 | `t_receipt_encodemapping` | 发票云-编码映射-主表 | 0 | [er_receipt_encodemapping.md](./er_receipt_encodemapping.md) |
| 35 | `t_receipt_encodemapping_l` | 发票云-编码映射-多语言表 | 0 | [er_receipt_encodemapping.md](./er_receipt_encodemapping.md) |
