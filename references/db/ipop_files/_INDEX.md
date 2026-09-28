# ipop 模块表清单

> 本模块共收录 **50** 张表定义，来自 `ipop_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ipop
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ipop_abc_item` | 入门必学事项-主表 | 3 | [ipop_abc_reading_itemcfg.md](./ipop_abc_reading_itemcfg.md) |
| 2 | `t_ipop_abc_itemcfg` | 入门必读事项配置-主表 | 16 | [ipop_abc_itemcfg.md](./ipop_abc_itemcfg.md) |
| 3 | `t_ipop_abc_itemcfg_l` | 入门必读事项配置-多语言表 | 4 | [ipop_abc_itemcfg.md](./ipop_abc_itemcfg.md) |
| 4 | `t_ipop_abc_modulecfg` | 入门必读模块配置-主表 | 12 | [ipop_abc_modulecfg.md](./ipop_abc_modulecfg.md) |
| 5 | `t_ipop_abc_modulecfg_l` | 入门必读模块配置-多语言表 | 4 | [ipop_abc_modulecfg.md](./ipop_abc_modulecfg.md) |
| 6 | `t_ipop_abc_result` | 入门必读用户学习统计-主表 | 7 | [ipop_abc_result.md](./ipop_abc_result.md) |
| 7 | `t_ipop_errloginfo` | 异常日志-主表 | 8 | [ipop_errloginfo.md](./ipop_errloginfo.md) |
| 8 | `t_ipop_groupentity` | 分组配置单据体-子表 | 4 | [ipop_resourcegrpconfig.md](./ipop_resourcegrpconfig.md) |
| 9 | `t_ipop_groupmodule` | 分组内模块-多选基础资料表 | 4 | [ipop_resourcegrpconfig.md](./ipop_resourcegrpconfig.md) |
| 10 | `t_ipop_init_item` | 初始化子任务单据-主表 | 9 | [ipop_init_bill_itemcfg.md](./ipop_init_bill_itemcfg.md) |
| 11 | `t_ipop_init_itemcfg` | 初始化事项配置-主表 | 22 | [ipop_init_itemcfg.md](./ipop_init_itemcfg.md) |
| 12 | `t_ipop_init_itemcfg_l` | 初始化事项配置-多语言表 | 4 | [ipop_init_itemcfg.md](./ipop_init_itemcfg.md) |
| 13 | `t_ipop_init_itemcfgentry` | 单据体-子表 | 4 | [ipop_init_itemcfg.md](./ipop_init_itemcfg.md) |
| 14 | `t_ipop_init_licgroupcfg` | 模块许可分组配置-主表 | 12 | [ipop_init_licgroupcfg.md](./ipop_init_licgroupcfg.md) |
| 15 | `t_ipop_init_licgroupcfg_l` | 模块许可分组配置-多语言表 | 4 | [ipop_init_licgroupcfg.md](./ipop_init_licgroupcfg.md) |
| 16 | `t_ipop_init_modulecfg` | 初始化模块配置-主表 | 22 | [ipop_init_modulecfg.md](./ipop_init_modulecfg.md) |
| 17 | `t_ipop_init_modulecfg_l` | 初始化模块配置-多语言表 | 4 | [ipop_init_modulecfg.md](./ipop_init_modulecfg.md) |
| 18 | `t_ipop_init_result` | 初始化标记结果-主表 | 8 | [ipop_init_result.md](./ipop_init_result.md) |
| 19 | `t_ipop_init_usercfg` | 初始化事项负责人-主表 | 9 | [ipop_init_usercfg.md](./ipop_init_usercfg.md) |
| 20 | `t_ipop_initbasedata` | 基础资料录入（废弃）-主表 | 11 | [ipop_initbasedata.md](./ipop_initbasedata.md) |
| 21 | `t_ipop_initbasedatatype` | 基础资料录入类型（废弃）-主表 | 9 | [ipop_initbasedatatype.md](./ipop_initbasedatatype.md) |
| 22 | `t_ipop_initbasedatatype_l` | 基础资料录入类型（废弃）-多语言表 | 5 | [ipop_initbasedatatype.md](./ipop_initbasedatatype.md) |
| 23 | `t_ipop_initcompany` | 企业信息维护（废弃）-主表 | 9 | [ipop_initcompany.md](./ipop_initcompany.md) |
| 24 | `t_ipop_initcompany_l` | 企业信息维护（废弃）-多语言表 | 4 | [ipop_initcompany.md](./ipop_initcompany.md) |
| 25 | `t_ipop_initdynamicdata` | 动态数据录入（废弃）-主表 | 11 | [ipop_initdynamicdata.md](./ipop_initdynamicdata.md) |
| 26 | `t_ipop_initdynamictype` | 动态数据录入类型（废弃）-主表 | 8 | [ipop_initdynamictype.md](./ipop_initdynamictype.md) |
| 27 | `t_ipop_initdynamictype_l` | 动态数据录入类型（废弃）-多语言表 | 5 | [ipop_initdynamictype.md](./ipop_initdynamictype.md) |
| 28 | `t_ipop_initendinitial` | 结束初始化（废弃）-主表 | 4 | [ipop_initendinitial.md](./ipop_initendinitial.md) |
| 29 | `t_ipop_initendinitial_l` | 结束初始化（废弃）-多语言表 | 4 | [ipop_initendinitial.md](./ipop_initendinitial.md) |
| 30 | `t_ipop_initgl` | 基础资料录入-总账-主表 | 0 | [ipop_initgl.md](./ipop_initgl.md) |
| 31 | `t_ipop_initperiodsetting` | 启用期间设置（废弃）-主表 | 0 | [ipop_initperiodsetting.md](./ipop_initperiodsetting.md) |
| 32 | `t_ipop_initsysconfig` | 系统基础配置（废弃）-主表 | 9 | [ipop_initsysconfig.md](./ipop_initsysconfig.md) |
| 33 | `t_ipop_initsysconfig_l` | 系统基础配置（废弃）-多语言表 | 4 | [ipop_initsysconfig.md](./ipop_initsysconfig.md) |
| 34 | `t_ipop_inituserperm` | 用户权限维护（废弃）-主表 | 9 | [ipop_inituserperm.md](./ipop_inituserperm.md) |
| 35 | `t_ipop_inituserperm_l` | 用户权限维护（废弃）-多语言表 | 4 | [ipop_inituserperm.md](./ipop_inituserperm.md) |
| 36 | `t_ipop_messagenotify` | 消息通知配置-主表 | 6 | [ipop_messagenotify.md](./ipop_messagenotify.md) |
| 37 | `t_ipop_resauxiliarydata` | 资源辅助资料-主表 | 4 | [ipop_resauxiliarydata.md](./ipop_resauxiliarydata.md) |
| 38 | `t_ipop_resauxiliarydata_l` | 资源辅助资料-多语言表 | 4 | [ipop_resauxiliarydata.md](./ipop_resauxiliarydata.md) |
| 39 | `t_ipop_resourcebaseconfig` | 资源基础资料配置-主表 | 10 | [ipop_resourcebaseconfig.md](./ipop_resourcebaseconfig.md) |
| 40 | `t_ipop_resourcegrpconfig` | 资源分组配置-主表 | 9 | [ipop_resourcegrpconfig.md](./ipop_resourcegrpconfig.md) |
| 41 | `t_ipop_resourcelistentity` | 资源清单明细-主表 | 19 | [ipop_resoucelistdetail.md](./ipop_resoucelistdetail.md) |
| 42 | `t_ipop_resourcelistentity` | 资源清单单据体-子表 | 19 | [ipop_resourcebaseconfig.md](./ipop_resourcebaseconfig.md) |
| 43 | `t_ipop_task_modulecfg` | 任务分配模块配置-主表 | 12 | [ipop_task_modulecfg.md](./ipop_task_modulecfg.md) |
| 44 | `t_ipop_task_modulecfg_l` | 任务分配模块配置-多语言表 | 4 | [ipop_task_modulecfg.md](./ipop_task_modulecfg.md) |
| 45 | `t_ipop_thresholdsetting` | 阈值配置-主表 | 8 | [ipop_thresholdsetting.md](./ipop_thresholdsetting.md) |
| 46 | `t_ipop_vipknowledge` | 社区知识管理-主表 | 14 | [ipop_vipknowledge.md](./ipop_vipknowledge.md) |
| 47 | `t_ipop_vipknowledge_l` | 社区知识管理-多语言表 | 4 | [ipop_vipknowledge.md](./ipop_vipknowledge.md) |
| 48 | `t_ipop_vipknowledgetag` | 社区知识标签-主表 | 11 | [ipop_vipknowledgetag.md](./ipop_vipknowledgetag.md) |
| 49 | `t_ipop_vipknowledgetag_l` | 社区知识标签-多语言表 | 4 | [ipop_vipknowledgetag.md](./ipop_vipknowledgetag.md) |
| 50 | `t_ipop_warningrecord` | 预警记录-主表 | 5 | [ipop_warningrecord.md](./ipop_warningrecord.md) |
