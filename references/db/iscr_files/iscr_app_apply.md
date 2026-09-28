# 云资源应用申请-iscr_app_apply

## 云资源应用申请-主表 t_iscr_app_apply

- **表名称：** 云资源应用申请-主表
- **表名：** t_iscr_app_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 4 | fpublickey_enp | fpublickey_enp | text | 0 |  |  | null |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fserver_accountid | 云端账套ID | varchar | 100 |  | √ | ' ' | 云端账套ID |
| 7 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 8 | faccountname | 当前账套名称 | varchar | 50 |  | √ | ' ' | 当前账套名称 |
| 9 | fmodifier | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ftenantid | 当前租户ID | varchar | 50 |  | √ | ' ' | 当前租户ID |
| 11 | fmodifytime | 最后申请时间 | timestamp | 0 |  |  | null | 最后申请时间 |
| 12 | ffileserver | 云端文件服务器地址 | varchar | 255 |  | √ | ' ' | 云端文件服务器地址 |
| 13 | fpublickey | 摘要加密认证密钥 | varchar | 255 |  | √ | ' ' | 摘要加密认证密钥 |
| 14 | fstatus | 申请状态 | varchar | 50 |  | √ | ' ' | 申请状态,枚举: A :暂存 B :申请成功 C :已审核 |
| 15 | fapp_name | 开放应用名称 | varchar | 50 |  | √ | ' ' | 开放应用名称 |
| 16 | ftenantname | 当前租户名称 | varchar | 50 |  | √ | ' ' | 当前租户名称 |
| 17 | fserver_url | 云端地址 | varchar | 255 |  | √ | ' ' | 云端地址 |
| 18 | fapp_number | 开放应用编码 | varchar | 50 |  | √ | ' ' | 开放应用编码 |
| 19 | faccountid | 当前账套ID | varchar | 50 |  | √ | ' ' | 当前账套ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscr_app_apply |  | fid |
| 2 | idx_t_iscr_app_apply |  | fapp_number |
