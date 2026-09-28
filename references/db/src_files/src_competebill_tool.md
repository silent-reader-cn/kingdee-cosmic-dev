# 竞价单(工具)-src_competebill_tool

## 报价分录-子表 t_src_vie_detail

- **表名称：** 报价分录-子表
- **表名：** t_src_vie_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | flocprice | flocprice | numeric | 23 | 10 | √ | 0 |  |
| 7 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 8 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fprotaxamount | fprotaxamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 12 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 13 | fproamount | fproamount | numeric | 23 | 10 | √ | 0 |  |
| 14 | frestofbidcount | frestofbidcount | int4 | 32 |  | √ | 0 |  |
| 15 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 16 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 17 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 18 | fmaxtaxamount | fmaxtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 19 | fispresent | fispresent | bpchar | 1 |  | √ | '0' |  |
| 20 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 22 | fincreaseprice | fincreaseprice | numeric | 23 | 10 | √ | 0 |  |
| 23 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 24 | freducetype | freducetype | varchar | 2 |  | √ | ' ' |  |
| 25 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 26 | freduceamt | freduceamt | numeric | 23 | 10 | √ | 0 |  |
| 27 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 28 | fpkgrank | fpkgrank | int4 | 32 |  | √ | 0 |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 31 | frank | frank | int4 | 32 |  | √ | 0 |  |
| 32 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fmaxtaxprice | fmaxtaxprice | numeric | 23 | 10 | √ | 0 |  |
| 34 | fviediffer | fviediffer | numeric | 23 | 10 | √ | 0 |  |
| 35 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | 'A' |  |
| 36 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | flocquoteamt | 本币报价金额 | numeric | 23 | 10 | √ | 0 | 本币报价金额 |
| 38 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0 |  |
| 39 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 41 | fmaxprice | fmaxprice | numeric | 23 | 10 | √ | 0 |  |
| 42 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 43 | fcostdetail | fcostdetail | bpchar | 1 |  | √ | '0' |  |
| 44 | fpkgamount | fpkgamount | numeric | 23 | 10 | √ | 0 |  |
| 45 | fexchange | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 46 | fvieratio | fvieratio | numeric | 23 | 10 | √ | 0 |  |
| 47 | fviefrom | fviefrom | numeric | 23 | 10 | √ | 0 |  |
| 48 | fturns | fturns | varchar | 2 |  | √ | ' ' |  |
| 49 | fpkgtaxamount | fpkgtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | floctaxamount | floctaxamount | numeric | 23 | 10 | √ | 0 |  |
| 51 | fvieto | fvieto | numeric | 23 | 10 | √ | 0 |  |
| 52 | fvieturns | fvieturns | varchar | 2 |  | √ | ' ' |  |
| 53 | fquotedate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 54 | floctaxprice | floctaxprice | numeric | 23 | 10 | √ | 0 |  |
| 55 | fquoteamt | 报价金额 | numeric | 23 | 10 | √ | 0 | 报价金额 |
| 56 | ftaxitemid | ftaxitemid | int8 | 64 |  | √ | 0 |  |
| 57 | flocamount | flocamount | numeric | 23 | 10 | √ | 0 |  |
| 58 | flocreduceamt | flocreduceamt | numeric | 23 | 10 | √ | 0 |  |
| 59 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 60 | fprorank | fprorank | int4 | 32 |  | √ | 0 |  |
| 61 | fexchrate | fexchrate | numeric | 23 | 10 | √ | 0 |  |
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

## 竞价轮次分录-子表 t_src_vie_turns

- **表名称：** 竞价轮次分录-子表
- **表名：** t_src_vie_turns

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 来源分录ID(竞价计划ID) | int8 | 64 |  | √ | 0 | 来源分录ID(竞价计划ID) |
| 3 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :报名中 B :准备竞价 C :竞价中 D :评标中 E :已定标 F :已执行 G :已废弃 H :已暂停 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbidtimes | 竞价时长(分钟) | int4 | 32 |  | √ | 0 | 竞价时长(分钟) |
| 6 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) |
| 7 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 8 | fbidtime | fbidtime | timestamp | 0 |  |  | null |  |
| 9 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) |
| 10 | fopen4 | 竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | '0' | 竞价大厅隐藏供应商报价 |
| 11 | flasttime | 最后几分钟如果价格有变化则补计时 | int4 | 32 |  | √ | 0 | 最后几分钟如果价格有变化则补计时 |
| 12 | fopen2 | 竞价大厅显示竞价排名 | bpchar | 1 |  | √ | '0' | 竞价大厅显示竞价排名 |
| 13 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 14 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 15 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | '0' | 竞价开始时间到达时自动启动竞价 |
| 16 | fopen1 | 竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | '0' | 竞价大厅隐藏供应商名称 |
| 17 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 18 | fsrcbillid | 来源单据ID(如议价单ID) | int8 | 64 |  | √ | 0 | 来源单据ID(如议价单ID) |
| 19 | fopendate | 竞价开始时间 | timestamp | 0 |  |  | null | 竞价开始时间 |
| 20 | fbidcount | 最多报价次数 | int4 | 32 |  | √ | 0 | 最多报价次数 |
| 21 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 22 | fwinerqty | 中标供应商数量 | int4 | 32 |  | √ | 0 | 中标供应商数量 |
| 23 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 24 | fturnsenddate | 竞价结束时间 | timestamp | 0 |  |  | null | 竞价结束时间 |
| 25 | freducetype | 调价方式 | bpchar | 1 |  | √ | ' ' | 调价方式,枚举: A :按比例 B :按金额 |
| 26 | fdelaytime | 补计时时长(分钟) | int4 | 32 |  | √ | 0 | 补计时时长(分钟) |
| 27 | fbidnumber | 参与竞价至少应有几家 | int4 | 32 |  | √ | 0 | 参与竞价至少应有几家 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fisdiscarded | 是否进行弃标的控制 | bpchar | 1 |  | √ | '0' | 是否进行弃标的控制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_vie_turns_fid |  | fid |
| 2 | idx_src_vie_turns_turn |  | fturns |
| 3 | idx_src_vie_turns_vietrurn |  | fvieturns |
| 4 | pk_src_vie_turns |  | fentryid |

---

## 竞价计划分录-子表 t_src_vie_turns2

- **表名称：** 竞价计划分录-子表
- **表名：** t_src_vie_turns2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :未开始 B :已执行 C :已关闭 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbidtimes | 竞价时长(分钟) | int4 | 32 |  | √ | 0 | 竞价时长(分钟) |
| 5 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) |
| 6 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 7 | fbidtime | fbidtime | int4 | 32 |  | √ | 0 |  |
| 8 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) |
| 9 | fopen4 | 竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | '0' | 竞价大厅隐藏供应商报价 |
| 10 | flasttime | 最后几分钟如果价格有变化则补计时 | int4 | 32 |  | √ | 0 | 最后几分钟如果价格有变化则补计时 |
| 11 | fopen2 | 竞价大厅显示竞价排名 | bpchar | 1 |  | √ | '0' | 竞价大厅显示竞价排名 |
| 12 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 13 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 14 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | '0' | 竞价开始时间到达时自动启动竞价 |
| 15 | fopen1 | 竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | '0' | 竞价大厅隐藏供应商名称 |
| 16 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 17 | fsrcbillid | 来源单据ID(如议价单ID) | int8 | 64 |  | √ | 0 | 来源单据ID(如议价单ID) |
| 18 | fopendate | 竞价开始时间 | timestamp | 0 |  |  | null | 竞价开始时间 |
| 19 | fbidcount | 最多报价次数 | int4 | 32 |  | √ | 0 | 最多报价次数 |
| 20 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 21 | fwinerqty | 中标供应商数量 | int4 | 32 |  | √ | 0 | 中标供应商数量 |
| 22 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 23 | freducetype | 调价方式 | bpchar | 1 |  | √ | '0' | 调价方式,枚举: A :按比例 B :按金额 |
| 24 | fdelaytime | 补计时时长(分钟) | int4 | 32 |  | √ | 0 | 补计时时长(分钟) |
| 25 | fbidnumber | 参与竞价至少应有几家 | int4 | 32 |  | √ | 0 | 参与竞价至少应有几家 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fisdiscarded | 是否进行弃标的控制 | bpchar | 1 |  | √ | '0' | 是否进行弃标的控制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_vie_turns2_turn |  | fturns |
| 2 | pk_src_vie_turns2 |  | fentryid |
| 3 | idx_src_vie_turns2_fid |  | fid |
| 4 | idx_src_vie_turns2_vietrurn |  | fvieturns |

---

## 竞价单(工具)-主表 t_src_project

- **表名称：** 竞价单(工具)-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | 未税总价 | numeric | 23 | 10 | √ | 0 | 未税总价 |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | 寻源项目编号 | varchar | 30 |  | √ | ' ' | 寻源项目编号 |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | 中标供应商数量 | int8 | 64 |  | √ | 0 | 中标供应商数量 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | 是否发布竞价 | bpchar | 1 |  | √ | '0' | 是否发布竞价 |
| 41 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 42 | fdecidedate | fdecidedate | timestamp | 0 |  |  | null |  |
| 43 | fbilldate | 招标时间 | timestamp | 0 |  |  | null | 招标时间 |
| 44 | fwinruleid | fwinruleid | int8 | 64 |  | √ | 0 |  |
| 45 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 46 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsystype | fsystype | bpchar | 1 |  | √ | '1' |  |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 54 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 55 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 58 | fopenstatus | 开标状态 | bpchar | 1 |  | √ | '1' | 开标状态,枚举: 1 :待开标 2 :已开技术标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 59 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 60 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 61 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | 是否发布招标 | bpchar | 1 |  | √ | '0' | 是否发布招标 |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | 含税总价 | numeric | 23 | 10 | √ | 0 | 含税总价 |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 80 | fratiotype | fratiotype | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_sourceid |  | fsourceid |
| 2 | idx_src_project_parentid |  | fparentid |
| 3 | pk_src_project |  | fid |
| 4 | idx_src_project_sourceclassid |  | fsourceclassid |
| 5 | idx_src_project_status |  | fopenstatus |
| 6 | idx_src_project_type |  | fsrctypeid |

---

## 竞价单(工具)-多语言表 t_src_project_l

- **表名称：** 竞价单(工具)-多语言表
- **表名：** t_src_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | fnodename | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbidname | 寻源项目名称 | varchar | 300 |  | √ | ' ' | 寻源项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_l_flocaleid |  | flocaleid,fid |
| 2 | pk__src_project_l |  | fpkid |

---

## 竞价单(工具)-分表 t_src_project_o

- **表名称：** 竞价单(工具)-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :待报名 B :竞争准备 C :竞价中 D :评标中 E :待执行 F :已执行 G :已终止 H :已暂停 |
| 3 | frankprice | 竞价大厅单价排名字段 | varchar | 30 |  | √ | ' ' | 竞价大厅单价排名字段,枚举: |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fcashdeposit | 竞价保证金 | numeric | 23 | 10 | √ | 0 | 竞价保证金 |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fchecktype | 资审方式 | bpchar | 1 |  | √ | ' ' | 资审方式,枚举: 1 :资格预审 2 :资格后审 3 :资格免审 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fplanopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 10 | fenddate | 竞价结束时间 | timestamp | 0 |  |  | null | 竞价结束时间 |
| 11 | frankamount | 竞价大厅金额排名字段 | varchar | 30 |  | √ | ' ' | 竞价大厅金额排名字段,枚举: |
| 12 | faddtime | 累计补计时(分钟) | int8 | 64 |  | √ | 0 | 累计补计时(分钟) |
| 13 | fbidtime | 竞价时长(分钟) | int8 | 64 |  | √ | 0 | 竞价时长(分钟) |
| 14 | flasttime | 最后几分钟如果价格有变化则补计时 | int8 | 64 |  | √ | 0 | 最后几分钟如果价格有变化则补计时 |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fviepattern | 竞价模式 | bpchar | 1 |  | √ | ' ' | 竞价模式,枚举: 1 :按单价竞价 2 :按比率竞价 3 :按价差竞价 |
| 17 | fresultdate | 预计公布结果时间 | timestamp | 0 |  |  | null | 预计公布结果时间 |
| 18 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 22 | faddtimecount | 累计补计时次数 | int4 | 32 |  | √ | 0 | 累计补计时次数 |
| 23 | fbidcount | 最多报价次数 | int8 | 64 |  | √ | 0 | 最多报价次数 |
| 24 | fbidrestoftime | 竞价剩余时长(毫秒) | int8 | 64 |  | √ | 0 | 竞价剩余时长(毫秒) |
| 25 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 26 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 27 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 28 | fisregioncontrol | 多轮竞价时进行竞价区间控制 | bpchar | 1 |  | √ | ' ' | 多轮竞价时进行竞价区间控制,枚举: 1 :进行竞价区间控制 2 :不进行竞价区间控制 |
| 29 | freducetype | 调价方式 | bpchar | 1 |  | √ | ' ' | 调价方式,枚举: A :按比例(%) B :按金额 |
| 30 | flastquotedate | 最后一次报价时间 | timestamp | 0 |  |  | null | 最后一次报价时间 |
| 31 | fstopbiddate | 补录价格截止时间 | timestamp | 0 |  |  | null | 补录价格截止时间 |
| 32 | fisnewprice | 竞价结果取供应商最新报价 | bpchar | 1 |  | √ | '0' | 竞价结果取供应商最新报价 |
| 33 | fenrolldate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 36 | fisbizscore | fisbizscore | bpchar | 1 |  | √ | '0' |  |
| 37 | fisdiscarded | 是否进行弃标的控制 | bpchar | 1 |  | √ | '0' | 是否进行弃标的控制 |
| 38 | fisnoderank | fisnoderank | bpchar | 1 |  | √ | '0' |  |
| 39 | fmaxamount | 报价最高限额 | numeric | 23 | 10 | √ | 0 | 报价最高限额 |
| 40 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :竞价中 C :已竞价 D :已终止 E :已暂停 Z :无需处理 |
| 41 | famount | 竞价基准金额(含税) | numeric | 23 | 10 | √ | 0 | 竞价基准金额(含税) |
| 42 | fisautoviebyplan | 是否按竞价计划自动启动竞价 | bpchar | 1 |  | √ | '0' | 是否按竞价计划自动启动竞价 |
| 43 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 44 | fpauseamt | 竞价暂停最新报价 | numeric | 23 | 10 | √ | 0 | 竞价暂停最新报价 |
| 45 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 46 | fopen4 | 采购方竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅隐藏供应商报价 |
| 47 | fopen2 | 供应商竞价大厅显示竞价排名 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅显示竞价排名 |
| 48 | fpausetime | 竞价暂停时间 | timestamp | 0 |  |  | null | 竞价暂停时间 |
| 49 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 50 | fopen3 | 竞价后公布胜出公司 | bpchar | 1 |  | √ | ' ' | 竞价后公布胜出公司 |
| 51 | fsumtype | 竞价大厅排名方式 | bpchar | 1 |  | √ | ' ' | 竞价大厅排名方式,枚举: |
| 52 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | ' ' | 竞价开始时间到达时自动启动竞价 |
| 53 | fopen1 | 采购方竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅隐藏供应商名称 |
| 54 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 55 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 56 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 57 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 58 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 59 | fopendate | 实际竞价开始时间(后台字段) | timestamp | 0 |  |  | null | 实际竞价开始时间(后台字段) |
| 60 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 61 | fminamount | 报价最低限额 | numeric | 23 | 10 | √ | 0 | 报价最低限额 |
| 62 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 63 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 64 | fvietype | 竞价类型 | bpchar | 1 |  | √ | ' ' | 竞价类型,枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 65 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 66 | fdelaytime | 补计时时长(分钟) | int8 | 64 |  | √ | 0 | 补计时时长(分钟) |
| 67 | fbidnumber | 参与竞价至少应有几家 | int8 | 64 |  | √ | 0 | 参与竞价至少应有几家 |
| 68 | fopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 69 | fpausestarttime | 竞价暂停开始时间 | timestamp | 0 |  |  | null | 竞价暂停开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_o_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_o |  | fid |
