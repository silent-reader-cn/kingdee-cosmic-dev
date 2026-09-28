# CAD迁移结果-plmdc_cadupdateresult

## CAD迁移结果-主表 t_plmdc_cadupdate_result

- **表名称：** CAD迁移结果-主表
- **表名：** t_plmdc_cadupdate_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | value | varchar | 50 |  | √ | ' ' | value |
| 3 | fkey | key | varchar | 50 |  | √ | ' ' | key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_cadupdate_result |  | fid |
| 2 | idx_plmdc_up_result_key |  | fkey |
