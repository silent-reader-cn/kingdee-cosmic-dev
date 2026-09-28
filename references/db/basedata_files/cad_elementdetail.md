# 成本要素与子要素关系-cad_elementdetail

## 成本要素与子要素关系-主表 t_cad_elementdetail

- **表名称：** 成本要素与子要素关系-主表
- **表名：** t_cad_elementdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 4 | felementtypeid | 成本要素分类 | int8 | 64 |  | √ | 0 | 成本要素分类 cad_elementtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_elementdetail_pkey |  | fid |
