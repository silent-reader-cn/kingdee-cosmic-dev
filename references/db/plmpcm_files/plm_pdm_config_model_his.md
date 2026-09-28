# 型号配置参数记录表单-plm_pdm_config_model_his

## 型号配置参数记录表单-主表 t_pcm_modelnum_params_his

- **表名称：** 型号配置参数记录表单-主表
- **表名：** t_pcm_modelnum_params_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fis_multi_choose | 是否多选 | bpchar | 1 |  | √ | '0' | 是否多选 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fconfig_item | 选项 | int8 | 64 |  | √ | 0 | [选项 plm_pdm_option](../plmsm_files/plm_pdm_option.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fconfig_collect_id | 配置集合ID | int8 | 64 |  | √ | 0 | 配置集合ID |
| 7 | fmanual | 手工录入值 | varchar | 512 |  | √ | ' ' | 手工录入值 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fconfig_value | 选项值 | int8 | 64 |  | √ | 0 | [选项值 plm_pdm_optionvalue](../plmsm_files/plm_pdm_optionvalue.md) |
| 10 | fbomid | 配置BOMID | int8 | 64 |  | √ | 0 | 配置BOMID |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fconfigresultid | 配置结果 | int8 | 64 |  | √ | 0 | 配置结果 |
| 13 | fmodelnum_id | 所属型号 | int8 | 64 |  | √ | 0 | 所属型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pcm_modelnum_params_his |  | fid |
| 2 | idx_t_pcm_modelnum_param_his |  | fbomid,fconfig_collect_id |
