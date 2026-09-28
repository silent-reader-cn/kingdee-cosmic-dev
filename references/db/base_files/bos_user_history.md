# 人员历史-bos_user_history

## 人员历史-主表 t_sec_user_h

- **表名称：** 人员历史-主表
- **表名：** t_sec_user_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fidcard | 证件号码 | varchar | 20 |  | √ | ' ' | 证件号码 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fns_abbr | 缩写 | varchar | 50 |  | √ | ' ' | 缩写 |
| 6 | fns_country | 国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 7 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | fns_middlename | 中间名 | varchar | 50 |  | √ | ' ' | 中间名 |
| 9 | fthirduserid | 第三方用户内码 | varchar | 100 |  | √ | ' ' | 第三方用户内码 |
| 10 | fdptid | fdptid | int8 | 64 |  | √ | 0 |  |
| 11 | fuid | 云之家账号内码 | int8 | 64 |  | √ | 0 | 云之家账号内码 |
| 12 | fusertype | 类型（过时） | varchar | 100 |  | √ | ' ' | 类型（过时）,枚举: |
| 13 | fidtype | 证件类型 | int8 | 64 |  | √ | 0 | [个人证件号码格式 cts_personal_identity](../cts_files/cts_personal_identity.md) |
| 14 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 15 | fphone | 手机号码 | varchar | 36 |  | √ | ' ' | 手机号码 |
| 16 | fns_nickname | Nick Name | varchar | 50 |  | √ | ' ' | Nick Name |
| 17 | fisshruser | 是否存在s-HR同步映射关系 | varchar | 50 |  | √ | ' ' | 是否存在s-HR同步映射关系,枚举: 0 :否 1 :是 |
| 18 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 19 | fns_firstname | 名 | varchar | 255 |  | √ | ' ' | 名 |
| 20 | fxksource | 数据来源 | int8 | 64 |  |  | null | [数据来源 xkbos_data_sources](../xkbase_files/xkbos_data_sources.md) |
| 21 | fns_posttitle | 职称 | varchar | 50 |  | √ | ' ' | 职称,枚举: |
| 22 | fsortcode | fsortcode | varchar | 10 |  |  | null |  |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fnickname | fnickname | varchar | 300 |  | √ | ' ' |  |
| 25 | fns_customfield3 | Suffix | varchar | 50 |  | √ | ' ' | Suffix |
| 26 | fns_customfield4 | 自定义字段4 | varchar | 50 |  | √ | ' ' | 自定义字段4 |
| 27 | fsimplepinyin | 姓名简拼 | varchar | 50 |  | √ | ' ' | 姓名简拼 |
| 28 | fns_customfield1 | Second Name | varchar | 50 |  | √ | ' ' | Second Name |
| 29 | fns_customfield2 | Initials | varchar | 50 |  | √ | ' ' | Initials |
| 30 | fopenid | 用户云之家OpenID | varchar | 50 |  | √ | ' ' | 用户云之家OpenID |
| 31 | feid | 工作圈eid | int8 | 64 |  | √ | 0 | 工作圈eid |
| 32 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 33 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 工号 | varchar | 36 |  | √ | ' ' | 工号 |
| 35 | ffullpinyin | 姓名全拼 | varchar | 100 |  | √ | ' ' | 姓名全拼 |
| 36 | ftruename | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 37 | fns_lastname | 姓 | varchar | 50 |  | √ | ' ' | 姓 |
| 38 | fsource | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源,枚举: HR :HR |
| 39 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 40 | favatar | 人员头像 | varchar | 300 |  | √ | ' ' | 人员头像 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 43 | ftid | 团队ID | int8 | 64 |  | √ | 0 | 团队ID |
| 44 | fbillssatusfield | fbillssatusfield | varchar | 50 |  |  | null |  |
| 45 | fns_namestyle | 姓名格式 | int8 | 64 |  | √ | 0 | 姓名文本格式 cts_nameconfigformat |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | fgender | 性别 | varchar | 15 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 :保密 |
| 50 | fns_title | Title | varchar | 50 |  | √ | ' ' | Title,枚举: |
| 51 | fheadsculpture | 人员头像 | varchar | 300 |  | √ | ' ' | 人员头像 |
| 52 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 53 | fuserid | 人员内码 | int8 | 64 |  | √ | 0 | 人员内码 |
| 54 | fsortnumber | 排序码 | int8 | 64 |  | √ | 1000000 | 排序码 |
| 55 | fhiredate | fhiredate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_user_h_pkey |  | fid |
| 2 | idx_sec_user_h_time |  | fcreatetime |
| 3 | idx_sec_user_h_uidnumphonemail |  | fuserid,fnumber,fphone,femail |
| 4 | idx_t_sec_user_h_fuid |  | fuid |

---

## 部门分录-子表 t_sec_userposition_h

- **表名称：** 部门分录-子表
- **表名：** t_sec_userposition_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 3 | forgstructureid | 组织结构 | int8 | 64 |  | √ | 0 | [行政组织结构 bos_adminorg_structure](../base_files/bos_adminorg_structure.md) |
| 4 | fispartjob | 兼职 | bpchar | 1 |  | √ | '0' | 兼职 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpostid | fpostid | varchar | 36 |  | √ | ' ' |  |
| 7 | fsource | fsource | varchar | 10 |  |  | null |  |
| 8 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 9 | fsuperiorid | 直接上级 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisincharge | 负责人 | bpchar | 1 |  | √ | '0' | 负责人 |
| 11 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 12 | fdptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fenable | fenable | bpchar | 1 |  | √ | ' ' |  |
| 14 | fposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 15 | fpositionid | 岗位 | int8 | 64 |  | √ | 0 | [岗位 bos_position](../base_files/bos_position.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_userposition_h_pkey |  | fentryid |
| 2 | idx_t_sec_userposition_h |  | fid |

---

## 类型-多选基础资料表 t_sec_usertypes_h

- **表名称：** 类型-多选基础资料表
- **表名：** t_sec_usertypes_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员类型 bos_usertype](../base_files/bos_usertype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_usertypes_h |  | fpkid |
| 2 | idx_t_sec_usertypes_h_fid |  | fid |

---

## 人员历史-多语言表 t_sec_user_h_l

- **表名称：** 人员历史-多语言表
- **表名：** t_sec_user_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftruename | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
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
| 1 | idx_t_sec_user_h_l_fid |  | fid,flocaleid |
| 2 | t_sec_user_h_l_pkey |  | fpkid |

---

## 人员历史-使用范围表 t_sec_user_h_u

- **表名称：** 人员历史-使用范围表
- **表名：** t_sec_user_h_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrcount | 密码错误次数 | int8 | 64 |  | √ | 0 | 密码错误次数 |
| 3 | fuserdisablerid | 用户禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexternaluuid | 外部ID | varchar | 255 |  | √ | ' ' | 外部ID |
| 5 | fpsweffectivedate | 密码生效日期 | timestamp | 0 |  |  | null | 密码生效日期 |
| 6 | fuserdisabletime | 用户禁用时间 | timestamp | 0 |  |  | null | 用户禁用时间 |
| 7 | fuserid | fuserid | int8 | 64 |  | √ | 0 |  |
| 8 | fpassword | 密码 | varchar | 255 |  | √ | ' ' | 密码 |
| 9 | fusername | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 10 | flastloginip | 上次登录ip | varchar | 128 |  | √ | ' ' | 上次登录ip |
| 11 | fisactived | 激活状态 | bpchar | 1 |  | √ | '0' | 激活状态 |
| 12 | ftype | 用户类型 | varchar | 10 |  | √ | ' ' | 用户类型,枚举: |
| 13 | flastlogintime | 上次登录时间 | timestamp | 0 |  |  | null | 上次登录时间 |
| 14 | fauthorstatus | 授权状态 | varchar | 10 |  |  | null | 授权状态,枚举: |
| 15 | fuseenddate | 使用系统结束日期 | timestamp | 0 |  |  | null | 使用系统结束日期 |
| 16 | fislocked | 是否锁定 | bpchar | 1 |  | √ | ' ' | 是否锁定 |
| 17 | fisforbidden | 用户禁用 | bpchar | 1 |  | √ | ' ' | 用户禁用 |
| 18 | fpswhisstr | 历史密码 | varchar | 2000 |  | √ | ' ' | 历史密码 |
| 19 | flockedtime | 锁定日期 | timestamp | 0 |  |  | null | 锁定日期 |
| 20 | fisregisted | 注册状态 | bpchar | 1 |  | √ | '0' | 注册状态 |
| 21 | fpswstrategyid | 密码策略 | int8 | 64 |  | √ | 0 | [密码策略 perm_pswstrategy](../base_files/perm_pswstrategy.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sec_user_h_u_psw |  | fpassword |
| 2 | t_sec_user_h_u_pkey |  | fid |

---

## 联系方式分录-子表 t_sec_usercontact_h

- **表名称：** 联系方式分录-子表
- **表名：** t_sec_usercontact_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontact | 联系方式 | varchar | 1024 |  | √ | ' ' | 联系方式 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcontacttypeid | 类型 | int8 | 64 |  | √ | 0 | [人员联系方式类型 bos_user_contacttype](../base_files/bos_user_contacttype.md) |
| 6 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_usercontact_h_pkey |  | fentryid |
| 2 | idx_t_sec_usercontact_type_h |  | fcontacttypeid |
| 3 | idx_t_sec_usercontact_h |  | fid |

---

## 部门分录-多语言表 t_sec_userposition_h_l

- **表名称：** 部门分录-多语言表
- **表名：** t_sec_userposition_h_l

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
| 1 | t_sec_userposition_h_l_pkey |  | fpkid |
