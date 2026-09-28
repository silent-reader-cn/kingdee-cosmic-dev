# 引用关系-gai_refrence_relation

## 引用关系-主表 t_gai_refrence_relation

- **表名称：** 引用关系-主表
- **表名：** t_gai_refrence_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frefrenceformid | 引用表单编码 | varchar | 50 |  | √ | ' ' | 引用表单编码 |
| 3 | fdataid | 数据ID | int8 | 64 |  | √ | 0 | 数据ID |
| 4 | frefrenceid | 引用者ID | int8 | 64 |  | √ | 0 | 引用者ID |
| 5 | fformid | 数据表单编码 | varchar | 50 |  | √ | ' ' | 数据表单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_ref_relation_form |  | fdataid,fformid |
| 2 | pk_t_gai_refrence_relation |  | fid |
| 3 | idx_gai_ref_relation_ref |  | frefrenceformid,frefrenceid |
