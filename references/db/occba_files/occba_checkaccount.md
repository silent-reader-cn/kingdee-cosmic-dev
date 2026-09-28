# 往来对账单-occba_checkaccount

## 单据体-子表 t_occba_checkactentry

- **表名称：** 单据体-子表
- **表名：** t_occba_checkactentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 3 | fopeningbalance | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fpayamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 7 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | fsrcbillentryseq | 源单分录行号 | int4 | 32 |  | √ | 0 | 源单分录行号 |
| 9 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | faccountdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 11 | fpayableamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 12 | fsrcbillentity | 源单实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | freceivableamount | 应收余额 | numeric | 23 | 10 | √ | 0 | 应收余额 |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 18 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsrcbillentryid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 20 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 21 | fsettlechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 22 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 23 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 24 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 25 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fsrcbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fsummary | 摘要 | varchar | 36 |  | √ | ' ' | 摘要,枚举: im_saloutbill :收到商品金额 cas_recbill :采购付款金额 occba_moneyincome :采购付款金额 sum :小计 occba_channelbalance :期初余额 |
| 29 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_checkactentry_fid |  | fid |
| 2 | pk_occba_checkactentry |  | fentryid |

---

## 往来对账单-主表 t_occba_checkaccount

- **表名称：** 往来对账单-主表
- **表名：** t_occba_checkaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplychannelid | 供货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 3 | fcheckuserid | 对账人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fopeningbalance | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 5 | fpayamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 6 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisdetail | 是否明细对账表 | bpchar | 1 |  | √ | '0' | 是否明细对账表 |
| 11 | fpayableamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 12 | fcheckdate | 对账日期 | timestamp | 0 |  |  | null | 对账日期 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | finvalidstatus | 作废状态 | bpchar | 1 |  | √ | 'A' | 作废状态,枚举: A :未作废 B :已作废 |
| 21 | fsettlechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 22 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 23 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 24 | fbalance | 应收余额 | numeric | 23 | 10 | √ | 0 | 应收余额 |
| 25 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 29 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | 'A' | 对账状态,枚举: A :未确认 B :已确认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_checkaccount |  | fid |
| 2 | idx_occba_checkaccount_bno |  | fbillno |
