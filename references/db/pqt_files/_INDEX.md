# pqt 模块表清单

> 本模块共收录 **16** 张表定义，来自 `pqt_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category pqt
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_pqt_billretrace` | 单据追溯逻辑-主表 | 29 | [pqt_billretracelogic.md](./pqt_billretracelogic.md) |
| 2 | `t_pqt_billretrace_l` | 单据追溯逻辑-多语言表 | 4 | [pqt_billretracelogic.md](./pqt_billretracelogic.md) |
| 3 | `t_pqt_billretrace_u` | 单据追溯逻辑-使用范围表 | 3 | [pqt_billretracelogic.md](./pqt_billretracelogic.md) |
| 4 | `t_pqt_entityobject` | 追溯业务对象设置-主表 | 14 | [pqt_entityobject.md](./pqt_entityobject.md) |
| 5 | `t_pqt_entityobject_l` | 追溯业务对象设置-多语言表 | 4 | [pqt_entityobject.md](./pqt_entityobject.md) |
| 6 | `t_pqt_mateentry` | 匹配分录-子表 | 12 | [pqt_retracemodel.md](./pqt_retracemodel.md) |
| 7 | `t_pqt_retentry` | 追溯清单分录-子表 | 28 | [pqt_retracemodel.md](./pqt_retracemodel.md) |
| 8 | `t_pqt_retracemodel` | 质量追溯范围-主表 | 24 | [pqt_retracemodel.md](./pqt_retracemodel.md) |
| 9 | `t_pqt_retracemodel_l` | 质量追溯范围-多语言表 | 4 | [pqt_retracemodel.md](./pqt_retracemodel.md) |
| 10 | `t_pqt_retracemodel_u` | 质量追溯范围-使用范围表 | 3 | [pqt_retracemodel.md](./pqt_retracemodel.md) |
| 11 | `t_pqt_retraceroute` | 产品树追溯路径-主表 | 25 | [pqt_retraceroute.md](./pqt_retraceroute.md) |
| 12 | `t_pqt_retraceroute_l` | 产品树追溯路径-多语言表 | 4 | [pqt_retraceroute.md](./pqt_retraceroute.md) |
| 13 | `t_pqt_retraceroute_u` | 产品树追溯路径-使用范围表 | 3 | [pqt_retraceroute.md](./pqt_retraceroute.md) |
| 14 | `t_pqt_routeentry` | 追溯路径-子表 | 9 | [pqt_retraceroute.md](./pqt_retraceroute.md) |
| 15 | `t_pqt_traceconfig` | 追溯查询方案设置-主表 | 20 | [pqt_traceconfig.md](./pqt_traceconfig.md) |
| 16 | `t_pqt_traceorg` | 查询组织-多选基础资料表 | 3 | [pqt_traceconfig.md](./pqt_traceconfig.md) |
