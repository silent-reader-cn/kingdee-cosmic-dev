# 注册用户审批-srm_user

## 注册用户审批-多语言表 t_pur_user_l

- **表名称：** 注册用户审批-多语言表
- **表名：** t_pur_user_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名(管理员) | varchar | 255 |  | √ | ' ' | 姓名(管理员) |
| 3 | fenterprise | 企业名称 | varchar | 255 |  | √ | ' ' | 企业名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_user_l_fid |  | fid,flocaleid |
| 2 | idx_pur_user_enterprise |  | flocaleid,fenterprise |
| 3 | t_pur_user_l_pkey |  | fpkid |

---

## 注册用户审批-主表 t_pur_user

- **表名称：** 注册用户审批-主表
- **表名：** t_pur_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fphone | fphone | varchar | 20 |  | √ | ' ' |  |
| 5 | fname | 姓名(管理员) | varchar | 255 |  | √ | ' ' | 姓名(管理员) |
| 6 | fenterprise | 企业名称 | varchar | 255 |  | √ | ' ' | 企业名称 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 9 | fidcard | fidcard | varchar | 20 |  | √ | ' ' |  |
| 10 | fcreditno | 信用代码 | varchar | 60 |  | √ | ' ' | 信用代码 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fpassword | 登录密码 | varchar | 50 |  | √ | ' ' | 登录密码 |
| 13 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 14 | fsupplierid | 正式供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 审核状态 | bpchar | 1 |  | √ | ' ' | 审核状态,枚举: A :保存 B :已提交 C :已审核 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsupplierregid | 注册资料单id | varchar | 50 |  | √ | ' ' | 注册资料单id |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 账号(手机号/邮箱) | varchar | 50 |  | √ | ' ' | 账号(手机号/邮箱) |
| 22 | fusertype | 用户类型 | varchar | 2 |  | √ | '1' | 用户类型,枚举: 1 :供应商用户 2 :专家用户 |
| 23 | fdeptduty | 部门及职务 | varchar | 50 |  | √ | ' ' | 部门及职务 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_user_fnumber |  | fnumber |
| 2 | t_pur_user_pkey |  | fid |
