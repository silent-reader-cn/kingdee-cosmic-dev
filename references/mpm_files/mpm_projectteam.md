# 项目团队-mpm_projectteam

## 项目团队-子表 t_mpm_projteamentity

- **表名称：** 项目团队-子表
- **表名：** t_mpm_projteamentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fteamdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fteamroleid | 项目角色 | int8 | 64 |  | √ | 0 | 项目角色 mpm_projectrole |
| 4 | fteamuserid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fteamusrcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fteamoutdate | 离开时间 | timestamp | 0 |  |  | null | 离开时间 |
| 7 | fteamplanworktime | 计划投入（天） | numeric | 23 | 10 | √ | 0 | 计划投入（天） |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fteamdeptid | 负责部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fteamusrcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fteamindate | 加入时间 | timestamp | 0 |  |  | null | 加入时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projteamentity_fk |  | fid |
| 2 | pk_mpm_projteamentity |  | fentryid |

---

## 项目团队-主表 t_mpm_projectteam

- **表名称：** 项目团队-主表
- **表名：** t_mpm_projectteam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprojaprovbillid | 项目立项单ID | int8 | 64 |  | √ | 0 | 项目立项单ID |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fprojaprovbillno | 项目立项单编码 | varchar | 80 |  | √ | ' ' | 项目立项单编码 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
