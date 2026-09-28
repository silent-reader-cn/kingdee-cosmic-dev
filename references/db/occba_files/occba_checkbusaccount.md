# 资金池对账单-occba_checkbusaccount

## 单据体-子表 t_occba_checkbusactentry

- **表名称：** 单据体-子表
- **表名：** t_occba_checkbusactentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryamount | 入账金额 | numeric | 23 | 10 | √ | 0 | 入账金额 |
| 3 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 4 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsettlechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | frebateamount | 回退金额 | numeric | 23 | 10 | √ | 0 | 回退金额 |
| 8 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 9 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | fuseamount | 使用金额 | numeric | 23 | 10 | √ | 0 | 使用金额 |
| 11 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fsrcbillentity | 源单实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fsrcbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |
| 14 | freceivableamount | 应收余额 | numeric | 23 | 10 | √ | 0 | 应收余额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | faccountid | 账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 18 | fsummary | 摘要 | varchar | 36 |  | √ | ' ' | 摘要,枚举: 0 :期初余额 1 :余额入账 2 :余额调整 3 :余额使用 4 :订单关闭退回余额 5 :退货退回余额 |
| 19 | fcustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_checkbusactentry |  | fentryid |
| 2 | idx_occba_checkbusactentry |  | fid |

---

## 资金池对账单-主表 t_occba_checkbusaccount

- **表名称：** 资金池对账单-主表
- **表名：** t_occba_checkbusaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentryamount | 入账金额 | numeric | 23 | 10 | √ | 0 | 入账金额 |
| 3 | fcheckuserid | 对账人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fopeningbalance | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 5 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | frebateamount | 回退金额 | numeric | 23 | 10 | √ | 0 | 回退金额 |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisdetail | 是否明细对账表 | bpchar | 1 |  | √ | '0' | 是否明细对账表 |
| 11 | fcheckdate | 对账日期 | timestamp | 0 |  |  | null | 对账日期 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | finvalidstatus | 作废状态 | bpchar | 1 |  | √ | 'A' | 作废状态,枚举: A :未作废 B :已作废 |
| 20 | fsettlechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 21 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 22 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 23 | fbalance | 期末余额 | numeric | 23 | 10 | √ | 0 | 期末余额 |
| 24 | fuseamount | 使用金额 | numeric | 23 | 10 | √ | 0 | 使用金额 |
| 25 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | faccountid | 账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 29 | fcustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 30 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | 'A' | 对账状态,枚举: A :未确认 B :已确认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_checkbusaccount |  | fid |
| 2 | idx_occba_checkbusact_key |  | fsettleorgid,fsettlechannelid,fcustomerid,faccountid,fcurrencyid |
| 3 | idx_occba_checkbusact_bno |  | fbillno |
