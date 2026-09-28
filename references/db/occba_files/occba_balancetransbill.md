# 资金池调拨单-occba_balancetransbill

## 资金池调拨单-主表 t_occba_baltransbill

- **表名称：** 资金池调拨单-主表
- **表名：** t_occba_baltransbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frecchannelid | 收款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ftransdate | 调拨日期 | timestamp | 0 |  |  | null | 调拨日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftransstatus | 调拨状态 | bpchar | 1 |  | √ | 'A' | 调拨状态,枚举: A :未调拨 B :已调拨 |
| 13 | ftranstype | 调拨类型 | bpchar | 1 |  | √ | 'A' | 调拨类型,枚举: A :品牌商 B :渠道商 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_baltransdate |  | ftransdate |
| 2 | pk_occba_baltransbill |  | fid |

---

## 调拨明细-子表 t_occba_baltransentry

- **表名称：** 调拨明细-子表
- **表名：** t_occba_baltransentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutaccbalance | 调出账户余额 | numeric | 23 | 10 | √ | 0 | 调出账户余额 |
| 3 | fjoinoutamt | 已关联调出金额 | numeric | 23 | 10 | √ | 0 | 已关联调出金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | foutacctype | 调出账号标识 | bpchar | 1 |  | √ | ' ' | 调出账号标识,枚举: A :激励 B :费用 C :资金 |
| 6 | finaccid | 调入账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 7 | fafterinbalance | 调入后余额 | numeric | 23 | 10 | √ | 0 | 调入后余额 |
| 8 | fincustomerid | 调入客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 9 | finamt | 调入金额 | numeric | 23 | 10 | √ | 0 | 调入金额 |
| 10 | fafteroutbalance | 调出后余额 | numeric | 23 | 10 | √ | 0 | 调出后余额 |
| 11 | foutdeptid | 调出部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | findeptid | 调入部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | finitemclsid | 调入商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 14 | foutchannelid | 调出渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | ftotaloutamt | 已累计调出金额 | numeric | 23 | 10 | √ | 0 | 已累计调出金额 |
| 16 | foutcustomerid | 调出客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | foutaccid | 调出账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 18 | fjoininamt | 已关联调入金额 | numeric | 23 | 10 | √ | 0 | 已关联调入金额 |
| 19 | foutamt | 调出金额 | numeric | 23 | 10 | √ | 0 | 调出金额 |
| 20 | finchannelid | 调入渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 21 | foutitemclsid | 调出商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 22 | ftotalinamt | 已累计调入金额 | numeric | 23 | 10 | √ | 0 | 已累计调入金额 |
| 23 | finacctype | 调入账号标识 | bpchar | 1 |  | √ | ' ' | 调入账号标识,枚举: A :激励 B :费用 C :资金 |
| 24 | finaccbalance | 调入账户余额 | numeric | 23 | 10 | √ | 0 | 调入账户余额 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_baltransentry |  | fid |
| 2 | pk_occba_baltransentry |  | fentryid |
