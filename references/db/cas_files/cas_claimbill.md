# 我的认领处理-cas_claimbill

## 我的认领处理-主表 t_cas_claimbill

- **表名称：** 我的认领处理-主表
- **表名：** t_cas_claimbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 3 | fsourceid | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 4 | fclaimtype | 类型 | varchar | 2 |  | √ | ' ' | 类型,枚举: 0 :认领 1 :变更 2 :申诉 3 :调整 |
| 5 | frecpayer | 付款人 | varchar | 255 |  | √ | ' ' | 付款人 |
| 6 | frecbilltype | 收款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 9 | frecviewpayee | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 10 | fdrawername | 出票人名称 | varchar | 80 |  | √ | ' ' | 出票人名称 |
| 11 | fsourceclaimid | 原认领单id | int8 | 64 |  | √ | 0 | 原认领单id |
| 12 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 13 | foppbanknumber | 对方账号 | varchar | 200 |  | √ | ' ' | 对方账号 |
| 14 | fpaymentee | fpaymentee | varchar | 255 |  | √ | ' ' |  |
| 15 | fpaymenttype | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 16 | fbillno | 认领单编号 | varchar | 30 |  | √ | ' ' | 认领单编号 |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 H :已作废 |
| 18 | fisnoticemerge | 通知单是否被合并 | bpchar | 1 |  | √ | '0' | 通知单是否被合并 |
| 19 | freamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 20 | frejectreason | 驳回原因 | varchar | 255 |  | √ | ' ' | 驳回原因 |
| 21 | fpayeetype | 收款人类型 | varchar | 50 |  | √ | ' ' | 收款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fclaimedamount | 已认领金额 | numeric | 23 | 10 | √ | 0 | 已认领金额 |
| 24 | frecviewpayer | 付款人 | varchar | 255 |  | √ | ' ' | 付款人 |
| 25 | funclaimamount | 未认领金额 | numeric | 23 | 10 | √ | 0 | 未认领金额 |
| 26 | ftradetime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 27 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 ticket :收票登记 |
| 28 | frecpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 29 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 30 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | faccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 33 | fsinglestream | 手续费独立流水 | bpchar | 1 |  | √ | '0' | 手续费独立流水 |
| 34 | frecpaytype | 收款用途 （废弃） | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 35 | ftradeid | 交易明细id | varchar | 50 |  | √ | ' ' | 交易明细id |
| 36 | fclaimno | 认领通知单 | varchar | 50 |  | √ | ' ' | 认领通知单 |
| 37 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 38 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: recticket :票据 rec :收款 pay :付款 |
| 39 | fpayamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 40 | ffee | 手续费 | numeric | 23 | 10 | √ | 0 | 手续费 |
| 41 | fclaimamount | 认领金额 | numeric | 19 | 6 | √ | 0.000000 | 认领金额 |
| 42 | fcreatorid | 认领人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fpaybilltype | 付款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 44 | fsourcetype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_claimcenterbill :认领通知单 |
| 45 | fclaimstatus | 认领通知单状态 | varchar | 2 |  | √ | ' ' | 认领通知单状态,枚举: 0 :待认领 1 :部分认领 2 :已认领 3 :已确认 4 :申诉中 5 :变更中 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | ftradedetailno | 交易明细编号 | varchar | 50 |  | √ | ' ' | 交易明细编号 |
| 49 | ftradeno | 明细流水号 | varchar | 50 |  | √ | ' ' | 明细流水号 |
| 50 | fpaytype | 付款用途 （废弃） | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 51 | frecpayorg | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 52 | fwritebackarfinarbill | 是否已调用反写财务应收单接口 | bpchar | 1 |  | √ | '0' | 是否已调用反写财务应收单接口 |
| 53 | fisconfireworkflow | 是否配置工作流 | varchar | 50 |  | √ | ' ' | 是否配置工作流 |
| 54 | fhandlestatus | 确认状态 | varchar | 30 |  | √ | '0' | 确认状态,枚举: 0 :未确认 1 :已确认 |
| 55 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 56 | frecbasetype | 收款人基础类型 | varchar | 50 |  | √ | ' ' | 收款人基础类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 57 | frecbasepayee | 收款人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 58 | fcenterorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 59 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | fbasepaymenttype | 付款人基础类型 | varchar | 50 |  | √ | ' ' | 付款人基础类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_claimbill_cb |  | fbillstatus,fclaimno |
| 2 | t_cas_claimbill_pkey |  | fid |
| 3 | idx_cas_claimbill_bo |  | fbillno |
| 4 | idx_cas_claimbill_co |  | fclaimno |

---

## 我的认领处理-多语言表 t_cas_claimbill_l

- **表名称：** 我的认领处理-多语言表
- **表名：** t_cas_claimbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_claimbill_l_pkey |  | fpkid |
| 2 | idx_cas_cbl_fid |  | fid |

---

## 我的认领处理-反写记录表 t_cas_claimbill_wb

- **表名称：** 我的认领处理-反写记录表
- **表名：** t_cas_claimbill_wb

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
| 1 | t_cas_claimbill_wb_pkey |  | fentryid |
| 2 | idx_cas_claimbill_wb_fk |  | fid |

---

## 付款认领单据体-子表 t_cas_claimpayentry

- **表名称：** 付款认领单据体-子表
- **表名：** t_cas_claimpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaycorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 3 | fpaysalesgroup | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 4 | fpayconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 5 | fpaybonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpaypurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 8 | fpaycorebillno | 核心单据编号 | varchar | 30 |  | √ | ' ' | 核心单据编号 |
| 9 | fpaysettlecur | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fpaysalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fpaycorebilltype | 核心单据类型 | varchar | 50 |  | √ | ' ' | 核心单据类型,枚举: ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 12 | fcontractnumber | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 13 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 14 | fpayremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 16 | fpaycorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 17 | fpaypurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 18 | fcontactunittype | 往来单位类型 | varchar | 80 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 19 | fpayconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 20 | fpayfundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 21 | fpaypurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fpaysalesman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 23 | fpayconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 24 | fpayconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 25 | fpaylicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 26 | fpaysalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fmobiledeldoneflag1 | 移动端删除完成标志 | int8 | 64 |  | √ | 0 | 移动端删除完成标志 |
| 28 | fpayconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fpaysettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fpaydiscountamt | 现金折扣 | numeric | 23 | 10 | √ | 0 | 现金折扣 |
| 31 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 32 | fepaytype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 33 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 34 | fpaymaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fpaypurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fpayactamt | 实付金额 | numeric | 23 | 10 | √ | 0 | 实付金额 |
| 38 | fpaycorebillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_claimpayentry |  | fentryid |
| 2 | idx_cas_claimpayentry |  | fid |

---

## 我的认领处理-关联追踪表 t_cas_claimbill_tc

- **表名称：** 我的认领处理-关联追踪表
- **表名：** t_cas_claimbill_tc

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
| 1 | idx_cas_claimbill_tc_tid |  | ftid |
| 2 | t_cas_claimbill_tc_pkey |  | fid |
| 3 | idx_cas_claimbill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_cas_claimdetailentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_claimdetailentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_claimdetailentry_lk |  | fpkid |
| 2 | idx_cas_claimdetailentry_lk_fk |  | fentryid |

---

## 单据体-子表 t_cas_claimdetailentry

- **表名称：** 单据体-子表
- **表名：** t_cas_claimdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsaleman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 4 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 5 | fecorebillno | 核心单据编号 | varchar | 64 |  | √ | '' | 核心单据编号 |
| 6 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 10 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 13 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 14 | fcorebillno | 认领单据编号 | varchar | 30 |  | √ | ' ' | 认领单据编号 |
| 15 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 16 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 17 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 18 | fsettlecur | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fecorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 20 | freceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 21 | fcorebilltype | 认领单据类型 | varchar | 30 |  | √ | ' ' | 认领单据类型,枚举: ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 22 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 25 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 27 | fcontactunittype | 往来单位类型 | varchar | 80 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 28 | fcorebillid | 认领单据ID | varchar | 50 |  | √ | ' ' | 认领单据ID |
| 29 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 30 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 31 | flenamount | 长短款 | numeric | 23 | 10 | √ | 0 | 长短款 |
| 32 | fecorebilltype | 核心单据类型 | varchar | 32 |  | √ | '' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 |
| 33 | factamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 34 | fcorebillentryseq | 认领单据行号 | int8 | 64 |  | √ | 0 | 认领单据行号 |
| 35 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 36 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fredisctamount | 折后金额折币种 | numeric | 19 | 6 | √ | 0 | 折后金额折币种 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fcorebillentryid | 认领单据行id | int8 | 64 |  | √ | 0 | 认领单据行id |
| 42 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_claimdetailentry_pkey |  | fentryid |
| 2 | idx_cas_claimd_id |  | fid |

---

## 关联子实体-子表 t_cas_claimbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_claimbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_claimbill_lk_pkey |  | fpkid |
| 2 | idx_cas_claimbill_lk_fk |  | fid |
