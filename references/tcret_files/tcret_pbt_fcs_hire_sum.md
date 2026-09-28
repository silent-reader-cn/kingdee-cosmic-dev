# 从租计征房产税税源明细-tcret_pbt_fcs_hire_sum

## 单据体-子表 t_tcret_pbt_fcs_hire_det

- **表名称：** 单据体-子表
- **表名：** t_tcret_pbt_fcs_hire_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjmcodeid | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 3 | fjmamount | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 4 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 5 | fyjmamount | 月减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 月减免税额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fend | 减免终止时间 | timestamp | 0 |  |  | null | 减免终止时间 |
| 8 | famount | 减免租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 减免租金收入 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_pbt_fcs_hire_det_fk |  | fid |
| 2 | pk_tcret_pbt_fcs_hire_det |  | fentryid |

---

## 租赁信息-子表 t_tcret_pbt_fcs_hire_rent

- **表名称：** 租赁信息-子表
- **表名：** t_tcret_pbt_fcs_hire_rent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 申报租金所属期止 | timestamp | 0 |  |  | null | 申报租金所属期止 |
| 3 | fhirearea | 出租面积 | numeric | 23 | 10 | √ | 0 | 出租面积 |
| 4 | fstartdate | 申报租金所属期起 | timestamp | 0 |  |  | null | 申报租金所属期起 |
| 5 | ftenantry | 承租方名称 | varchar | 50 |  | √ | ' ' | 承租方名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frentincome | 申报租金收入 | numeric | 23 | 10 | √ | 0 | 申报租金收入 |
| 8 | fhiretaxcode | 承租方纳税人识别号 | varchar | 50 |  | √ | ' ' | 承租方纳税人识别号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_pbt_fcs_hire_rent |  | fentryid |
| 2 | idx_tcret_pbt_fcs_hire_rent_fk |  | fid |

---

## 从租计征房产税税源明细-主表 t_tcret_pbt_fcs_hire_sum

- **表名称：** 从租计征房产税税源明细-主表
- **表名：** t_tcret_pbt_fcs_hire_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisxgm | 是否小规模 | bpchar | 1 |  | √ | '0' | 是否小规模 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsourceid | 房产出租信息 | int8 | 64 |  | √ | 0 | 房产出租信息 tdm_house_rental_info |
| 7 | fcontractstart | 申报租金所属租赁期起 | timestamp | 0 |  |  | null | 申报租金所属租赁期起 |
| 8 | fcurrentpayable | 本期应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应纳税额 |
| 9 | fleaseename | 承租方名称 | varchar | 50 |  | √ | ' ' | 承租方名称 |
| 10 | fcurrental | 本期申报租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 本期申报租金收入 |
| 11 | fpaidtaxes | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 12 | funifiedsocialcode | 所有权人纳税人识别号 | varchar | 50 |  | √ | ' ' | 所有权人纳税人识别号 |
| 13 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 14 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 15 | fcontractend | 申报租金所属租赁期止 | timestamp | 0 |  |  | null | 申报租金所属租赁期止 |
| 16 | fleasecontractno | 租赁合同编号 | varchar | 50 |  | √ | ' ' | 租赁合同编号 |
| 17 | ffcsapanage | 房产税属地管理 | int8 | 64 |  | √ | 0 | 房产税属地管理 tpo_tcret_fcs_apanage |
| 18 | ftaxauthorityid | ftaxauthorityid | int8 | 64 |  | √ | 0 |  |
| 19 | fleaseetaxcode | 承租方纳税人识别号 | varchar | 50 |  | √ | ' ' | 承租方纳税人识别号 |
| 20 | fdraftid | 底稿ID | int8 | 64 |  | √ | 0 | 底稿ID |
| 21 | fname | 房产名称 | varchar | 50 |  | √ | ' ' | 房产名称 |
| 22 | ftaxauthority | 房产所属主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 23 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 24 | fmaindataid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 25 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 26 | fleasearea | 出租面积 | numeric | 23 | 10 | √ | 0 | 出租面积 |
| 27 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 28 | fnumber | 房产编号 | varchar | 50 |  | √ | ' ' | 房产编号 |
| 29 | fcurrentjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_pbt_fcs_hire_sum |  | fid |
| 2 | idx_tcret_pbt_fcs_hire_sum |  | fmaindataid |
