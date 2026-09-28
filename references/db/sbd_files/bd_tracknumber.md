# 跟踪号-bd_tracknumber

## 跟踪号-主表 t_bd_tracknumber

- **表名称：** 跟踪号-主表
- **表名：** t_bd_tracknumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fsourcebillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 13 | ftracknumbergroupid | 跟踪号组 | int8 | 64 |  | √ | 0 | 跟踪号分组 bd_tracknumbergroup |
| 14 | fcreateorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcebillentryid | 来源单据分录id | varchar | 50 |  | √ | ' ' | 来源单据分录id |
| 17 | fsourcebilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fsourcebillentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 23 | fsourcebillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 24 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 跟踪号 | varchar | 50 |  | √ | ' ' | 跟踪号 |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | ftrackstatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: 0 :未关闭 1 :关闭 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_tracknumber_master |  | fmasterid |
| 2 | idx_bd_tracknumber_number |  | fnumber |
| 3 | idx_t_bd_tracknumber_createorg |  | fcreateorgid |
| 4 | t_bd_tracknumber_pkey |  | fid |

---

## 跟踪号-使用范围位图表 t_bd_tracknumber_m

- **表名称：** 跟踪号-使用范围位图表
- **表名：** t_bd_tracknumber_m

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
| 1 | pk_t_bd_tracknumber_m |  | forgid |

---

## 跟踪号-使用范围表 t_bd_tracknumber_u

- **表名称：** 跟踪号-使用范围表
- **表名：** t_bd_tracknumber_u

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
| 1 | idx_t_bd_tracknumber_u_uo |  | fuseorgid |
| 2 | t_bd_tracknumber_u_pkey |  | fdataid,fuseorgid |

---

## 跟踪号-多语言表 t_bd_tracknumber_l

- **表名称：** 跟踪号-多语言表
- **表名：** t_bd_tracknumber_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname |  | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_tracknumber_l_pkey |  | fpkid |
| 2 | idx_bd_tracknumber_l_fid |  | fid,flocaleid |
