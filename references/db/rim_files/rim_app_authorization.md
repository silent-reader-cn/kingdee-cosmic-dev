# 第三方应用授权-rim_app_authorization

## 第三方应用授权-主表 t_rim_app_authorization

- **表名称：** 第三方应用授权-主表
- **表名：** t_rim_app_authorization

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frim_user | 第三方用户 | int8 | 64 |  | √ | 0 | 第三方用户 |
| 3 | fstatus | 授权状态 | varchar | 4 |  | √ | ' ' | 授权状态,枚举: 1 :已授权 2 :未授权 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fapptype | 授权方 | varchar | 4 |  | √ | ' ' | 授权方,枚举: 1 :滴滴 2 :云票 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fphone_no | 手机号码 | varchar | 20 |  | √ | ' ' | 手机号码 |
| 9 | fappid | 接入方标识 | varchar | 50 |  | √ | ' ' | 接入方标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_app_authorization |  | fid |
| 2 | idx_rim_app_authorization |  | fuserid,frim_user |
| 3 | idx_rim_app_authorization2 |  | fphone_no |
