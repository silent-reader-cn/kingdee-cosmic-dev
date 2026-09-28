# tsate 模块表清单

> 本模块共收录 **71** 张表定义，来自 `tsate_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category tsate
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bdtaxr_taxbureau_sbb` | 税局版申报表-主表 | 57 | [tsate_declare_history.md](./tsate_declare_history.md) |
| 2 | `t_tctb_declare_main` | 一键报税-主表 | 66 | [tsate_declare_query_list.md](./tsate_declare_query_list.md) |
| 3 | `t_tctb_taxtype_verify` | 税费种核定信息-主表 | 25 | [tsate_taxtype_verify.md](./tsate_taxtype_verify.md) |
| 4 | `t_tsate_api_token` | 通道token数据-主表 | 14 | [tsate_api_token.md](./tsate_api_token.md) |
| 5 | `t_tsate_area_config` | 地区信息-主表 | 10 | [tsate_area_config.md](./tsate_area_config.md) |
| 6 | `t_tsate_area_config_l` | 地区信息-多语言表 | 4 | [tsate_area_config.md](./tsate_area_config.md) |
| 7 | `t_tsate_areainfo_setting` | 税企直连行政区化配置-主表 | 12 | [tsate_areainfo_setting.md](./tsate_areainfo_setting.md) |
| 8 | `t_tsate_areainfo_setting_l` | 税企直连行政区化配置-多语言表 | 4 | [tsate_areainfo_setting.md](./tsate_areainfo_setting.md) |
| 9 | `t_tsate_base_info` | 税企直连基础信息维护-主表 | 3 | [tsate_baseinfo.md](./tsate_baseinfo.md) |
| 10 | `t_tsate_base_info_entry` | 单据体-子表 | 11 | [tsate_baseinfo.md](./tsate_baseinfo.md) |
| 11 | `t_tsate_channel` | 申报通道-主表 | 11 | [tsate_channel.md](./tsate_channel.md) |
| 12 | `t_tsate_channel_config` | 申报通道-主表 | 13 | [tsate_declare_channel.md](./tsate_declare_channel.md) |
| 13 | `t_tsate_channel_l` | 申报通道-多语言表 | 4 | [tsate_channel.md](./tsate_channel.md) |
| 14 | `t_tsate_checklist` | 申报检查-主表 | 25 | [tsate_declare_checklist.md](./tsate_declare_checklist.md) |
| 15 | `t_tsate_checklist_body` | 单据体-子表 | 31 | [tsate_checklist_group.md](./tsate_checklist_group.md) |
| 16 | `t_tsate_checklist_config` | 申报清册比对配置-主表 | 18 | [tsate_checklist_config.md](./tsate_checklist_config.md) |
| 17 | `t_tsate_checklist_config_l` | 申报清册比对配置-多语言表 | 4 | [tsate_checklist_config.md](./tsate_checklist_config.md) |
| 18 | `t_tsate_checklist_head` | 申报检查-主表 | 17 | [tsate_checklist_group.md](./tsate_checklist_group.md) |
| 19 | `t_tsate_connect_config` | 税企直连设置-主表 | 19 | [tsate_connect_config.md](./tsate_connect_config.md) |
| 20 | `t_tsate_credit_level` | 纳税人信用等级-主表 | 21 | [tsate_credit_level_list.md](./tsate_credit_level_list.md) |
| 21 | `t_tsate_declare_area` | 申报地区信息-主表 | 12 | [tsate_declare_area.md](./tsate_declare_area.md) |
| 22 | `t_tsate_declare_base` | 申报信息基础运维表-主表 | 17 | [tsate_declare_base.md](./tsate_declare_base.md) |
| 23 | `t_tsate_declare_base_type` | 申报表类型-多选基础资料表 | 3 | [tsate_declare_base.md](./tsate_declare_base.md) |
| 24 | `t_tsate_declare_config` | 税局登录配置-主表 | 28 | [tsate_declare_config.md](./tsate_declare_config.md) |
| 25 | `t_tsate_declare_dynsh` | 同步税号-主表 | 14 | [tsate_declare_dynsh.md](./tsate_declare_dynsh.md) |
| 26 | `t_tsate_declare_dynuser` | 同步用户-主表 | 14 | [tsate_declare_dynuser.md](./tsate_declare_dynuser.md) |
| 27 | `t_tsate_declare_record` | 报税任务监控-主表 | 26 | [tsate_declare_record.md](./tsate_declare_record.md) |
| 28 | `t_tsate_declare_record` | 同步日志-主表 | 26 | [tsate_dyn_log.md](./tsate_dyn_log.md) |
| 29 | `t_tsate_declare_record` | 一键报税日志弹窗-主表 | 26 | [tsate_msg_yjbs.md](./tsate_msg_yjbs.md) |
| 30 | `t_tsate_declare_register` | 税期直连-注册信息-主表 | 5 | [tsate_declare_register.md](./tsate_declare_register.md) |
| 31 | `t_tsate_declare_request` | 税企直连-申报信息记录-主表 | 21 | [tsate_declare_status_info.md](./tsate_declare_status_info.md) |
| 32 | `t_tsate_declare_shinfo` | 税号同步信息-主表 | 4 | [tsate_declare_shinfo.md](./tsate_declare_shinfo.md) |
| 33 | `t_tsate_declare_sycj` | 税企直连-税源采集-主表 | 10 | [tsate_declare_sycj.md](./tsate_declare_sycj.md) |
| 34 | `t_tsate_declare_taxorgan` | 申报税局-多选基础资料表 | 3 | [tsate_declare_channel.md](./tsate_declare_channel.md) |
| 35 | `t_tsate_declare_taxtype` | 申报税种-多选基础资料表 | 3 | [tsate_declare_channel.md](./tsate_declare_channel.md) |
| 36 | `t_tsate_declare_yhinfo` | 用户同步信息-主表 | 3 | [tsate_declare_userinfo.md](./tsate_declare_userinfo.md) |
| 37 | `t_tsate_declare_yhinfo` | 用户同步信息-主表 | 3 | [tsate_declare_yhinfo.md](./tsate_declare_yhinfo.md) |
| 38 | `t_tsate_declare_zspm` | 税企直连-印花税征收品目(河北电子税局专用)-主表 | 11 | [tsate_declare_zspm.md](./tsate_declare_zspm.md) |
| 39 | `t_tsate_declare_zspm_l` | 税企直连-印花税征收品目(河北电子税局专用)-多语言表 | 4 | [tsate_declare_zspm.md](./tsate_declare_zspm.md) |
| 40 | `t_tsate_jmxzdm` | 减免性质代码全集-主表 | 10 | [tsate_jmxzdm.md](./tsate_jmxzdm.md) |
| 41 | `t_tsate_jmxzdm_l` | 减免性质代码全集-多语言表 | 5 | [tsate_jmxzdm.md](./tsate_jmxzdm.md) |
| 42 | `t_tsate_jmxzdm_mapping` | 减免性质代码申报映射-主表 | 15 | [tsate_jmxzdm_mapping.md](./tsate_jmxzdm_mapping.md) |
| 43 | `t_tsate_jmxzdm_mapping_l` | 减免性质代码申报映射-多语言表 | 4 | [tsate_jmxzdm_mapping.md](./tsate_jmxzdm_mapping.md) |
| 44 | `t_tsate_map_funclable` | 功能标签-主表 | 10 | [tsate_map_funclable.md](./tsate_map_funclable.md) |
| 45 | `t_tsate_map_funclable_l` | 功能标签-多语言表 | 4 | [tsate_map_funclable.md](./tsate_map_funclable.md) |
| 46 | `t_tsate_msg_log` | 税企日志-主表 | 17 | [tsate_msg_log.md](./tsate_msg_log.md) |
| 47 | `t_tsate_msg_receive` | 消息接收-主表 | 12 | [tsate_msg_receive.md](./tsate_msg_receive.md) |
| 48 | `t_tsate_msg_send` | 消息发送-主表 | 16 | [tsate_msg_send.md](./tsate_msg_send.md) |
| 49 | `t_tsate_msgconfig` | 消息发送配置-主表 | 9 | [tsate_msg_send_config.md](./tsate_msg_send_config.md) |
| 50 | `t_tsate_msgconfig_detail` | 单据体-子表 | 5 | [tsate_msg_send_config.md](./tsate_msg_send_config.md) |
| 51 | `t_tsate_param_config` | 税企直连认证信息配置-主表 | 12 | [tsate_param_config.md](./tsate_param_config.md) |
| 52 | `t_tsate_param_setting` | 税企直连-系统配置-主表 | 3 | [tsate_param_setting.md](./tsate_param_setting.md) |
| 53 | `t_tsate_pupupdata_declare` | 申报弹框业务数据单据-主表 | 19 | [tsate_pupupdata_declare.md](./tsate_pupupdata_declare.md) |
| 54 | `t_tsate_sbpz_admin` | 申报凭证-主表 | 20 | [tsate_sbpz_admin.md](./tsate_sbpz_admin.md) |
| 55 | `t_tsate_sbpz_admin` | 上传凭证-主表 | 20 | [tsate_sbpz_upload.md](./tsate_sbpz_upload.md) |
| 56 | `t_tsate_secret_config` | 加密参数配置-主表 | 5 | [tsate_secret_config.md](./tsate_secret_config.md) |
| 57 | `t_tsate_setting_bw` | 报文配置-主表 | 15 | [tsate_setting_bw.md](./tsate_setting_bw.md) |
| 58 | `t_tsate_setting_qxy_xh` | 企享云小号配置-主表 | 3 | [tsate_setting_qxy_xh.md](./tsate_setting_qxy_xh.md) |
| 59 | `t_tsate_sign_info` | 税企直连-标识信息-主表 | 19 | [tsate_sign_info.md](./tsate_sign_info.md) |
| 60 | `t_tsate_tasktype` | 任务类型-主表 | 11 | [tsate_tasktype.md](./tsate_tasktype.md) |
| 61 | `t_tsate_tasktype_l` | 任务类型-多语言表 | 4 | [tsate_tasktype.md](./tsate_tasktype.md) |
| 62 | `t_tsate_taxtype` | 税种-多选基础资料表 | 3 | [tsate_taxtype_mapping.md](./tsate_taxtype_mapping.md) |
| 63 | `t_tsate_taxtype_mapping` | 申报表类型税种映射配置-主表 | 10 | [tsate_taxtype_mapping.md](./tsate_taxtype_mapping.md) |
| 64 | `t_tsate_taxtype_mapping_l` | 申报表类型税种映射配置-多语言表 | 4 | [tsate_taxtype_mapping.md](./tsate_taxtype_mapping.md) |
| 65 | `t_tsate_template_type` | 申报表类型-多选基础资料表 | 3 | [tsate_declare_config.md](./tsate_declare_config.md) |
| 66 | `t_tsate_templatetype` | 申报表类型-多选基础资料表 | 3 | [tsate_taxtype_mapping.md](./tsate_taxtype_mapping.md) |
| 67 | `t_tsate_text_map` | 文本映射-主表 | 13 | [tsate_text_map.md](./tsate_text_map.md) |
| 68 | `t_tsate_text_map_l` | 文本映射-多语言表 | 4 | [tsate_text_map.md](./tsate_text_map.md) |
| 69 | `t_tsate_workflow_test` | 工作流测试-主表 | 0 | [tsate_workflow_test.md](./tsate_workflow_test.md) |
| 70 | `t_tsate_yhs_taxitem` | 印花税税目(云合使用)-主表 | 10 | [tsate_yhs_taxitem.md](./tsate_yhs_taxitem.md) |
| 71 | `t_tsate_yhs_taxitem_l` | 印花税税目(云合使用)-多语言表 | 4 | [tsate_yhs_taxitem.md](./tsate_yhs_taxitem.md) |
