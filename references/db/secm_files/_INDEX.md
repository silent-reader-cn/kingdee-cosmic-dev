# secm 模块表清单

> 本模块共收录 **17** 张表定义，来自 `secm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category secm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_perm_drctrl_blacklist` | 数据规则严控黑名单-主表 | 4 | [perm_drctrl_blacklist.md](./perm_drctrl_blacklist.md) |
| 2 | `t_perm_drctrl_whitelist` | 数据规则严控白名单-主表 | 4 | [perm_drctrl_whitelist.md](./perm_drctrl_whitelist.md) |
| 3 | `t_sec_userclean` | 人员信息清除记录-主表 | 5 | [bos_user_clean.md](./bos_user_clean.md) |
| 4 | `t_sec_userinfocleanscheme` | 人员个人信息清除方案-主表 | 15 | [bos_user_infocleanscheme.md](./bos_user_infocleanscheme.md) |
| 5 | `t_sec_userinfocleanscheme_l` | 人员个人信息清除方案-多语言表 | 5 | [bos_user_infocleanscheme.md](./bos_user_infocleanscheme.md) |
| 6 | `t_sec_userinfoclnschentry` | 清除内容-子表 | 4 | [bos_user_infocleanscheme.md](./bos_user_infocleanscheme.md) |
| 7 | `t_xkperm_handover_bill` | 权限交接-主表 | 17 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 8 | `t_xkperm_handover_bill_l` | 权限交接-多语言表 | 4 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 9 | `t_xkperm_hd_drpermsentry` | 权限数据规则-子表 | 9 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 10 | `t_xkperm_hd_drprsentry` | 基础资料范围数据规则-子表 | 10 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 11 | `t_xkperm_hd_feilddsentry` | 明细字段子单据体-子表 | 8 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 12 | `t_xkperm_hd_feildssentry` | 字段方案子单据体-子表 | 6 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 13 | `t_xkperm_hd_funcsentry` | 功能权限子单据体-子表 | 6 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 14 | `t_xkperm_hd_mulpermdr` | 原数据规则方案-多选基础资料表 | 3 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 15 | `t_xkperm_hd_mulprdr` | 原数据规则方案-多选基础资料表 | 3 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 16 | `t_xkperm_hd_roleentry` | 单据体-子表 | 9 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
| 17 | `t_xkperm_hdbill_admins` | 管理员分组-多选基础资料表 | 3 | [xkperm_handover_bill.md](./xkperm_handover_bill.md) |
