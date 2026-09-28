# 参标人员后台数据-src_project_referf7

## 参标人员后台数据-主表 t_src_memberentry

- **表名称：** 参标人员后台数据-主表
- **表名：** t_src_memberentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 6 | fisnotify | fisnotify | bpchar | 1 |  | √ | '0' |  |
| 7 | fclarifytime | fclarifytime | timestamp | 0 |  |  | null |  |
| 8 | fbidderid | 姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fisclarify | fisclarify | bpchar | 1 |  | √ | '0' |  |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 pds_bizrole |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fbidder1 | fbidder1 | int8 | 64 |  | √ | 0 |  |
| 15 | fphone | fphone | varchar | 20 |  | √ | ' ' |  |
| 16 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 18 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | fbidder5 | fbidder5 | int8 | 64 |  | √ | 0 |  |
| 23 | fbidder4 | fbidder4 | int8 | 64 |  | √ | 0 |  |
| 24 | fneedmessage | fneedmessage | bpchar | 1 |  | √ | '0' |  |
| 25 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 26 | fbidder3 | fbidder3 | int8 | 64 |  | √ | 0 |  |
| 27 | fbidder2 | fbidder2 | int8 | 64 |  | √ | 0 |  |
| 28 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 29 | ftype | ftype | bpchar | 1 |  | √ | ' ' |  |
| 30 | fissignin | fissignin | bpchar | 1 |  | √ | '0' |  |
| 31 | fsignintime | fsignintime | timestamp | 0 |  |  | null |  |
| 32 | fisbenifit | fisbenifit | bpchar | 1 |  | √ | '0' |  |
| 33 | fneedsignin | fneedsignin | bpchar | 1 |  | √ | '0' |  |
| 34 | fenable | 有效否 | bpchar | 1 |  | √ | '1' | 有效否 |
| 35 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_memberentry_fbiz |  | fbizroleid |
| 2 | idx_src_memberentry_ftype |  | ftype |
| 3 | idx_src_memberentry_pid |  | fprojectid |
| 4 | idx_src_memberentry_fbid |  | fbidderid |
| 5 | pk_src_memberentry |  | fentryid |
| 6 | idx_src_memberentry_fpid |  | fparentid |
| 7 | idx_src_memberentry_fid |  | fid |

---

## 参标类型-多选基础资料表 t_src_referencetype

- **表名称：** 参标类型-多选基础资料表
- **表名：** t_src_referencetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_referencetype |  | fpkid |
| 2 | idx_src_reftype_bid |  | fbasedataid |
| 3 | idx_src_reftype_eid |  | fentryid |
