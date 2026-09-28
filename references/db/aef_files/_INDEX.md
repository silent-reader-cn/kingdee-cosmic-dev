# aef 模块表清单

> 本模块共收录 **39** 张表定义，来自 `aef_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category aef
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aef_acelre_rpt_log` | 报表归档记录查询-主表 | 35 | [aef_acelre_rpt.md](./aef_acelre_rpt.md) |
| 2 | `t_aef_archieve_imagepath` | 归档影像路径-主表 | 8 | [aef_archieve_imagepath.md](./aef_archieve_imagepath.md) |
| 3 | `t_aef_archive_log` | 归档记录查询-主表 | 27 | [aef_acelre.md](./aef_acelre.md) |
| 4 | `t_aef_archiveconfig` | 归档配置记录-主表 | 6 | [aef_archieveconfig.md](./aef_archieveconfig.md) |
| 5 | `t_aef_archiveentry` | 归档数据-子表 | 21 | [aef_archivescheme.md](./aef_archivescheme.md) |
| 6 | `t_aef_archivegroup` | 归档分组-主表 | 15 | [aef_archivegroup.md](./aef_archivegroup.md) |
| 7 | `t_aef_archivegroup_l` | 归档分组-多语言表 | 5 | [aef_archivegroup.md](./aef_archivegroup.md) |
| 8 | `t_aef_archivescheme` | 归档方案-主表 | 20 | [aef_archivescheme.md](./aef_archivescheme.md) |
| 9 | `t_aef_archivescheme_l` | 归档方案-多语言表 | 5 | [aef_archivescheme.md](./aef_archivescheme.md) |
| 10 | `t_aef_archivescheme_u` | 归档方案-使用范围表 | 3 | [aef_archivescheme.md](./aef_archivescheme.md) |
| 11 | `t_aef_archivetax_log` | 税务归档记录查询-主表 | 31 | [aef_acelre_tax.md](./aef_acelre_tax.md) |
| 12 | `t_aef_archivewriteconfig` | 归档反写配置-主表 | 5 | [aef_archivewriteconfig.md](./aef_archivewriteconfig.md) |
| 13 | `t_aef_atrreceiver` | 航空运输电子客票行程单-主表 | 21 | [aef_atrreceiver.md](./aef_atrreceiver.md) |
| 14 | `t_aef_atrreceiverentry` | 单据体-子表 | 8 | [aef_atrreceiver.md](./aef_atrreceiver.md) |
| 15 | `t_aef_billconfig` | 业务单据配置-主表 | 11 | [aef_billconfig.md](./aef_billconfig.md) |
| 16 | `t_aef_bkerreceiver` | 银行电子回单-主表 | 24 | [aef_bkerreceiver.md](./aef_bkerreceiver.md) |
| 17 | `t_aef_bkerreceiverentry` | 单据体-子表 | 8 | [aef_bkerreceiver.md](./aef_bkerreceiver.md) |
| 18 | `t_aef_bkrs` | 银行对账单-主表 | 24 | [aef_bkrs.md](./aef_bkrs.md) |
| 19 | `t_aef_bkrsentry` | 单据体-子表 | 22 | [aef_bkrs.md](./aef_bkrs.md) |
| 20 | `t_aef_efi` | 财政电子票据-主表 | 18 | [aef_efi.md](./aef_efi.md) |
| 21 | `t_aef_efientry` | 单据体-子表 | 8 | [aef_efi.md](./aef_efi.md) |
| 22 | `t_aef_einvordentry` | 单据体-子表 | 8 | [aef_einvordreceiver.md](./aef_einvordreceiver.md) |
| 23 | `t_aef_einvordreceiver` | 数电票普通发票-主表 | 33 | [aef_einvordreceiver.md](./aef_einvordreceiver.md) |
| 24 | `t_aef_einvspclentry` | 单据体-子表 | 8 | [aef_einvspclreceiver.md](./aef_einvspclreceiver.md) |
| 25 | `t_aef_einvspclreceiver` | 数电票专用发票-主表 | 38 | [aef_einvspclreceiver.md](./aef_einvspclreceiver.md) |
| 26 | `t_aef_errorlog` | 归档错误日志-主表 | 9 | [aef_errorlog.md](./aef_errorlog.md) |
| 27 | `t_aef_invordreceiver` | 增值税电子普通发票-主表 | 33 | [aef_invordreceiver.md](./aef_invordreceiver.md) |
| 28 | `t_aef_invordreceiverentry` | 单据体-子表 | 8 | [aef_invordreceiver.md](./aef_invordreceiver.md) |
| 29 | `t_aef_invspclreceiver` | 增值税电子专用发票-主表 | 38 | [aef_invspclreceiver.md](./aef_invspclreceiver.md) |
| 30 | `t_aef_invspclrentry` | 单据体-子表 | 8 | [aef_invspclreceiver.md](./aef_invspclreceiver.md) |
| 31 | `t_aef_invtlfreceiver` | 收费公路通行费增值税电子普通发票-主表 | 35 | [aef_invtlfreceiver.md](./aef_invtlfreceiver.md) |
| 32 | `t_aef_invtlfreceiverentry` | 单据体-子表 | 8 | [aef_invtlfreceiver.md](./aef_invtlfreceiver.md) |
| 33 | `t_aef_ntrevgpmentry` | 单据体-子表 | 8 | [aef_ntrevgpmreceiver.md](./aef_ntrevgpmreceiver.md) |
| 34 | `t_aef_ntrevgpmreceiver` | 非税收入一般缴款书-主表 | 18 | [aef_ntrevgpmreceiver.md](./aef_ntrevgpmreceiver.md) |
| 35 | `t_aef_raireceiver` | 铁路电子客票行程单-主表 | 21 | [aef_raireceiver.md](./aef_raireceiver.md) |
| 36 | `t_aef_raireceiverentry` | 单据体-子表 | 8 | [aef_raireceiver.md](./aef_raireceiver.md) |
| 37 | `t_aef_serviceconfig` | 归档服务器配置-主表 | 22 | [aef_serviceconfig.md](./aef_serviceconfig.md) |
| 38 | `t_aef_serviceconfig_l` | 归档服务器配置-多语言表 | 4 | [aef_serviceconfig.md](./aef_serviceconfig.md) |
| 39 | `t_aef_sysparam` | 电子档案系统配置-主表 | 4 | [aef_sysparam.md](./aef_sysparam.md) |
