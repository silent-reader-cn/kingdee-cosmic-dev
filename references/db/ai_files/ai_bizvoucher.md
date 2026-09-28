# 业务凭证-ai_bizvoucher

## 单据体-子表 t_ai_bizvoucherentry

- **表名称：** 单据体-子表
- **表名：** t_ai_bizvoucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fautomatic | fautomatic | bpchar | 1 |  | √ | '0' |  |
| 3 | fcanchargeagainst | fcanchargeagainst | bpchar | 1 |  | √ | '0' |  |
| 4 | freportcredit | freportcredit | numeric | 19 | 6 | √ | 0.000000 |  |
| 5 | freportdebit | freportdebit | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdiffitemid | 差异项目 | int8 | 64 |  | √ | 0 | [差异项目 gl_diffitem](../gl_files/gl_diffitem.md) |
| 8 | foricurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fmaincfamount | 主表项目金额 | numeric | 19 | 6 | √ | 0.000000 | 主表项目金额 |
| 10 | fmaincfassgrpid | 主表核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 11 | fsupfamount | 补充资料金额 | numeric | 19 | 6 | √ | 0 | 补充资料金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fentrydc | 分录方向 | varchar | 2 |  | √ | '1' | 分录方向,枚举: 1 :借 -1 :贷 |
| 14 | flocaldebit | 借方 | numeric | 19 | 6 | √ | 0.000000 | 借方 |
| 15 | flocalcredit | 贷方 | numeric | 19 | 6 | √ | 0.000000 | 贷方 |
| 16 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 17 | fvchtempentry | 凭证模板分录 | varchar | 100 |  | √ | ' ' | 凭证模板分录 |
| 18 | fdiffamt | 差异金额 | numeric | 23 | 10 | √ | 0 | 差异金额 |
| 19 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fsourcebillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 21 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 22 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 23 | fmaincfitemid | 主表项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 24 | foridebit | 原币借方 | numeric | 19 | 6 | √ | 0.000000 | 原币借方 |
| 25 | freportexchangerate | freportexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | fdescription | 摘要 | varchar | 1020 |  |  | ' ' | 摘要 |
| 27 | fbookid | fbookid | int8 | 64 |  | √ | 0 |  |
| 28 | fsupcfitemid | 补充资料 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 29 | fbusinessnum | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 30 | flocalexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 31 | foricredit | 原币贷方 | numeric | 19 | 6 | √ | 0.000000 | 原币贷方 |
| 32 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_bizvchentry_fid |  | fid |
| 2 | idx_ai_bizvcentry_maincf |  | fmaincfitemid |
| 3 | t_ai_bizvoucherentry_pkey |  | fentryid |

---

## 子单据体-子表 t_ai_bizvouchersubentry

- **表名称：** 子单据体-子表
- **表名：** t_ai_bizvouchersubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalue | 业务维度值 | varchar | 100 |  | √ | ' ' | 业务维度值 |
| 2 | fflexfield | 业务维度 | varchar | 50 |  | √ | ' ' | 业务维度 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_bizvouchersubentry_fk |  | fentryid |
| 2 | pk_ai_bizvouchersubentry |  | fdetailid |

---

## 业务凭证-主表 t_ai_bizvoucher

- **表名称：** 业务凭证-主表
- **表名：** t_ai_bizvoucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftplgroupid | ftplgroupid | varchar | 36 |  | √ | ' ' |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdebitlocamount | 借方合计 | numeric | 22 | 6 | √ | 0 | 借方合计 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbuildglvoucher | 是否生成了凭证 | bpchar | 1 |  | √ | '0' | 是否生成了凭证 |
| 7 | fiserror | fiserror | bpchar | 1 |  | √ | '0' |  |
| 8 | flocalcurrencyid | 组织本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fisupdate | fisupdate | bpchar | 1 |  | √ | '0' |  |
| 12 | fsourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: 4 :机制凭证 8 :外部导入 0 :手工凭证 |
| 13 | fsuppstatus | 附表指定状态 | bpchar | 10 |  | √ | '0' | 附表指定状态,枚举: 0 :无需指定 1 :需指未指 2 :部分指定 3 :已指定 a :待调整 b :部分调整 c :已调整 |
| 14 | faimodelid | AI记账模型 | int8 | 64 |  | √ | 0 | [AI记账模型 ai_accountingmodel](../ai_files/ai_accountingmodel.md) |
| 15 | fglvoucherid | 凭证内码 | int8 | 64 |  | √ | 0 | 凭证内码 |
| 16 | fbizinfoschemeid | 会计事项 | int8 | 64 |  | √ | 0 | [会计事项 ai_bizinfoscheme](../ai_files/ai_bizinfoscheme.md) |
| 17 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 18 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 19 | freportcurrencyid | freportcurrencyid | int8 | 64 |  | √ | 0 |  |
| 20 | fvdescription | 摘要 | varchar | 1020 |  | √ | ' ' | 摘要 |
| 21 | fglbillno | 列表凭证号 | varchar | 80 |  | √ | ' ' | 列表凭证号 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 24 | ftemplateid | 凭证模板内码 | varchar | 36 |  | √ | ' ' | 凭证模板内码 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fsourcesys | 来源系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | 参考消息 | varchar | 255 |  | √ | ' ' | 参考消息 |
| 30 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 31 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 32 | fstrsourcebillid | 源单内码（字符型） | varchar | 18 |  | √ | ' ' | 源单内码（字符型） |
| 33 | ftypeid | 凭证字号 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 34 | fattachments | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 35 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 36 | fcreditlocamount | 贷方合计 | numeric | 22 | 6 | √ | 0 | 贷方合计 |
| 37 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 38 | fisai | AI记账 | bpchar | 1 |  | √ | '0' | AI记账 |
| 39 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 40 | fmainstatus | 主表指定状态 | bpchar | 10 |  | √ | '0' | 主表指定状态,枚举: 0 :无需指定 1 :需指未指 3 :已指定 2 :部分指定 |
| 41 | fnumber | 业务凭证编号 | varchar | 80 |  | √ | ' ' | 业务凭证编号 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_bizvoucher_pkey |  | fid |
| 2 | idx_ai_bizvoucher_book_src |  | fsourcebillid,fbookid,fsourcebill |
| 3 | idx_ai_bizvoucher |  | fbookid,forgid,fperiodid |
| 4 | idx_ai_bizvoucher_gv |  | fglvoucherid |
| 5 | idx_ai_bizvoucher_org |  | forgid,fbooktypeid,fperiodid |
