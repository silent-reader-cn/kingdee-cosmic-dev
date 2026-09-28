# invsm 模块表清单

> 本模块共收录 **15** 张表定义，来自 `invsm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope invsm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_invsm_apiconfig_setting` | 接口全局配置-主表 | 3 | [invsm_apiconfig_setting.md](./invsm_apiconfig_setting.md) |
| 2 | `t_invsm_bus_sys_config` | 第三方应用接入配置-主表 | 15 | [invsm_app_access_config.md](./invsm_app_access_config.md) |
| 3 | `t_invsm_callback_addr` | 同步财务云应收发票回调地址-主表 | 16 | [invsm_callback_addr.md](./invsm_callback_addr.md) |
| 4 | `t_invsm_callback_log` | 发票回推日志-主表 | 25 | [invsm_callback_log.md](./invsm_callback_log.md) |
| 5 | `t_invsm_config_mgr` | 参数配置管理-主表 | 4 | [invsm_config_mgr.md](./invsm_config_mgr.md) |
| 6 | `t_invsm_goodsinfo_setting` | 默认开票项-主表 | 14 | [invsm_goodsinfo_setting.md](./invsm_goodsinfo_setting.md) |
| 7 | `t_invsm_input_query` | 进项查询配置-主表 | 0 | [invsm_input_query.md](./invsm_input_query.md) |
| 8 | `t_invsm_input_query_exp` | 导出字段单据体-子表 | 0 | [invsm_input_query.md](./invsm_input_query.md) |
| 9 | `t_invsm_input_query_list` | 查询字段单据体-子表 | 0 | [invsm_input_query.md](./invsm_input_query.md) |
| 10 | `t_invsm_input_queryfilter` | 常用条件单据体-子表 | 0 | [invsm_input_query.md](./invsm_input_query.md) |
| 11 | `t_invsm_inv_item_setting` | 开票项设置-主表 | 11 | [invsm_inv_item_setting.md](./invsm_inv_item_setting.md) |
| 12 | `t_invsm_invoice_check` | 对账记录表-主表 | 3 | [invsm_invoice_check.md](./invsm_invoice_check.md) |
| 13 | `t_invsm_param_config` | 参数配置单据-主表 | 5 | [invsm_param_configuration.md](./invsm_param_configuration.md) |
| 14 | `t_invsm_qr_callback_log` | 扫码开票发票数据回传移动云-主表 | 11 | [invsm_qr_callback_log.md](./invsm_qr_callback_log.md) |
| 15 | `t_invsm_system_setting` | 系统设置-主表 | 3 | [invsm_system_setting.md](./invsm_system_setting.md) |
