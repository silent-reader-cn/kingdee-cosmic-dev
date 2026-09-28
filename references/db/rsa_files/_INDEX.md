# rsa 模块表清单

> 本模块共收录 **14** 张表定义，来自 `rsa_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category rsa
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_rsa_defaultdimension` | 默认统计维度-多选基础资料表 | 3 | [rsa_riskitem.md](./rsa_riskitem.md) |
| 2 | `t_rsa_exelog` | 扫描日志-主表 | 19 | [rsa_exelog.md](./rsa_exelog.md) |
| 3 | `t_rsa_exelogentry` | 单据体-子表 | 4 | [rsa_exelog.md](./rsa_exelog.md) |
| 4 | `t_rsa_noticeuser` | 通知用户列表-多选基础资料表 | 3 | [rsa_riskevent.md](./rsa_riskevent.md) |
| 5 | `t_rsa_otherdimension` | 其他统计维度-多选基础资料表 | 3 | [rsa_riskitem.md](./rsa_riskitem.md) |
| 6 | `t_rsa_riskevent` | 风险事件-主表 | 26 | [rsa_riskevent.md](./rsa_riskevent.md) |
| 7 | `t_rsa_riskgroup` | 风险类别-主表 | 14 | [rsa_riskgroup.md](./rsa_riskgroup.md) |
| 8 | `t_rsa_riskgroup_l` | 风险类别-多语言表 | 5 | [rsa_riskgroup.md](./rsa_riskgroup.md) |
| 9 | `t_rsa_riskitem` | 风险检查项-主表 | 23 | [rsa_riskitem.md](./rsa_riskitem.md) |
| 10 | `t_rsa_riskitem_l` | 风险检查项-多语言表 | 4 | [rsa_riskitem.md](./rsa_riskitem.md) |
| 11 | `t_rsa_riskitem_u` | 风险检查项-使用范围表 | 3 | [rsa_riskitem.md](./rsa_riskitem.md) |
| 12 | `t_rsa_riskitementry` | 风险触发条件-子表 | 7 | [rsa_riskitem.md](./rsa_riskitem.md) |
| 13 | `t_rsa_risklevel` | 风险等级-主表 | 10 | [rsa_risklevel.md](./rsa_risklevel.md) |
| 14 | `t_rsa_risklevel_l` | 风险等级-多语言表 | 4 | [rsa_risklevel.md](./rsa_risklevel.md) |
