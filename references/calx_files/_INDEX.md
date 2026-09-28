# calx 模块表清单

> 本模块共收录 **16** 张表定义，来自 `calx_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope calx
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cal_allocdiff` | 待分摊差异-主表 | 0 | [calx_allocdiff.md](./calx_allocdiff.md) |
| 2 | `t_cal_allocdiffentry` | 单据体-子表 | 0 | [calx_allocdiff.md](./calx_allocdiff.md) |
| 3 | `t_cal_diffallocrc` | 差异分摊记录-主表 | 12 | [calx_diffallocrc.md](./calx_diffallocrc.md) |
| 4 | `t_cal_diffallocrc_l` | 差异分摊记录-多语言表 | 4 | [calx_diffallocrc.md](./calx_diffallocrc.md) |
| 5 | `t_cal_diffallocrcentry` | 描述-子表 | 4 | [calx_diffallocrc.md](./calx_diffallocrc.md) |
| 6 | `t_cal_diffallocrpt` | 差异分摊报告-主表 | 24 | [calx_diffallocrpt.md](./calx_diffallocrpt.md) |
| 7 | `t_cal_diffallocrptentry` | 单据体-子表 | 14 | [calx_diffallocrpt.md](./calx_diffallocrpt.md) |
| 8 | `t_cal_diffallocrptentrydt` | 子单据体-子表 | 6 | [calx_diffallocrpt.md](./calx_diffallocrpt.md) |
| 9 | `t_cal_diffallocrs` | 差异分摊结果-主表 | 0 | [calx_diffallocrs.md](./calx_diffallocrs.md) |
| 10 | `t_cal_diffallocrsentry` | 单据体-子表 | 0 | [calx_diffallocrs.md](./calx_diffallocrs.md) |
| 11 | `t_cal_progress` | 进度展示-主表 | 3 | [cal_progress.md](./cal_progress.md) |
| 12 | `t_cal_progressentry` | 单据体-子表 | 8 | [cal_progress.md](./cal_progress.md) |
| 13 | `t_cal_runningallocbill` | 分摊中差异单据-主表 | 0 | [calx_runningalloc.md](./calx_runningalloc.md) |
| 14 | `t_cal_step` | 步骤-主表 | 3 | [cal_step.md](./cal_step.md) |
| 15 | `t_cal_step_l` | 步骤-多语言表 | 4 | [cal_step.md](./cal_step.md) |
| 16 | `t_cal_task` | 出库核算任务-主表 | 18 | [cal_task.md](./cal_task.md) |
