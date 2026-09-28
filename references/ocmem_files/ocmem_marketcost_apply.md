# 营销费用申请单-ocmem_marketcost_apply

## 单据体-分表 t_ocmem_mcost_applye_p

- **表名称：** 单据体-分表
- **表名：** t_ocmem_mcost_applye_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | 预算余额表 ocdbd_budgetbalance |
| 3 | flinkoutqty | 已关联出库数量 | numeric | 23 | 10 | √ | 0 | 已关联出库数量 |
| 4 | faccreimamont | 已累计人人报销金额 | numeric | 23 | 10 | √ | 0 | 已累计人人报销金额 |
| 5 | flinkreimamont | 已关联人人报销金额 | numeric | 23 | 10 | √ | 0 | 已关联人人报销金额 |
| 6 | fbudgetitemid | 预算产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 7 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 8 | fparentexpenseid | 费用大类 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 9 | fbudgetitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 10 | faccoutqty | 已累计出库数量 | numeric | 23 | 10 | √ | 0 | 已累计出库数量 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fbudget | 预算可用余额 | numeric | 23 | 10 | √ | 0 | 预算可用余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcost_applye_p |  | fentryid |
| 2 | idx_ocmem_mcostapplyep_fid |  | fid |

---

## 单据体-子表 t_ocmem_mcost_applye

- **表名称：** 单据体-子表
- **表名：** t_ocmem_mcost_applye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrywriteoffname | 核销方式 | varchar | 80 |  | √ | ' ' | 核销方式 |
| 3 | freachrate | freachrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | famtapproved | 已核销金额 | numeric | 23 | 10 | √ | 0 | 已核销金额 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fiteminfoid | 产品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 8 | fshopid | 门店名称 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 9 | famtunapproved | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 10 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | ffeecashtypeid | 费用兑付方式 | int8 | 64 |  | √ | 0 | 费用兑付方式 ocdbd_feecashtype |
| 13 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 14 | fpromotionaddress | 促销地点 | varchar | 100 |  | √ | ' ' | 促销地点 |
| 15 | fentryexpensetypeid | 行类型 | int8 | 64 |  | √ | 0 | 费用行类型分录 ocdbd_expensetype_entry |
| 16 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 17 | fshoptypeid | 门店类型 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 18 | fcostamount | fcostamount | numeric | 23 | 10 | √ | 0 |  |
| 19 | fplansaleqty | fplansaleqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | flossrate | flossrate | numeric | 23 | 10 | √ | 0 |  |
| 21 | fentrytype | fentrytype | bpchar | 1 |  | √ | ' ' |  |
| 22 | fproductprice | 活动产品价格（元） | numeric | 23 | 10 | √ | 0 | 活动产品价格（元） |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fentryenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 25 | ftotalqty | 累计已核销数量 | numeric | 23 | 10 | √ | 0 | 累计已核销数量 |
| 26 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 27 | frefundamount | frefundamount | numeric | 23 | 10 | √ | 0 |  |
| 28 | famount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 29 | foriginalamt | foriginalamt | numeric | 23 | 10 | √ | 0 |  |
| 30 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 31 | fimagesize | 形象尺寸 | varchar | 100 |  | √ | ' ' | 形象尺寸 |
| 32 | ffinalqty | ffinalqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fentrybegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 34 | ffinalamt | ffinalamt | numeric | 23 | 10 | √ | 0 |  |
| 35 | fdisplaytype | 陈列类型 | bpchar | 1 |  | √ | 'A' | 陈列类型,枚举: A :端货 B :堆头 C :货架 |
| 36 | fdisplayarea | 陈列面积（如：4m²*5m²） | varchar | 100 |  | √ | ' ' | 陈列面积（如：4m²*5m²） |
| 37 | fjoinqty | 已关联核销单数量 | numeric | 23 | 10 | √ | 0 | 已关联核销单数量 |
| 38 | fcontractpoint | fcontractpoint | numeric | 23 | 10 | √ | 0 |  |
| 39 | foldshopid | foldshopid | int8 | 64 |  | √ | 0 |  |
| 40 | fentryaccountid | 账户类型 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 41 | fpromotion | 是否有促销员 | bpchar | 1 |  | √ | '0' | 是否有促销员 |
| 42 | fisexecuted | 是否已执行 | bpchar | 1 |  | √ | '0' | 是否已执行 |
| 43 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 44 | foriginalqty | foriginalqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fentrywriteoffid | 费用行类型id | int8 | 64 |  | √ | 0 | 费用行类型 ocdbd_entryexpensetype |
| 46 | fpromotiontheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 47 | fcostprice | fcostprice | numeric | 23 | 10 | √ | 0 |  |
| 48 | fverifiedqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 49 | factualsaleqty | factualsaleqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fentrychannelid | 预算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcost_applye |  | fentryid |
| 2 | idx_ocmem_mcae_fid |  | fid |
| 3 | idx_ocmem_mcae_item |  | fiteminfoid |
| 4 | idx_ocmem_mcae_fshop |  | fshopid |
| 5 | idx_ocmem_mcae_oshop |  | foldshopid |

---

## 执行人-多选基础资料表 t_ocmem_executor

- **表名称：** 执行人-多选基础资料表
- **表名：** t_ocmem_executor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_executor_fbid |  | fentryid,fbasedataid |
| 2 | pk_ocmem_executor |  | fpkid |

---

## 营销费用申请单-关联追踪表 t_ocmem_mcost_apply_tc

- **表名称：** 营销费用申请单-关联追踪表
- **表名：** t_ocmem_mcost_apply_tc

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
| 1 | idx_ocmem_mcost_apply_tc_tid |  | ftid |
| 2 | idx_ocmem_mcost_apply_tc_tbill |  | ftbillid |
| 3 | pk_ocmem_mcost_apply_tc |  | fid |

---

## 关联子实体-子表 t_ocmem_mcost_applye_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocmem_mcost_applye_lk

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
| 1 | pk_ocmem_mcost_applye_lk |  | fpkid |
| 2 | idx_ocmem_mcost_applye_lk_fk |  | fentryid |

---

## 营销费用申请单-反写记录表 t_ocmem_mcost_apply_wb

- **表名称：** 营销费用申请单-反写记录表
- **表名：** t_ocmem_mcost_apply_wb

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
| 1 | pk_ocmem_mcost_apply_wb |  | fentryid |
| 2 | idx_ocmem_mcost_apply_wb_fk |  | fid |

---

## 营销费用申请单-主表 t_ocmem_mcost_apply

- **表名称：** 营销费用申请单-主表
- **表名：** t_ocmem_mcost_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseprojectid | fexpenseprojectid | int8 | 64 |  | √ | 0 |  |
| 3 | ftotalamtunapproved | 未核准金额合计 | numeric | 23 | 10 | √ | 0 | 未核准金额合计 |
| 4 | ftotalamount | 申请总金额 | numeric | 23 | 10 | √ | 0 | 申请总金额 |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fagencyid | fagencyid | int8 | 64 |  | √ | 0 |  |
| 7 | factivityplanid | 营销活动方案 | int8 | 64 |  | √ | 0 | 费用活动方案 ocmem_activityplan_f7 |
| 8 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | 活动类型 ocdbd_activitytype |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 12 | fenddate | 最晚结束日期 | timestamp | 0 |  |  | null | 最晚结束日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | forderchannelid | 申请渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 18 | fmonthid | 预算月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 19 | fshowreimbursebtn | 是否显示报销 | bpchar | 1 |  | √ | '0' | 是否显示报销,枚举: 1 :是 0 :否 |
| 20 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 22 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fdeptid | 费用申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fwarzoneid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :部分核销 G :已关闭 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fbegindate | 最早开始日期 | timestamp | 0 |  |  | null | 最早开始日期 |
| 29 | fparentexpenseid | fparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 30 | fpaymenthodid | fpaymenthodid | int8 | 64 |  | √ | 0 |  |
| 31 | fpayuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | freason | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 34 | fheadwriteoff | fheadwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 35 | ffreezestatus | ffreezestatus | bpchar | 1 |  | √ | 'E' |  |
| 36 | fbalancenumber | fbalancenumber | varchar | 100 |  | √ | ' ' |  |
| 37 | ftotalrefundamount | ftotalrefundamount | numeric | 23 | 10 | √ | 0 |  |
| 38 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未执行 B :执行中 C :已执行 |
| 39 | ftotalamtapproved | 已核销金额合计 | numeric | 23 | 10 | √ | 0 | 已核销金额合计 |
| 40 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 41 | faccounttypeid | faccounttypeid | int8 | 64 |  | √ | 0 |  |
| 42 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | fbudget | fbudget | numeric | 23 | 10 | √ | 0 |  |
| 45 | freimburseway | freimburseway | bpchar | 1 |  | √ | 'A' |  |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | ' ' | 预算周期维度,枚举: A :按年 B :按月 |
| 48 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcost_apply |  | fid |
| 2 | idx_ocmem_mcost_fcust |  | forderchannelid |
| 3 | idx_ocmem_mcost_fbilldate |  | fbilldate |
| 4 | idx_ocmem_mcost_fdept |  | fdeptid |
| 5 | idx_ocmem_mcost_fbno |  | fbillno |
