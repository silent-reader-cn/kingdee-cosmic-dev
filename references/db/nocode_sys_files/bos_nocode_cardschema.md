# 工作台视图-bos_nocode_cardschema

## 工作台视图-主表 t_nocode_cardschema

- **表名称：** 工作台视图-主表
- **表名：** t_nocode_cardschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 视图名称 | varchar | 50 |  | √ | ' ' | 视图名称 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_cardschema |  | fid |
| 2 | idx_nc_cs_fname |  | fname |
