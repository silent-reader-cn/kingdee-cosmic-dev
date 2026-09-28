# 预算余额流水-ocmem_flowrecord_bgbal

## 预算余额流水-反写记录表 t_occpic_flowrecord_wb

- **表名称：** 预算余额流水-反写记录表
- **表名：** t_occpic_flowrecord_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_flowrecord_wb |  | fentryid |
| 2 | idx_occpic_flowrecord_wb_fk |  | fid |

---

## 关联子实体-子表 t_occpic_flowrecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_flowrecord_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_flowrecord_lk_fk |  | fid |
| 2 | pk_occpic_flowrecord_lk |  | fpkid |

---

## 预算余额流水-关联追踪表 t_occpic_flowrecord_tc

- **表名称：** 预算余额流水-关联追踪表
- **表名：** t_occpic_flowrecord_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_flowrecord_tc |  | fid |
| 2 | idx_occpic_flowrecord_tc_tid |  | ftid |
| 3 | idx_occpic_flowrecord_tc_tbill |  | ftbillid |

---

## 预算余额流水-主表 t_ocmem_balrecord

- **表名称：** 预算余额流水-主表
- **表名：** t_ocmem_balrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalflowtypeid | 流水类型 | int8 | 64 |  | √ | 0 | [资金池流水类型 ocdbd_balflowtype](../occba_files/ocdbd_balflowtype.md) |
| 3 | fafteramount | 更新后余额 | numeric | 23 | 10 | √ | 0 | 更新后余额 |
| 4 | fupdatefieldkey | 更新字段标识 | varchar | 50 |  | √ | ' ' | 更新字段标识 |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbudgetmonthid | 月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 7 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 8 | ffeetype | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 9 | fbeforeamount | 更新前余额 | numeric | 23 | 10 | √ | 0 | 更新前余额 |
| 10 | fverifiedamount | 已核销金额 | numeric | 23 | 10 | √ | 0 | 已核销金额 |
| 11 | fflowtypeid | fflowtypeid | int8 | 64 |  | √ | 0 |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbalupdateruleid | 余额更新规则 | int8 | 64 |  | √ | 0 | [资金池余额更新规则 ocdbd_balupdaterule](../occba_files/ocdbd_balupdaterule.md) |
| 14 | fbudgetyearid | 年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 15 | fchangeamount | 发生金额 | numeric | 23 | 10 | √ | 0 | 发生金额 |
| 16 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 17 | foperation | 操作 | varchar | 80 |  | √ | ' ' | 操作 |
| 18 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 19 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | [预算余额表 ocdbd_budgetbalance](../ocmem_files/ocdbd_budgetbalance.md) |
| 20 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 21 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 22 | fcreatetime | 流水发生时间 | timestamp | 0 |  |  | null | 流水发生时间 |
| 23 | famountvalue | 更新金额值 | varchar | 510 |  | √ | ' ' | 更新金额值 |
| 24 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 25 | foperationname | 操作名称 | varchar | 80 |  | √ | ' ' | 操作名称 |
| 26 | fitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 27 | fupdateamount | fupdateamount | numeric | 23 | 10 | √ | 0 |  |
| 28 | fsourcebill | 来源单据名称 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 29 | fbilloperation | fbilloperation | varchar | 80 |  | √ | ' ' |  |
| 30 | fflowstatus | 流水状态 | bpchar | 1 |  | √ | ' ' | 流水状态,枚举: A :已更新 B :已回滚 |
| 31 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 32 | fchannelclassid | 渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 33 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fentryid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 35 | fupdatename | 更新字段名称 | varchar | 50 |  | √ | ' ' | 更新字段名称,枚举: availableamount :可用余额 amount :期初金额 usedamount :已用金额 targetamount :目标预算金额 availabletargetamount :目标可用余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocmem_balrecord_bbid |  | fbudgetbalanceid |
| 2 | pk_ocmem_balrecord |  | fid |
