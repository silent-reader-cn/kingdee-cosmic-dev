# 物料金额数据暂存单据-plm_plmsm_material_amount

## 物料金额数据暂存单据-主表 t_plmsm_material_amount

- **表名称：** 物料金额数据暂存单据-主表
- **表名：** t_plmsm_material_amount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fmaterialid | ERP物料id | int8 | 64 |  | √ | 0 | ERP物料id |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fclassifyid | 分类id | int8 | 64 |  | √ | 0 | 分类id |
| 7 | fpriceandtax | 采购金额（含税） | varchar | 50 |  | √ | ' ' | 采购金额（含税） |
| 8 | fperiodendprice | 存货金额 | varchar | 50 |  | √ | ' ' | 存货金额 |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_material_amount |  | fid |
| 2 | idx_plmsm_mat_amount_ferpmatid |  | fmaterialid |
