# 工序控制策略(废弃)-mpdm_proctrlstrategy

## 工序控制策略(废弃)-多语言表 t_mpdm_proctrlstry_l

- **表名称：** 工序控制策略(废弃)-多语言表
- **表名：** t_mpdm_proctrlstry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_proctrlstry_l_pkey |  | fpkid |
| 2 | idx_mpdm_proctrlstry_l |  | fid,flocaleid |

---

## 工序控制策略(废弃)-使用范围位图表 t_mpdm_proctrlstry_m

- **表名称：** 工序控制策略(废弃)-使用范围位图表
- **表名：** t_mpdm_proctrlstry_m

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
| 1 | pk_t_mpdm_proctrlstry_m |  | forgid |

---

## 工序控制策略(废弃)-使用范围表 t_mpdm_proctrlstry_u

- **表名称：** 工序控制策略(废弃)-使用范围表
- **表名：** t_mpdm_proctrlstry_u

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
| 1 | idx_t_mpdm_proctrlstry_u_uo |  | fuseorgid |
| 2 | t_mpdm_proctrlstry_u_pkey |  | fdataid,fuseorgid |

---

## 工序控制策略(废弃)-主表 t_mpdm_proctrlstry

- **表名称：** 工序控制策略(废弃)-主表
- **表名：** t_mpdm_proctrlstry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | freportmethod | 汇报方式 | varchar | 30 |  | √ | ' ' | 汇报方式,枚举: 1008 :必须汇报 1009 :可选汇报 1010 :不用汇报 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | freportseqctrl | 汇报顺序控制 | varchar | 30 |  | √ | ' ' | 汇报顺序控制,枚举: 1005 :顺序控制 1006 :告警 1007 :不控制 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fisenableinteropr | 启用内部工序 | bpchar | 1 |  | √ | ' ' | 启用内部工序 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fcheckmethod | 检验方式 | varchar | 30 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 17 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fpromode | 加工类型 | varchar | 30 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdeftimeunit | 工序时间默认单位 | varchar | 30 |  | √ | ' ' | 工序时间默认单位,枚举: 1014 :小时 1015 :分钟 1016 :秒 |
| 22 | freworkmethod | 返工方式 | varchar | 30 |  | √ | ' ' | 返工方式,枚举: 1 :直接返工 2 :返工工作台 |
| 23 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fisreportontransfer | 转移即汇报 | bpchar | 1 |  | √ | ' ' | 转移即汇报 |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fdisableorid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_proctrlstry_master |  | fmasterid |
| 2 | idx_mpdm_proctrl_org |  | fnumber,fcreateorgid |
| 3 | idx_t_mpdm_proctrlstry_createorg |  | fcreateorgid |
| 4 | t_mpdm_proctrlstry_pkey |  | fid |
