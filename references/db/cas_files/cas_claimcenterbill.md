# 收付认领处理中心-cas_claimcenterbill

## 付款认领明细-子表 t_cas_claimnoticebillp_e

- **表名称：** 付款认领明细-子表
- **表名：** t_cas_claimnoticebillp_e

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
| 8 | fpaybillstatus | 是否作废 | bpchar | 1 |  | √ | '0' | 是否作废 |
| 9 | fpayhandlestatus | 是否确认 | bpchar | 1 |  | √ | '0' | 是否确认 |
| 10 | fpayclaimtype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :认领 1 :变更 2 :申诉 3 :调整 4 :作废 |
| 11 | fpaysourceentryid | 原分录id | int8 | 64 |  | √ | 0 | 原分录id |
| 12 | fpaycorebillno | 核心单据编号 | varchar | 30 |  | √ | ' ' | 核心单据编号 |
| 13 | fpaysettlecur | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fpaysalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fpaycorebilltype | 核心单据类型 | varchar | 50 |  | √ | ' ' | 核心单据类型,枚举: ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 16 | fcontractnumber | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 17 | fpayclaimbill | 认领单 | varchar | 30 |  | √ | ' ' | 认领单 |
| 18 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 19 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fpayremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fpaycorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 22 | fpaypurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 23 | fpayfundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 24 | fpayconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 25 | fpaypurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fpaysalesman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 27 | fpayconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 28 | fe_contactunitp | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fpayconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 30 | fpaylicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | fpaysalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fe_contactunittypep | 往来单位类型 | varchar | 80 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 33 | fpayconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 34 | fpaysettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fpaydiscountamt | 现金折扣 | numeric | 23 | 10 | √ | 0 | 现金折扣 |
| 36 | fepaytype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 37 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 38 | fpaymaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fpayclaimperson | 认领人 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 41 | fpaypurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fpayactamt | 实付金额 | numeric | 23 | 10 | √ | 0 | 实付金额 |
| 43 | fpaycorebillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_claimnoticebillp_e |  | fentryid |
| 2 | idx_cas_claimnoticebillpe |  | fid |

---

## 收付认领处理中心-多语言表 t_cas_claimnoticebill_l

- **表名称：** 收付认领处理中心-多语言表
- **表名：** t_cas_claimnoticebill_l

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
| 1 | idx_cas_cnbl_fid |  | fid |
| 2 | t_cas_claimnoticebill_l_pkey |  | fpkid |

---

## 收款认领明细-子表 t_cas_claimnoticebill_e

- **表名称：** 收款认领明细-子表
- **表名：** t_cas_claimnoticebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fecorebillno | 核心单据编号 | varchar | 64 |  | √ | '' | 核心单据编号 |
| 3 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceentryid | 原分录id | int8 | 64 |  | √ | 0 | 原分录id |
| 5 | fclaimtype | 类型 | varchar | 2 |  | √ | ' ' | 类型,枚举: 0 :认领 1 :变更 2 :申诉 3 :调整 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frecpayer | 付款单位（文本） | varchar | 256 |  | √ | '' | 付款单位（文本） |
| 8 | frecbilltype | 收款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 10 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 11 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 12 | fclaimpersonid | 认领人 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 13 | fecorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 14 | fispushed | 是否已下推 | varchar | 16 |  | √ | '0' | 是否已下推 |
| 15 | fcorebilltype | 认领单据类型 | varchar | 30 |  | √ | ' ' | 认领单据类型,枚举: ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 16 | fpaymenttype | 付款单位类型 | varchar | 64 |  | √ | '' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 17 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fpaymentbasetype | 付款单位基础资料类型 | varchar | 64 |  | √ | '' | 付款单位基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 19 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fbillstatus | 是否作废 | varchar | 2 |  | √ | ' ' | 是否作废 |
| 22 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 23 | fcontactunittype | 往来单位类型 | varchar | 80 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 24 | fcorebillid | 认领单据ID | varchar | 50 |  | √ | ' ' | 认领单据ID |
| 25 | flenamount | 长短款 | numeric | 23 | 10 | √ | 0 | 长短款 |
| 26 | fecorebilltype | 核心单据类型 | varchar | 32 |  | √ | '' | 核心单据类型,枚举: ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 27 | fefee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 28 | factamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 29 | fcorebillentryseq | 认领单据行号 | int8 | 64 |  | √ | 0 | 认领单据行号 |
| 30 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 31 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fcorebillentryid | 认领单据行id | int8 | 64 |  | √ | 0 | 认领单据行id |
| 35 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 36 | fsaleman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 37 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 38 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 39 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 40 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 41 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 42 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 43 | fclaimbill | 认领单 | varchar | 80 |  | √ | ' ' | 认领单 |
| 44 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 45 | fcorebillno | 认领单据编号 | varchar | 80 |  | √ | ' ' | 认领单据编号 |
| 46 | fsettlecur | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | freceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 48 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 49 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 50 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 51 | frecpayorg | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 52 | frecbasepayer | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 53 | fhandlestatus | 是否确认 | bpchar | 1 |  | √ | '0' | 是否确认 |
| 54 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 55 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fredisctamount | 折后金额折币种 | numeric | 19 | 6 | √ | 0 | 折后金额折币种 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_claimnoticebill_fpid |  | fid |
| 2 | t_cas_claimnoticebill_e_pkey |  | fentryid |

---

## 收付认领处理中心-分表 t_cas_claimnoticebill_c

- **表名称：** 收付认领处理中心-分表
- **表名：** t_cas_claimnoticebill_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpagetype | fpagetype | varchar | 50 |  | √ | ' ' |  |
| 3 | fisaccount | 是否已入账 | varchar | 16 |  | √ | '0' | 是否已入账 |
| 4 | frulesname | 规则项名称 | varchar | 100 |  | √ | ' ' | 规则项名称 |
| 5 | fnotaccount | 未入账笔数 | int8 | 64 |  | √ | 0 | 未入账笔数 |
| 6 | fdrawbilldate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 7 | funaccountamount | 未入账金额 | numeric | 19 | 6 |  | null | 未入账金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_cnbc_fid |  | frulesname |
| 2 | t_cas_claimnoticebill_c_pkey |  | fid |

---

## 收付认领处理中心-关联追踪表 t_cas_claimnoticebill_tc

- **表名称：** 收付认领处理中心-关联追踪表
- **表名：** t_cas_claimnoticebill_tc

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
| 1 | t_cas_claimnoticebill_tc_pkey |  | fid |
| 2 | idx_cas_claimnoticebill_tc_tbill |  | ftbillid |
| 3 | idx_cas_claimnoticebill_tc_tid |  | ftid |

---

## 认领人单据-子表 t_cas_claimtype_e

- **表名称：** 认领人单据-子表
- **表名：** t_cas_claimtype_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclaimtype | 认领类别 | bpchar | 1 |  | √ | '0' | 认领类别,枚举: 1 :用户 2 :用户组 3 :业务单元 4 :角色 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fclaimtypeid | 认领人id | varchar | 80 |  | √ | ' ' | 认领人id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_claimtype_e |  | fid |
| 2 | t_cas_claimtype_e_pkey |  | fentryid |
| 3 | idx_cas_claimtype_ctypeid |  | fclaimtypeid |

---

## 关联子实体-子表 t_claimbill_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_claimbill_entry_lk

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
| 1 | t_claimbill_entry_lk_pkey |  | fpkid |
| 2 | idx_claimbill_entry_lk_fk |  | fentryid |

---

## 收付认领处理中心-反写记录表 t_cas_claimnoticebill_wb

- **表名称：** 收付认领处理中心-反写记录表
- **表名：** t_cas_claimnoticebill_wb

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
| 1 | idx_cas_claimnoticebill_wb_fk |  | fid |
| 2 | t_cas_claimnoticebill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_cas_claimnoticebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_claimnoticebill_lk

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
| 1 | t_cas_claimnoticebill_lk_pkey |  | fpkid |
| 2 | idx_cas_claimnoticebill_lk_fk |  | fid |

---

## 收付认领处理中心-主表 t_cas_claimnoticebill

- **表名称：** 收付认领处理中心-主表
- **表名：** t_cas_claimnoticebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankcheckflag | 对账标识码 | varchar | 1024 |  | √ | ' ' | 对账标识码 |
| 3 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 5 | fsourceid | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 6 | frecpayer | 付款人 | varchar | 255 |  | √ | ' ' | 付款人 |
| 7 | fmargeid | 合并生成单id | int8 | 64 |  | √ | 0 | 合并生成单id |
| 8 | frecbilltype | 收款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchargereason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 11 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 12 | fdrawername | 出票人名称 | varchar | 80 |  | √ | ' ' | 出票人名称 |
| 13 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 14 | fisaddfee | 是否补充手续费 | bpchar | 1 |  | √ | '0' | 是否补充手续费 |
| 15 | fsettlementtype | 结算方式类别 | varchar | 30 |  | √ | ' ' | 结算方式类别,枚举: 1 :支票 2 :本票 5 :商业承兑汇票 6 :银行承兑汇票 |
| 16 | foppbanknumber | 对方账号 | varchar | 200 |  | √ | ' ' | 对方账号 |
| 17 | fpaymenttype | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 18 | fbillno | 认领通知单 | varchar | 30 |  | √ | ' ' | 认领通知单 |
| 19 | fconfirmdate | 确认认领时间 | timestamp | 0 |  |  | null | 确认认领时间 |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | freamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 22 | fjoinclaim | 参与认领用户组 | varchar | 1024 |  | √ | ' ' | 参与认领用户组 |
| 23 | fpayeetype | 收款人类型 | varchar | 50 |  | √ | ' ' | 收款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | frecviewpayer | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 26 | funclaimamount | 未认领金额 | numeric | 19 | 6 | √ | 0.000000 | 未认领金额 |
| 27 | ftradetime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 28 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 ticket :收票登记 |
| 29 | frecpayee | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 30 | fclaimme | fclaimme | bpchar | 1 |  | √ | '0' |  |
| 31 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 32 | fisunclaim | 是否未认领入账 | bpchar | 1 |  | √ | '0' | 是否未认领入账 |
| 33 | faccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fsinglestream | 手续费独立流水 | bpchar | 1 |  | √ | '0' | 手续费独立流水 |
| 36 | frecpaytype | 收款用途（废弃） | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 37 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 38 | fjoinrule | 参与认领角色 | varchar | 1024 |  | √ | ' ' | 参与认领角色 |
| 39 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: recticket :票据 rec :收款 pay :付款 |
| 40 | fpayamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 41 | fbizrefno | 业务参考号 | varchar | 50 |  | √ | ' ' | 业务参考号 |
| 42 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 43 | fclaimamount | 已认领金额 | numeric | 19 | 6 | √ | 0.000000 | 已认领金额 |
| 44 | fjoinunit | 参与认领业务单元 | varchar | 1024 |  | √ | ' ' | 参与认领业务单元 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fmergestatus | 合并状态 | varchar | 30 |  | √ | ' ' | 合并状态,枚举: 0 :未合并 1 :被合并 2 :已合并 |
| 47 | fpaybilltype | 付款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 48 | fsourcetype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: bei_transdetail :交易明细 cdm_receivablebill :应收票据 |
| 49 | fclaimstatus | 认领通知单状态 | varchar | 30 |  | √ | ' ' | 认领通知单状态,枚举: 0 :待认领 1 :部分认领 2 :已认领 3 :已确认 5 :变更中 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fconfirmuserid | 确认认领人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | ftradedetailno | 交易明细编号 | varchar | 50 |  | √ | ' ' | 交易明细编号 |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | ftradeno | 明细流水号 | varchar | 50 |  | √ | ' ' | 明细流水号 |
| 55 | fappealme | fappealme | bpchar | 1 |  | √ | '0' |  |
| 56 | fpaytype | 付款用途（废弃） | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 57 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 58 | frecbasetype | 收款人基础类型 | varchar | 50 |  | √ | ' ' | 收款人基础类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 59 | fclaimusers | 参与认领用户 | varchar | 1024 |  | √ | ' ' | 参与认领用户 |
| 60 | frecbasepayee | 收款人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 61 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_claimnoticebill_pkey |  | fid |
| 2 | idx_cas_claimnoticebill_mer |  | fmargeid |
| 3 | idx_cas_claimnoticebill_bank |  | faccountbankid |
| 4 | idx_cas_claimnoticebill_bo |  | fbillno |
| 5 | idx_cas_claimnoticebill_cb |  | fclaimstatus |
| 6 | idx_cas_claimnoticebill_org |  | forgid |
