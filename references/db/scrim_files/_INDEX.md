# scrim 模块表清单

> 本模块共收录 **24** 张表定义，来自 `scrim_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category scrim
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_scrim_industry_relation` | 产业关系表-主表 | 6 | [scrim_industry_relation.md](./scrim_industry_relation.md) |
| 2 | `t_scrim_material_info` | 物料看板信息表-主表 | 0 | [scrim_material_info.md](./scrim_material_info.md) |
| 3 | `t_scrim_material_relation` | 物料关联表单-主表 | 8 | [scrim_material_relation.md](./scrim_material_relation.md) |
| 4 | `t_scrim_riskevent` | 风险事件-主表 | 18 | [scrim_riskevent.md](./scrim_riskevent.md) |
| 5 | `t_scrim_riskevent_group` | 风险事件分组-主表 | 16 | [scrim_riskevent_group.md](./scrim_riskevent_group.md) |
| 6 | `t_scrim_riskevent_group_l` | 风险事件分组-多语言表 | 6 | [scrim_riskevent_group.md](./scrim_riskevent_group.md) |
| 7 | `t_scrim_riskevent_l` | 风险事件-多语言表 | 5 | [scrim_riskevent.md](./scrim_riskevent.md) |
| 8 | `t_scrim_riskevententry` | 指标明细-子表 | 8 | [scrim_riskevent.md](./scrim_riskevent.md) |
| 9 | `t_scrim_riskreportdata` | 风险报告数据-主表 | 8 | [scrim_riskreportdata.md](./scrim_riskreportdata.md) |
| 10 | `t_scrim_risksubs` | 风险订阅-主表 | 21 | [scrim_risksubs.md](./scrim_risksubs.md) |
| 11 | `t_scrim_risksubs_event` | 风险事件-子表 | 4 | [scrim_risksubs.md](./scrim_risksubs.md) |
| 12 | `t_scrim_risksubs_group` | 风险订阅分组-主表 | 16 | [scrim_risksubs_group.md](./scrim_risksubs_group.md) |
| 13 | `t_scrim_risksubs_group_l` | 风险订阅分组-多语言表 | 6 | [scrim_risksubs_group.md](./scrim_risksubs_group.md) |
| 14 | `t_scrim_risksubs_l` | 风险订阅-多语言表 | 5 | [scrim_risksubs.md](./scrim_risksubs.md) |
| 15 | `t_scrim_risksubs_level` | 风险级别控制-子表 | 6 | [scrim_risksubs.md](./scrim_risksubs.md) |
| 16 | `t_scrim_risksubs_mapping` | 维度字段映射-子表 | 7 | [scrim_risksubs.md](./scrim_risksubs.md) |
| 17 | `t_scrim_risksubs_org` | 适用组织-子表 | 4 | [scrim_risksubs.md](./scrim_risksubs.md) |
| 18 | `t_scrim_riskwarning` | 风险预警设置-主表 | 20 | [scrim_riskwarning.md](./scrim_riskwarning.md) |
| 19 | `t_scrim_riskwarning_group` | 风险预警分组-主表 | 16 | [scrim_riskwarning_group.md](./scrim_riskwarning_group.md) |
| 20 | `t_scrim_riskwarning_group_l` | 风险预警分组-多语言表 | 6 | [scrim_riskwarning_group.md](./scrim_riskwarning_group.md) |
| 21 | `t_scrim_riskwarning_l` | 风险预警设置-多语言表 | 5 | [scrim_riskwarning.md](./scrim_riskwarning.md) |
| 22 | `t_scrim_riskwarningentry` | 风险规则-子表 | 10 | [scrim_riskwarning.md](./scrim_riskwarning.md) |
| 23 | `t_scrim_supply_credit` | 供应商信用表-主表 | 7 | [scrim_supply_credit.md](./scrim_supply_credit.md) |
| 24 | `t_scrim_supply_relation` | 供应链关系表-主表 | 8 | [scrim_supply_relation.md](./scrim_supply_relation.md) |
