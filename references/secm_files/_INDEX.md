# secm 模块表清单

> 本模块共收录 **4** 张表定义，来自 `secm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope secm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_sec_userclean` | 人员信息清除记录-主表 | 5 | [bos_user_clean.md](./bos_user_clean.md) |
| 2 | `t_sec_userinfocleanscheme` | 人员个人信息清除方案-主表 | 15 | [bos_user_infocleanscheme.md](./bos_user_infocleanscheme.md) |
| 3 | `t_sec_userinfocleanscheme_l` | 人员个人信息清除方案-多语言表 | 4 | [bos_user_infocleanscheme.md](./bos_user_infocleanscheme.md) |
| 4 | `t_sec_userinfoclnschentry` | 清除内容-子表 | 4 | [bos_user_infocleanscheme.md](./bos_user_infocleanscheme.md) |
