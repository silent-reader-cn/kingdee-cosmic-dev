# 参标人员后台数据-src_project_referf7

## 参标人员后台数据-主表 t_src_memberentry

- **表名称：** 参标人员后台数据-主表
- **表名：** t_src_memberentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fagentid | fagentid | int8 | 64 |  | √ | 0 |  |
| 3 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 6 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 7 | fisnotify | fisnotify | bpchar | 1 |  | √ | '0' |  |
| 8 | fclarifytime | fclarifytime | timestamp | 0 |  |  | null |  |
| 9 | fbidderid | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisclarify | fisclarify | bpchar | 1 |  | √ | '0' |  |
| 11 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |
| 15 | fscorestatus | fscorestatus | bpchar | 1 |  | √ | ' ' |  |
| 16 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 17 | fbidder1 | fbidder1 | int8 | 64 |  | √ | 0 |  |
| 18 | fphone | fphone | varchar | 20 |  | √ | ' ' |  |
| 19 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 24 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 25 | fbidder5 | fbidder5 | int8 | 64 |  | √ | 0 |  |
| 26 | fbidder4 | fbidder4 | int8 | 64 |  | √ | 0 |  |
| 27 | fneedmessage | fneedmessage | bpchar | 1 |  | √ | '0' |  |
| 28 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 29 | fbidder3 | fbidder3 | int8 | 64 |  | √ | 0 |  |
| 30 | fbidder2 | fbidder2 | int8 | 64 |  | √ | 0 |  |
| 31 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 32 | ftype | ftype | bpchar | 1 |  | √ | ' ' |  |
| 33 | fissignin | fissignin | bpchar | 1 |  | √ | '0' |  |
| 34 | fsignintime | fsignintime | timestamp | 0 |  |  | null |  |
| 35 | fisbenifit | fisbenifit | bpchar | 1 |  | √ | '0' |  |
| 36 | fneedsignin | fneedsignin | bpchar | 1 |  | √ | '0' |  |
| 37 | fenable | 有效否 | bpchar | 1 |  | √ | '1' | 有效否 |
| 38 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
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
