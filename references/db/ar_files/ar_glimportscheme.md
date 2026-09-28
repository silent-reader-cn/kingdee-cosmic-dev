# 从总账引入初始数据方案-ar_glimportscheme

## 曾用名列表-子表 t_ar_glimportschemenh

- **表名称：** 曾用名列表-子表
- **表名：** t_ar_glimportschemenh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fenable | 是否生效 | bpchar | 1 |  | √ | '1' | 是否生效 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ar_glimportschemenh |  | fentryid |
| 2 | idx_ar_glimportschemenh_fk |  | fid |

---

## 从总账引入初始数据方案-主表 t_ar_glimportscheme

- **表名称：** 从总账引入初始数据方案-主表
- **表名：** t_ar_glimportscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fappid | 应用AppId | varchar | 30 |  | √ | ' ' | 应用AppId,枚举: ar :应收 ap :应付 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 17 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 18 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ar_glimportscheme_createorg |  | fcreateorgid |
| 2 | idx_t_ar_glimportscheme_master |  | fmasterid |
| 3 | pk_t_ar_glimportscheme |  | fid |
| 4 | idx_ar_glimpt_number |  | fnumber |

---

## 映射信息-子表 t_ar_glimportschemeentry

- **表名称：** 映射信息-子表
- **表名：** t_ar_glimportschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmappingfield3 | 维度3映射字段 | varchar | 50 |  | √ | ' ' | 维度3映射字段 |
| 3 | fmappingfield2 | 维度2映射字段 | varchar | 50 |  | √ | ' ' | 维度2映射字段 |
| 4 | fmappingfield5 | 维度5映射字段 | varchar | 50 |  | √ | ' ' | 维度5映射字段 |
| 5 | fbalancemappingfield | 科目余额映射单据金额字段 | varchar | 50 |  | √ | ' ' | 科目余额映射单据金额字段 |
| 6 | fmappingfield4 | 维度4映射字段 | varchar | 50 |  | √ | ' ' | 维度4映射字段 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fmappingfield6 | 维度6映射字段 | varchar | 50 |  | √ | ' ' | 维度6映射字段 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :业务单元 |
| 11 | fentityobject | 引入对象 | varchar | 50 |  | √ | ' ' | 引入对象,枚举: |
| 12 | fbalancetype | 余额取值 | varchar | 30 |  | √ | ' ' | 余额取值,枚举: 1 :不为0 2 :大于0 3 :小于0 |
| 13 | fasstactitemid | 核算维度(往来) | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 14 | frectypeid | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 15 | fasstactitemid4 | 核算维度4 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 16 | fasstactitemid3 | 核算维度3 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fasstactitemid6 | 核算维度6 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 19 | fasstactitemid5 | 核算维度5 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 20 | fbalancedc | 单据金额方向取值 | varchar | 5 |  | √ | ' ' | 单据金额方向取值,枚举: 0 :按余额取值赋值 1 :按余额取值取反 |
| 21 | fasstactitemid2 | 核算维度2 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 22 | fasstactitemid1 | 核算维度1 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 23 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 24 | fbalancemappingfieldname | 科目余额映射单据金额 | varchar | 100 |  | √ | ' ' | 科目余额映射单据金额 |
| 25 | farpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | [应收款项性质 ar_payproperty](../ar_files/ar_payproperty.md) |
| 26 | fappaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | [应付款项性质 ap_payproperty](../ap_files/ap_payproperty.md) |
| 27 | fmappingfieldname3 | 维度3映射字段 | varchar | 100 |  | √ | ' ' | 维度3映射字段 |
| 28 | fmappingfieldname4 | 维度4映射字段 | varchar | 100 |  | √ | ' ' | 维度4映射字段 |
| 29 | fmappingfieldname1 | 维度1映射字段 | varchar | 100 |  | √ | ' ' | 维度1映射字段 |
| 30 | fpaymenttypeid | 付款类型 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 31 | fmappingfieldname2 | 维度2映射字段 | varchar | 100 |  | √ | ' ' | 维度2映射字段 |
| 32 | fmappingfieldname5 | 维度5映射字段 | varchar | 100 |  | √ | ' ' | 维度5映射字段 |
| 33 | fmappingfieldname6 | 维度6映射字段 | varchar | 100 |  | √ | ' ' | 维度6映射字段 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 36 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 37 | fmappingfield1 | 维度1映射字段 | varchar | 50 |  | √ | ' ' | 维度1映射字段 |
| 38 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_glimportschemeentry |  | fentryid |
| 2 | idx_ar_glimptentry_id |  | fid |

---

## 曾用名列表-多语言表 t_ar_glimportschemenh_l

- **表名称：** 曾用名列表-多语言表
- **表名：** t_ar_glimportschemenh_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_glimportschemenh_l_0 |  | fentryid,flocaleid |
| 2 | pk_ar_glimportschemenh_l |  | fpkid |

---

## 从总账引入初始数据方案-使用范围位图表 t_ar_glimportscheme_m

- **表名称：** 从总账引入初始数据方案-使用范围位图表
- **表名：** t_ar_glimportscheme_m

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
| 1 | pk_t_ar_glimportscheme_m |  | forgid |

---

## 从总账引入初始数据方案-使用范围表 t_ar_glimportscheme_u

- **表名称：** 从总账引入初始数据方案-使用范围表
- **表名：** t_ar_glimportscheme_u

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
| 1 | pk_t_ar_glimportscheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_ar_glimportscheme_u_uo |  | fuseorgid |

---

## 从总账引入初始数据方案-多语言表 t_ar_glimportscheme_l

- **表名称：** 从总账引入初始数据方案-多语言表
- **表名：** t_ar_glimportscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_glimportscheme_l |  | fpkid |
| 2 | idx_ar_glimpt_l_fid |  | fid,flocaleid |
