# 工序计划f7(废弃)-sfc_manftech_head_f7

## 工序计划f7(废弃)-主表 t_pom_mftorderentry_m

- **表名称：** 工序计划f7(废弃)-主表
- **表名：** t_pom_mftorderentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrouteid | fprocessrouteid | int8 | 64 |  | √ | 0 |  |
| 3 | fproductionworkshopid | fproductionworkshopid | int8 | 64 |  | √ | 0 |  |
| 4 | fbomversion | fbomversion | varchar | 50 |  | √ | ' ' |  |
| 5 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 8 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fparentplanid | fparentplanid | varchar | 50 |  | √ | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 14 | fmanufactureorder | fmanufactureorder | varchar | 50 |  | √ | ' ' |  |
| 15 | fbillno | 工序计划编号 | varchar | 30 |  | √ | ' ' | 工序计划编号 |
| 16 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fmftentryseq | 生产工单行号 | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 18 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: |
| 21 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fplanfinishtime | fplanfinishtime | timestamp | 0 |  |  | null |  |
| 24 | fparentseqid | fparentseqid | varchar | 50 |  | √ | ' ' |  |
| 25 | fmanufactureorderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 26 | fplantype | fplantype | varchar | 30 |  | √ | ' ' |  |
| 27 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fplanstarttime | fplanstarttime | timestamp | 0 |  |  | null |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | fschedulplanid | fschedulplanid | int8 | 64 |  | √ | 0 |  |
| 31 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorderent_m_fbillno |  | fbillno |
| 2 | idx_pom_tech_fcreatetime |  | fcreatetime |
| 3 | idx_manufetch_fconfiguredcode |  | fconfiguredcodeid |
| 4 | idx_manufetch_forderentryid |  | fmftentryseq |
| 5 | idx_manufetch_ftracknumber |  | ftracknumberid |
| 6 | pk_pom_mftorderentry_m |  | fid |
| 7 | idx_manufetch_forderid |  | fmanufactureorderid |
| 8 | idx_mftorderentry_m_orgfid |  | forgid,fid |
| 9 | idx_sfctech_mid |  | fmaterialid |

---

## 单据体-子表 t_pom_manftechentry

- **表名称：** 单据体-子表
- **表名：** t_pom_manftechentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprplanbegintime | foprplanbegintime | timestamp | 0 |  |  | null |  |
| 3 | foprtotaloutqty | foprtotaloutqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 6 | foprtotalqualifiedqty | foprtotalqualifiedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | foproverlapqty | foproverlapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | foprproductionqty | foprproductionqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | foprrepairedqty | foprrepairedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | foprnonum | foprnonum | int8 | 64 |  | √ | 0 |  |
| 11 | fbasebatchqty | fbasebatchqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | foprworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 13 | foprworkshopid | foprworkshopid | int8 | 64 |  | √ | 0 |  |
| 14 | foprtimeunit | foprtimeunit | varchar | 30 |  | √ | ' ' |  |
| 15 | foprparentnum | foprparentnum | int8 | 64 |  | √ | 0 |  |
| 16 | foproperationid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 17 | foprtotalmaterialqty | foprtotalmaterialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | foprsuggestsplitqty | foprsuggestsplitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 20 | foprissplit | foprissplit | bpchar | 1 |  | √ | '0' |  |
| 21 | foprsourcetype | foprsourcetype | varchar | 30 |  | √ | ' ' |  |
| 22 | foprorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | foprunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
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
| 45 | foprctrlstrategy | foprctrlstrategy | int8 | 64 |  | √ | 0 |  |
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
