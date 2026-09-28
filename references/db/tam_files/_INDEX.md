# tam 模块表清单

> 本模块共收录 **21** 张表定义，来自 `tam_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category tam
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_tam_archives_change` | 税务档案变更记录-主表 | 5 | [tam_archives_change.md](./tam_archives_change.md) |
| 2 | `t_tam_archives_change_l` | 税务档案变更记录-多语言表 | 3 | [tam_archives_change.md](./tam_archives_change.md) |
| 3 | `t_tam_archives_label` | 档案标签单据体-子表 | 4 | [tam_tax_archives.md](./tam_tax_archives.md) |
| 4 | `t_tam_archives_type` | 档案类型-主表 | 12 | [tam_archives_type.md](./tam_archives_type.md) |
| 5 | `t_tam_archives_type_l` | 档案类型-多语言表 | 4 | [tam_archives_type.md](./tam_archives_type.md) |
| 6 | `t_tam_archivestype_group` | 档案类型分组-主表 | 13 | [tam_archivestype_group.md](./tam_archivestype_group.md) |
| 7 | `t_tam_archivestype_group_l` | 档案类型分组-多语言表 | 6 | [tam_archivestype_group.md](./tam_archivestype_group.md) |
| 8 | `t_tam_base_init_config` | 基础初始化配置-主表 | 16 | [tam_base_init_config.md](./tam_base_init_config.md) |
| 9 | `t_tam_base_init_org` | 税务组织信息初始化-主表 | 6 | [tam_base_init_org.md](./tam_base_init_org.md) |
| 10 | `t_tam_base_init_org_group` | 汇总方案初始化-主表 | 8 | [tam_base_init_org_group.md](./tam_base_init_org_group.md) |
| 11 | `t_tam_base_init_org_map` | 税务组织映射关系初始化-主表 | 8 | [tam_base_init_org_mapping.md](./tam_base_init_org_mapping.md) |
| 12 | `t_tam_base_init_org_param` | 税务组织参数配置初始化-主表 | 7 | [tam_base_init_org_param.md](./tam_base_init_org_param.md) |
| 13 | `t_tam_base_init_taxmain` | 纳税主体信息初始化-主表 | 6 | [tam_base_init_taxmain.md](./tam_base_init_taxmain.md) |
| 14 | `t_tam_change_detail` | 变更明细-子表 | 6 | [tam_archives_change.md](./tam_archives_change.md) |
| 15 | `t_tam_declare_entry` | 单据体-子表 | 7 | [tam_declare_bill.md](./tam_declare_bill.md) |
| 16 | `t_tam_declare_entry` | 申报表分录单据-主表 | 7 | [tam_declare_entry.md](./tam_declare_entry.md) |
| 17 | `t_tam_tax_archives` | 税务档案-主表 | 14 | [tam_tax_archives.md](./tam_tax_archives.md) |
| 18 | `t_tam_tax_archives_l` | 税务档案-多语言表 | 4 | [tam_tax_archives.md](./tam_tax_archives.md) |
| 19 | `t_tctb_declare_main` | 申报表单据列表-主表 | 80 | [tam_declare_bill.md](./tam_declare_bill.md) |
| 20 | `t_tctb_draft_main` | 底稿列表-主表 | 32 | [tam_draft_bill.md](./tam_draft_bill.md) |
| 21 | `t_tpo_declare_main_tsd` | 计提底稿任务-主表 | 59 | [tam_declare_main_tsd.md](./tam_declare_main_tsd.md) |
