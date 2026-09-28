# 总账付款申请单-fr_glreim_paybill

## 总账付款申请单-多语言表 t_fr_glrpaybill_l

- **表名称：** 总账付款申请单-多语言表
- **表名：** t_fr_glrpaybill_l

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
| 1 | idx_fr_glrpaybill_flocaleid |  | fid,flocaleid |
| 2 | pk_t_fr_glrpaybill_l |  | fpkid |

---

## 关联申请分录-子表 t_fr_glrassoapply

- **表名称：** 关联申请分录-子表
- **表名：** t_fr_glrassoapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillentitynum | fbillentitynum | varchar | 30 |  | √ | ' ' |  |
| 3 | fapplydate_aa | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 4 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | freimamount_aa | 报账金额 | numeric | 23 | 10 | √ | 0 | 报账金额 |
| 6 | fassoreimbillnum | 关联报账单号 | varchar | 80 |  | √ | ' ' | 关联报账单号 |
| 7 | fcontractnum_aa | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdescrible_aa | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 10 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcurrency_aa | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fassoreimbillid | 关联报账单id | varchar | 50 |  | √ | ' ' | 关联报账单id |
| 14 | fbiztype_aa | 报账业务类型 | int8 | 64 |  | √ | 0 | [报账业务类型 bd_businessitem](../fibd_files/bd_businessitem.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_glrassoappl_fid |  | fid |
| 2 | pk_fr_glrassoapply |  | fentryid |

---

## 总账付款申请单-主表 t_fr_glrpaybill

- **表名称：** 总账付款申请单-主表
- **表名：** t_fr_glrpaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fpayee | 收款方 | varchar | 50 |  | √ | ' ' | 收款方 |
| 4 | ftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 5 | fpayer | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | flocalcurrency | 币别（本位币） | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fpayerbank | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | faccountingorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fattachmentnum | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 12 | fbiztype | 报账业务类型 | int8 | 64 |  | √ | 0 | [报账业务类型 bd_businessitem](../fibd_files/bd_businessitem.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftotalamountloc | 合计金额（本位币） | numeric | 23 | 10 | √ | 0 | 合计金额（本位币） |
| 17 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核通过 E :审核不通过 F :废弃 |
| 19 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdept | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fpayeetype | 收款方类型 | varchar | 16 |  | √ | ' ' | 收款方类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 er_payeer :职员 other :其他 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 25 | fpayeeid | 收款方_id | varchar | 50 |  | √ | ' ' | 收款方_id |
| 26 | fisgenvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 27 | ftallydate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fpayeebank | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 29 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 30 | fpayeeaccbank | 收款银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 31 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 32 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 33 | fcontractnum | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 34 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fpayeraccount | 付款账号 | varchar | 50 |  | √ | ' ' | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 36 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fpayeeaccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 39 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_glrpaybill_billno |  | fbillno |
| 2 | pk_t_fr_glrpaybill |  | fid |

---

## 记账明细分录-子表 t_fr_glrpaytallydetail

- **表名称：** 记账明细分录-子表
- **表名：** t_fr_glrpaytallydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fbizdetailtype | 业务项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fdept_t | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 6 | ftallyamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbizdate_t | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fcontractnum_t | 合同 | varchar | 50 |  | √ | ' ' | 合同 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fr_glrpaytallydetail |  | fentryid |
| 2 | idx_fr_glrpaybill_fid |  | fid |

---

## 付款计划分录-子表 t_fr_glrpayplan

- **表名称：** 付款计划分录-子表
- **表名：** t_fr_glrpayplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark_pp | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fsettletype_pp | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 4 | fsettledamt | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 5 | funlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0 | 未锁定金额 |
| 6 | fplanduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 7 | funsettleamt | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0 | 已锁定金额 |
| 10 | fpayamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fr_glrpayplan |  | fentryid |
| 2 | idx_fr_glrpayplan_fid |  | fid |

---

## 付款计划子分录(反写)-子表 t_fr_glrpayplanwriteback

- **表名称：** 付款计划子分录(反写)-子表
- **表名：** t_fr_glrpayplanwriteback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperate | 反写操作 | varchar | 16 |  | √ | ' ' | 反写操作 |
| 2 | fwritebacktime | 反写时间 | timestamp | 0 |  |  | null | 反写时间 |
| 3 | ftargetentity | 下游单据标识 | varchar | 32 |  | √ | ' ' | 下游单据标识 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | ftargetentryid | 下游单据分录ID | int8 | 64 |  | √ | 0 | 下游单据分录ID |
| 8 | ftargetid | 下游单据ID | int8 | 64 |  | √ | 0 | 下游单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_glrpayplanwb_fentryid |  | fentryid |
| 2 | t_fr_glrpayplanwriteback_pkey |  | fdetailid |
