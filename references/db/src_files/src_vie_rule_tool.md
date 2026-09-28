# 竞价规则(工具)-src_vie_rule_tool

## 竞价轮次分录-子表 t_src_vie_turns

- **表名称：** 竞价轮次分录-子表
- **表名：** t_src_vie_turns

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 来源分录ID(竞价计划ID) | int8 | 64 |  | √ | 0 | 来源分录ID(竞价计划ID) |
| 3 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :报名中 B :竞价准备 C :竞价中 D :竞价结束 E :已完成 F :已执行 G :已作废 H :已暂停 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbidtimes | 预计竞价时长(分钟) | int4 | 32 |  | √ | 0 | 预计竞价时长(分钟) |
| 6 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 7 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 8 | fbidtime | fbidtime | timestamp | 0 |  |  | null |  |
| 9 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) |
| 10 | fopen4 | 采购方竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | '0' | 采购方竞价大厅隐藏供应商报价 |
| 11 | flasttime | 最后几分钟价格变化补计时(分钟) | int4 | 32 |  | √ | 0 | 最后几分钟价格变化补计时(分钟) |
| 12 | fopen2 | 供应商竞价大厅显示竞价排名 | bpchar | 1 |  | √ | '0' | 供应商竞价大厅显示竞价排名 |
| 13 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 14 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 15 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | '0' | 竞价开始时间到达时自动启动竞价 |
| 16 | fopen1 | 采购方竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | '0' | 采购方竞价大厅隐藏供应商名称 |
| 17 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 18 | fsrcbillid | 来源单据ID(如议价单ID) | int8 | 64 |  | √ | 0 | 来源单据ID(如议价单ID) |
| 19 | fopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 20 | fbidcount | 最多报价次数 | int4 | 32 |  | √ | 0 | 最多报价次数 |
| 21 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 22 | fwinerqty | 中标供应商数量 | int4 | 32 |  | √ | 0 | 中标供应商数量 |
| 23 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 24 | fturnsenddate | 实际竞价结束时间 | timestamp | 0 |  |  | null | 实际竞价结束时间 |
| 25 | freducetype | 每次调价方式 | bpchar | 1 |  | √ | ' ' | 每次调价方式,枚举: A :按比例(%) B :按金额 |
| 26 | fdelaytime | 补计时时长(分钟) | int4 | 32 |  | √ | 0 | 补计时时长(分钟) |
| 27 | fbidnumber | 竞价最低参与供应商数量 | int4 | 32 |  | √ | 0 | 竞价最低参与供应商数量 |
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
| 2 | fbidstatus | 计划状态 | bpchar | 1 |  | √ | ' ' | 计划状态,枚举: A :未开始 B :竞价准备 C :竞价中 D :竞价结束 E :已完成 F :已执行 G :已作废 H :已暂停 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbidtimes | 计划竞价时长(分钟) | int4 | 32 |  | √ | 0 | 计划竞价时长(分钟) |
| 5 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 6 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 7 | fbidtime | fbidtime | int4 | 32 |  | √ | 0 |  |
| 8 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) |
| 9 | fopen4 | 采购方竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | '0' | 采购方竞价大厅隐藏供应商报价 |
| 10 | flasttime | 最后几分钟价格变化补计时(分钟) | int4 | 32 |  | √ | 0 | 最后几分钟价格变化补计时(分钟) |
| 11 | fopen2 | 供应商竞价大厅显示竞价排名 | bpchar | 1 |  | √ | '0' | 供应商竞价大厅显示竞价排名 |
| 12 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 13 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 14 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | '0' | 竞价开始时间到达时自动启动竞价 |
| 15 | fopen1 | 采购方竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | '0' | 采购方竞价大厅隐藏供应商名称 |
| 16 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 17 | fsrcbillid | 来源单据ID(如议价单ID) | int8 | 64 |  | √ | 0 | 来源单据ID(如议价单ID) |
| 18 | fopendate | 计划竞价开始时间 | timestamp | 0 |  |  | null | 计划竞价开始时间 |
| 19 | fbidcount | 最多报价次数 | int4 | 32 |  | √ | 0 | 最多报价次数 |
| 20 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 21 | fwinerqty | 中标供应商数量 | int4 | 32 |  | √ | 0 | 中标供应商数量 |
| 22 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 23 | freducetype | 每次调价方式 | bpchar | 1 |  | √ | '0' | 每次调价方式,枚举: A :按比例(%) B :按金额 |
| 24 | fdelaytime | 补计时时长(分钟) | int4 | 32 |  | √ | 0 | 补计时时长(分钟) |
| 25 | fbidnumber | 竞价最低参与供应商数量 | int4 | 32 |  | √ | 0 | 竞价最低参与供应商数量 |
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

## 竞价规则(工具)-主表 t_src_project

- **表名称：** 竞价规则(工具)-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
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
| 33 | fruleassess | 商务报价计算规则（招标） | bpchar | 1 |  | √ | ' ' | 商务报价计算规则（招标）,枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 41 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 42 | fdecidedate | fdecidedate | timestamp | 0 |  |  | null |  |
| 43 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 44 | fwinruleid | 中标原则 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 45 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
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
| 58 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 59 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 60 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 61 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 70 | fratio_biz | 商务标占比(%) | numeric | 23 | 10 | √ | 0 | 商务标占比(%) |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 76 | fextfilterid | 自动议价筛选方案 | int8 | 64 |  | √ | 0 | [扩展过滤 pds_extfilter](../pds_files/pds_extfilter.md) |
| 77 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 80 | fratiotype | 定标份额分配方式 | bpchar | 1 |  | √ | '1' | 定标份额分配方式,枚举: 1 :手工分配份额 2 :自动分配份额(按项目) 3 :自动分配份额(按标段) 4 :自动分配份额(按标的) 9 :不需要份额分配与控制 |

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

## 竞价规则(工具)-分表 t_src_project_q

- **表名称：** 竞价规则(工具)-分表
- **表名：** t_src_project_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispkgscheme | fispkgscheme | bpchar | 1 |  | √ | '0' |  |
| 3 | fismanualscore | fismanualscore | bpchar | 1 |  | √ | '0' |  |
| 4 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fschemeid | 推荐方案 | int8 | 64 |  | √ | 0 | [推荐方案 src_pattern](../src_files/src_pattern.md) |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fnegschemeid | 议价管控方案 | int8 | 64 |  | √ | 0 | [议价管控方案 src_negscheme](../src_files/src_negscheme.md) |
| 11 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 12 | fremark | 综合计算备注 | varchar | 510 |  | √ | ' ' | 综合计算备注 |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 15 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 16 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 18 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | ftendency | ftendency | varchar | 50 |  | √ | ' ' |  |
| 23 | fbasescore | fbasescore | numeric | 23 | 10 | √ | 0 |  |
| 24 | fminscore | fminscore | numeric | 23 | 10 | √ | 0 |  |
| 25 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 26 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 27 | ftopsupplier | 前几名供应商 | int8 | 64 |  | √ | 1 | 前几名供应商 |
| 28 | fnegotiaterule | 议价规则（范围） | bpchar | 1 |  | √ | ' ' | 议价规则（范围）,枚举: 1 :预中标供应商 2 :前几名供应商 3 :投标供应商 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_q_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_q |  | fid |

---

## 竞价规则(工具)-分表 t_src_project_o

- **表名称：** 竞价规则(工具)-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :报名中 B :竞价准备 C :竞价中 D :竞价结束 E :已完成 F :已执行 G :已作废 H :已暂停 报名截止 :I |
| 3 | frankprice | 竞价大厅单价排名字段 | varchar | 30 |  | √ | ' ' | 竞价大厅单价排名字段,枚举: locprice :本币未税单价 loctaxprice :本币含税单价 |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fcashdeposit | 竞价保证金 | numeric | 23 | 10 | √ | 0 | 竞价保证金 |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fplanopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 10 | fenddate | 实际竞价结束时间 | timestamp | 0 |  |  | null | 实际竞价结束时间 |
| 11 | frankamount | 竞价大厅金额排名字段 | varchar | 30 |  | √ | ' ' | 竞价大厅金额排名字段,枚举: locamount :本币未税金额 loctaxamount :本币价税合计 |
| 12 | faddtime | 累计补计时(分钟) | int8 | 64 |  | √ | 0 | 累计补计时(分钟) |
| 13 | fbidtime | 竞价时长(分钟) | int8 | 64 |  | √ | 0 | 竞价时长(分钟) |
| 14 | flasttime | 最后几分钟价格变化补计时(分钟) | int8 | 64 |  | √ | 0 | 最后几分钟价格变化补计时(分钟) |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fviepattern | 竞价模式 | bpchar | 1 |  | √ | ' ' | 竞价模式,枚举: 1 :按单价竞价 2 :按比率竞价 3 :按价差竞价 |
| 17 | fresultdate | 公布结果时间 | timestamp | 0 |  |  | null | 公布结果时间 |
| 18 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 20 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 22 | faddtimecount | 累计补计时次数 | int4 | 32 |  | √ | 0 | 累计补计时次数 |
| 23 | fbidcount | 最多报价次数 | int8 | 64 |  | √ | 0 | 最多报价次数 |
| 24 | fbidrestoftime | 竞价剩余时长(毫秒) | int8 | 64 |  | √ | 0 | 竞价剩余时长(毫秒) |
| 25 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 26 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 27 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 28 | fisregioncontrol | 多轮竞价时进行竞价区间控制 | bpchar | 1 |  | √ | ' ' | 多轮竞价时进行竞价区间控制,枚举: 1 :进行竞价区间控制 2 :不进行竞价区间控制 |
| 29 | freducetype | 每次调价方式 | bpchar | 1 |  | √ | ' ' | 每次调价方式,枚举: A :按比例(%) B :按金额 |
| 30 | flastquotedate | 最后一次报价时间 | timestamp | 0 |  |  | null | 最后一次报价时间 |
| 31 | fstopbiddate | 补录价格截止时间 | timestamp | 0 |  |  | null | 补录价格截止时间 |
| 32 | fisnewprice | 竞价结果取最新报价 | bpchar | 1 |  | √ | '0' | 竞价结果取最新报价 |
| 33 | fenrolldate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 36 | fisbizscore | fisbizscore | bpchar | 1 |  | √ | '0' |  |
| 37 | fisdiscarded | 是否进行弃标的控制 | bpchar | 1 |  | √ | '0' | 是否进行弃标的控制 |
| 38 | fisnoderank | fisnoderank | bpchar | 1 |  | √ | '0' |  |
| 39 | fmaxamount | 报价最高限额 | numeric | 23 | 10 | √ | 0 | 报价最高限额 |
| 40 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
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
| 51 | fsumtype | 竞价大厅汇总排名方式 | bpchar | 1 |  | √ | ' ' | 竞价大厅汇总排名方式,枚举: 1 :按供应商汇总排名 2 :按供应商+标段汇总排名 |
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
| 67 | fbidnumber | 竞价最低参与供应商数量 | int8 | 64 |  | √ | 0 | 竞价最低参与供应商数量 |
| 68 | fopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 69 | fpausestarttime | 竞价暂停后重启时间 | timestamp | 0 |  |  | null | 竞价暂停后重启时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_o_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_o |  | fid |

---

## 份额分配比率-子表 t_src_ruleentry

- **表名称：** 份额分配比率-子表
- **表名：** t_src_ruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderratio06 | 第六名份额(%) | numeric | 23 | 10 | √ | 0 | 第六名份额(%) |
| 3 | ftrainqty | 培养供应商数 | int4 | 32 |  | √ | 0 | 培养供应商数 |
| 4 | forderratio05 | 第五名份额(%) | numeric | 23 | 10 | √ | 0 | 第五名份额(%) |
| 5 | forderratio08 | 第八名份额(%) | numeric | 23 | 10 | √ | 0 | 第八名份额(%) |
| 6 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 7 | forderratio07 | 第七名份额(%) | numeric | 23 | 10 | √ | 0 | 第七名份额(%) |
| 8 | forderratio09 | 第九名份额(%) | numeric | 23 | 10 | √ | 0 | 第九名份额(%) |
| 9 | falterqty | 备选供应商数 | int4 | 32 |  | √ | 0 | 备选供应商数 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fwinerqty | 中标供应商数 | int4 | 32 |  | √ | 0 | 中标供应商数 |
| 12 | forderratio10 | 第十名份额(%) | numeric | 23 | 10 | √ | 0 | 第十名份额(%) |
| 13 | fpurlistid | 标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 14 | forderratio02 | 第二名份额(%) | numeric | 23 | 10 | √ | 0 | 第二名份额(%) |
| 15 | forderratio01 | 第一名份额(%) | numeric | 23 | 10 | √ | 0 | 第一名份额(%) |
| 16 | forderratio04 | 第四名份额(%) | numeric | 23 | 10 | √ | 0 | 第四名份额(%) |
| 17 | forderratio03 | 第三名份额(%) | numeric | 23 | 10 | √ | 0 | 第三名份额(%) |
| 18 | fsurplusratio | 剩余份额分配方式 | bpchar | 1 |  | √ | '1' | 剩余份额分配方式,枚举: 1 :分配给第一名供应商 2 :按中标供应商份额权重分摊 3 :在中标供应商间平均分摊 9 :不需要处理 |
| 19 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 20 | forderratio | 份额合计(%) | numeric | 23 | 10 | √ | 0 | 份额合计(%) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_ruleentry |  | fentryid |
| 2 | idx_src_ruleentry_fid |  | fid |
| 3 | idx_src_ruleentry_pid |  | fprojectid |
