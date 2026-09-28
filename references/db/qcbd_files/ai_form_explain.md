# 表格解析数据-ai_form_explain

## 表格解析数据-主表 t_ai_form_explain

- **表名称：** 表格解析数据-主表
- **表名：** t_ai_form_explain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fformurl | 文件位置 | varchar | 1024 |  | √ | '' | 文件位置 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fnumber | 编号 | varchar | 50 |  | √ | '' | 编号 |
| 6 | fendtime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_form_explain |  | fid |
| 2 | idx_ai_form_explain_fnumber |  | fnumber |
