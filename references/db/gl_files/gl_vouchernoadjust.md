# 凭证号整理-gl_vouchernoadjust

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
| 6 | fmaincfassgrpid | 主表核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 7 | fmaincfamount | 主表项目金额 | numeric | 21 | 6 | √ | 0.000000 | 主表项目金额 |
| 8 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 9 | fentrydc | 分录方向 | varchar | 2 |  | √ | '1' | 分录方向,枚举: 1 :借 -1 :贷 |
| 10 | flocaldebit | 借方 | numeric | 21 | 6 | √ | 0.000000 | 借方 |
| 11 | flocalcredit | 贷方 | numeric | 21 | 6 | √ | 0.000000 | 贷方 |
| 12 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 13 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 14 | fsuppcfamount | 附表项目金额 | numeric | 21 | 6 | √ | 0.000000 | 附表项目金额 |
| 15 | fperiodid | eperiod | int8 | 64 |  | √ | 0 | eperiod |
| 16 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 17 | fmaincfitemid | 主表项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 18 | fbiznumrecordid | 业务编号核销记录 | int8 | 64 |  | √ | 0 | 业务编号核销记录 |
| 19 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 20 | fbusinessnum | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 21 | flocalexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 22 | fsuppcfitemid | 附表项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 23 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | foriginaldebit | 原币借方 | numeric | 21 | 6 | √ | 0.000000 | 原币借方 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

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

---

## 凭证号整理-主表 t_gl_voucher

- **表名称：** 凭证号整理-主表
- **表名：** t_gl_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispost | 是否过账 | bpchar | 1 |  | √ | '0' | 是否过账 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdebitlocamount | 借方合计 | numeric | 22 | 6 | √ | 0.000000 | 借方合计 |
| 5 | fvoucherno | 整数凭证号 | int8 | 64 |  | √ | 0 | 整数凭证号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | '0' | 来源类型,枚举: 0 :手工凭证 1 :结转损益 2 :期末调汇 4 :机制凭证 5 :凭证摊销 6 :自动转账 8 :外部导入 a :凭证转存 b :凭证手工转存 c :余额结转 |
| 10 | fsuppstatus | 附表指定状态 | bpchar | 1 |  | √ | '0' | 附表指定状态,枚举: 0 :无需指定 1 :需指未指 2 :部分指定 3 :已指定 a :待调整 b :部分调整 c :已调整 |
| 11 | fisreverse | 是否冲销凭证 | bpchar | 1 |  | √ | '0' | 是否冲销凭证 |
| 12 | fcancellerid | 作废 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcashierid | 复核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fvdescription | 序时簿摘要 | varchar | 255 |  | √ | ' ' | 序时簿摘要 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fposttime | 过账时间 | timestamp | 0 |  |  | null | 过账时间 |
| 17 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fsourcebilltype | 来源表单类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 19 | fbillstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: A :暂存 B :已提交 C :已审核 D :已作废 |
| 20 | ferrormsg | 驳回信息 | varchar | 255 |  | √ | ' ' | 驳回信息 |
| 21 | fsubmitterid | 制单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fposterid | 过账人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsourcesys | 来源系统 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 27 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 28 | ftypeid | 凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 29 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 30 | fattachments | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 31 | fcreditlocamount | 贷方合计 | numeric | 22 | 6 | √ | 0.000000 | 贷方合计 |
| 32 | ferrorstatus | 审核驳回 | bpchar | 1 |  | √ | '0' | 审核驳回,枚举: 1 :是 0 :否 |
| 33 | floccurrency | 组织本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 35 | fhasreverse | 是否已被冲销 | bpchar | 1 |  | √ | '0' | 是否已被冲销 |
| 36 | fisaibuild | AI记账 | bpchar | 1 |  | √ | '0' | AI记账 |
| 37 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 38 | fmainstatus | 主表指定状态 | bpchar | 1 |  | √ | '0' | 主表指定状态,枚举: 0 :无需指定 1 :需指未指 3 :已指定 2 :部分指定 |
| 39 | fnumber | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fischeck | 复核状态 | bpchar | 1 |  | √ | 'a' | 复核状态,枚举: a :无需复核 b :待复核 c :已复核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_vchsourcetype |  | fsourcetype,fbookid,fperiodid |
| 2 | t_gl_voucher_pkey |  | fid |
| 3 | idx_gl_vch_iop |  | fbookid,fispost |
| 4 | idx_gl_vch_1 |  | forgid,fbooktypeid,fperiodid,fbookeddate,fnumber,fid |
| 5 | idx_gl_vchnum |  | fnumber,fbookid,fperiodid |
