# dhc 模块表清单

> 本模块共收录 **23** 张表定义，来自 `dhc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category dhc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_dhc_billaccessed` | 接入单据-主表 | 12 | [dhc_billaccessed.md](./dhc_billaccessed.md) |
| 2 | `t_dhc_billaccessed_l` | 接入单据-多语言表 | 4 | [dhc_billaccessed.md](./dhc_billaccessed.md) |
| 3 | `t_dhc_billclassify` | 报账分类-主表 | 9 | [dhc_billclassification.md](./dhc_billclassification.md) |
| 4 | `t_dhc_billclassify_l` | 报账分类-多语言表 | 4 | [dhc_billclassification.md](./dhc_billclassification.md) |
| 5 | `t_dhc_billdatainit` | 报账数据初始化-主表 | 14 | [dhc_billdatainit.md](./dhc_billdatainit.md) |
| 6 | `t_dhc_billidentry` | 单据体-子表 | 4 | [dhc_billclassification.md](./dhc_billclassification.md) |
| 7 | `t_dhc_billmapping` | 单据映射-主表 | 19 | [dhc_billmapping.md](./dhc_billmapping.md) |
| 8 | `t_dhc_billmapping_l` | 单据映射-多语言表 | 6 | [dhc_billmapping.md](./dhc_billmapping.md) |
| 9 | `t_dhc_billstatusdetail` | 单据状态转换流水记录表-主表 | 10 | [dhc_billstatusdetail.md](./dhc_billstatusdetail.md) |
| 10 | `t_dhc_billsubject` | 单据主题-主表 | 12 | [dhc_billsubject.md](./dhc_billsubject.md) |
| 11 | `t_dhc_billsubject_l` | 单据主题-多语言表 | 4 | [dhc_billsubject.md](./dhc_billsubject.md) |
| 12 | `t_dhc_btn_entry` | 单据体-子表 | 4 | [dhc_buttonvisible_conf.md](./dhc_buttonvisible_conf.md) |
| 13 | `t_dhc_btnconf` | 单据按钮隐藏配置-主表 | 3 | [dhc_buttonvisible_conf.md](./dhc_buttonvisible_conf.md) |
| 14 | `t_dhc_datainitrecord` | 报账初始化记录-主表 | 17 | [dhc_datainitrecord.md](./dhc_datainitrecord.md) |
| 15 | `t_dhc_inquirybill` | 共享问询工单-主表 | 17 | [dhc_inquirybill.md](./dhc_inquirybill.md) |
| 16 | `t_dhc_inquirybill_l` | 共享问询工单-多语言表 | 4 | [dhc_inquirybill.md](./dhc_inquirybill.md) |
| 17 | `t_dhc_knowledge_add` | 新增知识问答-主表 | 7 | [dhc_knowledge_add.md](./dhc_knowledge_add.md) |
| 18 | `t_dhc_knowledge_entry` | 知识问答单据体-子表 | 8 | [dhc_knowledge_add.md](./dhc_knowledge_add.md) |
| 19 | `t_dhc_mybilllist` | 我的报账-主表 | 23 | [dhc_mybilllist.md](./dhc_mybilllist.md) |
| 20 | `t_dhc_operation` | 单据操作-主表 | 5 | [dhc_operation.md](./dhc_operation.md) |
| 21 | `t_dhc_reimorder` | 报账工单-主表 | 18 | [dhc_reimorder.md](./dhc_reimorder.md) |
| 22 | `t_dhc_reimorder_l` | 报账工单-多语言表 | 4 | [dhc_reimorder.md](./dhc_reimorder.md) |
| 23 | `t_dhc_subjectentry` | 单据体-子表 | 7 | [dhc_billsubject.md](./dhc_billsubject.md) |
