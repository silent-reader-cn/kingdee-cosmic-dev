# 分类属性仓库-plm_plmsm_lib_attributes

## 分类属性仓库-主表 t_plm_pdm_basic_attr

- **表名称：** 分类属性仓库-主表
- **表名：** t_plm_pdm_basic_attr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanufacturer | fmanufacturer | varchar | 50 |  | √ | ' ' |  |
| 3 | felectricity | felectricity | numeric | 23 | 10 | √ | 0 |  |
| 4 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 5 | fcolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色 |
| 6 | fmaterialnum | 物料编码 | varchar | 50 |  | √ | ' ' | 物料编码 |
| 7 | fresistance | fresistance | numeric | 23 | 10 | √ | 0 |  |
| 8 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 9 | fvoltage | fvoltage | numeric | 23 | 10 | √ | 0 |  |
| 10 | fspec | 规格 | varchar | 50 |  | √ | ' ' | 规格 |
| 11 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 12 | fmaterial | 材质 | varchar | 50 |  | √ | ' ' | 材质 |
| 13 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 14 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |
| 15 | fmaterialname | 物料名称 | varchar | 50 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pdm_basic_attr |  | fid |
| 2 | idx_basic_fmanufacturer |  | fmanufacturer |
