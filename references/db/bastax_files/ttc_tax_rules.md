# 税务规则-ttc_tax_rules

## 税务规则-主表 t_bastax_tax_rules

- **表名称：** 税务规则-主表
- **表名：** t_bastax_tax_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 5 | fitemclass | 税码/税组 | varchar | 50 |  | √ | ' ' | 税码/税组,枚举: bastax_taxcode :税码 bastax_taxgroup :税组 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftaxareagroup | 税收辖区(废弃) | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 20 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | ftype | 税则分类 | int8 | 64 |  | √ | 0 | [税务规则分类 ttc_tax_rules_type](../bastax_files/ttc_tax_rules_type.md) |
| 22 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fitemresult | 规则结果 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fdesc | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fcountry | 国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bastax_tax_rules_master |  | fmasterid |
| 2 | pk_bastax_tax_rules |  | fid |
| 3 | idx_t_bastax_tax_rules_createorg |  | fcreateorgid |

---

## 税务规则-多语言表 t_bastax_tax_rules_l

- **表名称：** 税务规则-多语言表
- **表名：** t_bastax_tax_rules_l

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
| 1 | idx_bastax_tax_rules_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_tax_rules_l |  | fpkid |

---

## 税务规则-使用范围表 t_bastax_tax_rules_u

- **表名称：** 税务规则-使用范围表
- **表名：** t_bastax_tax_rules_u

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
| 1 | idx_t_bastax_tax_rules_u_uo |  | fuseorgid |
| 2 | pk_t_bastax_tax_rules_u |  | fdataid,fuseorgid |

---

## 规则结果-子表 t_bastax_tax_rules_result

- **表名称：** 规则结果-子表
- **表名：** t_bastax_tax_rules_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forder | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftaxcodenumber | 税码编码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_tax_rules_result_fk |  | fid |
| 2 | pk_bastax_tax_rules_result |  | fentryid |

---

## 规则条件-子表 t_bastax_tax_rules_entry

- **表名称：** 规则条件-子表
- **表名：** t_bastax_tax_rules_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flink | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: AND :并且 |
| 3 | fentryclass | 税要素大类 | varchar | 50 |  | √ | ' ' | 税要素大类,枚举: bastax_addresstype :地址条件 ttc_quality_type :税务资质 bastax_taxproduct :税务产品 bastax_process_type :自定义税要素 |
| 4 | fvalueid | 值ID | varchar | 500 |  | √ | ' ' | 值ID |
| 5 | fvaluenumber | 值编码 | varchar | 500 |  | √ | ' ' | 值编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: = :等于 <> :不等于 in :在...中 not in :不在...中 >= :大于等于 <= :小于等于 > :大于 < :小于 |
| 8 | fentrytype | 税要素小类 | int8 | 64 |  | √ | 0 | 地址类型 bastax_addresstype |
| 9 | fvaluename | 值 | varchar | 500 |  | √ | ' ' | 值 |
| 10 | fadministrativelevel | 行政级次 | varchar | 50 |  | √ | ' ' | 行政级次,枚举: taxarea :税收区域 country :国家或地区 admindivision :行政区划 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_tax_rules_entry_fk |  | fid |
| 2 | pk_bastax_tax_rules_entry |  | fentryid |
