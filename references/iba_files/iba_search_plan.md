# 查询方案-iba_search_plan

## 查询方案-主表 t_iba_searchplan

- **表名称：** 查询方案-主表
- **表名：** t_iba_searchplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalues | 查询方案 | varchar | 255 |  | √ | ' ' | 查询方案 |
| 3 | fvalues_tag | 查询方案_详情 | text | 0 |  |  | '' | 查询方案_详情 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fentityid | 元数据标识 | varchar | 50 |  | √ | ' ' | 元数据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_searchplan |  | fid |
| 2 | idx_iba_searchplan_user |  | fuserid |
