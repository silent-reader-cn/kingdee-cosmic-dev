# 报销级别设置-er_reimbursesetting

## 部门分录-子表 t_sec_userposition

- **表名称：** 部门分录-子表
- **表名：** t_sec_userposition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 3 | forgstructureid | 组织结构 | int8 | 64 |  | √ | 0 | 行政组织结构 bos_adminorg_structure |
| 4 | fispartjob | 兼职 | bpchar | 1 |  | √ | ' ' | 兼职 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpostid | fpostid | varchar | 36 |  |  | null |  |
| 7 | fsource | fsource | varchar | 10 |  |  | null |  |
| 8 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 9 | fsuperiorid | 直接上级 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fisincharge | 负责人 | bpchar | 1 |  | √ | ' ' | 负责人 |
| 11 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 12 | fdptid | 部门 | int8 | 64 |  | √ | null | 业务单元 bos_org |
| 13 | fenable | fenable | bpchar | 1 |  |  | null |  |
| 14 | fposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 15 | fpositionid | 岗位 | int8 | 64 |  | √ | 0 | 岗位 bos_position |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_userposition_pkey |  | fentryid |
| 2 | idx_t_sec_userposition_fid |  | fid |
| 3 | idx_t_sec_userposition |  | fdptid |

---

## 报销级别设置-分表 t_sec_user_e

- **表名称：** 报销级别设置-分表
- **表名：** t_sec_user_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauditstatus | 状态 | varchar | 30 |  | √ | 'A' | 状态,枚举: A :未审核 C :已审核 |
| 3 | fsubaccountname | fsubaccountname | varchar | 100 |  | √ | ' ' |  |
| 4 | freimburselevelid | 报销级别(废弃) | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_user_e_pkey |  | fid |
| 2 | idx_t_sec_user_e_level |  | freimburselevelid |

---

## 报销级别设置-使用范围表 t_sec_user_u

- **表名称：** 报销级别设置-使用范围表
- **表名：** t_sec_user_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrcount | 密码错误次数 | int8 | 64 |  | √ | 0 | 密码错误次数 |
| 3 | fuserdisablerid | 用户禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fexternaluuid | 外部ID | varchar | 255 |  | √ | ' ' | 外部ID |
| 5 | fpsweffectivedate | 密码生效日期 | timestamp | 0 |  |  | null | 密码生效日期 |
| 6 | fuserdisabletime | 用户禁用时间 | timestamp | 0 |  |  | null | 用户禁用时间 |
| 7 | fpassword | 密码 | varchar | 255 |  | √ | ' ' | 密码 |
| 8 | fusername | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 9 | flastloginip | flastloginip | varchar | 128 |  | √ | ' ' |  |
| 10 | fisactived | 激活状态 | bpchar | 1 |  | √ | '0' | 激活状态 |
| 11 | ftype | 用户类型 | varchar | 10 |  |  | null | 用户类型,枚举: |
| 12 | flastlogintime | flastlogintime | timestamp | 0 |  |  | null |  |
| 13 | fauthorstatus | 授权状态 | varchar | 10 |  |  | null | 授权状态,枚举: |
| 14 | fuseenddate | 使用系统结束时间 | timestamp | 0 |  |  | null | 使用系统结束时间 |
| 15 | fislocked | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 16 | fisforbidden | 用户禁用 | bpchar | 1 |  | √ | '0' | 用户禁用 |
| 17 | fpswhisstr | 历史密码 | varchar | 2000 |  | √ | ' ' | 历史密码 |
| 18 | flockedtime | 锁定时间 | timestamp | 0 |  |  | null | 锁定时间 |
| 19 | fisregisted | 注册状态 | bpchar | 1 |  | √ | '0' | 注册状态 |
| 20 | fpswstrategyid | 密码策略 | int8 | 64 |  | √ | 0 | 密码策略 perm_pswstrategy |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sec_user_u_psw |  | fpassword |
| 2 | ux_t_sec_user_u_username |  | fusername |
| 3 | t_sec_user_u_pkey |  | fid |

---

## 部门分录-多语言表 t_sec_userposition_l

- **表名称：** 部门分录-多语言表
- **表名：** t_sec_userposition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sec_userposition_l_entry |  | fentryid,flocaleid |
| 2 | t_sec_userposition_l_pkey |  | fpkid |

---

## 报销级别设置-多语言表 t_sec_user_l

- **表名称：** 报销级别设置-多语言表
- **表名：** t_sec_user_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftruename | 职员名称 | varchar | 255 |  | √ | ' ' | 职员名称 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_user_l_pkey |  | fpkid |
| 2 | idx_t_sec_user_l_fid |  | fid,flocaleid |

---

## 报销级别设置-主表 t_sec_user

- **表名称：** 报销级别设置-主表
- **表名：** t_sec_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftruename | 职员名称 | varchar | 255 |  | √ | ' ' | 职员名称 |
| 3 | fidcard | 身份证号 | varchar | 20 |  |  | null | 身份证号 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fsource | 数据来源 | varchar | 10 |  |  | null | 数据来源,枚举: HR :HR |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | favatar | 人员头像 | varchar | 300 |  | √ | ' ' | 人员头像 |
| 9 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fthirduserid | 第三方用户内码 | varchar | 100 |  | √ | ' ' | 第三方用户内码 |
| 13 | ftid | 团队ID | int8 | 64 |  | √ | 0 | 团队ID |
| 14 | fdptid | fdptid | int8 | 64 |  |  | null |  |
| 15 | fuid | 云之家账号内码 | int8 | 64 |  | √ | 0 | 云之家账号内码 |
| 16 | fpositionid | fpositionid | int8 | 64 |  | √ | 0 |  |
| 17 | fusertype | 类型（过时） | varchar | 100 |  | √ | ' ' | 类型（过时）,枚举: |
| 18 | fbillssatusfield | fbillssatusfield | varchar | 50 |  |  | null |  |
| 19 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 20 | fphone | 手机号码 | varchar | 36 |  | √ | ' ' | 手机号码 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fisshruser | 是否存在s-HR同步映射关系 | bpchar | 1 |  | √ | '0' | 是否存在s-HR同步映射关系,枚举: 0 :否 1 :是 |
| 25 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 26 | fgender | 性别 | varchar | 15 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 :保密 |
| 27 | fxksource | 数据来源 | int8 | 64 |  | √ | 0 | 数据来源 xkbos_data_sources |
| 28 | fsortcode | fsortcode | varchar | 10 |  |  | null |  |
| 29 | fheadsculpture | 人员头像 | varchar | 300 |  | √ | ' ' | 人员头像 |
| 30 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 31 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | 人员 bos_user |
| 32 | fnickname | fnickname | varchar | 300 |  |  | null |  |
| 33 | fsimplepinyin | 姓名简拼 | varchar | 50 |  | √ | ' ' | 姓名简拼 |
| 34 | fopenid | 用户云之家OpenID | varchar | 50 |  | √ | ' ' | 用户云之家OpenID |
| 35 | feid | 工作圈eid | int8 | 64 |  | √ | 0 | 工作圈eid |
| 36 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 职员编码 | varchar | 36 |  | √ | ' ' | 职员编码 |
| 39 | fhiredate | fhiredate | timestamp | 0 |  |  | null |  |
| 40 | ffullpinyin | 姓名全拼 | varchar | 100 |  | √ | ' ' | 姓名全拼 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sec_user_phone |  | fphone |
| 2 | t_sec_user_pkey |  | fid |
| 3 | idx_t_sec_user_fuid |  | fuid |
| 4 | idx_t_sec_user_number |  | fnumber |
| 5 | idx_t_sec_user_email |  | femail |
| 6 | idx_t_sec_user_thirduserid |  | fthirduserid |
| 7 | idx_t_sec_user_usertype |  | fusertype |

---

## 联系方式分录-子表 t_sec_usercontact

- **表名称：** 联系方式分录-子表
- **表名：** t_sec_usercontact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontact | 联系方式 | varchar | 1024 |  | √ | ' ' | 联系方式 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcontacttypeid | 类型 | int8 | 64 |  | √ | 0 | 人员联系方式类型 bos_user_contacttype |
| 6 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sec_usercontact_type |  | fcontacttypeid |
| 2 | idx_t_sec_usercontact |  | fid |
| 3 | t_sec_usercontact_pkey |  | fentryid |

---

## 类型-多选基础资料表 t_sec_usertypes

- **表名称：** 类型-多选基础资料表
- **表名：** t_sec_usertypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员类型 bos_usertype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_usertypes |  | fpkid |
| 2 | idx_t_sec_usertypes_fid |  | fid |
