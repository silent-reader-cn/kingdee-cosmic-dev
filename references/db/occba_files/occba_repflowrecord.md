# 货补池流水表-occba_repflowrecord

## 货补池流水表-主表 t_occba_repflowrecord

- **表名称：** 货补池流水表-主表
- **表名：** t_occba_repflowrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalflowtypeid | 流水类型 | int8 | 64 |  | √ | 0 | [资金池流水类型 ocdbd_balflowtype](../occba_files/ocdbd_balflowtype.md) |
| 3 | fupdatefieldkey | 更新字段标识 | varchar | 50 |  | √ | ' ' | 更新字段标识 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fperiodyearid | 年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 7 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbalupdateruleid | 余额更新规则 | int8 | 64 |  | √ | 0 | [货补池更新规则 occba_repupdaterule](../occba_files/occba_repupdaterule.md) |
| 10 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fchangeamount | 变动金额 | numeric | 23 | 10 | √ | 0 | 变动金额 |
| 12 | fbillentity | 来源单据 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 13 | fstmcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | foperation | 操作 | varchar | 150 |  | √ | ' ' | 操作 |
| 15 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 16 | fbillno | 流水编号 | varchar | 80 |  | √ | ' ' | 流水编号 |
| 17 | frebateaccountid | 货补池 | int8 | 64 |  | √ | 0 | [货补池表 occba_replenishment](../occba_files/occba_replenishment.md) |
| 18 | fchangeqty | 变动数值 | numeric | 23 | 10 | √ | 0 | 变动数值 |
| 19 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 20 | fdeptid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 22 | frepaccounttypeid | 货补台账类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 23 | frepunitid | 货补单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fcreatetime | 流水发生时间 | timestamp | 0 |  |  | null | 流水发生时间 |
| 25 | famountvalue | 更新金额值 | varchar | 255 |  | √ | ' ' | 更新金额值 |
| 26 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 27 | foperationname | 操作名称 | varchar | 150 |  | √ | ' ' | 操作名称 |
| 28 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 31 | fsettlechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 32 | fflowstatus | 流水状态 | bpchar | 1 |  | √ | ' ' | 流水状态,枚举: A :已更新 B :已回滚 |
| 33 | frepaccountid | 货补账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 34 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 35 | fupdatevalue | 更新值(回滚用) | varchar | 50 |  | √ | ' ' | 更新值(回滚用) |
| 36 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 37 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 38 | fentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 39 | fupdatename | 更新字段名称 | varchar | 50 |  | √ | ' ' | 更新字段名称,枚举: repqty :货补数量 occupyqty :占用数量 availableqty :可用数量 accountamt :货补金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_repfr_billno |  | fbillno |
| 2 | pk_t_occba_repflowrecord |  | fid |
