# 分类动态渲染模型-plm_plmsm_classify

## 分类动态渲染模型-主表 t_plm_pdm_basic_attr

- **表名称：** 分类动态渲染模型-主表
- **表名：** t_plm_pdm_basic_attr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 |  |
| 3 | fmanufacturer | fmanufacturer | varchar | 50 |  | √ | ' ' |  |
| 4 | felectricity | felectricity | numeric | 23 | 10 | √ | 0 |  |
| 5 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 6 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 7 | fcolor | fcolor | varchar | 255 |  | √ | ' ' |  |
| 8 | fresistance | fresistance | numeric | 23 | 10 | √ | 0 |  |
| 9 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 10 | fvoltage | fvoltage | numeric | 23 | 10 | √ | 0 |  |
| 11 | fspec | fspec | varchar | 255 |  | √ | ' ' |  |
| 12 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 13 | fmaterial | fmaterial | varchar | 255 |  | √ | ' ' |  |
| 14 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 15 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 16 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pdm_basic_attr |  | fid |
| 2 | idx_basic_fmanufacturer |  | fmanufacturer |
