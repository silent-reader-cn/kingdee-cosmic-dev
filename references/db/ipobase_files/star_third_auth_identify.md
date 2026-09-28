# 星空第三方授权身份-star_third_auth_identify

## 星空第三方授权身份-主表 t_star_third_identify

- **表名称：** 星空第三方授权身份-主表
- **表名：** t_star_third_identify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusername | 登录用户名 | varchar | 50 |  | √ | ' ' | 登录用户名 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fappsec | 应用密钥 | varchar | 50 |  | √ | ' ' | 应用密钥 |
| 5 | facctid | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 6 | flcid | 账套语系，默认2052 | int4 | 32 |  | √ | 2052 | 账套语系，默认2052 |
| 7 | fipoorgid | IPO编制组织 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 8 | fserverurl | 请求地址 | varchar | 50 |  | √ | ' ' | 请求地址 |
| 9 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_star_third_identify |  | fid |
| 2 | idx_star_third_identify_uq |  | fipoorgid |
