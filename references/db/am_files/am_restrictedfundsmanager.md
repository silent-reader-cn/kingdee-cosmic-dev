# 受限资金管理-am_restrictedfundsmanager

## 受限资金管理-反写记录表 t_am_restrictedfundsmanag_wb

- **表名称：** 受限资金管理-反写记录表
- **表名：** t_am_restrictedfundsmanag_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_am_restrictedfundsmanag_wb |  | fentryid |
| 2 | idx_am_restrictedfundsm_wb_0 |  | fid |

---

## 受限资金管理-主表 t_am_restrictedfundsmanag

- **表名称：** 受限资金管理-主表
- **表名：** t_am_restrictedfundsmanag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisautolift | 到期自动解除受限 | bpchar | 1 |  | √ | '0' | 到期自动解除受限 |
| 3 | fsrcbillno | 受限资金单据编号 | varchar | 30 |  | √ | ' ' | 受限资金单据编号 |
| 4 | festimatedliftdate | 预计解除受限日期 | timestamp | 0 |  |  | null | 预计解除受限日期 |
| 5 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | factualliftdate | 实际解除受限日期 | timestamp | 0 |  |  | null | 实际解除受限日期 |
| 7 | fbusinesstype | 业务分类 | varchar | 50 |  | √ | ' ' | 业务分类,枚举: 1 :增加受限 2 :解除受限 |
| 8 | fliftdate | 解除受限日期 | timestamp | 0 |  |  | null | 解除受限日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fisallrestricted | fisallrestricted | bpchar | 1 |  | √ | '0' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | frestrictedfoundstypeid | 受限资金类型 | int8 | 64 |  | √ | 0 | 受限资金类型 am_restrictedfundstype |
| 13 | funrestrictedamt | 当前可解除受限金额 | numeric | 23 | 10 | √ | 0 | 当前可解除受限金额 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fbankacctid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 16 | fthistimeunblockamt | 本次解除受限金额 | numeric | 23 | 10 | √ | 0 | 本次解除受限金额 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcomment | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | frestricteddate | 受限日期 | timestamp | 0 |  |  | null | 受限日期 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 24 | frestrictedamt | 受限金额 | numeric | 23 | 10 | √ | 0 | 受限金额 |
| 25 | fbankid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 26 | fcurrencyid | 受限资金币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_restrictedfundsmanag_0 |  | fbillstatus,fbusinesstype,fsrcbillno |
| 2 | pk_t_am_restrictedfundsmanag |  | fid |

---

## 受限资金管理-关联追踪表 t_am_restrictedfundsmanag_tc

- **表名称：** 受限资金管理-关联追踪表
- **表名：** t_am_restrictedfundsmanag_tc

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
| 1 | idx_am_restrictedfundsmanag_tc_tid |  | ftid |
| 2 | idx_am_restrictedfundsm_tc_0 |  | ftbillid |
| 3 | idx_am_restrictedfundsm_tc_1 |  | ftid |
| 4 | pk_am_restrictedfundsmanag_tc |  | fid |
| 5 | idx_am_restrictedfundsmanag_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_am_restrictedfundsmanag_lk

- **表名称：** 关联子实体-子表
- **表名：** t_am_restrictedfundsmanag_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_am_restrictedfundsmanag_lk |  | fpkid |
| 2 | idx_am_restrictedfundsm_lk_0 |  | fid |
