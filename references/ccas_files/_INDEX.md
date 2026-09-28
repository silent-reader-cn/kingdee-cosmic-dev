# ccas 模块表清单

> 本模块共收录 **16** 张表定义，来自 `ccas_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope ccas
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ccas_cisconfig` | 集成服务配置-主表 | 17 | [ccas_cisconfig.md](./ccas_cisconfig.md) |
| 2 | `t_ccas_cisconfig` | 集成服务配置-主表 | 17 | [ccas_cisconfig2.md](./ccas_cisconfig2.md) |
| 3 | `t_ccas_cisconfig_entry` | 单据体-子表 | 5 | [ccas_cisconfig.md](./ccas_cisconfig.md) |
| 4 | `t_ccas_cisconfig_l` | 集成服务配置-多语言表 | 0 | [ccas_cisconfig2.md](./ccas_cisconfig2.md) |
| 5 | `t_ccas_ciservice` | 集成服务（GCP）-主表 | 0 | [ccas_ciservice.md](./ccas_ciservice.md) |
| 6 | `t_ccas_ciservice_l` | 集成服务（GCP）-多语言表 | 0 | [ccas_ciservice.md](./ccas_ciservice.md) |
| 7 | `t_ccas_clearsetting` | 清理集成日志设置-主表 | 3 | [ccas_clearsetting.md](./ccas_clearsetting.md) |
| 8 | `t_ccas_esenterprice` | 法人企业-主表 | 27 | [ccas_esenterprice.md](./ccas_esenterprice.md) |
| 9 | `t_ccas_esenterprice_l` | 法人企业-多语言表 | 4 | [ccas_esenterprice.md](./ccas_esenterprice.md) |
| 10 | `t_ccas_esignprovider` | 电子签章服务商-主表 | 14 | [ccas_esserviceprovider.md](./ccas_esserviceprovider.md) |
| 11 | `t_ccas_esignprovider_l` | 电子签章服务商-多语言表 | 5 | [ccas_esserviceprovider.md](./ccas_esserviceprovider.md) |
| 12 | `t_ccas_esignprovider_p` | 电子签章服务商-分表 | 8 | [ccas_esserviceprovider.md](./ccas_esserviceprovider.md) |
| 13 | `t_ccas_integratedlog` | 集成日志-主表 | 19 | [ccas_integratedlog.md](./ccas_integratedlog.md) |
| 14 | `t_ccas_integratedlog_l` | 集成日志-多语言表 | 5 | [ccas_integratedlog.md](./ccas_integratedlog.md) |
| 15 | `t_ccas_integratedmanage` | 集成服务商管理-主表 | 9 | [ccas_integratedmanage.md](./ccas_integratedmanage.md) |
| 16 | `t_ccas_shrintegration` | s-HR集成配置-主表 | 12 | [ccas_shrintegration.md](./ccas_shrintegration.md) |
