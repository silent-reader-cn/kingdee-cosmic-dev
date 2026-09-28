# 轻应用集成用户映射-bas_immapping

## 轻应用集成用户映射-主表 t_bas_immapping

- **表名称：** 轻应用集成用户映射-主表
- **表名：** t_bas_immapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 3 | fencryopenid | 移动平台用户加密ID | varchar | 255 |  | √ | ' ' | 移动平台用户加密ID |
| 4 | fopenid | 移动平台用户ID | varchar | 80 |  | √ | ' ' | 移动平台用户ID |
| 5 | fthirdappusername | 移动平台用户名 | varchar | 50 |  | √ | ' ' | 移动平台用户名 |
| 6 | fthird_user_phone_num | 移动平台用户手机号 | varchar | 20 |  | √ | ' ' | 移动平台用户手机号 |
| 7 | fimtypeid | 移动平台类型 | int8 | 64 |  | √ | 0 | 移动平台类型 bas_instantmsgtype |
| 8 | frefuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fuserid | 金蝶云用户 | int8 | 64 |  | √ | 0 | 金蝶云用户 |
| 10 | fthirdappcorpid | 企业团队ID | varchar | 50 |  | √ | ' ' | 企业团队ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_immapping_pkey |  | fid |
| 2 | idx_user_type |  | frefuserid,fimtypeid |
| 3 | idx_bas_immap_typeuseropen |  | fimtypeid,fuserid,fopenid |
