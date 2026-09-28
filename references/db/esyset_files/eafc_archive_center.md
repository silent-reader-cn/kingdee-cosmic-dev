# 档案中心-eafc_archive_center

## 档案中心-主表 tk_eafc_archive_center

- **表名称：** 档案中心-主表
- **表名：** tk_eafc_archive_center

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_contacts | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 3 | fk_eafc_contacts_phone | 联系人电话 | varchar | 50 |  | √ | ' ' | 联系人电话 |
| 4 | fk_eafc_auth_code | 授权码 | varchar | 50 |  | √ | ' ' | 授权码 |
| 5 | fk_eafc_archive_name | 档案名称 | varchar | 50 |  | √ | ' ' | 档案名称 |
| 6 | fk_eafc_createtime | 创建日期 | int4 | 32 |  |  | null | 创建日期 |
| 7 | fk_eafc_email | 联系人邮箱 | varchar | 50 |  | √ | ' ' | 联系人邮箱 |
| 8 | fk_eafc_archive_no | 档案中心编码 | varchar | 50 |  | √ | ' ' | 档案中心编码 |
| 9 | fk_eafc_status | 状态 | varchar | 50 |  | √ | ' ' | 状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_archive_center |  | fid |
