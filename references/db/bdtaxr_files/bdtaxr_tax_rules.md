# 税务规则-bdtaxr_tax_rules

## 税务规则-主表 t_bdtaxr_tax_rules

- **表名称：** 税务规则-主表
- **表名：** t_bdtaxr_tax_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 5 | fitemclass | 税码/税组 | varchar | 50 |  | √ | ' ' | 税码/税组,枚举: bastax_taxcode :税码 bastax_taxgroup :税组 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 18 | ftype | 税则分类 | int8 | 64 |  | √ | 0 | 税务规则分类 bdtaxr_tax_rules_type |
| 19 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fitemresult | 规则结果 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fdesc | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fcountry | 国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bdtaxr_tax_rules_createorg |  | fcreateorgid |
| 2 | idx_t_bdtaxr_tax_rules_master |  | fmasterid |
| 3 | idx_bdtaxr_tax_rules |  | forgid,fstartdate,fenddate |
| 4 | pk_bdtaxr_tax_rules |  | fid |

---

## 规则条件-子表 t_bdtaxr_tax_rules_entry

- **表名称：** 规则条件-子表
- **表名：** t_bdtaxr_tax_rules_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flink | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: AND :并且 |
| 3 | fentryclass | 税要素大类 | varchar | 50 |  | √ | ' ' | 税要素大类,枚举: bastax_addresstype :地址条件 bastax_party_type :交易方资质 bastax_taxproduct :税务产品 bastax_process_type :自定义税要素 |
| 4 | fvalueid | 值ID | varchar | 500 |  | √ | ' ' | 值ID |
| 5 | fvaluenumber | 值编码 | varchar | 500 |  | √ | ' ' | 值编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: = :等于 <> :不等于 in :在...中 not in :不在...中 |
| 8 | fentrytype | 税要素小类 | int8 | 64 |  | √ | 0 | 地址类型 bastax_addresstype |
| 9 | fvaluename | 值 | varchar | 500 |  | √ | ' ' | 值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_tax_rules_entry |  | fentryid |
| 2 | idx_bdtaxr_tax_rules_entry_fk |  | fid |

---

## 税务规则-多语言表 t_bdtaxr_tax_rules_l

- **表名称：** 税务规则-多语言表
- **表名：** t_bdtaxr_tax_rules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_tax_rules_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_tax_rules_l |  | fpkid |

---

## 税务规则-使用范围位图表 t_bdtaxr_tax_rules_m

- **表名称：** 税务规则-使用范围位图表
- **表名：** t_bdtaxr_tax_rules_m

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
| 1 | pk_t_bdtaxr_tax_rules_m |  | forgid |

---

## 税务规则-使用范围表 t_bdtaxr_tax_rules_u

- **表名称：** 税务规则-使用范围表
- **表名：** t_bdtaxr_tax_rules_u

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
| 1 | pk_t_bdtaxr_tax_rules_u |  | fdataid,fuseorgid |
| 2 | idx_t_bdtaxr_tax_rules_u_uo |  | fuseorgid |
