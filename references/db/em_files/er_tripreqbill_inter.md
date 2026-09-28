# 全球出差申请单-er_tripreqbill_inter

## 收款信息（废弃）-子表 t_er_nreqaccountentry

- **表名称：** 收款信息（废弃）-子表
- **表名：** t_er_nreqaccountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccpaidamount | 已还款金额（本位币） | numeric | 23 | 10 | √ | 0 | 已还款金额（本位币） |
| 3 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0 | 已出单金额 |
| 4 | foriamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fpayeraccount01 | 银行账号4位 | varchar | 50 |  | √ | ' ' | 银行账号4位 |
| 6 | fpayertype | 收款人类型 | varchar | 50 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 7 | fentrystatus | 分录状态 | varchar | 50 |  | √ | ' ' | 分录状态,枚举: F :等待付款 G :已付款 E :审核通过 I :关闭 |
| 8 | fpayerdeptid | 收款人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fpayercompid | 收款人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | foriaccappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | famount | 金额（本位币） | numeric | 23 | 10 | √ | 0 | 金额（本位币） |
| 13 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 15 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 16 | fpayeraccountname | 账户名称 | varchar | 50 |  | √ | ' ' | 账户名称 |
| 17 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 18 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 19 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0 | 可用余额（本位币） |
| 20 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 21 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 22 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 23 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 24 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 25 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0 | 未付金额(本位币) |
| 26 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 27 | fpayeraccount02 | 银行账号(_old) | varchar | 50 |  | √ | ' ' | 银行账号(_old) |
| 28 | fpaidamount | 已还款金额 | numeric | 23 | 10 | √ | 0 | 已还款金额 |
| 29 | fpayeraccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 30 | faccappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fquotetype | 换算方式(收款) | bpchar | 1 |  | √ | '0' | 换算方式(收款),枚举: 0 :直接汇率 1 :间接汇率 |
| 33 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreqaccountentry |  | fid,fseq |
| 2 | pk_er_nreqaccountentry |  | fentryid |

---

## 行程变更历史记录（废弃）-子表 t_er_ntripchangehistory

- **表名称：** 行程变更历史记录（废弃）-子表
- **表名：** t_er_ntripchangehistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 原始分录id | int8 | 64 |  | √ | 0 | 原始分录id |
| 3 | foriamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 4 | ftriporiaccappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 5 | ftripcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ftripamount | 申请金额（本位币） | numeric | 23 | 10 | √ | 0 | 申请金额（本位币） |
| 8 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 12 | fistripmulcurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 13 | fchangedate | 变更日期（废弃） | timestamp | 0 |  |  | null | 变更日期（废弃） |
| 14 | fvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |
| 15 | fchanger | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fsrcentrydata | 原始分录json数据 | text | 0 |  |  | null | 原始分录json数据 |
| 19 | ftripexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fsrcentrydata_tag | 原始分录json数据_详情 | text | 0 |  |  | null | 原始分录json数据_详情 |
| 21 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 22 | ftripaccappamount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0 | 核定金额(本位币) |
| 23 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nchange_srcentryid |  | fsrcentryid |
| 2 | pk_er_ntripchangehistory |  | fentryid |

---

## 出差人-多选基础资料表 t_er_ntripmultitravelers

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_ntripmultitravelers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntravelersbillid |  | fid |
| 2 | idx_er_ntravelersuserid |  | fbasedataid |
| 3 | pk_er_ntripmultitravelers |  | fpkid |

---

## 全球出差申请单-多语言表 t_er_nreqbill_l

- **表名称：** 全球出差申请单-多语言表
- **表名：** t_er_nreqbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreqbill_l |  | fid,flocaleid |
| 2 | pk_er_nreqbill_l |  | fpkid |

---

## 全球出差申请单-分表 t_er_nreqbill_a

- **表名称：** 全球出差申请单-分表
- **表名：** t_er_nreqbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 3 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 4 | fneedimagescan | 需要影像扫描 | varchar | 50 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 5 | fcountry | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_nreqbill_a |  | fid |

---

## 行程信息-子表 t_er_nreqtripentry

- **表名称：** 行程信息-子表
- **表名：** t_er_nreqtripentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriamount | foriamount | numeric | 23 | 10 | √ | 0 |  |
| 3 | ftripexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 4 | ftriporiaccappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 5 | faccusedamount | 已报销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已报销金额（本位币） |
| 6 | ftripcurrencyid | 行程币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fsourcetripid | 源单行程id | int8 | 64 |  | √ | 0 | 源单行程id |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftripentrystatus | 行程状态 | varchar | 50 |  | √ | ' ' | 行程状态,枚举: A :暂存 B :提交 C :审核中 D :审核不通过 E :审核通过 G :已付款 I :关闭 |
| 10 | ftripamount | 借款金额（本位币） | numeric | 23 | 10 | √ | 0 | 借款金额（本位币） |
| 11 | ftoadm | 目的地 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 12 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fenddate | 行程期间.结束 | timestamp | 0 |  |  | null | 行程期间.结束 |
| 14 | ffromadm | 出发地 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 15 | ftoplaceid | 目的地(城市) | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 16 | fistripmulcurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 17 | frcurrencyid | 冗余表头本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0 | 可用余额（本位币） |
| 19 | fvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |
| 20 | ffromplaceid | 出发地(城市) | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 21 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 22 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | foriaccusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 24 | findex | 整数 | int4 | 32 |  | √ | 0 | 整数 |
| 25 | foriaccbalanceamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 26 | fexpeorirepayamount | 还款金额 | numeric | 23 | 10 | √ | 0 | 还款金额 |
| 27 | fentrykey | 关键字段 | varchar | 50 |  | √ | 'tripentrykey' | 关键字段 |
| 28 | ftripcancel | 行程取消 | bpchar | 1 |  | √ | ' ' | 行程取消 |
| 29 | ftripexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 30 | fentrycreatetime | 行程分录创建时间 | timestamp | 0 |  |  | null | 行程分录创建时间 |
| 31 | ftripentryarea | 出差地域 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 32 | fexperepayamount | 还款金额（本位币） | numeric | 23 | 10 | √ | 0 | 还款金额（本位币） |
| 33 | ftriporiamount | 借款金额 | numeric | 23 | 10 | √ | 0 | 借款金额 |
| 34 | fstartdate | 行程期间.开始 | timestamp | 0 |  |  | null | 行程期间.开始 |
| 35 | ftripaccappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 36 | ftripquotetype | 换算方式(行程) | bpchar | 1 |  | √ | '0' | 换算方式(行程),枚举: 0 :直接汇率 1 :间接汇率 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | ftripday | 行程天数 | int4 | 32 |  | √ | 0 | 行程天数 |
| 40 | fvehicles | 交通工具 | varchar | 500 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_nreqtripentry |  | fentryid |
| 2 | idx_er_nreqtripentry |  | fid |

---

## 多出差人-多选基础资料表 t_er_ntripchangetravel

- **表名称：** 多出差人-多选基础资料表
- **表名：** t_er_ntripchangetravel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntripchangetravel |  | fentryid |
| 2 | pk_er_ntripchangetravel |  | fpkid |

---

## 出差人-多选基础资料表 t_er_nreqbillpartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_nreqbillpartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreqbillpartner |  | fentryid |
| 2 | pk_er_nreqbillpartner |  | fpkid |

---

## 关联子实体-子表 t_er_nreqbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_nreqbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreqbill_lk_fid |  | fid |
| 2 | pk_t_er_nreqbill_lk |  | fpkid |

---

## 项目干系人-多选基础资料表 t_er_ntripreqower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_ntripreqower

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_ntripreqower |  | fpkid |
| 2 | idx_er_ntripreqower_fid |  | fid |

---

## 全球出差申请单-关联追踪表 t_er_nreqbill_tc

- **表名称：** 全球出差申请单-关联追踪表
- **表名：** t_er_nreqbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreqbill_tc_fsbld |  | fsbillid |
| 2 | idx_er_nreqbill_tc_tbill |  | ftbillid |
| 3 | idx_er_nreqbill_tc_tid |  | ftid |
| 4 | idx_er_nreqbill_tc_ftbld |  | ftbillid |
| 5 | pk_er_nreqbill_tc |  | fid |

---

## 关联子实体-子表 t_er_nreqtripentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_nreqtripentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_nreqtripentry_lk |  | fpkid |
| 2 | idx_er_nreqtripentry_lk_fentry |  | fentryid |

---

## 付款信息（废弃）-子表 t_er_ntripreqpayentry

- **表名称：** 付款信息（废弃）-子表
- **表名：** t_er_ntripreqpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0 | 兑换汇率 |
| 13 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0 | 收款金额(本位币) |
| 14 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 17 | ffeecurrency | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 23 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 24 | ftargetcurrency | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | ftargetsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntqpe_feq |  | fid,fseq |
| 2 | idx_er_ntqpe_targetbillid_no |  | ftargetbillid,ftargetbillno |
| 3 | pk_er_ntripreqpayentry |  | fentryid |

---

## 全球出差申请单-反写记录表 t_er_nreqbill_wb

- **表名称：** 全球出差申请单-反写记录表
- **表名：** t_er_nreqbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_nreqbill_wb |  | fentryid |
| 2 | idx_er_nreqbill_wb |  | fid |

---

## 发票云附件-子表 t_er_ninvoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_ninvoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 3 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 6 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 7 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 10 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 12 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ninvoiceattachinfo_fid |  | fid |
| 2 | pk_er_ninvoiceattachinfo |  | fentryid |

---

## 途径地-多选基础资料表 t_er_historymulwaytointer

- **表名称：** 途径地-多选基础资料表
- **表名：** t_er_historymulwaytointer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_histormulwaytointer |  | fentryid |
| 2 | pk_er_histormulwaytointer |  | fpkid |

---

## 费用明细-子表 t_er_nreqentry

- **表名称：** 费用明细-子表
- **表名：** t_er_nreqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fnotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | foriamount | 预计金额 | numeric | 23 | 10 | √ | 0 | 预计金额 |
| 7 | fsourceentryid | 源明细id | int8 | 64 |  | √ | 0 | 源明细id |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdetailquotetype | 换算方式(明细) | bpchar | 1 |  | √ | '0' | 换算方式(明细),枚举: 0 :直接汇率 1 :间接汇率 |
| 10 | famount | 预计金额（本位币） | numeric | 23 | 10 | √ | 0 | 预计金额（本位币） |
| 11 | ftriptoplaceid | 出差地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 12 | fdaycount | 天数 | int8 | 64 |  | √ | 0 | 天数 |
| 13 | fisvactax | 增值税专票 | bpchar | 1 |  | √ | '0' | 增值税专票 |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_nreqentry |  | fdetailid |
| 2 | idx_er_nreqentryid |  | fentryid |

---

## 途径地-多选基础资料表 t_er_tripmulwaytointer

- **表名称：** 途径地-多选基础资料表
- **表名：** t_er_tripmulwaytointer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_tripmulwaytointer |  | fpkid |
| 2 | idx_er_tripmulwaytointer |  | fentryid |

---

## 全球出差申请单-主表 t_er_nreqbill

- **表名称：** 全球出差申请单-主表
- **表名：** t_er_nreqbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  | √ | ' ' | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 7 | froutetype | 单程/往返（废弃） | varchar | 50 |  | √ | ' ' | 单程/往返（废弃）,枚举: 0 :单程 1 :往返 |
| 8 | frvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :中转 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 11 | forigin | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 1 :WEB 2 :移动端 3 :语音助手 |
| 12 | fattachmentcount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 13 | fismanualrepay | 手否手动还款（废弃） | bpchar | 1 |  | √ | '0' | 手否手动还款（废弃） |
| 14 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 16 | ffirstto | ffirstto | varchar | 50 |  | √ | ' ' |  |
| 17 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 18 | fimageno | 影像编号 | varchar | 100 |  | √ | ' ' | 影像编号 |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fexpensesassumeshowtypes | fexpensesassumeshowtypes | numeric | 23 | 10 | √ | 0 |  |
| 21 | fisquerybudget | fisquerybudget | bpchar | 1 |  | √ | '0' |  |
| 22 | frfirstendate | 第一段结束日期（废弃） | timestamp | 0 |  |  | null | 第一段结束日期（废弃） |
| 23 | fischange | 变更（废弃） | bpchar | 1 |  | √ | '0' | 变更（废弃） |
| 24 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 27 | frfirstto | 第一段目的地（废弃） | varchar | 50 |  | √ | ' ' | 第一段目的地（废弃） |
| 28 | ffullapp | ffullapp | bpchar | 1 |  | √ | '0' |  |
| 29 | frstartdate | 出发日期 | timestamp | 0 |  |  | null | 出发日期 |
| 30 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 31 | fnotpayamount | 未付金额（废弃） | numeric | 23 | 10 | √ | 0 | 未付金额（废弃） |
| 32 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fbalanceamount | 未还余额（废弃） | numeric | 23 | 10 | √ | 0 | 未还余额（废弃） |
| 36 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 37 | fraccexchangerate | 借款汇率表头冗余（废弃） | numeric | 23 | 10 | √ | 0 | 借款汇率表头冗余（废弃） |
| 38 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 39 | fistravelers | 多出差人（废弃） | bpchar | 1 |  | √ | '0' | 多出差人（废弃） |
| 40 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 41 | fpayamount | 已付金额（废弃） | numeric | 23 | 10 | √ | 0 | 已付金额（废弃） |
| 42 | fplandays | 预计天数 | int8 | 64 |  | √ | 0 | 预计天数 |
| 43 | fraccountcurrency | 借款币种表头冗余（废弃） | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fbiztype | 申请类型 | varchar | 2 |  | √ | ' ' | 申请类型,枚举: 1 :出差申请 2 :出差变更 3 :出差记录 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fusedamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 47 | fencashamount | 付现金额（废弃） | numeric | 23 | 10 | √ | 0 | 付现金额（废弃） |
| 48 | funrepaymentamount | 申请人未还款 | numeric | 23 | 10 | √ | 0 | 申请人未还款 |
| 49 | feditentry | 操作分录 | varchar | 50 |  | √ | ' ' | 操作分录,枚举: 1 :编辑 2 :删除 3 :完成 0 :初始化 |
| 50 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | forireceiveamount | 借款金额原币表头冗余（废弃） | numeric | 23 | 10 | √ | 0 | 借款金额原币表头冗余（废弃） |
| 52 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_reqbill :费用申请单 er_tripreimbursebill :差旅费报销单 er_reimbursebill :费用报销单 er_loanbill :借款单 er_repaymentbill :还款单 er_tripreqbill_inter :全球出差申请单 |
| 53 | freimbuesetime | 报销次数 | int8 | 64 |  | √ | 0 | 报销次数 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | ftriptypeid | 出差类型 | int8 | 64 |  | √ | 0 | [出差类型 er_triptype](../em_files/er_triptype.md) |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 58 | fwritebillmode | 填单模式 | varchar | 2 |  | √ | ' ' | 填单模式,枚举: 1 :简要行程 2 :常规行程 |
| 59 | freturnedmount | 已还金额（废弃） | numeric | 23 | 10 | √ | 0 | 已还金额（废弃） |
| 60 | fismulwayto | 开启途经地 | bpchar | 1 |  | √ | '0' | 开启途经地 |
| 61 | floanamount | 借款金额（废弃） | numeric | 23 | 10 | √ | 0 | 借款金额（废弃） |
| 62 | fisloan | 借款（废弃） | bpchar | 1 |  | √ | '0' | 借款（废弃） |
| 63 | fapplierposition | 职位 | varchar | 200 |  | √ | ' ' | 职位 |
| 64 | fbizitem | 差旅业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 65 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | frfrom | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 67 | fispaybyhead | 按单头付款（废弃） | bpchar | 1 |  | √ | '0' | 按单头付款（废弃） |
| 68 | fheadpaydate | 付款日期（废弃） | timestamp | 0 |  |  | null | 付款日期（废弃） |
| 69 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 70 | frto | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 71 | fsourcebillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 72 | frenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 73 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 74 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 75 | frepaymentdate | 还款日期（废弃） | timestamp | 0 |  |  | null | 还款日期（废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_nreqbill |  | fid |
| 2 | idx_er_nreqbillno |  | fbillno |
