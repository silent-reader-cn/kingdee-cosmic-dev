# 营销活动方案-ocmem_activityplan

## 活动客户方案-子表 t_ocmem_ap_chlentry

- **表名称：** 活动客户方案-子表
- **表名：** t_ocmem_ap_chlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchannelgradeid | 客户等级 | int8 | 64 |  | √ | 0 | 渠道等级 ocdbd_channel_grade |
| 3 | fchannelremark | 客户行备注 | varchar | 510 |  | √ | ' ' | 客户行备注 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fchannelid | 客户编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 6 | fchannelclassesid | 客户分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
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
| 2 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 3 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 4 | forgrowremark | 部门行备注 | varchar | 510 |  | √ | ' ' | 部门行备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbudgetamount | 预算金额 | numeric | 23 | 10 | √ | 0 | 预算金额 |
| 7 | fexpensesource | 费用预算来源 | bpchar | 1 |  | √ | ' ' | 费用预算来源,枚举: A :常规预算 B :专项预算申请 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpayorgid | 承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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

## 营销活动方案-主表 t_ocmem_activityplan

- **表名称：** 营销活动方案-主表
- **表名：** t_ocmem_activityplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumsaleamount | 预计销售总额 | numeric | 23 | 10 | √ | 0 | 预计销售总额 |
| 3 | factivityuserid | 活动负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbuyuserqty | 购买人数 | numeric | 23 | 10 | √ | 0 | 购买人数 |
| 5 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | 活动类型 ocdbd_activitytype |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fplandescription | 方案简述 | varchar | 510 |  | √ | ' ' | 方案简述 |
| 8 | fstartactivitydate | 预计活动日期.开始 | timestamp | 0 |  |  | null | 预计活动日期.开始 |
| 9 | ffeesalerate | 预计费效比% | numeric | 23 | 10 | √ | 0 | 预计费效比% |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbuyamount | 购买金额 | numeric | 23 | 10 | √ | 0 | 购买金额 |
| 12 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fplandate | 策划日期 | timestamp | 0 |  |  | null | 策划日期 |
| 14 | fuserqty | 参加人数 | numeric | 23 | 10 | √ | 0 | 参加人数 |
| 15 | fimplementation_tag | 执行状况_详情 | text | 0 |  |  | null | 执行状况_详情 |
| 16 | fimplementation | 执行状况 | text | 0 |  |  | null | 执行状况 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fpicture6 | 照片6 | varchar | 255 |  | √ | ' ' | 照片6 |
| 21 | fpicture5 | 照片5 | varchar | 255 |  | √ | ' ' | 照片5 |
| 22 | fpicture4 | 照片4 | varchar | 255 |  | √ | ' ' | 照片4 |
| 23 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fpicture3 | 照片3 | varchar | 255 |  | √ | ' ' | 照片3 |
| 25 | fplanorgid | 策划部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fpicture2 | 照片2 | varchar | 255 |  | √ | ' ' | 照片2 |
| 28 | factivitystatus | 活动状态 | bpchar | 1 |  | √ | ' ' | 活动状态,枚举: A :计划 B :已完成 C :进行中 D :已取消 E :已结案 |
| 29 | fpicture1 | 照片1 | varchar | 255 |  | √ | ' ' | 照片1 |
| 30 | fsettorgid | 主办公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | ftotalapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 35 | fsumfeeamount | 预计费用总额 | numeric | 23 | 10 | √ | 0 | 预计费用总额 |
| 36 | fendactivitydate | 预计活动日期.结束 | timestamp | 0 |  |  | null | 预计活动日期.结束 |
| 37 | fapproveamount | 核销金额 | numeric | 23 | 10 | √ | 0 | 核销金额 |
| 38 | faccamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 39 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | fplantarget | 方案目标 | varchar | 510 |  | √ | ' ' | 方案目标 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fplanrebateamount | 预计返利金额 | numeric | 23 | 10 | √ | 0 | 预计返利金额 |
| 8 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 9 | fitemremark | 产品行备注 | varchar | 510 |  | √ | ' ' | 产品行备注 |
| 10 | fpromotecondition | 促销条件 | varchar | 510 |  | √ | ' ' | 促销条件 |
| 11 | fplansaleqty | 预计销售数量 | numeric | 23 | 10 | √ | 0 | 预计销售数量 |
| 12 | fitembrandid | 品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 13 | fitemgroupid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 14 | frebatetype | 返利方案 | bpchar | 1 |  | √ | ' ' | 返利方案,枚举: A :单位返利 B :返点返利 C :其他 |
| 15 | fnormalprice | 正常价格 | numeric | 23 | 10 | √ | 0 | 正常价格 |
| 16 | fpromotestrategy | 促销策略 | varchar | 510 |  | √ | ' ' | 促销策略 |
| 17 | fpromotiontype | 促销方案 | bpchar | 1 |  | √ | ' ' | 促销方案,枚举: A :折扣 B :满减 C :买赠 D :降价 E :其他 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | frebatestrategy | 返利策略 | varchar | 510 |  | √ | ' ' | 返利策略 |

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
| 3 | fsignusername | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftelephone | 手机号 | varchar | 80 |  | √ | ' ' | 手机号 |

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

## 活动费用方案-子表 t_ocmem_ap_planentry

- **表名称：** 活动费用方案-子表
- **表名：** t_ocmem_ap_planentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fcompanyamount | 公司承担费用 | numeric | 23 | 10 | √ | 0 | 公司承担费用 |
| 4 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fentrywriteoffid | 费用行类型id | int8 | 64 |  | √ | 0 | 费用行类型 ocdbd_entryexpensetype |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapplyamount | 已申请金额 | numeric | 23 | 10 | √ | 0 | 已申请金额 |
| 8 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 9 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | fcompanyrate | 公司承担（%） | numeric | 23 | 10 | √ | 0 | 公司承担（%） |
| 11 | flinkqty | 已关联数量 | numeric | 23 | 10 | √ | 0 | 已关联数量 |
| 12 | ffeeentryremark | 费用行备注 | varchar | 510 |  | √ | ' ' | 费用行备注 |
| 13 | fapporveamount | 已核销金额 | numeric | 23 | 10 | √ | 0 | 已核销金额 |
| 14 | ffeeamount | 费用金额 | numeric | 23 | 10 | √ | 0 | 费用金额 |
| 15 | fexpenserowtypeid | 活动行类型 | int8 | 64 |  | √ | 0 | 费用行类型分录 ocdbd_expensetype_entry |
| 16 | fapplyqty | 已申请数量 | numeric | 23 | 10 | √ | 0 | 已申请数量 |
| 17 | flinkamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 18 | ffeeexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_ap_planentry |  | fentryid |
| 2 | idx_ocmem_ap_planentry_fid |  | fid |
