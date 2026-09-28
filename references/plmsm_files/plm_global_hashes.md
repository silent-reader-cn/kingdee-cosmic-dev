# plm_global_hashes-plm_global_hashes

## plm_global_hashes-主表 t_plm_global_hash

- **表名称：** plm_global_hashes-主表
- **表名：** t_plm_global_hash

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fhashstring | hash串 | varchar | 1024 |  | √ | ' ' | hash串 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | frealvalue | 实际值 | int8 | 64 |  |  | 0 | 实际值 |
| 7 | fhashvalue | hash值 | int8 | 64 |  | √ | 0 | hash值 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_global_hash |  | fhashvalue,frealvalue |
| 2 | pk_t_plm_global_hash |  | fid |
