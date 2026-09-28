# 坏账计提-ar_baddebtaccrue_pro

## 坏账计提-主表 t_ar_baddebtaccrue

- **表名称：** 坏账计提-主表
- **表名：** t_ar_baddebtaccrue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faginggroup | 计提比率账龄分组 | int8 | 64 |  | √ | 0 | 应收账龄分组设置 ar_accrualaging |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fasstacttype | 往来类型 | varchar | 255 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 5 | flistperiod | 计提期间 | varchar | 255 |  | √ | ' ' | 计提期间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fotherbaddebtaccrue | 其他应收参与计提 | bpchar | 1 |  | √ | '0' | 其他应收参与计提 |
| 8 | faginggroupdetail | 计提比率账龄分组明细 | varchar | 255 |  | √ | ' ' | 计提比率账龄分组明细 |
| 9 | farbustobaddebtaccrue | 暂估应收单参与计提 | bpchar | 1 |  | √ | '0' | 暂估应收单参与计提 |
| 10 | farbusagingstartdate | 暂估应收单账龄起算日 | varchar | 30 |  |  | ' ' | 暂估应收单账龄起算日,枚举: bizdate :业务日期 bookdate :记账日期 duedate :最后到期日 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | faccrualstatus | 计提状态 | varchar | 30 |  | √ | ' ' | 计提状态,枚举: 0 :未计提 1 :已计提 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | faragingstartdate | 财务应收单账龄起算日 | varchar | 30 |  |  | ' ' | 财务应收单账龄起算日,枚举: bizdate :业务日期 bookdate :记账日期 duedate :最后到期日 planduedate :收款计划.到期日 invoicedate :发票日期 |
| 15 | faccrualfrequency | 计提频率 | varchar | 30 |  | √ | ' ' | 计提频率,枚举: month :月 quarter :季 semiannual :半年 year :年 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fperiodid | 计提期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | frecedbaddebtaccrue | 预收单参与计提 | bpchar | 1 |  | √ | '0' | 预收单参与计提 |
| 21 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 22 | faccrualschemeid | faccrualschemeid | int8 | 64 |  | √ | 0 |  |
| 23 | faginggroupdetail_tag | 计提比率账龄分组明细_详情 | text | 0 |  |  | null | 计提比率账龄分组明细_详情 |
| 24 | fpreperiodid | 上一期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fisperiod | 是否首次计提 | bpchar | 1 |  | √ | '0' | 是否首次计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_baddebtaccrue |  | fid |
| 2 | idx_ar_baddebt_scheme |  | faccrualschemeid |
| 3 | idx_ar_baddebt_period_org |  | fperiodid,forgid |
| 4 | idx_ar_baddebt_org |  | forgid |

---

## 个别认定单据体-子表 t_ar_baddebtaccrueentry

- **表名称：** 个别认定单据体-子表
- **表名：** t_ar_baddebtaccrueentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccrualentityobj | faccrualentityobj | varchar | 50 |  | √ | ' ' |  |
| 3 | fasstacttypeid | fasstacttypeid | int8 | 64 |  | √ | 0 |  |
| 4 | faccrualobjid | faccrualobjid | int8 | 64 |  | √ | 0 |  |
| 5 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | findividualreason | 个别认定原因 | varchar | 255 |  | √ | ' ' | 个别认定原因 |
| 8 | faccrualagingid | 计提比率账龄分组 | int8 | 64 |  | √ | 0 | 应收账龄分组设置 ar_accrualaging |
| 9 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | faccrualpercent | faccrualpercent | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_baddebtaccrueentry |  | fentryid |
| 2 | idx_ar_bdaentry_fid |  | fid |

---

## 分组认定分录-子表 t_ar_baddebtaccruegpentry

- **表名称：** 分组认定分录-子表
- **表名：** t_ar_baddebtaccruegpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcondition_tag | 分组条件(隐藏)_详情 | text | 0 |  |  | null | 分组条件(隐藏)_详情 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcondition | 分组条件(隐藏) | varchar | 255 |  | √ | ' ' | 分组条件(隐藏) |
| 5 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 6 | faccrualagingid | 计提比率账龄分组 | int8 | 64 |  | √ | 0 | 应收账龄分组设置 ar_accrualaging |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_bdagpentry_fid |  | fid |
| 2 | pk_t_ar_baddebtaccruegpentry |  | fentryid |
