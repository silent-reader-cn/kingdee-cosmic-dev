# PLM数据资源库-plm_data_bank

## PLM数据资源库-主表 t_plm_data_bank

- **表名称：** PLM数据资源库-主表
- **表名：** t_plm_data_bank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdata_tag | 数据内容_详情 | text | 0 |  |  | null | 数据内容_详情 |
| 3 | fdata | 数据内容 | varchar | 128 |  | √ | ' ' | 数据内容 |
| 4 | fdatatype | 数据类型 | varchar | 300 |  | √ | '0' | 数据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fdatatype |
| 2 | fdatatype | fid,fdatatype |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_data_bank_data |  | fdata |
| 2 | pk_t_plm_data_bank |  | fid,fdatatype |
