# 用户信息-bos_usergroup_user

## 部门信息分录-子表 t_sec_userposition

- **表名称：** 部门信息分录-子表
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
| 14 | fposition | fposition | varchar | 255 |  | √ | ' ' |  |
| 15 | fpositionid | fpositionid | int8 | 64 |  | √ | 0 |  |
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

## 用户信息-使用范围表 t_sec_user_u

- **表名称：** 用户信息-使用范围表
- **表名：** t_sec_user_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrcount | ferrcount | int8 | 64 |  | √ | 0 |  |
| 3 | fuserdisablerid | 用户禁用人（废弃） | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fexternaluuid | fexternaluuid | varchar | 255 |  | √ | ' ' |  |
| 5 | fpsweffectivedate | fpsweffectivedate | timestamp | 0 |  |  | null |  |
| 6 | fuserdisabletime | 用户禁用时间（废弃） | timestamp | 0 |  |  | null | 用户禁用时间（废弃） |
| 7 | fpassword | fpassword | varchar | 255 |  | √ | ' ' |  |
| 8 | fusername | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 9 | flastloginip | flastloginip | varchar | 128 |  | √ | ' ' |  |
| 10 | fisactived | fisactived | bpchar | 1 |  | √ | '0' |  |
| 11 | ftype | ftype | varchar | 10 |  |  | null |  |
| 12 | flastlogintime | flastlogintime | timestamp | 0 |  |  | null |  |
| 13 | fauthorstatus | fauthorstatus | varchar | 10 |  |  | null |  |
| 14 | fuseenddate | 使用系统结束时间 | timestamp | 0 |  |  | null | 使用系统结束时间 |
| 15 | fislocked | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 16 | fisforbidden | 用户禁用 | bpchar | 1 |  | √ | '0' | 用户禁用 |
| 17 | fpswhisstr | fpswhisstr | varchar | 2000 |  | √ | ' ' |  |
| 18 | flockedtime | flockedtime | timestamp | 0 |  |  | null |  |
| 19 | fisregisted | fisregisted | bpchar | 1 |  | √ | '0' |  |
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

## 部门信息分录-多语言表 t_sec_userposition_l

- **表名称：** 部门信息分录-多语言表
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

## 用户信息-多语言表 t_sec_user_l

- **表名称：** 用户信息-多语言表
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

## 用户信息-主表 t_sec_user

- **表名称：** 用户信息-主表
- **表名：** t_sec_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftruename | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 3 | fidcard | 身份证号 | varchar | 20 |  |  | null | 身份证号 |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fsource | fsource | varchar | 10 |  |  | null |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | favatar | 头像 | varchar | 300 |  | √ | ' ' | 头像 |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fthirduserid | fthirduserid | varchar | 100 |  | √ | ' ' |  |
| 13 | ftid | ftid | int8 | 64 |  | √ | 0 |  |
| 14 | fdptid | fdptid | int8 | 64 |  |  | null |  |
| 15 | fuid | fuid | int8 | 64 |  | √ | 0 |  |
| 16 | fpositionid | fpositionid | int8 | 64 |  | √ | 0 |  |
| 17 | fusertype | 类型（废弃） | varchar | 100 |  | √ | ' ' | 类型（废弃）,枚举: 1 :职员 3 :客户 4 :供应商 |
| 18 | fbillssatusfield | fbillssatusfield | varchar | 50 |  |  | null |  |
| 19 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 20 | fphone | 手机 | varchar | 36 |  | √ | ' ' | 手机 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fisshruser | fisshruser | bpchar | 1 |  | √ | '0' |  |
| 25 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 26 | fgender | 性别 | varchar | 15 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 :保密 |
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
| 38 | fnumber | 工号 | varchar | 36 |  | √ | ' ' | 工号 |
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
