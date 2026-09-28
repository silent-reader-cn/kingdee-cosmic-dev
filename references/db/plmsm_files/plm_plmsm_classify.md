# 分类动态渲染模型-plm_plmsm_classify

## 分类动态渲染模型-主表 t_plm_pdm_basic_attr

- **表名称：** 分类动态渲染模型-主表
- **表名：** t_plm_pdm_basic_attr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanufacturer | fmanufacturer | varchar | 50 |  | √ | ' ' |  |
| 3 | felectricity | felectricity | numeric | 23 | 10 | √ | 0 |  |
| 4 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 5 | fcolor | fcolor | varchar | 50 |  | √ | ' ' |  |
| 6 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 7 | fresistance | fresistance | numeric | 23 | 10 | √ | 0 |  |
| 8 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 9 | fvoltage | fvoltage | numeric | 23 | 10 | √ | 0 |  |
| 10 | fspec | fspec | varchar | 50 |  | √ | ' ' |  |
| 11 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 12 | fmaterial | fmaterial | varchar | 50 |  | √ | ' ' |  |
| 13 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 14 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |
| 15 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pdm_basic_attr |  | fid |
| 2 | idx_basic_fmanufacturer |  | fmanufacturer |
