# msmob 模块表清单

> 本模块共收录 **22** 张表定义，来自 `msmob_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category msmob
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_mob_datasourceconfig` | 数据源配置-主表 | 13 | [mob_datasourceconfig.md](./mob_datasourceconfig.md) |
| 2 | `t_mob_datasourceconfig_l` | 数据源配置-多语言表 | 5 | [mob_datasourceconfig.md](./mob_datasourceconfig.md) |
| 3 | `t_mob_entrymapping` | 分录映射关系-子表 | 10 | [mob_datasourceconfig.md](./mob_datasourceconfig.md) |
| 4 | `t_mob_fieldmaprelation` | 字段映射关系-子表 | 15 | [mob_datasourceconfig.md](./mob_datasourceconfig.md) |
| 5 | `t_mob_invqfieldmapentry` | 单据体-子表 | 14 | [msmob_invquerymapconfig.md](./msmob_invquerymapconfig.md) |
| 6 | `t_mob_invquerymapconfig` | 移动库存查询字段映射配置-主表 | 14 | [msmob_invquerymapconfig.md](./msmob_invquerymapconfig.md) |
| 7 | `t_mob_invquerymapconfig_l` | 移动库存查询字段映射配置-多语言表 | 5 | [msmob_invquerymapconfig.md](./msmob_invquerymapconfig.md) |
| 8 | `t_mob_searchkey_e` | 搜索控件字段-子表 | 6 | [mob_datasourceconfig.md](./mob_datasourceconfig.md) |
| 9 | `t_msmob_parseservice` | 码解析服务配置-主表 | 18 | [msmob_parseserviceconfig.md](./msmob_parseserviceconfig.md) |
| 10 | `t_msmob_parseservice_l` | 码解析服务配置-多语言表 | 5 | [msmob_parseserviceconfig.md](./msmob_parseserviceconfig.md) |
| 11 | `t_msmob_scan_result_cfg` | 扫描结果配置-主表 | 14 | [msmob_scan_result_cfg.md](./msmob_scan_result_cfg.md) |
| 12 | `t_msmob_scan_result_cfg_l` | 扫描结果配置-多语言表 | 4 | [msmob_scan_result_cfg.md](./msmob_scan_result_cfg.md) |
| 13 | `t_msmob_scan_skill` | 技能-主表 | 13 | [msmob_skill.md](./msmob_skill.md) |
| 14 | `t_msmob_scan_skill_l` | 技能-多语言表 | 5 | [msmob_skill.md](./msmob_skill.md) |
| 15 | `t_msmob_scheme` | 移动方案基础资料-主表 | 17 | [msmob_scheme.md](./msmob_scheme.md) |
| 16 | `t_msmob_scheme_l` | 移动方案基础资料-多语言表 | 5 | [msmob_scheme.md](./msmob_scheme.md) |
| 17 | `t_msmob_skill_entry` | 技能选择分录关系-子表 | 8 | [msmob_scan_result_cfg.md](./msmob_scan_result_cfg.md) |
| 18 | `t_msmob_skill_family` | 技能族-主表 | 13 | [msmob_skill_family.md](./msmob_skill_family.md) |
| 19 | `t_msmob_skill_family_l` | 技能族-多语言表 | 4 | [msmob_skill_family.md](./msmob_skill_family.md) |
| 20 | `t_msmob_skill_skillfamily` | 所属技能族-多选基础资料表 | 3 | [msmob_skill.md](./msmob_skill.md) |
| 21 | `t_msmob_unittest_support` | 数据源配置单元测试（勿删）-主表 | 0 | [msmob_unittest_support.md](./msmob_unittest_support.md) |
| 22 | `t_msmob_unittest_support_l` | 数据源配置单元测试（勿删）-多语言表 | 0 | [msmob_unittest_support.md](./msmob_unittest_support.md) |
