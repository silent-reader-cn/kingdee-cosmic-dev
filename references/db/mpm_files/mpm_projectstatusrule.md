# 项目状态规则基础资料-mpm_projectstatusrule

## 项目状态规则基础资料-使用范围表 t_mpm_prostarule_u

- **表名称：** 项目状态规则基础资料-使用范围表
- **表名：** t_mpm_prostarule_u

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
| 1 | idx_t_mpm_prostarule_u_uo |  | fuseorgid |
| 2 | pk_t_mpm_prostarule_u |  | fdataid,fuseorgid |

---

## 项目状态规则基础资料-多语言表 t_mpm_prostarule_l

- **表名称：** 项目状态规则基础资料-多语言表
- **表名：** t_mpm_prostarule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_prostarule_l |  | fpkid |
| 2 | idx_mpm_prostarule_fidflid |  | fid,flocaleid |

---

## 项目状态规则基础资料-主表 t_mpm_prostarule

- **表名称：** 项目状态规则基础资料-主表
- **表名：** t_mpm_prostarule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 3 | fisnotification | 状态变更通知 | bpchar | 1 |  | √ | '0' | 状态变更通知 |
| 4 | ftargetstatusid | 目标状态 | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbeginstatusid | 开始状态 | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fisinitialstatus | 开始状态为初始状态 | bpchar | 1 |  | √ | '0' | 开始状态为初始状态 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_prostarule_fnumber |  | fnumber |
| 2 | pk_mpm_prostarule |  | fid |
| 3 | idx_t_mpm_prostarule_createorg |  | fcreateorgid |
| 4 | idx_t_mpm_prostarule_master |  | fmasterid |
