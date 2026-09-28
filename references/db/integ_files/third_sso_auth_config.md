# 单点登录-third_sso_auth_config

## 单点登录-主表 t_bas_third_sso_config

- **表名称：** 单点登录-主表
- **表名：** t_bas_third_sso_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | App Secret | varchar | 256 |  | √ | ' ' | App Secret |
| 3 | fthirduser | 代理用户名 | varchar | 50 |  | √ | ' ' | 代理用户名 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fxkmethod | 验证接口地址 | varchar | 200 |  | √ | ' ' | 验证接口地址 |
| 6 | fsource | 来源 | bpchar | 1 |  | √ | '1' | 来源,枚举: 0 :集团分发 1 :手动创建 |
| 7 | fintegmode | 集成方式 | bpchar | 1 |  | √ | '0' | 集成方式,枚举: 0 :标准集成 1 :自定义集成 2 :星空企业版集成 3 :生态产品集成(非苍穹架构) |
| 8 | fappid | App ID | varchar | 50 |  | √ | ' ' | App ID |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fauth_protocol | 认证协议 | bpchar | 1 |  | √ | '0' | 认证协议,枚举: 0 :OAuth 2.0 |
| 11 | fuserflag | 用户唯一标识 | bpchar | 1 |  | √ | '1' | 用户唯一标识,枚举: 0 :用户名 1 :手机号 2 :邮箱 3 :工号 |
| 12 | furl | 域名地址 | varchar | 255 |  | √ | ' ' | 域名地址 |
| 13 | fenable | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :可用 |
| 14 | fxkuserlinktype | 用户映射类型 | varchar | 50 |  | √ | ' ' | 用户映射类型,枚举: 1 :星空企业版用户映射 2 :用户名映射 |
| 15 | fsystemname | 系统名称 | varchar | 255 |  | √ | ' ' | 系统名称 |
| 16 | faccountid | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 17 | fdefaultloginpage | 默认登录页 | bpchar | 1 |  | √ | '0' | 默认登录页,枚举: 1 :是 0 :否 |
| 18 | fssoplugin | 单点登录插件 | varchar | 1024 |  | √ | ' ' | 单点登录插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_third_sso_config |  | fappid |
| 2 | pk_t_bas_third_sso_config |  | fid |
