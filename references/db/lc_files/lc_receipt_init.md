# 信用证收证初始化-lc_receipt_init

## 交单分录-子表 t_lc_credit_initentry

- **表名称：** 交单分录-子表
- **表名：** t_lc_credit_initentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farrivalno | 交单编号 | varchar | 50 |  | √ | ' ' | 交单编号 |
| 3 | fendacceptdate | 最迟承兑/付款日期 | timestamp | 0 |  |  | null | 最迟承兑/付款日期 |
| 4 | farrivalamount | 交单金额 | numeric | 19 | 6 | √ | 0 | 交单金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | farrivalway | 交单处理方式 | varchar | 50 |  | √ | ' ' | 交单处理方式,枚举: protest :拒付 accept :承兑 payment :付款 |
| 7 | fdoneamount | 已收金额 | numeric | 19 | 6 | √ | 0 | 已收金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | farrivaldate | 交单日期 | timestamp | 0 |  |  | null | 交单日期 |
| 10 | fendpaydate | 最迟付款日期 | timestamp | 0 |  |  | null | 最迟付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_credit_initentry |  | fentryid |
| 2 | idx_lc_credit_initentry |  | fid |

---

## 信用证收证初始化-主表 t_lc_receipt_init

- **表名称：** 信用证收证初始化-主表
- **表名：** t_lc_receipt_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 3 | freceiptdate | 收证日期 | timestamp | 0 |  |  | null | 收证日期 |
| 4 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 5 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 8 | fcreditno | 信用证号 | varchar | 80 |  | √ | ' ' | 信用证号 |
| 9 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' |  |
| 10 | fiscancel | 可撤销 | bpchar | 1 |  | √ | '0' | 可撤销 |
| 11 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 15 | flowstr | 金额下限 | varchar | 50 |  | √ | ' ' | 金额下限 |
| 16 | fisnationalcard | 国际证 | bpchar | 1 |  | √ | '0' | 国际证 |
| 17 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | famountscaleupper | 溢短装金额浮动比例上限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例上限（%） |
| 20 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fismakeover | 可转让 | bpchar | 1 |  | √ | '0' | 可转让 |
| 23 | fcreditstatus | 信用证状态 | varchar | 50 |  | √ | ' ' | 信用证状态,枚举: done_register :已登记 done_close :已闭卷 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fapplydate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 28 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 30 | fbenefitaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 31 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 32 | fbizcontactinfo | 业务联系方式 | varchar | 80 |  | √ | ' ' | 业务联系方式 |
| 33 | fapplyaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 34 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 35 | fbankid | 通知行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 36 | famountscalelow | 溢短装金额浮动比例下限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例下限（%） |
| 37 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | fupperstr | 金额上限 | varchar | 50 |  | √ | ' ' | 金额上限 |
| 39 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_receipt_init |  | fbillno |
| 2 | pk_t_lc_receipt_init |  | fid |

---

## 信用证收证初始化-多语言表 t_lc_receipt_init_l

- **表名称：** 信用证收证初始化-多语言表
- **表名：** t_lc_receipt_init_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 4 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 5 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | fbenefitaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 8 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 9 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 10 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 11 | fapplyaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 12 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 13 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_receipt_init_l |  | fid,flocaleid |
| 2 | pk_t_lc_receipt_init_l |  | fpkid |

---

## 信用证收证初始化-分表 t_lc_receipt_init_e

- **表名称：** 信用证收证初始化-分表
- **表名：** t_lc_receipt_init_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankcountryid | 通知行国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 3 | freimbursingbank | 偿付行 | varchar | 255 |  | √ | ' ' | 偿付行 |
| 4 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 5 | forgid | 受益人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fnoticebank | 开证行 | varchar | 255 |  | √ | ' ' | 开证行 |
| 7 | fnegotiatingbank | 议付行 | varchar | 255 |  | √ | ' ' | 议付行 |
| 8 | fdealbilltermend | 交单期限.结束 | timestamp | 0 |  |  | null | 交单期限.结束 |
| 9 | fistransfer | 转运 | bpchar | 1 |  | √ | '0' | 转运 |
| 10 | fnoticebankid | 开证行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 11 | fconfirmingbank | 保兑行 | varchar | 255 |  | √ | ' ' | 保兑行 |
| 12 | fbenefitcountryid | 开证人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 13 | fbenefiterother | 开证人 | varchar | 255 |  | √ | ' ' | 开证人 |
| 14 | fisnegotiating | 议付 | bpchar | 1 |  | √ | '0' | 议付 |
| 15 | fcargocountryid | 货物国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 16 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 17 | fnegotiatingdate | 议付日期 | timestamp | 0 |  |  | null | 议付日期 |
| 18 | fapplycountryid | 受益人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 19 | fisbatch | 分批 | bpchar | 1 |  | √ | '0' | 分批 |
| 20 | fbenefitertype | 开证人类型 | varchar | 50 |  | √ | ' ' | 开证人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 21 | fbenefiterid | 开证人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fdealbilltermstart | 交单期限.开始 | timestamp | 0 |  |  | null | 交单期限.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_receipt_init_e |  | forgid |
| 2 | pk_t_lc_receipt_init_e |  | fid |
