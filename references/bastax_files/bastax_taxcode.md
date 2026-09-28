# 税码-bastax_taxcode

## 税码-主表 t_bastax_taxcode

- **表名称：** 税码-主表
- **表名：** t_bastax_taxcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | ftaxcodetype | 税码分类 | int8 | 64 |  | √ | 0 | 税码分类 bastax_taxcode_type |
| 7 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fimpactcost | 影响成本 | bpchar | 1 |  | √ | ' ' | 影响成本 |
| 16 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 17 | ftaxcodeproperty | 税码属性 | varchar | 50 |  | √ | ' ' | 税码属性,枚举: jx :进项 xx :销项 qt :其他 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fcontainstax | 含税标识 | bpchar | 1 |  | √ | ' ' | 含税标识 |
| 22 | foffsetlogo | 扣减结算 | bpchar | 1 |  | √ | ' ' | 扣减结算 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 25 | foffsettax | 是否流转税 | bpchar | 1 |  | √ | ' ' | 是否流转税 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fdeductible | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fcountry | 国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bastax_taxcode_createorg |  | fcreateorgid |
| 2 | idx_bastax_taxcode |  | forgid |
| 3 | idx_t_bastax_taxcode_master |  | fmasterid |
| 4 | pk_bastax_taxcode |  | fid |

---

## 税码-使用范围表 t_bastax_taxcode_u

- **表名称：** 税码-使用范围表
- **表名：** t_bastax_taxcode_u

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
| 1 | pk_t_bastax_taxcode_u |  | fdataid,fuseorgid |
| 2 | idx_t_bastax_taxcode_u_uo |  | fuseorgid |

---

## 税码明细-子表 t_bastax_taxcode_details

- **表名称：** 税码明细-子表
- **表名：** t_bastax_taxcode_details

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaluesource | 值来源 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fvaluedecimal | 值小数(废弃) | numeric | 23 | 10 | √ | 0 | 值小数(废弃) |
| 4 | fvalueid | 值id | varchar | 200 |  | √ | ' ' | 值id |
| 5 | fvaluenumber | 值 | varchar | 300 |  | √ | ' ' | 值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fresult | 税码明细类型 | int8 | 64 |  | √ | 0 | 税码明细结果类型 bastax_code_detailstype |
| 8 | fvaluetype | 值类型 | varchar | 50 |  | √ | ' ' | 值类型,枚举: 0 :系统预设 1 :数值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdecimalprecision | 小数精度(废弃) | int8 | 64 |  | √ | 0 | 小数精度(废弃) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_taxcode_details |  | fentryid |
| 2 | idx_bastax_taxcode_details_fk |  | fid |

---

## 税码-多语言表 t_bastax_taxcode_l

- **表名称：** 税码-多语言表
- **表名：** t_bastax_taxcode_l

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
| 1 | idx_bastax_taxcode_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_taxcode_l |  | fpkid |

---

## 税码-使用范围位图表 t_bastax_taxcode_m

- **表名称：** 税码-使用范围位图表
- **表名：** t_bastax_taxcode_m

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
| 1 | pk_t_bastax_taxcode_m |  | forgid |

---

## 税率表-子表 t_bastax_taxcode_taxrate

- **表名称：** 税率表-子表
- **表名：** t_bastax_taxcode_taxrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_taxcode_taxrate |  | fentryid |
| 2 | idx_bastax_taxcode_taxrate_fk |  | fid |
