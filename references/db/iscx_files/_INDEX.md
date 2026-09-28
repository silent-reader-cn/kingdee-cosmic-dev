# iscx 模块表清单

> 本模块共收录 **30** 张表定义，来自 `iscx_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category iscx
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_iscx_catalog_systems` | 解决方案关联系统-多选基础资料表 | 3 | [iscx_catalog.md](./iscx_catalog.md) |
| 2 | `t_iscx_cntype_industry` | 连接类型_行业-主表 | 3 | [iscx_cntype_industry.md](./iscx_cntype_industry.md) |
| 3 | `t_iscx_connector` | 连接器-主表 | 11 | [iscx_connector.md](./iscx_connector.md) |
| 4 | `t_iscx_data_flow_define` | 数据流已发布定义-主表 | 24 | [iscx_data_flow_define.md](./iscx_data_flow_define.md) |
| 5 | `t_iscx_data_stream_log` | 数据流失败日志-主表 | 13 | [iscx_data_stream_log.md](./iscx_data_stream_log.md) |
| 6 | `t_iscx_data_stream_trace` | 数据流成功日志-主表 | 7 | [iscx_data_stream_trace.md](./iscx_data_stream_trace.md) |
| 7 | `t_iscx_datax_connector` | 连接器绑定-子表 | 7 | [iscx_data_flow_trigger.md](./iscx_data_flow_trigger.md) |
| 8 | `t_iscx_datax_param` | 参数绑定-子表 | 8 | [iscx_data_flow_trigger.md](./iscx_data_flow_trigger.md) |
| 9 | `t_iscx_datax_stream` | 数据流实例-主表 | 17 | [iscx_data_stream.md](./iscx_data_stream.md) |
| 10 | `t_iscx_datax_trigger` | 数据流启动方案-主表 | 27 | [iscx_data_flow_trigger.md](./iscx_data_flow_trigger.md) |
| 11 | `t_iscx_datax_trigger_l` | 数据流启动方案-多语言表 | 4 | [iscx_data_flow_trigger.md](./iscx_data_flow_trigger.md) |
| 12 | `t_iscx_guide_res` | 数据流向导-主表 | 13 | [iscx_guide_resource.md](./iscx_guide_resource.md) |
| 13 | `t_iscx_guide_res_l` | 数据流向导-多语言表 | 4 | [iscx_guide_resource.md](./iscx_guide_resource.md) |
| 14 | `t_iscx_home_demo1` | 数据流demo1-主表 | 0 | [iscx_home_demo1.md](./iscx_home_demo1.md) |
| 15 | `t_iscx_home_demo1_l` | 数据流demo1-多语言表 | 0 | [iscx_home_demo1.md](./iscx_home_demo1.md) |
| 16 | `t_iscx_icon_repository` | 图标库-主表 | 4 | [iscx_icon_repository.md](./iscx_icon_repository.md) |
| 17 | `t_iscx_res_catalog` | 资源目录-主表 | 16 | [iscx_catalog.md](./iscx_catalog.md) |
| 18 | `t_iscx_res_catalog_l` | 资源目录-多语言表 | 4 | [iscx_catalog.md](./iscx_catalog.md) |
| 19 | `t_iscx_res_ext_depends` | 依赖资源-多选基础资料表 | 3 | [iscx_resource_ext.md](./iscx_resource_ext.md) |
| 20 | `t_iscx_res_main` | 数据流资源-主表 | 25 | [iscx_resource.md](./iscx_resource.md) |
| 21 | `t_iscx_res_main` | 资源信息公共模板-主表 | 25 | [iscx_resource_base.md](./iscx_resource_base.md) |
| 22 | `t_iscx_res_main` | 资源扩展-主表 | 25 | [iscx_resource_ext.md](./iscx_resource_ext.md) |
| 23 | `t_iscx_res_main` | 资源配置（运行时）-主表 | 25 | [iscx_resource_rtm.md](./iscx_resource_rtm.md) |
| 24 | `t_iscx_res_main_depends` | 依赖资源-多选基础资料表 | 3 | [iscx_resource.md](./iscx_resource.md) |
| 25 | `t_iscx_res_main_l` | 数据流资源-多语言表 | 4 | [iscx_resource.md](./iscx_resource.md) |
| 26 | `t_iscx_res_main_l` | 资源信息公共模板-多语言表 | 4 | [iscx_resource_base.md](./iscx_resource_base.md) |
| 27 | `t_iscx_res_main_l` | 资源扩展-多语言表 | 4 | [iscx_resource_ext.md](./iscx_resource_ext.md) |
| 28 | `t_iscx_res_main_l` | 资源配置（运行时）-多语言表 | 4 | [iscx_resource_rtm.md](./iscx_resource_rtm.md) |
| 29 | `t_iscx_res_type` | 资源类型-主表 | 9 | [iscx_resource_type.md](./iscx_resource_type.md) |
| 30 | `t_iscx_res_type_l` | 资源类型-多语言表 | 4 | [iscx_resource_type.md](./iscx_resource_type.md) |
