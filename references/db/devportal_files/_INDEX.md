# devportal 模块表清单

> 本模块共收录 **5** 张表定义，来自 `devportal_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category devportal
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_meta_appintegrityerror` | 应用完整性错误信息-主表 | 8 | [bos_devp_appintegrityerr.md](./bos_devp_appintegrityerr.md) |
| 2 | `t_meta_gitmanager` | git快速开放管理-主表 | 2 | [bos_devp_gitmanager.md](./bos_devp_gitmanager.md) |
| 3 | `t_meta_industryinfo` | 行业信息-主表 | 2 | [bos_devp_industry.md](./bos_devp_industry.md) |
| 4 | `t_meta_industryinfo_l` | 行业信息-多语言表 | 6 | [bos_devp_industry.md](./bos_devp_industry.md) |
| 5 | `t_sys_performancelog` | 性能审计日志-主表 | 10 | [bos_performancelog.md](./bos_performancelog.md) |
