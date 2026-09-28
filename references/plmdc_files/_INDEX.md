# plmdc 模块表清单

> 本模块共收录 **61** 张表定义，来自 `plmdc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope plmdc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_plm_plmdc_fileicon` | 文档库图标-主表 | 0 | [plm_plmdc_icon.md](./plm_plmdc_icon.md) |
| 2 | `t_plmdc_batch_import` | 文档库批量导入-主表 | 12 | [plm_plmdc_batch_import.md](./plm_plmdc_batch_import.md) |
| 3 | `t_plmdc_cadapplymat` | CAD物料申请记录-主表 | 8 | [plm_plmdc_cadapplymat.md](./plm_plmdc_cadapplymat.md) |
| 4 | `t_plmdc_cadrecords` | cad上传记录-主表 | 6 | [plm_plmdc_cadrecords.md](./plm_plmdc_cadrecords.md) |
| 5 | `t_plmdc_controlledseal` | 受控章信息-主表 | 9 | [plmdc_controlledseal.md](./plmdc_controlledseal.md) |
| 6 | `t_plmdc_convert_task` | 转换任务-主表 | 22 | [plm_plmdc_convert_task.md](./plm_plmdc_convert_task.md) |
| 7 | `t_plmdc_convert_task_l` | 转换任务-多语言表 | 4 | [plm_plmdc_convert_task.md](./plm_plmdc_convert_task.md) |
| 8 | `t_plmdc_detail_mapping` | 明细栏数据对应关系单据体-子表 | 20 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 9 | `t_plmdc_detail_mapping_l` | 明细栏数据对应关系单据体-多语言表 | 5 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 10 | `t_plmdc_drawnogroup` | 图号分组-主表 | 16 | [plm_plmdc_drawnogroup.md](./plm_plmdc_drawnogroup.md) |
| 11 | `t_plmdc_drawnogroup_l` | 图号分组-多语言表 | 5 | [plm_plmdc_drawnogroup.md](./plm_plmdc_drawnogroup.md) |
| 12 | `t_plmdc_drawnolibrary` | 图号-主表 | 24 | [plm_plmdc_drawnolibrary.md](./plm_plmdc_drawnolibrary.md) |
| 13 | `t_plmdc_drawnorule` | 图号规则列表-主表 | 12 | [plm_plmdc_drawnorule.md](./plm_plmdc_drawnorule.md) |
| 14 | `t_plmdc_drawnorule_l` | 图号规则列表-多语言表 | 4 | [plm_plmdc_drawnorule.md](./plm_plmdc_drawnorule.md) |
| 15 | `t_plmdc_drawnoruleentry` | 编码分析-子表 | 19 | [plm_plmdc_drawnorule.md](./plm_plmdc_drawnorule.md) |
| 16 | `t_plmdc_electron_org` | 组织-子表 | 4 | [plm_plmdc_storage_scheme.md](./plm_plmdc_storage_scheme.md) |
| 17 | `t_plmdc_eplan_attr` | EPLAN属性-主表 | 12 | [plm_plmdc_eplan_attr.md](./plm_plmdc_eplan_attr.md) |
| 18 | `t_plmdc_eplan_attr_l` | EPLAN属性-多语言表 | 4 | [plm_plmdc_eplan_attr.md](./plm_plmdc_eplan_attr.md) |
| 19 | `t_plmdc_file_type` | 文件类型-主表 | 21 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 20 | `t_plmdc_file_type_l` | 文件类型-多语言表 | 4 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 21 | `t_plmdc_file_type_u` | 文件类型-使用范围表 | 3 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 22 | `t_plmdc_filetype_bomrule` | 生成BOM规则配置单据体-子表 | 6 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 23 | `t_plmdc_filetype_entry` | 文件扩展名单据体-子表 | 5 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 24 | `t_plmdc_filetype_entry_l` | 文件扩展名单据体-多语言表 | 4 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 25 | `t_plmdc_filetype_mapping` | 数据对应关系单据体-子表 | 22 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 26 | `t_plmdc_filetype_mapping_l` | 数据对应关系单据体-多语言表 | 5 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 27 | `t_plmdc_filetype_matmodel` | 绑定物料业务模型-多选基础资料表 | 3 | [plm_plmdc_file_type.md](./plm_plmdc_file_type.md) |
| 28 | `t_plmdc_fs_cfg` | 服务器配置-主表 | 23 | [plm_plmdc_fs_cfg.md](./plm_plmdc_fs_cfg.md) |
| 29 | `t_plmdc_fs_cfg_l` | 服务器配置-多语言表 | 4 | [plm_plmdc_fs_cfg.md](./plm_plmdc_fs_cfg.md) |
| 30 | `t_plmdc_fs_cfg_u` | 服务器配置-使用范围表 | 3 | [plm_plmdc_fs_cfg.md](./plm_plmdc_fs_cfg.md) |
| 31 | `t_plmdc_fs_entity` | 单据体-子表 | 14 | [plm_plmdc_fs_cfg.md](./plm_plmdc_fs_cfg.md) |
| 32 | `t_plmdc_group_drawnorule` | 图号规则-子表 | 4 | [plm_plmdc_drawnogroup.md](./plm_plmdc_drawnogroup.md) |
| 33 | `t_plmdc_grouptemplate` | 单据体-子表 | 6 | [plm_plmdc_drawnogroup.md](./plm_plmdc_drawnogroup.md) |
| 34 | `t_plmdc_maxserial` | 图号规则最大号-主表 | 10 | [plm_plmdc_maxserial.md](./plm_plmdc_maxserial.md) |
| 35 | `t_plmdc_multicontrolledse` | 受控章-多选基础资料表 | 3 | [plmdc_signatureplan.md](./plmdc_signatureplan.md) |
| 36 | `t_plmdc_physical_file` | 物理文件属性-主表 | 32 | [plm_plmdc_physical_file.md](./plm_plmdc_physical_file.md) |
| 37 | `t_plmdc_physical_file_l` | 物理文件属性-多语言表 | 4 | [plm_plmdc_physical_file.md](./plm_plmdc_physical_file.md) |
| 38 | `t_plmdc_physical_file_u` | 物理文件属性-使用范围表 | 3 | [plm_plmdc_physical_file.md](./plm_plmdc_physical_file.md) |
| 39 | `t_plmdc_qrcode_entry` | 二维码信息配置-子表 | 13 | [plm_plmdc_qrcodeswitch.md](./plm_plmdc_qrcodeswitch.md) |
| 40 | `t_plmdc_qrcodeswitch` | 二维码方案-主表 | 28 | [plm_plmdc_qrcodeswitch.md](./plm_plmdc_qrcodeswitch.md) |
| 41 | `t_plmdc_qrcodeswitch_l` | 二维码方案-多语言表 | 4 | [plm_plmdc_qrcodeswitch.md](./plm_plmdc_qrcodeswitch.md) |
| 42 | `t_plmdc_qrcodeswitch_u` | 二维码方案-使用范围表 | 3 | [plm_plmdc_qrcodeswitch.md](./plm_plmdc_qrcodeswitch.md) |
| 43 | `t_plmdc_signature_config` | 签字方案配置-主表 | 3 | [plmdc_signatureplan.md](./plmdc_signatureplan.md) |
| 44 | `t_plmdc_signature_task` | 签字任务-主表 | 24 | [plmdc_signature_task.md](./plmdc_signature_task.md) |
| 45 | `t_plmdc_signaturepdffile` | 签字任务PDF文件管理-主表 | 4 | [plmdc_signaturepdffile.md](./plmdc_signaturepdffile.md) |
| 46 | `t_plmdc_signflow_relation` | 流程方案配置映射-子表 | 11 | [plmdc_signatureplan.md](./plmdc_signatureplan.md) |
| 47 | `t_plmdc_simulator_att` | 附件-附件表 | 0 | [plm_plmdc_simulator_data.md](./plm_plmdc_simulator_data.md) |
| 48 | `t_plmdc_simulator_data` | 模拟器数据包附件-主表 | 0 | [plm_plmdc_simulator_data.md](./plm_plmdc_simulator_data.md) |
| 49 | `t_plmdc_simulator_data_l` | 模拟器数据包附件-多语言表 | 0 | [plm_plmdc_simulator_data.md](./plm_plmdc_simulator_data.md) |
| 50 | `t_plmdc_storage_scheme` | 存储方案-主表 | 31 | [plm_plmdc_storage_scheme.md](./plm_plmdc_storage_scheme.md) |
| 51 | `t_plmdc_storage_scheme_l` | 存储方案-多语言表 | 4 | [plm_plmdc_storage_scheme.md](./plm_plmdc_storage_scheme.md) |
| 52 | `t_plmdc_storage_scheme_u` | 存储方案-使用范围表 | 3 | [plm_plmdc_storage_scheme.md](./plm_plmdc_storage_scheme.md) |
| 53 | `t_plmdc_switch_rule` | 转换规则单据体-子表 | 9 | [plm_plmdc_switch_scheme.md](./plm_plmdc_switch_scheme.md) |
| 54 | `t_plmdc_switch_scheme` | 转换方案-主表 | 24 | [plm_plmdc_switch_scheme.md](./plm_plmdc_switch_scheme.md) |
| 55 | `t_plmdc_switch_scheme_l` | 转换方案-多语言表 | 4 | [plm_plmdc_switch_scheme.md](./plm_plmdc_switch_scheme.md) |
| 56 | `t_plmdc_switch_scheme_u` | 转换方案-使用范围表 | 3 | [plm_plmdc_switch_scheme.md](./plm_plmdc_switch_scheme.md) |
| 57 | `t_plmdc_system_property` | 系统属性-主表 | 10 | [plm_plmdc_system_property.md](./plm_plmdc_system_property.md) |
| 58 | `t_plmdc_system_property_l` | 系统属性-多语言表 | 4 | [plm_plmdc_system_property.md](./plm_plmdc_system_property.md) |
| 59 | `t_plmdc_watermark` | 水印方案配置-主表 | 13 | [plmdc_watermark_plan.md](./plmdc_watermark_plan.md) |
| 60 | `t_plmdc_watermark_conf` | 水印内容配置-主表 | 4 | [plmdc_watermark_conf.md](./plmdc_watermark_conf.md) |
| 61 | `t_plmdc_watermkcof_entry` | 水印内容信息配置-子表 | 9 | [plmdc_watermark_conf.md](./plmdc_watermark_conf.md) |
