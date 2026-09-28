# 资金请款申请-fca_applytransdownbill

## 资金请款申请-关联追踪表 t_fca_applytransdownbill_tc

- **表名称：** 资金请款申请-关联追踪表
- **表名：** t_fca_applytransdownbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | t_fca_applytransdownbill_tc_pkey |  | fid |
| 2 | idx_fca_applytransdownbill_tc_tid |  | ftid |
| 3 | idx_fca_applytransdownbill_tc_tbill |  | ftbillid |

---

## 划拨明细-多语言表 t_fca_apptransdown_entry_l

- **表名称：** 划拨明细-多语言表
- **表名：** t_fca_apptransdown_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftransdetail | 划拨业务处理说明 | varchar | 255 |  | √ | ' ' | 划拨业务处理说明 |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fca_apptransdown_entry_l |  | fpkid |
| 2 | idx_fca_apptransdentry_fenryid |  | fentryid |

---

## 关联子实体-子表 t_fca_applytransdownbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fca_applytransdownbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_applytransdownbill_lk_pkey |  | fpkid |
| 2 | idx_fca_applytransdownbill_lk_fk |  | fid |

---

## 划拨明细-子表 t_fca_apptransdown_entry

- **表名称：** 划拨明细-子表
- **表名：** t_fca_apptransdown_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 请款事由 | varchar | 255 |  | √ | ' ' | 请款事由 |
| 3 | ftransbillno | 划拨单 | varchar | 80 |  | √ | ' ' | 划拨单 |
| 4 | facctgrpid | 母子账户组 | int8 | 64 |  | √ | 0 | [母子账户组 fca_acctgroup](../fca_files/fca_acctgroup.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | finneracctid | 子账户内部账号 | int8 | 64 |  | √ | 0 | [内部账户管理 ifm_inneracct](../ifm_files/ifm_inneracct.md) |
| 7 | ftransdetail | ftransdetail | varchar | 255 |  | √ | ' ' |  |
| 8 | fpbankacctid | 母账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 9 | fpaystatus | 付款状态 | varchar | 80 |  | √ | ' ' | 付款状态,枚举: beiproc :银企处理中 payproc :付款处理中 paysuccess :付款成功 payfail :付款失败 noconfirm :交易未确认 init : |
| 10 | ftransbill | ftransbill | int8 | 64 |  | √ | 0 |  |
| 11 | fisgeneratebill | 是否生成请款单 | bpchar | 1 |  | √ | '0' | 是否生成请款单 |
| 12 | fapplyamt | 申请下拨金额 | numeric | 19 | 6 | √ | 0.000000 | 申请下拨金额 |
| 13 | ftransamt | 核定下拨金额 | numeric | 19 | 6 | √ | 0.000000 | 核定下拨金额 |
| 14 | flockedamt | 已锁定金额 | numeric | 19 | 6 | √ | 0 | 已锁定金额 |
| 15 | fabankacctid | 实际母账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fsubacctid | 子账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fca_transdowndetail_fid |  | fid,fseq |
| 2 | t_fca_apptransdown_entry_pkey |  | fentryid |

---

## 资金请款申请-主表 t_fca_apptransdown

- **表名称：** 资金请款申请-主表
- **表名：** t_fca_apptransdown

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fparentorgid | 母账户资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织(不用) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreateuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftransamount | 核定下拨总金额 | numeric | 19 | 6 | √ | 0.000000 | 核定下拨总金额 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | famount | 申请下拨总金额 | numeric | 19 | 6 | √ | 0.000000 | 申请下拨总金额 |
| 11 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 15 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 16 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fexpcdate | 期望下拨日期 | timestamp | 0 |  |  | null | 期望下拨日期 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcompanyid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_apptransdown_billno |  | fbillno |
| 2 | idx_apptransdown_parorg |  | fparentorgid |
| 3 | t_fca_apptransdown_pkey |  | fid |
| 4 | idx_apptransdown_company |  | fcompanyid |

---

## 资金请款申请-反写记录表 t_fca_applytransdownbill_wb

- **表名称：** 资金请款申请-反写记录表
- **表名：** t_fca_applytransdownbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_applytransdownbill_wb_pkey |  | fentryid |
| 2 | idx_fca_applytransdownbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_fca_transdowndetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fca_transdowndetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transdowndetail_lk_pkey |  | fpkid |
| 2 | idx_fca_transdowndetail_lk_fk |  | fentryid |

---

## 资金请款申请-多语言表 t_fca_apptransdown_l

- **表名称：** 资金请款申请-多语言表
- **表名：** t_fca_apptransdown_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 申请事由 | varchar | 255 |  | √ | ' ' | 申请事由 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_apptransdown_l_pkey |  | fpkid |
| 2 | idx_pk_fca_apptransdown_l_fid |  | fid,flocaleid |
