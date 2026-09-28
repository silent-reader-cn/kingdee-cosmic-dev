# 报价查询-tnd_vieanalyze

## 报价查询-主表 t_src_vie_detail

- **表名称：** 报价查询-主表
- **表名：** t_src_vie_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | 税率值(%) | numeric | 23 | 10 | √ | 0 | 税率值(%) |
| 4 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | flocprice | 本币未税单价 | numeric | 23 | 10 | √ | 0 | 本币未税单价 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fexchtypeid | 汇率 | int8 | 64 |  | √ | 0 | 汇率 bd_exrate_tree |
| 9 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 10 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 11 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 12 | frestofbidcount | 报价剩余次数 | int4 | 32 |  | √ | 0 | 报价剩余次数 |
| 13 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 14 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 15 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 16 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 17 | fbidcount | 报价次数 | int4 | 32 |  | √ | 0 | 报价次数 |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 19 | fincreaseprice | 调价幅度 | numeric | 23 | 10 | √ | 0 | 调价幅度 |
| 20 | fsuppliertype | fsuppliertype | varchar | 50 |  | √ | ' ' |  |
| 21 | freducetype | 调价方式 | varchar | 2 |  | √ | ' ' | 调价方式,枚举: A :按比例(%) B :按金额 |
| 22 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 23 | freduceamt | freduceamt | numeric | 23 | 10 | √ | 0 |  |
| 24 | fsupplierip | 供应商IP地址 | varchar | 100 |  | √ | ' ' | 供应商IP地址 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fisdiscarded | 是否弃标的 | bpchar | 1 |  | √ | '0' | 是否弃标的 |
| 27 | frank | 本轮排名 | int4 | 32 |  | √ | 0 | 本轮排名 |
| 28 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 29 | fmaxtaxprice | 最高含税单价 | numeric | 23 | 10 | √ | 0 | 最高含税单价 |
| 30 | fviediffer | 竞价价差 | numeric | 23 | 10 | √ | 0 | 竞价价差 |
| 31 | fentrystatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: B :已报价 C :已开标 D :已关闭 |
| 32 | flocquoteamt | flocquoteamt | numeric | 23 | 10 | √ | 0 |  |
| 33 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 34 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 35 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 36 | fmaxprice | 最高未税单价 | numeric | 23 | 10 | √ | 0 | 最高未税单价 |
| 37 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 38 | fexchange | fexchange | numeric | 23 | 10 | √ | 0 |  |
| 39 | fvieratio | 竞价比例(%) | numeric | 23 | 10 | √ | 0 | 竞价比例(%) |
| 40 | fviefrom | 竞价区间从(>) | numeric | 23 | 10 | √ | 0 | 竞价区间从(>) |
| 41 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 42 | floctaxamount | 本币含税金额 | numeric | 23 | 10 | √ | 0 | 本币含税金额 |
| 43 | fvieto | 竞价区间至(<) | numeric | 23 | 10 | √ | 0 | 竞价区间至(<) |
| 44 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) |
| 45 | fquotedate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 46 | floctaxprice | 本币含税单价 | numeric | 23 | 10 | √ | 0 | 本币含税单价 |
| 47 | fquoteamt | fquoteamt | numeric | 23 | 10 | √ | 0 |  |
| 48 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 49 | flocamount | 本币未税金额 | numeric | 23 | 10 | √ | 0 | 本币未税金额 |
| 50 | flocreduceamt | flocreduceamt | numeric | 23 | 10 | √ | 0 |  |
| 51 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 52 | fexchrate | 汇率值 | numeric | 23 | 10 | √ | 0 | 汇率值 |
| 53 | fcurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_vie_detail |  | fentryid |
| 2 | idx_src_vie_detail_time |  | fquotedate |
| 3 | idx_src_vie_detail_turn |  | fturns |
| 4 | idx_src_vie_detail_pid |  | fpurlistid |
| 5 | idx_src_vie_detail_vieturn |  | fvieturns |
| 6 | idx_src_vie_detail_sid |  | fsupplierid |
| 7 | idx_src_vie_detail_fid |  | fid |
| 8 | idx_src_vie_detail_type |  | fsuppliertype |

---

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 报价查询-多语言表 t_src_vie_detail_l

- **表名称：** 报价查询-多语言表
- **表名：** t_src_vie_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
