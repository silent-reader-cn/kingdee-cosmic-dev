# ecollect 模块表清单

> 本模块共收录 **90** 张表定义，来自 `ecollect_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ecollect
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_eafc_file_receive_dir` | 文件移交接收目录-主表 | 27 | [eafc_file_receive_dir.md](./eafc_file_receive_dir.md) |
| 2 | `t_eafc_handoveraccentry` | 单据体-子表 | 9 | [eafc_handoveraccept.md](./eafc_handoveraccept.md) |
| 3 | `t_eafc_handoveraccept` | 移交接收-主表 | 11 | [eafc_handoveraccept.md](./eafc_handoveraccept.md) |
| 4 | `t_eafc_volume_receive_dir` | 案卷移交接收目录-主表 | 22 | [eafc_volume_receive_dir.md](./eafc_volume_receive_dir.md) |
| 5 | `t_fpy_eafc_collect_app` | token配置-主表 | 13 | [fpy_eafc_collect_app.md](./fpy_eafc_collect_app.md) |
| 6 | `tk_eafc_arc_record_billog` | 登记归档日志-文件-主表 | 32 | [eafc_arc_record_bil_log.md](./eafc_arc_record_bil_log.md) |
| 7 | `tk_eafc_arc_record_vollog` | 登记归档日志-案卷-主表 | 22 | [eafc_arc_record_vol_log.md](./eafc_arc_record_vol_log.md) |
| 8 | `tk_eafc_archive_detaillog` | 接收详细日志-主表 | 35 | [eafc_archive_detail_log.md](./eafc_archive_detail_log.md) |
| 9 | `tk_eafc_archive_info` | 手工批量采集-主表 | 28 | [eafc_archive_info.md](./eafc_archive_info.md) |
| 10 | `tk_eafc_archive_info_ent` | 凭证册信息-子表 | 16 | [eafc_archive_info.md](./eafc_archive_info.md) |
| 11 | `tk_eafc_archive_log` | 在线接收日志-主表 | 32 | [eafc_archive_log.md](./eafc_archive_log.md) |
| 12 | `tk_eafc_archive_request` | 归档请求-主表 | 7 | [eafc_archive_request.md](./eafc_archive_request.md) |
| 13 | `tk_eafc_archivenum_fail` | 编目失败-主表 | 19 | [eafc_archivenum_fail.md](./eafc_archivenum_fail.md) |
| 14 | `tk_eafc_autovolsc_ruson_e` | 明细维度单据体-子表 | 12 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 15 | `tk_eafc_autovolsche_org` | 分配组织单据体-子表 | 4 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 16 | `tk_eafc_autovolsche_ruent` | 单据体-子表 | 9 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 17 | `tk_eafc_autovolsche_soent` | 排序单据体-子表 | 6 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 18 | `tk_eafc_autovolume_sche` | 组卷方案配置-主表 | 23 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 19 | `tk_eafc_autovolume_sche_l` | 组卷方案配置-多语言表 | 4 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 20 | `tk_eafc_autovolume_sche_u` | 组卷方案配置-使用范围表 | 3 | [eafc_autovolume_scheme.md](./eafc_autovolume_scheme.md) |
| 21 | `tk_eafc_bill_invoice_log` | 单据发票关系表日志-主表 | 10 | [eafc_bill_invoice_log.md](./eafc_bill_invoice_log.md) |
| 22 | `tk_eafc_collect_tree` | 采集页面树形单据体-主表 | 52 | [eafc_collect_tree.md](./eafc_collect_tree.md) |
| 23 | `tk_eafc_diff_detail` | 差异明细-主表 | 22 | [fpy_eafc_diffdetail.md](./fpy_eafc_diffdetail.md) |
| 24 | `tk_eafc_formal_volume` | 单据体-子表 | 16 | [eafc_reverse_archive.md](./eafc_reverse_archive.md) |
| 25 | `tk_eafc_formal_volume` | 案卷单据体-子表 | 16 | [fpy_formal_archive.md](./fpy_formal_archive.md) |
| 26 | `tk_eafc_im_content` | 集成内容-主表 | 21 | [eafc_im_content.md](./eafc_im_content.md) |
| 27 | `tk_eafc_im_content_l` | 集成内容-多语言表 | 4 | [eafc_im_content.md](./eafc_im_content.md) |
| 28 | `tk_eafc_im_content_out` | 单据体-子表 | 9 | [eafc_im_content.md](./eafc_im_content.md) |
| 29 | `tk_eafc_im_ds` | 集成数据源-主表 | 21 | [eafc_im_ds.md](./eafc_im_ds.md) |
| 30 | `tk_eafc_im_ds_header` | 请求头单据体-子表 | 6 | [eafc_im_ds.md](./eafc_im_ds.md) |
| 31 | `tk_eafc_im_ds_in` | 输入单据体-子表 | 10 | [eafc_im_ds.md](./eafc_im_ds.md) |
| 32 | `tk_eafc_im_ds_l` | 集成数据源-多语言表 | 4 | [eafc_im_ds.md](./eafc_im_ds.md) |
| 33 | `tk_eafc_im_ds_out` | 输出单据体-子表 | 9 | [eafc_im_ds.md](./eafc_im_ds.md) |
| 34 | `tk_eafc_im_ds_request_log` | 数据源请求日志-主表 | 22 | [eafc_im_ds_request_log.md](./eafc_im_ds_request_log.md) |
| 35 | `tk_eafc_im_dstype` | 数据源类型-主表 | 10 | [eafc_im_dstype.md](./eafc_im_dstype.md) |
| 36 | `tk_eafc_im_dstype_in` | 请求单据体-子表 | 7 | [eafc_im_dstype.md](./eafc_im_dstype.md) |
| 37 | `tk_eafc_im_dstype_l` | 数据源类型-多语言表 | 4 | [eafc_im_dstype.md](./eafc_im_dstype.md) |
| 38 | `tk_eafc_im_dstype_out` | 响应单据体-子表 | 8 | [eafc_im_dstype.md](./eafc_im_dstype.md) |
| 39 | `tk_eafc_im_fs` | 文件服务器-主表 | 18 | [eafc_im_fs.md](./eafc_im_fs.md) |
| 40 | `tk_eafc_im_fs_item` | 单据体-子表 | 10 | [eafc_im_fs.md](./eafc_im_fs.md) |
| 41 | `tk_eafc_im_fs_l` | 文件服务器-多语言表 | 4 | [eafc_im_fs.md](./eafc_im_fs.md) |
| 42 | `tk_eafc_im_proj_category` | 方案分类-主表 | 15 | [eafc_im_proj_category.md](./eafc_im_proj_category.md) |
| 43 | `tk_eafc_im_proj_category_l` | 方案分类-多语言表 | 5 | [eafc_im_proj_category.md](./eafc_im_proj_category.md) |
| 44 | `tk_eafc_im_proj_content` | 内容单据体-子表 | 6 | [eafc_im_project.md](./eafc_im_project.md) |
| 45 | `tk_eafc_im_proj_exec_log` | 资料捕获-主表 | 25 | [eafc_im_project_exec_log.md](./eafc_im_project_exec_log.md) |
| 46 | `tk_eafc_im_proj_org` | 组织单据体-子表 | 6 | [eafc_im_project.md](./eafc_im_project.md) |
| 47 | `tk_eafc_im_proj_sub_log` | 方案执行详细日志-主表 | 26 | [eafc_im_proj_exec_sub_log.md](./eafc_im_proj_exec_sub_log.md) |
| 48 | `tk_eafc_im_project` | 集成方案-主表 | 27 | [eafc_im_project.md](./eafc_im_project.md) |
| 49 | `tk_eafc_im_project_l` | 集成方案-多语言表 | 4 | [eafc_im_project.md](./eafc_im_project.md) |
| 50 | `tk_eafc_im_project_u` | 集成方案-使用范围表 | 3 | [eafc_im_project.md](./eafc_im_project.md) |
| 51 | `tk_eafc_im_system` | 集成系统-主表 | 14 | [eafc_im_system.md](./eafc_im_system.md) |
| 52 | `tk_eafc_im_system_l` | 集成系统-多语言表 | 4 | [eafc_im_system.md](./eafc_im_system.md) |
| 53 | `tk_eafc_image_syn_log` | 影像调用日志-主表 | 18 | [eafc_image_syn_log.md](./eafc_image_syn_log.md) |
| 54 | `tk_eafc_inspect_batch` | 送检批次-主表 | 19 | [eafc_inspect_batch.md](./eafc_inspect_batch.md) |
| 55 | `tk_eafc_project_content` | 内容单据体-子表 | 4 | [eafc_xk_project.md](./eafc_xk_project.md) |
| 56 | `tk_eafc_project_org` | 组织单据体-子表 | 4 | [eafc_xk_project.md](./eafc_xk_project.md) |
| 57 | `tk_eafc_record_save` | 移交归档日志-主表 | 43 | [eafc_record_save.md](./eafc_record_save.md) |
| 58 | `tk_eafc_record_save_file` | 关联文件分录-子表 | 8 | [eafc_record_save.md](./eafc_record_save.md) |
| 59 | `tk_eafc_scan_voucher` | 扫码凭证组卷-主表 | 16 | [eafc_scan_voucher.md](./eafc_scan_voucher.md) |
| 60 | `tk_eafc_upload_attachment` | 归档附件上传-主表 | 10 | [eafc_upload_attachment.md](./eafc_upload_attachment.md) |
| 61 | `tk_eafc_upload_xml` | 归档xml上传-主表 | 12 | [eafc_upload_xml.md](./eafc_upload_xml.md) |
| 62 | `tk_eafc_volume` | 组卷-主表 | 80 | [eafc_volume.md](./eafc_volume.md) |
| 63 | `tk_eafc_volume_ent` | 单据体-子表 | 14 | [eafc_volume.md](./eafc_volume.md) |
| 64 | `tk_eafc_voucher_bank_log` | 凭证回单关系日志-主表 | 10 | [eafc_voucher_bank_log.md](./eafc_voucher_bank_log.md) |
| 65 | `tk_eafc_voucher_bill_log` | 凭证与单据关联关系日志-主表 | 10 | [eafc_voucher_bill_log.md](./eafc_voucher_bill_log.md) |
| 66 | `tk_eafc_voucher_inv_log` | 凭证发票关系日志-主表 | 10 | [eafc_voucher_inv_log.md](./eafc_voucher_inv_log.md) |
| 67 | `tk_eafc_voucher_soft_box` | 档案盒盘点-主表 | 41 | [eafc_voucher_soft_box.md](./eafc_voucher_soft_box.md) |
| 68 | `tk_eafc_xk_content` | 集成内容-星空(停用)-主表 | 14 | [eafc_xk_content.md](./eafc_xk_content.md) |
| 69 | `tk_eafc_xk_content_l` | 集成内容-星空(停用)-多语言表 | 4 | [eafc_xk_content.md](./eafc_xk_content.md) |
| 70 | `tk_eafc_xk_meta` | 集成对象-星空(停用)-主表 | 16 | [eafc_xk_meta.md](./eafc_xk_meta.md) |
| 71 | `tk_eafc_xk_meta_param` | 单据体-子表 | 8 | [eafc_xk_meta.md](./eafc_xk_meta.md) |
| 72 | `tk_eafc_xk_project` | 集成方案-星空(停用)-主表 | 14 | [eafc_xk_project.md](./eafc_xk_project.md) |
| 73 | `tk_eafc_xk_system` | 集成系统-星空(停用)-主表 | 14 | [eafc_xk_system.md](./eafc_xk_system.md) |
| 74 | `tk_eafc_xk_system_l` | 集成系统-星空(停用)-多语言表 | 4 | [eafc_xk_system.md](./eafc_xk_system.md) |
| 75 | `tk_fpy_formal_archive` | 反归档审批-主表 | 25 | [eafc_reverse_archive.md](./eafc_reverse_archive.md) |
| 76 | `tk_fpy_formal_archive` | 移交归档审批-主表 | 25 | [fpy_formal_archive.md](./fpy_formal_archive.md) |
| 77 | `tk_fpy_get_file_id_model` | 获取上传文件id-主表 | 9 | [fpy_get_file_id_model.md](./fpy_get_file_id_model.md) |
| 78 | `tk_fpy_match_config_item` | 自动组件规则-子表 | 14 | [fpy_match_relation_conf.md](./fpy_match_relation_conf.md) |
| 79 | `tk_fpy_match_config_org` | 适用组织-子表 | 4 | [fpy_match_relation_conf.md](./fpy_match_relation_conf.md) |
| 80 | `tk_fpy_match_relate_conf` | 组件方案配置-主表 | 15 | [fpy_match_relation_conf.md](./fpy_match_relation_conf.md) |
| 81 | `tk_fpy_match_relate_conf_l` | 组件方案配置-多语言表 | 4 | [fpy_match_relation_conf.md](./fpy_match_relation_conf.md) |
| 82 | `tk_fpy_relation_log` | 组件日志记录-主表 | 21 | [fpy_relation_log.md](./fpy_relation_log.md) |
| 83 | `tk_fpy_relation_task` | 组件任务监控-主表 | 12 | [fpy_relation_task.md](./fpy_relation_task.md) |
| 84 | `tk_fpy_upload_chunk` | 分块上传文件-主表 | 10 | [fpy_upload_chunk.md](./fpy_upload_chunk.md) |
| 85 | `tk_fpy_volume_operate` | 组卷/拆卷日志-主表 | 11 | [fpy_volume_operation.md](./fpy_volume_operation.md) |
| 86 | `tk_fpy_voucherconversios` | EAI凭证拉取规则(五菱)-主表 | 15 | [fpy_voucherconversio.md](./fpy_voucherconversio.md) |
| 87 | `tk_fpy_voucherintermed` | 凭证中间表(五菱)-主表 | 27 | [fpy_voucherintermediate.md](./fpy_voucherintermediate.md) |
| 88 | `tk_fpy_wl_file` | 单据体-子表 | 9 | [fpy_voucherintermediate.md](./fpy_voucherintermediate.md) |
| 89 | `tk_fpy_wl_item` | 单据体-子表 | 13 | [fpy_voucherintermediate.md](./fpy_voucherintermediate.md) |
| 90 | `tk_fpy_wl_uppervoucherli` | 单据体-子表 | 6 | [fpy_voucherintermediate.md](./fpy_voucherintermediate.md) |
