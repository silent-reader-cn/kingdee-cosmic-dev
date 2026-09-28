# 物料优选分组织数据单据-plm_plmsm_mat_prefdata

## 物料优选分组织数据单据-主表 t_plmsm_prefer_data

- **表名称：** 物料优选分组织数据单据-主表
- **表名：** t_plmsm_prefer_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fvalue | 数据值 | varchar | 100 |  | √ | ' ' | 数据值 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :存货价格 2 :采购价格 3 :呆滞数量 4 :库存数量 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialid | 物料id | int8 | 64 |  | √ | 0 | 物料id |
| 8 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 9 | ferpmaterialid | erp物料id | int8 | 64 |  | √ | 0 | erp物料id |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_prefer_data |  | fid |
| 2 | idx_preferdata_materialid |  | fmaterialid,ftype |
