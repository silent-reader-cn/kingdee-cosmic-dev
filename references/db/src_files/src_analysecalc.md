# 重新计算-src_analysecalc

## 比价设置分录-子表 t_src_compare_set

- **表名称：** 比价设置分录-子表
- **表名：** t_src_compare_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fpkgschemeid | 比价方案 | int8 | 64 |  | √ | 0 | [推荐方案 src_pattern](../src_files/src_pattern.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_compare_set |  | fentryid |
| 2 | idx_src_compare_set_sid |  | fpkgschemeid |
| 3 | idx_src_compare_set_fid |  | fid |
| 4 | idx_src_compare_set_pid |  | fpackageid |

---

## 重新计算-主表 t_src_project

- **表名称：** 重新计算-主表
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
| 15 | fisbyproject | 按项目设置评标方案 | bpchar | 1 |  | √ | '0' | 按项目设置评标方案 |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 19 | fratio_oth | 商务综合占比(%) | numeric | 23 | 10 | √ | 0 | 商务综合占比(%) |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | 备选供应商数量 | int8 | 64 |  | √ | 0 | 备选供应商数量 |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | 中标供应商数量 | int8 | 64 |  | √ | 0 | 中标供应商数量 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 33 | fruleassess | 商务报价计算规则 | bpchar | 1 |  | √ | ' ' | 商务报价计算规则,枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
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
| 55 | fismultipackage | 是否包含多标段 | bpchar | 1 |  | √ | '0' | 是否包含多标段 |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 58 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 59 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 60 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 61 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | 是否按标段开标 | bpchar | 1 |  | √ | '0' | 是否按标段开标 |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 70 | fratio_biz | 商务标占比(%) | numeric | 23 | 10 | √ | 0 | 商务标占比(%) |
| 71 | fratio_tec | 技术标占比(%) | numeric | 23 | 10 | √ | 0 | 技术标占比(%) |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 76 | fextfilterid | 自动议价筛选方案 | int8 | 64 |  | √ | 0 | [扩展过滤 pds_extfilter](../pds_files/pds_extfilter.md) |
| 77 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
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

## 重新计算-分表 t_src_project_a

- **表名称：** 重新计算-分表
- **表名：** t_src_project_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherruleassess | fotherruleassess | varchar | 255 |  |  | ' ' |  |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 5 | fresult | 推荐结果 | bpchar | 1 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 0 :手工选择，不自动推荐 |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fisbidnotice | fisbidnotice | bpchar | 1 |  | √ | '0' |  |
| 9 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 10 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 11 | fversion | fversion | int8 | 64 |  | √ | 1 |  |
| 12 | famountrange | famountrange | varchar | 50 |  | √ | ' ' |  |
| 13 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsourcestateprint | fsourcestateprint | varchar | 100 |  | √ | ' ' |  |
| 16 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 17 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 18 | fprojectcreatorid | fprojectcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | ' ' |  |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | fotherwinrule | 其他中标原则 | varchar | 255 |  |  | ' ' | 其他中标原则 |
| 24 | fdecisionname | fdecisionname | varchar | 100 |  | √ | ' ' |  |
| 25 | fispaper | fispaper | bpchar | 1 |  | √ | '0' |  |
| 26 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 27 | fissplitdoc | fissplitdoc | bpchar | 1 |  | √ | '0' |  |
| 28 | freasonremark_tag | 独家谈判原因备注_详情 | text | 0 |  |  | null | 独家谈判原因备注_详情 |
| 29 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 30 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 31 | faftertalkrule | 标后谈判原则 | varchar | 255 |  |  | ' ' | 标后谈判原则 |
| 32 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | '0' |  |
| 33 | fsolereason | 独家谈判原因 | bpchar | 1 |  | √ | ' ' | 独家谈判原因,枚举: 1 :供应商资源唯一 2 :合同续签 3 :合同内议价 4 :内部供应商采购 5 :客户指定供应商 9 :其他 |
| 34 | forderrule | 订单分配原则 | varchar | 255 |  | √ | ' ' | 订单分配原则 |
| 35 | freasonremark | 独家谈判原因备注 | varchar | 255 |  | √ | ' ' | 独家谈判原因备注 |
| 36 | fopentypep | fopentypep | varchar | 50 |  | √ | ' ' |  |
| 37 | fdecisionbillno | fdecisionbillno | varchar | 50 |  | √ | ' ' |  |
| 38 | fcontractcycle | fcontractcycle | varchar | 50 |  | √ | ' ' |  |
| 39 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 42 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 43 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 44 | fbidaddress | fbidaddress | varchar | 50 |  | √ | ' ' |  |
| 45 | fsourcestate | fsourcestate | varchar | 30 |  | √ | ' ' |  |
| 46 | fsrcapplyid | fsrcapplyid | int8 | 64 |  | √ | 0 |  |
| 47 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 48 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 49 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 50 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 51 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 52 | fprojectcreatetime | fprojectcreatetime | timestamp | 0 |  |  | null |  |
| 53 | fismustapply | fismustapply | bpchar | 1 |  | √ | '0' |  |
| 54 | fdiscardrule | 废标原则 | varchar | 255 |  |  | ' ' | 废标原则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_a |  | fid |
| 2 | idx_src_project_a_fcreatorid |  | fcreatorid |
| 3 | idx_src_project_a_fsrcapplyid |  | fsrcapplyid |

---

## 重新计算-分表 t_src_project_q

- **表名称：** 重新计算-分表
- **表名：** t_src_project_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispkgscheme | 按标段设置比价方案 | bpchar | 1 |  | √ | '0' | 按标段设置比价方案 |
| 3 | fismanualscore | 手工录入商务得分 | bpchar | 1 |  | √ | '0' | 手工录入商务得分 |
| 4 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fschemeid | 推荐方案 | int8 | 64 |  | √ | 0 | [推荐方案 src_pattern](../src_files/src_pattern.md) |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fnegschemeid | 议价管控方案 | int8 | 64 |  | √ | 0 | [议价管控方案 src_negscheme](../src_files/src_negscheme.md) |
| 11 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 12 | fremark | 系统自动计算结果及异常信息提示 | varchar | 510 |  | √ | ' ' | 系统自动计算结果及异常信息提示 |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 15 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 16 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 18 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | ftendency | 报价趋势 | varchar | 50 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 23 | fbasescore | 基准商务得分 | numeric | 23 | 10 | √ | 0 | 基准商务得分 |
| 24 | fminscore | 最低商务得分 | numeric | 23 | 10 | √ | 0 | 最低商务得分 |
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

## 重新计算-分表 t_src_project_o

- **表名称：** 重新计算-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | fbidstatus | bpchar | 1 |  | √ | ' ' |  |
| 3 | frankprice | frankprice | varchar | 30 |  | √ | ' ' |  |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fcashdeposit | fcashdeposit | numeric | 23 | 10 | √ | 0 |  |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fplanopendate | fplanopendate | timestamp | 0 |  |  | null |  |
| 10 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 11 | frankamount | frankamount | varchar | 30 |  | √ | ' ' |  |
| 12 | faddtime | faddtime | int8 | 64 |  | √ | 0 |  |
| 13 | fbidtime | fbidtime | int8 | 64 |  | √ | 0 |  |
| 14 | flasttime | flasttime | int8 | 64 |  | √ | 0 |  |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fviepattern | fviepattern | bpchar | 1 |  | √ | ' ' |  |
| 17 | fresultdate | fresultdate | timestamp | 0 |  |  | null |  |
| 18 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 20 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 22 | faddtimecount | faddtimecount | int4 | 32 |  | √ | 0 |  |
| 23 | fbidcount | fbidcount | int8 | 64 |  | √ | 0 |  |
| 24 | fbidrestoftime | fbidrestoftime | int8 | 64 |  | √ | 0 |  |
| 25 | ftendency | ftendency | bpchar | 1 |  | √ | ' ' |  |
| 26 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 27 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 28 | fisregioncontrol | fisregioncontrol | bpchar | 1 |  | √ | ' ' |  |
| 29 | freducetype | freducetype | bpchar | 1 |  | √ | ' ' |  |
| 30 | flastquotedate | flastquotedate | timestamp | 0 |  |  | null |  |
| 31 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 32 | fisnewprice | fisnewprice | bpchar | 1 |  | √ | '0' |  |
| 33 | fenrolldate | fenrolldate | timestamp | 0 |  |  | null |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 36 | fisbizscore | 需要专家评商务分 | bpchar | 1 |  | √ | '0' | 需要专家评商务分 |
| 37 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 38 | fisnoderank | fisnoderank | bpchar | 1 |  | √ | '0' |  |
| 39 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 41 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fisautoviebyplan | fisautoviebyplan | bpchar | 1 |  | √ | '0' |  |
| 43 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 44 | fpauseamt | fpauseamt | numeric | 23 | 10 | √ | 0 |  |
| 45 | freducepct | freducepct | numeric | 23 | 10 | √ | 0 |  |
| 46 | fopen4 | fopen4 | bpchar | 1 |  | √ | ' ' |  |
| 47 | fopen2 | fopen2 | bpchar | 1 |  | √ | ' ' |  |
| 48 | fpausetime | fpausetime | timestamp | 0 |  |  | null |  |
| 49 | fsubmittype | fsubmittype | bpchar | 1 |  | √ | ' ' |  |
| 50 | fopen3 | fopen3 | bpchar | 1 |  | √ | ' ' |  |
| 51 | fsumtype | fsumtype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fautoconfirm | fautoconfirm | bpchar | 1 |  | √ | ' ' |  |
| 53 | fopen1 | fopen1 | bpchar | 1 |  | √ | ' ' |  |
| 54 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 55 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 56 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 57 | fvie_purlist | fvie_purlist | bpchar | 1 |  | √ | ' ' |  |
| 58 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 59 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 60 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 61 | fminamount | fminamount | numeric | 23 | 10 | √ | 0 |  |
| 62 | faddtimenum | faddtimenum | int4 | 32 |  | √ | 0 |  |
| 63 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 64 | fvietype | 竞价类型 | bpchar | 1 |  | √ | ' ' | 竞价类型,枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 65 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 66 | fdelaytime | fdelaytime | int8 | 64 |  | √ | 0 |  |
| 67 | fbidnumber | fbidnumber | int8 | 64 |  | √ | 0 |  |
| 68 | fopinion | fopinion | varchar | 255 |  | √ | ' ' |  |
| 69 | fpausestarttime | fpausestarttime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_o_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_o |  | fid |
