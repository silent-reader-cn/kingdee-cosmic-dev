# token配置-fpy_eafc_collect_app

## token配置-主表 t_fpy_eafc_collect_app

- **表名称：** token配置-主表
- **表名：** t_fpy_eafc_collect_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_tenantid | 租户编码 | varchar | 50 |  | √ | ' ' | 租户编码 |
| 3 | fk_fpy_user | 用户 | varchar | 50 |  | √ | ' ' | 用户 |
| 4 | fk_fpy_modifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fk_fpy_modifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fk_fpy_createrf | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fk_fpy_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fk_fpy_status | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 9 | fk_fpy_baseurl | baseurl | varchar | 100 |  | √ | ' ' | baseurl |
| 10 | fk_fpy_usertype | 用户类型 | varchar | 10 |  | √ | ' ' | 用户类型,枚举: UserName :UserName Mobile :Mobile |
| 11 | fk_fpy_appid | appid | varchar | 50 |  | √ | ' ' | appid |
| 12 | fk_fpy_app_secret | app_secret | varchar | 100 |  | √ | ' ' | app_secret |
| 13 | fk_fpy_accountid | 数据中心 | varchar | 50 |  | √ | ' ' | 数据中心 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_eafc_collect_app |  | fid |
