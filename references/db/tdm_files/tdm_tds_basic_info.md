# 土地税源信息-tdm_tds_basic_info

## 减免登记台账-子表 t_tdm_tds_basic_reduction

- **表名称：** 减免登记台账-子表
- **表名：** t_tdm_tds_basic_reduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 3 | fregisterule | 减免面积登记规则 | varchar | 30 |  | √ | ' ' | 减免面积登记规则,枚举: 1 :全部登记 2 :按百分比登记 3 :录入登记值 |
| 4 | fratio | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ftaxdeduction | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 7 | fend | 减免终止时间 | timestamp | 0 |  |  | null | 减免终止时间 |
| 8 | fregisteretio | 登记减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 登记减免比例 |
| 9 | fentervalue | 录入登记值 | numeric | 23 | 10 | √ | 0.0000000000 | 录入登记值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmonthlimit | 每月减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 每月减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tds_basic_reduction |  | fentryid |
| 2 | idx_tdm_tds_basic_reduction_fk |  | fid |

---

## 变更登记台账-子表 t_tdm_tds_basic_change

- **表名称：** 变更登记台账-子表
- **表名：** t_tdm_tds_basic_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flevel | 变更后土地等级 | varchar | 50 |  | √ | ' ' | 变更后土地等级 |
| 5 | fmodifydate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fchangedate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fchangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: tdmj :土地面积变更 tddj :土地等级变更 other :其他信息项变更 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | flandarea | 变更后占用土地面积（平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后占用土地面积（平方米） |
| 11 | ftaxstandard | 变更后税额标准（元/平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后税额标准（元/平方米） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tds_basic_change_fk |  | fid |
| 2 | pk_tdm_tds_basic_change |  | fentryid |

---

## 资产编码-多选基础资料表 t_tdm_tds_asset

- **表名称：** 资产编码-多选基础资料表
- **表名：** t_tdm_tds_asset

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
| 1 | pk_tdm_tds_asset |  | fpkid |
| 2 | idx_tdm_tds_asset_fk |  | fid |

---

## 应摊入土地价值-子表 t_tdm_tds_basic_house

- **表名称：** 应摊入土地价值-子表
- **表名：** t_tdm_tds_basic_house

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhousearea | 建筑面积（平方米） | numeric | 23 | 10 | √ | 0 | 建筑面积（平方米） |
| 3 | fvalue | 应摊入土地价值（元） | numeric | 23 | 10 | √ | 0 | 应摊入土地价值（元） |
| 4 | fhousemodifier | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fhousemodifydate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fhousenumber | 房产编号 | int8 | 64 |  | √ | 0 | [房产基础信息 tdm_fcs_basic_info](../tdm_files/tdm_fcs_basic_info.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tds_basic_house |  | fentryid |
| 2 | idx_t_tdm_tds_basic_house |  | fid |

---

## 土地税源信息-多语言表 t_tdm_tds_basic_info_l

- **表名称：** 土地税源信息-多语言表
- **表名：** t_tdm_tds_basic_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 土地名称 | varchar | 50 |  | √ | ' ' | 土地名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_tds_basic_info_l_pkey |  | fpkid |
| 2 | idx_tdm_tds_basic_info_l_0 |  | fid,flocaleid |

---

## 土地税源信息-主表 t_tdm_tds_basic_info

- **表名称：** 土地税源信息-主表
- **表名：** t_tdm_tds_basic_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxtimelimit | 纳税期限 | varchar | 30 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 |
| 3 | ftaxauthoritydyo | 土地所属主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftransregional | 跨区域申报 | varchar | 50 |  | √ | ' ' | 跨区域申报,枚举: true :是 false :否 |
| 6 | fendmonth | 终了前月份数 | varchar | 30 |  | √ | ' ' | 终了前月份数,枚举: 1 :1个月 2 :2个月 3 :3个月 4 :4个月 5 :5个月 6 :6个月 7 :7个月 8 :8个月 9 :9个月 10 :10个月 11 :11个月 12 :12个月 |
| 7 | flandplotratio | 宗地容积率 | numeric | 23 | 10 | √ | 0 | 宗地容积率 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | ffixassertnumber | 不动产权证号 | varchar | 50 |  | √ | ' ' | 不动产权证号 |
| 12 | ftaxpayertype | 纳税人类型 | varchar | 30 |  | √ | ' ' | 纳税人类型,枚举: 1 :土地使用权人 2 :集体土地使用人 3 :无偿使用人 4 :代管人 5 :实际使用人 |
| 13 | fcity | 市 | varchar | 50 |  | √ | ' ' | 市 |
| 14 | ftaxtimepoint | 纳税时点 | varchar | 30 |  | √ | ' ' | 纳税时点,枚举: monthbefore :月度终了前 monthafter :月度终了后 yearbefore :年度终了前 yearafter :年度终了后 seasonbefore :季度终了前 seasonafter :季度终了后 halfyearbefore :半年终了前 halfyearafter :半年终了后 —— :—— |
| 15 | flanddevcost | 土地开发成本（元） | numeric | 23 | 10 | √ | 0.0000000000 | 土地开发成本（元） |
| 16 | faddr | 土地坐落地址 | varchar | 50 |  | √ | ' ' | 土地坐落地址 |
| 17 | flandunitprice | 土地单价（元） | numeric | 23 | 10 | √ | 0 | 土地单价（元） |
| 18 | fparcelcode | 宗地号 | varchar | 50 |  | √ | ' ' | 宗地号 |
| 19 | fdatefield | 土地取得时间 | timestamp | 0 |  |  | null | 土地取得时间 |
| 20 | ftdsapanageld | ftdsapanageld | int8 | 64 |  | √ | 0 |  |
| 21 | fthirdquartermonth | 三季度申报月份 | varchar | 50 |  | √ | '9' | 三季度申报月份,枚举: 7 :7月 8 :8月 9 :9月 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 土地编号 | varchar | 30 |  | √ | ' ' | 土地编号 |
| 24 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 25 | flandarea | 占用土地面积（平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 占用土地面积（平方米） |
| 26 | fcountry | 县 | varchar | 50 |  | √ | ' ' | 县 |
| 27 | fdatatype | 数据来源 | varchar | 50 |  | √ | '1' | 数据来源,枚举: 1 :手工新增 2 :税局下载 |
| 28 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | flandnature | 土地性质 | varchar | 30 |  | √ | ' ' | 土地性质,枚举: 1 :国有 2 :集体 |
| 30 | fdetailaddr | 详细地址 | varchar | 50 |  | √ | ' ' | 详细地址 |
| 31 | ffirsthalfmonth | 上半年申报月份 | varchar | 50 |  | √ | '6' | 上半年申报月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 |
| 32 | fsecondhalfmonth | 下半年申报月份 | varchar | 50 |  | √ | '12' | 下半年申报月份,枚举: 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 33 | fchangetype | 纳税义务终止类型 | varchar | 30 |  | √ | ' ' | 纳税义务终止类型,枚举: ownerTransfer :权属转移 taxObligationStop :其他纳税义务终止 |
| 34 | fprice | 地价（元） | numeric | 23 | 10 | √ | 0.0000000000 | 地价（元） |
| 35 | ftaxstandard | 税额标准（元/平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 税额标准（元/平方米） |
| 36 | ffourthquartermonth | 四季度申报月份 | varchar | 50 |  | √ | '12' | 四季度申报月份,枚举: 10 :10月 11 :11月 12 :12月 |
| 37 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 40 | ffixassertunitcode | 不动产单元号 | varchar | 50 |  | √ | ' ' | 不动产单元号 |
| 41 | fsyzt | 税源状态 | varchar | 50 |  | √ | ' ' | 税源状态,枚举: 1 :正常 2 :义务终止 |
| 42 | faftermonth | 终了后月份数 | varchar | 50 |  | √ | ' ' | 终了后月份数,枚举: 1 :1个月 2 :2个月 3 :3个月 4 :4个月 5 :5个月 6 :6个月 7 :7个月 8 :8个月 9 :9个月 10 :10个月 11 :11个月 12 :12个月 |
| 43 | fusagerightamount | 取得土地使用权支付金额（元） | numeric | 23 | 10 | √ | 0.0000000000 | 取得土地使用权支付金额（元） |
| 44 | fsecondquartermonth | 二季度申报月份 | varchar | 50 |  | √ | '6' | 二季度申报月份,枚举: 4 :4月 5 :5月 6 :6月 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | ftaxauthority | 主管税务机关（废弃） | varchar | 50 |  | √ | ' ' | 主管税务机关（废弃） |
| 47 | flandobtainway | 土地取得方式 | varchar | 30 |  | √ | ' ' | 土地取得方式,枚举: 1 :划拨 2 :出让 3 :转让 4 :租赁 5 :其他 |
| 48 | ftaxratio | ftaxratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 51 | ftdsapanageid | 土地属地管理 | int8 | 64 |  | √ | 0 | 土地税属地管理 tpo_tcret_tds_apanage |
| 52 | flevel | 土地等级 | varchar | 50 |  | √ | ' ' | 土地等级 |
| 53 | ffirstquartermonth | 一季度申报月份 | varchar | 50 |  | √ | '3' | 一季度申报月份,枚举: 1 :1月 2 :2月 3 :3月 |
| 54 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 55 | fchangetime | 纳税义务终止时间 | timestamp | 0 |  |  | null | 纳税义务终止时间 |
| 56 | flandpurpose | 土地用途 | varchar | 30 |  | √ | ' ' | 土地用途,枚举: 1 :工业 2 :商业 3 :居住 4 :综合 5 :房地产开发企业的开发用地 6 :其他 |
| 57 | fprovince | 省 | varchar | 50 |  | √ | ' ' | 省 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_tds_basic_info_pkey |  | fid |
| 2 | idx_tdm_tds_basic_info |  | fnumber |
