# plmpcm 模块表清单

> 本模块共收录 **8** 张表定义，来自 `plmpcm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category plmpcm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_pcm_modelnum_params_his` | 型号配置参数记录表单-主表 | 13 | [plm_pdm_config_model_his.md](./plm_pdm_config_model_his.md) |
| 2 | `t_plm_cof_con_main` | 配置BOM条件关系表单-主表 | 6 | [plm_conf_con_relation.md](./plm_conf_con_relation.md) |
| 3 | `t_plm_cof_con_relation` | 单据体-子表 | 25 | [plm_conf_con_relation.md](./plm_conf_con_relation.md) |
| 4 | `t_plm_pcm_generate_list` | 单据体-子表 | 9 | [plm_pcm_configresult.md](./plm_pcm_configresult.md) |
| 5 | `t_plm_pcm_modelnum_params` | 型号配置参数表单-主表 | 12 | [plm_pdm_config_modelnum_p.md](./plm_pdm_config_modelnum_p.md) |
| 6 | `t_plmpcm_configresult` | 配置结果-主表 | 13 | [plm_pcm_configresult.md](./plm_pcm_configresult.md) |
| 7 | `t_plmpcm_gen_batch` | 生成批次单据-主表 | 9 | [plm_plmpcm_gen_batch.md](./plm_plmpcm_gen_batch.md) |
| 8 | `t_plmpcm_gen_result` | 生成结果及校验单据-主表 | 13 | [plm_plmpcm_gen_result.md](./plm_plmpcm_gen_result.md) |
