# 税源采集台账数据-tcret_yhs_tax_account_fb

## 税源采集台账数据-主表 t_tcret_yhs_tzfb

- **表名称：** 税源采集台账数据-主表
- **表名：** t_tcret_yhs_tzfb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 4 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 印花税税率 tpo_tcsd_taxrateentry |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftaxsourceno | 税源采集编号 | varchar | 50 |  | √ | ' ' | 税源采集编号 |
| 7 | fvoucherdate | 应纳税凭证书立（领受）日期 | timestamp | 0 |  |  | null | 应纳税凭证书立（领受）日期 |
| 8 | fvoucherno | 应纳税凭证编号 | varchar | 50 |  | √ | ' ' | 应纳税凭证编号 |
| 9 | ftaxation | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: aqhz :按期汇总 hdzs :核定征收 |
| 10 | forignalid | 台账id | int8 | 64 |  | √ | 0 | 台账id |
| 11 | fvouchername | 应税凭证名称 | varchar | 50 |  | √ | ' ' | 应税凭证名称 |
| 12 | fskssqz | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 13 | fbizdimensiontype | 业务维度（废弃） | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fsubtaxitem | 子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 15 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 16 | fcalctaxamount | 计税金额或件数 | numeric | 23 | 10 | √ | 0 | 计税金额或件数 |
| 17 | fverifyrate | 核定比例 | numeric | 23 | 10 | √ | 0 | 核定比例 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季度 halfyear :半年 year :年 single :次 |
| 20 | fbizdimensionname | 业务维度值（废弃） | varchar | 200 |  | √ | ' ' | 业务维度值（废弃） |
| 21 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 22 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: aqsb :按期申报 acsb :按次申报 |
| 23 | fvouchernum | 应税凭证数量 | int8 | 64 |  | √ | 0 | 应税凭证数量 |
| 24 | fpaytype | 缴纳类型 | varchar | 50 |  | √ | ' ' | 缴纳类型,枚举: bdjn :本地缴纳 ydjn :异地缴纳 |
| 25 | fskssqq | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 26 | fdeductioncode | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 27 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 29 | fbizdimensionid | 业务维度值ID（废弃） | varchar | 50 |  | √ | ' ' | 业务维度值ID（废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_yhs_tzfb |  | fid |
| 2 | t_tcret_yhs_tzfb_forgid_idx |  | forgid,fskssqq,fskssqz,ftaxitem |
