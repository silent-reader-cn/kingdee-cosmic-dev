# 文化事业建设费台账-totf_whsyjsf_account

## 文化事业建设费台账-主表 t_totf_whsyjsf_account

- **表名称：** 文化事业建设费台账-主表
- **表名：** t_totf_whsyjsf_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftaxableitem | 应征收入 | numeric | 23 | 10 | √ | 0 | 应征收入 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | famount | 本期应纳费额 | numeric | 23 | 10 | √ | 0 | 本期应纳费额 |
| 10 | fbqybtse | 本期应补（退）税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税（费）额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 13 | fenddate | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | frate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 16 | fstartdate | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 17 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 |
| 18 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 19 | ftaxdeductionid | 减免政策代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 20 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_whsyjsf_account |  | fid |
| 2 | idx_totf_whsyjsf_org_date |  | forgid,fstartdate,fenddate |
