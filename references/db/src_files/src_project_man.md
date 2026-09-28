# 项目成员-src_project_man

## 项目成员-主表 t_src_member

- **表名称：** 项目成员-主表
- **表名：** t_src_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginid | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_member_pid |  | fparentid |
| 2 | pk_src_member |  | fid |

---

## 成员分录-子表 t_src_memberentry

- **表名称：** 成员分录-子表
- **表名：** t_src_memberentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :正常 B :已转交 C :已授权 D :已处理 E :已终止 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fisnotify | 已通知 | bpchar | 1 |  | √ | '0' | 已通知 |
| 7 | fclarifytime | fclarifytime | timestamp | 0 |  |  | null |  |
| 8 | fbidderid | 姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fisclarify | 已澄清 | bpchar | 1 |  | √ | '0' | 已澄清 |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 pds_bizrole |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fbidder1 | 项目负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fphone | 联系电话 | varchar | 20 |  | √ | ' ' | 联系电话 |
| 16 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 18 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | femail | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 21 | fdescription | 利益关系申报 | varchar | 255 |  | √ | ' ' | 利益关系申报 |
| 22 | fbidder5 | 定标负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbidder4 | 评标负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fneedmessage | 是否发送消息 | bpchar | 1 |  | √ | '0' | 是否发送消息 |
| 25 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 26 | fbidder3 | 后审负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fbidder2 | 预审负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 29 | ftype | 人员类型 | bpchar | 1 |  | √ | ' ' | 人员类型,枚举: 1 :项目成员 2 :参标人员 3 :评委 |
| 30 | fissignin | 已签到 | bpchar | 1 |  | √ | '0' | 已签到 |
| 31 | fsignintime | 签到时间 | timestamp | 0 |  |  | null | 签到时间 |
| 32 | fisbenifit | 利益冲突 | bpchar | 1 |  | √ | '0' | 利益冲突,枚举: 0 :无冲突 1 :有冲突 2 :未澄清 |
| 33 | fneedsignin | 是否需要签到 | bpchar | 1 |  | √ | '0' | 是否需要签到 |
| 34 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 35 | fnumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
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
