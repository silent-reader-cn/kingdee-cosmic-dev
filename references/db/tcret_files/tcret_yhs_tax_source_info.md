# 印花税税源信息-tcret_yhs_tax_source_info

## 印花税税源信息-主表 t_tcret_sycj_yhsxx

- **表名称：** 印花税税源信息-主表
- **表名：** t_tcret_sycj_yhsxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fvoucherdate | 应税凭证书立日期 | timestamp | 0 |  |  | null | 应税凭证书立日期 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fvouchertaxno | 应税凭证税务编号 | varchar | 50 |  | √ | ' ' | 应税凭证税务编号 |
| 7 | fbizdimensiontype | 业务维度（废弃） | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fsbbbillno | 申报表编号（废弃） | varchar | 50 |  | √ | ' ' | 申报表编号（废弃） |
| 9 | fdfslrmc | 对方书立人名称 | varchar | 50 |  | √ | ' ' | 对方书立人名称 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fsbbbillstatus | 申报表单据状态（废弃） | varchar | 50 |  | √ | ' ' | 申报表单据状态（废弃）,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fverifyrate | 核定比例 | numeric | 23 | 10 | √ | 0.0000000000 | 核定比例 |
| 14 | fserialno | 规则取数明细流水号 | varchar | 50 |  | √ | ' ' | 规则取数明细流水号 |
| 15 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季度 halfyear :半年 year :年 single :次 |
| 16 | fvouchernum | 应税凭证数量 | int8 | 64 |  | √ | 0 | 应税凭证数量 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 19 | fdeductioncode | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 20 | factualsettledate | 实际结算日期 | timestamp | 0 |  |  | null | 实际结算日期 |
| 21 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 22 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 23 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统采集 import :模板引入 useradd :手工新增 fromacc :台账采集 |
| 24 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 25 | fbizdimensionid | 业务维度值ID（废弃） | varchar | 50 |  | √ | ' ' | 业务维度值ID（废弃） |
| 26 | factualsettleamount | 实际结算金额 | numeric | 23 | 10 | √ | 0 | 实际结算金额 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fisxgm | 是否小规模 | bpchar | 1 |  | √ | '0' | 是否小规模 |
| 30 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 印花税税率（树） tpo_tcsd_taxrateentrytree |
| 31 | fdfslrsjje | 对方书立人涉及金额 | numeric | 23 | 10 | √ | 0 | 对方书立人涉及金额 |
| 32 | fgathernumber | 采集编号 | varchar | 50 |  | √ | ' ' | 采集编号 |
| 33 | fvoucherno | 应税凭证编号 | varchar | 50 |  | √ | ' ' | 应税凭证编号 |
| 34 | ftaxation | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: aqhz :按期汇总 hdzs :核定征收 |
| 35 | fdfslrnssbh | 对方书立人纳税识别号（统一社会信用代码） | varchar | 50 |  | √ | ' ' | 对方书立人纳税识别号（统一社会信用代码） |
| 36 | fdeclarestatus | 申报状态（废弃） | varchar | 50 |  | √ | ' ' | 申报状态（废弃）,枚举: editing :未申报 declaring :申报中 declared :已申报 undeclare :未编制 declarefailed :申报失败 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fvouchername | 应税凭证名称 | varchar | 50 |  | √ | ' ' | 应税凭证名称 |
| 39 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 40 | fsubtaxitem | 子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 41 | fynse | 本期（次）应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期（次）应纳税额 |
| 42 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 43 | fcalctaxamount | 计税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 计税金额 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fbizdimensionname | 业务维度值（废弃） | varchar | 200 |  | √ | ' ' | 业务维度值（废弃） |
| 47 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 48 | fdeclaretype | 申报期限类型 | varchar | 50 |  | √ | ' ' | 申报期限类型,枚举: aqsb :按期申报 acsb :按次申报 |
| 49 | fdeclareid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 50 | fpaytype | 缴纳类型 | varchar | 50 |  | √ | ' ' | 缴纳类型,枚举: bdjn :本地缴纳 ydjn :异地缴纳 |
| 51 | fverifybasis | 计税依据 | numeric | 23 | 10 | √ | 0.0000000000 | 计税依据 |
| 52 | fdeducttax | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_sycj_yhsxx |  | fid |
| 2 | idx_tcret_sycj_yhsxx |  | forgid,fskssqq,fskssqz |
