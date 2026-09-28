# 单据计税配置-bdtaxr_billtax_configs

## 交易方资质-子表 t_bastax_billtax_party

- **表名称：** 交易方资质-子表
- **表名：** t_bastax_billtax_party

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpartyconditionjson | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 3 | fbussinesstype | fbussinesstype | int8 | 64 |  | √ | 0 |  |
| 4 | fparty | 交易方资质 | int8 | 64 |  | √ | 0 | [交易方资质 bastax_party](../bastax_files/bastax_party.md) |
| 5 | fpartytype | 交易方类型 | int8 | 64 |  | √ | 0 | [交易方类型 ttc_quality_type](../bastax_files/ttc_quality_type.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpartyfield | 业务要素字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 8 | fpartycondition | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 9 | fbusiness | fbusiness | int8 | 64 |  | √ | 0 |  |
| 10 | fpartysource | 业务要素来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fpartysourcekey | 业务要素来源标识 | varchar | 100 |  | √ | ' ' | 业务要素来源标识 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fpartyfieldkey | 业务要素字段标识 | varchar | 50 |  | √ | ' ' | 业务要素字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_billtax_party |  | fentryid |
| 2 | idx_bastax_billtax_party_fk |  | fid |

---

## 单据计税配置-主表 t_bastax_billtax_configs

- **表名称：** 单据计税配置-主表
- **表名：** t_bastax_billtax_configs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftaxtation | ftaxtation | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcallbillkey | 调用单据key | varchar | 100 |  | √ | ' ' | 调用单据key |
| 9 | fcallbill | 调用单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fcallcondition | 调用条件 | varchar | 2000 |  | √ | ' ' | 调用条件 |
| 12 | fcallconditionjson | 调用条件json | varchar | 2000 |  | √ | ' ' | 调用条件json |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 24 | fcountry | 国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_billtax_configs |  | fnumber |
| 2 | pk_bastax_billtax_configs |  | fid |
| 3 | idx_t_bastax_billtax_configs_createorg |  | fcreateorgid |
| 4 | idx_t_bastax_billtax_configs_master |  | fmasterid |

---

## 自定义税要素-子表 t_bastax_billtax_element

- **表名称：** 自定义税要素-子表
- **表名：** t_bastax_billtax_element

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalueid | 值ID | varchar | 500 |  | √ | ' ' | 值ID |
| 3 | felementcondition | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 4 | fvaluenumber | 值编码 | varchar | 500 |  | √ | ' ' | 值编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprocesstype | 自定义税要素类型 | int8 | 64 |  | √ | 0 | [自定义税要素类型 bastax_process_type](../bastax_files/bastax_process_type.md) |
| 7 | felementfield | 业务要素字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 8 | fprocess | 自定义税要素(已废弃) | int8 | 64 |  | √ | 0 | [自定义税要素 bastax_process](../bastax_files/bastax_process.md) |
| 9 | felementsourcekey | 业务要素来源标识 | varchar | 100 |  | √ | ' ' | 业务要素来源标识 |
| 10 | felementsource | 业务要素来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | felementconditionjson | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 12 | felementfieldkey | 业务要素字段标识 | varchar | 50 |  | √ | ' ' | 业务要素字段标识 |
| 13 | fvaluename | 自定义税要素 | varchar | 500 |  | √ | ' ' | 自定义税要素 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_billtax_element_fk |  | fid |
| 2 | pk_bastax_billtax_element |  | fentryid |

---

## 特定产品-子表 t_bastax_billtax_specific

- **表名称：** 特定产品-子表
- **表名：** t_bastax_billtax_specific

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspecificsource | 业务要素来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | feuproduct | 欧盟特定产品 | varchar | 50 |  | √ | ' ' | 欧盟特定产品,枚举: 1 :是 0 :否 |
| 4 | fspecificproduct | 税务产品 | int8 | 64 |  | √ | 0 | [税务产品 bastax_taxproduct](../bastax_files/bastax_taxproduct.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fspecificfield | 业务要素字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 7 | fspecificcondition | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fspecificconditionjson | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 10 | fspecificsourcekey | 业务要素来源标识 | varchar | 120 |  | √ | ' ' | 业务要素来源标识 |
| 11 | fspecificfieldkey | 业务要素字段标识 | varchar | 120 |  | √ | ' ' | 业务要素字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_billtax_specific |  | fentryid |
| 2 | idx_bastax_billtax_specific_fk |  | fid |

---

## 单据计税配置-使用范围表 t_bastax_billtax_configs_u

- **表名称：** 单据计税配置-使用范围表
- **表名：** t_bastax_billtax_configs_u

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
| 1 | pk_t_bastax_billtax_configs_u |  | fdataid,fuseorgid |
| 2 | idx_t_bastax_billtax_configs_u_uo |  | fuseorgid |

---

## 单据计税配置-多语言表 t_bastax_billtax_configs_l

- **表名称：** 单据计税配置-多语言表
- **表名：** t_bastax_billtax_configs_l

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
| 1 | idx_bastax_billtax_configs_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_billtax_configs_l |  | fpkid |

---

## 地址条件-子表 t_bastax_billtax_address

- **表名称：** 地址条件-子表
- **表名：** t_bastax_billtax_address

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconditiontype | 地址条件类型 | int8 | 64 |  | √ | 0 | [地址类型 bastax_addresstype](../bastax_files/bastax_addresstype.md) |
| 3 | faddressfieldkey | 业务要素字段标识 | varchar | 100 |  | √ | ' ' | 业务要素字段标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | faddressfield | 业务要素字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 7 | faddresssource | 业务要素来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | faddresssourcekey | 业务要素来源标识 | varchar | 100 |  | √ | ' ' | 业务要素来源标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_billtax_address |  | fentryid |
| 2 | idx_bastax_billtax_address_fk |  | fid |

---

## 税务产品-子表 t_bastax_billtax_product

- **表名称：** 税务产品-子表
- **表名：** t_bastax_billtax_product

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductsource | 业务要素来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fproductsourcekey | 业务要素来源标识 | varchar | 100 |  | √ | ' ' | 业务要素来源标识 |
| 4 | fproductcondition | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 5 | fproductconditionjson | 转换条件 | varchar | 2000 |  | √ | ' ' | 转换条件 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fproductfield | 业务要素字段 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 8 | fproductfieldkey | 业务要素字段标识 | varchar | 100 |  | √ | ' ' | 业务要素字段标识 |
| 9 | fvaluerules | 值转换规则 | int8 | 64 |  | √ | 0 | [值转换规则 ttc_valuerules](../bastax_files/ttc_valuerules.md) |
| 10 | fproduct | 税务产品 | int8 | 64 |  | √ | 0 | [税务产品 bastax_taxproduct](../bastax_files/bastax_taxproduct.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fconverttype | 转换类型 | varchar | 50 |  | √ | ' ' | 转换类型,枚举: 1 :直接转换 2 :按规则转换 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_billtax_product_fk |  | fid |
| 2 | pk_bastax_billtax_product |  | fentryid |
