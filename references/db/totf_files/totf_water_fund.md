# 水利建设基金台账-totf_water_fund

## 水利建设基金台账-主表 t_totf_water_fund

- **表名称：** 水利建设基金台账-主表
- **表名：** t_totf_water_fund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 5 | famount | 本期应纳费额 | numeric | 23 | 10 | √ | 0 | 本期应纳费额 |
| 6 | fdeclaration | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立申报 2 :汇总申报 |
| 7 | fsourcedata | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 import :数据导入 autocollect :自动取数 zzsprepay :增值税预缴申报表 |
| 8 | fbqybtse | 本期应补（退）税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税（费）额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 11 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | frate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 14 | ftaxdeductionid | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftaxableitem | 应税项 | numeric | 23 | 10 | √ | 0 | 应税项 |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 21 | fcollectionitem | 征收项目-废弃 | varchar | 50 |  | √ | ' ' | 征收项目-废弃 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 24 | fprepaytype | 预缴项目类型 | varchar | 50 |  | √ | ' ' | 预缴项目类型,枚举: VAT_YJXMLX_001 :异地建筑服务 VAT_YJXMLX_002 :建筑服务预收款 VAT_YJXMLX_003 :房地产项目预售 VAT_YJXMLX_004 :不动产转让 VAT_YJXMLX_005 :异地不动产出租 |
| 25 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 |
| 26 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 27 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_water_fund |  | fid |
| 2 | idx_taxc_waterfund_org_date |  | forgid,fstartdate,fenddate |
