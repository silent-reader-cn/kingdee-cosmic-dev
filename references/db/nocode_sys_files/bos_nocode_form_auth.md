# 表单授权-bos_nocode_form_auth

## 表单授权-主表 t_nocode_form_auth

- **表名称：** 表单授权-主表
- **表名：** t_nocode_form_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 是否获取权限 | varchar | 50 |  | √ | ' ' | 是否获取权限,枚举: 1 :审核中 2 :否 3 :是 4 :已弃权 5 :已撤销 |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fapplyreason | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 5 | fappname | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 6 | fapplyappid | 申请应用id | varchar | 50 |  | √ | ' ' | 申请应用id |
| 7 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | faudittext | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 9 | fapplyappname | 申请应用 | varchar | 50 |  | √ | ' ' | 申请应用 |
| 10 | fformid | 表单id | varchar | 50 |  | √ | ' ' | 表单id |
| 11 | fformname | 表单 | varchar | 50 |  | √ | ' ' | 表单 |
| 12 | fappid | 表单所属应用id | varchar | 50 |  | √ | ' ' | 表单所属应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_form_auth |  | fid |
| 2 | idx_nc_fa_formid |  | fformid |
