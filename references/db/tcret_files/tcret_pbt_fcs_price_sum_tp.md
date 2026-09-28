# 从价计征房产税税源明细（暂存）-tcret_pbt_fcs_price_sum_tp

## 单据体-子表 t_tcret_pbt_fcs_price_det_tp

- **表名称：** 单据体-子表
- **表名：** t_tcret_pbt_fcs_price_det_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjmcodeid | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 3 | fjmamount | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 4 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 5 | fyjmamount | 月减免税额 | numeric | 23 | 10 | √ | 0 | 月减免税额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fend | 减免终止时间 | timestamp | 0 |  |  | null | 减免终止时间 |
| 8 | famount | 减免房产原值 | numeric | 23 | 10 | √ | 0 | 减免房产原值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_pbt_fcs_price_det_tp |  | fentryid |
| 2 | idx_tcret_fcs_price_det_tp |  | fid |

---

## 从价计征房产税税源明细（暂存）-主表 t_tcret_pbt_fcs_price_sum_tp

- **表名称：** 从价计征房产税税源明细（暂存）-主表
- **表名：** t_tcret_pbt_fcs_price_sum_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fisxgm | 是否小规模 | bpchar | 1 |  | √ | '0' | 是否小规模 |
| 4 | fsjssqz | 税局所属期止 | timestamp | 0 |  |  | null | 税局所属期止 |
| 5 | fownername | 所有权人名称 | varchar | 200 |  | √ | ' ' | 所有权人名称 |
| 6 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsourceid | 房产基础信息 | int8 | 64 |  | √ | 0 | [房产基础信息 tdm_fcs_basic_info](../tdm_files/tdm_fcs_basic_info.md) |
| 9 | flandnumber | 房屋所在土地编号 | varchar | 50 |  | √ | ' ' | 房屋所在土地编号 |
| 10 | fdetailaddr | 详细地址 | varchar | 50 |  | √ | ' ' | 详细地址 |
| 11 | fcurrentpayable | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 12 | fchangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: |
| 13 | fpaidtaxes | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 14 | funifiedsocialcode | 所有权人纳税人识别号 | varchar | 50 |  | √ | ' ' | 所有权人纳税人识别号 |
| 15 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 16 | ffixassertunitcode | 不动产单元号 | varchar | 50 |  | √ | ' ' | 不动产单元号 |
| 17 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 18 | fhirearea | 出租房产面积（平方米） | numeric | 23 | 10 | √ | 0 | 出租房产面积（平方米） |
| 19 | ftaxpayer | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型,枚举: owner :产权所有人 manager :经营管理人 pledgee :承典人 proxy :房屋代管人 user :房屋使用人 renter :融资租赁承租人 |
| 20 | ffixassertnumber | 不动产权证号 | varchar | 50 |  | √ | ' ' | 不动产权证号 |
| 21 | fchangedate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 22 | frentalvalue | 其中出租房产原值 | numeric | 23 | 10 | √ | 0 | 其中出租房产原值 |
| 23 | ftaxtimepoint | 纳税时点 | varchar | 50 |  | √ | ' ' | 纳税时点,枚举: monthbefore :月度终了前 monthafter :月度终了后 yearbefore :年度终了前 yearafter :年度终了后 seasonbefore :季度终了前 seasonafter :季度终了后 halfyearbefore :半年终了前 halfyearafter :半年终了后 —— :—— |
| 24 | faddr | 房产坐落地址 | varchar | 50 |  | √ | ' ' | 房产坐落地址 |
| 25 | fdraftid | 底稿ID | int8 | 64 |  | √ | 0 | 底稿ID |
| 26 | fname | 房产名称 | varchar | 50 |  | √ | ' ' | 房产名称 |
| 27 | fassertvalue | 房产原值 | numeric | 23 | 10 | √ | 0 | 房产原值 |
| 28 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 29 | ftaxratio | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 30 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 31 | fmaindataid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 32 | fbuildingusage | 房产用途 | varchar | 50 |  | √ | ' ' | 房产用途,枚举: industry :工业 bussiness :商业及办公 house :住房 other :其他 |
| 33 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 34 | facquiredate | 房产取得时间 | timestamp | 0 |  |  | null | 房产取得时间 |
| 35 | ftaxbasis | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 36 | farea | 建筑面积（平方米） | numeric | 23 | 10 | √ | 0 | 建筑面积（平方米） |
| 37 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 38 | fsjssqq | 税局所属期起 | timestamp | 0 |  |  | null | 税局所属期起 |
| 39 | fnumber | 房产编码 | varchar | 50 |  | √ | ' ' | 房产编码 |
| 40 | fcurrentjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_pbt_fcs_price_sum_tp |  | fmaindataid |
| 2 | pk_tcret_pbt_fcs_price_sum_tp |  | fid |
