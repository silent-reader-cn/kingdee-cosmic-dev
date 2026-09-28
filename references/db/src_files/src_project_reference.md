# 参标人员-src_project_reference

## 参标人员-主表 t_src_member

- **表名称：** 参标人员-主表
- **表名：** t_src_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginid | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | friskinfo | 风险信息 | varchar | 2000 |  | √ | ' ' | 风险信息 |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fmemberschemeid | fmemberschemeid | int8 | 64 |  | √ | 0 |  |
| 9 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

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

## 人员分录-子表 t_src_memberentry

- **表名称：** 人员分录-子表
- **表名：** t_src_memberentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | fagentid | int8 | 64 |  | √ | 0 |  |
| 3 | fsrcentryid | 源单分录id(评标设置分录) | int8 | 64 |  | √ | 0 | 源单分录id(评标设置分录) |
| 4 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :正常 B :已转交 C :已授权 D :已处理 E :已终止 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fisnotify | 已通知 | bpchar | 1 |  | √ | '0' | 已通知 |
| 8 | fclarifytime | fclarifytime | timestamp | 0 |  |  | null |  |
| 9 | fbidderid | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisclarify | 已澄清 | bpchar | 1 |  | √ | '0' | 已澄清 |
| 11 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |
| 15 | fscorestatus | 评分状态 | bpchar | 1 |  | √ | ' ' | 评分状态,枚举: 0 :未开始 1 :待评分 2 :已评分 3 :无需评分 4 :已关闭 |
| 16 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 17 | fbidder1 | 项目负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fphone | 联系电话 | varchar | 20 |  | √ | ' ' | 联系电话 |
| 19 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | femail | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 24 | fdescription | 利益关系申报 | varchar | 255 |  | √ | ' ' | 利益关系申报 |
| 25 | fbidder5 | 定标负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbidder4 | 评标负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fneedmessage | 是否发送消息 | bpchar | 1 |  | √ | '0' | 是否发送消息 |
| 28 | ffinishdate | 完成评标时间 | timestamp | 0 |  |  | null | 完成评标时间 |
| 29 | fbidder3 | 后审负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbidder2 | 预审负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 32 | ftype | 人员类型 | bpchar | 1 |  | √ | ' ' | 人员类型,枚举: 1 :项目成员 2 :参标人员 3 :评委 |
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
