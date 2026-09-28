# 授权信息-dm_auth

## 授权信息-主表 t_dm_auth

- **表名称：** 授权信息-主表
- **表名：** t_dm_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 4 | fmodifier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftenantid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 6 | ferpid | 云端ID（弃用） | varchar | 50 |  | √ | ' ' | 云端ID（弃用） |
| 7 | fmodifytime | 最后申请时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 最后申请时间 |
| 8 | fpublickey | 公钥 | varchar | 1024 |  | √ | ' ' | 公钥 |
| 9 | flicensehash | 许可哈希值 | varchar | 255 |  | √ | ' ' | 许可哈希值 |
| 10 | ferpsecret | 云端秘钥（弃用） | varchar | 256 |  | √ | ' ' | 云端秘钥（弃用） |
| 11 | ftenantname | 租户名称 | varchar | 50 |  | √ | ' ' | 租户名称 |
| 12 | fauthsecret | 授权秘钥 | varchar | 256 |  | √ | ' ' | 授权秘钥 |
| 13 | faccountid | 账套ID | varchar | 50 |  | √ | ' ' | 账套ID |
| 14 | fauthkey | 授权key | varchar | 50 |  | √ | ' ' | 授权key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_auth_accountid |  | faccountid |
| 2 | pk_t_dm_auth |  | fid |
| 3 | idx_dm_auth_tenantid |  | ftenantid |
