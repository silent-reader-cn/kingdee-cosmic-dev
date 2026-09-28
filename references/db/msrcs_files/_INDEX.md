# msrcs 模块表清单

> 本模块共收录 **34** 张表定义，来自 `msrcs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category msrcs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_msrcs_interfacerule` | 界面规则单据体-子表 | 6 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 2 | `t_msrcs_interfacerule_l` | 界面规则单据体-多语言表 | 4 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 3 | `t_msrcs_policyparse` | 政策解析规则-主表 | 17 | [msrcs_policyparserule.md](./msrcs_policyparserule.md) |
| 4 | `t_msrcs_policyparse_l` | 政策解析规则-多语言表 | 4 | [msrcs_policyparserule.md](./msrcs_policyparserule.md) |
| 5 | `t_msrcs_policyparserc` | 计算变量映射规则-子表 | 10 | [msrcs_policyparserule.md](./msrcs_policyparserule.md) |
| 6 | `t_msrcs_policyparsere` | 查询条件匹配规则-子表 | 10 | [msrcs_policyparserule.md](./msrcs_policyparserule.md) |
| 7 | `t_msrcs_rebateclass` | 返利类别-主表 | 15 | [msrcs_rebateclass.md](./msrcs_rebateclass.md) |
| 8 | `t_msrcs_rebateclass_l` | 返利类别-多语言表 | 4 | [msrcs_rebateclass.md](./msrcs_rebateclass.md) |
| 9 | `t_msrcs_rebatefactor` | 返利计算指标-主表 | 20 | [msrcs_rebatefactor.md](./msrcs_rebatefactor.md) |
| 10 | `t_msrcs_rebatefactor_l` | 返利计算指标-多语言表 | 4 | [msrcs_rebatefactor.md](./msrcs_rebatefactor.md) |
| 11 | `t_msrcs_rebatefactorde` | 指定维度分录-子表 | 7 | [msrcs_rebatefactor.md](./msrcs_rebatefactor.md) |
| 12 | `t_msrcs_rebateformula` | 返利计算公式-主表 | 21 | [msrcs_rebateformula.md](./msrcs_rebateformula.md) |
| 13 | `t_msrcs_rebateformula_l` | 返利计算公式-多语言表 | 4 | [msrcs_rebateformula.md](./msrcs_rebateformula.md) |
| 14 | `t_msrcs_rebateformulae` | 插件变量-子表 | 5 | [msrcs_rebateformula.md](./msrcs_rebateformula.md) |
| 15 | `t_msrcs_rebateoutput` | 计算输出规则-主表 | 20 | [msrcs_rebateoutput.md](./msrcs_rebateoutput.md) |
| 16 | `t_msrcs_rebateoutput_be` | 属性单据体-子表 | 14 | [msrcs_rebateoutput.md](./msrcs_rebateoutput.md) |
| 17 | `t_msrcs_rebateoutput_l` | 计算输出规则-多语言表 | 4 | [msrcs_rebateoutput.md](./msrcs_rebateoutput.md) |
| 18 | `t_msrcs_rebateschema` | 返利计算方案-主表 | 15 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 19 | `t_msrcs_rebateschema_ac` | 返利预提公式分录-子表 | 10 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 20 | `t_msrcs_rebateschema_cf` | 计算公式分录-子表 | 8 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 21 | `t_msrcs_rebateschema_js` | 判断标准分录-子表 | 7 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 22 | `t_msrcs_rebateschema_l` | 返利计算方案-多语言表 | 4 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 23 | `t_msrcs_rebateschema_se` | 数据源分录-子表 | 9 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 24 | `t_msrcs_rebateschemaobj` | 返利对象单据体-子表 | 6 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 25 | `t_msrcs_rebatesource` | 返利计算数据源-主表 | 15 | [msrcs_rebatesource.md](./msrcs_rebatesource.md) |
| 26 | `t_msrcs_rebatesource_e` | 字段映射分录-子表 | 19 | [msrcs_rebatesource.md](./msrcs_rebatesource.md) |
| 27 | `t_msrcs_rebatesource_e_l` | 字段映射分录-多语言表 | 4 | [msrcs_rebatesource.md](./msrcs_rebatesource.md) |
| 28 | `t_msrcs_rebatesource_l` | 返利计算数据源-多语言表 | 4 | [msrcs_rebatesource.md](./msrcs_rebatesource.md) |
| 29 | `t_msrcs_rebatesourcelink` | 单据体-子表 | 8 | [msrcs_rebatesource.md](./msrcs_rebatesource.md) |
| 30 | `t_msrcs_rowamtmode` | 返利行金额计算方式-主表 | 11 | [msrcs_rowamtmode.md](./msrcs_rowamtmode.md) |
| 31 | `t_msrcs_rowamtmode_l` | 返利行金额计算方式-多语言表 | 4 | [msrcs_rowamtmode.md](./msrcs_rowamtmode.md) |
| 32 | `t_msrcs_schema_qcond` | 查询条件匹配规则-子表 | 8 | [msrcs_rebateschema.md](./msrcs_rebateschema.md) |
| 33 | `t_msrcs_subtask` | 返利子任务-主表 | 12 | [msrcs_subtask.md](./msrcs_subtask.md) |
| 34 | `t_msrcs_task` | 返利任务-主表 | 10 | [msrcs_task.md](./msrcs_task.md) |
