# 产业关系表-scrim_industry_relation

## 产业关系表-主表 t_scrim_industry_relation

- **表名称：** 产业关系表-主表
- **表名：** t_scrim_industry_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | ftype | 类型 | varchar | 10 |  |  | null | 类型 |
| 5 | fparentid | 父级Id | int8 | 64 |  | √ | 0 | 父级Id |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_industry_relation |  | fid |
| 2 | idx_industry_parentid |  | fparentid |
