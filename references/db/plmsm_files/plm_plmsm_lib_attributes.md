# 分类属性仓库-plm_plmsm_lib_attributes

## 分类属性仓库-主表 t_plm_pdm_basic_attr

- **表名称：** 分类属性仓库-主表
- **表名：** t_plm_pdm_basic_attr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasedataid | 多选基础资料使用 | int8 | 64 |  | √ | 0 | 多选基础资料使用 |
| 3 | fmanufacturer | fmanufacturer | varchar | 50 |  | √ | ' ' |  |
| 4 | felectricity | felectricity | numeric | 23 | 10 | √ | 0 |  |
| 5 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 6 | fmaterialnum | 物料编码 | varchar | 50 |  | √ | ' ' | 物料编码 |
| 7 | fcolor | 颜色 | varchar | 255 |  | √ | ' ' | 颜色 |
| 8 | fresistance | fresistance | numeric | 23 | 10 | √ | 0 |  |
| 9 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 10 | fvoltage | fvoltage | numeric | 23 | 10 | √ | 0 |  |
| 11 | fspec | 规格 | varchar | 255 |  | √ | ' ' | 规格 |
| 12 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 13 | fmaterial | 材质 | varchar | 255 |  | √ | ' ' | 材质 |
| 14 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 15 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 16 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pdm_basic_attr |  | fid |
| 2 | idx_basic_fmanufacturer |  | fmanufacturer |
