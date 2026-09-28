# 表单双向关联关系-bos_nocode_association

## 表单双向关联关系-主表 t_nocode_association

- **表名称：** 表单双向关联关系-主表
- **表名：** t_nocode_association

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffirst_formid | 第一个单据id | varchar | 50 |  | √ | ' ' | 第一个单据id |
| 3 | fsecond_formid | 第二个单据id | varchar | 50 |  | √ | ' ' | 第二个单据id |
| 4 | ffirst_form_ref_fieldkey | 第一个单据引用的字段 | varchar | 50 |  | √ | ' ' | 第一个单据引用的字段 |
| 5 | fsecond_form_ref_fieldkey | 第二个单据引用的字段 | varchar | 50 |  | √ | ' ' | 第二个单据引用的字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_nocode_association |  | fid |
| 2 | idx_nc_first_formid_refkey |  | ffirst_form_ref_fieldkey |
| 3 | idx_nc_second_formid |  | fsecond_formid |
| 4 | idx_nc_second_formid_refkey |  | fsecond_form_ref_fieldkey |
| 5 | idx_nc_first_formid |  | ffirst_formid |
