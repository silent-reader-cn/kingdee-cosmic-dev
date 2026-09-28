# 总账收款申请单-fr_glreim_recbill

## 资金反写分录-子表 t_fr_glrreccaswriteback

- **表名称：** 资金反写分录-子表
- **表名：** t_fr_glrreccaswriteback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwritebackbill | 单据类型 | varchar | 32 |  | √ | ' ' | 单据类型 |
| 3 | fwritebacktime | 反写时间 | timestamp | 0 |  |  | null | 反写时间 |
| 4 | fwritebackbillid | 下游单据id | int8 | 64 |  | √ | 0 | 下游单据id |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fwritebackop | 操作类型 | varchar | 16 |  | √ | ' ' | 操作类型 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fr_glrreccaswriteback_pkey |  | fentryid |
| 2 | idx_fr_glrreccaswb_fwbid |  | fwritebackbillid |

---

## 总账收款申请单-主表 t_fr_glrrecbill

- **表名称：** 总账收款申请单-主表
- **表名：** t_fr_glrrecbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | varchar | 36 |  | √ | ' ' | 汇率表 bd_exratetable |
| 3 | freceipteraccountid | 收款方银行账号id | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 4 | flocalcurrency | 币别（本位币） | varchar | 36 |  | √ | ' ' | 币种 bd_currency |
| 5 | freceipter | 收款方 | varchar | 36 |  | √ | ' ' | 业务单元 bos_org |
| 6 | fcastorecamount | 待收款金额 | numeric | 23 | 10 | √ | 0 | 待收款金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | faccountingorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fattachmentnum | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 11 | fclaimamount | 已冻结金额 | numeric | 23 | 10 | √ | 0 | 已冻结金额 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | freceipterbank | 行名行号 | varchar | 36 |  | √ | ' ' | 行名行号 bd_bebank |
| 14 | fbillno | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fvoucherid | 凭证号 | varchar | 36 |  | √ | ' ' | 凭证号 |
| 17 | frecbillno | 收款处理单据号 | varchar | 400 |  | √ | ' ' | 收款处理单据号 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核通过 E :审核不通过 F :废弃 |
| 19 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdept | 部门 | varchar | 36 |  | √ | ' ' | 业务单元 bos_org |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 24 | fisgenvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 25 | ftallydate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 26 | freceipterfinbank | 开户银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 27 | fimagenumber | 影像编码 | varchar | 36 |  | √ | ' ' | 影像编码 |
| 28 | ftype | 报账业务类型 | int8 | 64 |  | √ | 0 | 报账业务类型 bd_businessitem |
| 29 | frecamountsum | 记账合计金额 | numeric | 23 | 10 | √ | 0 | 记账合计金额 |
| 30 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 31 | freceipteraccount | 银行账号 | varchar | 36 |  | √ | ' ' | 银行账号 |
| 32 | fcasrecamount | 已收款金额 | numeric | 23 | 10 | √ | 0 | 已收款金额 |
| 33 | fcurrencyfield | 币别 | varchar | 36 |  | √ | ' ' | 币种 bd_currency |
| 34 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fstandardrecamountsum | 记账合计金额（本位币） | numeric | 23 | 10 | √ | 0 | 记账合计金额（本位币） |
| 37 | fcompanyid | 申请人公司 | varchar | 36 |  | √ | ' ' | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fr_glrrecbill |  | fid |
| 2 | idx_fr_glrrecbill_billno |  | fbillno |

---

## 结算信息-子表 t_fr_glrrecsettleentry

- **表名称：** 结算信息-子表
- **表名：** t_fr_glrrecsettleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayeraccountid | 付款方银行账号id | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 3 | fcustomer | 付款人（客户） | varchar | 36 |  | √ | ' ' | 客户 bd_customer |
| 4 | fpayertype | 付款方类型 | varchar | 36 |  | √ | ' ' | 付款方类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :内部公司 er_payeer :人员 other :其他 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpayer | 付款人（个人） | varchar | 36 |  | √ | ' ' | 收款信息 er_payeer |
| 7 | fcasorg | 付款人（内部公司） | varchar | 36 |  | √ | ' ' | 业务单元 bos_org |
| 8 | fpayerbank | 开户银行 | varchar | 36 |  | √ | ' ' | 行名行号 bd_bebank |
| 9 | fpayername | 付款方 | varchar | 50 |  | √ | ' ' | 付款方 |
| 10 | fsupplier | 付款人（供应商） | varchar | 36 |  | √ | ' ' | 供应商 bd_supplier |
| 11 | frecamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 12 | fstandardrecamount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 13 | fsettlementtype | 结算方式 | varchar | 36 |  | √ | ' ' | 结算方式 bd_settlementtype |
| 14 | fpayeraccount | 银行账号 | varchar | 36 |  | √ | ' ' | 银行账号 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_glrrecsettleentry_id |  | fid |
| 2 | pk_t_fr_glrrecsettleentry |  | fdetailid |

---

## 核销付款-子表 t_fr_glrreccaventry

- **表名称：** 核销付款-子表
- **表名：** t_fr_glrreccaventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcdescription | 事由 | varchar | 500 |  | √ | ' ' | 事由 |
| 3 | fsourceentryid | 原单分录id | varchar | 36 |  | √ | ' ' | 原单分录id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcavunpayamount | 可核销金额 | numeric | 23 | 10 | √ | 0 | 可核销金额 |
| 6 | fsourcecurrency | 原单币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fcreceiptertype | 收款方类型 | bpchar | 1 |  | √ | ' ' | 收款方类型 |
| 8 | fpayamount | 报账金额 | numeric | 23 | 10 | √ | 0 | 报账金额 |
| 9 | fsourcelocalcurrency | 原单币别（本位币） | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fstandardpayamount | 报账金额（本位币） | numeric | 23 | 10 | √ | 0 | 报账金额（本位币） |
| 11 | fccavrouteamount | 在途核销金额 | numeric | 23 | 10 | √ | 0 | 在途核销金额 |
| 12 | fcavpayamount | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 13 | fcremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fcbiztypedetail | 业务项目 | varchar | 36 |  | √ | ' ' | 费用项目 er_expenseitemedit |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fccavamount | 已核销金额 | numeric | 23 | 10 | √ | 0 | 已核销金额 |
| 17 | fcbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fcreceipter | 收款方 | varchar | 36 |  | √ | ' ' | 收款方 |
| 19 | fsourcebillno | 原单编码 | varchar | 36 |  | √ | ' ' | 原单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_glrreccaventry_id |  | fid |
| 2 | pk_t_fr_glrreccaventry |  | fdetailid |

---

## 总账收款申请单-多语言表 t_fr_glrrecbill_l

- **表名称：** 总账收款申请单-多语言表
- **表名：** t_fr_glrrecbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fr_glrrecbill_l |  | fpkid |
| 2 | idx_fr_glrrecbill_flocaleid |  | fid,flocaleid |

---

## 记账明细-子表 t_fr_glrrectallyentry

- **表名称：** 记账明细-子表
- **表名：** t_fr_glrrectallyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbiztypedetail | 业务项目 | varchar | 36 |  | √ | ' ' | 费用项目 er_expenseitemedit |
| 3 | fstandardtallyamount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0 | 收款金额（本位币） |
| 4 | fdepartment | 部门 | varchar | 36 |  | √ | ' ' | 业务单元 bos_org |
| 5 | ftbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | ftallyvoucherid | 凭证号 | varchar | 36 |  | √ | ' ' | 凭证号 |
| 7 | ftallyamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 8 | ftcostcenter | 成本中心 | varchar | 36 |  | √ | ' ' | 成本中心 bos_costcenter |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | ftremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_glrrectallyentry_id |  | fid |
| 2 | pk_t_fr_glrrectallyentry |  | fdetailid |
