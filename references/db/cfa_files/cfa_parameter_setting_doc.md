# 参数设置单据-cfa_parameter_setting_doc

## 参数设置单据-主表 t_cfa_parameter_setting

- **表名称：** 参数设置单据-主表
- **表名：** t_cfa_parameter_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fparamvalue | value | varchar | 255 |  | √ | ' ' | value |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fparamvalue_tag | value_详情 | text | 0 |  |  | null | value_详情 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_parameter_setting |  | fid |
| 2 | index_cfa_parameter_setting |  | fparamvalue |
