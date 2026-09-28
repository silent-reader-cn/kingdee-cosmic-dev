# ctsy 模块表清单

> 本模块共收录 **44** 张表定义，来自 `ctsy_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ctsy
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_tenant_auth_config` | 租户认证配置-主表 | 12 | [tenant_auth_config.md](./tenant_auth_config.md) |
| 2 | `t_bas_tenant_auth_detail` | 租户配置分发明细-主表 | 6 | [tenant_auth_config_detail.md](./tenant_auth_config_detail.md) |
| 3 | `t_ctbotp_attsynclog` | 附件同步记录-主表 | 14 | [bos_ctbotp_attsynclog.md](./bos_ctbotp_attsynclog.md) |
| 4 | `t_ctbotp_billinfors` | 主数据分发检测单据-主表 | 9 | [ct_botp_billinfos.md](./ct_botp_billinfos.md) |
| 5 | `t_ctbotp_billinfors_l` | 主数据分发检测单据-多语言表 | 4 | [ct_botp_billinfos.md](./ct_botp_billinfos.md) |
| 6 | `t_ctbotp_billlk` | 单据关联关系-主表 | 17 | [bos_ctbotp_billlk.md](./bos_ctbotp_billlk.md) |
| 7 | `t_ctbotp_billroute` | 单据同步路线-主表 | 10 | [bos_ctbotp_billroute.md](./bos_ctbotp_billroute.md) |
| 8 | `t_ctbotp_convertrule` | 数据协同规则-主表 | 34 | [ct_botp_crlist.md](./ct_botp_crlist.md) |
| 9 | `t_ctbotp_convertrule_l` | 数据协同规则-多语言表 | 9 | [ct_botp_crlist.md](./ct_botp_crlist.md) |
| 10 | `t_ctbotp_convertrule_s` | 数据协同规则-分表 | 9 | [ct_botp_crlist.md](./ct_botp_crlist.md) |
| 11 | `t_ctbotp_entrytracker` | 多租户反写快照-主表 | 0 | [ctbotp_snapshot.md](./ctbotp_snapshot.md) |
| 12 | `t_ctbotp_entrytracker` | 业务跟踪表-主表 | 0 | [ctbotp_snapshot_tc.md](./ctbotp_snapshot_tc.md) |
| 13 | `t_ctbotp_gsynclog` | 集团同步记录-主表 | 20 | [bos_ctbotp_synclog_g.md](./bos_ctbotp_synclog_g.md) |
| 14 | `t_ctbotp_gsynclog_c` | 集团同步记录-分表 | 6 | [bos_ctbotp_synclog_g.md](./bos_ctbotp_synclog_g.md) |
| 15 | `t_ctbotp_rule_synclog` | 数据协同同步记录-主表 | 18 | [ct_botp_rule_synclog.md](./ct_botp_rule_synclog.md) |
| 16 | `t_ctbotp_scheme_rec` | 主数据分发方案检测结果-主表 | 8 | [ct_botp_scheme_rec.md](./ct_botp_scheme_rec.md) |
| 17 | `t_ctbotp_scheme_rec_l` | 主数据分发方案检测结果-多语言表 | 4 | [ct_botp_scheme_rec.md](./ct_botp_scheme_rec.md) |
| 18 | `t_ctbotp_synclog` | 源单同步记录-主表 | 22 | [bos_ctbotp_synclog_s.md](./bos_ctbotp_synclog_s.md) |
| 19 | `t_ctbotp_synclog_c` | 源单同步记录-分表 | 6 | [bos_ctbotp_synclog_s.md](./bos_ctbotp_synclog_s.md) |
| 20 | `t_ctbotp_syncroute` | 同步路线-主表 | 8 | [bos_ctbotp_syncroute.md](./bos_ctbotp_syncroute.md) |
| 21 | `t_ctbotp_tenantpath` | 租户路线-主表 | 12 | [bos_ctbotp_tenantpath.md](./bos_ctbotp_tenantpath.md) |
| 22 | `t_ctbotp_tenantpath_l` | 租户路线-多语言表 | 4 | [bos_ctbotp_tenantpath.md](./bos_ctbotp_tenantpath.md) |
| 23 | `t_ctbotp_tsynclog` | 目标单同步记录-主表 | 21 | [bos_ctbotp_synclog_t.md](./bos_ctbotp_synclog_t.md) |
| 24 | `t_ctbotp_tsynclog_c` | 目标单同步记录-分表 | 6 | [bos_ctbotp_synclog_t.md](./bos_ctbotp_synclog_t.md) |
| 25 | `t_ctbotp_unique` | 数据协同防重-主表 | 0 | [bos_ctbotp_unique.md](./bos_ctbotp_unique.md) |
| 26 | `t_ctbotp_uniquedb` | 数据协同防重分库-主表 | 4 | [ctbotp_uniquedb.md](./ctbotp_uniquedb.md) |
| 27 | `t_ctbotp_writebacksnap` | 反写记录单据体-子表 | 0 | [ctbotp_snapshot.md](./ctbotp_snapshot.md) |
| 28 | `t_ctlog_register` | 日志注册-主表 | 15 | [bos_ctlog_register.md](./bos_ctlog_register.md) |
| 29 | `t_ctlog_register_l` | 日志注册-多语言表 | 4 | [bos_ctlog_register.md](./bos_ctlog_register.md) |
| 30 | `t_ctlog_register_status` | 日志状态单据体-子表 | 6 | [bos_ctlog_register.md](./bos_ctlog_register.md) |
| 31 | `t_ctlog_register_status_l` | 日志状态单据体-多语言表 | 4 | [bos_ctlog_register.md](./bos_ctlog_register.md) |
| 32 | `t_ctsy_basedata` | 主数据域管理-主表 | 14 | [ctsy_domain.md](./ctsy_domain.md) |
| 33 | `t_ctsy_basedata_l` | 主数据域管理-多语言表 | 4 | [ctsy_domain.md](./ctsy_domain.md) |
| 34 | `t_ctsy_ctrl_sync_data` | 数据分录-子表 | 6 | [ctsy_ctrlstrategy_sync.md](./ctsy_ctrlstrategy_sync.md) |
| 35 | `t_ctsy_ctrl_sync_org` | 组织分录-子表 | 6 | [ctsy_ctrlstrategy_sync.md](./ctsy_ctrlstrategy_sync.md) |
| 36 | `t_ctsy_ctrlstrategy_sync` | 基础资料使用关系同步记录-主表 | 13 | [ctsy_ctrlstrategy_sync.md](./ctsy_ctrlstrategy_sync.md) |
| 37 | `t_ctsy_distributscheme` | 主数据分发方案-主表 | 24 | [ctsy_distribut_scheme.md](./ctsy_distribut_scheme.md) |
| 38 | `t_ctsy_distributscheme_l` | 主数据分发方案-多语言表 | 4 | [ctsy_distribut_scheme.md](./ctsy_distribut_scheme.md) |
| 39 | `t_ctsy_distschemefilters` | 过滤条件-子表 | 10 | [ctsy_distribut_scheme.md](./ctsy_distribut_scheme.md) |
| 40 | `t_ctsy_distschemetenants` | 目标租户-多选基础资料表 | 4 | [ctsy_distribut_scheme.md](./ctsy_distribut_scheme.md) |
| 41 | `t_ctsy_disttriggers` | 主数据分发启动方案-主表 | 8 | [ctsy_dist_trigger.md](./ctsy_dist_trigger.md) |
| 42 | `t_ctsy_tenant` | 租户配置-主表 | 25 | [ctsy_tenant.md](./ctsy_tenant.md) |
| 43 | `t_ctsy_tenant_l` | 租户配置-多语言表 | 4 | [ctsy_tenant.md](./ctsy_tenant.md) |
| 44 | `t_ctsy_tenantorgrelation` | 组织与租户隶属关系-主表 | 6 | [ctsy_tenantorgrelation.md](./ctsy_tenantorgrelation.md) |
