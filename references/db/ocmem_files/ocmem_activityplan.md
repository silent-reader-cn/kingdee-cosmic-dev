# 营销活动方案-ocmem_activityplan

## 营销活动方案-主表 t_ocmem_activityplan

- **表名称：** 营销活动方案-主表
- **表名：** t_ocmem_activityplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumsaleamount | 预计销售总额 | numeric | 23 | 10 | √ | 0 | 预计销售总额 |
| 3 | factivityuserid | 活动负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbuyuserqty | 购买人数 | numeric | 23 | 10 | √ | 0 | 购买人数 |
| 5 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | [活动类型 ocdbd_activitytype](../ocmem_files/ocdbd_activitytype.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | fstartactivitydate | 预计活动日期.开始 | timestamp | 0 |  |  | null | 预计活动日期.开始 |
| 9 | fplandate | 策划日期 | timestamp | 0 |  |  | null | 策划日期 |
| 10 | fuserqty | 参加人数 | numeric | 23 | 10 | √ | 0 | 参加人数 |
| 11 | fimplementation_tag | 执行状况_详情 | text | 0 |  |  | null | 执行状况_详情 |
| 12 | flocalapproveamount | 核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 核销金额（本位币） |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | flocalaccamount | 关联金额（本位币） | numeric | 23 | 10 | √ | 0 | 关联金额（本位币） |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | flocaltotalapplyamount | 申请金额（本位币） | numeric | 23 | 10 | √ | 0 | 申请金额（本位币） |
| 17 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fplanorgid | 策划部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | factivitystatus | 活动状态 | bpchar | 1 |  | √ | ' ' | 活动状态,枚举: A :计划 B :已完成 C :进行中 D :已取消 E :已结案 |
| 21 | fsettorgid | 主办公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | ftotalapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 24 | fsumfeeamount | 预计费用总额 | numeric | 23 | 10 | √ | 0 | 预计费用总额 |
| 25 | fendactivitydate | 预计活动日期.结束 | timestamp | 0 |  |  | null | 预计活动日期.结束 |
| 26 | fapproveamount | 核销金额 | numeric | 23 | 10 | √ | 0 | 核销金额 |
| 27 | factivityresultid | 活动结果 | int8 | 64 |  | √ | 0 | 活动结果记录单 ocmem_activityresult |
| 28 | fplantarget | 方案目标 | varchar | 510 |  | √ | ' ' | 方案目标 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | flocalsumfeeamount | 预计费用总额（本位币） | numeric | 23 | 10 | √ | 0 | 预计费用总额（本位币） |
| 32 | fplandescription | 方案简述 | varchar | 510 |  | √ | ' ' | 方案简述 |
| 33 | ffeesalerate | 预计费效比% | numeric | 23 | 10 | √ | 0 | 预计费效比% |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fbuyamount | 购买金额 | numeric | 23 | 10 | √ | 0 | 购买金额 |
| 36 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fimplementation | 执行状况 | text | 0 |  |  | null | 执行状况 |
| 38 | fresultstatus | 活动结果状态 | bpchar | 1 |  | √ | 'A' | 活动结果状态,枚举: A :暂存 B :提交 C :审核 |
| 39 | flocalsumsaleamount | 预计销售总额（本位币） | numeric | 23 | 10 | √ | 0 | 预计销售总额（本位币） |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fpicture6 | 照片6 | varchar | 255 |  | √ | ' ' | 照片6 |
| 42 | fpicture5 | 照片5 | varchar | 255 |  | √ | ' ' | 照片5 |
| 43 | fpicture4 | 照片4 | varchar | 255 |  | √ | ' ' | 照片4 |
| 44 | fpicture3 | 照片3 | varchar | 255 |  | √ | ' ' | 照片3 |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fpicture2 | 照片2 | varchar | 255 |  | √ | ' ' | 照片2 |
| 47 | fpicture1 | 照片1 | varchar | 255 |  | √ | ' ' | 照片1 |
| 48 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 51 | flocalbuyamount | 购买金额（本位币） | numeric | 23 | 10 | √ | 0 | 购买金额（本位币） |
| 52 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 53 | frelactivityid | 关联活动 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 54 | faccamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 55 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_activityplan |  | fid |
| 2 | idx_ocmem_activityplan_billno |  | fbillno |

---

## 活动产品方案-子表 t_ocmem_ap_itementry

- **表名称：** 活动产品方案-子表
- **表名：** t_ocmem_ap_itementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpromoteprice | 促销价格 | numeric | 23 | 10 | √ | 0 | 促销价格 |
| 3 | frebatecondition | 返利条件 | varchar | 510 |  | √ | ' ' | 返利条件 |
| 4 | fplansaleamount | 预计销售金额 | numeric | 23 | 10 | √ | 0 | 预计销售金额 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | flocalplanrebateamount | 预计返利金额（本位币） | numeric | 23 | 10 | √ | 0 | 预计返利金额（本位币） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fplanrebateamount | 预计返利金额 | numeric | 23 | 10 | √ | 0 | 预计返利金额 |
| 9 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 10 | flocalplansaleamount | 预计销售金额（本位币） | numeric | 23 | 10 | √ | 0 | 预计销售金额（本位币） |
| 11 | fitemremark | 产品行备注 | varchar | 510 |  | √ | ' ' | 产品行备注 |
| 12 | fpromotecondition | 促销条件 | varchar | 510 |  | √ | ' ' | 促销条件 |
| 13 | fplansaleqty | 预计销售数量 | numeric | 23 | 10 | √ | 0 | 预计销售数量 |
| 14 | fitembrandid | 品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 15 | fitemgroupid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 16 | frebatetype | 返利方案 | bpchar | 1 |  | √ | ' ' | 返利方案,枚举: A :单位返利 B :返点返利 C :其他 |
| 17 | fnormalprice | 正常价格 | numeric | 23 | 10 | √ | 0 | 正常价格 |
| 18 | fpromotestrategy | 促销策略 | varchar | 510 |  | √ | ' ' | 促销策略 |
| 19 | fpromotiontype | 促销方案 | bpchar | 1 |  | √ | ' ' | 促销方案,枚举: A :折扣 B :满减 C :买赠 D :降价 E :其他 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | frebatestrategy | 返利策略 | varchar | 510 |  | √ | ' ' | 返利策略 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_ap_itementry |  | fentryid |
| 2 | idx_ocmem_ap_itementry_fid |  | fid |

---

## 活动人员列表-子表 t_ocmem_actplanuserentry

- **表名称：** 活动人员列表-子表
- **表名：** t_ocmem_actplanuserentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissignin | 已签到 | bpchar | 1 |  | √ | '0' | 已签到 |
| 3 | fsignintime | 签到时间 | timestamp | 0 |  |  | null | 签到时间 |
| 4 | fsigninnumber | 人数 | int4 | 32 |  | √ | 0 | 人数 |
| 5 | fsignusername | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftelephone | 手机号 | varchar | 80 |  | √ | ' ' | 手机号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actplanuserentryfid |  | fid |
| 2 | pk_ocmem_actplanuserentry |  | fentryid |

---

## 活动客户方案-子表 t_ocmem_ap_chlentry

- **表名称：** 活动客户方案-子表
- **表名：** t_ocmem_ap_chlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchannelgradeid | 客户等级 | int8 | 64 |  | √ | 0 | [渠道等级 ocdbd_channel_grade](../ocdbd_files/ocdbd_channel_grade.md) |
| 3 | fchannelremark | 客户行备注 | varchar | 510 |  | √ | ' ' | 客户行备注 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fchannelid | 客户编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 6 | fchannelclassesid | 客户分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_ap_chlentry |  | fentryid |
| 2 | idx_ocmem_ap_chlentry_fid |  | fid |

---

## 部门承担预算-子表 t_ocmem_ap_orgentry

- **表名称：** 部门承担预算-子表
- **表名：** t_ocmem_ap_orgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocalbudgetamount | 预算金额（本位币） | numeric | 23 | 10 | √ | 0 | 预算金额（本位币） |
| 3 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 4 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 5 | forgrowremark | 部门行备注 | varchar | 510 |  | √ | ' ' | 部门行备注 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbudgetamount | 预算金额 | numeric | 23 | 10 | √ | 0 | 预算金额 |
| 8 | fexpensesource | 费用预算来源 | bpchar | 1 |  | √ | ' ' | 费用预算来源,枚举: A :常规预算 B :专项预算申请 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpayorgid | 承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_ap_orgentry_fid |  | fid |
| 2 | pk_ocmem_ap_orgentry |  | fentryid |

---

## 活动关注物-多选基础资料表 t_ocmem_actfocusobj

- **表名称：** 活动关注物-多选基础资料表
- **表名：** t_ocmem_actfocusobj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [活动关注物 ocmem_activity_focus](../ocmem_files/ocmem_activity_focus.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_actfocusobj |  | fpkid |
| 2 | idx_ocmem_actfocusobj |  | fid,fbasedataid |

---

## 活动费用方案-子表 t_ocmem_ap_planentry

- **表名称：** 活动费用方案-子表
- **表名：** t_ocmem_ap_planentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocallinkamount | 已关联金额（本位币） | numeric | 23 | 10 | √ | 0 | 已关联金额（本位币） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 5 | flinkqty | 已关联数量 | numeric | 23 | 10 | √ | 0 | 已关联数量 |
| 6 | ffeeentryremark | 费用行备注 | varchar | 510 |  | √ | ' ' | 费用行备注 |
| 7 | flocalcompanyamount | 公司承担费用（本位币） | numeric | 23 | 10 | √ | 0 | 公司承担费用（本位币） |
| 8 | fapporveamount | 已核销金额 | numeric | 23 | 10 | √ | 0 | 已核销金额 |
| 9 | ffeeamount | 费用金额 | numeric | 23 | 10 | √ | 0 | 费用金额 |
| 10 | flinkamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 11 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | ffeeexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 13 | flocalapplyamount | 已申请金额（本位币） | numeric | 23 | 10 | √ | 0 | 已申请金额（本位币） |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fcompanyamount | 公司承担费用 | numeric | 23 | 10 | √ | 0 | 公司承担费用 |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fentrywriteoffid | 费用行类型id | int8 | 64 |  | √ | 0 | [费用行类型 ocdbd_entryexpensetype](../ocmem_files/ocdbd_entryexpensetype.md) |
| 18 | flocaltaxfeeamount | 费用金额（本位币） | numeric | 23 | 10 | √ | 0 | 费用金额（本位币） |
| 19 | fapplyamount | 已申请金额 | numeric | 23 | 10 | √ | 0 | 已申请金额 |
| 20 | flocalapporveamount | 已核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已核销金额（本位币） |
| 21 | fitemid | 产品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 22 | fcompanyrate | 公司承担（%） | numeric | 23 | 10 | √ | 0 | 公司承担（%） |
| 23 | fexpenserowtypeid | 活动行类型 | int8 | 64 |  | √ | 0 | [费用行类型分录 ocdbd_expensetype_entry](../ocmem_files/ocdbd_expensetype_entry.md) |
| 24 | fapplyqty | 已申请数量 | numeric | 23 | 10 | √ | 0 | 已申请数量 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_ap_planentry |  | fentryid |
| 2 | idx_ocmem_ap_planentry_fid |  | fid |
