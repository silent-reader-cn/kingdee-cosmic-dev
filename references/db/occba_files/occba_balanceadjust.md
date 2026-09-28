# 资金池调整单-occba_balanceadjust

## 资金池调整单-主表 t_occpic_balanceadjust

- **表名称：** 资金池调整单-主表
- **表名：** t_occpic_balanceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fadjustclass | 调整类别 | bpchar | 1 |  | √ | 'B' | 调整类别,枚举: A :错误调整 B :业务调整 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | frptofficeid | frptofficeid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 10 | freceivechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsignpartyid | fsignpartyid | int8 | 64 |  | √ | 0 |  |
| 15 | fadjusttype | 调整类型 | bpchar | 1 |  | √ | 'A' | 调整类型,枚举: A :品牌商 B :渠道商 |
| 16 | fadjusttime | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 17 | fareadeptid | fareadeptid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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

## 关联子实体-子表 t_occpic_balancead_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_balancead_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustamount | 调整金额_确认携带值 | numeric | 23 | 10 |  | null | 调整金额_确认携带值 |
| 2 | fadjustamount_old | 调整金额_原始携带值 | numeric | 23 | 10 |  | null | 调整金额_原始携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_balancead_entry_lk |  | fpkid |
| 2 | idx_occpic_balancead_entry_lk_fk |  | fentryid |

---

## 单据体-子表 t_occpic_balancead_entry

- **表名称：** 单据体-子表
- **表名：** t_occpic_balancead_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | faccountamount | 账户金额 | numeric | 23 | 10 | √ | 0 | 账户金额 |
| 6 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 7 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 8 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 9 | fadjustedamount | 调整后余额 | numeric | 23 | 10 | √ | 0 | 调整后余额 |
| 10 | faccounttypeid | 资金账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 11 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fcustomerid | 直接客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

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

## 资金池调整单-反写记录表 t_occpic_balanceadjust_wb

- **表名称：** 资金池调整单-反写记录表
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

## 资金池调整单-关联追踪表 t_occpic_balanceadjust_tc

- **表名称：** 资金池调整单-关联追踪表
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
