# rpap 模块表清单

> 本模块共收录 **28** 张表定义，来自 `rpap_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope rpap
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_rpap_argumententry` | 单据体-子表 | 6 | [rpap_process.md](./rpap_process.md) |
| 2 | `t_rpap_config_setting` | 集成配置-主表 | 14 | [rpap_config.md](./rpap_config.md) |
| 3 | `t_rpap_config_setting_l` | 集成配置-多语言表 | 4 | [rpap_config.md](./rpap_config.md) |
| 4 | `t_rpap_isrpa_license` | 许可-主表 | 17 | [rpap_isrpa_license.md](./rpap_isrpa_license.md) |
| 5 | `t_rpap_isrpa_license_bind` | 许可使用-主表 | 23 | [rpap_isrpa_license_bind.md](./rpap_isrpa_license_bind.md) |
| 6 | `t_rpap_isrpa_license_bind_l` | 许可使用-多语言表 | 4 | [rpap_isrpa_license_bind.md](./rpap_isrpa_license_bind.md) |
| 7 | `t_rpap_isrpa_license_l` | 许可-多语言表 | 4 | [rpap_isrpa_license.md](./rpap_isrpa_license.md) |
| 8 | `t_rpap_plantask` | 调度计划-主表 | 30 | [rpap_plantask.md](./rpap_plantask.md) |
| 9 | `t_rpap_plantask_process` | 单据体-子表 | 5 | [rpap_plantask.md](./rpap_plantask.md) |
| 10 | `t_rpap_process` | 流程-主表 | 25 | [rpap_process.md](./rpap_process.md) |
| 11 | `t_rpap_process_l` | 流程-多语言表 | 4 | [rpap_process.md](./rpap_process.md) |
| 12 | `t_rpap_process_m` | 流程-使用范围位图表 | 2 | [rpap_process.md](./rpap_process.md) |
| 13 | `t_rpap_process_u` | 流程-使用范围表 | 3 | [rpap_process.md](./rpap_process.md) |
| 14 | `t_rpap_processversion` | 流程版本-主表 | 15 | [rpap_processversion.md](./rpap_processversion.md) |
| 15 | `t_rpap_processversion_l` | 流程版本-多语言表 | 4 | [rpap_processversion.md](./rpap_processversion.md) |
| 16 | `t_rpap_robot` | 机器人-主表 | 26 | [rpap_robot.md](./rpap_robot.md) |
| 17 | `t_rpap_robot_l` | 机器人-多语言表 | 4 | [rpap_robot.md](./rpap_robot.md) |
| 18 | `t_rpap_robot_m` | 机器人-使用范围位图表 | 2 | [rpap_robot.md](./rpap_robot.md) |
| 19 | `t_rpap_robot_u` | 机器人-使用范围表 | 3 | [rpap_robot.md](./rpap_robot.md) |
| 20 | `t_rpap_serviceconf` | 服务配置-主表 | 13 | [rpap_serviceconfig.md](./rpap_serviceconfig.md) |
| 21 | `t_rpap_serviceconf_l` | 服务配置-多语言表 | 4 | [rpap_serviceconfig.md](./rpap_serviceconfig.md) |
| 22 | `t_rpap_task` | 任务-主表 | 28 | [rpap_task.md](./rpap_task.md) |
| 23 | `t_rpap_taskargentry` | 单据体-子表 | 6 | [rpap_task.md](./rpap_task.md) |
| 24 | `t_rpap_taskoutargentry` | 单据体-子表 | 6 | [rpap_task.md](./rpap_task.md) |
| 25 | `t_rpap_thirdtype` | 第三方类型-主表 | 12 | [rpap_thirdtype.md](./rpap_thirdtype.md) |
| 26 | `t_rpap_thirdtype_l` | 第三方类型-多语言表 | 4 | [rpap_thirdtype.md](./rpap_thirdtype.md) |
| 27 | `t_rpap_user_type` | 客户端类型-主表 | 11 | [rpap_usertype.md](./rpap_usertype.md) |
| 28 | `t_rpap_user_type_l` | 客户端类型-多语言表 | 4 | [rpap_usertype.md](./rpap_usertype.md) |
