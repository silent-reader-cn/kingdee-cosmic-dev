# 资源连接配置-ipop_resotpconfig

## 资源连接配置-主表 t_ipop_resotpconfig

- **表名称：** 资源连接配置-主表
- **表名：** t_ipop_resotpconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclientid | 应用id | varchar | 50 |  | √ | ' ' | 应用id,枚举: 204950 :test 204759 :prod |
| 3 | fotpurl | OTP地址 | varchar | 50 |  | √ | ' ' | OTP地址,枚举: https://consoleuat.kingdee.com :test https://console.kingdee.com :prod |
| 4 | fpublic | 公有云 | varchar | 1 |  | √ | '0' | 公有云 |
| 5 | fcloudsz | 云通行证地址 | varchar | 50 |  | √ | ' ' | 云通行证地址,枚举: https://passporttest.kingdee.com :test https://passport.kingdee.com :prod |
| 6 | fdesigndeploy | 指定部署方式 | varchar | 1 |  | √ | '0' | 指定部署方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_resotpconfig_cloudsz |  | fcloudsz |
| 2 | pk_ipop_resotpconfig |  | fid |
