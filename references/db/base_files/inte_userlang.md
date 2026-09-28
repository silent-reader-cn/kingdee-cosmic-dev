# 用户语言-inte_userlang

## 用户语言-主表 t_int_userlang

- **表名称：** 用户语言-主表
- **表名：** t_int_userlang

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | flangid | 语言 | int8 | 64 |  | √ | 0 | 语言种类 inte_language |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_int_userlang_pkey |  | fid |
| 2 | idx_t_int_userlang_user |  | fuserid |
