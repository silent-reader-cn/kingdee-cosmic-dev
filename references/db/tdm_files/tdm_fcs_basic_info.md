# 房产基础信息-tdm_fcs_basic_info

## 附件-附件表 t_tdm_fcs_basic_change_a

- **表名称：** 附件-附件表
- **表名：** t_tdm_fcs_basic_change_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_fcs_basic_change_a |  | fpkid |
| 2 | idx_t_tdm_fbca_entryid |  | fentryid |

---

## 减免登记台账-子表 t_tdm_fcs_basic_reduction

- **表名称：** 减免登记台账-子表
- **表名：** t_tdm_fcs_basic_reduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 3 | fregisterule | 减免原值登记规则 | varchar | 30 |  | √ | ' ' | 减免原值登记规则,枚举: 1 :全部登记 2 :按百分比登记 3 :录入登记值 |
| 4 | fratio | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ftaxdeduction | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 7 | fend | 减免终止时间 | timestamp | 0 |  |  | null | 减免终止时间 |
| 8 | fmonthly | 按月独立减免 | bpchar | 1 |  | √ | '0' | 按月独立减免 |
| 9 | fregisteretio | 登记减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 登记减免比例 |
| 10 | fentervalue | 录入登记值 | numeric | 23 | 10 | √ | 0.0000000000 | 录入登记值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmonthlimit | 每月减免税额 | numeric | 23 | 10 |  | null | 每月减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_fcs_basic_reduction_fk |  | fid |
| 2 | pk_tdm_fcs_basic_reduction |  | fentryid |

---

## 资产编码-多选基础资料表 t_tdm_fcs_asset

- **表名称：** 资产编码-多选基础资料表
- **表名：** t_tdm_fcs_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资产清单 tdm_asset_data](../tdm_files/tdm_asset_data.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_fcs_asset_fk |  | fid |
| 2 | pk_tdm_fcs_asset |  | fpkid |

---

## 变更登记台账-子表 t_tdm_fcs_basic_change

- **表名称：** 变更登记台账-子表
- **表名：** t_tdm_fcs_basic_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fassertvalue | 变更后房产原值（元） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后房产原值（元） |
| 5 | fbghousevalue | 其中：房屋原值（元） | numeric | 23 | 10 | √ | 0 | 其中：房屋原值（元） |
| 6 | fbgequipmentvalue | 其中：房屋附属设备及配套设施（元） | numeric | 23 | 10 | √ | 0 | 其中：房屋附属设备及配套设施（元） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fchangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: fcyz :房产原值变更 czfcyz :出租房产原值变更 other :其他信息项变更 equipment :其中：房屋附属设备及配套设施（元） ytrtdjz :其中：应摊入土地价值（元） fwyz :其中：房屋原值（元） |
| 9 | fbgvalue | 其中：应摊入土地价值（元） | numeric | 23 | 10 | √ | 0 | 其中：应摊入土地价值（元） |
| 10 | fmodifydate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 11 | fhireassertvalue | 变更后出租房产原值（元） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后出租房产原值（元） |
| 12 | fchangedate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 13 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工录入 1 :系统生成 2 :税局下载 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_fcs_basic_change_fk |  | fid |
| 2 | pk_tdm_fcs_basic_change |  | fentryid |

---

## 房产基础信息-多语言表 t_tdm_fcs_basic_info_l

- **表名称：** 房产基础信息-多语言表
- **表名：** t_tdm_fcs_basic_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 房产名称 | varchar | 50 |  | √ | ' ' | 房产名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_fcs_basic_info_l_pkey |  | fpkid |
| 2 | idx_tdm_fcs_basic_info_l_0 |  | fid,flocaleid |

---

## 房产基础信息-主表 t_tdm_fcs_basic_info

- **表名称：** 房产基础信息-主表
- **表名：** t_tdm_fcs_basic_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxauthoritydyo | 房产所属主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 3 | ftransregional | 跨区域申报 | varchar | 50 |  | √ | ' ' | 跨区域申报,枚举: true :是 false :否 |
| 4 | fendmonth | 终了前月份数 | varchar | 30 |  | √ | ' ' | 终了前月份数,枚举: 1 :1个月 2 :2个月 3 :3个月 4 :4个月 5 :5个月 6 :6个月 7 :7个月 8 :8个月 9 :9个月 10 :10个月 11 :11个月 12 :12个月 |
| 5 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdataflag | 数据标识 | varchar | 50 |  | √ | ' ' | 数据标识 |
| 8 | fhirearea | 出租房产面积（平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 出租房产面积（平方米） |
| 9 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | ffixassertnumber | 不动产权证号 | varchar | 50 |  | √ | ' ' | 不动产权证号 |
| 11 | ftaxtimepoint | 纳税时点 | varchar | 30 |  | √ | ' ' | 纳税时点,枚举: monthbefore :月度终了前 monthafter :月度终了后 yearbefore :年度终了前 yearafter :年度终了后 seasonbefore :季度终了前 seasonafter :季度终了后 halfyearbefore :半年终了前 halfyearafter :半年终了后 —— :—— |
| 12 | faddr | 房产坐落地址 | varchar | 50 |  | √ | ' ' | 房产坐落地址 |
| 13 | fbuildingusage | 房产用途 | varchar | 30 |  | √ | ' ' | 房产用途,枚举: industry :工业 bussiness :商业及办公 house :住房 other :其他 |
| 14 | ftaxpaylimit | 纳税期限 | varchar | 30 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 15 | fthirdquartermonth | 三季度申报月份 | varchar | 50 |  | √ | '9' | 三季度申报月份,枚举: 7 :7月 8 :8月 9 :9月 |
| 16 | farea | 建筑面积（平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 建筑面积（平方米） |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 房产编号 | varchar | 30 |  | √ | ' ' | 房产编号 |
| 19 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 20 | fdatatype | 数据来源 | varchar | 50 |  | √ | '1' | 数据来源,枚举: 1 :手工新增 2 :税局下载 |
| 21 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | flandnumber | 房屋所在土地编号 | varchar | 50 |  | √ | ' ' | 房屋所在土地编号 |
| 23 | fdetailaddr | 详细地址 | varchar | 50 |  | √ | ' ' | 详细地址 |
| 24 | ffirsthalfmonth | 上半年申报月份 | varchar | 50 |  | √ | '6' | 上半年申报月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 |
| 25 | fsecondhalfmonth | 下半年申报月份 | varchar | 50 |  | √ | '12' | 下半年申报月份,枚举: 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 26 | fhousevalue | 房屋原值（初始价值） | numeric | 23 | 10 | √ | 0 | 房屋原值（初始价值） |
| 27 | fchangetype | 纳税义务终止类型 | varchar | 30 |  | √ | ' ' | 纳税义务终止类型,枚举: ownerTransfer :权属转移 taxObligationStop :其他纳税义务终止 |
| 28 | ffourthquartermonth | 四季度申报月份 | varchar | 50 |  | √ | '12' | 四季度申报月份,枚举: 10 :10月 11 :11月 12 :12月 |
| 29 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 32 | ffixassertunitcode | 不动产单元号 | varchar | 50 |  | √ | ' ' | 不动产单元号 |
| 33 | fsyzt | 税源状态 | varchar | 50 |  | √ | ' ' | 税源状态,枚举: 1 :正常 2 :义务终止 |
| 34 | ftaxpayer | 纳税人类型 | varchar | 30 |  | √ | ' ' | 纳税人类型,枚举: owner :产权所有人 manager :经营管理人 pledgee :承典人 proxy :房屋代管人 user :房屋使用人 renter :融资租赁承租人 |
| 35 | fhireassertvalue | 出租房产原值（元） | numeric | 23 | 10 | √ | 0.0000000000 | 出租房产原值（元） |
| 36 | ftaxbureaunumber | 企业登记房产编号 | varchar | 50 |  | √ | ' ' | 企业登记房产编号 |
| 37 | fchangedate | 纳税义务终止时间 | timestamp | 0 |  |  | null | 纳税义务终止时间 |
| 38 | fassetdata | 资产编码(废弃) | int8 | 64 |  | √ | 0 | [资产清单 tdm_asset_data](../tdm_files/tdm_asset_data.md) |
| 39 | faftermonth | 终了后月份数 | varchar | 50 |  | √ | ' ' | 终了后月份数,枚举: 1 :1个月 2 :2个月 3 :3个月 4 :4个月 5 :5个月 6 :6个月 7 :7个月 8 :8个月 9 :9个月 10 :10个月 11 :11个月 12 :12个月 |
| 40 | fsecondquartermonth | 二季度申报月份 | varchar | 50 |  | √ | '6' | 二季度申报月份,枚举: 4 :4月 5 :5月 6 :6月 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fequipmentvalue | 房屋附属设备及配套设施（初始价值） | numeric | 23 | 10 | √ | 0 | 房屋附属设备及配套设施（初始价值） |
| 43 | ftaxauthority | 主管税务机关（废弃） | varchar | 50 |  | √ | ' ' | 主管税务机关（废弃） |
| 44 | fassertvalue | 房产原值（元） | numeric | 23 | 10 | √ | 0.0000000000 | 房产原值（元） |
| 45 | ftaxratio | 计税比例 | numeric | 23 | 10 | √ | 0.0000000000 | 计税比例 |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 48 | flandtaxsource | 土地税源信息 | int8 | 64 |  | √ | 0 | [土地税源信息 tdm_tds_basic_info](../tdm_files/tdm_tds_basic_info.md) |
| 49 | ffirstquartermonth | 一季度申报月份 | varchar | 50 |  | √ | '3' | 一季度申报月份,枚举: 1 :1月 2 :2月 3 :3月 |
| 50 | fvalue | 应摊入土地价值（初始价值） | numeric | 23 | 10 | √ | 0 | 应摊入土地价值（初始价值） |
| 51 | facquiredate | 房产取得时间 | timestamp | 0 |  |  | null | 房产取得时间 |
| 52 | fbasedatafield | 房产属地管理 | int8 | 64 |  | √ | 0 | 房产税属地管理 tpo_tcret_fcs_apanage |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_fcs_basic_info |  | forg |
| 2 | t_tdm_fcs_basic_info_pkey |  | fid |
