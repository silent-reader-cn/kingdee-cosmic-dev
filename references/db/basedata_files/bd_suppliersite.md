# 供应商地点-bd_suppliersite

## 供应商地点-主表 t_bd_suppliersite

- **表名称：** 供应商地点-主表
- **表名：** t_bd_suppliersite

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 业务地址 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 3 | flogo |  | varchar | 255 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fpriceclause | 价格条款 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | finvoiceaddress | 收票地址 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 9 | fbilladdress | 开票地址 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 10 | finvoicecategory | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsupmasterid | 供应商masterid | varchar | 100 |  | √ | ' ' | 供应商masterid |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | ftaxrateid | 默认税率(%) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | freighttype | 货运方式 | varchar | 30 |  | √ | ' ' | 货运方式,枚举: 1 :送货 2 :自提 |
| 20 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 24 | fpaymentunit | 支付周期 | varchar | 30 |  | √ | ' ' | 支付周期,枚举: 1 :日 2 :周 3 :月 |
| 25 | fmatchingrule | 发票匹配规则 | varchar | 30 |  | √ | ' ' | 发票匹配规则,枚举: two :匹配订单（2重匹配） three :匹配接收（3重匹配） four :匹配验收（4重匹配） |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fbizfunction | 业务职能 | varchar | 20 |  | √ | ' ' | 业务职能,枚举: 1 :采购 2 :付款 |
| 28 | freceiveraddress | 收货地址 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 29 | fscstype | SCS类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 30 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fpaymentcondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 32 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 33 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 34 | finvoicetype | 发票类型（已失效） | bpchar | 1 |  | √ | '0' | 发票类型（已失效）,枚举: 1 :增值税专用发票 2 :普通发票 |
| 35 | fsettlementcyid | 交易币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 36 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 38 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 40 | fpaymentcurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fratetype | 汇率类型 | varchar | 30 |  | √ | ' ' | 汇率类型,枚举: 1 :即期 2 :公司 3 :用户定义 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_suppliersite_master |  | fmasterid |
| 2 | idx_t_bd_suppliersite_createorg |  | fcreateorgid |
| 3 | t_bd_suppliersite_pkey |  | fid |
| 4 | idx_t_bd_suppliersite_number |  | fnumber |

---

## 供应商地点-多语言表 t_bd_suppliersite_l

- **表名称：** 供应商地点-多语言表
- **表名：** t_bd_suppliersite_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_suppliersite_l_pkey |  | fpkid |
| 2 | idx_t_bd_suppliersite_l_fid |  | fid,flocaleid |

---

## 供应商地点-使用范围位图表 t_bd_suppliersite_m

- **表名称：** 供应商地点-使用范围位图表
- **表名：** t_bd_suppliersite_m

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
| 1 | pk_t_bd_suppliersite_m |  | forgid |

---

## 供应商地点-使用范围表 t_bd_suppliersite_u

- **表名称：** 供应商地点-使用范围表
- **表名：** t_bd_suppliersite_u

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
| 1 | t_bd_suppliersite_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_suppliersite_u_uo |  | fuseorgid |

---

## 银行信息分录-多语言表 t_bd_suppliersitebank_l

- **表名称：** 银行信息分录-多语言表
- **表名：** t_bd_suppliersitebank_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supplierstiebank_l_entr |  | fentryid,flocaleid |
| 2 | t_bd_suppliersitebank_l_pkey |  | fpkid |

---

## 银行信息分录-子表 t_bd_suppliersitebank

- **表名称：** 银行信息分录-子表
- **表名：** t_bd_suppliersitebank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 3 | fbankaccounttype | 银行账户类型 | varchar | 120 |  | √ | ' ' | 银行账户类型,枚举: |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbankaccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 6 | fcommissionbearer | 默认手续费承担方 | varchar | 30 |  | √ | ' ' | 默认手续费承担方,枚举: 1 :付款方 2 :收款方 |
| 7 | fagentbankaccount | 代理行账号 | varchar | 80 |  | √ | ' ' | 代理行账号 |
| 8 | fsettlment | 默认结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 9 | fliquidationparam | 默认清算要求参数 | varchar | 125 |  | √ | ' ' | 默认清算要求参数 |
| 10 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fagentbank | 默认代理行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 14 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_suppliersitebank_pkey |  | fentryid |
| 2 | idx_bd_suppliersitebank_supp |  | fid |
