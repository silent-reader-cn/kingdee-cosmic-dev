# 手工现金日记账-cas_manualcashjournal

## 手工现金日记账-主表 t_cas_manualcashjournal

- **表名称：** 手工现金日记账-主表
- **表名：** t_cas_manualcashjournal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 4 | fsourcebilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |
| 5 | fperiodid | 期间类型 | int8 | 64 |  |  | null | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已登记 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreditamount | 贷方金额（支出） | numeric | 19 | 6 | √ | 0 | 贷方金额（支出） |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fcashacctid | 现金账户 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 12 | fdebitamount | 借方金额（收入） | numeric | 19 | 6 | √ | 0 | 借方金额（收入） |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdirection | 方向 | varchar | 30 |  | √ | ' ' | 方向,枚举: 1 :借 2 :贷 |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 18 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 19 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_manualcashjournal |  | fid |
| 2 | idx_cas_mcj_fbillno |  | fbillno |

---

## 单据体-子表 t_cas_manualcashjentry

- **表名称：** 单据体-子表
- **表名：** t_cas_manualcashjentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0 | 折本位币金额 |
| 3 | foppunit | 对方单位 | varchar | 255 |  | √ | ' ' | 对方单位 |
| 4 | foppbank | foppbank | varchar | 255 |  | √ | ' ' |  |
| 5 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 8 | fcreditamount | 贷方金额（支出） | numeric | 19 | 6 | √ | 0 | 贷方金额（支出） |
| 9 | fdebitamount | 借方金额（收入） | numeric | 19 | 6 | √ | 0 | 借方金额（收入） |
| 10 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 11 | fsourcebillnumber | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 12 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | foppacctnumber | foppacctnumber | varchar | 255 |  | √ | ' ' |  |
| 16 | fsettlementnumber | fsettlementnumber | varchar | 2000 |  | √ | ' ' |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 19 | fischeck | 勾对 | bpchar | 1 |  | √ | '0' | 勾对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_manualcashjentry |  | fid |
| 2 | pk_cas_manualcashjentry |  | fentryid |
