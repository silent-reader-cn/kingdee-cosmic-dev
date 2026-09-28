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
| 2 | fnamenotmatch_ci | 发票抬头与企业名称一致： | bpchar | 1 |  | √ | '0' | 发票抬头与企业名称一致：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ffirmname | 企业工商登记名 | varchar | 150 |  | √ | ' ' | 企业工商登记名 |
| 5 | fclientkey | 接入标识 | varchar | 50 |  | √ | ' ' | 接入标识 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finvoicecurrency | 发票币种设置 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fencrypt_key | 加密密钥 | varchar | 50 |  | √ | ' ' | 加密密钥 |
| 11 | fsync | 是同步来的数据 | bpchar | 1 |  | √ | '0' | 是同步来的数据 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | freimed_ci | 重复报销： | bpchar | 1 |  | √ | '0' | 重复报销：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fchecknotpass_ci | 发票真伪： | bpchar | 1 |  | √ | '0' | 发票真伪：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fidenticalpartyinvcom | 往来单位与开票公司一致 | bpchar | 1 |  | √ | '2' | 往来单位与开票公司一致,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fclients | 客户端标识 | varchar | 50 |  | √ | ' ' | 客户端标识 |
| 22 | fclient_secret | 授权密钥 | varchar | 50 |  | √ | ' ' | 授权密钥 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ftaxnumnotmatch_ci | 发票税号与企业税号一致： | bpchar | 1 |  | √ | '0' | 发票税号与企业税号一致：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 25 | fnonoffsetcomputoutaount | 抵扣为否，是否计算转出金额 | bpchar | 1 |  | √ | '0' | 抵扣为否，是否计算转出金额,枚举: 1 :是 0 :否 |
| 26 | fignorechar | 忽略特殊符号差异 | varchar | 80 |  | √ | ' ' | 忽略特殊符号差异,枚举: 1 :空格（企业名称首尾空格） 5 :空格（所有空格） 2 :中英文括号 3 :中英文破折号 |
| 27 | fclient_id | 发票云授权标识 | varchar | 50 |  | √ | ' ' | 发票云授权标识 |
| 28 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | ftaxlenvalidrang | 校验税号长度 | varchar | 100 |  | √ | ' ' | 校验税号长度 |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 32 | ftaxregnum | 企业税号 | varchar | 150 |  | √ | ' ' | 企业税号 |
| 33 | foffsetonlyfrominvoice | 仅按发票判断可抵扣 | bpchar | 1 |  | √ | '0' | 仅按发票判断可抵扣,枚举: 1 :是 0 :否 |
| 34 | fbuyernamele5_ci | 个人发票抬头与企业名称一致： | bpchar | 1 |  | √ | '0' | 个人发票抬头与企业名称一致：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 36 | fdeductibleoftaxpayer | 按纳税人类型判断可抵扣 | bpchar | 1 |  | √ | '1' | 按纳税人类型判断可抵扣,枚举: 1 :是 0 :否 |
| 37 | fnonoffsetimporttaxamout | 导入不可抵扣发票的税额 | bpchar | 1 |  | √ | '0' | 导入不可抵扣发票的税额,枚举: 1 :是 0 :否 |
| 38 | fcountry | 国家/区域 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

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
