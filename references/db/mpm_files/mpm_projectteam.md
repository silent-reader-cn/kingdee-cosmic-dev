# 项目团队-mpm_projectteam

## 项目团队-子表 t_mpm_projteamentity

- **表名称：** 项目团队-子表
- **表名：** t_mpm_projteamentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fteamroleid | 项目角色 | int8 | 64 |  | √ | 0 | [项目角色 mpm_projectrole](../mpm_files/mpm_projectrole.md) |
| 3 | fteamuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fteamoutdate | 离开时间 | timestamp | 0 |  |  | null | 离开时间 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fteamdeptid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fteamusrcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fteamorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fteamdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fteamusrcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | 'A' | 来源类型,枚举: A :手工添加 B :特殊权限设置 |
| 13 | fteamplanworktime | 计划投入（天） | numeric | 23 | 10 | √ | 0 | 计划投入（天） |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fteamindate | 加入时间 | timestamp | 0 |  |  | null | 加入时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projteamentity_user |  | fteamuserid |
| 2 | idx_mpm_projteamentity_fk |  | fid |
| 3 | pk_mpm_projteamentity |  | fentryid |

---

## 项目团队-主表 t_mpm_projectteam

- **表名称：** 项目团队-主表
- **表名：** t_mpm_projectteam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fprojaprovbillid | 项目立项单ID | int8 | 64 |  | √ | 0 | 项目立项单ID |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fprojaprovbillno | 项目立项单编码 | varchar | 80 |  | √ | ' ' | 项目立项单编码 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_projectteam |  | fid |
| 2 | idx_mpm_projectteam_fprj |  | fprojectid |
| 3 | idx_mpm_projectteam_fbillno |  | fbillno |
| 4 | idx_mpm_projectteam_proapprid |  | fprojaprovbillid |

---

## 项目团队-多语言表 t_mpm_projteamentity_l

- **表名称：** 项目团队-多语言表
- **表名：** t_mpm_projteamentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fteamdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
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
| 1 | pk_mpm_projteamentity_l |  | fpkid |
| 2 | idx_mpm_projteamentity_l |  | fentryid,flocaleid |
