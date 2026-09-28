# 客户-bd_customer

## 曾用名称信息-子表 t_bd_customerrecord

- **表名称：** 曾用名称信息-子表
- **表名：** t_bd_customerrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpirytime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fstate | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态 |
| 4 | feffectime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 5 | foriginator | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 1 | idx_bd_customerrecord_id |  | fid |
| 2 | pk_t_bd_customerrecord |  | fentryid |

---

## 税务资质-子表 t_bd_customertax

- **表名称：** 税务资质-子表
- **表名：** t_bd_customertax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxcertificate | 税务资质 | int8 | 64 |  | √ | 0 | [税务资质 bd_taxaptitudes](../basedata_files/bd_taxaptitudes.md) |
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
| 1 | pk_t_bd_customertax |  | fentryid |
| 2 | idx_t_bd_customertax_fid |  | fid |

---

## 曾用名称信息-多语言表 t_bd_customerrecord_l

- **表名称：** 曾用名称信息-多语言表
- **表名：** t_bd_customerrecord_l

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
| 1 | pk_t_bd_customerrecord_l |  | fpkid |
| 2 | idx_bd_customerrecord_lang |  | fentryid,flocaleid |

---

## 联系人信息-多语言表 t_bd_customerlinkman_l

- **表名称：** 联系人信息-多语言表
- **表名：** t_bd_customerlinkman_l

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
| 1 | t_bd_customerlinkman_l_pkey |  | fpkid |
| 2 | idx_bd_custlinkman_l_entry |  | fentryid,flocaleid |

---

## 客户-使用范围表 t_bd_customer_u

- **表名称：** 客户-使用范围表
- **表名：** t_bd_customer_u

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
| 1 | t_bd_customer_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_customer_u_uo |  | fuseorgid |

---

## 银行信息-子表 t_bd_customerbank

- **表名称：** 银行信息-子表
- **表名：** t_bd_customerbank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fapproverid | fapproverid | int8 | 64 |  |  | null |  |
| 3 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 5 | forgid | forgid | int8 | 64 |  |  | null |  |
| 6 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 8 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 9 | fbankaccount | 银行账号 | varchar | 80 |  |  | null | 银行账号 |
| 10 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 11 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | fadminorgid | fadminorgid | int8 | 64 |  |  | null |  |
| 15 | fdisablestatus | fdisablestatus | bpchar | 1 |  |  | null |  |
| 16 | fbankid | 开户银行 | int8 | 64 |  |  | null | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 17 | fibanid | 国际银行账户号码 | varchar | 50 |  | √ | ' ' | 国际银行账户号码 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 19 | fcurrencyid | 币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fisdefault | 默认 | bpchar | 1 |  |  | null | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_customerbank_pkey |  | fentryid |
| 2 | idx_bd_customerbank_cust |  | fid |

---

## 客户-分表 t_bd_customer_b

- **表名称：** 客户-分表
- **表名：** t_bd_customer_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | 联系电话 | varchar | 255 |  | √ | ' ' | 联系电话 |
| 3 | fk_bj73_basedatafield | 一级架构.名称 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 4 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 5 | forgcode | 组织机构代码(已废弃) | varchar | 255 |  | √ | ' ' | 组织机构代码(已废弃) |
| 6 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 7 | fcuregcapital | 注册资本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fidno | 身份证号 | varchar | 50 |  | √ | ' ' | 身份证号 |
| 9 | fk_bj73_textfield2 | fk_bj73_textfield2 | varchar | 50 |  | √ | ' ' |  |
| 10 | fk_bj73_textfield1 | 物流备注 | varchar | 200 |  | √ | ' ' | 物流备注 |
| 11 | fduns | 邓白氏编码 | varchar | 9 |  | √ | ' ' | 邓白氏编码 |
| 12 | fpostalcode | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 13 | finternalcompanyid | 内部业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | festablishdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 15 | ffax | 传真 | varchar | 40 |  | √ | ' ' | 传真 |
| 16 | furl | 公司网址 | varchar | 255 |  | √ | ' ' | 公司网址 |
| 17 | fadmindivision | 行政区划 | varchar | 100 |  | √ | ' ' | 行政区划 |
| 18 | fbizregisterno | 工商登记号(已废弃) | varchar | 255 |  | √ | ' ' | 工商登记号(已废弃) |
| 19 | ftxregisterno | 纳税人识别号 | varchar | 255 |  | √ | ' ' | 纳税人识别号 |
| 20 | fk_bj73_assistantfield6 | 业态场景 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_bd_customer_b_idno |  | fidno |
| 2 | t_bd_customer_b_pkey |  | fid |
| 3 | index_bd_customer_internal_com |  | finternalcompanyid |

---

## 客户-使用范围位图表 t_bd_customer_m

- **表名称：** 客户-使用范围位图表
- **表名：** t_bd_customer_m

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
| 1 | pk_t_bd_customer_m |  | forgid |

---

## 客户-多语言表 t_bd_customer_l

- **表名称：** 客户-多语言表
- **表名：** t_bd_customer_l

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
| 8 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 9 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 11 | fregcapital | 注册资本 | varchar | 40 |  | √ | ' ' | 注册资本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_customer_l_name |  | fname |
| 2 | idx_t_bd_customer_l_fid |  | fid,flocaleid |
| 3 | t_bd_customer_l_pkey |  | fpkid |

---

## 联系人信息-子表 t_bd_customerlinkman

- **表名称：** 联系人信息-子表
- **表名：** t_bd_customerlinkman

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fphone | 固定电话 | varchar | 255 |  | √ | ' ' | 固定电话 |
| 3 | faddress | 地址(已废弃) | varchar | 100 |  |  | null | 地址(已废弃) |
| 4 | fgivenname | 名 | varchar | 150 |  | √ | ' ' | 名 |
| 5 | fgender | 性别(已废弃) | varchar | 50 |  |  | null | 性别(已废弃),枚举: 1 :男 2 :女 |
| 6 | femail | 邮箱 | varchar | 255 |  | √ | ' ' | 邮箱 |
| 7 | fdept | 部门 | varchar | 80 |  | √ | ' ' | 部门 |
| 8 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 9 | fassociatedaddress | 关联地址 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 10 | faddresspurpose | faddresspurpose | int8 | 64 |  | √ | 0 |  |
| 11 | fmobile | 手机(已废弃) | varchar | 40 |  |  | null | 手机(已废弃) |
| 12 | frole | 角色 | varchar | 30 |  | √ | ' ' | 角色,枚举: 1 :业务 2 :财务 3 :发票 |
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
| 23 | fcellphone | 移动电话 | varchar | 50 |  | √ | ' ' | 移动电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_customerlinkman_pkey |  | fentryid |
| 2 | idx_bd_custlinkman_cust |  | fid |

---

## 关联子实体-子表 t_bd_customer_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bd_customer_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_customer_lk |  | fpkid |
| 2 | idx_bd_customer_lk_fk |  | fid |

---

## 银行信息-多语言表 t_bd_customerbank_l

- **表名称：** 银行信息-多语言表
- **表名：** t_bd_customerbank_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 2 | fbank | fbank | varchar | 80 |  |  | null |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_customerbank_l_entry |  | fentryid,flocaleid |
| 2 | t_bd_customerbank_l_pkey |  | fpkid |

---

## 客户-主表 t_bd_customer

- **表名称：** 客户-主表
- **表名：** t_bd_customer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fsaldeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 管理组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | freceivingcondid | 收款条件 | int8 | 64 |  |  | null | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | feffectivedt | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | finvoicecategory | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbusinessscope | 经营范围 | varchar | 2000 |  | √ | ' ' | 经营范围 |
| 10 | fpaymentcustomerid | 付款客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 11 | fdelivercustomerid | 收货客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 12 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 13 | freservedays | 预留天数 | int8 | 64 |  | √ | 0 | 预留天数 |
| 14 | finvoicehold | 发票冻结 | bpchar | 1 |  | √ | '0' | 发票冻结 |
| 15 | fsaloperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 16 | fk_bj73_assistantfield1 | 考核大区 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 17 | fk_bj73_assistantfield2 | 考核省区 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 18 | fk_bj73_assistantfield3 | 价格类型 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 19 | fk_bj73_assistantfield4 | B端属性 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 20 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 22 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 23 | fk_bj73_assistantfield5 | C端属性 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fk_bj73_assistantfield6 | fk_bj73_assistantfield6 | int8 | 64 |  | √ | 0 |  |
| 26 | fpaymentcurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fsaledeptid | 负责组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fexpirydt | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 29 | fk_bj73_radiooptgroupfield | 结账方式 | varchar | 50 |  | √ | ' ' | 结账方式,枚举: 101 :账期 102 :现款 |
| 30 | fstatus | 数据状态 | varchar | 30 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 33 | fsaloperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 34 | ftaxrateid | 默认税率(%) | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 35 | fpricelist | 销售价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 36 | fsettlementtypeid | 结算方式 | int8 | 64 |  |  | null | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 37 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fk_bj73_combofield | fk_bj73_combofield | varchar | 50 |  | √ | ' ' |  |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fbizpartnerid | 商务伙伴 | int8 | 64 |  |  | null | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 42 | fregcapital | 注册资本 | varchar | 40 |  | √ | ' ' | 注册资本 |
| 43 | fk_bj73_radiooptgroupfield8 | 一级渠道 | varchar | 50 |  | √ | ' ' | 一级渠道,枚举: 101 :B端 102 :C端 |
| 44 | ftype | 伙伴类型 | varchar | 30 |  | √ | ' ' | 伙伴类型,枚举: 1 :法人企业 2 :非法人企业 3 :非企业单位 4 :个人 5 :个体户 |
| 45 | fk_bj73_radiooptgroupfield5 | 头部百强 | varchar | 50 |  | √ | ' ' | 头部百强,枚举: 101 :是 102 :否 |
| 46 | fk_bj73_radiooptgroupfield4 | 是否合作 | varchar | 50 |  | √ | ' ' | 是否合作,枚举: 101 :是 102 :否 |
| 47 | fsettlementcyid | 交易币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | fk_bj73_radiooptgroupfield7 | 二级渠道 | varchar | 50 |  | √ | ' ' | 二级渠道,枚举: 101 :餐饮重客 102 :餐饮质量终端 103 :餐饮经销商 104 :餐饮配送商 105 :餐饮其他 106 :零售重客 107 :零售KA 108 :零售经销商 109 :零售配送商 110 :零售其他 |
| 49 | fk_bj73_radiooptgroupfield6 | 是否账期客户 | varchar | 50 |  | √ | ' ' | 是否账期客户,枚举: 101 :是 102 :否 |
| 50 | fk_bj73_largetextfield_tag | 特殊备注_详情 | text | 0 |  |  | null | 特殊备注_详情 |
| 51 | fapproverid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fgroupid | 客户分类 | int8 | 64 |  |  | null | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 53 | faddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 54 | fk_bj73_radiooptgroupfield1 | 经销商/终端 | varchar | 50 |  | √ | ' ' | 经销商/终端,枚举: 101 :经销商 102 :终端 |
| 55 | fk_bj73_radiooptgroupfield3 | 是否含运 | varchar | 50 |  | √ | ' ' | 是否含运,枚举: 101 :是 102 :否 |
| 56 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 57 | fk_bj73_radiooptgroupfield2 | 是否含税 | varchar | 50 |  | √ | ' ' | 是否含税,枚举: 101 :是 102 :否 |
| 58 | fsalerid | 负责人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 59 | fcustomerstatus | 客户状态 | int8 | 64 |  | √ | 0 | [客户状态 bd_customerstatus](../basedata_files/bd_customerstatus.md) |
| 60 | fk_bj73_combofield5 | fk_bj73_combofield5 | varchar | 50 |  | √ | ' ' |  |
| 61 | fk_bj73_combofield6 | fk_bj73_combofield6 | varchar | 50 |  | √ | ' ' |  |
| 62 | fk_bj73_combofield7 | fk_bj73_combofield7 | varchar | 50 |  | √ | ' ' |  |
| 63 | fk_bj73_combofield8 | fk_bj73_combofield8 | varchar | 50 |  | √ | ' ' |  |
| 64 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 65 | ftaxno | 税号 | varchar | 60 |  | √ | ' ' | 税号 |
| 66 | fk_bj73_combofield1 | fk_bj73_combofield1 | varchar | 50 |  | √ | ' ' |  |
| 67 | fk_bj73_combofield2 | fk_bj73_combofield2 | varchar | 50 |  | √ | ' ' |  |
| 68 | fk_bj73_combofield3 | fk_bj73_combofield3 | varchar | 50 |  | √ | ' ' |  |
| 69 | fk_bj73_combofield4 | fk_bj73_combofield4 | varchar | 50 |  | √ | ' ' |  |
| 70 | fblockedorder | 销售冻结 | bpchar | 1 |  | √ | '0' | 销售冻结 |
| 71 | fbizfunction | 业务职能 | varchar | 30 |  | √ | ',1,2,3,4,' | 业务职能,枚举: 1 :销售 2 :结算 3 :付款 4 :收货 |
| 72 | fk_bj73_largetextfield | 特殊备注 | varchar | 255 |  | √ | ' ' | 特殊备注 |
| 73 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 74 | ftransportleadtime | 运输提前期（天） | int8 | 64 |  | √ | 0 | 运输提前期（天） |
| 75 | fsimplepinyin | 简拼 | varchar | 255 |  | √ | ' ' | 简拼 |
| 76 | finvoicetype | 发票类型（已失效） | varchar | 30 |  | √ | ' ' | 发票类型（已失效）,枚举: 1 :增值税专用发票 2 :普通发票 |
| 77 | fbusinessterm | 营业期限 | varchar | 60 |  | √ | ' ' | 营业期限 |
| 78 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 79 | fk_bj73_assistantfield | 客户等级 | int8 | 64 |  |  | null | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 80 | fk_bj73_textfield6 | fk_bj73_textfield6 | varchar | 50 |  | √ | ' ' |  |
| 81 | flogo | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 82 | fk_bj73_textfield7 | fk_bj73_textfield7 | varchar | 50 |  | √ | ' ' |  |
| 83 | fk_bj73_textfield4 | 法人代表联系方式 | varchar | 50 |  | √ | ' ' | 法人代表联系方式 |
| 84 | fbloccustomer | 所属集团 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 85 | fk_bj73_textfield5 | fk_bj73_textfield5 | varchar | 50 |  | √ | ' ' |  |
| 86 | fk_bj73_textfield8 | 账龄 | varchar | 50 |  | √ | ' ' | 账龄 |
| 87 | fk_bj73_textfield9 | 科目 | varchar | 50 |  | √ | ' ' | 科目 |
| 88 | fk_bj73_textfield12 | 经营范围 | varchar | 50 |  | √ | ' ' | 经营范围 |
| 89 | fk_bj73_textfield11 | fk_bj73_textfield11 | varchar | 50 |  | √ | ' ' |  |
| 90 | fk_bj73_textfield14 | 门店数 | varchar | 50 |  | √ | ' ' | 门店数 |
| 91 | fk_bj73_textfield13 | fk_bj73_textfield13 | varchar | 50 |  | √ | ' ' |  |
| 92 | finvoiceaddress | 收票地址 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 93 | fk_bj73_textfield2 | 账期信用 | varchar | 200 |  | √ | ' ' | 账期信用 |
| 94 | fk_bj73_textfield3 | 授信额度 | varchar | 50 |  | √ | ' ' | 授信额度 |
| 95 | fk_bj73_textfield10 | 市场 | varchar | 50 |  | √ | ' ' | 市场 |
| 96 | fk_bj73_textfield16 | fk_bj73_textfield16 | varchar | 50 |  | √ | ' ' |  |
| 97 | fblocflag | 集团客户 | bpchar | 1 |  | √ | '0' | 集团客户 |
| 98 | fk_bj73_textfield15 | 分仓数 | varchar | 50 |  | √ | ' ' | 分仓数 |
| 99 | fblockedshipment | 发货冻结 | bpchar | 1 |  | √ | '0' | 发货冻结 |
| 100 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 101 | fcheckexpectqtyctrl | 可发量控制 | bpchar | 1 |  | √ | '1' | 可发量控制 |
| 102 | fk_bj73_textfield17 | 发展描述 | varchar | 50 |  | √ | ' ' | 发展描述 |
| 103 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 104 | fconsignment | 可委托代销 | bpchar | 1 |  | √ | '0' | 可委托代销 |
| 105 | ftaxregistplace | 税务注册地 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 106 | fctrlstrategy | 控制策略 | varchar | 10 |  |  | null | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 107 | finvoicecustomerid | 结算客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 108 | fadminorgid | 管理组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 109 | fsimplename | 简称 | varchar | 255 |  | √ | ' ' | 简称 |
| 110 | fk_bj73_textfield | 客诉等级 | varchar | 50 |  | √ | ' ' | 客诉等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_customer_type |  | ftype |
| 2 | idx_t_bd_customer_ecsss |  | fenable,fcustomerstatus |
| 3 | idx_t_bd_customer_group |  | fgroupid |
| 4 | t_bd_customer_pkey |  | fid |
| 5 | idx_t_bd_customer_sp |  | fsimplepinyin |
| 6 | idx_t_bd_customer_masterid |  | fmasterid |
| 7 | idx_t_bd_customer_master |  | fmasterid |
| 8 | idx_t_bd_customersrcid |  | fsourcedataid |
| 9 | idx_t_bd_customer_number |  | fnumber |
| 10 | idx_t_bd_customer_createorg |  | fcreateorgid |
| 11 | idx_t_bd_customer_bizpt |  | fbizpartnerid |
| 12 | idx_t_bd_customerbit |  | fbitindex |
| 13 | idx_t_bd_customer_orgstrat |  | fctrlstrategy,forgid |
