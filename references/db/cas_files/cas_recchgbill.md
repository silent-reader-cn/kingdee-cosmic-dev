# 收款业务变更-cas_recchgbill

## 关联子实体-子表 t_cas_receivingbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_receivingbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_receivingbill_lk_pkey |  | fpkid |
| 2 | receiving_lk_fid |  | fid |

---

## 收款明细（变更前）-子表 t_cas_recbillchangbentry

- **表名称：** 收款明细（变更前）-子表
- **表名：** t_cas_recbillchangbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbfee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 3 | ftaxrate | 预估税率(%) | numeric | 23 | 10 | √ | 0 | 预估税率(%) |
| 4 | fsettledtaxlocalamt | 已核销税额本位币 | numeric | 23 | 10 | √ | 0 | 已核销税额本位币 |
| 5 | fbcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbrealreccompany | 实际收款公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 9 | fbunsettledamount | 未核销金额 | numeric | 19 | 6 | √ | 0.000000 | 未核销金额 |
| 10 | fsettledtaxamt | 已核销税额 | numeric | 23 | 10 | √ | 0 | 已核销税额 |
| 11 | fbreceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 12 | fbconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 13 | fbcorebillno | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 14 | fbremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 15 | fbsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbcontractnumber | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 17 | ftaxlocalamt | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 18 | ftaxamt | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | fbconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 20 | fbsuretyoutamt | 保证金转出金额 | numeric | 23 | 10 | √ | 0 | 保证金转出金额 |
| 21 | fbmatchselltag | 已匹配核心单据标识 | bpchar | 1 |  | √ | '0' | 已匹配核心单据标识 |
| 22 | fbdiscountlocamount | 现金折扣结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣结算本位币 |
| 23 | fbsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 24 | fbcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: PO :采购订单 ec_contract :建筑收入合同 ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 25 | fblocalfee | 手续费折本币 | numeric | 23 | 10 | √ | 0 | 手续费折本币 |
| 26 | fbactamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 27 | fbdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fbconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 30 | fbcorebillid | 核心单据id | varchar | 50 |  | √ | ' ' | 核心单据id |
| 31 | fbsettledlocalamt | 已核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 已核销金额结算本位币 |
| 32 | fbfundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 33 | fclaimbill | fclaimbill | varchar | 50 |  | √ | ' ' |  |
| 34 | fbcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 35 | fbreceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 36 | fbconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 37 | fbsettledamount | 已核销金额 | numeric | 19 | 6 | √ | 0.000000 | 已核销金额 |
| 38 | fbsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 39 | fbmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 40 | fbprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 41 | fbsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 42 | fbredisctamount | 折后金额折币种 | numeric | 23 | 10 | √ | 0 | 折后金额折币种 |
| 43 | fblenamount | 长短款 | numeric | 23 | 10 | √ | 0 | 长短款 |
| 44 | fbreceivablelocamount | 应收金额结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 应收金额结算本位币 |
| 45 | fbsuretyavbamt | 可用保证金 | numeric | 23 | 10 | √ | 0 | 可用保证金 |
| 46 | fbbizunit | 内部业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fblocallenamount | 长短款本位币 | numeric | 23 | 10 | √ | 0 | 长短款本位币 |
| 48 | fbunlockamount | 未锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 未锁定金额 |
| 49 | fbunsettledlocalamt | 未核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 未核销金额结算本位币 |
| 50 | fblocalamt | 实收折本币 | numeric | 19 | 6 | √ | 0.000000 | 实收折本币 |
| 51 | fblockamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 52 | fbexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recbillchangbentry_pkey |  | fentryid |
| 2 | idx_rbebchg_fid |  | fid |

---

## 收款业务变更-关联追踪表 t_cas_recchgbill_tc

- **表名称：** 收款业务变更-关联追踪表
- **表名：** t_cas_recchgbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | idx_cas_recchgbill_tc_tid |  | ftid |
| 2 | t_cas_recchgbill_tc_pkey |  | fid |
| 3 | idx_cas_recchgbill_tc_tbill |  | ftbillid |

---

## 收款明细（变更后）-子表 t_cas_recbillchangentry

- **表名称：** 收款明细（变更后）-子表
- **表名：** t_cas_recbillchangentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybizdate | fentrybizdate | timestamp | 0 |  |  | null |  |
| 3 | fbizunit | 内部业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 预估税率(%) | numeric | 23 | 10 | √ | 0 | 预估税率(%) |
| 5 | fsettledtaxlocalamt | 已核销税额本位币 | numeric | 23 | 10 | √ | 0 | 已核销税额本位币 |
| 6 | flocallenamount | 长短款本位币 | numeric | 23 | 10 | √ | 0 | 长短款本位币 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | forgsdividebatch | forgsdividebatch | varchar | 255 |  | √ | ' ' |  |
| 9 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 10 | fsettledtaxamt | 已核销税额 | numeric | 23 | 10 | √ | 0 | 已核销税额 |
| 11 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fsourcebillresentryid | fsourcebillresentryid | int8 | 64 |  | √ | 0 |  |
| 14 | frefundlockamt | frefundlockamt | numeric | 23 | 10 | √ | 0 |  |
| 15 | freceivablelocamount | 应收金额结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 应收金额结算本位币 |
| 16 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 17 | fcontractnumber | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 18 | frefundamt | frefundamt | numeric | 23 | 10 | √ | 0 |  |
| 19 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: PO :采购订单 ec_contract :建筑收入合同 ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 20 | funsettledamount | 未核销金额 | numeric | 19 | 6 | √ | 0.000000 | 未核销金额 |
| 21 | ftaxlocalamt | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 22 | ftaxamt | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 23 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 24 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 25 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fdiscountlocamount | 现金折扣结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣结算本位币 |
| 27 | fcorebillid | 核心单据id | varchar | 50 |  | √ | ' ' | 核心单据id |
| 28 | flenamount | 长短款 | numeric | 23 | 10 | √ | 0 | 长短款 |
| 29 | fmatchselltag | 已匹配核心单据标识 | bpchar | 1 |  | √ | '0' | 已匹配核心单据标识 |
| 30 | flocalfee | 手续费本位币 | numeric | 23 | 10 | √ | 0 | 手续费本位币 |
| 31 | factamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 32 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 33 | fcontractbatch | fcontractbatch | varchar | 255 |  | √ | ' ' |  |
| 34 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 37 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 38 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 39 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 40 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 41 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 42 | funsettledlocalamt | 未核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 未核销金额结算本位币 |
| 43 | fclaimbill | fclaimbill | varchar | 50 |  | √ | ' ' |  |
| 44 | fcorebillno | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 45 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 46 | fsuretyavbamt | 可用保证金 | numeric | 23 | 10 | √ | 0 | 可用保证金 |
| 47 | funlockamount | 未锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 未锁定金额 |
| 48 | fsettledlocalamt | 已核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 已核销金额结算本位币 |
| 49 | freceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 50 | fsuretyoutamt | 保证金转出金额 | numeric | 23 | 10 | √ | 0 | 保证金转出金额 |
| 51 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 52 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 53 | fblenamount | fblenamount | numeric | 23 | 10 | √ | 0 |  |
| 54 | frealreccompany | 实际收款公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 55 | fsourcechgbillentryid | 拆分明细源分录ID | int8 | 64 |  | √ | 0 | 拆分明细源分录ID |
| 56 | fsourcerecbillentryid | 收款单源单分录ID | int8 | 64 |  | √ | 0 | 收款单源单分录ID |
| 57 | fsourcebillnumber | fsourcebillnumber | varchar | 255 |  | √ | ' ' |  |
| 58 | flocalamt | 实收本位币 | numeric | 19 | 6 | √ | 0.000000 | 实收本位币 |
| 59 | frecorgid | frecorgid | int8 | 64 |  | √ | 0 |  |
| 60 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 61 | flockamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 62 | fdividestatus | fdividestatus | varchar | 30 |  | √ | ' ' |  |
| 63 | fsettledamount | 已核销金额 | numeric | 19 | 6 | √ | 0.000000 | 已核销金额 |
| 64 | fredisctamount | 折后金额折币种 | numeric | 23 | 10 | √ | 0 | 折后金额折币种 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rbechg_fid |  | fid |
| 2 | t_cas_recbillchangentry_pkey |  | fentryid |

---

## 收款明细（变更前）-分表 t_cas_recbillchangbentry_e

- **表名称：** 收款明细（变更前）-分表
- **表名：** t_cas_recbillchangbentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | '0' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 3 | fbcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 4 | fbpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | fbsalesman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 6 | fclaimbilltypeb | 认领单据类型 | varchar | 32 |  | √ | '' | 认领单据类型,枚举: sm_salorder :销售订单 ar_finarbill :财务应收单 |
| 7 | fbpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbsettlecur | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fbsettlemainbookid | 结算本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fclaimbillnob | 认领单据编号 | varchar | 64 |  | √ | '' | 认领单据编号 |
| 11 | fbsetexratetableid | 结算汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fbpurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 13 | fbbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fblicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 15 | fbcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fbsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 18 | fbsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbsetmainexrate | 结算本币兑本币汇率 | numeric | 23 | 10 | √ | 0 | 结算本币兑本币汇率 |
| 20 | fsrccontactunit | 源单往来单位（转销） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 21 | fbsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fclaimbillrowb | 认领单据行号 | int8 | 64 |  | √ | 0 | 认领单据行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_recbillchangbentry_e |  | fentryid |
| 2 | idx_recbillchangbentry_fid |  | fid |

---

## 收款业务变更-反写记录表 t_cas_recchgbill_wb

- **表名称：** 收款业务变更-反写记录表
- **表名：** t_cas_recchgbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recchgbill_wb_pkey |  | fentryid |
| 2 | idx_cas_recchgbill_wb_fk |  | fid |

---

## 收款明细（变更后）-分表 t_cas_recbillchangentry_e

- **表名称：** 收款明细（变更后）-分表
- **表名：** t_cas_recbillchangentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclaimbillrow | 认领单据行号 | int8 | 64 |  | √ | 0 | 认领单据行号 |
| 3 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | funmatchedamt | funmatchedamt | numeric | 23 | 10 | √ | 0 |  |
| 5 | fsetexratetableid | 结算汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 6 | fsalesman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 7 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 8 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 9 | fsettlecur | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fmatchedamt | fmatchedamt | numeric | 23 | 10 | √ | 0 |  |
| 11 | fisscmcexpense | fisscmcexpense | bpchar | 1 |  | √ | '0' |  |
| 12 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsetmainexrate | 结算本币兑本币汇率 | numeric | 23 | 10 | √ | 0 | 结算本币兑本币汇率 |
| 14 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 15 | fmpmtasknoid | fmpmtasknoid | int8 | 64 |  | √ | 0 |  |
| 16 | fcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 17 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 18 | fclaimbillno | 认领单据编号 | varchar | 64 |  | √ | '' | 认领单据编号 |
| 19 | fismatch | fismatch | bpchar | 1 |  | √ | '0' |  |
| 20 | fsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | '0' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 21 | fsalorderpush | fsalorderpush | bpchar | 1 |  | √ | '0' |  |
| 22 | fclaimbilltype | 认领单据类型 | varchar | 32 |  | √ | '' | 认领单据类型,枚举: sm_salorder :销售订单 ar_finarbill :财务应收单 |
| 23 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 24 | fsettlemainbookid | 结算本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsrccontactunit | 源单往来单位（转销） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rbchangentrye_fid |  | fid |
| 2 | pk_cas_recbillchangentry_e |  | fentryid |

---

## 收款业务变更-分表 t_cas_recbillchang_e

- **表名称：** 收款业务变更-分表
- **表名：** t_cas_recbillchang_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbpayername | 付款人 | varchar | 255 |  | √ | ' ' | 付款人 |
| 3 | fpayernumber | fpayernumber | varchar | 255 |  | √ | ' ' |  |
| 4 | fbfee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 5 | fsourcemigratedata | fsourcemigratedata | varchar | 80 |  | √ | ' ' |  |
| 6 | fbitempayertypeid | 付款人类型(多类别基础资料类型 前) | varchar | 30 |  | √ | ' ' | 付款人类型(多类别基础资料类型 前),枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 7 | fbbillstatus | 变更前单据状态 | varchar | 5 |  | √ | ' ' | 变更前单据状态,枚举: C :已审核 D :已收款 |
| 8 | fbexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | fadjusteprofitloss | fadjusteprofitloss | numeric | 23 | 10 | √ | 0 |  |
| 10 | fitempayertypeid | 付款人类型(多类别基础资料类型 后) | varchar | 30 |  | √ | ' ' | 付款人类型(多类别基础资料类型 后),枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 11 | fmigrateentrydata | fmigrateentrydata | varchar | 1000 |  | √ | ' ' |  |
| 12 | fispushrefund | fispushrefund | bpchar | 1 |  | √ | '0' |  |
| 13 | fprojectdataid | fprojectdataid | int8 | 64 |  | √ | 0 |  |
| 14 | fbackuserid | fbackuserid | int8 | 64 |  | √ | 0 |  |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | fchgreson | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 17 | fdetailid | fdetailid | varchar | 200 |  | √ | ' ' |  |
| 18 | fischgvoucher | 是否已更改凭证 | bpchar | 1 |  | √ | '0' | 是否已更改凭证 |
| 19 | fisclaimchange | fisclaimchange | bpchar | 1 |  | √ | '0' |  |
| 20 | frefundbatchseqid | frefundbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 21 | fischangeamount | fischangeamount | bpchar | 1 |  | √ | '0' |  |
| 22 | fbbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 23 | fvouchernum | fvouchernum | varchar | 255 |  | √ | ' ' |  |
| 24 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 25 | fbdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 26 | fsourcesys | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: cas :出纳 sm :销售 |
| 27 | fistransfer | 转销生成 | bpchar | 1 |  | √ | '0' | 转销生成 |
| 28 | fimagenumber | fimagenumber | varchar | 50 |  | √ | ' ' |  |
| 29 | fmatchdetailtype | fmatchdetailtype | varchar | 64 |  | √ | ' ' |  |
| 30 | fbankcheckflagtag | fbankcheckflagtag | text | 0 |  |  | null |  |
| 31 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 32 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 33 | fisunclaim | fisunclaim | bpchar | 1 |  | √ | '0' |  |
| 34 | fisperiod | fisperiod | bpchar | 1 |  | √ | '0' |  |
| 35 | fisvirtual | 是否虚拟收款单 | bpchar | 1 |  | √ | '0' | 是否虚拟收款单 |
| 36 | fitempayerid | 付款人(多类别基础资料) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fbitempayerid | 付款人(多类别基础资料) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fislockexratedate | fislockexratedate | bpchar | 1 |  | √ | '0' |  |
| 39 | fhandmttransdetail | fhandmttransdetail | bpchar | 1 |  | √ | '0' |  |
| 40 | fchangetype | 变更类型 | varchar | 30 |  | √ | ' ' | 变更类型,枚举: hand :手工变更 claim :认领变更 business :业务变更 |
| 41 | fbankcheckflagtag_tag | fbankcheckflagtag_tag | text | 0 |  |  | null |  |
| 42 | fbackdate | fbackdate | timestamp | 0 |  |  | null |  |
| 43 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 44 | fbreceivingtype | 收款用途（废弃） | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 45 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 46 | fismatchtransdetail | fismatchtransdetail | varchar | 16 |  | √ | '0' |  |
| 47 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 48 | fbsettletnumber | 结算号 | varchar | 2000 |  |  | ' ' | 结算号 |
| 49 | fchangeamount | fchangeamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fhotaccount | 红冲标识 | bpchar | 1 |  | √ | '0' | 红冲标识,枚举: 1 :被红冲单 2 :红冲单 |
| 51 | fisrefund | fisrefund | bpchar | 1 |  | √ | '0' |  |
| 52 | fbpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 53 | fisfullrefund | fisfullrefund | bpchar | 1 |  | √ | '0' |  |
| 54 | fbexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 55 | fbpayertype | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 56 | fbexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 57 | ftransfertype | 转销单据类型 | varchar | 30 |  | √ | ' ' | 转销单据类型,枚举: normal :普通单据 trans_red :新转销生成的红单 trans_blue :新转销生成的蓝单 |
| 58 | frecorgid | frecorgid | int8 | 64 |  | √ | 0 |  |
| 59 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 60 | fblocalamt | 折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 折本位币 |
| 61 | fbsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 62 | fbpaybankno | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_recechg_e |  | frefundbatchseqid |
| 2 | t_cas_recbillchang_e_pkey |  | fid |

---

## 收款业务变更-主表 t_cas_recbillchang

- **表名称：** 收款业务变更-主表
- **表名：** t_cas_recbillchang

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpaymentmode | fpaymentmode | varchar | 30 |  | √ | ' ' |  |
| 3 | fopenorgid | fopenorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 5 | fbankcheckflag | fbankcheckflag | varchar | 1024 |  | √ | ' ' |  |
| 6 | forgid | 收款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpayeebankid | fpayeebankid | int8 | 64 |  | √ | 0 |  |
| 8 | fk_bj73_dsorg | fk_bj73_dsorg | int8 | 64 |  | √ | 0 |  |
| 9 | freceivingtypeid | 收款用途（废弃） | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fpayeeacctbankid | 收款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 13 | fpayername | 付款人 | varchar | 255 |  | √ | ' ' | 付款人 |
| 14 | fclerk | fclerk | int8 | 64 |  | √ | 0 |  |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fcashierid | fcashierid | int8 | 64 |  | √ | 0 |  |
| 17 | fisagent | fisagent | bpchar | 1 |  | √ | '0' |  |
| 18 | ffundflowitem | ffundflowitem | int8 | 64 |  | √ | 0 |  |
| 19 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_recbill :收款单 |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fbsuretybiztype | 保证金业务类型 | varchar | 50 |  | √ | ' ' | 保证金业务类型,枚举: suretyrec :保证金收款 surety2sale :保证金转货款 surety2other :保证金转其他 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 24 | fpayeraccformid | fpayeraccformid | varchar | 30 |  | √ | ' ' |  |
| 25 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 28 | fpayeedate | fpayeedate | timestamp | 0 |  |  | null |  |
| 29 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 30 | fpayerbanknum | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 31 | fisdelete | 是否允许删除 | bpchar | 1 |  | √ | '0' | 是否允许删除 |
| 32 | fbusinesstype | fbusinesstype | int8 | 64 |  | √ | 0 |  |
| 33 | fhotaccountbillid | fhotaccountbillid | int8 | 64 |  | √ | 0 |  |
| 34 | fk_bj73_textfield2 | fk_bj73_textfield2 | varchar | 50 |  | √ | ' ' |  |
| 35 | fk_bj73_textfield1 | fk_bj73_textfield1 | varchar | 50 |  | √ | ' ' |  |
| 36 | fbiztype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: SalesRec :销售收款 OtherRec :其他收款 |
| 37 | fcreatorid | 变更申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | faccountcash | 收款账号 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 39 | fisarchive | fisarchive | bpchar | 1 |  | √ | '0' |  |
| 40 | factpayaccountid | factpayaccountid | int8 | 64 |  | √ | 0 |  |
| 41 | fpayerid | 付款人ID | int8 | 64 |  | √ | 0 | 付款人ID |
| 42 | fpayeracctbankid | fpayeracctbankid | int8 | 64 |  | √ | 0 |  |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fpayerbankid | fpayerbankid | int8 | 64 |  | √ | 0 |  |
| 45 | fsuretybiztype | 保证金业务类型 | varchar | 50 |  | √ | ' ' | 保证金业务类型,枚举: suretyrec :保证金收款 surety2sale :保证金转货款 surety2other :保证金转其他 |
| 46 | fcreatetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 47 | frecsourcebilltype | frecsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 48 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 49 | factrecamtsour | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 50 | fpayertypeid | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 51 | fpayerformid | fpayerformid | varchar | 30 |  | √ | ' ' |  |
| 52 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 53 | fsourcebillnumber | 源单编号 | varchar | 255 |  | √ | ' ' | 源单编号 |
| 54 | flocalamt | 实收本位币 | numeric | 19 | 6 | √ | 0.000000 | 实收本位币 |
| 55 | fsettletnumber | 结算号 | varchar | 255 |  | √ | ' ' | 结算号 |
| 56 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 57 | fk_bj73_dsamount | fk_bj73_dsamount | numeric | 23 | 10 |  | null |  |
| 58 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 59 | fk_bj73_textfield | fk_bj73_textfield | varchar | 50 |  | √ | ' ' |  |
| 60 | factrecamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 61 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recbillchang_pkey |  | fid |
| 2 | idx_cas_recechg_billno |  | fbillno |
| 3 | idx_cas_recechg_dateorg |  | fbizdate,forgid |
| 4 | idx_cas_recechg_statusorgid |  | fbillstatus,forgid |
