# 福费廷-lc_forfaiting

## 福费廷-反写记录表 t_lc_forfaiting_wb

- **表名称：** 福费廷-反写记录表
- **表名：** t_lc_forfaiting_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_forfaiting_wb_fk |  | fid |
| 2 | pk_lc_forfaiting_wb |  | fentryid |

---

## 福费廷-主表 t_lc_forfaiting

- **表名称：** 福费廷-主表
- **表名：** t_lc_forfaiting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 融资期限（ymd） | varchar | 50 |  | √ | ' ' | 融资期限（ymd） |
| 3 | forgid | 受益人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbuyoutcurrencyid | 融资买断币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | ftotalfeeamount | 费用金额合计 | numeric | 19 | 6 | √ | 0 | 费用金额合计 |
| 6 | flettercreditid | 信用证号 | int8 | 64 |  | √ | 0 | [收证信用证 lc_receipt_f7](../lc_files/lc_receipt_f7.md) |
| 7 | fsubjectid | 融资主体 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fendpaydate | 对方最迟付款日期 | timestamp | 0 |  |  | null | 对方最迟付款日期 |
| 10 | fenddate | 融资到期日期 | timestamp | 0 |  |  | null | 融资到期日期 |
| 11 | frate | 融资利率（%） | numeric | 23 | 10 | √ | 0 | 融资利率（%） |
| 12 | fcomprehensivecostrate | 综合成本率（%） | numeric | 23 | 10 | √ | 0 | 综合成本率（%） |
| 13 | fcomprehensivecost | 综合成本 | numeric | 19 | 6 | √ | 0 | 综合成本 |
| 14 | fvaliddate | 融资生效日期 | timestamp | 0 |  |  | null | 融资生效日期 |
| 15 | finvoiceno | 交单发票号 | varchar | 50 |  | √ | ' ' | 交单发票号 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | farrivalcurrencyid | 交单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | ffinancingtype | 融资类型 | varchar | 50 |  | √ | ' ' | 融资类型,枚举: forfaiting :福费廷 agent_forfaiting :代理福费廷 export_discount :出口贴现 |
| 19 | finterestdeferreddays | 计息顺延天数 | int8 | 64 |  | √ | 0 | 计息顺延天数 |
| 20 | frecbillno | 收款单编号 | varchar | 50 |  | √ | ' ' | 收款单编号 |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | farrivalamount | 交单金额 | numeric | 19 | 6 | √ | 0 | 交单金额 |
| 23 | fisforward | 远期 | bpchar | 1 |  | √ | '1' | 远期 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | farrivalnoid | 交单编号 | int8 | 64 |  | √ | 0 | [交单F7 lc_present_f7](../lc_files/lc_present_f7.md) |
| 26 | fendacceptdate | 对方最迟承兑/付款确认日期 | timestamp | 0 |  |  | null | 对方最迟承兑/付款确认日期 |
| 27 | frecnetamount | 融资到款净额 | numeric | 19 | 6 | √ | 0 | 融资到款净额 |
| 28 | farrivalway | 交单对方处理方式 | varchar | 50 |  | √ | ' ' | 交单对方处理方式,枚举: accept :承兑 payment :付款 protest :拒付 |
| 29 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 30 | fbenefitertype | 开证人类型 | varchar | 50 |  | √ | ' ' | 开证人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | farrivaldate | 交单日期 | timestamp | 0 |  |  | null | 交单日期 |
| 33 | fisrelatedtrd | 涉及关联交易 | bpchar | 1 |  | √ | '0' | 涉及关联交易 |
| 34 | farrivaltype | 交单类型 | varchar | 50 |  | √ | ' ' | 交单类型,枚举: credit :信用证 da :DA交单 dp :DP交单 |
| 35 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' |  |
| 36 | fbuyoutamount | 融资买断金额 | numeric | 19 | 6 | √ | 0 | 融资买断金额 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fbenefiterother | 开证人 | varchar | 255 |  | √ | ' ' | 开证人 |
| 39 | frecaccountid | 收款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 40 | fisreceipt | 存在关联收款单 | bpchar | 1 |  | √ | '0' | 存在关联收款单 |
| 41 | facceptancebankid | 融资受理银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 42 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fpresendbankid | 交单行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 46 | fwithholdinterestamount | 预扣利息金额 | numeric | 19 | 6 | √ | 0 | 预扣利息金额 |
| 47 | fratedays | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: 360 :Actual/360 365 :Actual/365 |
| 48 | fbizdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 49 | fbenefiterid | 开证人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_forfaiting |  | fbillno |
| 2 | pk_lc_forfaiting |  | fid |

---

## 福费廷-关联追踪表 t_lc_forfaiting_tc

- **表名称：** 福费廷-关联追踪表
- **表名：** t_lc_forfaiting_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lc_forfaiting_tc |  | fid |
| 2 | idx_lc_forfaiting_tc_tbill |  | ftbillid |
| 3 | idx_lc_forfaiting_tc_tid |  | ftid |

---

## 福费廷-多语言表 t_lc_forfaiting_l

- **表名称：** 福费廷-多语言表
- **表名：** t_lc_forfaiting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_forfaiting_l_0 |  | fid,flocaleid |
| 2 | pk_lc_forfaiting_l |  | fpkid |

---

## 关联子实体-子表 t_lc_forfaiting_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_forfaiting_lk

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
| 1 | idx_lc_forfaiting_lk_fk |  | fid |
| 2 | pk_lc_forfaiting_lk |  | fpkid |
