# 全渠道资金池流水-occba_flowrecord_chl

## 全渠道资金池流水-反写记录表 t_occpic_flowrecord_wb

- **表名称：** 全渠道资金池流水-反写记录表
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

## 全渠道资金池流水-主表 t_occpic_flowrecord

- **表名称：** 全渠道资金池流水-主表
- **表名：** t_occpic_flowrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalflowtypeid | 流水类型 | int8 | 64 |  | √ | 0 | [资金池流水类型 ocdbd_balflowtype](../occba_files/ocdbd_balflowtype.md) |
| 3 | fafteramount | 更新后余额 | numeric | 23 | 10 | √ | 0 | 更新后余额 |
| 4 | fproductlineid | fproductlineid | int8 | 64 |  | √ | 0 |  |
| 5 | fupdatefieldkey | 更新字段标识 | varchar | 50 |  | √ | ' ' | 更新字段标识 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbeforeamount | 更新前余额 | numeric | 23 | 10 | √ | 0 | 更新前余额 |
| 8 | freceivechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | faccoutid | 资金账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 10 | ftransaction | 更新事务 | bpchar | 1 |  | √ | 'A' | 更新事务,枚举: A :结算支付 B :余额冻结 C :单据使用 D :余额调整 E :资金使用 F :订单变更 G :余额释放 H :单据释放 I :订单关闭 J :订单反关闭 K :金额冻结 L :金额解冻 R :余额回滚 |
| 11 | fverifiedamount | 已核销金额 | numeric | 23 | 10 | √ | 0 | 已核销金额 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbalupdateruleid | 余额更新规则 | int8 | 64 |  | √ | 0 | [资金池余额更新规则 ocdbd_balupdaterule](../occba_files/ocdbd_balupdaterule.md) |
| 14 | fchangeamount | 变动金额 | numeric | 23 | 10 | √ | 0 | 变动金额 |
| 15 | fofficeid | fofficeid | int8 | 64 |  | √ | 0 |  |
| 16 | fchannelid | 渠道ID | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 17 | fstmcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fbillentity | 来源单据名称 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 19 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 20 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 21 | fbillno | 流水ID | varchar | 80 |  | √ | ' ' | 流水ID |
| 22 | frebateaccountid | 资金池余额 | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |
| 23 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 24 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 25 | fcreatetime | 流水发生时间 | timestamp | 0 |  |  | null | 流水发生时间 |
| 26 | famountvalue | 更新金额值 | varchar | 255 |  | √ | ' ' | 更新金额值 |
| 27 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 28 | foperationname | 操作名称 | varchar | 100 |  | √ | ' ' | 操作名称 |
| 29 | fflowstatus | 流水状态 | bpchar | 1 |  | √ | 'A' | 流水状态,枚举: A :已更新 B :已回滚 |
| 30 | fproductid | fproductid | int8 | 64 |  | √ | 0 |  |
| 31 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 32 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 33 | fentryid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 34 | fupdatename | 更新字段名称 | varchar | 50 |  | √ | ' ' | 更新字段名称,枚举: balance :账户金额 occupyamount :占用金额 availablebalance :可用余额 |
| 35 | fbilltype | 来源单据 | bpchar | 1 |  | √ | 'A' | 来源单据,枚举: A :返利结算单 B :要货订单 C :返利余额调整单 D :要货订单变更单 E :资金收入单 F :营销费用报销单 G :返利使用单 |
| 36 | fcustomerid | 直接客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_flow_channel |  | fchannelid |
| 2 | idx_occpic_flowrd_sbillid |  | fsourcebillid,fflowstatus |
| 3 | idx_occpic_flow_createtime |  | fcreatetime |
| 4 | pk_occpic_flowrecord |  | fid |
| 5 | idx_ocdbd_flowrecord_bno |  | fbillno |

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

## 全渠道资金池流水-关联追踪表 t_occpic_flowrecord_tc

- **表名称：** 全渠道资金池流水-关联追踪表
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
