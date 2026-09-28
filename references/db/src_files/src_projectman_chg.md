# 项目成员变更-src_projectman_chg

## 参标类型(变更后)-多选基础资料表 t_src_referencetype_new

- **表名称：** 参标类型(变更后)-多选基础资料表
- **表名：** t_src_referencetype_new

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
| 1 | pk_src_referencetype_new |  | fpkid |
| 2 | idx_src_reftype_new_bid |  | fbasedataid |
| 3 | idx_src_reftype_new_eid |  | fentryid |

---

## 项目成员变更-主表 t_src_projectmanchg

- **表名称：** 项目成员变更-主表
- **表名：** t_src_projectmanchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fprojectcreatorid | 项目创建人(变更前) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fnewprojectcreatorid | 项目创建人(变更后) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectmanchg_pid |  | fparentid |
| 2 | pk_src_projectmanchg |  | fid |

---

## 项目成员变更分录-子表 t_src_promanchgentry

- **表名称：** 项目成员变更分录-子表
- **表名：** t_src_promanchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 原单分录ID | varchar | 50 |  | √ | ' ' | 原单分录ID |
| 3 | fnewbidderid | 姓名(变更后) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fneedsignin_new | 是否需要签到 | bpchar | 1 |  | √ | '0' | 是否需要签到 |
| 6 | fneedmessage | 是否发送消息(变更前) | bpchar | 1 |  | √ | '0' | 是否发送消息(变更前) |
| 7 | fbidderid | 姓名(变更前) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbizrolenewid | 业务角色(变更后) | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |
| 9 | ftype | 人员类型 | bpchar | 1 |  | √ | '1' | 人员类型,枚举: 1 :项目成员 2 :参标人员 |
| 10 | fneedsignin | 是否需要签到(变更前) | bpchar | 1 |  | √ | '0' | 是否需要签到(变更前) |
| 11 | fisnew | 变更方式 | bpchar | 1 |  | √ | '0' | 变更方式,枚举: 1 :修改 2 :删除 3 :新增 0 :无变化 |
| 12 | fneedmessage_new | 是否发送消息 | bpchar | 1 |  | √ | '0' | 是否发送消息 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbizroleid | 业务角色(变更前) | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_promanchgentry_fid |  | fid |
| 2 | pk_src_promanchgentry |  | fentryid |

---

## 参标类型(变更前)-多选基础资料表 t_src_referencetype_chg

- **表名称：** 参标类型(变更前)-多选基础资料表
- **表名：** t_src_referencetype_chg

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
| 1 | idx_src_reftype_chg_eid |  | fentryid |
| 2 | idx_src_reftype_chg_bid |  | fbasedataid |
| 3 | pk_src_referencetype_chg |  | fpkid |
