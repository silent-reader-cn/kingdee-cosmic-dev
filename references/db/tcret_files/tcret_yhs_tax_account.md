# 印花税台账-tcret_yhs_tax_account

## 附件-附件表 t_tcret_yhs_tz_a

- **表名称：** 附件-附件表
- **表名：** t_tcret_yhs_tz_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_yhs_tz_a |  | fpkid |
| 2 | idx_yhs_tz_a_fbasedataid |  | fbasedataid |
| 3 | idx_yhs_tz_a_fid |  | fid |

---

## 印花税台账-主表 t_tcret_yhs_tz

- **表名称：** 印花税台账-主表
- **表名：** t_tcret_yhs_tz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 4 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 印花税税率 tpo_tcsd_taxrateentry |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsourceid | 税源ID | int8 | 64 |  | √ | 0 | [印花税税源信息基础资料 tcret_yhs_taxsource_base](../tcret_files/tcret_yhs_taxsource_base.md) |
| 7 | fvoucherdate | 应税凭证书立日期 | timestamp | 0 |  |  | null | 应税凭证书立日期 |
| 8 | fgathernumber | 采集编号 | varchar | 50 |  | √ | ' ' | 采集编号 |
| 9 | fvoucherno | 应税凭证编号 | varchar | 50 |  | √ | ' ' | 应税凭证编号 |
| 10 | ftaxation | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: aqhz :按期汇总 hdzs :核定征收 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fvouchername | 应税凭证名称 | varchar | 50 |  | √ | ' ' | 应税凭证名称 |
| 14 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 15 | fbizdimensiontype | 业务维度（废弃） | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fsubtaxitem | 子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 17 | fynse | 本期（次）应纳税额 | numeric | 23 | 10 | √ | 0 | 本期（次）应纳税额 |
| 18 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fcalctaxamount | 计税金额 | numeric | 23 | 10 | √ | 0 | 计税金额 |
| 21 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fverifyrate | 核定比例 | numeric | 23 | 10 | √ | 0 | 核定比例 |
| 26 | fserialno | 规则取数明细流水号 | varchar | 50 |  | √ | ' ' | 规则取数明细流水号 |
| 27 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季度 halfyear :半年 year :年 single :次 |
| 28 | fbizdimensionname | 业务维度值（废弃） | varchar | 200 |  | √ | ' ' | 业务维度值（废弃） |
| 29 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 30 | fdeclaretype | 申报期限类型 | varchar | 50 |  | √ | ' ' | 申报期限类型,枚举: aqsb :按期申报 acsb :按次申报 |
| 31 | fvouchernum | 应税凭证数量 | int8 | 64 |  | √ | 0 | 应税凭证数量 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fpaytype | 缴纳类型 | varchar | 50 |  | √ | ' ' | 缴纳类型,枚举: bdjn :本地缴纳 ydjn :异地缴纳 |
| 34 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 35 | fdeductioncode | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 36 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 37 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 38 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 39 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :自动取数 useradd :手工新增 import :数据引入 prepay :增值税预缴申报表 |
| 40 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 41 | fbizdimensionid | 业务维度值ID（废弃） | varchar | 50 |  | √ | ' ' | 业务维度值ID（废弃） |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_yhs_tz |  | fid |
| 2 | idx_t_tcret_yhs_tz_forgid |  | forgid,fskssqq,fskssqz,ftaxitem |
