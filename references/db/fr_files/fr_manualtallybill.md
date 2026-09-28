# 通用转账申请单-fr_manualtallybill

## 通用转账申请单-主表 t_fr_manutalbill

- **表名称：** 通用转账申请单-主表
- **表名：** t_fr_manutalbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证类型 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 3 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fabstract | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 5 | fhrelatebillno | 关联单据编码 | varchar | 60 |  | √ | ' ' | 关联单据编码 |
| 6 | fexratebackcal | 反算汇率 | bpchar | 1 |  | √ | '0' | 反算汇率 |
| 7 | famount | 记账金额合计(本位币) | numeric | 23 | 10 | √ | 0 | 记账金额合计(本位币) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbiztype | 报账业务类型 | int8 | 64 |  | √ | 0 | [报账业务类型 bd_businessitem](../fibd_files/bd_businessitem.md) |
| 10 | fbizdetailtype | 业务项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fappendixnum | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 14 | foribackcal | 反算原币金额 | bpchar | 1 |  | √ | '0' | 反算原币金额 |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | faccountbook | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fismulticurrency | 多币别 | bpchar | 1 |  | √ | ' ' | 多币别 |
| 19 | fwriteoff | 冲销标识 | varchar | 9 |  | √ | ' ' | 冲销标识,枚举: 1 :未冲销单 2 :冲销单 3 :已冲销单 |
| 20 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核通过 E :审核不通过 F :废弃 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdescription | 事由 | varchar | 600 |  | √ | ' ' | 事由 |
| 25 | fhrelatebill | 关联单据类型 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 26 | fisgenvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 27 | fapplierposition | 职位 | varchar | 64 |  | √ | ' ' | 职位 |
| 28 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 29 | fverifytag | 引入校验标识 | bpchar | 1 |  | √ | ' ' | 引入校验标识,枚举: Y :已校验 N :未校验 |
| 30 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 31 | fperiod | 记账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 32 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 33 | fimporttag | 引入标识 | bpchar | 1 |  | √ | '0' | 引入标识 |
| 34 | fpricebackcal | 反算单价 | bpchar | 1 |  | √ | '0' | 反算单价 |
| 35 | ftallycompany | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | fnextauditor | 当前处理人 | varchar | 64 |  | √ | ' ' | 当前处理人 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fr_manutalbill |  | fid |
| 2 | idx_fr_manual_billno |  | fbillno |

---

## 科目核算维度-子表 t_fr_amortassgrpentry

- **表名称：** 科目核算维度-子表
- **表名：** t_fr_amortassgrpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalue | 值 | int8 | 64 |  | √ | 0 | [科目影响因素（旧） ai_vchentrytype](../ai_files/ai_vchentrytype.md) |
| 2 | fvaluesstr | 核算项目值集合 | varchar | 1024 |  | √ | ' ' | 核算项目值集合 |
| 3 | ftxtval | 手工维度值 | varchar | 2000 |  | √ | ' ' | 手工维度值 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ffieldnameid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fnumber | 值.编码 | bpchar | 50 |  | √ | ' ' | 值.编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fisrequire | 必录 | bpchar | 1 |  | √ | '0' | 必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_amoasstentry_id |  | fentryid |
| 2 | pk_t_fr_amortassgrpentry |  | fdetailid |

---

## 记账明细-子表 t_fr_manutalentry

- **表名称：** 记账明细-子表
- **表名：** t_fr_manutalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelatebillno | 关联单据编码 | varchar | 50 |  | √ | ' ' | 关联单据编码 |
| 3 | fratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 4 | foriamount | 原币金额 | numeric | 23 | 10 | √ | 0 | 原币金额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmaincfamount | 主表项目金额 | numeric | 23 | 10 | √ | 0 | 主表项目金额 |
| 7 | faccount | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 8 | fmaincfitem | 主表项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | ftallyabstract | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 11 | fquantities | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 12 | fexchangerate | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 16 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 17 | fbaseprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 18 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 19 | fassgrpdesc | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 20 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 21 | fmaincfassgrp | 主表核算维度 | varchar | 2000 |  | √ | ' ' | 主表核算维度 |
| 22 | fstaff | 职工 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | floanstanamount | 贷方金额 | numeric | 23 | 10 | √ | 0 | 贷方金额 |
| 24 | frelatedbill | 关联单据类型 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 25 | fassetclass | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 26 | floanamount | 原币贷方 | numeric | 23 | 10 | √ | 0 | 原币贷方 |
| 27 | fstandardamount | 借方金额 | numeric | 23 | 10 | √ | 0 | 借方金额 |
| 28 | ftallyamount | 原币借方 | numeric | 23 | 10 | √ | 0 | 原币借方 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fcuscurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_manutalentry_id |  | fid |
| 2 | pk_t_fr_manutalentry |  | fentryid |

---

## 通用转账申请单-多语言表 t_fr_manutalbill_l

- **表名称：** 通用转账申请单-多语言表
- **表名：** t_fr_manutalbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 64 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fr_manutalbill_l_id |  | fid,flocaleid |
| 2 | pk_t_fr_manutalbill_l |  | fpkid |

---

## 通用转账申请单-反写记录表 t_fr_manutalbill_wb

- **表名称：** 通用转账申请单-反写记录表
- **表名：** t_fr_manutalbill_wb

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
| 1 | t_fr_manutalbill_wb_pkey |  | fentryid |
| 2 | idx_fr_manutalbill_wb_fk |  | fid |

---

## 主表项目核算维度-子表 t_fr_amortmainassgrpentry

- **表名称：** 主表项目核算维度-子表
- **表名：** t_fr_amortmainassgrpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmainfieldnameid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 2 | fmainisrequire | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fmainvalue | 值 | int8 | 64 |  | √ | 0 | [科目影响因素（旧） ai_vchentrytype](../ai_files/ai_vchentrytype.md) |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fmainnumber | 值.编码 | varchar | 50 |  | √ | ' ' | 值.编码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fmaintxtval | 手工维度值 | varchar | 2000 |  | √ | ' ' | 手工维度值 |
| 9 | fmainvaluesstr | 核算项目值集合 | varchar | 1024 |  | √ | ' ' | 核算项目值集合 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fr_amortmainassgrpentry |  | fdetailid |
| 2 | idx_fr_amomainasstentry_id |  | fentryid |

---

## 通用转账申请单-关联追踪表 t_fr_manutalbill_tc

- **表名称：** 通用转账申请单-关联追踪表
- **表名：** t_fr_manutalbill_tc

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
| 1 | t_fr_manutalbill_tc_pkey |  | fid |
| 2 | idx_fr_manutalbill_tc_tbill |  | ftbillid |
| 3 | idx_fr_manutalbill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_fr_manutalentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fr_manutalentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fr_manutalentry_lk_pkey |  | fpkid |
| 2 | idx_fr_manutalentry_lk_fk |  | fdetailid |
