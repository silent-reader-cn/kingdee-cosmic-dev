# 保证金预提利息单-fbd_surety_preint

## 关联子实体-子表 t_fbd_surety_settleint_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fbd_surety_settleint_lk

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
| 1 | idx_fbd_surety_settleint_lk_fk |  | fid |
| 2 | pk_fbd_surety_settleint_lk |  | fpkid |

---

## 保证金预提利息单-关联追踪表 t_fbd_surety_settleint_tc

- **表名称：** 保证金预提利息单-关联追踪表
- **表名：** t_fbd_surety_settleint_tc

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
| 1 | idx_fbd_surety_settleint_tc_tbill |  | ftbillid |
| 2 | idx_fbd_surety_settleint_tc_tid |  | ftid |
| 3 | pk_fbd_surety_settleint_tc |  | fid |

---

## 保证金预提利息单-主表 t_fbd_surety_settleint

- **表名称：** 保证金预提利息单-主表
- **表名：** t_fbd_surety_settleint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwriteoffamt | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 3 | fispushrec | fispushrec | bpchar | 1 |  | √ | '0' |  |
| 4 | finsttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 5 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | frecordstatus | 记账状态 | varchar | 50 |  | √ | ' ' | 记账状态,枚举: norecord :未记账 alrecord :已记账 |
| 7 | fnowriteoffamt | 剩余未冲销金额 | numeric | 23 | 10 | √ | 0 | 剩余未冲销金额 |
| 8 | fwriteoffstatus | 冲销状态 | varchar | 50 |  | √ | ' ' | 冲销状态,枚举: part_writeoff :部分冲销 writeoff :已冲销 no_writeoff :未冲销 red_writeoff :红字冲销 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsurplusamount | 剩余金额 | numeric | 23 | 10 | √ | 0 | 剩余金额 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fprestenddate | 预提结束日 | timestamp | 0 |  |  | null | 预提结束日 |
| 13 | foperatetype | 操作类别 | varchar | 50 |  | √ | ' ' | 操作类别,枚举: preint :预提利息 reverseint :冲销预提利息 |
| 14 | fexpiredate | 保证金到期日期 | timestamp | 0 |  |  | null | 保证金到期日期 |
| 15 | fdrawamount | 存款金额 | numeric | 23 | 10 | √ | 0 | 存款金额 |
| 16 | fintdate | 保证金起息日期 | timestamp | 0 |  |  | null | 保证金起息日期 |
| 17 | factpreinstamt | 实际预提利息 | numeric | 23 | 10 | √ | 0 | 实际预提利息 |
| 18 | frecbillid | frecbillid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 预提单编号 | varchar | 30 |  | √ | ' ' | 预提单编号 |
| 20 | fclientorgid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 21 | fremark | fremark | varchar | 50 |  | √ | ' ' |  |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | frecbillno | frecbillno | varchar | 30 |  | √ | ' ' |  |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 预提单创建时间 | timestamp | 0 |  |  | null | 预提单创建时间 |
| 26 | floanbillno | 保证金单编号 | varchar | 50 |  | √ | ' ' | 保证金单编号 |
| 27 | fwriteoffpreintbillid | 被冲销预提单id | int8 | 64 |  | √ | 0 | 被冲销预提单id |
| 28 | frevenuetype | frevenuetype | varchar | 50 |  | √ | ' ' |  |
| 29 | fprestartdate | 预提开始日 | timestamp | 0 |  |  | null | 预提开始日 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | floanorgid | 贷款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | floantype | 贷款类型 | varchar | 50 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 33 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 34 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 35 | fpredictpreinstamt | 测算预提利息 | numeric | 23 | 10 | √ | 0 | 测算预提利息 |
| 36 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: settleint :收益 preint :预提 |
| 37 | floaneracctbankid | floaneracctbankid | int8 | 64 |  | √ | 0 |  |
| 38 | fcurrencyid | 存款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | ffinorginfoid | 贷款人 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_surety_settleint |  | fid |
| 2 | idx_fbd_surety_settleint_sid |  | fsourcebillid |
| 3 | idx_fbd_surety_settleint |  | fbillno |

---

## 保证金预提利息单-反写记录表 t_fbd_surety_settleint_wb

- **表名称：** 保证金预提利息单-反写记录表
- **表名：** t_fbd_surety_settleint_wb

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
| 1 | pk_fbd_surety_settleint_wb |  | fentryid |
| 2 | idx_fbd_surety_settleint_wb_fk |  | fid |

---

## 利息预算明细-子表 t_fbd_preinstbill_entry

- **表名称：** 利息预算明细-子表
- **表名：** t_fbd_preinstbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frate | 利率(%) | numeric | 23 | 10 | √ | 0 | 利率(%) |
| 3 | finststartdate | 计息开始日 | timestamp | 0 |  |  | null | 计息开始日 |
| 4 | finstdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 5 | fratetrandays | 利率转换天数 | int8 | 64 |  | √ | 0 | 利率转换天数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finstenddate | 计息结束日 | timestamp | 0 |  |  | null | 计息结束日 |
| 8 | finstprincipalamt | 计息本金 | numeric | 23 | 10 | √ | 0 | 计息本金 |
| 9 | finstamt | 利息金额 | numeric | 23 | 10 | √ | 0 | 利息金额 |
| 10 | finstctg | 利息类别 | varchar | 50 |  | √ | ' ' | 利息类别,枚举: normal :正常利息 extend :展期利息 overdue :逾期利息 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_preinstbill_entry |  | fid |
| 2 | pk_fbd_preinstbill_entry |  | fentryid |
