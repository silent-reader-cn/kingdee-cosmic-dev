# 用户位图下标-lic_userbitmapindex

## 用户位图下标-主表 t_lic_userbitmapindex

- **表名称：** 用户位图下标-主表
- **表名：** t_lic_userbitmapindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 3 | fusername | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 4 | fbitmapindex | 位图下标 | int8 | 64 |  | √ | 0 | 位图下标 |
| 5 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 6 | fciphertext | 密文 | varchar | 255 |  | √ | ' ' | 密文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fphone,femail,fusername,fbitmapindex |
| 2 | fphone | fid,fphone,femail,fusername,fbitmapindex |
| 3 | femail | fid,fphone,femail,fusername,fbitmapindex |
| 4 | fusername | fid,fphone,femail,fusername,fbitmapindex |
| 5 | fbitmapindex | fid,fphone,femail,fusername,fbitmapindex |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_userbitmapindex_bitmap |  | fbitmapindex |
| 2 | pk_t_lic_userbitmapindex |  | fid,fphone,femail,fusername,fbitmapindex |
