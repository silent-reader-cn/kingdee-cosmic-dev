# 竞价规则-src_vie_rule

## 竞价轮次分录-子表 t_src_vie_turns

- **表名称：** 竞价轮次分录-子表
- **表名：** t_src_vie_turns

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :报名中 B :竞价准备 C :竞价中 D :竞价结束 E :已完成 F :已执行 G :已作废 H :已暂停 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbidtimes | 竞价时长(分钟) | int4 | 32 |  | √ | 0 | 竞价时长(分钟) |
| 5 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 6 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 7 | fbidtime | fbidtime | timestamp | 0 |  |  | null |  |
| 8 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) |
| 9 | fopen4 | 采购方竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | '0' | 采购方竞价大厅隐藏供应商报价 |
| 10 | flasttime | 最后几分钟价格变化补计时(分钟) | int4 | 32 |  | √ | 0 | 最后几分钟价格变化补计时(分钟) |
| 11 | fopen2 | 供应商竞价大厅显示竞价排名 | bpchar | 1 |  | √ | '0' | 供应商竞价大厅显示竞价排名 |
| 12 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 13 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 14 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | '0' | 竞价开始时间到达时自动启动竞价 |
| 15 | fopen1 | 采购方竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | '0' | 采购方竞价大厅隐藏供应商名称 |
| 16 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 17 | fopendate | 竞价开始时间 | timestamp | 0 |  |  | null | 竞价开始时间 |
| 18 | fbidcount | 最多报价次数 | int4 | 32 |  | √ | 0 | 最多报价次数 |
| 19 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 20 | fwinerqty | 中标供应商数量 | int4 | 32 |  | √ | 0 | 中标供应商数量 |
| 21 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 22 | freducetype | 每次调价方式 | bpchar | 1 |  | √ | ' ' | 每次调价方式,枚举: A :按比例(%) B :按金额 |
| 23 | fdelaytime | 补计时时长(分钟) | int4 | 32 |  | √ | 0 | 补计时时长(分钟) |
| 24 | fbidnumber | 竞价最低参与供应商数量 | int4 | 32 |  | √ | 0 | 竞价最低参与供应商数量 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fisdiscarded | 是否进行弃标的控制 | bpchar | 1 |  | √ | '0' | 是否进行弃标的控制 |

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

## 竞价规则-主表 t_src_project

- **表名称：** 竞价规则-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
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
| 44 | fwinruleid | 中标原则 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 45 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 46 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 47 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 48 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 50 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 51 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 52 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 53 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 54 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 55 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 56 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 57 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 58 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 59 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 60 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 61 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 62 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 63 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 64 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 65 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 66 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 67 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 68 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 69 | fratio_biz | 商务标占比(%) | numeric | 23 | 10 | √ | 0 | 商务标占比(%) |
| 70 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 71 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 72 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 73 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 74 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 75 | fextfilterid | 自动议价筛选方案 | int8 | 64 |  | √ | 0 | 扩展过滤 pds_extfilter |
| 76 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 77 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 78 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 79 | fratiotype | 定标份额分配方式 | bpchar | 1 |  | √ | '1' | 定标份额分配方式,枚举: 1 :手工分配份额 2 :自动分配份额(按项目) 3 :自动分配份额(按标段) 4 :自动分配份额(按标的) 9 :不需要份额分配与控制 |

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
| 4 | idx_src_project_type |  | fsrctypeid |
| 5 | idx_src_project_sourceclassid |  | fsourceclassid |
| 6 | idx_src_project_status |  | fopenstatus |

---

## 竞价规则-分表 t_src_project_q

- **表名称：** 竞价规则-分表
- **表名：** t_src_project_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispkgscheme | fispkgscheme | bpchar | 1 |  | √ | '0' |  |
| 3 | fismanualscore | fismanualscore | bpchar | 1 |  | √ | '0' |  |
| 4 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fschemeid | 推荐方案 | int8 | 64 |  | √ | 0 | 推荐方案 src_pattern |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fnegschemeid | 议价管控方案 | int8 | 64 |  | √ | 0 | 议价管控方案 src_negscheme |
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

## 竞价规则-分表 t_src_project_o

- **表名称：** 竞价规则-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :报名中 B :竞价准备 C :竞价中 D :竞价结束 E :已完成 F :已执行 G :已作废 H :已暂停 I :报名截止 |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fcashdeposit | 竞价保证金 | numeric | 23 | 10 | √ | 0 | 竞价保证金 |
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fplanopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 9 | faddtime | 累计补计时(分钟) | int8 | 64 |  | √ | 0 | 累计补计时(分钟) |
| 10 | fbidtime | 竞价时长(分钟) | int8 | 64 |  | √ | 0 | 竞价时长(分钟) |
| 11 | flasttime | 最后几分钟价格变化补计时(分钟) | int8 | 64 |  | √ | 0 | 最后几分钟价格变化补计时(分钟) |
| 12 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 13 | fviepattern | 竞价模式 | bpchar | 1 |  | √ | ' ' | 竞价模式,枚举: 1 :按单价竞价 2 :按比率竞价 3 :按价差竞价 |
| 14 | fresultdate | 公布结果时间 | timestamp | 0 |  |  | null | 公布结果时间 |
| 15 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 17 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 18 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 19 | faddtimecount | 累计补计时次数 | int4 | 32 |  | √ | 0 | 累计补计时次数 |
| 20 | fbidcount | 最多报价次数 | int8 | 64 |  | √ | 0 | 最多报价次数 |
| 21 | fbidrestoftime | 竞价剩余时长(毫秒) | int8 | 64 |  | √ | 0 | 竞价剩余时长(毫秒) |
| 22 | ftendency | 报价趋势 | bpchar | 1 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 25 | fisregioncontrol | 多轮竞价时进行竞价区间控制 | bpchar | 1 |  | √ | ' ' | 多轮竞价时进行竞价区间控制,枚举: 1 :进行竞价区间控制 2 :不进行竞价区间控制 |
| 26 | freducetype | 每次调价方式 | bpchar | 1 |  | √ | ' ' | 每次调价方式,枚举: A :按比例(%) B :按金额 |
| 27 | flastquotedate | 最后一次报价时间 | timestamp | 0 |  |  | null | 最后一次报价时间 |
| 28 | fstopbiddate | 补录价格截止时间 | timestamp | 0 |  |  | null | 补录价格截止时间 |
| 29 | fisnewprice | 竞价结果取最新报价 | bpchar | 1 |  | √ | '0' | 竞价结果取最新报价 |
| 30 | fenrolldate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fisbizscore | fisbizscore | bpchar | 1 |  | √ | '0' |  |
| 34 | fisdiscarded | 是否进行弃标的控制 | bpchar | 1 |  | √ | '0' | 是否进行弃标的控制 |
| 35 | fmaxamount | 报价最高限额 | numeric | 23 | 10 | √ | 0 | 报价最高限额 |
| 36 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 37 | famount | 竞价基准金额(含税) | numeric | 23 | 10 | √ | 0 | 竞价基准金额(含税) |
| 38 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 39 | fpauseamt | 竞价暂停最新报价 | numeric | 23 | 10 | √ | 0 | 竞价暂停最新报价 |
| 40 | freducepct | 每次调价幅度 | numeric | 23 | 10 | √ | 0 | 每次调价幅度 |
| 41 | fopen4 | 采购方竞价大厅隐藏供应商报价 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅隐藏供应商报价 |
| 42 | fopen2 | 供应商竞价大厅显示竞价排名 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅显示竞价排名 |
| 43 | fpausetime | 竞价暂停时间 | timestamp | 0 |  |  | null | 竞价暂停时间 |
| 44 | fsubmittype | 供应商竞价大厅报价提交方式 | bpchar | 1 |  | √ | ' ' | 供应商竞价大厅报价提交方式,枚举: 1 :所有分录一起提交 2 :提交选中分录(多选) 3 :提交选中分录(单选) |
| 45 | fopen3 | 竞价后公布胜出公司 | bpchar | 1 |  | √ | ' ' | 竞价后公布胜出公司 |
| 46 | fautoconfirm | 竞价开始时间到达时自动启动竞价 | bpchar | 1 |  | √ | ' ' | 竞价开始时间到达时自动启动竞价 |
| 47 | fopen1 | 采购方竞价大厅隐藏供应商名称 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅隐藏供应商名称 |
| 48 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 49 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 50 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 51 | fvie_purlist | 采购方竞价大厅显示标的 | bpchar | 1 |  | √ | ' ' | 采购方竞价大厅显示标的,枚举: 1 :仅本轮次有报价的标的 2 :所有轮次有报价的标的 3 :所有标的(含无报价) |
| 52 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 53 | fopendate | 实际竞价开始时间(后台字段) | timestamp | 0 |  |  | null | 实际竞价开始时间(后台字段) |
| 54 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 55 | fminamount | 报价最低限额 | numeric | 23 | 10 | √ | 0 | 报价最低限额 |
| 56 | faddtimenum | 每轮最多补计时次数 | int4 | 32 |  | √ | 0 | 每轮最多补计时次数 |
| 57 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 58 | fvietype | 竞价类型 | bpchar | 1 |  | √ | ' ' | 竞价类型,枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 59 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 60 | fdelaytime | 补计时时长(分钟) | int8 | 64 |  | √ | 0 | 补计时时长(分钟) |
| 61 | fbidnumber | 竞价最低参与供应商数量 | int8 | 64 |  | √ | 0 | 竞价最低参与供应商数量 |
| 62 | fopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 63 | fpausestarttime | 竞价暂停开始时间 | timestamp | 0 |  |  | null | 竞价暂停开始时间 |

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
| 6 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
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
| 19 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
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
