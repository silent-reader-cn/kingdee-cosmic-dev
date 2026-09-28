# 营销费用核销单-ocmem_mc_reimburse

## 营销费用核销单-反写记录表 t_ocmem_mc_reimbur_wb

- **表名称：** 营销费用核销单-反写记录表
- **表名：** t_ocmem_mc_reimbur_wb

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
| 1 | idx_ocmem_mc_reimbur_wb_fk |  | fid |
| 2 | pk_ocmem_mc_reimbur_wb |  | fentryid |

---

## 关联子实体-子表 t_ocmem_mc_reiment_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocmem_mc_reiment_lk

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
| 1 | pk_ocmem_mc_reiment_lk |  | fpkid |
| 2 | idx_ocmem_mc_reiment_lk_fk |  | fentryid |

---

## 核销分录-子表 t_ocmem_mc_reimentry

- **表名称：** 核销分录-子表
- **表名：** t_ocmem_mc_reimentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrywriteoffname | 核销方式 | varchar | 80 |  | √ | ' ' | 核销方式 |
| 3 | freachrate | freachrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | famtapproved | 核准金额 | numeric | 23 | 10 | √ | 0 | 核准金额 |
| 5 | fsourceid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 6 | fsourceentryid | 来源单据分录id | varchar | 100 |  | √ | ' ' | 来源单据分录id |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmeasurementunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fiteminfoid | 产品名称 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 12 | fshopid | 门店名称 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 13 | famtunapproved | 未核准金额 | numeric | 23 | 10 | √ | 0 | 未核准金额 |
| 14 | famtapply | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 15 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | ffeecashtypeid | 费用兑付方式 | int8 | 64 |  | √ | 0 | [费用兑付方式 ocdbd_feecashtype](../ocmem_files/ocdbd_feecashtype.md) |
| 18 | fqty | 核销数量 | numeric | 23 | 10 | √ | 0 | 核销数量 |
| 19 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 20 | fpromotionaddress | 促销地点 | varchar | 100 |  | √ | ' ' | 促销地点 |
| 21 | fentryexpensetypeid | 行类型 | int8 | 64 |  | √ | 0 | [费用行类型分录 ocdbd_expensetype_entry](../ocmem_files/ocdbd_expensetype_entry.md) |
| 22 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 23 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 24 | fshoptypeid | 门店类型 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 25 | fcostamount | fcostamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fplansaleqty | fplansaleqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | flossrate | flossrate | numeric | 23 | 10 | √ | 0 |  |
| 28 | fentrytype | fentrytype | bpchar | 1 |  | √ | ' ' |  |
| 29 | fproductprice | 活动产品价格（元） | numeric | 23 | 10 | √ | 0 | 活动产品价格（元） |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fverifiedrebateamount | 已使用核销金额 | numeric | 23 | 10 | √ | 0 | 已使用核销金额 |
| 32 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 33 | funcomplianceamount | 不合规扣减额 | numeric | 23 | 10 | √ | 0 | 不合规扣减额 |
| 34 | famount | 核销金额 | numeric | 23 | 10 | √ | 0 | 核销金额 |
| 35 | foriginalamt | 初审金额 | numeric | 23 | 10 | √ | 0 | 初审金额 |
| 36 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 37 | fimagesize | 形象尺寸 | varchar | 100 |  | √ | ' ' | 形象尺寸 |
| 38 | ffinalqty | 终审数量 | numeric | 23 | 10 | √ | 0 | 终审数量 |
| 39 | ffinalamt | 终审金额 | numeric | 23 | 10 | √ | 0 | 终审金额 |
| 40 | fdisplaytype | 陈列类型 | bpchar | 1 |  | √ | ' ' | 陈列类型,枚举: A :端货 B :堆头 C :货架 |
| 41 | fdisplayarea | 陈列面积 | varchar | 100 |  | √ | ' ' | 陈列面积 |
| 42 | fcontractpoint | fcontractpoint | numeric | 23 | 10 | √ | 0 |  |
| 43 | foldshopid | foldshopid | int8 | 64 |  | √ | 0 |  |
| 44 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 45 | fentryaccountid | 账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 46 | fpromotion | 是否有促销员 | bpchar | 1 |  | √ | '0' | 是否有促销员 |
| 47 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 48 | foriginalqty | 初审数量 | numeric | 23 | 10 | √ | 0 | 初审数量 |
| 49 | frowparentexpenseid | 费用大类 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 50 | funrevieamount | 不达标扣减额 | numeric | 23 | 10 | √ | 0 | 不达标扣减额 |
| 51 | fentrywriteoffid | 费用行类型id | int8 | 64 |  | √ | 0 | [费用行类型 ocdbd_entryexpensetype](../ocmem_files/ocdbd_entryexpensetype.md) |
| 52 | frowexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 53 | fpromotiontheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 54 | fcostprice | fcostprice | numeric | 23 | 10 | √ | 0 |  |
| 55 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 56 | fverifiedqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 57 | factualsaleqty | factualsaleqty | numeric | 23 | 10 | √ | 0 |  |
| 58 | fentrychannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mcre_fseid |  | fsourceentryid |
| 2 | pk_ocmem_mc_reimentry |  | fentryid |
| 3 | idx_ocmem_mcre_itemid |  | fiteminfoid |
| 4 | idx_ocmem_mcre_ospid |  | foldshopid |
| 5 | idx_ocmem_mcre_fid |  | fid |
| 6 | idx_ocmem_mcre_fsid |  | fsourceid |

---

## 核销分录-分表 t_ocmem_mc_reimentry_p

- **表名称：** 核销分录-分表
- **表名：** t_ocmem_mc_reimentry_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocallinksettamt | 已关联兑付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联兑付金额（本位币） |
| 3 | flocalamount | 核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 核销金额（本位币） |
| 4 | flocalfinalamt | 终审金额（本位币） | numeric | 23 | 10 | √ | 0 | 终审金额（本位币） |
| 5 | fbudgetitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 6 | fbudgetchlclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 7 | flinkaccamount | 已累计兑付金额 | numeric | 23 | 10 | √ | 0 | 已累计兑付金额 |
| 8 | flocallinkaccamt | 已累计兑付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已累计兑付金额（本位币） |
| 9 | flocalamtunapproved | 未核准金额（本位币） | numeric | 23 | 10 | √ | 0 | 未核准金额（本位币） |
| 10 | flocalamtapply | 申请金额（本位币） | numeric | 23 | 10 | √ | 0 | 申请金额（本位币） |
| 11 | flocalamtapproved | 核准金额（本位币） | numeric | 23 | 10 | √ | 0 | 核准金额（本位币） |
| 12 | flinksettamount | 已关联兑付金额 | numeric | 23 | 10 | √ | 0 | 已关联兑付金额 |
| 13 | fbudgetitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | flocaloriginalamt | 初审金额（本位币） | numeric | 23 | 10 | √ | 0 | 初审金额（本位币） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mc_reimentry_p_fid |  | fid |
| 2 | pk_ocmem_mc_reimentry_p |  | fentryid |

---

## 关联子实体-子表 t_ocmem_mc_reimbur_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocmem_mc_reimbur_lk

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
| 1 | pk_ocmem_mc_reimbur_lk |  | fpkid |
| 2 | idx_ocmem_mc_reimbur_lk_fk |  | fid |

---

## 营销费用核销单-关联追踪表 t_ocmem_mc_reimbur_tc

- **表名称：** 营销费用核销单-关联追踪表
- **表名：** t_ocmem_mc_reimbur_tc

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
| 1 | idx_ocmem_mc_reimbur_tc_tbill |  | ftbillid |
| 2 | pk_ocmem_mc_reimbur_tc |  | fid |
| 3 | idx_ocmem_mc_reimbur_tc_tid |  | ftid |

---

## 营销费用核销单-主表 t_ocmem_mc_reimburse

- **表名称：** 营销费用核销单-主表
- **表名：** t_ocmem_mc_reimburse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目关联部门 bd_expitemreldept](../basedata_files/bd_expitemreldept.md) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | famounttotal | 核销金额合计 | numeric | 23 | 10 | √ | 0 | 核销金额合计 |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fagencyid | fagencyid | int8 | 64 |  | √ | 0 |  |
| 7 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | [活动类型 ocdbd_activitytype](../ocmem_files/ocdbd_activitytype.md) |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 11 | fmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 14 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 15 | ftoriginalamt | 初审金额合计 | numeric | 23 | 10 | √ | 0 | 初审金额合计 |
| 16 | fdeptid | 费用申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核不通过 E :审核通过 F :部分兑付 G :已完成 |
| 18 | fexcludetaxamt | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 19 | fpaymethodid | fpaymethodid | int8 | 64 |  | √ | 0 |  |
| 20 | freimburseuserid | 核销申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | ftotalamtapply | 申请金额合计 | numeric | 23 | 10 | √ | 0 | 申请金额合计 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | freasons | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 24 | fapplybillid | fapplybillid | int8 | 64 |  | √ | 0 |  |
| 25 | finvoicetype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: A :普通发票 B :专用发票 C :电子发票 |
| 26 | faccounttypeid | faccounttypeid | int8 | 64 |  | √ | 0 |  |
| 27 | ftotalamtinvoice | 发票总金额 | numeric | 23 | 10 | √ | 0 | 发票总金额 |
| 28 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | ' ' | 预算周期维度,枚举: A :按年 B :按月 |
| 31 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | ftotalamtunapproved | 核准金额合计 | numeric | 23 | 10 | √ | 0 | 核准金额合计 |
| 33 | factivityplanid | 营销活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 34 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 35 | ftfinalamt | 终审金额合计 | numeric | 23 | 10 | √ | 0 | 终审金额合计 |
| 36 | ftotallinksettamount | 已关联兑付金额 | numeric | 23 | 10 | √ | 0 | 已关联兑付金额 |
| 37 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 38 | flocaltoriginalamt | 初审金额合计（本位币） | numeric | 23 | 10 | √ | 0 | 初审金额合计（本位币） |
| 39 | ftotallinkaccamount | 已累计兑付金额 | numeric | 23 | 10 | √ | 0 | 已累计兑付金额 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | forderchannelid | 申请渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 43 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 44 | ftotalverifiedamount | 已使用核销金额 | numeric | 23 | 10 | √ | 0 | 已使用核销金额 |
| 45 | flocalttlinksettamt | 已关联兑付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联兑付金额（本位币） |
| 46 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | flocalttamtapply | 申请金额合计 （本位币） | numeric | 23 | 10 | √ | 0 | 申请金额合计 （本位币） |
| 48 | ftoriginalqty | 初审数量合计 | numeric | 23 | 10 | √ | 0 | 初审数量合计 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | flocalttlinkaccamt | 已累计兑付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已累计兑付金额（本位币） |
| 51 | fachierate | 达成率% | numeric | 23 | 10 | √ | 0 | 达成率% |
| 52 | fwarzoneid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | ftfinalqty | 终审数量合计 | numeric | 23 | 10 | √ | 0 | 终审数量合计 |
| 54 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 55 | fparentexpenseid | fparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 56 | flocaltfinalamt | 终审金额合计（本位币） | numeric | 23 | 10 | √ | 0 | 终审金额合计（本位币） |
| 57 | fheadwriteoff | fheadwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 58 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 59 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 60 | fsourcebillid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 61 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 62 | flocalttamount | 核销金额合计（本位币） | numeric | 23 | 10 | √ | 0 | 核销金额合计（本位币） |
| 63 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 64 | freimburseway | freimburseway | bpchar | 1 |  | √ | 'A' |  |
| 65 | flocalttamtapproved | 核准金额合计（本位币） | numeric | 23 | 10 | √ | 0 | 核准金额合计（本位币） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mcr_fbilldate |  | fbilldate |
| 2 | idx_ocmem_mcr_fsoid |  | fsourcebillid |
| 3 | pk_ocmem_mc_reimburse |  | fid |
| 4 | idx_ocmem_mcr_faid |  | fapplybillid |
| 5 | idx_ocmem_mcr_fbno |  | fbillno |

---

## 收款信息-子表 t_ocmem_mc_receentry

- **表名称：** 收款信息-子表
- **表名：** t_ocmem_mc_receentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaycustomerid | 客户名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 4 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 5 | fpaycurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freceivableamt | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 8 | fpaytype | 收款人类型 | bpchar | 1 |  | √ | ' ' | 收款人类型,枚举: A :客户 B :个人 |
| 9 | fpayrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | freceivableamtlocal | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |
| 11 | fpayeraccount | 银行账户 | varchar | 100 |  | √ | ' ' | 银行账户 |
| 12 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fsettlementtypeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mc_receentry_fid |  | fid |
| 2 | pk_ocmem_mc_receentry |  | fentryid |
