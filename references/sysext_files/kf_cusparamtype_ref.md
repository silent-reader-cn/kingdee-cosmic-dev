# 自定义参数引用-kf_cusparamtype_ref

## 自定义参数引用-主表 t_kf_cusparamtype_ref

- **表名称：** 自定义参数引用-主表
- **表名：** t_kf_cusparamtype_ref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcptnumber | 参数编码 | varchar | 50 |  | √ | ' ' | 参数编码 |
| 3 | finsnumber | 实例编码 | varchar | 50 |  | √ | ' ' | 实例编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kf_cpt_ref_cptnumber |  | fcptnumber |
| 2 | idx_kf_cpt_ref_insnumber |  | finsnumber |
| 3 | pk_t_kf_cusparamtype_ref |  | fid |
