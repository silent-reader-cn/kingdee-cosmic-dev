# 模型关联关系-plm_pdm_model_relation

## 模型关联关系-主表 t_plm_pdm_model_relation

- **表名称：** 模型关联关系-主表
- **表名：** t_plm_pdm_model_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendid | 结束ID | int8 | 64 |  | √ | 0 | 结束ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :结构视图展示 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftargetmodelid | 目标模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 8 | fsourcemodelid | 源模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 9 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 10 | fbeginid | 开始ID | int8 | 64 |  | √ | 0 | 开始ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_model_relation_fk |  | fsourcemodelid |
| 2 | pk_t_plm_pdm_model_relation |  | fid |
