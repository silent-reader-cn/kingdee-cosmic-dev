# 关注用户信息-ipop_concernuserinfo

## 关注用户信息-主表 t_ipop_concernuserinfo

- **表名称：** 关注用户信息-主表
- **表名：** t_ipop_concernuserinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fconcerntype | 关注原因类型 | varchar | 100 |  | √ | ' ' | 关注原因类型,枚举: lowRate :登录频率低 forbidden :用户已禁用，但员工仍然有效 otherPlaceLogin :异地多次登录 |
| 5 | floginday | 登录天数 | int4 | 32 |  | √ | 0 | 登录天数 |
| 6 | flatestlogintime | 最近登录时间 | timestamp | 0 |  |  | null | 最近登录时间 |
| 7 | frecordtime | 记录时间 | timestamp | 0 |  |  | null | 记录时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_concernuserinfo |  | frecordtime |
| 2 | pk_t_ipop_concernuserinfo |  | fid |
| 3 | idx_ipop_concernuserinfo_type |  | fconcerntype |
