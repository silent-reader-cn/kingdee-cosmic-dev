# 采购返利结算单-occpic_supbgt

## 关联子实体-子表 t_occpic_supbgtentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_supbgtentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconsignqty_old | 数量_原始携带值 | numeric | 23 | 10 |  | null | 数量_原始携带值 |
| 2 | ftaxrate | 税率（%）_确认携带值 | numeric | 23 | 10 |  | null | 税率（%）_确认携带值 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftaxrate_old | 税率（%）_原始携带值 | numeric | 23 | 10 |  | null | 税率（%）_原始携带值 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 7 | fprice | 价格_确认携带值 | numeric | 23 | 10 |  | null | 价格_确认携带值 |
| 8 | fperunitrebateamount | 单位数量返利_确认携带值 | numeric | 23 | 10 |  | null | 单位数量返利_确认携带值 |
| 9 | fperunitrebateamount_old | 单位数量返利_原始携带值 | numeric | 23 | 10 |  | null | 单位数量返利_原始携带值 |
| 10 | frebateamount | 返利金额_确认携带值 | numeric | 23 | 10 |  | null | 返利金额_确认携带值 |
| 11 | fconsignqty | 数量_确认携带值 | numeric | 23 | 10 |  | null | 数量_确认携带值 |
| 12 | ftax_old | 税额_原始携带值 | numeric | 23 | 10 |  | null | 税额_原始携带值 |
| 13 | ftax | 税额_确认携带值 | numeric | 23 | 10 |  | null | 税额_确认携带值 |
| 14 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 15 | fprofitrate_old | 返点率%_原始携带值 | numeric | 23 | 10 |  | null | 返点率%_原始携带值 |
| 16 | fprofitrate | 返点率%_确认携带值 | numeric | 23 | 10 |  | null | 返点率%_确认携带值 |
| 17 | factualunitrebate_old | 平均单位返利_原始携带值 | numeric | 23 | 10 |  | null | 平均单位返利_原始携带值 |
| 18 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 19 | fprice_old | 价格_原始携带值 | numeric | 23 | 10 |  | null | 价格_原始携带值 |
| 20 | frebateamount_old | 返利金额_原始携带值 | numeric | 23 | 10 |  | null | 返利金额_原始携带值 |
| 21 | fsaleamount_old | 金额_原始携带值 | numeric | 23 | 10 |  | null | 金额_原始携带值 |
| 22 | fsaleamount | 金额_确认携带值 | numeric | 23 | 10 |  | null | 金额_确认携带值 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 24 | factualunitrebate | 平均单位返利_确认携带值 | numeric | 23 | 10 |  | null | 平均单位返利_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_supbgtentry_lk |  | fpkid |
| 2 | idx_occpic_supbgtentry_lk_fk |  | fentryid |

---

## 采购返利结算单-关联追踪表 t_occpic_supbgt_tc

- **表名称：** 采购返利结算单-关联追踪表
- **表名：** t_occpic_supbgt_tc

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
| 1 | idx_occpic_supbgt_tc_tid |  | ftid |
| 2 | pk_occpic_supbgt_tc |  | fid |
| 3 | idx_occpic_supbgt_tc_tbill |  | ftbillid |

---

## 采购返利结算单-主表 t_occpic_supbgt

- **表名称：** 采购返利结算单-主表
- **表名：** t_occpic_supbgt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcashmode | 兑付方式 | bpchar | 1 |  | √ | 'A' | 兑付方式,枚举: A :上账资金池 B :应付账款红冲 |
| 3 | ftotalprecvyqty | 总数量 | numeric | 23 | 10 | √ | 0 | 总数量 |
| 4 | frpbudgetcycle | 结算周期 | bpchar | 1 |  | √ | 'A' | 结算周期,枚举: A :按年 B :按月 C :按周 D :全生命周期 E :按季度 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | ftotaltax | 总税额 | numeric | 23 | 10 | √ | 0 | 总税额 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprebudgetorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 12 | ftotallocaltax | 总税额(本位币) | numeric | 23 | 10 | √ | 0 | 总税额(本位币) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | frpenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 15 | frebateaccountid | 返利账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftotallocalrebateamount | 总返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 总返利金额(本位币) |
| 18 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | frpbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 23 | ftotalrbtamount | 总返利金额 | numeric | 23 | 10 | √ | 0 | 总返利金额 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 26 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 29 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 30 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | 采购返利政策 occpic_supplierpolicy |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | frpprecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 采购政策目标 occpic_suppliertarget |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_supbgtnum |  | fbillno |
| 2 | pk_occpic_supbgt |  | fid |

---

## 采购返利结算单-反写记录表 t_occpic_supbgtentry_wb

- **表名称：** 采购返利结算单-反写记录表
- **表名：** t_occpic_supbgtentry_wb

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
| 1 | idx_occpic_supbgtentry_wb_fk |  | fid |
| 2 | pk_occpic_supbgtentry_wb |  | fentryid |

---

## 关联子实体-子表 t_occpic_supbgt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_supbgt_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftotalprecvyqty | 总数量_确认携带值 | numeric | 23 | 10 |  | null | 总数量_确认携带值 |
| 3 | ftotalrbtamount_old | 总返利金额_原始携带值 | numeric | 23 | 10 |  | null | 总返利金额_原始携带值 |
| 4 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftotalrbtamount | 总返利金额_确认携带值 | numeric | 23 | 10 |  | null | 总返利金额_确认携带值 |
| 9 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 10 | ftotalprecvyqty_old | 总数量_原始携带值 | numeric | 23 | 10 |  | null | 总数量_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_supbgt_lk_fk |  | fid |
| 2 | pk_occpic_supbgt_lk |  | fpkid |

---

## 结算明细-子表 t_occpic_supbgtentry

- **表名称：** 结算明细-子表
- **表名：** t_occpic_supbgtentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 3 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fsaleorderid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpurinbillno | 采购入库单编码 | varchar | 80 |  | √ | ' ' | 采购入库单编码 |
| 7 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 8 | fperunitrebateamount | 单位数量返利 | numeric | 23 | 10 | √ | 0 | 单位数量返利 |
| 9 | frepolicytgtgroup | 政策目标组号 | int4 | 32 |  | √ | 0 | 政策目标组号 |
| 10 | frebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 12 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 13 | fconsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fpurinbillentryid | 采购入库单行ID | int8 | 64 |  | √ | 0 | 采购入库单行ID |
| 15 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 16 | fprofitrate | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 19 | fsaleamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 20 | fjoinamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 21 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 22 | fnojoinamount | 未关联金额 | numeric | 23 | 10 | √ | 0 | 未关联金额 |
| 23 | fisexistcombrow | 是否存在行合并 | bpchar | 1 |  | √ | '1' | 是否存在行合并 |
| 24 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | ftotalapbusamount | 累计应付金额 | numeric | 23 | 10 | √ | 0 | 累计应付金额 |
| 27 | flocalrebateamount | 返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 返利金额(本位币) |
| 28 | fsaleordernumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 29 | fsrcbillentryid | 源单行ID | int8 | 64 |  | √ | 0 | 源单行ID |
| 30 | fpurinbillid | 采购入库单ID | int8 | 64 |  | √ | 0 | 采购入库单ID |
| 31 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 32 | fjoinapbusamount | 关联应付金额 | numeric | 23 | 10 | √ | 0 | 关联应付金额 |
| 33 | fdeliveytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 34 | ffixedamount | 固定返利金额 | numeric | 23 | 10 | √ | 0 | 固定返利金额 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | factualunitrebate | 平均单位返利 | numeric | 23 | 10 | √ | 0 | 平均单位返利 |
| 37 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 采购政策目标 occpic_suppliertarget |
| 38 | fbizbillentryid | 业务单据行ID | int8 | 64 |  | √ | 0 | 业务单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_supbgtentryfid |  | fid |
| 2 | pk_occpic_supbgtentry |  | fentryid |
