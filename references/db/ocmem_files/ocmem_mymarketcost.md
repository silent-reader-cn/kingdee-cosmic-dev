# 我的费用申请-ocmem_mymarketcost

## 执行人-多选基础资料表 t_ocmem_executor

- **表名称：** 执行人-多选基础资料表
- **表名：** t_ocmem_executor

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
| 1 | idx_ocmem_executor_fbid |  | fentryid,fbasedataid |
| 2 | pk_ocmem_executor |  | fpkid |

---

## 我的费用申请-反写记录表 t_ocmem_mcost_apply_wb

- **表名称：** 我的费用申请-反写记录表
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

## 我的费用申请-主表 t_ocmem_mcost_apply

- **表名称：** 我的费用申请-主表
- **表名：** t_ocmem_mcost_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseprojectid | fexpenseprojectid | int8 | 64 |  | √ | 0 |  |
| 3 | fsumlinklocalborwamount | 已关联借款金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联借款金额（本位币） |
| 4 | ftotalamount | 申请总金额 | numeric | 23 | 10 | √ | 0 | 申请总金额 |
| 5 | fsumlinkborwamount | 已关联借款金额 | numeric | 23 | 10 | √ | 0 | 已关联借款金额 |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fagencyid | fagencyid | int8 | 64 |  | √ | 0 |  |
| 8 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | [活动类型 ocdbd_activitytype](../ocmem_files/ocdbd_activitytype.md) |
| 9 | fsupervisestatus | 督查状态 | bpchar | 1 |  | √ | 'A' | 督查状态,枚举: A :未督查 B :已督查 C :督查中 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsumaccreimamont | 已累计报销 | numeric | 23 | 10 | √ | 0 | 已累计报销 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fenddate | 最晚结束日期 | timestamp | 0 |  |  | null | 最晚结束日期 |
| 14 | fsumlalinkamtapproved | 已关联核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联核销金额（本位币） |
| 15 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 16 | fmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 18 | fsumlinkreimamont | 已关联报销 | numeric | 23 | 10 | √ | 0 | 已关联报销 |
| 19 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 20 | flocaltotalamtunapproved | 未核准金额合计（本位币） | numeric | 23 | 10 | √ | 0 | 未核准金额合计（本位币） |
| 21 | fdeptid | 费用申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :部分核销 G :已关闭 |
| 23 | fpaymenthodid | fpaymenthodid | int8 | 64 |  | √ | 0 |  |
| 24 | fpayuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | freason | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 27 | fbalancenumber | fbalancenumber | varchar | 100 |  | √ | ' ' |  |
| 28 | ftotalrefundamount | ftotalrefundamount | numeric | 23 | 10 | √ | 0 |  |
| 29 | flocalsumamount | 申请总金额 （本位币） | numeric | 23 | 10 | √ | 0 | 申请总金额 （本位币） |
| 30 | ftotalamtapproved | 已核销金额合计 | numeric | 23 | 10 | √ | 0 | 已核销金额合计 |
| 31 | faccounttypeid | faccounttypeid | int8 | 64 |  | √ | 0 |  |
| 32 | flocalsumlinkreimamt | 已关联报销（本位币） | numeric | 23 | 10 | √ | 0 | 已关联报销（本位币） |
| 33 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fbudget | fbudget | numeric | 23 | 10 | √ | 0 |  |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | ' ' | 预算周期维度,枚举: A :按年 B :按月 |
| 37 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | '2087111909521252352' | 单据类型 bos_billtype |
| 39 | ftotalamtunapproved | 未核准金额合计 | numeric | 23 | 10 | √ | 0 | 未核准金额合计 |
| 40 | factivityplanid | 营销活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 41 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 42 | flocalsumaccreimamt | 已累计报销（本位币） | numeric | 23 | 10 | √ | 0 | 已累计报销（本位币） |
| 43 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fsumlinkamtapproved | 已关联核销金额 | numeric | 23 | 10 | √ | 0 | 已关联核销金额 |
| 46 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | forderchannelid | 申请渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 48 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 49 | fshowreimbursebtn | 是否显示报销 | bpchar | 1 |  | √ | '0' | 是否显示报销,枚举: 1 :是 0 :否 |
| 50 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 52 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fsumaccborwamount | 已累计借款金额 | numeric | 23 | 10 | √ | 0 | 已累计借款金额 |
| 54 | fwarzoneid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fbegindate | 最早开始日期 | timestamp | 0 |  |  | null | 最早开始日期 |
| 57 | fparentexpenseid | fparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 58 | fheadwriteoff | fheadwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 59 | ffreezestatus | ffreezestatus | bpchar | 1 |  | √ | 'E' |  |
| 60 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 61 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未执行 B :执行中 C :已执行 |
| 62 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 63 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 64 | fsumacclocalborwamount | 已累计借款金额（本位币） | numeric | 23 | 10 | √ | 0 | 已累计借款金额（本位币） |
| 65 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 66 | freimburseway | freimburseway | bpchar | 1 |  | √ | 'A' |  |
| 67 | fclosereasonid | 关闭原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 68 | flocalttamtapproved | 已核销金额合计（本位币） | numeric | 23 | 10 | √ | 0 | 已核销金额合计（本位币） |

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

---

## 单据体-分表 t_ocmem_mcost_applye_p

- **表名称：** 单据体-分表
- **表名：** t_ocmem_mcost_applye_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryexecutestatus | 行执行状态 | bpchar | 1 |  | √ | ' ' | 行执行状态,枚举: A :未执行 B :已执行 C :执行中 D :无需执行 |
| 3 | fbudgetitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 4 | fexecuteresult | 行执行结果 | bpchar | 1 |  | √ | ' ' | 行执行结果,枚举: A :非常好 B :良好 C :合格 D :不合格 |
| 5 | fbudgetchlclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 6 | flocalamtunapproved | 可用金额（本位币） | numeric | 23 | 10 | √ | 0 | 可用金额（本位币） |
| 7 | flocalamtapproved | 已核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已核销金额（本位币） |
| 8 | flocalaccreimamont | 已累计报销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已累计报销金额（本位币） |
| 9 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 10 | fbudgetitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 11 | faccoutqty | 已累计出库基本数量 | numeric | 23 | 10 | √ | 0 | 已累计出库基本数量 |
| 12 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | [预算余额表 ocdbd_budgetbalance](../ocmem_files/ocdbd_budgetbalance.md) |
| 13 | ftargetbudget | 目标预算可用余额 | numeric | 23 | 10 | √ | 0 | 目标预算可用余额 |
| 14 | flocaladvicereduceamt | 建议核减金额（本位币） | numeric | 23 | 10 | √ | 0 | 建议核减金额（本位币） |
| 15 | flocalamount | 申请金额（本位币） | numeric | 23 | 10 | √ | 0 | 申请金额（本位币） |
| 16 | flocallinkreimamont | 已关联报销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联报销金额（本位币） |
| 17 | fparentexpenseid | 费用大类 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 18 | flinkoutbaseqty | 已关联出库基本数量 | numeric | 23 | 10 | √ | 0 | 已关联出库基本数量 |
| 19 | flinkoutqty | 已关联出库数量 | numeric | 23 | 10 | √ | 0 | 已关联出库数量 |
| 20 | fentrysupervisestatus | 行督查状态 | bpchar | 1 |  | √ | 'A' | 行督查状态,枚举: A :未督查 B :已督查 C :督查中 D :无需督查 |
| 21 | flinklocalamtapproved | 已关联核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联核销金额（本位币） |
| 22 | faccreimamont | 已累计报销金额 | numeric | 23 | 10 | √ | 0 | 已累计报销金额 |
| 23 | flinkreimamont | 已关联报销金额 | numeric | 23 | 10 | √ | 0 | 已关联报销金额 |
| 24 | fsuperviseresult | 行督查结果 | bpchar | 1 |  | √ | ' ' | 行督查结果,枚举: A :非常好 B :良好 C :合格 D :不合格 |
| 25 | fadvicereduceamount | 建议核减金额 | numeric | 23 | 10 | √ | 0 | 建议核减金额 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fbudget | 预算可用余额 | numeric | 23 | 10 | √ | 0 | 预算可用余额 |

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
| 7 | fmeasurementunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fiteminfoid | 产品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 9 | fshopid | 门店名称 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | famtunapproved | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 11 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | ffeecashtypeid | 费用兑付方式 | int8 | 64 |  | √ | 0 | [费用兑付方式 ocdbd_feecashtype](../ocmem_files/ocdbd_feecashtype.md) |
| 14 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 15 | fpromotionaddress | 促销地点 | varchar | 100 |  | √ | ' ' | 促销地点 |
| 16 | fentryexpensetypeid | 行类型 | int8 | 64 |  | √ | 0 | [费用行类型分录 ocdbd_expensetype_entry](../ocmem_files/ocdbd_expensetype_entry.md) |
| 17 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 18 | fshoptypeid | 门店类型 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 19 | fcostamount | fcostamount | numeric | 23 | 10 | √ | 0 |  |
| 20 | fbaseverifiedqty | 基本核准数量 | numeric | 23 | 10 | √ | 0 | 基本核准数量 |
| 21 | faccborwamount | 已累计借款金额 | numeric | 23 | 10 | √ | 0 | 已累计借款金额 |
| 22 | fplansaleqty | fplansaleqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | flossrate | flossrate | numeric | 23 | 10 | √ | 0 |  |
| 24 | fentrytype | fentrytype | bpchar | 1 |  | √ | ' ' |  |
| 25 | fproductprice | 活动产品价格（元） | numeric | 23 | 10 | √ | 0 | 活动产品价格（元） |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fentryenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 28 | ftotalqty | 累计已核销数量 | numeric | 23 | 10 | √ | 0 | 累计已核销数量 |
| 29 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 30 | frefundamount | frefundamount | numeric | 23 | 10 | √ | 0 |  |
| 31 | famount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 32 | foriginalamt | foriginalamt | numeric | 23 | 10 | √ | 0 |  |
| 33 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 34 | fimagesize | 形象尺寸 | varchar | 100 |  | √ | ' ' | 形象尺寸 |
| 35 | ffinalqty | ffinalqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | fentrybegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 37 | ffinalamt | ffinalamt | numeric | 23 | 10 | √ | 0 |  |
| 38 | fdisplaytype | 陈列类型 | bpchar | 1 |  | √ | 'A' | 陈列类型,枚举: A :端货 B :堆头 C :货架 |
| 39 | fdisplayarea | 陈列面积（如：4m²*5m²） | varchar | 100 |  | √ | ' ' | 陈列面积（如：4m²*5m²） |
| 40 | fjoinqty | 已关联核销数量 | numeric | 23 | 10 | √ | 0 | 已关联核销数量 |
| 41 | flinkamtapproved | 已关联核销金额 | numeric | 23 | 10 | √ | 0 | 已关联核销金额 |
| 42 | fcontractpoint | fcontractpoint | numeric | 23 | 10 | √ | 0 |  |
| 43 | foldshopid | foldshopid | int8 | 64 |  | √ | 0 |  |
| 44 | fentryaccountid | 账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 45 | fpromotion | 是否有促销员 | bpchar | 1 |  | √ | '0' | 是否有促销员 |
| 46 | fisexecuted | 是否已执行 | bpchar | 1 |  | √ | '0' | 是否已执行 |
| 47 | flinklocalborwamount | 已关联借款金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联借款金额（本位币） |
| 48 | facclocalborwamount | 已累计借款金额（本位币） | numeric | 23 | 10 | √ | 0 | 已累计借款金额（本位币） |
| 49 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 50 | foriginalqty | foriginalqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | fentrywriteoffid | 费用行类型id | int8 | 64 |  | √ | 0 | [费用行类型 ocdbd_entryexpensetype](../ocmem_files/ocdbd_entryexpensetype.md) |
| 52 | fpromotiontheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 53 | fcostprice | fcostprice | numeric | 23 | 10 | √ | 0 |  |
| 54 | fverifiedqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 55 | factualsaleqty | factualsaleqty | numeric | 23 | 10 | √ | 0 |  |
| 56 | fentrychannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 57 | flinkborwamount | 已关联借款金额 | numeric | 23 | 10 | √ | 0 | 已关联借款金额 |

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

## 我的费用申请-关联追踪表 t_ocmem_mcost_apply_tc

- **表名称：** 我的费用申请-关联追踪表
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
