# 配置结果-plm_pcm_configresult

## 配置结果-主表 t_plmpcm_configresult

- **表名称：** 配置结果-主表
- **表名：** t_plmpcm_configresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductmodelid | 产品型号 | int8 | 64 |  | √ | 0 | [产品型号 plm_pdm_productmodel](../plmsm_files/plm_pdm_productmodel.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fconfigresultbatchid | 配置结果批次 | int4 | 32 |  | √ | 0 | 配置结果批次 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fconfigbomid | 配置BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |
| 8 | fconfigcollectid | 配置集合 | int8 | 64 |  | √ | 0 | [配置集合 plm_pdm_configcollect](../plmsm_files/plm_pdm_configcollect.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fproductmodelvalueid | 产品型号值 | int8 | 64 |  | √ | 0 | [产品型号值 plm_pdm_modelvalue](../plmsm_files/plm_pdm_modelvalue.md) |
| 12 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 13 | finstancebomid | 实例BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmpcm_configresult |  | fid |
| 2 | idx_configresult_fcongifbomid |  | fconfigbomid |

---

## 单据体-子表 t_plm_pcm_generate_list

- **表名称：** 单据体-子表
- **表名：** t_plm_pcm_generate_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfig_value | fconfig_value | int8 | 64 |  | √ | 0 |  |
| 3 | fconfigurablebomid | 可配置BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |
| 4 | fgeneratematerialid | 生成的物料 | int8 | 64 |  | √ | 0 | [物料版本 plm_pdm_material_revision](../plmsm_files/plm_pdm_material_revision.md) |
| 5 | fconfigurablematerialid | 可配置物料 | int8 | 64 |  | √ | 0 | [物料版本 plm_pdm_material_revision](../plmsm_files/plm_pdm_material_revision.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmanual | fmanual | int8 | 64 |  | √ | 0 |  |
| 8 | fgeneratebomid | 生成的BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pcm_generate_list |  | fid |
| 2 | pk_t_plm_pcm_generate_list |  | fentryid |
