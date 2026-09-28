# 账单池核销记录-er_billing_writeoff_rec

## 账单池核销记录-主表 t_er_billing_writeoff

- **表名称：** 账单池核销记录-主表
- **表名：** t_er_billing_writeoff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freasonfortransferout | 转出原因 | varchar | 50 |  | √ | ' ' | 转出原因 |
| 3 | fexecinoutamount | 执行转出金额 | numeric | 23 | 10 | √ | 0 | 执行转出金额 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fbillingid | 单据 | int8 | 64 |  | √ | 0 | 账单池 er_billingpool |
| 7 | fexecoffsetamount | 执行抵扣金额 | numeric | 23 | 10 | √ | 0 | 执行抵扣金额 |
| 8 | fexecamount | 本次执行报销金额 | numeric | 23 | 10 | √ | 0 | 本次执行报销金额 |
| 9 | fentitytype | 目标单据标识 | varchar | 50 |  | √ | ' ' | 目标单据标识 |
| 10 | famount | 本次报销金额 | numeric | 23 | 10 | √ | 0 | 本次报销金额 |
| 11 | fjsondata | 原始请求参数 | varchar | 1024 |  | √ | ' ' | 原始请求参数 |
| 12 | fruleversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |
| 13 | foffsetamount | 抵扣金额 | numeric | 23 | 10 | √ | 0 | 抵扣金额 |
| 14 | ftentryid | 目标单分录id | int8 | 64 |  | √ | 0 | 目标单分录id |
| 15 | fstatus | 执行状态 | varchar | 1 |  | √ | ' ' | 执行状态,枚举: 1 :成功 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fjsondata_tag | 原始请求参数_详情 | text | 0 |  |  | null | 原始请求参数_详情 |
| 18 | foperatetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: submit :提交 audit :审核 unsubmit :撤销 unaudit :反审核 |
| 19 | ftid | 目标单id | int8 | 64 |  | √ | 0 | 目标单id |
| 20 | fdesc | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 21 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 22 | fbillno | 目标单据编号 | varchar | 50 |  | √ | ' ' | 目标单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_billing_writeoff |  | fid |
| 2 | idx_er_billingid |  | fbillingid |
