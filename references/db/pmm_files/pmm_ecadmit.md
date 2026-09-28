# 电商授权-pmm_ecadmit

## 电商授权-多语言表 t_mal_ecadmit_l

- **表名称：** 电商授权-多语言表
- **表名：** t_mal_ecadmit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
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
| 1 | idx_mal_ecadmit_l_fid |  | fid,flocaleid |
| 2 | t_mal_ecadmit_l_pkey |  | fpkid |

---

## 电商授权-使用范围位图表 t_mal_ecadmit_m

- **表名称：** 电商授权-使用范围位图表
- **表名：** t_mal_ecadmit_m

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
| 1 | pk_t_mal_ecadmit_m |  | forgid |

---

## 电商授权-使用范围表 t_mal_ecadmit_u

- **表名称：** 电商授权-使用范围表
- **表名：** t_mal_ecadmit_u

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
| 1 | idx_t_mal_ecadmit_u_uo |  | fuseorgid |
| 2 | t_mal_ecadmit_u_pkey |  | fdataid,fuseorgid |

---

## 单据体-子表 t_mal_ecadmitentry

- **表名称：** 单据体-子表
- **表名：** t_mal_ecadmitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvatid | fvatid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | finvoiceorg | 发票抬头 | varchar | 100 |  | √ | ' ' | 发票抬头 |
| 5 | fmallpwd | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 6 | frcvorg | 默认收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcompanyorg | 授权核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | ftoken | token | varchar | 100 |  | √ | ' ' | token |
| 9 | funeffectualdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fquasynstatus | fquasynstatus | bpchar | 1 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fpurorg | 默认采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fmallaccount | 平台账号 | varchar | 100 |  | √ | ' ' | 平台账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_ecadmitentry_pkey |  | fentryid |
| 2 | idx_mal_ecadmitentry_fid |  | fid |

---

## 电商授权-主表 t_mal_ecadmit

- **表名称：** 电商授权-主表
- **表名：** t_mal_ecadmit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 对应采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | ftenantid | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fmesureunitsid | 指定电商计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fopenstatus | 开通状态 | bpchar | 1 |  | √ | ' ' | 开通状态,枚举: 1 :待开通 2 :运行中 3 :已停用 4 :初始化中 5 :初始化失败 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 20 | finvoicetypeid | 默认发票类型 | int8 | 64 |  | √ | 0 | 发票类型 pbd_invoicetype |
| 21 | fclient_secret | 秘钥 | varchar | 50 |  | √ | ' ' | 秘钥 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fproxy | 代理配置 | varchar | 255 |  | √ | ' ' | 代理配置 |
| 24 | finvoiceorg | 开票机构码 | varchar | 50 |  | √ | ' ' | 开票机构码 |
| 25 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fclient_id | ClientID | varchar | 50 |  | √ | ' ' | ClientID |
| 28 | fmalsupplierid | 指定电商供应商 | int8 | 64 |  | √ | 0 | 商城供应商 bd_malsupplier |
| 29 | femalemail | 指定电商邮箱 | varchar | 80 |  | √ | ' ' | 指定电商邮箱 |
| 30 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fpaytypeid | 默认支付方式 | int8 | 64 |  | √ | 0 | 商城支付方式 pbd_paytype |
| 32 | finitconfigid | 电商初始化配置 | int8 | 64 |  | √ | 0 | 电商初始化配置 pmm_initconfig |
| 33 | fstandardid | 电商分类标准 | int8 | 64 |  | √ | 0 | 商品分类标准 bd_goodsclassstandard |
| 34 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 36 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fskunum | SKU数量限制 | int4 | 32 |  | √ | 0 | SKU数量限制 |
| 38 | fcurrencyid | 指定电商人民币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_ecadmit_pkey |  | fid |
| 2 | idx_mal_ecadmit_fmasterid |  | fmasterid |
| 3 | idx_t_mal_ecadmit_master |  | fmasterid |
| 4 | idx_mal_ecadmit_fnumber |  | fnumber |
| 5 | idx_t_mal_ecadmit_createorg |  | fcreateorgid |
