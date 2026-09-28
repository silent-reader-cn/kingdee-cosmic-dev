# 城镇土地使用税税源明细（暂存）-tcret_pbt_tds_sum_tp

## 城镇土地使用税税源明细（暂存）-主表 t_tcret_pbt_tds_sum_tp

- **表名称：** 城镇土地使用税税源明细（暂存）-主表
- **表名：** t_tcret_pbt_tds_sum_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisxgm | 是否小规模 | bpchar | 1 |  | √ | '0' | 是否小规模 |
| 4 | fownername | 土地使用权人名称 | varchar | 50 |  | √ | ' ' | 土地使用权人名称 |
| 5 | flandnature | 土地性质 | varchar | 50 |  | √ | ' ' | 土地性质,枚举: 1 :国有 2 :集体 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsourceid | 土地税源信息 | int8 | 64 |  | √ | 0 | 土地税源信息 tdm_tds_basic_info |
| 8 | fobtaintime | 土地取得时间 | timestamp | 0 |  |  | null | 土地取得时间 |
| 9 | ftdsapanage | 土地属地管理 | int8 | 64 |  | √ | 0 | 土地税属地管理 tpo_tcret_tds_apanage |
| 10 | fdetailaddr | 土地坐落地址（详细地址） | varchar | 50 |  | √ | ' ' | 土地坐落地址（详细地址） |
| 11 | fcurrentpayable | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 12 | fchangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: |
| 13 | fprice | 地价（元） | numeric | 23 | 10 | √ | 0 | 地价（元） |
| 14 | fpaidtaxes | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 15 | ftaxstandard | 税额标准 | numeric | 23 | 10 | √ | 0 | 税额标准 |
| 16 | funifiedsocialcode | 土地使用权人纳税人识别号 | varchar | 50 |  | √ | ' ' | 土地使用权人纳税人识别号 |
| 17 | ftextfield | 土地名称 | varchar | 50 |  | √ | ' ' | 土地名称 |
| 18 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 19 | ffixassertunitcode | 不动产单元号 | varchar | 50 |  | √ | ' ' | 不动产单元号 |
| 20 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 21 | ffixassertnumber | 不动产权证号 | varchar | 50 |  | √ | ' ' | 不动产权证号 |
| 22 | fchangedate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 23 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型,枚举: 1 :土地使用权人 2 :集体土地使用人 3 :无偿使用人 4 :代管人 5 :实际使用人 |
| 24 | fdraftid | 底稿ID | int8 | 64 |  | √ | 0 | 底稿ID |
| 25 | ftaxauthority | 土地所属主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 26 | flandobtainway | 土地取得方式 | varchar | 50 |  | √ | ' ' | 土地取得方式,枚举: 1 :划拨 2 :出让 3 :转让 4 :租赁 5 :其他 |
| 27 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 28 | fmaindataid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 29 | fparcelcode | 宗地号 | varchar | 50 |  | √ | ' ' | 宗地号 |
| 30 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 31 | flandlevel | 土地等级 | varchar | 50 |  | √ | ' ' | 土地等级 |
| 32 | ftaxbasis | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 33 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 34 | foccupylandarea | 占用土地面积 | numeric | 23 | 10 | √ | 0 | 占用土地面积 |
| 35 | fnumber | 土地编号 | varchar | 50 |  | √ | ' ' | 土地编号 |
| 36 | fcurrentjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 37 | flandpurpose | 土地用途 | varchar | 50 |  | √ | ' ' | 土地用途,枚举: 1 :工业 2 :商业 3 :居住 4 :综合 5 :房地产开发企业的开发用地 6 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_pbt_tds_sum_tp |  | fmaindataid |
| 2 | pk_tcret_pbt_tds_sum_tp |  | fid |

---

## 单据体-子表 t_tcret_pbt_tds_det_tp

- **表名称：** 单据体-子表
- **表名：** t_tcret_pbt_tds_det_tp

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
| 8 | famount | 减免税面积 | numeric | 23 | 10 | √ | 0 | 减免税面积 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_pbt_tds_det_tp_fk |  | fid |
| 2 | pk_tcret_pbt_tds_det_tp |  | fentryid |
