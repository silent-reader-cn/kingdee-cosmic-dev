# 水利建设基金台账-totf_water_fund

## 水利建设基金台账-主表 t_totf_water_fund

- **表名称：** 水利建设基金台账-主表
- **表名：** t_totf_water_fund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 4 | famount | 本期应纳费额 | numeric | 23 | 10 | √ | 0 | 本期应纳费额 |
| 5 | fdeclaration | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立申报 2 :汇总申报 |
| 6 | fbqybtse | 本期应补（退）税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税（费）额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 9 | fenddate | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | frate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 12 | ftaxdeductionid | 减免政策代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftaxableitem | 应税项 | numeric | 23 | 10 | √ | 0 | 应税项 |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fcollectionitem | 征收项目-废弃 | varchar | 50 |  | √ | ' ' | 征收项目-废弃 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fstartdate | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 21 | fprepaytype | 预缴项目类型 | varchar | 50 |  | √ | ' ' | 预缴项目类型,枚举: VAT_YJXMLX_001 :异地建筑服务 VAT_YJXMLX_002 :建筑服务预收款 VAT_YJXMLX_003 :房地产项目预售 VAT_YJXMLX_004 :不动产转让 VAT_YJXMLX_005 :异地不动产出租 |
| 22 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 |
| 23 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 24 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_water_fund |  | fid |
| 2 | idx_taxc_waterfund_org_date |  | forgid,fstartdate,fenddate |
