# 前端词条-cts_frontend_entry

## 前端词条-主表 t_cts_frontendentry

- **表名称：** 前端词条-主表
- **表名：** t_cts_frontendentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 原名称 | varchar | 1024 |  | √ | ' ' | 原名称 |
| 4 | ftype | 词条类型 | varchar | 50 |  | √ | ' ' | 词条类型 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnewname | 新名称 | varchar | 1024 |  | √ | ' ' | 新名称 |
| 8 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |
| 9 | flangid | 语言 | int8 | 64 |  | √ | 0 | 语言种类 inte_language |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_frontendentry |  | fid |
| 2 | idx_t_cts_frontendentry |  | fnumber |
