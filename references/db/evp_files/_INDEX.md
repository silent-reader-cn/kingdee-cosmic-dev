# evp 模块表清单

> 本模块共收录 **34** 张表定义，来自 `evp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category evp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_evp_atrreceiver` | 航空客票行程单-主表 | 43 | [evp_atrreceiver.md](./evp_atrreceiver.md) |
| 2 | `t_evp_bkerreceiver` | 银行电子回单-主表 | 44 | [evp_bkerreceiver.md](./evp_bkerreceiver.md) |
| 3 | `t_evp_bkrs` | 银行对账单-主表 | 45 | [evp_bkrs.md](./evp_bkrs.md) |
| 4 | `t_evp_bkrsentry` | 单据体-子表 | 22 | [evp_bkrs.md](./evp_bkrs.md) |
| 5 | `t_evp_daptracker` | 电子凭证关系-主表 | 4 | [evp_daptracker.md](./evp_daptracker.md) |
| 6 | `t_evp_dataconfig` | 数据来源配置-主表 | 0 | [evp_dataconfig.md](./evp_dataconfig.md) |
| 7 | `t_evp_dataconfigorgs` | 核算组织-多选基础资料表 | 0 | [evp_dataconfig.md](./evp_dataconfig.md) |
| 8 | `t_evp_efi` | 财政电子票据-主表 | 41 | [evp_efi.md](./evp_efi.md) |
| 9 | `t_evp_einvordreceiver` | 数电票普通发票-主表 | 55 | [evp_einvordreceiver.md](./evp_einvordreceiver.md) |
| 10 | `t_evp_einvspclreceiver` | 数电票专用发票-主表 | 60 | [evp_einvspclreceiver.md](./evp_einvspclreceiver.md) |
| 11 | `t_evp_elevouchertype` | 电子凭证类型-主表 | 12 | [evp_elevouchertype.md](./evp_elevouchertype.md) |
| 12 | `t_evp_elevouchertype_l` | 电子凭证类型-多语言表 | 4 | [evp_elevouchertype.md](./evp_elevouchertype.md) |
| 13 | `t_evp_evtentity` | 字段配置-子表 | 13 | [evp_elevouchertype.md](./evp_elevouchertype.md) |
| 14 | `t_evp_exporttask` | 电子凭证导出日志-主表 | 23 | [evp_exporttask.md](./evp_exporttask.md) |
| 15 | `t_evp_invoiceentry` | 票证关系-主表 | 0 | [evp_invoicevchrel.md](./evp_invoicevchrel.md) |
| 16 | `t_evp_invordreceiver` | 增值税普通发票-主表 | 55 | [evp_invordreceiver.md](./evp_invordreceiver.md) |
| 17 | `t_evp_invspclreceiver` | 增值税专用发票-主表 | 60 | [evp_invspclreceiver.md](./evp_invspclreceiver.md) |
| 18 | `t_evp_invtlfreceiver` | 公路增值税普票-主表 | 56 | [evp_invtlfreceiver.md](./evp_invtlfreceiver.md) |
| 19 | `t_evp_mulsourcesys` | 来源系统-多选基础资料表 | 3 | [evp_originsys_config.md](./evp_originsys_config.md) |
| 20 | `t_evp_ntrevgpmreceiver` | 非税收入缴款书-主表 | 41 | [evp_ntrevgpmreceiver.md](./evp_ntrevgpmreceiver.md) |
| 21 | `t_evp_orgsocialcode` | 统一社会信用代码-主表 | 11 | [evp_org_socialcode.md](./evp_org_socialcode.md) |
| 22 | `t_evp_orgsocialcode_l` | 统一社会信用代码-多语言表 | 4 | [evp_org_socialcode.md](./evp_org_socialcode.md) |
| 23 | `t_evp_originsys` | 集成系统配置-主表 | 12 | [evp_originsys.md](./evp_originsys.md) |
| 24 | `t_evp_originsys_config` | 票据类型来源系统配置-主表 | 7 | [evp_originsys_config.md](./evp_originsys_config.md) |
| 25 | `t_evp_originsys_l` | 集成系统配置-多语言表 | 4 | [evp_originsys.md](./evp_originsys.md) |
| 26 | `t_evp_queryinterface` | 发票类电子凭证池数据查询接口-主表 | 12 | [evp_queryinterface.md](./evp_queryinterface.md) |
| 27 | `t_evp_raireceiver` | 铁路客票行程单-主表 | 43 | [evp_raireceiver.md](./evp_raireceiver.md) |
| 28 | `t_evp_schedule` | 抽取数据调度计划-主表 | 22 | [evp_schedule.md](./evp_schedule.md) |
| 29 | `t_evp_schedule_l` | 抽取数据调度计划-多语言表 | 4 | [evp_schedule.md](./evp_schedule.md) |
| 30 | `t_evp_schedulebooks` | 适用账簿-多选基础资料表 | 3 | [evp_schedule.md](./evp_schedule.md) |
| 31 | `t_evp_sysparam` | 电子凭证池系统配置-主表 | 4 | [evp_sysconfig.md](./evp_sysconfig.md) |
| 32 | `t_evp_voucher` | 凭证-主表 | 30 | [evp_voucher.md](./evp_voucher.md) |
| 33 | `t_evp_voucher` | 凭证-主表 | 30 | [evp_voucherbasedata.md](./evp_voucherbasedata.md) |
| 34 | `t_evp_voucherentry` | 单据体-子表 | 7 | [evp_voucher.md](./evp_voucher.md) |
