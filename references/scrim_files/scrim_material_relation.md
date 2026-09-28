# 物料关联表单-scrim_material_relation

## 物料关联表单-主表 t_scrim_material_relation

- **表名称：** 物料关联表单-主表
- **表名：** t_scrim_material_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 4 | fstandardname | 标准名称 | varchar | 512 |  | √ | ' ' | 标准名称 |
| 5 | ftype | 类型 | varchar | 10 |  | √ | ' ' | 类型,枚举: 0 :物料 1 :产品结构 2 :大宗商品 |
| 6 | fparentid | 父级id | int8 | 64 |  |  | null | 父级id |
| 7 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fproportion | 占比 | numeric | 19 | 6 |  | null | 占比 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_material_relation |  | fid |
| 2 | idx_material_parentid |  | fparentid |
