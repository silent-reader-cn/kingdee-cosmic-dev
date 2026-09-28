# 营销费用汇总申请单-ocmem_convergeapply

## 关联子实体-子表 t_ocmem_cvapply_entity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocmem_cvapply_entity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_cvapply_entity_lk |  | fpkid |
| 2 | idx_ocmem_cvapply_entity_lk_fk |  | fentryid |

---

## 营销费用汇总申请单-关联追踪表 t_ocmem_convergeapply_tc

- **表名称：** 营销费用汇总申请单-关联追踪表
- **表名：** t_ocmem_convergeapply_tc

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
| 1 | idx_ocmem_convergeapply_tc_tid |  | ftid |
| 2 | pk_ocmem_convergeapply_tc |  | fid |
| 3 | idx_ocmem_convergeapply_tc_tbill |  | ftbillid |

---

## 营销费用汇总申请单-主表 t_ocmem_convergeapply

- **表名称：** 营销费用汇总申请单-主表
- **表名：** t_ocmem_convergeapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 5 | fenddate | 最晚结束日期 | timestamp | 0 |  |  | null | 最晚结束日期 |
| 6 | ftotallinkamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 7 | fpushbillentity | 下推生成单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | ftotalaccamount | 已累计金额 | numeric | 23 | 10 | √ | 0 | 已累计金额 |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdeptid | 费用申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fwarzoneid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :部分下推 E :已完成 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fbegindate | 最早开始日期 | timestamp | 0 |  |  | null | 最早开始日期 |
| 19 | fpayuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | freason | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | ftotalapplyamount | 申请总金额 | numeric | 23 | 10 | √ | 0 | 申请总金额 |
| 23 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 24 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 26 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | ' ' | 预算周期维度,枚举: A :按年 B :按月 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_convergeapply |  | fid |
| 2 | idx_ocmem_convergeapply_fid |  | fbillno |

---

## 单据体-子表 t_ocmem_cvapply_entity

- **表名称：** 单据体-子表
- **表名：** t_ocmem_cvapply_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbudgetitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 4 | fentryenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fbudgetmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 8 | factivityplanid | 营销活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | [活动类型 ocdbd_activitytype](../ocmem_files/ocdbd_activitytype.md) |
| 11 | fmeasurementunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fiteminfoid | 产品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 13 | famount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 15 | flinkqty | 已关联数量 | numeric | 23 | 10 | √ | 0 | 已关联数量 |
| 16 | fentrybegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 17 | fshopid | 门店名称 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 18 | fbgchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 19 | fbgchannelclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 20 | famtunapproved | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 21 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 22 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 23 | faccqty | 已累计数量 | numeric | 23 | 10 | √ | 0 | 已累计数量 |
| 24 | flinkamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 25 | fchannelid | 申请渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 26 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fbudgetitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 28 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | ffeecashtypeid | 费用兑付方式 | int8 | 64 |  | √ | 0 | [费用兑付方式 ocdbd_feecashtype](../ocmem_files/ocdbd_feecashtype.md) |
| 30 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 31 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 32 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | [预算余额表 ocdbd_budgetbalance](../ocmem_files/ocdbd_budgetbalance.md) |
| 33 | fparentexpenseid | 费用大类 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 34 | fbaseqty | 基本申请数量 | numeric | 23 | 10 | √ | 0 | 基本申请数量 |
| 35 | faccamount | 已累计金额 | numeric | 23 | 10 | √ | 0 | 已累计金额 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | faccountid | 账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_cvapply_entity |  | fentryid |
| 2 | idx_ocmem_cvapply_entity_fid |  | fid |

---

## 执行人-多选基础资料表 t_ocmem_cva_executors

- **表名称：** 执行人-多选基础资料表
- **表名：** t_ocmem_cva_executors

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_cva_executors |  | fpkid |
| 2 | idx_ocmem_cva_executors_fbid |  | fentryid,fbasedataid |

---

## 营销费用汇总申请单-反写记录表 t_ocmem_convergeapply_wb

- **表名称：** 营销费用汇总申请单-反写记录表
- **表名：** t_ocmem_convergeapply_wb

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
| 1 | idx_ocmem_convergeapply_wb_fk |  | fid |
| 2 | pk_ocmem_convergeapply_wb |  | fentryid |
