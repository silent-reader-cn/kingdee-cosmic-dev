# 重新计算-src_analysecalc

## 比价设置分录-子表 t_src_compare_set

- **表名称：** 比价设置分录-子表
- **表名：** t_src_compare_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fpkgschemeid | 比价方案 | int8 | 64 |  | √ | 0 | 推荐方案 src_pattern |

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
| 54 | fismultipackage | 是否包含多标段 | bpchar | 1 |  | √ | '0' | 是否包含多标段 |
| 55 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 56 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 57 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 58 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 59 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 60 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 61 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 62 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 63 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 64 | fisbypackage | 是否按标段开标 | bpchar | 1 |  | √ | '0' | 是否按标段开标 |
| 65 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 66 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 67 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 68 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 69 | fratio_biz | 商务标占比(%) | numeric | 23 | 10 | √ | 0 | 商务标占比(%) |
| 70 | fratio_tec | 技术标占比(%) | numeric | 23 | 10 | √ | 0 | 技术标占比(%) |
| 71 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 72 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 73 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 74 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 75 | fextfilterid | 自动议价筛选方案 | int8 | 64 |  | √ | 0 | 扩展过滤 pds_extfilter |
| 76 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 77 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 78 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 79 | fratiotype | fratiotype | bpchar | 1 |  | √ | '1' |  |

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
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fisbidnotice | fisbidnotice | bpchar | 1 |  | √ | '0' |  |
| 8 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 9 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 10 | famountrange | famountrange | varchar | 50 |  | √ | ' ' |  |
| 11 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 12 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fsourcestateprint | fsourcestateprint | varchar | 100 |  | √ | ' ' |  |
| 14 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 15 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 16 | fprojectcreatorid | fprojectcreatorid | int8 | 64 |  | √ | 0 |  |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | ' ' |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 21 | fotherwinrule | 其他中标原则 | varchar | 255 |  |  | ' ' | 其他中标原则 |
| 22 | fdecisionname | fdecisionname | varchar | 100 |  | √ | ' ' |  |
| 23 | fispaper | fispaper | bpchar | 1 |  | √ | '0' |  |
| 24 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 25 | fissplitdoc | fissplitdoc | bpchar | 1 |  | √ | '0' |  |
| 26 | freasonremark_tag | 独家谈判原因备注_详情 | text | 0 |  |  | null | 独家谈判原因备注_详情 |
| 27 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 28 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 29 | faftertalkrule | 标后谈判原则 | varchar | 255 |  |  | ' ' | 标后谈判原则 |
| 30 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | '0' |  |
| 31 | fsolereason | 独家谈判原因 | bpchar | 1 |  | √ | ' ' | 独家谈判原因,枚举: 1 :供应商资源唯一 2 :合同续签 3 :合同内议价 4 :内部供应商采购 5 :顺丰客户指定供应商 9 :其他 |
| 32 | forderrule | 订单分配原则 | varchar | 255 |  | √ | ' ' | 订单分配原则 |
| 33 | freasonremark | 独家谈判原因备注 | varchar | 255 |  | √ | ' ' | 独家谈判原因备注 |
| 34 | fopentypep | fopentypep | varchar | 50 |  | √ | ' ' |  |
| 35 | fdecisionbillno | fdecisionbillno | varchar | 50 |  | √ | ' ' |  |
| 36 | fcontractcycle | fcontractcycle | varchar | 50 |  | √ | ' ' |  |
| 37 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 38 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 39 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 40 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 41 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 42 | fbidaddress | fbidaddress | varchar | 50 |  | √ | ' ' |  |
| 43 | fsourcestate | fsourcestate | varchar | 30 |  | √ | ' ' |  |
| 44 | fsrcapplyid | fsrcapplyid | int8 | 64 |  | √ | 0 |  |
| 45 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 46 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 47 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 48 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 49 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 50 | fprojectcreatetime | fprojectcreatetime | timestamp | 0 |  |  | null |  |
| 51 | fismustapply | fismustapply | bpchar | 1 |  | √ | '0' |  |
| 52 | fdiscardrule | 废标原则 | varchar | 255 |  |  | ' ' | 废标原则 |

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
| 5 | fschemeid | 推荐方案 | int8 | 64 |  | √ | 0 | 推荐方案 src_pattern |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fnegschemeid | 议价管控方案 | int8 | 64 |  | √ | 0 | 议价管控方案 src_negscheme |
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
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fcashdeposit | fcashdeposit | numeric | 23 | 10 | √ | 0 |  |
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fplanopendate | fplanopendate | timestamp | 0 |  |  | null |  |
| 9 | faddtime | faddtime | int8 | 64 |  | √ | 0 |  |
| 10 | fbidtime | fbidtime | int8 | 64 |  | √ | 0 |  |
| 11 | flasttime | flasttime | int8 | 64 |  | √ | 0 |  |
| 12 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 13 | fviepattern | fviepattern | bpchar | 1 |  | √ | ' ' |  |
| 14 | fresultdate | fresultdate | timestamp | 0 |  |  | null |  |
| 15 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 17 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 18 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 19 | faddtimecount | faddtimecount | int4 | 32 |  | √ | 0 |  |
| 20 | fbidcount | fbidcount | int8 | 64 |  | √ | 0 |  |
| 21 | fbidrestoftime | fbidrestoftime | int8 | 64 |  | √ | 0 |  |
| 22 | ftendency | ftendency | bpchar | 1 |  | √ | ' ' |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 25 | fisregioncontrol | fisregioncontrol | bpchar | 1 |  | √ | ' ' |  |
| 26 | freducetype | freducetype | bpchar | 1 |  | √ | ' ' |  |
| 27 | flastquotedate | flastquotedate | timestamp | 0 |  |  | null |  |
| 28 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 29 | fisnewprice | fisnewprice | bpchar | 1 |  | √ | '0' |  |
| 30 | fenrolldate | fenrolldate | timestamp | 0 |  |  | null |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fisbizscore | 需要专家评商务分 | bpchar | 1 |  | √ | '0' | 需要专家评商务分 |
| 34 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 35 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 37 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 38 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 39 | fpauseamt | fpauseamt | numeric | 23 | 10 | √ | 0 |  |
| 40 | freducepct | freducepct | numeric | 23 | 10 | √ | 0 |  |
| 41 | fopen4 | fopen4 | bpchar | 1 |  | √ | ' ' |  |
| 42 | fopen2 | fopen2 | bpchar | 1 |  | √ | ' ' |  |
| 43 | fpausetime | fpausetime | timestamp | 0 |  |  | null |  |
| 44 | fsubmittype | fsubmittype | bpchar | 1 |  | √ | ' ' |  |
| 45 | fopen3 | fopen3 | bpchar | 1 |  | √ | ' ' |  |
| 46 | fautoconfirm | fautoconfirm | bpchar | 1 |  | √ | ' ' |  |
| 47 | fopen1 | fopen1 | bpchar | 1 |  | √ | ' ' |  |
| 48 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 49 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 50 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 51 | fvie_purlist | fvie_purlist | bpchar | 1 |  | √ | ' ' |  |
| 52 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 53 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 54 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 55 | fminamount | fminamount | numeric | 23 | 10 | √ | 0 |  |
| 56 | faddtimenum | faddtimenum | int4 | 32 |  | √ | 0 |  |
| 57 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 58 | fvietype | 竞价类型 | bpchar | 1 |  | √ | ' ' | 竞价类型,枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 59 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 60 | fdelaytime | fdelaytime | int8 | 64 |  | √ | 0 |  |
| 61 | fbidnumber | fbidnumber | int8 | 64 |  | √ | 0 |  |
| 62 | fopinion | fopinion | varchar | 255 |  | √ | ' ' |  |
| 63 | fpausestarttime | fpausestarttime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_o_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_o |  | fid |
