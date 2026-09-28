# 手工银行日记账-cas_manualbankjournal

## 单据体-子表 t_cas_manualbankjentry

- **表名称：** 单据体-子表
- **表名：** t_cas_manualbankjentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0 | 折本位币金额 |
| 3 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 4 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 5 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 8 | fcreditamount | 贷方金额（支出） | numeric | 19 | 6 | √ | 0 | 贷方金额（支出） |
| 9 | fdebitamount | 借方金额（收入） | numeric | 19 | 6 | √ | 0 | 借方金额（收入） |
| 10 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 11 | fsourcebillnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | foppacctnumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 16 | fsettlementnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 17 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fischeck | 勾对 | bpchar | 1 |  | √ | '0' | 勾对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_manualbankjentry |  | fentryid |
| 2 | idx_cas_manualbankjentry |  | fid |

---

## 手工银行日记账-主表 t_cas_manualbankjournal

- **表名称：** 手工银行日记账-主表
- **表名：** t_cas_manualbankjournal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 4 | fsourcebilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |
| 5 | fperiodid | 期间 | int8 | 64 |  |  | null | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已登记 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreditamount | 贷方金额（支出） | numeric | 19 | 6 | √ | 0 | 贷方金额（支出） |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fdebitamount | 借方金额（收入） | numeric | 19 | 6 | √ | 0 | 借方金额（收入） |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fbankacctid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 19 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_manualbankjournal |  | fid |
| 2 | idx_cas_mbj_fbillno |  | fbillno |
