# 运费方案-pmm_freightscheme

## 运费信息-子表 t_mal_freightentry

- **表名称：** 运费信息-子表
- **表名：** t_mal_freightentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffreight | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 3 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fprice | 单笔金额（小于） | numeric | 23 | 10 | √ | 0 | 单笔金额（小于） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_freightentry_fid_fseq |  | fid,fseq |
| 2 | pk_mal_freightentry |  | fentryid |

---

## 运费方案-使用范围表 t_mal_freight_u

- **表名称：** 运费方案-使用范围表
- **表名：** t_mal_freight_u

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
| 1 | t_mal_freight_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mal_freight_u_uo |  | fuseorgid |

---

## 运费方案-多语言表 t_mal_freight_l

- **表名称：** 运费方案-多语言表
- **表名：** t_mal_freight_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_freight_l_fid |  | fid,flocaleid |
| 2 | pk_mal_freight_l |  | fpkid |

---

## 运费方案-使用范围位图表 t_mal_freight_m

- **表名称：** 运费方案-使用范围位图表
- **表名：** t_mal_freight_m

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
| 1 | pk_t_mal_freight_m |  | forgid |

---

## 运费方案-主表 t_mal_freight

- **表名称：** 运费方案-主表
- **表名：** t_mal_freight

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 9 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 10 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 14 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 17 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 18 | fbasefreight | 基础运费 | numeric | 23 | 10 | √ | 0 | 基础运费 |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fnational | 全国供货 | bpchar | 1 |  | √ | ' ' | 全国供货 |
| 22 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 24 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_freight_fnumber |  | fnumber |
| 2 | idx_t_mal_freight_createorg |  | fcreateorgid |
| 3 | idx_t_mal_freight_master |  | fmasterid |
| 4 | pk_mal_freight |  | fid |

---

## 省-多选基础资料表 t_mal_freightentry_pro

- **表名称：** 省-多选基础资料表
- **表名：** t_mal_freightentry_pro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_freightentry_pro_fid |  | fid,fbasedataid |
| 2 | pk_mal_freightentry_pro |  | fpkid |

---

## 市-多选基础资料表 t_mal_freightentry_city

- **表名称：** 市-多选基础资料表
- **表名：** t_mal_freightentry_city

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_freightentry_city |  | fpkid |
| 2 | idx_mal_freightentry_city_fid |  | fid,fbasedataid |
