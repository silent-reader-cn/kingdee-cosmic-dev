# 型号配置参数表单-plm_pdm_config_modelnum_p

## 型号配置参数表单-主表 t_plm_pcm_modelnum_params

- **表名称：** 型号配置参数表单-主表
- **表名：** t_plm_pcm_modelnum_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfig_value | 选项值 | int8 | 64 |  | √ | 0 | [选项值 plm_pdm_optionvalue](../plmsm_files/plm_pdm_optionvalue.md) |
| 3 | fis_multi_choose | 是否多选 | bpchar | 1 |  | √ | '0' | 是否多选 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbomid | 配置BOMID | int8 | 64 |  | √ | 0 | 配置BOMID |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fconfig_item | 选项 | int8 | 64 |  | √ | 0 | [选项 plm_pdm_option](../plmsm_files/plm_pdm_option.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fconfig_collect_id | 配置集合ID | int8 | 64 |  | √ | 0 | 配置集合ID |
| 10 | fmanual | 手工录入值 | varchar | 512 |  | √ | ' ' | 手工录入值 |
| 11 | fmodelnum_id | 所属型号 | int8 | 64 |  | √ | 0 | 所属型号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pcm_modelnum_params |  | fid |
| 2 | idx_t_plm_pcm_modelnum_param |  | fbomid,fconfig_collect_id |
