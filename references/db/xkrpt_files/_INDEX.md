# xkrpt 模块表清单

> 本模块共收录 **85** 张表定义，来自 `xkrpt_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category xkrpt
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bd_debugtrace` | 调试日志统一管控-主表 | 10 | [xkrpt_debug_trace.md](./xkrpt_debug_trace.md) |
| 2 | `t_xkcr_rptreportinfo` | 单据体-子表 | 8 | [xkrpt_report.md](./xkrpt_report.md) |
| 3 | `t_xkrpt_autocreaterptlog` | 自动生成方案执行记录-主表 | 17 | [xkrpt_autocreatereportlog.md](./xkrpt_autocreatereportlog.md) |
| 4 | `t_xkrpt_autorptlogentry` | 报表生成信息-子表 | 11 | [xkrpt_autocreatereportlog.md](./xkrpt_autocreatereportlog.md) |
| 5 | `t_xkrpt_cts_diffdataitem` | 差异项目公式设置单据体-子表 | 6 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 6 | `t_xkrpt_cts_formula` | 单据体-子表 | 5 | [xkrpt_translation_method.md](./xkrpt_translation_method.md) |
| 7 | `t_xkrpt_cts_log_itementry` | 项目明细-子表 | 9 | [xkrpt_currencytranslog.md](./xkrpt_currencytranslog.md) |
| 8 | `t_xkrpt_cts_log_rptentry` | 报表明细-子表 | 12 | [xkrpt_currencytranslog.md](./xkrpt_currencytranslog.md) |
| 9 | `t_xkrpt_currencyscheme` | 折算方案-主表 | 20 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 10 | `t_xkrpt_currencyscheme_l` | 折算方案-多语言表 | 5 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 11 | `t_xkrpt_currencytranslog` | 外币折算日志-主表 | 10 | [xkrpt_currencytranslog.md](./xkrpt_currencytranslog.md) |
| 12 | `t_xkrpt_currscheme_curr` | 币别-多选基础资料表 | 3 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 13 | `t_xkrpt_currscheme_item` | 报表项目-多选基础资料表 | 3 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 14 | `t_xkrpt_currscheme_org` | 组织-多选基础资料表 | 3 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 15 | `t_xkrpt_currscheme_scope` | 合并范围-多选基础资料表 | 3 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 16 | `t_xkrpt_currscheme_temp` | 报表模板-多选基础资料表 | 3 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 17 | `t_xkrpt_currscheme_type` | 项目数据类型-多选基础资料表 | 3 | [xkrpt_currencyscheme.md](./xkrpt_currencyscheme.md) |
| 18 | `t_xkrpt_dimension` | 维度-主表 | 20 | [xkrpt_dimension.md](./xkrpt_dimension.md) |
| 19 | `t_xkrpt_dimension_l` | 维度-多语言表 | 5 | [xkrpt_dimension.md](./xkrpt_dimension.md) |
| 20 | `t_xkrpt_dimensionentry` | 单据体-子表 | 9 | [xkrpt_rptitemdimension.md](./xkrpt_rptitemdimension.md) |
| 21 | `t_xkrpt_dimensionmap` | 核算维度单据体-子表 | 6 | [xkrpt_recategorizescheme.md](./xkrpt_recategorizescheme.md) |
| 22 | `t_xkrpt_formulacalresult` | 单据体-子表 | 8 | [xkrpt_verifychkresult.md](./xkrpt_verifychkresult.md) |
| 23 | `t_xkrpt_formularegister` | 公式登记表-主表 | 7 | [xkrpt_formularegister.md](./xkrpt_formularegister.md) |
| 24 | `t_xkrpt_func_condition` | 取数参数-子表 | 9 | [xkrpt_func_define.md](./xkrpt_func_define.md) |
| 25 | `t_xkrpt_func_condition_l` | 取数参数-多语言表 | 4 | [xkrpt_func_define.md](./xkrpt_func_define.md) |
| 26 | `t_xkrpt_func_define` | 自定义函数-主表 | 18 | [xkrpt_func_define.md](./xkrpt_func_define.md) |
| 27 | `t_xkrpt_func_define_l` | 自定义函数-多语言表 | 6 | [xkrpt_func_define.md](./xkrpt_func_define.md) |
| 28 | `t_xkrpt_func_paradefine` | 取数参数管理-主表 | 17 | [xkrpt_func_paradefine.md](./xkrpt_func_paradefine.md) |
| 29 | `t_xkrpt_func_paradefine_l` | 取数参数管理-多语言表 | 5 | [xkrpt_func_paradefine.md](./xkrpt_func_paradefine.md) |
| 30 | `t_xkrpt_func_value_para` | 取数设置-子表 | 6 | [xkrpt_func_define.md](./xkrpt_func_define.md) |
| 31 | `t_xkrpt_hiscurrency` | 项目历史变动记录-主表 | 12 | [xkrpt_hiscurrency.md](./xkrpt_hiscurrency.md) |
| 32 | `t_xkrpt_hiscurrency_l` | 项目历史变动记录-多语言表 | 4 | [xkrpt_hiscurrency.md](./xkrpt_hiscurrency.md) |
| 33 | `t_xkrpt_hiscurrencyentry` | 单据体-子表 | 8 | [xkrpt_hiscurrency.md](./xkrpt_hiscurrency.md) |
| 34 | `t_xkrpt_home_kpi` | 首页关键指标-主表 | 12 | [xkrpt_home_kpi.md](./xkrpt_home_kpi.md) |
| 35 | `t_xkrpt_home_kpi_l` | 首页关键指标-多语言表 | 4 | [xkrpt_home_kpi.md](./xkrpt_home_kpi.md) |
| 36 | `t_xkrpt_internalparams` | 系统内部应用参数(存储数据)-主表 | 10 | [xkrpt_internalparams.md](./xkrpt_internalparams.md) |
| 37 | `t_xkrpt_itemrelaallocinfo` | 分配信息-子表 | 7 | [xkrpt_itemrelation.md](./xkrpt_itemrelation.md) |
| 38 | `t_xkrpt_itemrelation` | 项目勾稽关系-主表 | 20 | [xkrpt_itemrelation.md](./xkrpt_itemrelation.md) |
| 39 | `t_xkrpt_itemrelation_l` | 项目勾稽关系-多语言表 | 5 | [xkrpt_itemrelation.md](./xkrpt_itemrelation.md) |
| 40 | `t_xkrpt_presetstyle` | 预置表样-主表 | 24 | [xkrpt_sample_presetstyle.md](./xkrpt_sample_presetstyle.md) |
| 41 | `t_xkrpt_presetstyle_l` | 预置表样-多语言表 | 4 | [xkrpt_sample_presetstyle.md](./xkrpt_sample_presetstyle.md) |
| 42 | `t_xkrpt_presetstylegroup` | 预置表样分组-主表 | 14 | [xkrpt_presetstylegroup.md](./xkrpt_presetstylegroup.md) |
| 43 | `t_xkrpt_presetstylegroup_l` | 预置表样分组-多语言表 | 4 | [xkrpt_presetstylegroup.md](./xkrpt_presetstylegroup.md) |
| 44 | `t_xkrpt_projcurrencytran` | 报表项目关联折算方法-主表 | 14 | [xkrpt_projectcurrencytran.md](./xkrpt_projectcurrencytran.md) |
| 45 | `t_xkrpt_projcurrencytran_l` | 报表项目关联折算方法-多语言表 | 5 | [xkrpt_projectcurrencytran.md](./xkrpt_projectcurrencytran.md) |
| 46 | `t_xkrpt_projcurrtranentry` | 单据体-子表 | 7 | [xkrpt_projectcurrencytran.md](./xkrpt_projectcurrencytran.md) |
| 47 | `t_xkrpt_recategoryscheme` | 净额重分类方案-主表 | 18 | [xkrpt_recategorizescheme.md](./xkrpt_recategorizescheme.md) |
| 48 | `t_xkrpt_recategoryscheme_l` | 净额重分类方案-多语言表 | 5 | [xkrpt_recategorizescheme.md](./xkrpt_recategorizescheme.md) |
| 49 | `t_xkrpt_reschemedatatype` | 项目数据类型-多选基础资料表 | 3 | [xkrpt_recategorizescheme.md](./xkrpt_recategorizescheme.md) |
| 50 | `t_xkrpt_rpt` | 历史报表备查-主表 | 47 | [xkrpt_historyreport.md](./xkrpt_historyreport.md) |
| 51 | `t_xkrpt_rpt` | 报表-主表 | 47 | [xkrpt_report.md](./xkrpt_report.md) |
| 52 | `t_xkrpt_rpt` | api工具报表-主表 | 47 | [xkrpt_reportbase_apitool.md](./xkrpt_reportbase_apitool.md) |
| 53 | `t_xkrpt_rpt` | 报表模板-主表 | 47 | [xkrpt_rptsample.md](./xkrpt_rptsample.md) |
| 54 | `t_xkrpt_rpt_l` | 历史报表备查-多语言表 | 4 | [xkrpt_historyreport.md](./xkrpt_historyreport.md) |
| 55 | `t_xkrpt_rpt_l` | 报表-多语言表 | 4 | [xkrpt_report.md](./xkrpt_report.md) |
| 56 | `t_xkrpt_rpt_l` | api工具报表-多语言表 | 4 | [xkrpt_reportbase_apitool.md](./xkrpt_reportbase_apitool.md) |
| 57 | `t_xkrpt_rpt_l` | 报表模板-多语言表 | 4 | [xkrpt_rptsample.md](./xkrpt_rptsample.md) |
| 58 | `t_xkrpt_rptautocrt` | 报表自动生成方案-主表 | 23 | [xkrpt_rptautocrt.md](./xkrpt_rptautocrt.md) |
| 59 | `t_xkrpt_rptautocrt_l` | 报表自动生成方案-多语言表 | 5 | [xkrpt_rptautocrt.md](./xkrpt_rptautocrt.md) |
| 60 | `t_xkrpt_rptautocrtentry` | 报表范围分录-子表 | 17 | [xkrpt_rptautocrt.md](./xkrpt_rptautocrt.md) |
| 61 | `t_xkrpt_rptbasegroup` | 报表模板分组-主表 | 10 | [xkrpt_basegroup.md](./xkrpt_basegroup.md) |
| 62 | `t_xkrpt_rptbasegroup_l` | 报表模板分组-多语言表 | 4 | [xkrpt_basegroup.md](./xkrpt_basegroup.md) |
| 63 | `t_xkrpt_rptitemdimension` | 项目维度数据-主表 | 8 | [xkrpt_rptitemdimension.md](./xkrpt_rptitemdimension.md) |
| 64 | `t_xkrpt_sheet` | 单据体-子表 | 14 | [xkrpt_historyreport.md](./xkrpt_historyreport.md) |
| 65 | `t_xkrpt_sheet` | 单据体-子表 | 14 | [xkrpt_report.md](./xkrpt_report.md) |
| 66 | `t_xkrpt_sheet` | 单据体-子表 | 14 | [xkrpt_reportbase_apitool.md](./xkrpt_reportbase_apitool.md) |
| 67 | `t_xkrpt_sheet` | 单据体-子表 | 14 | [xkrpt_rptsample.md](./xkrpt_rptsample.md) |
| 68 | `t_xkrpt_trans_method` | 外币折算方法-主表 | 14 | [xkrpt_translation_method.md](./xkrpt_translation_method.md) |
| 69 | `t_xkrpt_trans_method_l` | 外币折算方法-多语言表 | 5 | [xkrpt_translation_method.md](./xkrpt_translation_method.md) |
| 70 | `t_xkrpt_trans_track` | 折算过程-主表 | 18 | [xkrpt_transtation_track.md](./xkrpt_transtation_track.md) |
| 71 | `t_xkrpt_trans_track_entry` | 单据体-子表 | 7 | [xkrpt_transtation_track.md](./xkrpt_transtation_track.md) |
| 72 | `t_xkrpt_verifyfunc` | 表内检查公式-主表 | 19 | [xkrpt_verification.md](./xkrpt_verification.md) |
| 73 | `t_xkrpt_verifyfunc_l` | 表内检查公式-多语言表 | 5 | [xkrpt_verification.md](./xkrpt_verification.md) |
| 74 | `t_xkrpt_verifyfuncctrl` | 单据体-子表 | 5 | [xkrpt_verification.md](./xkrpt_verification.md) |
| 75 | `t_xkrpt_verifyresult` | 勾稽关系检查结果-主表 | 17 | [xkrpt_verifychkresult.md](./xkrpt_verifychkresult.md) |
| 76 | `t_xkrpt_verifyresult_l` | 勾稽关系检查结果-多语言表 | 4 | [xkrpt_verifychkresult.md](./xkrpt_verifychkresult.md) |
| 77 | `t_xkrpt_wizarddatatype` | 项目数据类型单据体-子表 | 10 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 78 | `t_xkrpt_wizarddimedata` | 模板样式方案维度数据-主表 | 7 | [xkrpt_wizarddimedata.md](./xkrpt_wizarddimedata.md) |
| 79 | `t_xkrpt_wizarddimension` | 报告维度单据体-子表 | 7 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 80 | `t_xkrpt_wizardformula` | 取数设置单据体-子表 | 9 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 81 | `t_xkrpt_wizardformula_l` | 取数设置单据体-多语言表 | 4 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 82 | `t_xkrpt_wizarditem` | 报表项目单据体-子表 | 6 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 83 | `t_xkrpt_wizardscheme` | 模板样式方案-主表 | 44 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 84 | `t_xkrpt_wizardscheme_l` | 模板样式方案-多语言表 | 5 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
| 85 | `t_xkrpt_wizardspformula` | 特殊取数单据体-子表 | 7 | [xkrpt_wizardscheme.md](./xkrpt_wizardscheme.md) |
