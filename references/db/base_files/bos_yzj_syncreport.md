# 协同云同步报告-bos_yzj_syncreport

## 协同云同步报告-多语言表 t_yzj_syncreport_l

- **表名称：** 协同云同步报告-多语言表
- **表名：** t_yzj_syncreport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsyncobject | 对象 | varchar | 255 |  | √ | ' ' | 对象 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_syncreport_l_fid |  | fid,flocaleid |
| 2 | t_yzj_syncreport_l_pkey |  | fpkid |

---

## 单据体-子表 t_yzj_syncreportentry

- **表名称：** 单据体-子表
- **表名：** t_yzj_syncreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyzjvalue | 协同云属性值 | varchar | 1024 |  | √ | ' ' | 协同云属性值 |
| 3 | ferpvalue | 系统属性值 | varchar | 1024 |  | √ | ' ' | 系统属性值 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fproperty | 属性 | varchar | 30 |  | √ | ' ' | 属性,枚举: useropenid :openId fuid :UID name :名称 number :工号 phone :手机 email :邮箱 gender :性别 birthday :生日 picturefield :头像 mainJob :主职 partJob :兼职 id :ID rootId :根组织ID rootName :根组织名称 sortcode :排序 eid :工作圈EID tid :团队TID yzjparentorgid :上级组织 main_org :主职部门 main_position :主职职位 main_admin :主职负责人 part_org :兼职部门 part_position :兼职职位 part_admin :兼职负责人 yzjorgid :云之家ID fullname :长名称 rootOrg :根组织 main_superior :直接上级 sortnumber :排序码 |
| 6 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 7 | foperation | 处理方式 | varchar | 30 |  | √ | ' ' | 处理方式,枚举: add :新增 edit :修改 delete :删除 disable :禁用 enable :启用 freeze :封存 unfreeze :解封 move :移动 discard :废弃 manual :手工处理 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_yzj_syncreportentry_pkey |  | fentryid |
| 2 | idx_t_yzj_syncreportentry_fid |  | fid |

---

## 单据体-多语言表 t_yzj_syncreportentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_yzj_syncreportentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_yzj_syncreportentry_l_pkey |  | fpkid |

---

## 协同云同步报告-主表 t_yzj_syncreport

- **表名称：** 协同云同步报告-主表
- **表名：** t_yzj_syncreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsyncobject | 对象 | varchar | 255 |  | √ | ' ' | 对象 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :未同步 1 :已同步 2 :警告 3 :异常 4 :忽略 |
| 4 | fmodifierid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ferpdataid | 金蝶云数据主键 | varchar | 100 |  | √ | ' ' | 金蝶云数据主键 |
| 8 | fyzjdataid | 协同云数据主键 | varchar | 100 |  | √ | ' ' | 协同云数据主键 |
| 9 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 10 | ftaskid | 协同云同步任务 | int8 | 64 |  | √ | 0 | [协同云同步任务 bos_yzj_synctask](../base_files/bos_yzj_synctask.md) |
| 11 | fdatatype | 对象类型 | varchar | 30 |  | √ | ' ' | 对象类型,枚举: org :组织 user :人员 |
| 12 | fmodifytime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_syncreport_number |  | fnumber |
| 2 | t_yzj_syncreport_pkey |  | fid |
