# 我的资金池余额-ocdbd_myrebateaccount_b2b

## 关联子实体-子表 t_ocdbd_rebateaccount_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocdbd_rebateaccount_lk

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
| 1 | idx_ocdbd_rebateaccount_lk_fk |  | fid |
| 2 | pk_ocdbd_rebateaccount_lk |  | fpkid |

---

## 我的资金池余额-主表 t_ocdbd_rebateaccount

- **表名称：** 我的资金池余额-主表
- **表名：** t_ocdbd_rebateaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductlineid | fproductlineid | int8 | 64 |  | √ | 0 |  |
| 3 | foccupyamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsourceentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 6 | freceivechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 7 | favailablebalance | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 8 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fupdatedatetime | 最新更新时间 | timestamp | 0 |  |  | null | 最新更新时间 |
| 10 | ftype | 资金池类别 | bpchar | 1 |  | √ | 'A' | 资金池类别,枚举: A :品牌商 B :渠道商 |
| 11 | faccounttypeid | 账户类型 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 12 | fbalance | 账户金额 | numeric | 23 | 10 | √ | 0 | 账户金额 |
| 13 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 14 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 18 | fdimcolkey | 唯一标识 | varchar | 200 |  | √ | ' ' | 唯一标识 |
| 19 | fcustomerid | 客户名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_rebateaccount_occac |  | forgid,fcustomerid,fchannelid,faccounttypeid,fcurrencyid |
| 2 | pk_ocdbd_rebateaccount |  | fid |
