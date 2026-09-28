# 我的任务-src_memberclarify

## 我的任务-主表 t_src_memberentry

- **表名称：** 我的任务-主表
- **表名：** t_src_memberentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcentryid | 源单分录id(评标设置分录) | int8 | 64 |  | √ | 0 | 源单分录id(评标设置分录) |
| 4 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待处理 B :已转交 C :已授权 D :已处理 E :已终止 |
| 5 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fisnotify | 已通知 | bpchar | 1 |  | √ | '0' | 已通知 |
| 8 | fclarifytime | 澄清时间 | timestamp | 0 |  |  | null | 澄清时间 |
| 9 | fbidderid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisclarify | 已澄清 | bpchar | 1 |  | √ | '0' | 已澄清 |
| 11 | fcreatedate | 任务创建时间 | timestamp | 0 |  |  | null | 任务创建时间 |
| 12 | fcreatorid | 原处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |
| 15 | fscorestatus | 评分状态 | bpchar | 1 |  | √ | ' ' | 评分状态,枚举: 0 :未开始 1 :待评分 2 :已评分 3 :无需评分 4 :已关闭 |
| 16 | fremark | 处理情况 | varchar | 255 |  | √ | ' ' | 处理情况 |
| 17 | fbidder1 | 项目负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fphone | 联系电话 | varchar | 20 |  | √ | ' ' | 联系电话 |
| 19 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 22 | fcreatetime | 转交日期 | timestamp | 0 |  |  | null | 转交日期 |
| 23 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 24 | fdescription | 利益关系申报 | varchar | 255 |  | √ | ' ' | 利益关系申报 |
| 25 | fbidder5 | 定标负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbidder4 | 评标负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fneedmessage | 是否需发送消息 | bpchar | 1 |  | √ | '0' | 是否需发送消息 |
| 28 | ffinishdate | 首次完成评标时间 | timestamp | 0 |  |  | null | 首次完成评标时间 |
| 29 | fbidder3 | 资质后审负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbidder2 | 资质预审负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 32 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :项目成员 2 :参标人员 3 :评委 |
| 33 | fissignin | 已签到 | bpchar | 1 |  | √ | '0' | 已签到 |
| 34 | fsignintime | 签到时间 | timestamp | 0 |  |  | null | 签到时间 |
| 35 | fisbenifit | 利益冲突 | bpchar | 1 |  | √ | '0' | 利益冲突,枚举: 0 :无冲突 1 :有冲突 2 :未澄清 |
| 36 | fneedsignin | 是否需要签到 | bpchar | 1 |  | √ | '0' | 是否需要签到 |
| 37 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 38 | fnumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
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
