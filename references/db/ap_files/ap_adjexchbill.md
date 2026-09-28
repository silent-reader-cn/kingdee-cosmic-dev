# 应付调汇单-ap_adjexchbill

## 应付调汇单-主表 t_ap_adjexchbill

- **表名称：** 应付调汇单-主表
- **表名：** t_ap_adjexchbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 应付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisincludeentry | 是否含分录 | bpchar | 1 |  | √ | '0' | 是否含分录 |
| 4 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 5 | fcurlocalbalance | 当前余额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 当前余额(本位币) |
| 6 | fgainloss | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 7 | flastgainloss | 上期汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 上期汇兑损益 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fquotation | 当前换算方式 | varchar | 30 |  | √ | '0' | 当前换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | flocalbalance | 源单余额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 源单余额(本位币) |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | flastexchangerate | 源单汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 源单汇率 |
| 16 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_busbill :暂估应付单 ar_busbill :暂估应收单 ap_finapbill :财务应付单 ar_finarbill :财务应收单 cas_recbill :收款单 cas_paybill :付款单 ap_paidbill :期初预付单 ar_receivedbill :期初预收单 |
| 19 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsourcebilldate | 源单日期 | timestamp | 0 |  |  | null | 源单日期 |
| 26 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fbalance | 期间余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期间余额 |
| 29 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 30 | fbizsystem | 业务系统 | varchar | 30 |  | √ | ' ' | 业务系统,枚举: AR :应收 AP :应付 CAS :出纳 |
| 31 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 32 | fcurgainloss | 总汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 总汇兑损益 |
| 33 | fsrcbillquotation | 源单换算方式 | varchar | 30 |  | √ | '0' | 源单换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 34 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_adjexch_bizdate |  | fbizdate |
| 2 | idx_ap_adjexch_billno |  | fbillno |
| 3 | idx_ap_adjexch_srcebillid |  | fsourcebillid |
| 4 | idx_ap_adjexch_orgid |  | forgid,fperiodid,fbizsystem |
| 5 | pk_ap_adjexchbill |  | fid |

---

## 明细-子表 t_ap_adjexchbillentry

- **表名称：** 明细-子表
- **表名：** t_ap_adjexchbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcurlocalbalance | 当前余额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 当前余额(本位币) |
| 9 | fgainloss | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 10 | flastgainloss | 上期汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 上期汇兑损益 |
| 11 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 12 | fbalance | 期间余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期间余额 |
| 13 | fcurgainloss | 总汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 总汇兑损益 |
| 14 | flocalbalance | 源单余额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 源单余额(本位币) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_adjexch_pid |  | fid |
| 2 | pk_ap_adjexchbillentry |  | fentryid |
| 3 | idx_ap_adjexch_srcentryid |  | fsrcentryid |
