# 会计科目-bd_accountview

## 核算维度-子表 t_bd_accountasstactitem

- **表名称：** 核算维度-子表
- **表名：** t_bd_accountasstactitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenaccheck | 往来核算 | bpchar | 1 |  | √ | '0' | 往来核算 |
| 3 | fisdetail | 明细 | bpchar | 1 |  | √ | '0' | 明细 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fassgrpdefid | 默认值id | varchar | 30 |  | √ | ' ' | 默认值id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fasstactitemid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 8 | fisrequire | 必录 | bpchar | 1 |  | √ | '0' | 必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountasstactitem |  | fentryid |
| 2 | idx_bd_acctasstactitem_id |  | fid |

---

## 币种核算-子表 t_bd_accountcurrency

- **表名称：** 币种核算-子表
- **表名：** t_bd_accountcurrency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountcurrency |  | fentryid |
| 2 | idx_bd_acctcurrency_id |  | fid |

---

## 会计科目-主表 t_bd_account

- **表名称：** 会计科目-主表
- **表名：** t_bd_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 明细科目 | bpchar | 1 |  | √ | '0' | 明细科目 |
| 3 | fcontrollevel | 由分配组织创建的级次深度 | varchar | 2 |  | √ | ' ' | 由分配组织创建的级次深度,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | faccheck | 往来核算 | bpchar | 1 |  | √ | '0' | 往来核算 |
| 6 | fac | fac | bpchar | 1 |  | √ | '0' |  |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcurrencyhelp | 币种 | varchar | 30 |  | √ | ' ' | 币种 |
| 11 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | fpltype | 损益类型 | varchar | 30 |  | √ | ' ' | 损益类型,枚举: 1 :收入要素 2 :成本要素 3 :管理费用 4 :销售费用 5 :财务费用 6 :其它损益类型 0 :非损益类科目 |
| 15 | fcheckitemhelp | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 16 | facctcurrency | 外币核算类型 | varchar | 30 |  | √ | ' ' | 外币核算类型,枚举: nocurrency :不核算外币 descurrency :指定核算币种 allcurrency :核算所有币种 |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | ffullname | 全名 | varchar | 255 |  |  | ' ' | 全名 |
| 19 | fisbank | 银行科目 | bpchar | 1 |  | √ | '0' | 银行科目 |
| 20 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 21 | fiscash | 现金科目 | bpchar | 1 |  | √ | '0' | 现金科目 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fhelpcode | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 24 | fisqty | 数量核算 | bpchar | 1 |  | √ | '0' | 数量核算 |
| 25 | fischangecurrency | 期末调汇 | bpchar | 1 |  | √ | '0' | 期末调汇 |
| 26 | fisbudget | 是否预算科目 | bpchar | 1 |  | √ | '0' | 是否预算科目 |
| 27 | fstartdate | 版本化日期 | timestamp | 0 |  |  | null | 版本化日期 |
| 28 | faccounttypeid | 会计要素 | int8 | 64 |  | √ | 0 | [会计要素 bd_element](../gl_files/bd_element.md) |
| 29 | fisfreeze | fisfreeze | bpchar | 1 |  | √ | '0' |  |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fbw | 表外科目 | bpchar | 1 |  | √ | '0' | 表外科目 |
| 32 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 34 | fismanual | 手工录入 | bpchar | 1 |  | √ | '1' | 手工录入 |
| 35 | facnotice | 往来通知 | bpchar | 1 |  | √ | '0' | 往来通知 |
| 36 | fisjournal | 登日记账 | bpchar | 1 |  | √ | '0' | 登日记账 |
| 37 | faccrualdirection | 发生额方向 | varchar | 30 |  | √ | ' ' | 发生额方向,枚举: nocontrol :不控制 debit :借方 credit :贷方 |
| 38 | fisoutdailyaccount | fisoutdailyaccount | bpchar | 1 |  | √ | '0' |  |
| 39 | fmeasureunitgroupid | 计量单位分组 | int8 | 64 |  | √ | 0 | [计量单位分组 bd_measureunitsgroup](../base_files/bd_measureunitsgroup.md) |
| 40 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 43 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 44 | fcontrol | 受控系统 | varchar | 30 |  | √ | ' ' | 受控系统,枚举: nocontrol :无 receivesys :应收系统 copingsys :应付系统 assetmanage :资产管理 |
| 45 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 48 | fdc | 余额方向 | varchar | 30 |  | √ | ' ' | 余额方向,枚举: 1 :借 -1 :贷 |
| 49 | fisassist | 是否包含核算项目 | bpchar | 1 |  | √ | '0' | 是否包含核算项目 |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 52 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 53 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 54 | fiscashequivalent | 现金等价物 | bpchar | 1 |  | √ | '0' | 现金等价物 |
| 55 | fmeasureunitid | 默认计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 56 | fisallowca | 允许使用组织新增下级 | bpchar | 1 |  | √ | '0' | 允许使用组织新增下级 |
| 57 | fiscontrol | fiscontrol | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_acct_num |  | faccounttableid,fnumber |
| 2 | idx_t_bd_account_createorg |  | fcreateorgid |
| 3 | t_bd_account_pkey |  | fid |
| 4 | idx_acct_org |  | fctrlstrategy,forgid |
| 5 | idx_acct_parent |  | fparentid |
| 6 | idx_acct_masterid |  | fmasterid |
| 7 | idx_t_bd_account_master |  | fmasterid |
| 8 | idx_acct_createorg |  | fctrlstrategy,fcreateorgid |

---

## 会计科目-使用范围表 t_bd_account_u

- **表名称：** 会计科目-使用范围表
- **表名：** t_bd_account_u

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
| 1 | t_bd_account_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_account_u_uo |  | fuseorgid |

---

## 会计科目-多语言表 t_bd_account_l

- **表名称：** 会计科目-多语言表
- **表名：** t_bd_account_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  |  | ' ' | 名称 |
| 3 | fsimplename | fsimplename | varchar | 255 |  |  | ' ' |  |
| 4 | ffullname | 全名 | varchar | 255 |  |  | ' ' | 全名 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | fdescription | varchar | 255 |  |  | ' ' |  |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_account_l_pkey |  | fpkid |
| 2 | idx_bd_account_l_fid |  | fid,flocaleid |

---

## 会计科目-使用范围位图表 t_bd_account_m

- **表名称：** 会计科目-使用范围位图表
- **表名：** t_bd_account_m

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
| 1 | pk_t_bd_account_m |  | forgid |
