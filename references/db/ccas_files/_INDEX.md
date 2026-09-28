# ccas 模块表清单

> 本模块共收录 **41** 张表定义，来自 `ccas_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ccas
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ccas_cisconfig` | 集成服务配置-主表 | 22 | [ccas_cisconfig.md](./ccas_cisconfig.md) |
| 2 | `t_ccas_cisconfig` | 集成服务配置-主表 | 22 | [ccas_cisconfig2.md](./ccas_cisconfig2.md) |
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
| 13 | `t_ccas_integratedlog` | 集成日志-主表 | 20 | [ccas_integratedlog.md](./ccas_integratedlog.md) |
| 14 | `t_ccas_integratedlog_l` | 集成日志-多语言表 | 5 | [ccas_integratedlog.md](./ccas_integratedlog.md) |
| 15 | `t_ccas_integratedmanage` | 集成服务商管理-主表 | 9 | [ccas_integratedmanage.md](./ccas_integratedmanage.md) |
| 16 | `t_ccas_membermanage` | 成员管理-主表 | 13 | [ccas_membermanage.md](./ccas_membermanage.md) |
| 17 | `t_ccas_membermanage_l` | 成员管理-多语言表 | 3 | [ccas_membermanage.md](./ccas_membermanage.md) |
| 18 | `t_ccas_membermanagerole` | 电子签章角色-多选基础资料表 | 3 | [ccas_membermanage.md](./ccas_membermanage.md) |
| 19 | `t_ccas_memberrole` | 电子签章角色-主表 | 10 | [ccas_memberrole.md](./ccas_memberrole.md) |
| 20 | `t_ccas_memberrole_l` | 电子签章角色-多语言表 | 4 | [ccas_memberrole.md](./ccas_memberrole.md) |
| 21 | `t_ccas_param` | 参数配置-主表 | 11 | [ccas_param.md](./ccas_param.md) |
| 22 | `t_ccas_param_l` | 参数配置-多语言表 | 4 | [ccas_param.md](./ccas_param.md) |
| 23 | `t_ccas_relativeenterprise` | 相对方法人企业-主表 | 15 | [ccas_relativeenterprise.md](./ccas_relativeenterprise.md) |
| 24 | `t_ccas_relativeenterprise_l` | 相对方法人企业-多语言表 | 3 | [ccas_relativeenterprise.md](./ccas_relativeenterprise.md) |
| 25 | `t_ccas_shrintegration` | s-HR集成配置（废弃）-主表 | 12 | [ccas_shrintegration.md](./ccas_shrintegration.md) |
| 26 | `t_ccas_signature_entry` | 单据体-子表 | 14 | [ccas_signatureconfig.md](./ccas_signatureconfig.md) |
| 27 | `t_ccas_signatureconfig` | 签章配置-主表 | 5 | [ccas_signatureconfig.md](./ccas_signatureconfig.md) |
| 28 | `t_ccas_signatureconfig_l` | 签章配置-多语言表 | 3 | [ccas_signatureconfig.md](./ccas_signatureconfig.md) |
| 29 | `t_ccas_signrule` | 规则设置-主表 | 12 | [ccas_signconfigrule.md](./ccas_signconfigrule.md) |
| 30 | `t_ccas_signrule_l` | 规则设置-多语言表 | 3 | [ccas_signconfigrule.md](./ccas_signconfigrule.md) |
| 31 | `t_ccas_signruleentry` | 参与方-子表 | 14 | [ccas_signconfigrule.md](./ccas_signconfigrule.md) |
| 32 | `t_ccas_signtask` | 签署任务-主表 | 20 | [ccas_signtask.md](./ccas_signtask.md) |
| 33 | `t_ccas_signtask_actors` | 参与方-子表 | 11 | [ccas_signtask.md](./ccas_signtask.md) |
| 34 | `t_gsc_cv_apiconfig` | 海关接口配置-主表 | 12 | [gsc_cvapi_config.md](./gsc_cvapi_config.md) |
| 35 | `t_gsc_cv_apiconfig_l` | 海关接口配置-多语言表 | 3 | [gsc_cvapi_config.md](./gsc_cvapi_config.md) |
| 36 | `t_gsc_cv_provider` | 海关服务商-主表 | 14 | [gsc_customs_provider.md](./gsc_customs_provider.md) |
| 37 | `t_gsc_cv_provider_l` | 海关服务商-多语言表 | 4 | [gsc_customs_provider.md](./gsc_customs_provider.md) |
| 38 | `t_gsc_iv_apiconfig` | 发票接口配置-主表 | 12 | [gsc_ivapi_config.md](./gsc_ivapi_config.md) |
| 39 | `t_gsc_iv_apiconfig_l` | 发票接口配置-多语言表 | 3 | [gsc_ivapi_config.md](./gsc_ivapi_config.md) |
| 40 | `t_gsc_iv_provider` | 发票服务商-主表 | 14 | [gsc_invoice_provider.md](./gsc_invoice_provider.md) |
| 41 | `t_gsc_iv_provider_l` | 发票服务商-多语言表 | 4 | [gsc_invoice_provider.md](./gsc_invoice_provider.md) |
