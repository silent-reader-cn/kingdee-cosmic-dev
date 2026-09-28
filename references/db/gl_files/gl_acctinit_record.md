# 同步记录-gl_acctinit_record

## 同步记录-主表 t_gl_acctinit_record

- **表名称：** 同步记录-主表
- **表名：** t_gl_acctinit_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbegincreditfor | 期初余额贷方原币 | numeric | 23 | 10 | √ | 0 | 期初余额贷方原币 |
| 3 | fnewrecord | 是否最新记录 | bpchar | 1 |  | √ | '0' | 是否最新记录 |
| 4 | fsourceapp | 来源应用 | bpchar | 1 |  | √ | '1' | 来源应用,枚举: 1 :应收款管理 2 :应付款管理 |
| 5 | fbegindebitfor | 期初余额借方原币 | numeric | 23 | 10 | √ | 0 | 期初余额借方原币 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcurlocalid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fcreatorid | 操作人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsynctime | 同步日期 | timestamp | 0 |  |  | null | 同步日期 |
| 10 | fyeardebitqty | 本年累计借方数量 | numeric | 23 | 10 | √ | 0 | 本年累计借方数量 |
| 11 | fbillno | 记录编号 | varchar | 80 |  | √ | ' ' | 记录编号 |
| 12 | fyearcreditfor | 本年累计贷方原币 | numeric | 23 | 10 | √ | 0 | 本年累计贷方原币 |
| 13 | fyeardebitlocal | 本年累计借方本位币 | numeric | 23 | 10 | √ | 0 | 本年累计借方本位币 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbegindebitlocal | 期初余额借方本位币 | numeric | 23 | 10 | √ | 0 | 期初余额借方本位币 |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | funiquekey | 唯一标识 | varchar | 255 |  | √ | ' ' | 唯一标识 |
| 20 | fbegindebitqty | 期初余额借方数量 | numeric | 23 | 10 | √ | 0 | 期初余额借方数量 |
| 21 | fyearcreditqty | 本年累计贷方数量 | numeric | 23 | 10 | √ | 0 | 本年累计贷方数量 |
| 22 | fbegincreditlocal | 期初余额贷方本位币 | numeric | 23 | 10 | √ | 0 | 期初余额贷方本位币 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 25 | fmfailreason | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 26 | fbegincreditqty | 期初余额贷方数量 | numeric | 23 | 10 | √ | 0 | 期初余额贷方数量 |
| 27 | fyeardebitfor | 本年累计借方原币 | numeric | 23 | 10 | √ | 0 | 本年累计借方原币 |
| 28 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 29 | fyearcreditlocal | 本年累计贷方本位币 | numeric | 23 | 10 | √ | 0 | 本年累计贷方本位币 |
| 30 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | faccountid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 34 | fsyncstatus | 同步状态 | bpchar | 1 |  | √ | '1' | 同步状态,枚举: 0 :失败 1 :成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_acctinit_rcd_fperiodid |  | fperiod |
| 2 | pk_gl_acctinit_record |  | fid |
| 3 | idx_gl_acctinit_rcd_fbookid |  | fbookid |
| 4 | idx_gl_acctinit_rcd_funiquekey |  | funiquekey |
| 5 | idx_gl_acctinit_rcd_faccountid |  | faccountid |
| 6 | idx_gl_acctinit_rcd_fbillno |  | fbillno |

---

## 同步记录-多语言表 t_gl_acctinit_record_l

- **表名称：** 同步记录-多语言表
- **表名：** t_gl_acctinit_record_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmfailreason | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_acctinit_record_l |  | fpkid |
| 2 | idx_gl_acctinit_record_l |  | fid,flocaleid |
