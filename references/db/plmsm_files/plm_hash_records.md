# 模型列名时间记录表-plm_hash_records

## 模型列名时间记录表-主表 t_plm_model_hash_record

- **表名称：** 模型列名时间记录表-主表
- **表名：** t_plm_model_hash_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fmodelid | 模型 | int8 | 64 |  |  | 0 | 模型 |
| 6 | fcolumnname | 列名称 | varchar | 100 |  | √ | ' ' | 列名称 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_model_hash_record |  | fmodelid,fcolumnname |
| 2 | pk_t_plm_model_hash_record |  | fid |
