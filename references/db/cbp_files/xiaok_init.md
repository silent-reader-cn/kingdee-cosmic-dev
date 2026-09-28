# 智能初始化-xiaok_init

## 智能初始化-主表 t_daxk_xiaok_init

- **表名称：** 智能初始化-主表
- **表名：** t_daxk_xiaok_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclients | 使用渠道 | varchar | 255 |  |  | ' ' | 使用渠道 |
| 3 | fappsecret | 密钥 | varchar | 255 |  |  | null | 密钥 |
| 4 | fcreatetime | fcreatetime | varchar | 255 |  |  | ' ' |  |
| 5 | fthirdpwd_enp | fthirdpwd_enp | text | 0 |  |  | null |  |
| 6 | ftenantid | tenantid | varchar | 30 |  | √ | ' ' | tenantid |
| 7 | fthirdpwd | 系统密码 | varchar | 255 |  |  | null | 系统密码 |
| 8 | faappid | appId | varchar | 255 |  |  | null | appId |
| 9 | frobotname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 10 | fformatedcreatetime | 初始化时间 | timestamp | 0 |  |  | null | 初始化时间 |
| 11 | fserverurl | 服务器地址 | varchar | 255 |  |  | null | 服务器地址 |
| 12 | fappsecret_enp | fappsecret_enp | text | 0 |  |  | null |  |
| 13 | frobotstatus | 状态 | varchar | 255 |  |  | ' ' | 状态 |
| 14 | fthirdpwdsecret | 加密后的系统密码 | varchar | 255 |  |  | null | 加密后的系统密码 |
| 15 | fthirdappid | 系统编码 | varchar | 255 |  |  | null | 系统编码 |
| 16 | frobotid | robotId | int8 | 64 |  | √ | 0 | robotId |
| 17 | faccountid | accountId | varchar | 30 |  | √ | ' ' | accountId |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_daxk_xiaok_init |  | fid |
| 2 | idx_cbp_accountid |  | faccountid |
