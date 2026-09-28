# 人员任职-bos_userposition

## 人员任职-主表 t_sec_userposition

- **表名称：** 人员任职-主表
- **表名：** t_sec_userposition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 人员 | int8 | 64 |  | √ | null | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fmaintain | fmaintain | varchar | 10 |  |  | null |  |
| 3 | forgstructureid | 组织结构 | int8 | 64 |  | √ | 0 | [行政组织结构 bos_adminorg_structure](../base_files/bos_adminorg_structure.md) |
| 4 | fispartjob | 兼职 | bpchar | 1 |  | √ | ' ' | 兼职 |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fpostid | fpostid | varchar | 36 |  |  | null |  |
| 7 | fsource | fsource | varchar | 10 |  |  | null |  |
| 8 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 9 | fsuperiorid | 直接上级 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisincharge | 负责人 | bpchar | 1 |  | √ | ' ' | 负责人 |
| 11 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 12 | fdptid | 部门 | int8 | 64 |  | √ | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fenable | fenable | bpchar | 1 |  |  | null |  |
| 14 | fposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 15 | fpositionid | 岗位 | int8 | 64 |  | √ | 0 | [岗位 bos_position](../base_files/bos_position.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_userposition_pkey |  | fentryid |
| 2 | idx_t_sec_userposition_fid |  | fid |
| 3 | idx_t_sec_userposition |  | fdptid |

---

## 人员任职-多语言表 t_sec_userposition_l

- **表名称：** 人员任职-多语言表
- **表名：** t_sec_userposition_l

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
| 1 | idx_sec_userposition_l_entry |  | fentryid,flocaleid |
| 2 | t_sec_userposition_l_pkey |  | fpkid |
