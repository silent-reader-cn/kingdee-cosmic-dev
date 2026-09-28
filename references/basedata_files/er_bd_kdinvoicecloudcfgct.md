# 发票云配置(集团)-er_bd_kdinvoicecloudcfgct

## 发票云配置(集团)-使用范围表 t_er_kdinvoicectrlcfg_u

- **表名称：** 发票云配置(集团)-使用范围表
- **表名：** t_er_kdinvoicectrlcfg_u

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
| 1 | pk_t_er_kdinvoicectrlcfg_u |  | fdataid,fuseorgid |
| 2 | idx_t_er_kdinvoicectrlcfg_u_uo |  | fuseorgid |

---

## 发票云配置(集团)-主表 t_er_kdinvoicectrlcfg

- **表名称：** 发票云配置(集团)-主表
- **表名：** t_er_kdinvoicectrlcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnamenotmatch_ci | 发票抬头与企业名称一致： | bpchar | 1 |  | √ | '0' | 发票抬头与企业名称一致：,枚举: 0 :严格控制 1 :不控制 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ffirmname | 企业工商登记名 | varchar | 150 |  | √ | ' ' | 企业工商登记名 |
| 5 | fclientkey | 接入标识 | varchar | 50 |  | √ | ' ' | 接入标识 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fencrypt_key | 加密密钥 | varchar | 50 |  | √ | ' ' | 加密密钥 |
| 10 | fsync | 是否是同步来的数据 | bpchar | 1 |  | √ | '0' | 是否是同步来的数据 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | freimed_ci | 重复报销： | bpchar | 1 |  | √ | '0' | 重复报销：,枚举: 0 :严格控制 1 :不控制 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fchecknotpass_ci | 发票真伪： | bpchar | 1 |  | √ | '0' | 发票真伪：,枚举: 0 :严格控制 1 :不控制 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fclients | 客户端标识 | varchar | 50 |  | √ | ' ' | 客户端标识 |
| 20 | fclient_secret | 授权密钥 | varchar | 50 |  | √ | ' ' | 授权密钥 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | ftaxnumnotmatch_ci | 发票税号与企业税号一致： | bpchar | 1 |  | √ | '0' | 发票税号与企业税号一致：,枚举: 0 :严格控制 1 :不控制 |
| 23 | fnonoffsetcomputoutaount | 抵扣为否，是否计算转出金额 | bpchar | 1 |  | √ | '0' | 抵扣为否，是否计算转出金额,枚举: 1 :是 0 :否 |
| 24 | fclient_id | 发票云授权标识 | varchar | 50 |  | √ | ' ' | 发票云授权标识 |
| 25 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 28 | ftaxregnum | 企业税号 | varchar | 150 |  | √ | ' ' | 企业税号 |
| 29 | foffsetonlyfrominvoice | 仅按发票判断是否抵扣 | bpchar | 1 |  | √ | '0' | 仅按发票判断是否抵扣,枚举: 1 :是 0 :否 |
| 30 | fbuyernamele5_ci | 个人发票抬头与企业名称一致： | bpchar | 1 |  | √ | '0' | 个人发票抬头与企业名称一致：,枚举: 0 :严格控制 1 :不控制 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fdeductibleoftaxpayer | 按纳税人类型判断是否抵扣 | bpchar | 1 |  | √ | '1' | 按纳税人类型判断是否抵扣,枚举: 1 :是 0 :否 |
| 33 | fnonoffsetimporttaxamout | 导入不可抵扣发票的税额 | bpchar | 1 |  | √ | '0' | 导入不可抵扣发票的税额,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_kdinvoicectrlcfg_fnumbe |  | fnumber |
| 2 | idx_t_er_kdinvoicectrlcfg_createorg |  | fcreateorgid |
| 3 | idx_t_er_kdinvoicectrlcfg_master |  | fmasterid |
| 4 | pk_t_er_kdinvoicectrlcfg |  | fid |

---

## 发票云配置(集团)-多语言表 t_er_kdinvoicectrlcfg_l

- **表名称：** 发票云配置(集团)-多语言表
- **表名：** t_er_kdinvoicectrlcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_kdinvoicectrlcfg_l |  | fpkid |
| 2 | idx_er_kdinvoicectrlcfg_l_fnam |  | fname |
| 3 | idx_er_kdinvoicectrlcfg_l_fid |  | fid,flocaleid |

---

## 发票云配置(集团)-使用范围位图表 t_er_kdinvoicectrlcfg_m

- **表名称：** 发票云配置(集团)-使用范围位图表
- **表名：** t_er_kdinvoicectrlcfg_m

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
| 1 | pk_t_er_kdinvoicectrlcfg_m |  | forgid |
