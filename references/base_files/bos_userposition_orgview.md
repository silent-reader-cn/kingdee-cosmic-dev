# 人员任职组织视图关系-bos_userposition_orgview

## 人员任职组织视图关系-主表 t_sec_userposorgview

- **表名称：** 人员任职组织视图关系-主表
- **表名：** t_sec_userposorgview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserpositionid | 人员任职 | int8 | 64 |  | √ | 0 | 人员任职 bos_userposition |
| 3 | fisdisplay | 显示 | varchar | 1 |  | √ | ' ' | 显示 |
| 4 | fviewid | 行政组织视图 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_userposorgview_pkey |  | fid |
| 2 | idx_sec_userposorgview_view |  | fviewid |
