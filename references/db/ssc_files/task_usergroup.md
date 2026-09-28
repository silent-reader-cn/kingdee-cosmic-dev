# 用户组-task_usergroup

## 用户信息分录-子表 t_tk_usergroupentry

- **表名称：** 用户信息分录-子表
- **表名：** t_tk_usergroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskallnum_e | 处理任务总数上限 | int8 | 64 |  | √ | 10000 | 处理任务总数上限 |
| 3 | fgroupid | 用户组id | int8 | 64 |  | √ | 0 | 用户组id |
| 4 | fcurtasknum_e | 处理中任务数上限 | int8 | 64 |  | √ | 10000 | 处理中任务数上限 |
| 5 | fdptname | fdptname | int8 | 64 |  | √ | 0 |  |
| 6 | fusestatus | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fteamleader | 组长 | bpchar | 1 |  | √ | '0' | 组长 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fability | 能力值 | numeric | 19 | 10 | √ | 1.0000000000 | 能力值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_usergroupentry |  | fuserid |
| 2 | t_tk_usergroupentry_pkey |  | fentryid |
| 3 | idx_ssc_usergroup_e_fgrpid |  | fgroupid |
| 4 | idx_ssc_usergroup_e_fid |  | fid |

---

## 用户组-主表 t_tk_usergroup

- **表名称：** 用户组-主表
- **表名：** t_tk_usergroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisrobots | 智能机器人 | bpchar | 1 |  | √ | '0' | 智能机器人 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fadminid | fadminid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ftaskallnum | 处理任务总数上限 | int8 | 64 |  | √ | 10000 | 处理任务总数上限 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fssccenterid | 共享中心-废弃 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fuserid | fuserid | int8 | 64 |  | √ | 0 |  |
| 19 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fworkperiod | 工作期间 | bpchar | 1 |  | √ | '2' | 工作期间,枚举: 1 :每天 2 :每月 |
| 21 | fctrlstrategy | 控制策略 | varchar | 4 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fcurtasknum | 处理中任务数上限 | int8 | 64 |  | √ | 10000 | 处理中任务数上限 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tk_usergroup_createorg |  | fcreateorgid |
| 2 | index_ssc_usergroup |  | fnumber |
| 3 | t_tk_usergroup_pkey |  | fid |
| 4 | idx_t_tk_usergroup_master |  | fmasterid |

---

## 用户组-使用范围表 t_tk_usergroup_u

- **表名称：** 用户组-使用范围表
- **表名：** t_tk_usergroup_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tk_usergroup_u_uo |  | fuseorgid |
| 2 | t_tk_usergroup_u_pkey |  | fdataid,fuseorgid |

---

## 用户组-使用范围位图表 t_tk_usergroup_m

- **表名称：** 用户组-使用范围位图表
- **表名：** t_tk_usergroup_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_usergroup_m |  | forgid |

---

## 用户组-多语言表 t_tk_usergroup_l

- **表名称：** 用户组-多语言表
- **表名：** t_tk_usergroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_usergroup_l_pkey |  | fpkid |
| 2 | index_ssc_usergroup_l |  | fid,flocaleid |
