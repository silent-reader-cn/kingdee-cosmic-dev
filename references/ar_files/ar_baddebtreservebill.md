# 初始化坏账准备-ar_baddebtreservebill

## 初始化坏账准备-主表 t_ar_baddebtreservebill

- **表名称：** 初始化坏账准备-主表
- **表名：** t_ar_baddebtreservebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbaddebtreserveamt | 坏账准备金额 | numeric | 23 | 10 | √ | 0.0000000000 | 坏账准备金额 |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | freceivabledate | 应收款日 | timestamp | 0 |  |  | null | 应收款日 |
| 5 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsourcebillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | funsettlelocalamt | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 11 | freferencerate | 参考比率 | numeric | 19 | 6 | √ | 0.000000 | 参考比率 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 14 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fsourcebilltype | 源单标识 | varchar | 30 |  | √ | ' ' | 源单标识 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | finitbaddebtid | 初始化ID | int8 | 64 |  | √ | 0 | 初始化ID |
| 19 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | funsettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 21 | freceivableamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 24 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fpolicytypeid | 政策类型 | int8 | 64 |  | √ | 0 | 政策类型 ar_policytype |
| 26 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 27 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 28 | fsourcetypeid | 来源类型 | int8 | 64 |  | √ | 0 | 来源类型 ar_sourcetype |
| 29 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_baddebtresb_sb |  | fsourcebillid |
| 2 | idx_ar_baddebtreservebill_org |  | forgid |
| 3 | idx_ar_baddebtresb_init |  | finitbaddebtid |
| 4 | t_ar_baddebtreservebill_pkey |  | fid |
