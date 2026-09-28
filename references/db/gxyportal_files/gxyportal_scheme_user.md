# 方案用户-gxyportal_scheme_user

## 方案用户-使用范围表 t_sec_user_u

- **表名称：** 方案用户-使用范围表
- **表名：** t_sec_user_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrcount | ferrcount | int8 | 64 |  | √ | 0 |  |
| 3 | fuserdisablerid | fuserdisablerid | int8 | 64 |  | √ | 0 |  |
| 4 | fexternaluuid | fexternaluuid | varchar | 255 |  | √ | ' ' |  |
| 5 | fpsweffectivedate | fpsweffectivedate | timestamp | 0 |  |  | null |  |
| 6 | fuserdisabletime | fuserdisabletime | timestamp | 0 |  |  | null |  |
| 7 | fpassword | fpassword | varchar | 255 |  | √ | ' ' |  |
| 8 | fusername | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 9 | flastloginip | flastloginip | varchar | 128 |  | √ | ' ' |  |
| 10 | fisactived | fisactived | bpchar | 1 |  | √ | '0' |  |
| 11 | ftype | ftype | varchar | 10 |  |  | null |  |
| 12 | flastlogintime | flastlogintime | timestamp | 0 |  |  | null |  |
| 13 | fauthorstatus | fauthorstatus | varchar | 10 |  |  | null |  |
| 14 | fuseenddate | fuseenddate | timestamp | 0 |  |  | null |  |
| 15 | fislocked | fislocked | bpchar | 1 |  | √ | '0' |  |
| 16 | fisforbidden | fisforbidden | bpchar | 1 |  | √ | '0' |  |
| 17 | fpswhisstr | fpswhisstr | varchar | 2000 |  | √ | ' ' |  |
| 18 | flockedtime | flockedtime | timestamp | 0 |  |  | null |  |
| 19 | fisregisted | fisregisted | bpchar | 1 |  | √ | '0' |  |
| 20 | fpswstrategyid | fpswstrategyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sec_user_u_psw |  | fpassword |
| 2 | idx_t_sec_user_u_usedate |  | fisforbidden,fuseenddate |
| 3 | ux_t_sec_user_u_username |  | fusername |
| 4 | t_sec_user_u_pkey |  | fid |

---

## 方案用户-多语言表 t_sec_user_l

- **表名称：** 方案用户-多语言表
- **表名：** t_sec_user_l

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
| 1 | t_sec_user_l_pkey |  | fpkid |
| 2 | idx_sec_user_l_truename |  | ftruename,fid |
| 3 | idx_t_sec_user_l_fid |  | fid,flocaleid |

---

## 方案用户-主表 t_sec_user

- **表名称：** 方案用户-主表
- **表名：** t_sec_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fidcard | fidcard | varchar | 20 |  |  | null |  |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 5 | fns_abbr | fns_abbr | varchar | 50 |  | √ | ' ' |  |
| 6 | fns_country | fns_country | int8 | 64 |  | √ | 0 |  |
| 7 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 8 | fns_middlename | fns_middlename | varchar | 50 |  | √ | ' ' |  |
| 9 | fthirduserid | fthirduserid | varchar | 100 |  | √ | ' ' |  |
| 10 | fdptid | fdptid | int8 | 64 |  |  | null |  |
| 11 | fuid | fuid | int8 | 64 |  | √ | 0 |  |
| 12 | fpositionid | fpositionid | int8 | 64 |  | √ | 0 |  |
| 13 | fusertype | 类型 | varchar | 100 |  | √ | ' ' | 类型,枚举: 1 :职员 3 :客户 4 :供应商 |
| 14 | fidtype | fidtype | int8 | 64 |  | √ | 0 |  |
| 15 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 16 | fphone | 手机 | varchar | 100 |  | √ | ' ' | 手机 |
| 17 | fns_nickname | fns_nickname | varchar | 50 |  | √ | ' ' |  |
| 18 | fisshruser | fisshruser | bpchar | 1 |  | √ | '0' |  |
| 19 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 20 | fns_firstname | fns_firstname | varchar | 255 |  | √ | ' ' |  |
| 21 | fxksource | fxksource | int8 | 64 |  | √ | 0 |  |
| 22 | fns_posttitle | fns_posttitle | varchar | 50 |  | √ | ' ' |  |
| 23 | fsortcode | fsortcode | varchar | 10 |  |  | null |  |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 25 | fnickname | fnickname | varchar | 300 |  |  | null |  |
| 26 | fns_customfield3 | fns_customfield3 | varchar | 50 |  | √ | ' ' |  |
| 27 | fns_customfield4 | fns_customfield4 | varchar | 50 |  | √ | ' ' |  |
| 28 | fsimplepinyin | fsimplepinyin | varchar | 50 |  | √ | ' ' |  |
| 29 | fns_customfield1 | fns_customfield1 | varchar | 50 |  | √ | ' ' |  |
| 30 | fns_customfield2 | fns_customfield2 | varchar | 50 |  | √ | ' ' |  |
| 31 | fopenid | fopenid | varchar | 50 |  | √ | ' ' |  |
| 32 | feid | feid | int8 | 64 |  | √ | 0 |  |
| 33 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 34 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 36 | ffullpinyin | 姓名全拼 | varchar | 100 |  | √ | ' ' | 姓名全拼 |
| 37 | flist_usergrp | flist_usergrp | varchar | 255 |  | √ | ' ' |  |
| 38 | ftruename | ftruename | varchar | 255 |  | √ | ' ' |  |
| 39 | fns_lastname | fns_lastname | varchar | 50 |  | √ | ' ' |  |
| 40 | fsource | fsource | varchar | 10 |  |  | null |  |
| 41 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 42 | favatar | 头像 | varchar | 300 |  | √ | ' ' | 头像 |
| 43 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 44 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 45 | ftid | ftid | int8 | 64 |  | √ | 0 |  |
| 46 | fbillssatusfield | fbillssatusfield | varchar | 50 |  |  | null |  |
| 47 | fns_namestyle | fns_namestyle | int8 | 64 |  | √ | 0 |  |
| 48 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 49 | fbirthday | fbirthday | timestamp | 0 |  |  | null |  |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | fgender | 性别 | varchar | 15 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 52 | fns_title | fns_title | varchar | 50 |  | √ | ' ' |  |
| 53 | fheadsculpture | fheadsculpture | varchar | 300 |  | √ | ' ' |  |
| 54 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 55 | flist_license | flist_license | varchar | 255 |  | √ | ' ' |  |
| 56 | fsortnumber | fsortnumber | int8 | 64 |  | √ | 1000000 |  |
| 57 | fhiredate | fhiredate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sec_user_phone |  | fphone |
| 2 | t_sec_user_pkey |  | fid |
| 3 | idx_t_sec_user_sortnumber |  | fsortnumber,fnumber |
| 4 | idx_t_sec_user_fuid |  | fuid |
| 5 | idx_t_sec_user_number |  | fnumber |
| 6 | idx_t_sec_user_email |  | femail |
| 7 | idx_t_sec_user_thirduserid |  | fthirduserid |
| 8 | idx_t_sec_user_usertype |  | fusertype |
