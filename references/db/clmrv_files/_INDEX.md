# clmrv 模块表清单

> 本模块共收录 **19** 张表定义，来自 `clmrv_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category clmrv
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_clm_con_review_rule` | 合同评审规则设置-主表 | 24 | [clm_contract_review_rule.md](./clm_contract_review_rule.md) |
| 2 | `t_clm_con_review_rule_l` | 合同评审规则设置-多语言表 | 4 | [clm_contract_review_rule.md](./clm_contract_review_rule.md) |
| 3 | `t_clm_review_conm_type` | 适用合同类型-多选基础资料表 | 3 | [clm_contract_review_rule.md](./clm_contract_review_rule.md) |
| 4 | `t_clm_review_erdesignee` | 指定人员-多选基础资料表 | 3 | [clm_contract_review_rule.md](./clm_contract_review_rule.md) |
| 5 | `t_clm_review_sadesignee` | 指定人员-多选基础资料表 | 3 | [clm_contract_review_rule.md](./clm_contract_review_rule.md) |
| 6 | `t_clm_review_srdesignee` | 指定人员-多选基础资料表 | 3 | [clm_contract_review_rule.md](./clm_contract_review_rule.md) |
| 7 | `t_mscon_aiexamineentry` | 审查配置-子表 | 8 | [clm_mscon_aiexaminescheme.md](./clm_mscon_aiexaminescheme.md) |
| 8 | `t_mscon_aiexamineentry_l` | 审查配置-多语言表 | 6 | [clm_mscon_aiexaminescheme.md](./clm_mscon_aiexaminescheme.md) |
| 9 | `t_mscon_aiexaminescheme` | 审查方案-主表 | 16 | [clm_mscon_aiexaminescheme.md](./clm_mscon_aiexaminescheme.md) |
| 10 | `t_mscon_aiexaminescheme_l` | 审查方案-多语言表 | 5 | [clm_mscon_aiexaminescheme.md](./clm_mscon_aiexaminescheme.md) |
| 11 | `t_mscon_configinfo` | 参数配置信息-主表 | 7 | [mscon_configinfo.md](./mscon_configinfo.md) |
| 12 | `t_mscon_examineentry` | 单据体-子表 | 11 | [clm_mscon_examinerecord.md](./clm_mscon_examinerecord.md) |
| 13 | `t_mscon_examineitems` | 审查项-主表 | 18 | [clm_mscon_examineitems.md](./clm_mscon_examineitems.md) |
| 14 | `t_mscon_examineitems_l` | 审查项-多语言表 | 7 | [clm_mscon_examineitems.md](./clm_mscon_examineitems.md) |
| 15 | `t_mscon_examineitemsgroup` | 审查项分组-主表 | 15 | [mscon_examineitemsgroup.md](./mscon_examineitemsgroup.md) |
| 16 | `t_mscon_examineitemsgroup_l` | 审查项分组-多语言表 | 5 | [mscon_examineitemsgroup.md](./mscon_examineitemsgroup.md) |
| 17 | `t_mscon_examinerecord` | 审查结果-主表 | 22 | [clm_mscon_examinerecord.md](./clm_mscon_examinerecord.md) |
| 18 | `t_mscon_searchruleentry` | 检索规则单据体-子表 | 4 | [clm_mscon_examineitems.md](./clm_mscon_examineitems.md) |
| 19 | `t_mscon_searchruleentry_l` | 检索规则单据体-多语言表 | 4 | [clm_mscon_examineitems.md](./clm_mscon_examineitems.md) |
