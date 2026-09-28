# 变更支付渠道-fca_transchgbill

## 划拨明细-子表 t_fca_transchgbill_entry

- **表名称：** 划拨明细-子表
- **表名：** t_fca_transchgbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fsourceentryid_c | 源分录id | varchar | 50 |  | √ | ' ' | 源分录id |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ftransamt | 划拨金额 | numeric | 19 | 6 | √ | 0.000000 | 划拨金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsubacctid | 子账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 9 | fsubpaychan | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 online :网上银行 counter :柜台 |
| 10 | fsubacctcompid | 子账户资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_entry_pkey |  | fentryid |
| 2 | t_fca_transchgbill_et_fid |  | fid |

---

## 变更支付渠道-反写记录表 t_fca_transchgbill_wb

- **表名称：** 变更支付渠道-反写记录表
- **表名：** t_fca_transchgbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_wb_fid |  | fid |
| 2 | t_fca_transchgbill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_fca_transchgbill_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fca_transchgbill_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_entry_lk_pkey |  | fpkid |
| 2 | t_fca_trchgbi_et_lk_fid |  | fentryid |

---

## 变更支付渠道-主表 t_fca_transchgbill

- **表名称：** 变更支付渠道-主表
- **表名：** t_fca_transchgbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fpaychan | 新支付渠道 | varchar | 30 |  | √ | ' ' | 新支付渠道,枚举: |
| 8 | fsourcebillno | 划拨单号 | varchar | 60 |  | √ | ' ' | 划拨单号 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fischanging | 变更中 | bpchar | 1 |  | √ | '1' | 变更中 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcebilltype | 源单据类型 | varchar | 30 |  | √ | ' ' | 源单据类型 |
| 13 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :审核拒绝 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 17 | fprevpaychan | 原支付渠道 | varchar | 30 |  | √ | ' ' | 原支付渠道,枚举: bei :银企互联 online :网上银行 counter :柜台 |
| 18 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 19 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 20 | fbankid | fbankid | int8 | 64 |  | √ | 0 |  |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | faccountbankid | 母账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 24 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 25 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_pkey |  | fid |
| 2 | t_fca_transchgbill_num |  | fbillno |

---

## 关联子实体-子表 t_fca_transchgbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fca_transchgbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_lk_fid |  | fid |
| 2 | t_fca_transchgbill_lk_pkey |  | fpkid |

---

## 变更支付渠道-多语言表 t_fca_transchgbill_l

- **表名称：** 变更支付渠道-多语言表
- **表名：** t_fca_transchgbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescription | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_l_pkey |  | fpkid |
| 2 | t_fca_transchgbill_l_fid |  | fid,flocaleid |

---

## 变更支付渠道-关联追踪表 t_fca_transchgbill_tc

- **表名称：** 变更支付渠道-关联追踪表
- **表名：** t_fca_transchgbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transchgbill_tc_pkey |  | fid |
| 2 | idx_fca_transchgbill_tc_tid |  | ftid |
| 3 | t_fca_transchgbill_tc_fid |  | ftbillid |
| 4 | idx_fca_transchgbill_tc_tbill |  | ftbillid |
