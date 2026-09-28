# 客户资金池调整单-occba_cusbalancadjust_b2b

## 客户资金池调整单-反写记录表 t_occpic_balanceadjust_wb

- **表名称：** 客户资金池调整单-反写记录表
- **表名：** t_occpic_balanceadjust_wb

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
| 1 | pk_occpic_balanceadjust_wb |  | fentryid |
| 2 | idx_occpic_balanceadjust_wb_fk |  | fid |

---

## 客户资金池调整单-主表 t_occpic_balanceadjust

- **表名称：** 客户资金池调整单-主表
- **表名：** t_occpic_balanceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frptofficeid | frptofficeid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 9 | freceivechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsignpartyid | fsignpartyid | int8 | 64 |  | √ | 0 |  |
| 14 | fadjusttype | 调整类型 | bpchar | 1 |  | √ | 'A' | 调整类型,枚举: A :品牌商 B :渠道商 |
| 15 | fadjusttime | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 16 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_balanceadjust_no |  | fbillno |
| 2 | pk_occpic_balanceadjust |  | fid |

---

## 客户资金池调整单-关联追踪表 t_occpic_balanceadjust_tc

- **表名称：** 客户资金池调整单-关联追踪表
- **表名：** t_occpic_balanceadjust_tc

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
| 1 | pk_occpic_balanceadjust_tc |  | fid |
| 2 | idx_occpic_balanceadjust_tc_tbill |  | ftbillid |
| 3 | idx_occpic_balanceadjust_tc_tid |  | ftid |

---

## 单据体-子表 t_occpic_balancead_entry

- **表名称：** 单据体-子表
- **表名：** t_occpic_balancead_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 3 | fadjustedamount | 调整后余额 | numeric | 23 | 10 | √ | 0 | 调整后余额 |
| 4 | faccounttypeid | 资金账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | faccountamount | 账户金额 | numeric | 23 | 10 | √ | 0 | 账户金额 |
| 7 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fcustomerid | 直接客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_balanceadentry_fid |  | fid |
| 2 | pk_occpic_balancead_entry |  | fentryid |

---

## 关联子实体-子表 t_occpic_balanceadjust_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_balanceadjust_lk

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
| 1 | pk_occpic_balanceadjust_lk |  | fpkid |
| 2 | idx_occpic_balanceadjust_lk_fk |  | fid |
