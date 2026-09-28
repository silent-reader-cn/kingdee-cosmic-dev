# 租户管理-task_satisfiedtenant

## 租户管理-主表 t_tk_satisfiedtenant

- **表名称：** 租户管理-主表
- **表名：** t_tk_satisfiedtenant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fpasswd | 用户密码 | varchar | 50 |  | √ | ' ' | 用户密码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 8 | fsecretkey | secret_key | varchar | 200 |  | √ | ' ' | secret_key |
| 9 | fmobile | 手机 | varchar | 50 |  | √ | ' ' | 手机 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | faeskey | aes_key | varchar | 200 |  | √ | ' ' | aes_key |
| 12 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fsuperadmin | 超级管理员账号 | varchar | 50 |  | √ | ' ' | 超级管理员账号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fthirdorgid | 第三方系统租户id | varchar | 200 |  | √ | ' ' | 第三方系统租户id |
| 17 | finstanceid | 租户id | varchar | 200 |  | √ | ' ' | 租户id |
| 18 | fexpiredate | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | furl | 管理地址 | varchar | 250 |  | √ | ' ' | 管理地址 |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fuserstatus | 账户状态 | varchar | 4 |  | √ | ' ' | 账户状态,枚举: 0 :启用中 1 :停用中 2 :已过期 |
| 23 | fexpiredatatime | 过期时间Str | varchar | 50 |  | √ | ' ' | 过期时间Str |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_satisfied_tenantid |  | finstanceid |
| 2 | pk_t_tk_satisfiedtenant |  | fid |

---

## 租户管理-多语言表 t_tk_satisfiedtenant_l

- **表名称：** 租户管理-多语言表
- **表名：** t_tk_satisfiedtenant_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_satisfiedtenant_l_id |  | fid,flocaleid |
| 2 | pk_t_tk_satisfiedtenant_l |  | fpkid |
