# 同步财务云应收发票回调地址-invsm_callback_addr

## 同步财务云应收发票回调地址-主表 t_invsm_callback_addr

- **表名称：** 同步财务云应收发票回调地址-主表
- **表名：** t_invsm_callback_addr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwriteoff | 冲回接口 | varchar | 150 |  | √ | ' ' | 冲回接口 |
| 3 | fclientid | clientId | varchar | 32 |  | √ | ' ' | clientId |
| 4 | fuser | 有苍穹相应权限的用户标识 | varchar | 32 |  | √ | ' ' | 有苍穹相应权限的用户标识 |
| 5 | flanguage | 语言 | varchar | 16 |  | √ | ' ' | 语言 |
| 6 | ftenantid | 租户ID | varchar | 32 |  | √ | ' ' | 租户ID |
| 7 | faccesstoken | getAccessToken地址 | varchar | 150 |  | √ | ' ' | getAccessToken地址 |
| 8 | fpassword | 用户密码 | varchar | 100 |  | √ | ' ' | 用户密码 |
| 9 | frevenuenumber | 税号 | varchar | 20 |  | √ | ' ' | 税号 |
| 10 | fappid | 第三方应用编码 | varchar | 32 |  | √ | ' ' | 第三方应用编码 |
| 11 | fappsecuret | 第三方应用密码 | varchar | 32 |  | √ | ' ' | 第三方应用密码 |
| 12 | fabandon | 废弃接口 | varchar | 150 |  | √ | ' ' | 废弃接口 |
| 13 | fissue | 开票回推接口 | varchar | 150 |  | √ | ' ' | 开票回推接口 |
| 14 | fapptoken | getAppToken地址 | varchar | 150 |  | √ | ' ' | getAppToken地址 |
| 15 | fusertype | 用户标识类型 | varchar | 50 |  | √ | ' ' | 用户标识类型,枚举: Mobile :Mobile Email :Email Username :Username |
| 16 | faccountid | 数据中心ID | varchar | 32 |  | √ | ' ' | 数据中心ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invsm_callback_addr |  | fid |
| 2 | idx_invsm_callback_addr |  | frevenuenumber |
