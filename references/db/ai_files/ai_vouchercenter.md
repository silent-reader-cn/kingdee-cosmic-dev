# 凭证中心-ai_vouchercenter

## 凭证中心-主表 t_gl_voucher

- **表名称：** 凭证中心-主表
- **表名：** t_gl_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispost | 是否过账 | bpchar | 1 |  | √ | '0' | 是否过账 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdebitlocamount | 借方合计 | numeric | 22 | 6 | √ | 0.000000 | 借方合计 |
| 5 | fvoucherno | 整数凭证号 | int8 | 64 |  | √ | 0 | 整数凭证号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | '0' | 来源类型,枚举: 0 :手工凭证 1 :结转损益 2 :期末调汇 4 :机制凭证 5 :凭证摊销 6 :自动转账 8 :外部导入 a :凭证转存 b :凭证手工转存 c :余额结转 |
| 10 | fsuppstatus | 附表指定状态 | bpchar | 1 |  | √ | '0' | 附表指定状态,枚举: 0 :无需指定 1 :需指未指 2 :部分指定 3 :已指定 a :待调整 b :部分调整 c :已调整 |
| 11 | fisreverse | 是否冲销凭证 | bpchar | 1 |  | √ | '0' | 是否冲销凭证 |
| 12 | fcancellerid | 作废 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcashierid | 复核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fvdescription | 序时簿摘要 | varchar | 1020 |  | √ | ' ' | 序时簿摘要 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fposttime | 过账时间 | timestamp | 0 |  |  | null | 过账时间 |
| 17 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | fsourcebilltype | 来源表单类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 19 | fbillstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: A :暂存 B :已提交 C :已审核 D :已作废 |
| 20 | ferrormsg | 驳回信息 | varchar | 255 |  | √ | ' ' | 驳回信息 |
| 21 | fsubmitterid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fposterid | 过账人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsourcesys | 来源系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 27 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 28 | ftypeid | 凭证字 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 29 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 30 | fattachments | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 31 | fdiffitemstatus | 差异指定状态 | bpchar | 1 |  | √ | '0' | 差异指定状态,枚举: 0 :无需指定 1 :需指未指 2 :已指定 3 :部分指定 |
| 32 | fcreditlocamount | 贷方合计 | numeric | 22 | 6 | √ | 0.000000 | 贷方合计 |
| 33 | ferrorstatus | 审核驳回 | bpchar | 1 |  | √ | '0' | 审核驳回,枚举: 1 :是 0 :否 |
| 34 | floccurrency | 组织本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fhasreverse | 是否已被冲销 | bpchar | 1 |  | √ | '0' | 是否已被冲销 |
| 37 | fisaibuild | AI记账 | bpchar | 1 |  | √ | '0' | AI记账 |
| 38 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 39 | fmainstatus | 主表指定状态 | bpchar | 1 |  | √ | '0' | 主表指定状态,枚举: 0 :无需指定 1 :需指未指 3 :已指定 2 :部分指定 |
| 40 | fnumber | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fischeck | 复核状态 | bpchar | 1 |  | √ | 'a' | 复核状态,枚举: a :无需复核 b :待复核 c :已复核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_vchsourcetype |  | fsourcetype,fbookid,fperiodid |
| 2 | idx_gl_vch_defsort |  | fbookid,fperiodid,ftypeid,fvoucherno,fnumber,fid |
| 3 | t_gl_voucher_pkey |  | fid |
| 4 | idx_gl_vch_iop |  | fbookid,fispost |
| 5 | idx_gl_vch_1 |  | forgid,fbooktypeid,fperiodid,fbookeddate,fnumber,fid |
| 6 | idx_gl_vchnum |  | fnumber,fbookid,fperiodid |

---

## 分录体-多语言表 t_gl_voucherentry_l

- **表名称：** 分录体-多语言表
- **表名：** t_gl_voucherentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmuldescription | 多语言摘要 | varchar | 1020 |  | √ | ' ' | 多语言摘要 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_voucherentry_l_feid |  | fentryid,flocaleid |
| 2 | pk_gl_voucherentry_l |  | fpkid |

---

## 分录体-子表 t_gl_voucherentry

- **表名称：** 分录体-子表
- **表名：** t_gl_voucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriginalcredit | 原币贷方 | numeric | 21 | 6 | √ | 0.000000 | 原币贷方 |
| 3 | forgid | eorg | int8 | 64 |  | √ | 0 | eorg |
| 4 | fisdap | 是否dap生成 | bpchar | 1 |  | √ | '0' | 是否dap生成 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdiffitemid | 差异项目 | int8 | 64 |  | √ | 0 | [差异项目 gl_diffitem](../gl_files/gl_diffitem.md) |
| 7 | fmaincfassgrpid | 主表核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 8 | fmaincfamount | 主表项目金额 | numeric | 21 | 6 | √ | 0.000000 | 主表项目金额 |
| 9 | foriginalamount | 原币金额 | numeric | 23 | 10 | √ | 0 | 原币金额 |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fentrydc | 分录方向 | varchar | 2 |  | √ | '1' | 分录方向,枚举: 1 :借 -1 :贷 |
| 12 | fdiffitemamt | 差异金额 | numeric | 23 | 10 | √ | 0 | 差异金额 |
| 13 | flocaldebit | 借方 | numeric | 21 | 6 | √ | 0.000000 | 借方 |
| 14 | flocalcredit | 贷方 | numeric | 21 | 6 | √ | 0.000000 | 贷方 |
| 15 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 16 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 17 | fsuppcfamount | 附表项目金额 | numeric | 21 | 6 | √ | 0.000000 | 附表项目金额 |
| 18 | fperiodid | eperiod | int8 | 64 |  | √ | 0 | eperiod |
| 19 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 20 | fmaincfitemid | 主表项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 21 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 22 | fbiznumrecordid | 业务编号核销记录 | int8 | 64 |  | √ | 0 | 业务编号核销记录 |
| 23 | fdescription | 摘要 | varchar | 1020 |  | √ | ' ' | 摘要 |
| 24 | fbookid | ebook | int8 | 64 |  | √ | 0 | ebook |
| 25 | fbusinessnum | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 26 | flocalexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 27 | fsuppcfitemid | 附表项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 28 | fsettletnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 29 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | foriginaldebit | 原币借方 | numeric | 21 | 6 | √ | 0.000000 | 原币借方 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_vch_maincf |  | fmaincfitemid |
| 2 | idx_gl_vchenorg |  | forgid,fperiodid,faccountid,fassgrpid |
| 3 | idx_gl_vch_suppcf |  | fsuppcfitemid |
| 4 | idx_gl_voucherentry |  | fid,fseq |
| 5 | t_gl_voucherentry_pkey |  | fentryid |
| 6 | idx_gl_vchenacct |  | faccountid |
| 7 | idx_gl_vchenassgrp |  | fassgrpid |
