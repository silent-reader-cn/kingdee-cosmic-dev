# 收款业务变更-cas_recbill_change

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

## 收款明细-子表 t_cas_recbillchangbentry

- **表名称：** 收款明细-子表
- **表名：** t_cas_recbillchangbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbfee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 3 | fbconbillentity | fbconbillentity | varchar | 255 |  | √ | ' ' |  |
| 4 | fbcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbrealreccompany | 实际收款公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbcorebillid | 核心单据id | varchar | 50 |  | √ | ' ' | 核心单据id |
| 8 | fbsettledlocalamt | 已核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 已核销金额结算本位币 |
| 9 | fbfundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 10 | fbconbillrownum | fbconbillrownum | varchar | 255 |  | √ | ' ' |  |
| 11 | fclaimbill | fclaimbill | varchar | 50 |  | √ | ' ' |  |
| 12 | fbunsettledamount | 未核销金额 | numeric | 19 | 6 | √ | 0.000000 | 未核销金额 |
| 13 | fbcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 14 | fbreceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 15 | fbconbillid | fbconbillid | int8 | 64 |  | √ | 0 |  |
| 16 | fbreceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 17 | fbconbillentryid | fbconbillentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fbcorebillno | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 19 | fbremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 20 | fbsettledamount | 已核销金额 | numeric | 19 | 6 | √ | 0.000000 | 已核销金额 |
| 21 | fbsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 23 | fbmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 24 | fbcontractnumber | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 25 | fbprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | fbsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 27 | fbredisctamount | 折后金额折币别 | numeric | 23 | 10 | √ | 0 | 折后金额折币别 |
| 28 | fbconbillnumber | fbconbillnumber | varchar | 255 |  | √ | ' ' |  |
| 29 | fbreceivablelocamount | 应收金额折结算本币 | numeric | 19 | 6 | √ | 0.000000 | 应收金额折结算本币 |
| 30 | fbmatchselltag | 已匹配核心单据标识 | bpchar | 1 |  | √ | '0' | 已匹配核心单据标识 |
| 31 | fbdiscountlocamount | 现金折扣结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣结算本位币 |
| 32 | fbsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 33 | fbbizunit | 内部业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fbcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: PO :采购订单 ec_contract :建筑收入合同 ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 35 | fbunlockamount | 未锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 未锁定金额 |
| 36 | fblocalfee | 手续费折本币 | numeric | 23 | 10 | √ | 0 | 手续费折本币 |
| 37 | fbunsettledlocalamt | 未核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 未核销金额结算本位币 |
| 38 | fblocalamt | 实收折本币 | numeric | 19 | 6 | √ | 0.000000 | 实收折本币 |
| 39 | fblockamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 40 | fbactamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 41 | fbdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fbexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

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

## 结算信息-子表 t_cas_recchgsettleentry

- **表名称：** 结算信息-子表
- **表名：** t_cas_recchgsettleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 3 | fsettleremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recchgsettleentry_pkey |  | fentryid |
| 2 | idx_rbesettlechg_fid |  | fid |

---

## 关联子实体-子表 t_cas_receivingbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_receivingbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rbelk_fentryid |  | fentryid |
| 2 | t_cas_receivingbillentry_lk_pkey |  | fpkid |
| 3 | idx_rbelk_fseq |  | fseq |

---

## 单据体-子表 t_cas_recbankcheckflag

- **表名称：** 单据体-子表
- **表名：** t_cas_recbankcheckflag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | febankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_rbc_fid |  | fid |
| 2 | idx_cas_recbankcheckflag |  | febankcheckflag |
| 3 | pk_t_cas_recbankcheckflag |  | fentryid |

---

## 收款明细-子表 t_cas_recbillchangentry

- **表名称：** 收款明细-子表
- **表名：** t_cas_recbillchangentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | fbizunit | 内部业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | forgsdividebatch | forgsdividebatch | varchar | 255 |  | √ | ' ' |  |
| 6 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 7 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 8 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 9 | fsourcebillresentryid | 变更拆分分录ID | int8 | 64 |  | √ | 0 | 变更拆分分录ID |
| 10 | frefundlockamt | 关联退款金额 | numeric | 23 | 10 | √ | 0 | 关联退款金额 |
| 11 | freceivablelocamount | 应收金额结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 应收金额结算本位币 |
| 12 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 13 | fcontractnumber | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 14 | frefundamt | 退款金额 | numeric | 23 | 10 | √ | 0 | 退款金额 |
| 15 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: PO :采购订单 ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 er_repaymentbill :还款单 im_transapply :调拨申请单 amccsa_custschdorder :销售计划协议 amccsa_custschdorder_init :期初销售计划协议 pm_purorderbill :采购订单 occba_moneyincome :资金收入单 |
| 16 | funsettledamount | 未核销金额 | numeric | 19 | 6 | √ | 0.000000 | 未核销金额 |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 18 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 19 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fdiscountlocamount | 现金折扣结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣结算本位币 |
| 21 | fcorebillid | 认领单据id | varchar | 50 |  | √ | ' ' | 认领单据id |
| 22 | fmatchselltag | 已匹配核心单据标识 | bpchar | 1 |  | √ | '0' | 已匹配核心单据标识 |
| 23 | flocalfee | 手续费本位币 | numeric | 23 | 10 | √ | 0 | 手续费本位币 |
| 24 | factamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 25 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 26 | fcontractbatch | 挂合同批次号 | varchar | 255 |  | √ | ' ' | 挂合同批次号 |
| 27 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fcorebillentryid | 认领单据行id | int8 | 64 |  | √ | 0 | 认领单据行id |
| 30 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 31 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 32 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 33 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 34 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 35 | funsettledlocalamt | 未核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 未核销金额结算本位币 |
| 36 | fclaimbill | 认领单编码 | varchar | 50 |  | √ | ' ' | 认领单编码 |
| 37 | fcorebillno | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 38 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 39 | funlockamount | 未锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 未锁定金额 |
| 40 | fsettledlocalamt | 已核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 已核销金额结算本位币 |
| 41 | freceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 42 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 43 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 44 | frealreccompany | 实际收款公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fsourcechgbillentryid | 拆分明细源分录ID | int8 | 64 |  | √ | 0 | 拆分明细源分录ID |
| 46 | fsourcerecbillentryid | 收款单源单分录ID | int8 | 64 |  | √ | 0 | 收款单源单分录ID |
| 47 | flocalamt | 实收金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 实收金额本位币 |
| 48 | frecorgid | 收款组织(虚拟收款用) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 50 | flockamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 51 | fdividestatus | 清分状态 | varchar | 30 |  | √ | ' ' | 清分状态,枚举: normal :正常 waitdivide :待清分 yetdivide :已清分 |
| 52 | fsettledamount | 已核销金额 | numeric | 19 | 6 | √ | 0.000000 | 已核销金额 |
| 53 | fredisctamount | 折后金额折币别 | numeric | 23 | 10 | √ | 0 | 折后金额折币别 |

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

## 收款业务变更-反写记录表 t_cas_receivingbill_wb

- **表名称：** 收款业务变更-反写记录表
- **表名：** t_cas_receivingbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  |  | null |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  |  | null |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_rbtlwb_fid |  | fid |
| 2 | receiving_wb_fid_fsid |  | fsid,fsbillid |
| 3 | t_cas_receivingbill_wb_pkey |  | fentryid |

---

## 收款明细-分表 t_cas_recbillchangbentry_e

- **表名称：** 收款明细-分表
- **表名：** t_cas_recbillchangbentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | '0' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 3 | fbcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :职员 cas_othercontactunit :其他 |
| 4 | fbpurchaser | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | fbsalesman | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | fclaimbilltypeb | 认领单据类型 | varchar | 32 |  | √ | '' | 认领单据类型,枚举: sm_salorder :销售订单 ar_finarbill :财务应收单 |
| 7 | fbpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbsettlecur | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fbsettlemainbookid | 结算本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fclaimbillnob | 认领单据编号 | varchar | 64 |  | √ | '' | 认领单据编号 |
| 11 | fbsetexratetableid | 结算汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 12 | fbpurdept | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 13 | fbcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fbsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 16 | fbsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbsetmainexrate | 结算本币兑本币汇率 | numeric | 23 | 10 | √ | 0 | 结算本币兑本币汇率 |
| 18 | fbsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fclaimbillrowb | 认领单据行号 | int8 | 64 |  | √ | 0 | 认领单据行号 |

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

## 流水信息-子表 t_cas_receivinginfoentry

- **表名称：** 流水信息-子表
- **表名：** t_cas_receivinginfoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbeicreditamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 3 | fbeibillno | 交易明细编号 | varchar | 50 |  | √ | ' ' | 交易明细编号 |
| 4 | fcdmdraftbillno | 票据号码 | varchar | 50 |  | √ | ' ' | 票据号码 |
| 5 | fbeidetailid | 交易流水号 | varchar | 50 |  | √ | ' ' | 交易流水号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finfoid | 流水ID | int8 | 64 |  | √ | 0 | 流水ID |
| 8 | fbeicurrency | 交易明细币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcdmcurrency | 票据币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 11 | fcdmamount | 票面金额 | numeric | 19 | 6 | √ | 0.000000 | 票面金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_recinfoentry_fpid |  | fid |
| 2 | pk_t_cas_receivinginfoentry |  | fentryid |

---

## 结算号基础资料(隐藏)-多选基础资料表 t_cas_recbill_bl

- **表名称：** 结算号基础资料(隐藏)-多选基础资料表
- **表名：** t_cas_recbill_bl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 应收应付票据登记 cdm_payandrecdraft_f7 |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_recbill_bl_fk |  | fid |
| 2 | pk_t_cas_recbill_bl |  | fpkid |

---

## 票据信息-子表 t_cas_recbillchdraftentry

- **表名称：** 票据信息-子表
- **表名：** t_cas_recbillchdraftentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdraftamt | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.00 | 票面金额(子票包金额) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fourbankid | 我方银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_recbillchdraftentry |  | fentryid |
| 2 | idx_cas_rebchdraftentry_fid |  | fid |

---

## 收款业务变更-关联追踪表 t_cas_receivingbill_tc

- **表名称：** 收款业务变更-关联追踪表
- **表名：** t_cas_receivingbill_tc

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
| 1 | idx_cas_recetc_fsbillid |  | fsbillid |
| 2 | receiving_tc_ftbillid |  | ftbillid |
| 3 | idx_cas_receivingbill_tc_tid |  | ftid |
| 4 | idx_cas_receivingbill_tc_tbill |  | ftbillid |
| 5 | t_cas_receivingbill_tc_pkey |  | fid |

---

## 收款明细-分表 t_cas_recbillchangentry_e

- **表名称：** 收款明细-分表
- **表名：** t_cas_recbillchangentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclaimbillrow | 认领单据行号 | int8 | 64 |  | √ | 0 | 认领单据行号 |
| 3 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 4 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 5 | fcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 6 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 7 | fclaimbillno | 认领单据编号 | varchar | 64 |  | √ | '' | 认领单据编号 |
| 8 | fsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | '0' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 9 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsetexratetableid | 结算汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 11 | fsalesman | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 12 | fclaimbilltype | 认领单据类型 | varchar | 32 |  | √ | '' | 认领单据类型,枚举: sm_salorder :销售订单 ar_finarbill :财务应收单 |
| 13 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 14 | fsettlecur | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | fsettlemainbookid | 结算本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fsetmainexrate | 结算本币兑本币汇率 | numeric | 23 | 10 | √ | 0 | 结算本币兑本币汇率 |

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
| 3 | fpayernumber | 付款单位编码（废弃） | varchar | 255 |  | √ | ' ' | 付款单位编码（废弃） |
| 4 | fbfee | 变更前手续费 | numeric | 19 | 6 | √ | 0.000000 | 变更前手续费 |
| 5 | fbitempayertypeid | 付款人类型(多类别基础资料类型) | varchar | 30 |  | √ | ' ' | 付款人类型(多类别基础资料类型),枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 other :其他 cas_othercontactunit :其他往来单位 |
| 6 | fbbillstatus | 变更前单据状态 | varchar | 5 |  | √ | ' ' | 变更前单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已收款 |
| 7 | fbexratetableid | 变更前汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 8 | fadjusteprofitloss | 调整损益 | numeric | 23 | 10 | √ | 0 | 调整损益 |
| 9 | fitempayertypeid | 付款单位类型（隐藏） | varchar | 30 |  | √ | ' ' | 付款单位类型（隐藏）,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 10 | fispushrefund | 是否直接退款 | bpchar | 1 |  | √ | '0' | 是否直接退款 |
| 11 | fprojectdataid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 12 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | fchgreson | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 15 | fischgvoucher | 是否已更改凭证 | bpchar | 1 |  | √ | '0' | 是否已更改凭证 |
| 16 | fisclaimchange | 是否来源认领变更 | bpchar | 1 |  | √ | '0' | 是否来源认领变更 |
| 17 | frefundbatchseqid | 退款批次号 | varchar | 80 |  | √ | ' ' | 退款批次号 |
| 18 | fbbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 19 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 20 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 21 | fbdescription | 变更前摘要 | varchar | 255 |  | √ | ' ' | 变更前摘要 |
| 22 | fsourcesys | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: cas :出纳 sm :销售 |
| 23 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 24 | fmatchdetailtype | 匹配流水方式 | varchar | 64 |  | √ | ' ' | 匹配流水方式,枚举: rule :自动生成 hand :手工生成 automatch :自动匹配 handmatch :手工匹配 claim :认领生成 noclaim :未认领生成 beipay :对账标识码匹配 ecommerce :电商流水合并生成 |
| 25 | fbankcheckflagtag | 对账标识码 | text | 0 |  |  | null | 对账标识码 |
| 26 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fisunclaim | 是否未认领入账 | bpchar | 1 |  | √ | '0' | 是否未认领入账 |
| 29 | fisperiod | 往来期初 | bpchar | 1 |  | √ | '0' | 往来期初 |
| 30 | fisvirtual | 是否虚拟收款单 | bpchar | 1 |  | √ | '0' | 是否虚拟收款单 |
| 31 | fitempayerid | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 32 | fbitempayerid | 付款人(多类别基础资料) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fhandmttransdetail | 手工匹配关联银行交易明细 | bpchar | 1 |  | √ | '0' | 手工匹配关联银行交易明细 |
| 34 | fchangetype | 变更类型 | varchar | 30 |  | √ | ' ' | 变更类型,枚举: hand :手工变更 claim :认领变更 business :业务变更 |
| 35 | fbankcheckflagtag_tag | 对账标识码_详情 | text | 0 |  |  | null | 对账标识码_详情 |
| 36 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 37 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 38 | fbreceivingtype | 收款用途（废弃） | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 39 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | fismatchtransdetail | 是否匹配流水 | varchar | 16 |  | √ | '0' | 是否匹配流水 |
| 41 | finneraccountid | 账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 42 | fbsettletnumber | 结算号 | varchar | 30 |  | √ | ' ' | 结算号 |
| 43 | fhotaccount | 红冲标识 | bpchar | 1 |  | √ | '0' | 红冲标识,枚举: 1 :被红冲单 2 :红冲单 |
| 44 | fisrefund | 退款退票业务 | bpchar | 1 |  | √ | '0' | 退款退票业务 |
| 45 | fbpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 46 | fisfullrefund | 全额退款 | bpchar | 1 |  | √ | '0' | 全额退款 |
| 47 | fbexratedate | 变更前汇率日期 | timestamp | 0 |  |  | null | 变更前汇率日期 |
| 48 | fbpayertype | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :职员 other :其他 cas_othercontactunit :其他往来单位 |
| 49 | fbexchangerate | 变更前汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 变更前汇率 |
| 50 | frecorgid | 代收款核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 52 | fblocalamt | 折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 折本位币 |
| 53 | fbsettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 54 | fbpaybankno | 付款账户 | varchar | 255 |  | √ | ' ' | 付款账户 |

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
| 2 | fpaymentmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: cash :现销 credit :赊销 |
| 3 | fopenorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbankcheckflag | 对账标识码(旧) | varchar | 1024 |  | √ | ' ' | 对账标识码(旧) |
| 5 | forgid | 收款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 7 | freceivingtypeid | 收款用途（废弃） | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 收款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 收款汇率 |
| 10 | fpayeeacctbankid | 收款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 11 | fpayername | 付款单位 | varchar | 255 |  | √ | ' ' | 付款单位 |
| 12 | fclerk | 会计 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fisagent | 代理收款 | bpchar | 1 |  | √ | '0' | 代理收款 |
| 16 | ffundflowitem | 资金流量项目 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 17 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_recbill :收款单 er_repaymentbill :还款单 cas_betransdetail :交易明细 ar_finarbill :财务应收单 cas_paybill :付款单 fca_transdownbill :下拨单 sm_salorder :销售订单 cfm_loanbill :提款单 cdm_drafttradebill :票据业务处理单 ec_incomeapply :建筑请款单 cas_claimcenterbill :认领通知单 bei_intelrec :收款入账中心 bei_transdetail :交易明细 cim_invest_repaybill :本金收回 cim_invest_interestbill :收息处理 fca_transupbill :上划单 cfm_feebill :费用明细单 lc_present :交单处理 lc_forfaiting :福费廷 tm_businessbill :生命周期操作 ifm_loanbill :贷款放款处理 cdm_receivablebill :应收票据 cfm_loanbill_bond :债券发行 tm_structdeposit :结构性存款 tm_rateswap :互换 tm_bond_fix :固定利率债券/零息债券 tm_bond_float :浮动利率债券 tm_forex_options :外汇期权 cim_release :定期存款解活处理 cim_noticerelease :通知存款解活处理 scf_finrecbill :供应链融资收款处理 ifm_currentintbill :内部利息结息单 ifm_transrecvbill :收款结算单 pac_projectsuretybill :项目保证金 occba_moneyincome :资金收入单 ifm_linkpaybill :联动支付 |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已收款 E :变更中 F :收款处理中 G :已退单 H :已作废 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 21 | fpayeraccformid | 付款账户类型标识ID | varchar | 30 |  | √ | ' ' | 付款账户类型标识ID |
| 22 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 25 | fpayeedate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fpayerbanknum | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 28 | fisdelete | 是否允许删除 | bpchar | 1 |  | √ | '0' | 是否允许删除 |
| 29 | fbusinesstype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 30 | fhotaccountbillid | 红冲源单id | int8 | 64 |  | √ | 0 | 红冲源单id |
| 31 | fbiztype | 业务类型（已废弃） | varchar | 30 |  | √ | ' ' | 业务类型（已废弃）,枚举: SalesRec :销售收款 OtherRec :其他收款 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | faccountcash | 收款账号 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 34 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 35 | factpayaccountid | 实际付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 36 | fpayerid | 付款单位ID（废弃） | int8 | 64 |  | √ | 0 | 付款单位ID（废弃） |
| 37 | fpayeracctbankid | 付款账户ID | int8 | 64 |  | √ | 0 | 付款账户ID |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | frecsourcebilltype | 原收款单源单类型 | varchar | 50 |  | √ | ' ' | 原收款单源单类型,枚举: cas_recbill :收款单 er_repaymentbill :还款单 cas_betransdetail :交易明细 ar_finarbill :财务应收单 cas_paybill :付款单 fca_transdownbill :下拨单 sm_salorder :销售订单 cfm_loanbill :提款单 cdm_drafttradebill :业务处理 ec_incomeapply :建筑请款单 cas_claimcenterbill :认领通知单 bei_intelrec :收款入账中心 bei_transdetail :交易明细 cim_invest_repaybill :本金收回 cim_invest_interestbill :收息处理 fca_transupbill :上划单 cfm_feebill :费用明细单 lc_present :交单处理 lc_forfaiting :福费廷 tm_businessbill :生命周期操作 ifm_loanbill :贷款放款处理 cdm_receivablebill :收票登记 cfm_loanbill_bond :债券发行 tm_structdeposit :结构性存款 tm_rateswap :互换 tm_bond_fix :固定利率债券/零息债券 tm_bond_float :浮动利率债券 tm_forex_options :外汇期权 cim_release :定期存款解活处理 cim_noticerelease :通知存款解活处理 scf_finrecbill :供应链融资收款处理 |
| 42 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 43 | factrecamtsour | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 44 | fpayertypeid | 付款单位类型 | varchar | 30 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 45 | fpayerformid | 付款单位类型标识ID（废弃） | varchar | 30 |  | √ | ' ' | 付款单位类型标识ID（废弃） |
| 46 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 47 | fsourcebillnumber | 源单编号 | varchar | 255 |  | √ | ' ' | 源单编号 |
| 48 | flocalamt | 收款金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 收款金额本位币 |
| 49 | fsettletnumber | 结算号 | varchar | 255 |  | √ | ' ' | 结算号 |
| 50 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 51 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 52 | factrecamt | 收款金额比较 | numeric | 19 | 6 | √ | 0.000000 | 收款金额比较 |
| 53 | fcurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
