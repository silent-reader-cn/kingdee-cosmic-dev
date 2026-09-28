# 电子签章角色-ccas_memberrole

## 电子签章角色-多语言表 t_ccas_memberrole_l

- **表名称：** 电子签章角色-多语言表
- **表名：** t_ccas_memberrole_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_memberrole_l |  | fpkid |
| 2 | udx_ccas_memberrole_l |  | fid,flocaleid |

---

## 电子签章角色-主表 t_ccas_memberrole

- **表名称：** 电子签章角色-主表
- **表名：** t_ccas_memberrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | froleauthrange | 角色权限范围 | varchar | 1024 |  | √ | ' ' | 角色权限范围 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fprovidertype | 服务商对应枚举 | varchar | 50 |  | √ | ' ' | 服务商对应枚举 |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | fdefaultroleflag | 集成服务默认角色 | varchar | 1 |  | √ | '1' | 集成服务默认角色 |
| 10 | fintegratedserviceid | 集成服务标识 | varchar | 50 |  | √ | ' ' | 集成服务标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_memberrole |  | fid |
| 2 | idx_ccas_memberrole_sernum |  | fintegratedserviceid,fnumber |
| 3 | udx_ccas_memberrole_number |  | fnumber |
