# 成员管理-ccas_membermanage

## 成员管理-主表 t_ccas_membermanage

- **表名称：** 成员管理-主表
- **表名：** t_ccas_membermanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmemberauthstatus | 成员认证状态 | varchar | 1 |  | √ | 'A' | 成员认证状态,枚举: A :未认证 B :已认证 |
| 4 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisinvite | 是否已邀请 | varchar | 1 |  | √ | 'A' | 是否已邀请,枚举: A :未邀请 B :已邀请 |
| 7 | fproviderphone | 服务商手机号 | varchar | 50 |  | √ | ' ' | 服务商手机号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmemberid | 服务商成员id | varchar | 50 |  | √ | ' ' | 服务商成员id |
| 11 | fsignrole | 电子签章角色（废弃） | varchar | 1 |  | √ | 'B' | 电子签章角色（废弃）,枚举: A :超级管理员 B :成员 |
| 12 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fesserviceprovider | 集成服务 | int8 | 64 |  | √ | 0 | [集成服务配置 ccas_cisconfig](../ccas_files/ccas_cisconfig.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_membermanage |  | fid |
| 2 | idx_ccas_membermanage_orguser |  | forgfield,fuser,fesserviceprovider |

---

## 电子签章角色-多选基础资料表 t_ccas_membermanagerole

- **表名称：** 电子签章角色-多选基础资料表
- **表名：** t_ccas_membermanagerole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [电子签章角色 ccas_memberrole](../ccas_files/ccas_memberrole.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | udx_ccas_membermanagerole |  | fid,fbasedataid |
| 2 | pk_ccas_membermanagerole |  | fpkid |

---

## 成员管理-多语言表 t_ccas_membermanage_l

- **表名称：** 成员管理-多语言表
- **表名：** t_ccas_membermanage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 10 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_membermanage_l |  | fpkid |
| 2 | udx_ccas_membermanage_l |  | fid,flocaleid |
