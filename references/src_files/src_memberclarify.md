# 我的任务-src_memberclarify

## 我的任务-主表 t_src_memberentry

- **表名称：** 我的任务-主表
- **表名：** t_src_memberentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fsrcentryid | 源单分录id(评标设置分录) | int8 | 64 |  | √ | 0 | 源单分录id(评标设置分录) |
| 3 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待处理 B :已转交 C :已授权 D :已处理 E :已终止 |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fisnotify | 已通知 | bpchar | 1 |  | √ | '0' | 已通知 |
| 7 | fclarifytime | 澄清时间 | timestamp | 0 |  |  | null | 澄清时间 |
| 8 | fbidderid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fisclarify | 已澄清 | bpchar | 1 |  | √ | '0' | 已澄清 |
| 10 | fcreatedate | 任务创建时间 | timestamp | 0 |  |  | null | 任务创建时间 |
| 11 | fcreatorid | 原处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 pds_bizrole |
| 13 | fremark | 处理情况 | varchar | 255 |  | √ | ' ' | 处理情况 |
| 14 | fbidder1 | 项目负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fphone | 联系电话 | varchar | 20 |  | √ | ' ' | 联系电话 |
| 16 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 18 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | 转交日期 | timestamp | 0 |  |  | null | 转交日期 |
| 20 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 21 | fdescription | 利益关系申报 | varchar | 255 |  | √ | ' ' | 利益关系申报 |
| 22 | fbidder5 | 定标负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbidder4 | 评标负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fneedmessage | 是否需发送消息 | bpchar | 1 |  | √ | '0' | 是否需发送消息 |
| 25 | ffinishdate | 首次完成评标时间 | timestamp | 0 |  |  | null | 首次完成评标时间 |
| 26 | fbidder3 | 资质后审负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fbidder2 | 资质预审负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 29 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :项目成员 2 :参标人员 3 :评委 |
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
