# 资金池幂等性-occba_rebateact_id

## 资金池幂等性-主表 t_occba_rebateact_id

- **表名称：** 资金池幂等性-主表
- **表名：** t_occba_rebateact_id

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountvalue | 变动金额值 | varchar | 255 |  | √ | ' ' | 变动金额值 |
| 3 | fcreatetime | 发生时间 | timestamp | 0 |  |  | null | 发生时间 |
| 4 | ftransaction | 更新事务 | bpchar | 1 |  | √ | 'A' | 更新事务,枚举: A :结算支付 B :余额冻结 C :单据使用 D :余额调整 E :资金使用 F :订单变更 G :余额释放 H :单据释放 I :订单关闭 J :订单反关闭 K :金额冻结 L :金额解冻 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | faccounttypeid | 账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 7 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 8 | fbillentity | 来源单据名称 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 10 | fentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 11 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fbilltype | 来源单据 | bpchar | 1 |  | √ | 'A' | 来源单据,枚举: A :返利结算单 B :要货订单 C :返利余额调整单 D :要货订单变更单 E :资金收入单 F :营销费用报销单 G :返利使用单 |
| 13 | frebateaccountid | 资金池余额 | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |
| 14 | fcolkey | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_rebateact_id |  | fid |
| 2 | idx_occba_rebateact_ckey |  | fcolkey |
| 3 | idx_occba_rebateact_sno |  | fsourcebillno |

---

## 资金池幂等性-关联追踪表 t_occba_rebateact_id_tc

- **表名称：** 资金池幂等性-关联追踪表
- **表名：** t_occba_rebateact_id_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 资金池幂等性-反写记录表 t_occba_rebateact_id_wb

- **表名称：** 资金池幂等性-反写记录表
- **表名：** t_occba_rebateact_id_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
