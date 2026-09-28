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

## 预算余额流水-主表 t_ocmem_balrecord

- **表名称：** 预算余额流水-主表
- **表名：** t_ocmem_balrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalflowtypeid | 流水类型 | int8 | 64 |  | √ | 0 | 资金池流水类型 ocdbd_balflowtype |
| 3 | fafteramount | 更新后余额 | numeric | 23 | 10 | √ | 0 | 更新后余额 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbudgetmonthid | 月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 6 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | ffeetype | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 8 | fbeforeamount | 更新前余额 | numeric | 23 | 10 | √ | 0 | 更新前余额 |
| 9 | fflowtypeid | fflowtypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbalupdateruleid | 余额更新规则 | int8 | 64 |  | √ | 0 | 资金池余额更新规则 ocdbd_balupdaterule |
| 12 | fbudgetyearid | 年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 13 | fchangeamount | 发生金额 | numeric | 23 | 10 | √ | 0 | 发生金额 |
| 14 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | foperation | 操作 | varchar | 80 |  | √ | ' ' | 操作 |
| 16 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 17 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | 预算余额表 ocdbd_budgetbalance |
| 18 | fcreatetime | 流水发生时间 | timestamp | 0 |  |  | null | 流水发生时间 |
| 19 | famountvalue | 更新金额值 | varchar | 510 |  | √ | ' ' | 更新金额值 |
| 20 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 21 | foperationname | 操作名称 | varchar | 80 |  | √ | ' ' | 操作名称 |
| 22 | fitemid | 预算产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 23 | fupdateamount | fupdateamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | fsourcebill | 来源单据名称 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 25 | fbilloperation | fbilloperation | varchar | 80 |  | √ | ' ' |  |
| 26 | fflowstatus | 流水状态 | bpchar | 1 |  | √ | ' ' | 流水状态,枚举: A :已更新 B :已回滚 |
| 27 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 28 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fentryid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocmem_balrecord_bbid |  | fbudgetbalanceid |
| 2 | pk_ocmem_balrecord |  | fid |
