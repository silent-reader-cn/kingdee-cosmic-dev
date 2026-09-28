# 方案用户-portal_scheme_user

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
| 8 | fusername | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
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
| 2 | ux_t_sec_user_u_username |  | fusername |
| 3 | t_sec_user_u_pkey |  | fid |

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
| 2 | idx_t_sec_user_l_fid |  | fid,flocaleid |

---

## 方案用户-主表 t_sec_user

- **表名称：** 方案用户-主表
- **表名：** t_sec_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftruename | ftruename | varchar | 255 |  | √ | ' ' |  |
| 3 | fidcard | fidcard | varchar | 20 |  |  | null |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fsource | fsource | varchar | 10 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | favatar | 头像 | varchar | 300 |  | √ | ' ' | 头像 |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fthirduserid | fthirduserid | varchar | 100 |  | √ | ' ' |  |
| 13 | ftid | ftid | int8 | 64 |  | √ | 0 |  |
| 14 | fdptid | fdptid | int8 | 64 |  |  | null |  |
| 15 | fuid | fuid | int8 | 64 |  | √ | 0 |  |
| 16 | fpositionid | fpositionid | int8 | 64 |  | √ | 0 |  |
| 17 | fusertype | 类型 | varchar | 100 |  | √ | ' ' | 类型,枚举: 1 :职员 3 :客户 4 :供应商 |
| 18 | fbillssatusfield | fbillssatusfield | varchar | 50 |  |  | null |  |
| 19 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 20 | fphone | 手机 | varchar | 36 |  | √ | ' ' | 手机 |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 22 | fbirthday | fbirthday | timestamp | 0 |  |  | null |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fisshruser | fisshruser | bpchar | 1 |  | √ | '0' |  |
| 25 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 26 | fgender | 性别 | varchar | 15 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 27 | fxksource | fxksource | int8 | 64 |  | √ | 0 |  |
| 28 | fsortcode | fsortcode | varchar | 10 |  |  | null |  |
| 29 | fheadsculpture | fheadsculpture | varchar | 300 |  | √ | ' ' |  |
| 30 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 31 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 32 | fnickname | fnickname | varchar | 300 |  |  | null |  |
| 33 | fsimplepinyin | fsimplepinyin | varchar | 50 |  | √ | ' ' |  |
| 34 | fopenid | fopenid | varchar | 50 |  | √ | ' ' |  |
| 35 | feid | feid | int8 | 64 |  | √ | 0 |  |
| 36 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
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
