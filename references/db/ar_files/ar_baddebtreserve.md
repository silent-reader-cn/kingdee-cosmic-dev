# 坏账准备（废弃）-ar_baddebtreserve

## 坏账准备（废弃）-主表 t_ar_baddebtreserve

- **表名称：** 坏账准备（废弃）-主表
- **表名：** t_ar_baddebtreserve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccruedamt | 应计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应计金额 |
| 3 | fwriteoffamt | 冲回 | numeric | 23 | 10 | √ | 0.0000000000 | 冲回 |
| 4 | faccrualdate | 计提日期 | timestamp | 0 |  |  | null | 计提日期 |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | faccrualrate | 计提比率(%) | numeric | 19 | 6 | √ | 0.000000 | 计提比率(%) |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | frange | 区间 | varchar | 30 |  | √ | ' ' | 区间 |
| 12 | fadditionalamt | 补提 | numeric | 23 | 10 | √ | 0.0000000000 | 补提 |
| 13 | faccrualschtype | faccrualschtype | varchar | 30 |  | √ | ' ' |  |
| 14 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 17 | faccrualfrequency | 计提频率 | varchar | 30 |  | √ | ' ' | 计提频率,枚举: month :月 season :季 year :年 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | farpolicyid | 应收政策 | int8 | 64 |  | √ | 0 | 应收政策 ar_policy |
| 20 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fsourcebilltype | 源单标识 | varchar | 30 |  | √ | ' ' | 源单标识 |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | funsettleamt | 未结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未结算金额 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | freceivableamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 29 | fpreaccrualamt | 前期计提 | numeric | 23 | 10 | √ | 0.0000000000 | 前期计提 |
| 30 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 31 | faccrualschtypeid | faccrualschtypeid | int8 | 64 |  | √ | 0 |  |
| 32 | fbaseamount | 基准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 基准金额 |
| 33 | fbalanceamt | 坏账准备余额 | numeric | 23 | 10 | √ | 0.0000000000 | 坏账准备余额 |
| 34 | fpolicytypeid | 政策类型 | int8 | 64 |  | √ | 0 | 政策类型 ar_policytype |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 37 | fsourcetypeid | 来源类型 | int8 | 64 |  | √ | 0 | 来源类型 ar_sourcetype |
| 38 | faccrualschemeid | 计提方案 | int8 | 64 |  | √ | 0 | 计提方案 ar_accrualscheme |
| 39 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | ' ' | 生成凭证 |
| 40 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcurrentaccrualamt | 本次计提 | numeric | 23 | 10 | √ | 0.0000000000 | 本次计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_baddebtreserve_org |  | forgid |
| 2 | t_ar_baddebtreserve_pkey |  | fid |
