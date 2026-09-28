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
| 7 | fasstactitemid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
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

## 币别核算-子表 t_bd_accountcurrency

- **表名称：** 币别核算-子表
- **表名：** t_bd_accountcurrency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
| 3 | fcontrollevel | 控制级次 | varchar | 2 |  | √ | ' ' | 控制级次,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faccheck | 往来核算 | bpchar | 1 |  | √ | '0' | 往来核算 |
| 6 | fac | fac | bpchar | 1 |  | √ | '0' |  |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcurrencyhelp | 币别 | varchar | 30 |  | √ | ' ' | 币别 |
| 11 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | fpltype | 损益类型 | varchar | 30 |  | √ | ' ' | 损益类型,枚举: 1 :收入要素 2 :成本要素 3 :管理费用 4 :销售费用 5 :财务费用 6 :其它损益类型 0 :非损益类科目 |
| 15 | fcheckitemhelp | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 16 | facctcurrency | 外币核算类型 | varchar | 30 |  | √ | ' ' | 外币核算类型,枚举: nocurrency :不核算外币 descurrency :指定核算币别 allcurrency :核算所有币别 |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | ffullname | 全名 | varchar | 255 |  |  | ' ' | 全名 |
| 19 | fisbank | 银行科目 | bpchar | 1 |  | √ | '0' | 银行科目 |
| 20 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 21 | fiscash | 现金科目 | bpchar | 1 |  | √ | '0' | 现金科目 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fhelpcode | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 24 | fisqty | 数量核算 | bpchar | 1 |  | √ | '0' | 数量核算 |
| 25 | fischangecurrency | 期末调汇 | bpchar | 1 |  | √ | '0' | 期末调汇 |
| 26 | fstartdate | 版本化日期 | timestamp | 0 |  |  | null | 版本化日期 |
| 27 | faccounttypeid | 会计要素 | int8 | 64 |  | √ | 0 | 会计要素 bd_element |
| 28 | fisfreeze | fisfreeze | bpchar | 1 |  | √ | '0' |  |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fbw | 表外科目 | bpchar | 1 |  | √ | '0' | 表外科目 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 33 | fismanual | 手工录入 | bpchar | 1 |  | √ | '1' | 手工录入 |
| 34 | facnotice | 往来通知 | bpchar | 1 |  | √ | '0' | 往来通知 |
| 35 | fisjournal | 登日记账 | bpchar | 1 |  | √ | '0' | 登日记账 |
| 36 | faccrualdirection | 科目录入方向控制 | varchar | 30 |  | √ | ' ' | 科目录入方向控制,枚举: nocontrol :不控制 debit :借方 credit :贷方 |
| 37 | fisoutdailyaccount | fisoutdailyaccount | bpchar | 1 |  | √ | '0' |  |
| 38 | fmeasureunitgroupid | 计量单位分组 | int8 | 64 |  | √ | 0 | 计量单位分组 bd_measureunitsgroup |
| 39 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 42 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 43 | fcontrol | 受控系统 | varchar | 30 |  | √ | ' ' | 受控系统,枚举: nocontrol :无 receivesys :应收系统 copingsys :应付系统 assetmanage :资产管理 |
| 44 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 47 | fdc | 余额方向 | varchar | 30 |  | √ | ' ' | 余额方向,枚举: 1 :借 -1 :贷 |
| 48 | fisassist | 是否包含核算项目 | bpchar | 1 |  | √ | '0' | 是否包含核算项目 |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 51 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 52 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 53 | fiscashequivalent | 现金等价物 | bpchar | 1 |  | √ | '0' | 现金等价物 |
| 54 | fmeasureunitid | 默认计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 55 | fisallowca | 允许公司增加下级科目 | bpchar | 1 |  | √ | '0' | 允许公司增加下级科目 |
| 56 | fiscontrol | fiscontrol | bpchar | 1 |  | √ | '0' |  |

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
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
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
