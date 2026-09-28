# 其他往来单位-cas_othercontactunit

## 其他往来单位-主表 t_cas_othercontactunit

- **表名称：** 其他往来单位-主表
- **表名：** t_cas_othercontactunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | fgroupid | 其他往来单位分类 | int8 | 64 |  | √ | 0 | [其他往来单位分类 cas_otherunitgroup](../cas_files/cas_otherunitgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_othercontactunit |  | fid |
| 2 | idx_cas_othercontactunit_fnumber |  | fnumber |
| 3 | idx_t_cas_othercontactunit_master |  | fmasterid |
| 4 | idx_t_cas_othercontactunit_createorg |  | fcreateorgid |

---

## 银行信息分录-子表 t_cas_otherunit_bank

- **表名称：** 银行信息分录-子表
- **表名：** t_cas_otherunit_bank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 3 | fbankaccounttype | 银行账户类型 | varchar | 50 |  | √ | ' ' | 银行账户类型,枚举: |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbankaccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 6 | fpayeeaddress | 收款方详细地址 | varchar | 300 |  | √ | ' ' | 收款方详细地址 |
| 7 | fpayeephone | 收款方联系电话 | varchar | 100 |  | √ | ' ' | 收款方联系电话 |
| 8 | fcommissionbearer | 默认手续费承担方 | varchar | 50 |  | √ | ' ' | 默认手续费承担方,枚举: 1 :付款方 2 :收款方 |
| 9 | fagentbankaccount | 代理行账号 | varchar | 80 |  | √ | ' ' | 代理行账号 |
| 10 | fsettlment | 默认结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 11 | fliquidationparam | 默认清算要求参数 | varchar | 125 |  | √ | ' ' | 默认清算要求参数 |
| 12 | fibanid | 国际银行账户号码 | varchar | 50 |  | √ | ' ' | 国际银行账户号码 |
| 13 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fpayeeadmindivision | 收款方行政区划 | varchar | 50 |  | √ | ' ' | 收款方行政区划 |
| 17 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 18 | fagentbank | 默认代理行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_otherunit_bank |  | fentryid |
| 2 | idx_cas_otherunit_bank |  | fid |

---

## 银行信息分录-多语言表 t_cas_otherunit_bank_l

- **表名称：** 银行信息分录-多语言表
- **表名：** t_cas_otherunit_bank_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpayeeaddress | 收款方详细地址 | varchar | 300 |  | √ | ' ' | 收款方详细地址 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | null | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_otherunit_bank_l |  | fpkid |
| 2 | idx_cas_otherunit_bank_l |  | fentryid |

---

## 其他往来单位-多语言表 t_cas_othercontactunit_l

- **表名称：** 其他往来单位-多语言表
- **表名：** t_cas_othercontactunit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_othercontactunit_l |  | fpkid |
| 2 | idx_cas_othercontactunit_l_fid |  | fid,flocaleid |

---

## 其他往来单位-使用范围表 t_cas_othercontactunit_u

- **表名称：** 其他往来单位-使用范围表
- **表名：** t_cas_othercontactunit_u

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
| 1 | pk_t_cas_othercontactunit_u |  | fdataid,fuseorgid |
| 2 | idx_t_cas_othercontactunit_u_uo |  | fuseorgid |
