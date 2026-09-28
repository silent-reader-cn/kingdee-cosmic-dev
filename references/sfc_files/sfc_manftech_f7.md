# 工序计划分录f7(废弃)-sfc_manftech_f7

## 工序计划分录f7(废弃)-分表 t_pom_manftechentry_f

- **表名称：** 工序计划分录f7(废弃)-分表
- **表名：** t_pom_manftechentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprtotalunqualifiedqty | foprtotalunqualifiedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | ftaxrate | ftaxrate | int8 | 64 |  | √ | 0 |  |
| 4 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 5 | fpurchasegroupid | fpurchasegroupid | int8 | 64 |  | √ | 0 |  |
| 6 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 7 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fpushoproutorderbaseqty | fpushoproutorderbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fpushoproutorderqty | fpushoproutorderqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fmachiningtype | 加工类型 | varchar | 30 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 12 | ffloorratio | ffloorratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fpurordernumber | fpurordernumber | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fentrymaterialid | fentrymaterialid | int8 | 64 |  | √ | 0 |  |
| 15 | fentrustrinqty | fentrustrinqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | ftotaldownqty | ftotaldownqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fentrustorderqty | fentrustorderqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fsettlementcoefficient | fsettlementcoefficient | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fpurapplynumber | fpurapplynumber | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | ftotaloproutorderqty | ftotaloproutorderqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fpurchasepersonid | fpurchasepersonid | int8 | 64 |  | √ | 0 |  |
| 23 | fentrustedorderqty | fentrustedorderqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | ftotaloproutorderbaseqty | ftotaloproutorderbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | flockqty | flockqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | fentrustdinqty | fentrustdinqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | fentrustfinqty | fentrustfinqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | fcurrencyfield | fcurrencyfield | int8 | 64 |  | √ | 0 |  |
| 31 | fsettlementunitid | fsettlementunitid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftechentry_f |  | fprocessentryid |
| 2 | idx_pom_manftechentry_f_fid |  | fid |

---

## 工序计划分录f7(废弃)-分表 t_pom_manftechentry_e

- **表名称：** 工序计划分录f7(废弃)-分表
- **表名：** t_pom_manftechentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscripprice | fscripprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | foprtotalqualifiedbaseqty | foprtotalqualifiedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | foprtotalreportbaseqty | foprtotalreportbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fstoragepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 6 | ffloorqty | ffloorqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | foprrepairedbaseqty | foprrepairedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 9 | ffirstinspection | ffirstinspection | bpchar | 1 |  | √ | '0' |  |
| 10 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工序数量 |
| 11 | foprtotalreceivebaseqty | foprtotalreceivebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fpushpurbillqty | fpushpurbillqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | foprtotalreworkqty | foprtotalreworkqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | foprtotaljunkqty | foprtotaljunkqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fschedulingcalendar | fschedulingcalendar | int8 | 64 |  | √ | 0 |  |
| 16 | foprtotalwastebaseqty | foprtotalwastebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fpushreportbaseqty | fpushreportbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fpushreworkreportqty | fpushreworkreportqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | foprtotaljunkbaseqty | foprtotaljunkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fscriptaxprice | fscriptaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 22 | freworkreportqty | freworkreportqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | ffirstinspectioncontrol | ffirstinspectioncontrol | varchar | 30 |  | √ | ' ' |  |
| 24 | fpushreportqty | fpushreportqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | foprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 26 | freworkreportbaseqty | freworkreportbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | foperationunitid | foperationunitid | int8 | 64 |  | √ | 0 |  |
| 28 | foprtotaloutbaseqty | foprtotaloutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0.0000000000 | 表头数量 |
| 30 | foprtotalreceiveqty | 累计让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计让步接收数量 |
| 31 | fwastetaxprice | fwastetaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fwasteprice | fwasteprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fupperqty | fupperqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | foprtotalmaterialbaseqty | foprtotalmaterialbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | finspectiontype | finspectiontype | varchar | 30 |  | √ | '1011' |  |
| 36 | foprtotalinbaseqty | foprtotalinbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fpushreworkreportbaseqty | fpushreworkreportbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fupperratio | fupperratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | foprtotalreworkbaseqty | foprtotalreworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | ffirstinspectionstatus | ffirstinspectionstatus | varchar | 30 |  | √ | ' ' |  |
| 42 | fcollaborative | fcollaborative | bpchar | 1 |  | √ | '0' |  |
| 43 | fworkstationid | fworkstationid | int8 | 64 |  | √ | 0 |  |
| 44 | freworkedreworkqty | freworkedreworkqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftechentry_e |  | fprocessentryid |
| 2 | idx_pom_manftechentry_e_fid |  | fid |

---

## 工序计划分录f7(废弃)-主表 t_pom_manftechentry

- **表名称：** 工序计划分录f7(废弃)-主表
- **表名：** t_pom_manftechentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprplanbegintime | foprplanbegintime | timestamp | 0 |  |  | null |  |
| 3 | foprtotaloutqty | 累计转出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计转出数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 6 | foprtotalqualifiedqty | 累计合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计合格数量 |
| 7 | foproverlapqty | foproverlapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | foprproductionqty | foprproductionqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | foprrepairedqty | foprrepairedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | foprnonum | foprnonum | int8 | 64 |  | √ | 0 |  |
| 11 | fbasebatchqty | fbasebatchqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | foprworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 13 | foprworkshopid | foprworkshopid | int8 | 64 |  | √ | 0 |  |
| 14 | foprtimeunit | foprtimeunit | varchar | 30 |  | √ | ' ' |  |
| 15 | foprparentnum | foprparentnum | int8 | 64 |  | √ | 0 |  |
| 16 | foproperationid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 17 | foprtotalmaterialqty | foprtotalmaterialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | foprsuggestsplitqty | foprsuggestsplitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 20 | foprissplit | foprissplit | bpchar | 1 |  | √ | '0' |  |
| 21 | foprsourcetype | foprsourcetype | varchar | 30 |  | √ | ' ' |  |
| 22 | foprorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | foprunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | foprtotalsplitbaseqty | foprtotalsplitbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | ftotalsplitqty | ftotalsplitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | foprtotalreportqty | 累计汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计汇报数量 |
| 27 | foproverlaptimeunit | foproverlaptimeunit | varchar | 30 |  | √ | ' ' |  |
| 28 | foprtotalconcessionqty | foprtotalconcessionqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | foprearliestfinishtime | foprearliestfinishtime | timestamp | 0 |  |  | null |  |
| 30 | foprtotalinqty | foprtotalinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | foprisprocessoverlap | foprisprocessoverlap | bpchar | 1 |  | √ | '0' |  |
| 32 | foprminworktime | foprminworktime | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | foprstandardqty | foprstandardqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | foprqty | foprqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | foverlapunitid | foverlapunitid | int8 | 64 |  | √ | 0 |  |
| 36 | foprparent | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 37 | fopractualsplitqty | fopractualsplitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 39 | foprtotalwasteqty | foprtotalwasteqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fparentoprid | fparentoprid | varchar | 50 |  | √ | ' ' |  |
| 41 | foprsourceentryid | foprsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 42 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 | id |
| 43 | foprlatestfinishtime | foprlatestfinishtime | timestamp | 0 |  |  | null |  |
| 44 | foprminoverlaptime | foprminoverlaptime | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 45 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | 工序控制策略(废弃) mpdm_proctrlstrategy |
| 46 | foprinvalid | foprinvalid | bpchar | 1 |  | √ | '0' |  |
| 47 | foprtotalscrapqty | foprtotalscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | foprplanfinishtime | foprplanfinishtime | timestamp | 0 |  |  | null |  |
| 49 | foprstatus | foprstatus | varchar | 30 |  | √ | ' ' |  |
| 50 | foprearliestbegintime | foprearliestbegintime | timestamp | 0 |  |  | null |  |
| 51 | foprlatestbegintime | foprlatestbegintime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_manftechentry_fid |  | fid |
| 2 | pk_pom_manftechentry |  | fprocessentryid |
| 3 | idx_pom_tech_fparentoprnum |  | foprparentnum,foprnonum |
