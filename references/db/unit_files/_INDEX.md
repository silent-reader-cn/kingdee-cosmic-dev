# unit 模块表清单

> 本模块共收录 **16** 张表定义，来自 `unit_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category unit
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_unitestresultdetail` | 单据体-子表 | 10 | [ide_unit_test_result.md](./ide_unit_test_result.md) |
| 2 | `t_bas_unittestdetail` | 单元测试功能发布-主表 | 20 | [ide_unit_test_detail.md](./ide_unit_test_detail.md) |
| 3 | `t_bas_unittestdetail_a` | 单元测试功能发布-分表 | 6 | [ide_unit_test_detail.md](./ide_unit_test_detail.md) |
| 4 | `t_bas_unittestdetail_l` | 单元测试功能发布-多语言表 | 4 | [ide_unit_test_detail.md](./ide_unit_test_detail.md) |
| 5 | `t_bas_unittestresult` | 单元测试结果-主表 | 7 | [ide_unit_test_result.md](./ide_unit_test_result.md) |
| 6 | `t_unit_group` | 测试分组-主表 | 0 | [ut_group.md](./ut_group.md) |
| 7 | `t_unit_group_l` | 测试分组-多语言表 | 0 | [ut_group.md](./ut_group.md) |
| 8 | `t_unit_testformks` | KS基础资料测试-主表 | 0 | [unit_for_ks.md](./unit_for_ks.md) |
| 9 | `t_unit_testformks_l` | KS基础资料测试-多语言表 | 0 | [unit_for_ks.md](./unit_for_ks.md) |
| 10 | `t_unitdanjuti` | 单据体-子表 | 0 | [unit_test_bill.md](./unit_test_bill.md) |
| 11 | `t_unittestbill` | 单元测试用的单据-主表 | 0 | [unit_test_bill.md](./unit_test_bill.md) |
| 12 | `t_ut_app_set` | 应用配置单-主表 | 9 | [ut_app_set.md](./ut_app_set.md) |
| 13 | `t_ut_base_runtime` | 基础资料运行时测试-主表 | 8 | [ut_base_runtime.md](./ut_base_runtime.md) |
| 14 | `t_ut_base_runtime_l` | 基础资料运行时测试-多语言表 | 4 | [ut_base_runtime.md](./ut_base_runtime.md) |
| 15 | `t_ut_bill_runtime` | 单据运行时测试-主表 | 9 | [ut_bill_runtime.md](./ut_bill_runtime.md) |
| 16 | `t_ut_white_list` | 测试统计表单白名单-主表 | 3 | [ut_report_form_white_list.md](./ut_report_form_white_list.md) |
