# 返利预提单-occpic_rebateaccrual

## 关联子实体-子表 t_occpic_accrual_ee_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_accrual_ee_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | ftaxamount | numeric | 23 | 10 |  | null |  |
| 2 | flocaltaxamount | 预提金额(本位币)_确认携带值 | numeric | 23 | 10 |  | null | 预提金额(本位币)_确认携带值 |
| 3 | ftaxamount_old | ftaxamount_old | numeric | 23 | 10 |  | null |  |
| 4 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | flocaltaxamount_old | 预提金额(本位币)_原始携带值 | numeric | 23 | 10 |  | null | 预提金额(本位币)_原始携带值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_accrual_ee_lk_fk |  | fentryid |
| 2 | pk_occpic_accrual_ee_lk |  | fpkid |

---

## 返利预提单-主表 t_occpic_accrual

- **表名称：** 返利预提单-主表
- **表名：** t_occpic_accrual

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccrualdate | 预提日期 | timestamp | 0 |  |  | null | 预提日期 |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | frebateclassid | 返利类别 | int8 | 64 |  | √ | 1 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsumamount | 不含税预提金额合计 | numeric | 23 | 10 | √ | 0 | 不含税预提金额合计 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | ftotallocaltax | 税额合计(本位币) | numeric | 23 | 10 | √ | 0 | 税额合计(本位币) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ftotallocaltaxamount | 预提金额合计(本位币) | numeric | 23 | 10 | √ | 0 | 预提金额合计(本位币) |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | ftallydate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 23 | fsumtaxamount | 预提金额合计 | numeric | 23 | 10 | √ | 0 | 预提金额合计 |
| 24 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fcustomerid | 返利客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_accrual |  | fid |
| 2 | idx_occpic_accrual_no |  | fbillno |

---

## 返利预提单-关联追踪表 t_occpic_accrual_tc

- **表名称：** 返利预提单-关联追踪表
- **表名：** t_occpic_accrual_tc

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
| 1 | pk_occpic_accrual_tc |  | fid |
| 2 | idx_occpic_accrual_tc_tbill |  | ftbillid |
| 3 | idx_occpic_accrual_tc_tid |  | ftid |

---

## 返利预提单-反写记录表 t_occpic_accrual_wb

- **表名称：** 返利预提单-反写记录表
- **表名：** t_occpic_accrual_wb

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
| 1 | idx_occpic_accrual_wb_fk |  | fid |
| 2 | pk_occpic_accrual_wb |  | fentryid |

---

## 预提明细-子表 t_occpic_accrual_ee

- **表名称：** 预提明细-子表
- **表名：** t_occpic_accrual_ee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaltaxamount | 预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 预提金额(本位币) |
| 3 | fmemdepartmentid | 预算承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fiteminfoid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 8 | famount | 不含税预提金额 | numeric | 23 | 10 | √ | 0 | 不含税预提金额 |
| 9 | fbizbillno | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 11 | frebatetargetid | 政策目标 | int8 | 64 |  | √ | 0 | [政策目标F7 ocdbd_rebatetargetf7](../occpic_files/ocdbd_rebatetargetf7.md) |
| 12 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmemitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 15 | flocaltax | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fmemitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 19 | fmemprovinceid | 预算省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | ftaxamount | 预提金额 | numeric | 23 | 10 | √ | 0 | 预提金额 |
| 21 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 22 | fmemregionid | 预算大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fjoinarbusamount | 关联应收金额 | numeric | 23 | 10 | √ | 0 | 关联应收金额 |
| 24 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fdepartmentid | 业务部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 29 | fmemchannelclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 30 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 31 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 32 | fmemmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 33 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 34 | ftotalarbusamount | 累计应收金额 | numeric | 23 | 10 | √ | 0 | 累计应收金额 |
| 35 | fmemchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 36 | frebatepolicyid | 返利政策 | int8 | 64 |  | √ | 0 | [返利政策F7 ocdbd_rebatepolicyf7](../occpic_files/ocdbd_rebatepolicyf7.md) |
| 37 | fmemyearid | 预算年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_accrualee_fid |  | fid |
| 2 | pk_occpic_accrual_ee |  | fentryid |

---

## 预算汇总-子表 t_occpic_accrual_see

- **表名称：** 预算汇总-子表
- **表名：** t_occpic_accrual_see

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsmemchannelclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 3 | fsmemdepartmentid | 预算承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsaccrualamount | 预提金额 | numeric | 23 | 10 | √ | 0 | 预提金额 |
| 5 | fsmemprovinceid | 预算省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsmemitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 8 | fsmemchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | fsmemmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 10 | fsmemregionid | 预算大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsmemitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 12 | fsfeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 13 | fsmemyearid | 预算年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_accrualsee_fid |  | fid |
| 2 | pk_occpic_accrual_see |  | fentryid |
