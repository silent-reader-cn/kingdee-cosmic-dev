# 库存检验信息-qcnp_invinsp_info

## 库存检验信息-主表 t_qcnp_invinsp_inf

- **表名称：** 库存检验信息-主表
- **表名：** t_qcnp_invinsp_inf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flastinspdate | 最新检验日期 | timestamp | 0 |  |  | null | 最新检验日期 |
| 3 | fincheck | 是否在检 | bpchar | 1 |  | √ | '0' | 是否在检 |
| 4 | finvdimensiod_tag | finvdimensiod_tag | text | 0 |  |  | null |  |
| 5 | fmaterialid | 物料ID | int8 | 64 |  | √ | 0 | 物料ID |
| 6 | fexeschemeid | fexeschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | finventoryid | 及时库存ID | int8 | 64 |  | √ | 0 | 及时库存ID |
| 8 | fdatasource | 数据源 | varchar | 5 |  | √ | ' ' | 数据源,枚举: A :即时库存 B :物料主数据 |
| 9 | finvdimensiod | 库存维度 | varchar | 2000 |  | √ | ' ' | 库存维度 |
| 10 | finspres | finspres | varchar | 5 |  | √ | ' ' |  |
| 11 | fupdatedate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcnp_invinsp_fmat |  | fmaterialid |
| 2 | idx_qcnp_invinsp_finv |  | finventoryid |
| 3 | pk_qcnp_invinsp_inf |  | fid |
