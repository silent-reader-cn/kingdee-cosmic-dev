# 检修工序计划(废弃)-sfc_mromanuftech

## 工序组-子表 t_sfc_mrogroupentry

- **表名称：** 工序组-子表
- **表名：** t_sfc_mrogroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgromodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgromodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fgroprocessgroupid | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fgroremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fgrogroupstatus | 工序组状态 | varchar | 50 |  | √ | ' ' | 工序组状态,枚举: A :下达 B :开工 C :完工 D :取消 E :保留 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mrogroupentry |  | fentryid |
| 2 | idx_sfc_mrogroupentry_fk |  | fid |

---

## 检修工序计划(废弃)-关联追踪表 t_sfc_mromanuftech_tc

- **表名称：** 检修工序计划(废弃)-关联追踪表
- **表名：** t_sfc_mromanuftech_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_mromanuftech_tc_tid |  | ftid |
| 2 | idx_sfc_mromanuftech_tc_tbill |  | ftbillid |
| 3 | pk_sfc_mromanuftech_tc |  | fid |

---

## 工序排程资源-子表 t_sfc_mroschsubentry

- **表名称：** 工序排程资源-子表
- **表名：** t_sfc_mroschsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fschresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 4 | fsourceresid | 来源工序活动计划ID | varchar | 50 |  | √ | ' ' | 来源工序活动计划ID |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mroschsubentry |  | fdetailid |
| 2 | idx_sfc_mroschsubentry_fk |  | fentryid |

---

## 工序-分表 t_sfc_mromanftechentry_f

- **表名称：** 工序-分表
- **表名：** t_sfc_mromanftechentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscripprice | 废料单价 | numeric | 23 | 10 | √ | 0 | 废料单价 |
| 3 | foprtotalqualifiedbaseqty | 已合格基本数量 | numeric | 23 | 10 | √ | 0 | 已合格基本数量 |
| 4 | foprtotalreportbaseqty | 已普通汇报基本数量 | numeric | 23 | 10 | √ | 0 | 已普通汇报基本数量 |
| 5 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 6 | fstoragepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 7 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 8 | ffloorqty | 汇报下限数量 | numeric | 23 | 10 | √ | 0 | 汇报下限数量 |
| 9 | foprrepairedbaseqty | 已返修基本数量 | numeric | 23 | 10 | √ | 0 | 已返修基本数量 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 11 | foprtotalreceivebaseqty | 已让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 已让步接收基本数量 |
| 12 | fpushpurbillqty | 下推采购申请/订单数量 | numeric | 23 | 10 | √ | 0 | 下推采购申请/订单数量 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | fpurordernumber | 采购订单选单数量 | numeric | 23 | 10 | √ | 0 | 采购订单选单数量 |
| 15 | foprnonum | 工序号（数字） | int8 | 64 |  | √ | 0 | 工序号（数字） |
| 16 | fentrymaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | foprparentnum | 工序序列（数字） | int8 | 64 |  | √ | 0 | 工序序列（数字） |
| 18 | foprtotalwastebaseqty | 已工废基本数量 | numeric | 23 | 10 | √ | 0 | 已工废基本数量 |
| 19 | fpushreportbaseqty | 下推普通汇报基本数量 | numeric | 23 | 10 | √ | 0 | 下推普通汇报基本数量 |
| 20 | ftotaldownqty | 已采购申请数量 | numeric | 23 | 10 | √ | 0 | 已采购申请数量 |
| 21 | foprtotaljunkbaseqty | 已报废基本数量 | numeric | 23 | 10 | √ | 0 | 已报废基本数量 |
| 22 | fscriptaxprice | 废料含税单价 | numeric | 23 | 10 | √ | 0 | 废料含税单价 |
| 23 | fsettlementcoefficient | 结算系数 | numeric | 23 | 10 | √ | 0 | 结算系数 |
| 24 | fpurapplynumber | 采购申请选单数量 | numeric | 23 | 10 | √ | 0 | 采购申请选单数量 |
| 25 | fpurchasepersonid | 采购员(暂时不用) | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fpushreportqty | 下推汇总数量 | numeric | 23 | 10 | √ | 0 | 下推汇总数量 |
| 27 | freworkreportbaseqty | 已返工汇报基本数量 | numeric | 23 | 10 | √ | 0 | 已返工汇报基本数量 |
| 28 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | foprtotaloutbaseqty | 已转出基本数量 | numeric | 23 | 10 | √ | 0 | 已转出基本数量 |
| 30 | fwastetaxprice | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 31 | fwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 32 | fupperqty | 汇报上限数量 | numeric | 23 | 10 | √ | 0 | 汇报上限数量 |
| 33 | foprtotalmaterialbaseqty | 已料废基本数量 | numeric | 23 | 10 | √ | 0 | 已料废基本数量 |
| 34 | finspectiontype | 检验方式 | varchar | 50 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 35 | fpushreworkreportbaseqty | 下推返工汇报基本数量 | numeric | 23 | 10 | √ | 0 | 下推返工汇报基本数量 |
| 36 | foprtotalinbaseqty | 已转入基本数量 | numeric | 23 | 10 | √ | 0 | 已转入基本数量 |
| 37 | foprtotalreworkbaseqty | 已返工基本数量 | numeric | 23 | 10 | √ | 0 | 已返工基本数量 |
| 38 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | fcollaborative | 协作工序 | bpchar | 1 |  | √ | '0' | 协作工序 |
| 41 | fsettlementunitid | 结算单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 42 | fworkstationid | 工位 | int8 | 64 |  | √ | 0 | 工位 mpdm_workstation |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mroentry_f_fid |  | fid |
| 2 | pk_sfc_mromanftechentry_f |  | fentryid |

---

## 工序-分表 t_sfc_mromanftechentry_e

- **表名称：** 工序-分表
- **表名：** t_sfc_mromanftechentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprtotalunqualifiedqty | 已不合格数量 | numeric | 23 | 10 | √ | 0 | 已不合格数量 |
| 3 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | foprtotalinqty | 已转入数量 | numeric | 23 | 10 | √ | 0 | 已转入数量 |
| 5 | foprtotaloutqty | 已转出数量 | numeric | 23 | 10 | √ | 0 | 已转出数量 |
| 6 | foprisprocessoverlap | 是否工序重叠 | bpchar | 1 |  | √ | '0' | 是否工序重叠 |
| 7 | foprminworktime | 最小加工时间 | numeric | 23 | 10 | √ | 0 | 最小加工时间 |
| 8 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 9 | foprtotalqualifiedqty | 已合格数量 | numeric | 23 | 10 | √ | 0 | 已合格数量 |
| 10 | foprtotalreworkqty | 已返工数量 | numeric | 23 | 10 | √ | 0 | 已返工数量 |
| 11 | foproverlapqty | 重叠批量 | numeric | 23 | 10 | √ | 0 | 重叠批量 |
| 12 | foverlapunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | foprparent | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 14 | fopractualsplitqty | 实际拆分数 | numeric | 23 | 10 | √ | 0 | 实际拆分数 |
| 15 | ffloorratio | 汇报下限比例(%) | numeric | 23 | 10 | √ | 0 | 汇报下限比例(%) |
| 16 | fschedulingcalendar | 排程工厂日历 | int8 | 64 |  | √ | 0 | 生产日历 mpdm_calendar |
| 17 | foprrepairedqty | 已返修数量 | numeric | 23 | 10 | √ | 0 | 已返修数量 |
| 18 | fbasebatchqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 19 | fremaininghours | 剩余工时（小时） | numeric | 23 | 10 | √ | 0 | 剩余工时（小时） |
| 20 | foprtotalwasteqty | 已工废数量 | numeric | 23 | 10 | √ | 0 | 已工废数量 |
| 21 | foprtimeunit | 加工时间单位 | varchar | 50 |  | √ | ' ' | 加工时间单位,枚举: A :分钟 B :秒 |
| 22 | fabnormalstatus | 异常状态 | bpchar | 1 |  | √ | '0' | 异常状态 |
| 23 | fparentoprid | 父工序工序ID | varchar | 50 |  | √ | ' ' | 父工序工序ID |
| 24 | foprtotalmaterialqty | 已料废数量 | numeric | 23 | 10 | √ | 0 | 已料废数量 |
| 25 | foprsuggestsplitqty | 建议拆分数 | numeric | 23 | 10 | √ | 0 | 建议拆分数 |
| 26 | fpushreworkreportqty | 下推返工汇报数量 | numeric | 23 | 10 | √ | 0 | 下推返工汇报数量 |
| 27 | foprlatestfinishtime | 最晚完工时间 | timestamp | 0 |  |  | null | 最晚完工时间 |
| 28 | freworkreportqty | 返工汇报数量 | numeric | 23 | 10 | √ | 0 | 返工汇报数量 |
| 29 | foprissplit | 是否拆分排程 | bpchar | 1 |  | √ | '0' | 是否拆分排程 |
| 30 | foprminoverlaptime | 重叠最小时间 | numeric | 23 | 10 | √ | 0 | 重叠最小时间 |
| 31 | flockqty | 锁定数量 | numeric | 23 | 10 | √ | 0 | 锁定数量 |
| 32 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0 | 表头数量 |
| 34 | foprtotalreceiveqty | 已让步接收数量 | numeric | 23 | 10 | √ | 0 | 已让步接收数量 |
| 35 | fcompletionrate | 完成率（%） | numeric | 23 | 10 | √ | 0 | 完成率（%） |
| 36 | foprtotalscrapqty | 已报废数量 | numeric | 23 | 10 | √ | 0 | 已报废数量 |
| 37 | ftotalsplitqty | 已拆分/改制数量 | numeric | 23 | 10 | √ | 0 | 已拆分/改制数量 |
| 38 | fupperratio | 汇报上限比例(%) | numeric | 23 | 10 | √ | 0 | 汇报上限比例(%) |
| 39 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | foprtotalreportqty | 已汇报数量 | numeric | 23 | 10 | √ | 0 | 已汇报数量 |
| 41 | foprearliestbegintime | 最早开始时间 | timestamp | 0 |  |  | null | 最早开始时间 |
| 42 | foproverlaptimeunit | 重叠时间单位 | varchar | 50 |  | √ | ' ' | 重叠时间单位,枚举: A :分钟 B :秒 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 44 | foprlatestbegintime | 最晚开始时间 | timestamp | 0 |  |  | null | 最晚开始时间 |
| 45 | foprtotalconcessionqty | 已让步数量 | numeric | 23 | 10 | √ | 0 | 已让步数量 |
| 46 | foprearliestfinishtime | 最早完工时间 | timestamp | 0 |  |  | null | 最早完工时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mromanftechentry_e |  | fentryid |
| 2 | idx_mrotechentry_e_fid |  | fid |

---

## 工序序列-子表 t_sfc_mroprocessentry

- **表名称：** 工序序列-子表
- **表名：** t_sfc_mroprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessplanbegintime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 3 | fprocessplanouttime | 计划转出时间 | timestamp | 0 |  |  | null | 计划转出时间 |
| 4 | fprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 5 | fprocessrelation | 并行关系 | varchar | 50 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :开始-结束 C :结束-开始 D :结束-结束 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fprocessoutput | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 8 | fprocessinput | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 9 | fprocessplanendtime | 计划结束时间 | timestamp | 0 |  |  | null | 计划结束时间 |
| 10 | fprocessseqqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 11 | fprocessremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fprocessinputdesc | 转入工序说明 | varchar | 50 |  | √ | ' ' | 转入工序说明 |
| 13 | fprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 14 | fprocessreference | 参照序列 | varchar | 50 |  | √ | ' ' | 参照序列 |
| 15 | fsourceseqid | 来源工序工序列ID | varchar | 50 |  | √ | ' ' | 来源工序工序列ID |
| 16 | fprocessoutputdesc | 转出工序说明 | varchar | 50 |  | √ | ' ' | 转出工序说明 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fprocessplanintime | 计划转入时间 | timestamp | 0 |  |  | null | 计划转入时间 |
| 19 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_mroprocessentry_fk |  | fid |
| 2 | pk_sfc_mroprocessentry |  | fentryid |

---

## 序列关系-子表 t_sfc_mrorelationentry

- **表名称：** 序列关系-子表
- **表名：** t_sfc_mrorelationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftransferprocessname | 转入工序名称 | varchar | 50 |  | √ | ' ' | 转入工序名称 |
| 3 | frelationseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 4 | fplanturnouttime | 计划转出时间 | timestamp | 0 |  |  | null | 计划转出时间 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fturnoutprocessname | 转出工序名称 | varchar | 50 |  | √ | ' ' | 转出工序名称 |
| 7 | frelationparseq | 并行序列号 | varchar | 50 |  | √ | ' ' | 并行序列号 |
| 8 | frelationparseqname | 并行序列名称 | varchar | 50 |  | √ | ' ' | 并行序列名称 |
| 9 | ftransferprocessno | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 10 | fsourcerelid | 来源序列关系分录ID | varchar | 50 |  | √ | ' ' | 来源序列关系分录ID |
| 11 | fparallelration | 并行关系 | varchar | 50 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :结束-开始 C :结束-结束 D :开始-结束 |
| 12 | fplantransfertime | 计划转入时间 | timestamp | 0 |  |  | null | 计划转入时间 |
| 13 | fturnoutprocessno | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 14 | frelationname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_mrorelationentry_fk |  | fid |
| 2 | pk_sfc_mrorelationentry |  | fentryid |

---

## 检修工序计划(废弃)-主表 t_sfc_mromanuftech

- **表名称：** 检修工序计划(废弃)-主表
- **表名：** t_sfc_mromanuftech

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 3 | fproductionworkshopid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fworkcardid | 工卡 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fpageseq | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 10 | fmanufactureorder | 生产工单编号（废弃） | varchar | 50 |  | √ | ' ' | 生产工单编号（废弃） |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | ftransactiontypeid | 检修事务类型 | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 13 | fmaterialmodel | 产品型号 | varchar | 50 |  | √ | ' ' | 产品型号 |
| 14 | fmftentryseq | 检修工单行号ID | int8 | 64 |  | √ | 0 | 检修工单分录F7(废弃) sfc_mroorder_f7 |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | factualhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 23 | fplanfinishtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 24 | fmanufactureorderid | 检修工单ID | varchar | 50 |  | √ | ' ' | 检修工单ID |
| 25 | fmaterielmtc | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 26 | fplanstarttime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 27 | fmrtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrotech_fbillno |  | fbillno |
| 2 | idx_mrotech_forderid |  | fmanufactureorderid |
| 3 | idx_mrotech_fcreatetime |  | fcreatetime |
| 4 | idx_mrotech_forderentryid |  | fmftentryseq |
| 5 | pk_sfc_mromanuftech |  | fid |

---

## 检修工序计划(废弃)-反写记录表 t_sfc_mromanuftech_wb

- **表名称：** 检修工序计划(废弃)-反写记录表
- **表名：** t_sfc_mromanuftech_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mromanuftech_wb |  | fentryid |
| 2 | idx_sfc_mromanuftech_wb_fk |  | fid |

---

## 工序活动计划-子表 t_sfc_mroactsubentry

- **表名称：** 工序活动计划-子表
- **表名：** t_sfc_mroactsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 2 | factminformula1 | 最小值公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 3 | factactivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 4 | factplanbegintime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | factstandardformulaid | 标准公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fprocessstage | 工序阶段 | varchar | 50 |  | √ | ' ' | 工序阶段,枚举: A :排队阶段 B :准备阶段 C :加工阶段 D :拆卸阶段 E :等待阶段 F :转移阶段 |
| 9 | factplantotalqty | 计划总量 | numeric | 23 | 10 | √ | 0 | 计划总量 |
| 10 | factminformulaid | 最小值公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 11 | factresources | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 12 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: A :生产 B :成本 C :工资 |
| 13 | factplanfinishtime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fsourceactid | 来源工序活动计划ID | varchar | 50 |  | √ | ' ' | 来源工序活动计划ID |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | factstandardformula1id | 标准公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mroactsubentry |  | fdetailid |
| 2 | idx_sfc_mroactsubentry_fk |  | fentryid |

---

## 关联子实体-子表 t_sfc_mromanftechentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_mromanftechentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_mromanftechentry_lk_fk |  | fentryid |
| 2 | pk_sfc_mromanftechentry_lk |  | fpkid |

---

## 工序活动汇报-子表 t_sfc_mrorepsubentry

- **表名称：** 工序活动汇报-子表
- **表名：** t_sfc_mrorepsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factivityunit | 活动单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 2 | fsrcentryid | 来源分录id | varchar | 50 |  | √ | ' ' | 来源分录id |
| 3 | frepactualqty | 实际总量 | numeric | 23 | 10 | √ | 0 | 实际总量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frepbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 6 | frepactualfinishtime | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 7 | frepactualcihours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 8 | frepactivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 9 | frepresources | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 10 | frepactualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 11 | frepactualchours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mrorepsubentry |  | fdetailid |
| 2 | idx_sfc_mrorepsubentry_fk |  | fentryid |

---

## 关联子实体-子表 t_sfc_mromanuftech_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_mromanuftech_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_mromanuftech_lk_fk |  | fid |
| 2 | pk_sfc_mromanuftech_lk |  | fpkid |

---

## 接收人-多选基础资料表 t_sfc_mromulreceiver

- **表名称：** 接收人-多选基础资料表
- **表名：** t_sfc_mromulreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mromulreceiver |  | fpkid |
| 2 | idx_sfc_mromulreceiver_fk |  | fentryid |

---

## 检修工序计划(废弃)-分表 t_sfc_mromanuftech_e

- **表名称：** 检修工序计划(废弃)-分表
- **表名：** t_sfc_mromanuftech_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 3 | fparentseqid | 父工序序列ID | varchar | 50 |  | √ | ' ' | 父工序序列ID |
| 4 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 5 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fplantype | 计划类型 | varchar | 50 |  | √ | ' ' | 计划类型,枚举: A :主计划 B :拆卡-首序 C :拆卡-中间工序 D :拆卡-选中序 |
| 7 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fparentplanid | 父工序计划ID | varchar | 50 |  | √ | ' ' | 父工序计划ID |
| 11 | fauxptyqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 12 | fschedulplanid | 排程方案 | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_mro_fconfiguredcode |  | fconfiguredcodeid |
| 2 | idx_sfc_mro_ftracknumber |  | ftracknumberid |
| 3 | pk_sfc_mromanuftech_e |  | fid |

---

## 工序-子表 t_sfc_mromanftechentry

- **表名称：** 工序-子表
- **表名：** t_sfc_mromanftechentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprishandover | 交接 | bpchar | 1 |  | √ | '0' | 交接 |
| 3 | foprplanbegintime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 4 | foprsumactualhours | 合计消耗工时 | numeric | 23 | 10 | √ | 0 | 合计消耗工时 |
| 5 | fopractualendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 6 | foprremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foprworkhours | 标准工时（小时） | numeric | 23 | 10 | √ | 0 | 标准工时（小时） |
| 9 | foprstandardqty | 工序标准数量 | numeric | 23 | 10 | √ | 0 | 工序标准数量 |
| 10 | foprpageseq | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 11 | foprqty | 工序计划数量 | numeric | 23 | 10 | √ | 0 | 工序计划数量 |
| 12 | foprtotaljunkqty | 已报废数量(工序检验) | numeric | 23 | 10 | √ | 0 | 已报废数量(工序检验) |
| 13 | foprprofessionaid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 14 | fmachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 15 | foprproductionqty | 生产单位工序数量 | numeric | 23 | 10 | √ | 0 | 生产单位工序数量 |
| 16 | foprassignorid | 派工人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 18 | foprworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 19 | foprtaskid | 任务编码 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 20 | foprworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 21 | foprprocessgroupid | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 22 | foproperationid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 23 | foprsourceentryid | 工艺路线工序ID | varchar | 50 |  | √ | ' ' | 工艺路线工序ID |
| 24 | fopractualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 25 | foprwbsid | WBS | int8 | 64 |  | √ | 0 | WBS pmts_wbs |
| 26 | foprcustomhours | 消耗工时（小时） | numeric | 23 | 10 | √ | 0 | 消耗工时（小时） |
| 27 | foprworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | foprcheckerid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fopreffectivehours | 有效工时（小时） | numeric | 23 | 10 | √ | 0 | 有效工时（小时） |
| 31 | foprmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | foprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 33 | foprsourcetype | 工序来源类型 | varchar | 50 |  | √ | ' ' | 工序来源类型,枚举: A :工艺路线 B :人工新增 C :工卡 |
| 34 | foperationunitid | 工序单位（弃用） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | foprorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | 工序控制策略(废弃) mpdm_proctrlstrategy |
| 37 | foprinvalid | 作废 | bpchar | 1 |  | √ | '0' | 作废 |
| 38 | foprfunctionlocationid | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 39 | foprstudystatus | 学习状态 | varchar | 50 |  | √ | ' ' | 学习状态,枚举: A :已学习 B :未学习 N :空 |
| 40 | foprunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | foprplanfinishtime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 42 | foprstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :创建 B :计划 C :计划确认 D :下达 E :开工 F :检验完工 G :关闭 H :维修完工 I :取消 J :保留 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | foprworkgroupid | 班组 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrotechentry_fid |  | fid |
| 2 | pk_sfc_mromanftechentry |  | fentryid |
