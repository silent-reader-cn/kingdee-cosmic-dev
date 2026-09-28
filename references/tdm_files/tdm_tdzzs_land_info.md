# 土地信息-tdm_tdzzs_land_info

## 土地信息-主表 t_tdm_tdzzs_land_info

- **表名称：** 土地信息-主表
- **表名：** t_tdm_tdzzs_land_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flandsourceinfo | 土地税源信息 | varchar | 50 |  | √ | ' ' | 土地税源信息 |
| 3 | flandcontractno | 土地使用权受让（行政划拨）合同号 | varchar | 50 |  | √ | ' ' | 土地使用权受让（行政划拨）合同号 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | flanddate | 受让（行政划拨）时间 | timestamp | 0 |  |  | null | 受让（行政划拨）时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tdzzs_land_info_1 |  | fid |
| 2 | pk_tdm_tdzzs_land_info |  | fentryid |
