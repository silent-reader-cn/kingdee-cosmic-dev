# 竞价明细(后台元数据)-src_vie_detailf7

## 竞价明细(后台元数据)-主表 t_src_vie_detail

- **表名称：** 竞价明细(后台元数据)-主表
- **表名：** t_src_vie_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | ftaxrate | 税率值(%) | numeric | 23 | 10 | √ | 0 | 税率值(%) |
| 4 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | flocprice | 本币未税单价 | numeric | 23 | 10 | √ | 0 | 本币未税单价 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fexchtypeid | 汇率 | int8 | 64 |  | √ | 0 | [汇率 bd_exrate_tree](../base_files/bd_exrate_tree.md) |
| 9 | fprotaxamount | 项目含税金额 | numeric | 23 | 10 | √ | 0 | 项目含税金额 |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 12 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 13 | fproamount | 项目未税金额 | numeric | 23 | 10 | √ | 0 | 项目未税金额 |
| 14 | frestofbidcount | 报价剩余次数 | int4 | 32 |  | √ | 0 | 报价剩余次数 |
| 15 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 16 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 17 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 18 | fmaxtaxamount | 含税起标金额 | numeric | 23 | 10 | √ | 0 | 含税起标金额 |
| 19 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 20 | fbidcount | 报价次数 | int4 | 32 |  | √ | 0 | 报价次数 |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 22 | fincreaseprice | 调价幅度 | numeric | 23 | 10 | √ | 0 | 调价幅度 |
| 23 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 24 | freducetype | 调价方式 | varchar | 2 |  | √ | ' ' | 调价方式,枚举: A :按比例(%) B :按金额 |
| 25 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 26 | freduceamt | freduceamt | numeric | 23 | 10 | √ | 0 |  |
| 27 | fsupplierip | 供应商IP地址 | varchar | 100 |  | √ | ' ' | 供应商IP地址 |
| 28 | fpkgrank | 标段排名 | int4 | 32 |  | √ | 0 | 标段排名 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fisdiscarded | 是否弃标的 | bpchar | 1 |  | √ | '0' | 是否弃标的 |
| 31 | frank | 当前排名 | int4 | 32 |  | √ | 0 | 当前排名 |
| 32 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 33 | fmaxtaxprice | 含税起标单价 | numeric | 23 | 10 | √ | 0 | 含税起标单价 |
| 34 | fviediffer | 竞价价差 | numeric | 23 | 10 | √ | 0 | 竞价价差 |
| 35 | fentrystatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: B :已报价 C :已开标 D :已关闭 |
| 36 | fmaxamount | 未税起标金额 | numeric | 23 | 10 | √ | 0 | 未税起标金额 |
| 37 | flocquoteamt | flocquoteamt | numeric | 23 | 10 | √ | 0 |  |
| 38 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 39 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 40 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 41 | fmaxprice | 未税起标单价 | numeric | 23 | 10 | √ | 0 | 未税起标单价 |
| 42 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: 0 :待处理 1 :已处理 |
| 44 | fpkgamount | 标段未税金额 | numeric | 23 | 10 | √ | 0 | 标段未税金额 |
| 45 | fexchange | fexchange | numeric | 23 | 10 | √ | 0 |  |
| 46 | fvieratio | 竞价比例(%) | numeric | 23 | 10 | √ | 0 | 竞价比例(%) |
| 47 | fviefrom | 竞价区间从(>) | numeric | 23 | 10 | √ | 0 | 竞价区间从(>) |
| 48 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 49 | fpkgtaxamount | 标段含税金额 | numeric | 23 | 10 | √ | 0 | 标段含税金额 |
| 50 | floctaxamount | 本币含税金额 | numeric | 23 | 10 | √ | 0 | 本币含税金额 |
| 51 | fvieto | 竞价区间至(<) | numeric | 23 | 10 | √ | 0 | 竞价区间至(<) |
| 52 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) |
| 53 | fquotedate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 54 | floctaxprice | 本币含税单价 | numeric | 23 | 10 | √ | 0 | 本币含税单价 |
| 55 | fquoteamt | fquoteamt | numeric | 23 | 10 | √ | 0 |  |
| 56 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 57 | flocamount | 本币未税金额 | numeric | 23 | 10 | √ | 0 | 本币未税金额 |
| 58 | flocreduceamt | flocreduceamt | numeric | 23 | 10 | √ | 0 |  |
| 59 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 60 | fprorank | 项目排名 | int4 | 32 |  | √ | 0 | 项目排名 |
| 61 | fexchrate | 汇率值 | numeric | 23 | 10 | √ | 0 | 汇率值 |
| 62 | fcurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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

## 供应商附件-附件表 t_src_purlistentry_supfj

- **表名称：** 供应商附件-附件表
- **表名：** t_src_purlistentry_supfj

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
| 1 | pk_src_purlistentry_supfj |  | fpkid |
| 2 | idx_src_purlistentry_supfj_fid |  | fentryid |
| 3 | idx_src_purlistentry_supfj_bid |  | fbasedataid |
