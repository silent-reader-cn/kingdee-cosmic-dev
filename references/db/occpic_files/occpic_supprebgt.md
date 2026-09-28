# 采购返利预结算单-occpic_supprebgt

## 采购返利预结算单-关联追踪表 t_occpic_supprebgt_tc

- **表名称：** 采购返利预结算单-关联追踪表
- **表名：** t_occpic_supprebgt_tc

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
| 1 | idx_occpic_supprebgt_tc_tid |  | ftid |
| 2 | idx_occpic_supprebgt_tc_tbill |  | ftbillid |
| 3 | pk_occpic_supprebgt_tc |  | fid |

---

## 采购返利预结算单-主表 t_occpic_supprebgt

- **表名称：** 采购返利预结算单-主表
- **表名：** t_occpic_supprebgt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalprecvyqty | 总数量 | numeric | 23 | 10 | √ | 0 | 总数量 |
| 3 | faccrualformulaid | 预提计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 4 | frpbudgetcycle | 结算周期 | bpchar | 1 |  | √ | 'A' | 结算周期,枚举: A :按年 B :按月 C :按周 D :全生命周期 E :按季度 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | ftotaltax | 总税额 | numeric | 23 | 10 | √ | 0 | 总税额 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprebudgetorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | ftotalhasbgtamt | 总已结算金额 | numeric | 23 | 10 | √ | 0 | 总已结算金额 |
| 11 | fisbudgetfinish | 手工结算完成 | bpchar | 1 |  | √ | '0' | 手工结算完成 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | ftotallocaltax | 总税额(本位币) | numeric | 23 | 10 | √ | 0 | 总税额(本位币) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | frpenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftotallocalrebateamount | 总返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 总返利金额(本位币) |
| 19 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 F :结算完成 E :部分结算 |
| 21 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | frpbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | ftotalrbtamount | 总返利金额 | numeric | 23 | 10 | √ | 0 | 总返利金额 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsupplierid | 返利供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 29 | fbillsource | 单据来源 | bpchar | 1 |  | √ | 'A' | 单据来源,枚举: A :手工新增 B :自动化计算 |
| 30 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 31 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 32 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | 采购返利政策 occpic_supplierpolicy |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | frpprecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 采购政策目标 occpic_suppliertarget |
| 36 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_supprebgt_num |  | fbillno |
| 2 | pk_occpic_supprebgt |  | fid |

---

## 采购返利预结算单-反写记录表 t_occpic_supprebgt_wb

- **表名称：** 采购返利预结算单-反写记录表
- **表名：** t_occpic_supprebgt_wb

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
| 1 | pk_occpic_supprebgt_wb |  | fentryid |
| 2 | idx_occpic_supprebgt_wb_fk |  | fid |

---

## 关联子实体-子表 t_occpic_supprebgtentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_supprebgtentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | frebateamount_old | 返利金额_原始携带值 | numeric | 23 | 10 |  | null | 返利金额_原始携带值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 8 | frebateamount | 返利金额_确认携带值 | numeric | 23 | 10 |  | null | 返利金额_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_supprebgtentry_lk |  | fpkid |
| 2 | idx_occpic_supprebgtentry_lk_fk |  | fentryid |

---

## 预结算明细-子表 t_occpic_supprebgtentry

- **表名称：** 预结算明细-子表
- **表名：** t_occpic_supprebgtentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 3 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | faperunitrebateamount | 预提单位返利 | numeric | 23 | 10 | √ | 0 | 预提单位返利 |
| 5 | fsaleorderid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpurinbillno | 采购入库单编码 | varchar | 80 |  | √ | ' ' | 采购入库单编码 |
| 8 | fhasjoinamount | 关联结算金额 | numeric | 23 | 10 | √ | 0 | 关联结算金额 |
| 9 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 10 | fperunitrebateamount | 单位数量返利 | numeric | 23 | 10 | √ | 0 | 单位数量返利 |
| 11 | frepolicytgtgroup | 政策目标组号 | int4 | 32 |  | √ | 0 | 政策目标组号 |
| 12 | flocalhasbgtamount | 累计结算金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计结算金额(本位币) |
| 13 | frebateamount | 返利金额 | numeric | 23 | 10 | √ | 0 | 返利金额 |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 15 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 16 | fconsignqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 17 | fpurinbillentryid | 采购入库单行ID | int8 | 64 |  | √ | 0 | 采购入库单行ID |
| 18 | frowstatus | 行状态 | bpchar | 1 |  | √ | 'C' | 行状态,枚举: C :未结算 F :部分结算 E :结算完成 |
| 19 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 20 | fprofitrate | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 21 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 22 | fbizdatastatus | 业务数据状态 | bpchar | 1 |  | √ | 'N' | 业务数据状态,枚举: N :正常 D :已删除 |
| 23 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fsaleamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 25 | fjoinamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 26 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 27 | fisexistcombrow | 是否存在行合并 | bpchar | 1 |  | √ | '1' | 是否存在行合并 |
| 28 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 29 | fafixedamount | 预提固定返利金额 | numeric | 23 | 10 | √ | 0 | 预提固定返利金额 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | ftotalapbusamount | 累计应付金额 | numeric | 23 | 10 | √ | 0 | 累计应付金额 |
| 32 | flocalrebateamount | 返利金额(本位币) | numeric | 23 | 10 | √ | 0 | 返利金额(本位币) |
| 33 | fhasbgtamount | 累计结算金额 | numeric | 23 | 10 | √ | 0 | 累计结算金额 |
| 34 | fsaleordernumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 35 | fsrcbillentryid | 源单行ID | int8 | 64 |  | √ | 0 | 源单行ID |
| 36 | fpurinbillid | 采购入库单ID | int8 | 64 |  | √ | 0 | 采购入库单ID |
| 37 | faccrualamount | 预提金额 | numeric | 23 | 10 | √ | 0 | 预提金额 |
| 38 | faprofitrate | 预提返点率% | numeric | 23 | 10 | √ | 0 | 预提返点率% |
| 39 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 40 | fjoinapbusamount | 关联应付金额 | numeric | 23 | 10 | √ | 0 | 关联应付金额 |
| 41 | fdeliveytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 42 | ffixedamount | 固定返利金额 | numeric | 23 | 10 | √ | 0 | 固定返利金额 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | factualunitrebate | 平均单位返利 | numeric | 23 | 10 | √ | 0 | 平均单位返利 |
| 45 | frebatepolicytargetid | 政策目标 | int8 | 64 |  | √ | 0 | 采购政策目标 occpic_suppliertarget |
| 46 | fbizbillentryid | 业务单据行ID | int8 | 64 |  | √ | 0 | 业务单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_supprebgtentry |  | fentryid |
| 2 | idx_occpic_supprebgten_id |  | fid |
