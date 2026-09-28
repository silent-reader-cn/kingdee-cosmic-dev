# 租户认证配置-tenant_auth_config

## 租户认证配置-主表 t_bas_tenant_auth_config

- **表名称：** 租户认证配置-主表
- **表名：** t_bas_tenant_auth_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | App Secret | varchar | 256 |  | √ | ' ' | App Secret |
| 3 | fthirduser | 代理用户名 | varchar | 50 |  | √ | ' ' | 代理用户名 |
| 4 | fdistributnum | 分发数 | int4 | 32 |  | √ | 0 | 分发数 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fuserflag | 用户唯一标识 | bpchar | 1 |  | √ | '1' | 用户唯一标识,枚举: 0 :用户名 1 :手机号 2 :邮箱 3 :工号 |
| 7 | furl | 访问地址 | varchar | 255 |  | √ | ' ' | 访问地址 |
| 8 | ftenantid | 租户 | int8 | 64 |  | √ | 0 | [租户配置 ctsy_tenant](../ctsy_files/ctsy_tenant.md) |
| 9 | fsystemname | 系统名称 | varchar | 255 |  | √ | ' ' | 系统名称 |
| 10 | faccountid | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 11 | fappid | App ID | varchar | 50 |  | √ | ' ' | App ID |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_tenant_auth_config |  | fid |
| 2 | idx_tenant_auth_config_appid |  | fappid |
