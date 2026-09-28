# 房产出租信息-tdm_house_rental_info

## 房产出租信息-多语言表 t_tdm_house_rental_info_l

- **表名称：** 房产出租信息-多语言表
- **表名：** t_tdm_house_rental_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fbuildingname | 房产名称 | varchar | 50 |  | √ | ' ' | 房产名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_house_rental_info_l_pkey |  | fpkid |
| 2 | idx_tdm_house_rental_info_l_0 |  | fid,flocaleid |

---

## 子单据体-子表 t_tdm_house_rental_detail

- **表名称：** 子单据体-子表
- **表名：** t_tdm_house_rental_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fskperiod | 税款所属期 | varchar | 50 |  | √ | ' ' | 税款所属期 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | frental | 租金（元） | numeric | 23 | 10 | √ | 0 | 租金（元） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_house_rental_detail_fk |  | fentryid |
| 2 | pk_tdm_house_rental_detail |  | fdetailid |

---

## 从租计征-子表 t_tdm_house_rental_entity

- **表名称：** 从租计征-子表
- **表名：** t_tdm_house_rental_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | frentmonth | 合同约定租期（月份数） | int8 | 64 |  | √ | 0 | 合同约定租期（月份数） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fhouserentalinfo | 房产出租信息 | int8 | 64 |  | √ | 0 | 房产出租信息 tdm_house_rental_info |
| 7 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | fenddate | 申报租金所属租赁期止 | timestamp | 0 |  |  | null | 申报租金所属租赁期止 |
| 9 | fhirearea | 出租面积（㎡） | numeric | 23 | 10 | √ | 0 | 出租面积（㎡） |
| 10 | fstartdate | 申报租金所属租赁期起 | timestamp | 0 |  |  | null | 申报租金所属租赁期起 |
| 11 | ftenantry | 承租方名称 | varchar | 50 |  | √ | ' ' | 承租方名称 |
| 12 | feachrentincome | 每期申报租金收入 | numeric | 23 | 10 | √ | 0 | 每期申报租金收入 |
| 13 | frentincome | 租金收入（元） | numeric | 23 | 10 | √ | 0 | 租金收入（元） |
| 14 | fhiretaxcode | 承租方纳税人识别号 | varchar | 50 |  | √ | ' ' | 承租方纳税人识别号 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_house_rental_entity_fk |  | fid |
| 2 | pk_tdm_house_rental_entity |  | fentryid |

---

## 单据体-子表 t_tdm_house_rental_edit

- **表名称：** 单据体-子表
- **表名：** t_tdm_house_rental_edit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuildingno | fbuildingno | varchar | 50 |  | √ | ' ' |  |
| 3 | fskssq | 税款所属期 | varchar | 50 |  | √ | ' ' | 税款所属期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fleaseno | fleaseno | varchar | 50 |  | √ | ' ' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frent | 租金（元） | numeric | 23 | 10 | √ | 0.0000000000 | 租金（元） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_house_rental_edit_fk |  | fid |
| 2 | t_tdm_house_rental_edit_pkey |  | fentryid |

---

## 房产出租信息-主表 t_tdm_house_rental_info

- **表名称：** 房产出租信息-主表
- **表名：** t_tdm_house_rental_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ffcsbasicinfo | 房产编号 | int8 | 64 |  | √ | 0 | 房产基础信息 tdm_fcs_basic_info |
| 4 | ftaxauthoritydyo | 房产所属主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 5 | fcontractstart | 合同约定租赁期起 | timestamp | 0 |  |  | null | 合同约定租赁期起 |
| 6 | fdetailaddr | 详细地址 | varchar | 50 |  | √ | ' ' | 详细地址 |
| 7 | fleaseename | 承租方名称 | varchar | 50 |  | √ | ' ' | 承租方名称 |
| 8 | ffirsthalfmonth | 上半年申报月份 | varchar | 50 |  | √ | '6' | 上半年申报月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 |
| 9 | fendmonth | 终了前月份数 | varchar | 30 |  | √ | ' ' | 终了前月份数,枚举: 1 :1个月 2 :2个月 3 :3个月 4 :4个月 5 :5个月 6 :6个月 7 :7个月 8 :8个月 9 :9个月 10 :10个月 11 :11个月 12 :12个月 |
| 10 | fsecondhalfmonth | 下半年申报月份 | varchar | 50 |  | √ | '12' | 下半年申报月份,枚举: 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 11 | fcontractincome | 合同租金总收入 | numeric | 23 | 10 | √ | 0.0000000000 | 合同租金总收入 |
| 12 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ffourthquartermonth | 四季度申报月份 | varchar | 50 |  | √ | '12' | 四季度申报月份,枚举: 10 :10月 11 :11月 12 :12月 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | ffcsbyhirelimit | 从租计征房产税纳税期限 | varchar | 30 |  | √ | ' ' | 从租计征房产税纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fleasecontractno | 租赁合同编号 | varchar | 50 |  | √ | ' ' | 租赁合同编号 |
| 20 | fcontractend | 合同约定租赁期止 | timestamp | 0 |  |  | null | 合同约定租赁期止 |
| 21 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 22 | fcity | 市 | varchar | 50 |  | √ | ' ' | 市 |
| 23 | ftaxtimepoint | 纳税时点 | varchar | 30 |  | √ | ' ' | 纳税时点,枚举: monthbefore :月度终了前 monthafter :月度终了后 yearbefore :年度终了前 yearafter :年度终了后 seasonbefore :季度终了前 seasonafter :季度终了后 halfyearbefore :半年终了前 halfyearafter :半年终了后 —— :—— |
| 24 | feachincome | 每期申报租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 每期申报租金收入 |
| 25 | faddr | 房产坐落地址 | varchar | 50 |  | √ | ' ' | 房产坐落地址 |
| 26 | fleaseetaxcode | 承租方纳税识别号 | varchar | 50 |  | √ | ' ' | 承租方纳税识别号 |
| 27 | fsecondquartermonth | 二季度申报月份 | varchar | 50 |  | √ | '6' | 二季度申报月份,枚举: 4 :4月 5 :5月 6 :6月 |
| 28 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | ftaxauthority | 主管税务机关（废弃） | varchar | 50 |  | √ | ' ' | 主管税务机关（废弃） |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 32 | fbuildingusage | 房产用途 | varchar | 30 |  | √ | ' ' | 房产用途,枚举: industry :工业 bussiness :商业及办公 house :住房 other :其它 |
| 33 | fleasearea | 出租面积（平方米） | numeric | 23 | 10 | √ | 0.0000000000 | 出租面积（平方米） |
| 34 | ffirstquartermonth | 一季度申报月份 | varchar | 50 |  | √ | '3' | 一季度申报月份,枚举: 1 :1月 2 :2月 3 :3月 |
| 35 | fmonthnumber | 合同约定租期（月份数） | int8 | 64 |  | √ | 0 | 合同约定租期（月份数） |
| 36 | fthirdquartermonth | 三季度申报月份 | varchar | 50 |  | √ | '9' | 三季度申报月份,枚举: 7 :7月 8 :8月 9 :9月 |
| 37 | fbasedatafield | 房产属地管理 | int8 | 64 |  | √ | 0 | 房产税属地管理 tpo_tcret_fcs_apanage |
| 38 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 40 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 41 | fprovince | 省 | varchar | 50 |  | √ | ' ' | 省 |
| 42 | fcountry | 县 | varchar | 50 |  | √ | ' ' | 县 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_house_rental_info_pkey |  | fid |
| 2 | idx_tdm_house_rental_info |  | forg,ffcsbasicinfo |

---

## 减免登记台账-子表 t_tdm_fcs_renta_reduction

- **表名称：** 减免登记台账-子表
- **表名：** t_tdm_fcs_renta_reduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 3 | fregisterule | 减免租金登记规则 | varchar | 30 |  | √ | ' ' | 减免租金登记规则,枚举: 1 :全部登记 2 :按百分比登记 3 :录入登记值 |
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
| 1 | pk_tdm_fcs_renta_reduction |  | fentryid |
| 2 | idx_tdm_fcs_renta_reduction_fk |  | fid |
