# 客户对账函-ar_accountstate

## 对账函明细-子表 t_ar_accountstate_detail

- **表名称：** 对账函明细-子表
- **表名：** t_ar_accountstate_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferecorg | 收款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | feperiodincreasedrec | 本期增加收款 | numeric | 23 | 10 | √ | 0 | 本期增加收款 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | feduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 6 | feabstract | 摘要 | varchar | 50 |  | √ | ' ' | 摘要,枚举: periodbalance :期初余额 period_ar_finarbill :期初应收 period_ar_busbill :期初暂估应收 period_cas_recbill :期初收款 period_cas_paybill :期初退款 ar_finarbill :应收 ar_busbill :暂估应收 cas_recbill :收款 cas_paybill :退款 sum :合计 total :总计 subtotal :小计 |
| 7 | febookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 8 | feoverduedays | 逾期天数 | int4 | 32 |  | √ | 0 | 逾期天数 |
| 9 | febizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | feacctbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 11 | feperiodincreasedar | 本期增加应收 | numeric | 23 | 10 | √ | 0 | 本期增加应收 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fecurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | febalance | 期末余额 | numeric | 23 | 10 | √ | 0 | 期末余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_accountstate_detail |  | fentryid |
| 2 | idx_ar_accountstate_detail_fk |  | fid |

---

## 邮件发送记录-子表 t_ar_accountstate_mail

- **表名称：** 邮件发送记录-子表
- **表名：** t_ar_accountstate_mail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsendtime | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 3 | fmattachuid | 附件id | varchar | 200 |  | √ | ' ' | 附件id |
| 4 | fmoperateuser | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmaddress | 收件邮箱 | varchar | 200 |  |  | ' ' | 收件邮箱 |
| 6 | fmsentstatus | 邮件发送状态 | varchar | 50 |  | √ | ' ' | 邮件发送状态,枚举: A :发送成功 B :发送失败 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmerrorinfo | 失败说明 | varchar | 2000 |  |  | ' ' | 失败说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_accountstate_mail |  | fentryid |
| 2 | idx_ar_accountstate_mail_fk |  | fid |

---

## 客户对账函-主表 t_ar_accountstate

- **表名称：** 客户对账函-主表
- **表名：** t_ar_accountstate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | facctagegroupinfo | 账龄分组信息 | varchar | 255 |  | √ | ' ' | 账龄分组信息 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcontactmail | 收件邮箱 | varchar | 2000 |  |  | ' ' | 收件邮箱 |
| 14 | fmailstatus | 邮件发送状态 | varchar | 50 |  | √ | ' ' | 邮件发送状态,枚举: A :未发送 B :已发送 |
| 15 | facctagegroupinfo_tag | 账龄分组信息_详情 | text | 0 |  |  | null | 账龄分组信息_详情 |
| 16 | fcontact | 联系人 | varchar | 2000 |  |  | ' ' | 联系人 |
| 17 | fstartdate | 对账开始日期 | timestamp | 0 |  |  | null | 对账开始日期 |
| 18 | fstopdate | 对账截止日期 | timestamp | 0 |  |  | null | 对账截止日期 |
| 19 | fstandarddate | 账龄基准日期 | varchar | 50 |  | √ | ' ' | 账龄基准日期,枚举: bizdate :业务日期 bookdate :记账日期 planduedate :到期日 |
| 20 | faccountdate | 对账基准日期 | varchar | 50 |  | √ | ' ' | 对账基准日期,枚举: bizdate :业务日期 bookdate :记账日期 planduedate :到期日 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_accountstate_createdate |  | fcreatedate |
| 2 | idx_ar_account_bizdate_billno |  | fcreatedate,fbillno |
| 3 | idx_accountstate_billno |  | fbillno |
| 4 | pk_t_ar_accountstate |  | fid |

---

## 账龄详情-子表 t_ar_accountstate_age

- **表名称：** 账龄详情-子表
- **表名：** t_ar_accountstate_age

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgcurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fgtotalamt | 汇总金额 | numeric | 23 | 10 | √ | 0 | 汇总金额 |
| 4 | fgacctagegroup15 | 账龄分组15 | numeric | 23 | 10 | √ | 0 | 账龄分组15 |
| 5 | fgacctagegroup14 | 账龄分组14 | numeric | 23 | 10 | √ | 0 | 账龄分组14 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fgacctagegroup13 | 账龄分组13 | numeric | 23 | 10 | √ | 0 | 账龄分组13 |
| 8 | fgacctagegroup12 | 账龄分组12 | numeric | 23 | 10 | √ | 0 | 账龄分组12 |
| 9 | fgacctagegroup11 | 账龄分组11 | numeric | 23 | 10 | √ | 0 | 账龄分组11 |
| 10 | fgacctagegroup3 | 账龄分组3 | numeric | 23 | 10 | √ | 0 | 账龄分组3 |
| 11 | fgacctagegroup10 | 账龄分组10 | numeric | 23 | 10 | √ | 0 | 账龄分组10 |
| 12 | fgacctagegroup2 | 账龄分组2 | numeric | 23 | 10 | √ | 0 | 账龄分组2 |
| 13 | fgacctagegroup1 | 账龄分组1 | numeric | 23 | 10 | √ | 0 | 账龄分组1 |
| 14 | fgacctagegroup0 | 未到期 | numeric | 23 | 10 | √ | 0 | 未到期 |
| 15 | fgacctagegroup7 | 账龄分组7 | numeric | 23 | 10 | √ | 0 | 账龄分组7 |
| 16 | fgacctagegroup6 | 账龄分组6 | numeric | 23 | 10 | √ | 0 | 账龄分组6 |
| 17 | fgacctagegroup5 | 账龄分组5 | numeric | 23 | 10 | √ | 0 | 账龄分组5 |
| 18 | fgacctagegroup4 | 账龄分组4 | numeric | 23 | 10 | √ | 0 | 账龄分组4 |
| 19 | fgacctagegroup9 | 账龄分组9 | numeric | 23 | 10 | √ | 0 | 账龄分组9 |
| 20 | fgacctagegroup8 | 账龄分组8 | numeric | 23 | 10 | √ | 0 | 账龄分组8 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_accountstate_age_fk |  | fid |
| 2 | pk_t_ar_accountstate_age |  | fentryid |
