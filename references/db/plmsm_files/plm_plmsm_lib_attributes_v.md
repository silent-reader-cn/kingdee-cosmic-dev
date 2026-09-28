# 分类属性仓库版次-plm_plmsm_lib_attributes_v

## 分类属性仓库版次-主表 t_plm_pdm_basic_attrv

- **表名称：** 分类属性仓库版次-主表
- **表名：** t_plm_pdm_basic_attrv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fspec | 规格 | varchar | 255 |  | √ | ' ' | 规格 |
| 3 | fbasedataid | 多选基础资料使用 | int8 | 64 |  | √ | 0 | 多选基础资料使用 |
| 4 | fmanufacturer | fmanufacturer | varchar | 50 |  | √ | ' ' |  |
| 5 | fmaterialnum | 物料编码 | varchar | 50 |  | √ | ' ' | 物料编码 |
| 6 | fcolor | 颜色 | varchar | 255 |  | √ | ' ' | 颜色 |
| 7 | frevisionid | 版本ID | int8 | 64 |  |  | null | 版本ID |
| 8 | fmaterial | 材质 | varchar | 255 |  | √ | ' ' | 材质 |
| 9 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 10 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_basic_attrv_fmanufacturer |  | fmanufacturer |
| 2 | pk_t_plm_pdm_basic_attrv |  | fid |
