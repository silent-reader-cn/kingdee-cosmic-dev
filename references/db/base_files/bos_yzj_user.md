# 云之家用户-bos_yzj_user

## 云之家用户-主表 t_yzj_user

- **表名称：** 云之家用户-主表
- **表名：** t_yzj_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 手机 | varchar | 36 |  | √ | ' ' | 手机 |
| 3 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 4 | fbackuptype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: cloud-hub :云之家 before :同步前 after :同步后 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 7 | fgender | 性别 | varchar | 15 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 8 | fidcard | 身份证号 | varchar | 20 |  | √ | ' ' | 身份证号 |
| 9 | fheadsculpture | fheadsculpture | varchar | 300 |  | √ | ' ' |  |
| 10 | fuserid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | favatar | 头像 | varchar | 300 |  | √ | ' ' | 头像 |
| 13 | fsimplepinyin | 姓名简拼 | varchar | 50 |  | √ | ' ' | 姓名简拼 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fopenid | 用户云之家OpenID | varchar | 50 |  | √ | ' ' | 用户云之家OpenID |
| 16 | feid | 工作圈eid | int8 | 64 |  | √ | 0 | 工作圈eid |
| 17 | ftid | 团队ID | int8 | 64 |  | √ | 0 | 团队ID |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fuid | 云之家账号内码 | int8 | 64 |  | √ | 0 | 云之家账号内码 |
| 20 | fnumber | 工号 | varchar | 36 |  | √ | ' ' | 工号 |
| 21 | fusertype | 类型 | varchar | 100 |  | √ | ' ' | 类型,枚举: |
| 22 | ftaskid | 云之家同步任务 | int8 | 64 |  | √ | 0 | 协同云同步任务 bos_yzj_synctask |
| 23 | ffullpinyin | 姓名全拼 | varchar | 100 |  | √ | ' ' | 姓名全拼 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_user_fuid |  | fuid |
| 2 | idx_t_yzj_user_phonemail |  | fphone,femail |
| 3 | idx_yzj_user_taskbtuser |  | ftaskid,fbackuptype,fuserid |
| 4 | t_yzj_user_pkey |  | fid |
| 5 | idx_t_yzj_user_usertype |  | fusertype |

---

## 单据体-子表 t_yzj_userposition

- **表名称：** 单据体-子表
- **表名：** t_yzj_userposition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispartjob | 兼职 | bpchar | 1 |  | √ | '0' | 兼职 |
| 3 | fsuperiorid | 直接上级 | int8 | 64 |  | √ | 0 | 云之家用户 bos_yzj_user |
| 4 | fisincharge | 负责人 | bpchar | 1 |  | √ | '0' | 负责人 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdptid | 部门 | int8 | 64 |  | √ | 0 | 云之家组织 bos_yzj_org |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_userposition |  | fid |
| 2 | t_yzj_userposition_pkey |  | fentryid |

---

## 单据体-多语言表 t_yzj_userposition_l

- **表名称：** 单据体-多语言表
- **表名：** t_yzj_userposition_l

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
| 1 | t_yzj_userposition_l_pkey |  | fpkid |
| 2 | idx_yzj_userpos_l_fentryid |  | fentryid,flocaleid |

---

## 云之家用户-多语言表 t_yzj_user_l

- **表名称：** 云之家用户-多语言表
- **表名：** t_yzj_user_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftruename | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_user_l_fid |  | fid,flocaleid |
| 2 | t_yzj_user_l_pkey |  | fpkid |
