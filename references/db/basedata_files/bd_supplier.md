# 供应商-bd_supplier

## 联系人分录-多语言表 t_bd_supplierlinkman_l

- **表名称：** 联系人分录-多语言表
- **表名：** t_bd_supplierlinkman_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdept | 部门 | varchar | 80 |  |  | null | 部门 |
| 2 | fcontactperson | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  |  | null |  |
| 6 | fcontactpersonpost | 职务 | varchar | 60 |  |  | null | 职务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_supplierlinkman_l_pkey |  | fpkid |
| 2 | idx_bd_supplinkman_l_entry |  | fentryid,flocaleid |

---

## 曾用名称信息-子表 t_bd_supplierrecord

- **表名称：** 曾用名称信息-子表
- **表名：** t_bd_supplierrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpirytime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fstate | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态 |
| 4 | feffectime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 5 | foriginator | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fformername | 曾用名 | varchar | 255 |  | √ | ' ' | 曾用名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_supplierrecord |  | fentryid |
| 2 | idx_bd_supplierrecord_id |  | fid |

---

## 供应商-多语言表 t_bd_supplier_l

- **表名称：** 供应商-多语言表
- **表名：** t_bd_supplier_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fbusinessscope | 经营范围 | varchar | 2000 |  | √ | ' ' | 经营范围 |
| 3 | fname | 名称 | varchar | 255 |  |  | null | 名称 |
| 4 | faddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 5 | fsimplename | 简称 | varchar | 255 |  |  | null | 简称 |
| 6 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 7 | fbusinessterm | 营业期限 | varchar | 60 |  | √ | ' ' | 营业期限 |
| 8 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 9 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 11 | fregcapital | 注册资本 | varchar | 40 |  | √ | ' ' | 注册资本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_supplier_l_fid |  | fid,flocaleid |
| 2 | t_bd_supplier_l_pkey |  | fpkid |
| 3 | idx_bd_supplier_l_name |  | fname |

---

## 供应商-使用范围位图表 t_bd_supplier_m

- **表名称：** 供应商-使用范围位图表
- **表名：** t_bd_supplier_m

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
| 1 | pk_t_bd_supplier_m |  | forgid |

---

## 供应商-分表 t_bd_supplier_b

- **表名称：** 供应商-分表
- **表名：** t_bd_supplier_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | 联系电话 | varchar | 60 |  | √ | ' ' | 联系电话 |
| 3 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 4 | forgcode | 组织机构代码(已废弃) | varchar | 255 |  | √ | ' ' | 组织机构代码(已废弃) |
| 5 | fspsupplier | 简易供应商标识 | bpchar | 1 |  | √ | '0' | 简易供应商标识 |
| 6 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 7 | fcuregcapital | 注册资本币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | fidno | 身份证号 | varchar | 50 |  | √ | ' ' | 身份证号 |
| 9 | fduns | 邓白氏编码 | varchar | 9 |  | √ | ' ' | 邓白氏编码 |
| 10 | fpostalcode | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 11 | finternalcompanyid | 内部业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | festablishdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 13 | ffax | 传真 | varchar | 40 |  | √ | ' ' | 传真 |
| 14 | fexpirydate | 失效日期（废弃） | timestamp | 0 |  |  | null | 失效日期（废弃） |
| 15 | furl | 公司网址 | varchar | 255 |  | √ | ' ' | 公司网址 |
| 16 | fbizregisterno | 工商登记号(已废弃) | varchar | 255 |  | √ | ' ' | 工商登记号(已废弃) |
| 17 | fadmindivision | 行政区划 | varchar | 100 |  | √ | ' ' | 行政区划 |
| 18 | ftxregisterno | 纳税人识别号 | varchar | 255 |  | √ | ' ' | 纳税人识别号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | dx_t_bd_supplie_bl_orgstrat |  | finternalcompanyid |
| 2 | dx_t_bd_supplie_b_idno |  | fidno |
| 3 | t_bd_supplier_b_pkey |  | fid |

---

## 银行信息分录-多语言表 t_bd_supplierbank_l

- **表名称：** 银行信息分录-多语言表
- **表名：** t_bd_supplierbank_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 2 | fbank | fbank | varchar | 80 |  |  | null |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpayeeaddress | 收款方详细地址 | varchar | 300 |  | √ | ' ' | 收款方详细地址 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supplierbank_l_entry |  | fentryid,flocaleid |
| 2 | t_bd_supplierbank_l_pkey |  | fpkid |

---

## 供应商-使用范围表 t_bd_supplier_u

- **表名称：** 供应商-使用范围表
- **表名：** t_bd_supplier_u

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
| 1 | t_bd_supplier_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_supplier_u_uo |  | fuseorgid |

---

## 供应商-主表 t_bd_supplier

- **表名称：** 供应商-主表
- **表名：** t_bd_supplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fgroupid | 供应商分组 | int8 | 64 |  |  | null | 供应商分类 bd_suppliergroup |
| 4 | fdeliversupplierid | 供货供应商 | int8 | 64 |  |  | null | 供应商 bd_supplier |
| 5 | faddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 6 | forgid | 使用组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | feffectivedt | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fblocsupplier | 所属集团 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fbilladdress | 开票地址 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 12 | finvoicecategory | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fpayhold | 付款冻结 | bpchar | 1 |  | √ | '0' | 付款冻结 |
| 15 | fbusinessscope | 经营范围 | varchar | 2000 |  | √ | ' ' | 经营范围 |
| 16 | fenablevmi | 可VMI | bpchar | 1 |  | √ | '0' | 可VMI |
| 17 | finvoicesupplierid | 结算供应商 | int8 | 64 |  |  | null | 供应商 bd_supplier |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | ftaxno | 税号 | varchar | 60 |  | √ | ' ' | 税号 |
| 20 | freceivingsupplierid | 收款供应商 | int8 | 64 |  |  | null | 供应商 bd_supplier |
| 21 | fpuroperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 22 | fpurdepartid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 24 | fbizfunction | 业务职能 | varchar | 20 |  | √ | ' ' | 业务职能,枚举: 1 :采购 2 :结算 3 :收款 4 :供货 |
| 25 | finvoicehold | 发票冻结 | bpchar | 1 |  | √ | '0' | 发票冻结 |
| 26 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | 人员 bos_user |
| 27 | fpaymentcondid | 付款条件 | int8 | 64 |  |  | null | 付款条件 bd_paycondition |
| 28 | fmallstatus | 商城入驻状态 | varchar | 10 |  |  | null | 商城入驻状态,枚举: A :未入驻 B :已入驻 C :已冻结 D :已终止 |
| 29 | fsimplepinyin | 简拼 | varchar | 255 |  | √ | ' ' | 简拼 |
| 30 | finvoicetype | 发票类型(已失效) | bpchar | 1 |  | √ | '0' | 发票类型(已失效),枚举: 1 :增值税专用发票 2 :普通发票 |
| 31 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 33 | fbusinessterm | 营业期限 | varchar | 60 |  | √ | ' ' | 营业期限 |
| 34 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 35 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 36 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 37 | fpaymentcurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fpurchaserid | 负责人 | int8 | 64 |  |  | null | 人员 bos_user |
| 39 | flogo | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 40 | fsupplierstatus | 供应商状态 | int8 | 64 |  | √ | 0 | 供应商状态 bd_supplierstatus |
| 41 | fpurchasedeptid | 负责组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 42 | fexpirydt | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 43 | finvoiceaddress | 收票地址 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 44 | fstatus | 数据状态 | varchar | 30 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 46 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 47 | fblocflag | 集团供应商 | bpchar | 1 |  | √ | '0' | 集团供应商 |
| 48 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 49 | ftaxrateid | 默认税率(%) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 50 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 51 | fsettlementtypeid | 结算方式 | int8 | 64 |  |  | null | 结算方式 bd_settlementtype |
| 52 | ftaxtype | 计税类型 | varchar | 10 |  |  | null | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 53 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 54 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 55 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 56 | fpaymentunit | 支付周期 | varchar | 30 |  | √ | ' ' | 支付周期,枚举: 1 :日 2 :周 3 :月 |
| 57 | fmatchingrule | 发票匹配规则 | varchar | 30 |  | √ | ' ' | 发票匹配规则,枚举: two :匹配订单（2重匹配） three :匹配接收（3重匹配） four :匹配验收（4重匹配） |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | fmalldate | 商城入驻时间 | timestamp | 0 |  |  | null | 商城入驻时间 |
| 60 | ftaxregistplace | 税务注册地 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 61 | fbizpartnerid | 商务伙伴 | int8 | 64 |  |  | null | 商务伙伴 bd_bizpartner |
| 62 | fregcapital | 注册资本 | varchar | 40 |  | √ | ' ' | 注册资本 |
| 63 | fctrlstrategy | 控制策略 | varchar | 10 |  |  | null | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 64 | ftype | 伙伴类型 | varchar | 30 |  | √ | ' ' | 伙伴类型,枚举: 1 :法人企业 2 :非法人企业 3 :非企业单位 4 :个人 5 :个体户 |
| 65 | femployee | 员工 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 66 | fpurchasehold | 采购冻结 | bpchar | 1 |  | √ | '0' | 采购冻结 |
| 67 | fadminorgid | 管理组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 68 | fsimplename | 简称 | varchar | 255 |  | √ | ' ' | 简称 |
| 69 | fsettlementcyid | 交易币别 | int8 | 64 |  |  | null | 币种 bd_currency |
| 70 | fissuppcolla | 启用采购协同 | bpchar | 1 |  |  | null | 启用采购协同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_supplierbit |  | fbitindex |
| 2 | idx_t_bd_supplier_masterid |  | fmasterid |
| 3 | idx_t_bd_supplier_type |  | ftype |
| 4 | idx_t_bd_suppliersrcid |  | fsourcedataid |
| 5 | idx_t_bd_supplier_number |  | fnumber |
| 6 | idx_t_bd_supplier_orgstrat |  | fctrlstrategy,forgid |
| 7 | t_bd_supplier_pkey |  | fid |
| 8 | idx_t_bd_supplier_group |  | fgroupid |
| 9 | idx_t_bd_supplier_master |  | fmasterid |
| 10 | idx_t_bd_supplier_sp |  | fsimplepinyin |
| 11 | idx_t_bd_supplier_bizpt |  | fbizpartnerid |
| 12 | idx_t_bd_supplier_ecsss |  | fenable,fsupplierstatus,fstatus |
| 13 | idx_t_bd_supplier_createorg |  | fcreateorgid |

---

## 税务资质-子表 t_bd_suppliertax

- **表名称：** 税务资质-子表
- **表名：** t_bd_suppliertax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxcertificate | 税务资质 | int8 | 64 |  | √ | 0 | 税务资质 bd_taxaptitudes |
| 3 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 4 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_suppliertax |  | fentryid |
| 2 | idx_t_bd_suppliertax_fid |  | fid |

---

## 曾用名称信息-多语言表 t_bd_supplierrecord_l

- **表名称：** 曾用名称信息-多语言表
- **表名：** t_bd_supplierrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fformername | 曾用名 | varchar | 255 |  | √ | ' ' | 曾用名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supplierrecord_lang |  | fentryid,flocaleid |
| 2 | pk_t_bd_supplierrecord_l |  | fpkid |

---

## 联系人分录-子表 t_bd_supplierlinkman

- **表名称：** 联系人分录-子表
- **表名：** t_bd_supplierlinkman

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fphone | 联系电话 | varchar | 255 |  | √ | ' ' | 联系电话 |
| 3 | faddress | 地址(已废弃) | varchar | 100 |  |  | null | 地址(已废弃) |
| 4 | fgivenname | 名 | varchar | 150 |  | √ | ' ' | 名 |
| 5 | fgender | fgender | int8 | 64 |  |  | null |  |
| 6 | femail | 邮箱 | varchar | 255 |  | √ | ' ' | 邮箱 |
| 7 | fdept | 部门 | varchar | 80 |  | √ | ' ' | 部门 |
| 8 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 9 | fassociatedaddress | 关联地址 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 10 | faddresspurpose | faddresspurpose | int8 | 64 |  | √ | 0 |  |
| 11 | fmobile | 手机(已废弃) | varchar | 40 |  |  | null | 手机(已废弃) |
| 12 | frole | 角色 | varchar | 30 |  | √ | ' ' | 角色,枚举: 1 :业务 2 :财务 |
| 13 | fmiddlename | 中间名 | varchar | 150 |  | √ | ' ' | 中间名 |
| 14 | fpostalcode | 邮政编码(已废弃) | varchar | 10 |  |  | null | 邮政编码(已废弃) |
| 15 | ffamilyname | 姓 | varchar | 150 |  | √ | ' ' | 姓 |
| 16 | finvalid | 失效 | bpchar | 1 |  | √ | '0' | 失效 |
| 17 | ffax | 传真 | varchar | 40 |  |  | null | 传真 |
| 18 | fcontactperson | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 20 | falias | 别名 | varchar | 150 |  | √ | ' ' | 别名 |
| 21 | fisdefault | 默认 | bpchar | 1 |  |  | null | 默认 |
| 22 | fcontactpersonpost | 职务 | varchar | 60 |  | √ | ' ' | 职务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_supplierlinkman_pkey |  | fentryid |
| 2 | idx_bd_supplinkman_supp |  | fid |

---

## 关联子实体-子表 t_bd_supplier_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bd_supplier_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_supplier_lk_pkey |  | fpkid |

---

## 银行信息分录-子表 t_bd_supplierbank

- **表名称：** 银行信息分录-子表
- **表名：** t_bd_supplierbank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fapproverid | fapproverid | int8 | 64 |  |  | null |  |
| 3 | forgid | forgid | int8 | 64 |  |  | null |  |
| 4 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fbankaccount | 银行账号 | varchar | 80 |  |  | null | 银行账号 |
| 7 | fcommissionbearer | 默认手续费承担方 | varchar | 30 |  | √ | ' ' | 默认手续费承担方,枚举: 1 :付款方 2 :收款方 |
| 8 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 10 | fsettlment | 默认结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 11 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 12 | fliquidationparam | 默认清算要求参数 | varchar | 125 |  | √ | ' ' | 默认清算要求参数 |
| 13 | fpayeeadmindivision | 收款方行政区划 | varchar | 50 |  | √ | ' ' | 收款方行政区划 |
| 14 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 16 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 17 | fbankaccounttype | 银行账户类型 | varchar | 120 |  | √ | ' ' | 银行账户类型,枚举: |
| 18 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 19 | fpayeeaddress | 收款方详细地址 | varchar | 300 |  | √ | ' ' | 收款方详细地址 |
| 20 | fpayeephone | 收款方联系电话 | varchar | 100 |  | √ | ' ' | 收款方联系电话 |
| 21 | fagentbankaccount | 代理行账号 | varchar | 80 |  | √ | ' ' | 代理行账号 |
| 22 | fadminorgid | fadminorgid | int8 | 64 |  |  | null |  |
| 23 | fdisablestatus | fdisablestatus | bpchar | 1 |  |  | null |  |
| 24 | fbankid | 开户银行 | int8 | 64 |  |  | null | 行名行号 bd_bebank |
| 25 | fibanid | 国际银行账户号码 | varchar | 50 |  | √ | ' ' | 国际银行账户号码 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 27 | fcurrencyid | 币别 | int8 | 64 |  |  | null | 币种 bd_currency |
| 28 | fisdefault | 默认 | bpchar | 1 |  |  | null | 默认 |
| 29 | fagentbank | 默认代理行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supplierbank_supp |  | fid |
| 2 | t_bd_supplierbank_pkey |  | fentryid |
