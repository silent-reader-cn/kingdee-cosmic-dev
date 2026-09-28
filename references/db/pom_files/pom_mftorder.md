# 生产工单-pom_mftorder

## 生产工单-反写记录表 t_pom_mftorder_wb

- **表名称：** 生产工单-反写记录表
- **表名：** t_pom_mftorder_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_mftorder_wb_pkey |  | fentryid |
| 2 | idx_pom_mftorder_wb_fk |  | fid |

---

## 生产工单-主表 t_pom_mftorder

- **表名称：** 生产工单-主表
- **表名：** t_pom_mftorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_bj73_basedatafield | 包装部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 5 | fasyncstatuspom | 组件清单异步状态 | varchar | 50 |  | √ | ' ' | 组件清单异步状态,枚举: A :处理中 B :已完成 C :已失败 |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 8 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 12 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fasyncstatussfc | 工序计划异步状态 | varchar | 50 |  | √ | ' ' | 工序计划异步状态,枚举: A :处理中 B :已完成 C :已失败 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 9 :迁移生成 |
| 22 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 23 | fk_bj73_textareafield | 包装明细 | varchar | 500 |  | √ | ' ' | 包装明细 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorder_fk |  | fbillno |
| 2 | idx_mftorder_createtime |  | fcreatetime |
| 3 | idx_pom_mftorder_orgidfid |  | forgid,fid |
| 4 | t_pom_mftorder_pkey |  | fid |

---

## 关联子实体-子表 t_pom_mftorderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mftorderentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseunitexpoutqty_old | 基本单位预计产出数量_原始携带值 | numeric | 23 | 10 |  | null | 基本单位预计产出数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbaseunitexpoutqty | 基本单位预计产出数量_确认携带值 | numeric | 23 | 10 |  | null | 基本单位预计产出数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_mftorderentry_lk_pkey |  | fpkid |
| 2 | idx_pom_mftorderentry_lk_fk |  | fentryid |

---

## 生产工单-关联追踪表 t_pom_mftorder_tc

- **表名称：** 生产工单-关联追踪表
- **表名：** t_pom_mftorder_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_mftorder_tc_pkey |  | fid |
| 2 | idx_pom_mftorder_tc_tbill |  | ftbillid |
| 3 | idx_pom_mftorder_tc_tid |  | ftid |

---

## 产品明细-分表 t_pom_mftorderentry_f

- **表名称：** 产品明细-分表
- **表名：** t_pom_mftorderentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowsrctype | 行来源类型 | varchar | 5 |  | √ | ' ' | 行来源类型,枚举: A :生成下级工单_生成新工单 B :生成下级工单_生成新分录 C :生产改制 |
| 3 | fisgeneratedsuborder | 已生成下级工单 | bpchar | 1 |  | √ | '0' | 已生成下级工单 |
| 4 | fclosereason | 手工关闭原因 | varchar | 500 |  | √ | ' ' | 手工关闭原因 |
| 5 | foutputoperationnum | 产出工序号 | int4 | 32 |  | √ | 0 | 产出工序号 |
| 6 | fstockedqty | 待入库数量 | numeric | 23 | 10 | √ | 0 | 待入库数量 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 8 | foutputoperationseq | 产出工序序列 | int4 | 32 |  | √ | 0 | 产出工序序列 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 11 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 12 | fstockedbaseqty | 待入库基本数量 | numeric | 23 | 10 | √ | 0 | 待入库基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorderentry_f_fid |  | fid |
| 2 | pk_pom_mftorderentry_f |  | fentryid |

---

## 产品明细-分表 t_pom_mftorderentry_e

- **表名称：** 产品明细-分表
- **表名：** t_pom_mftorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 3 | fxkunquainwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 4 | fsuperiorstockentryid | 上级用料清单分录ID | int8 | 64 |  | √ | 0 | 上级用料清单分录ID |
| 5 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 6 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 7 | frepminbsqty | 汇报下限基本数量 | numeric | 23 | 10 | √ | 0 | 汇报下限基本数量 |
| 8 | fiscontrolqty | 控制入库数量 | bpchar | 1 |  | √ | '0' | 控制入库数量 |
| 9 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 10 | flocation | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fmtlcostqty | 料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废数量 |
| 12 | fxkstockqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 13 | fstockqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推入库基本数量 |
| 14 | frootdemandentryseq | 根需求单据行号 | int4 | 32 |  | √ | 0 | 根需求单据行号 |
| 15 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 16 | fxkquainwaqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 17 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fendcasetime | 齐套时间 | timestamp | 0 |  |  | null | 齐套时间 |
| 19 | fbrokenbsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 20 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 21 | frepminqty | 汇报下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限数量 |
| 22 | frepminrate | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限允差（%） |
| 23 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 24 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 25 | fnotreportqty | 待汇报数量 | numeric | 23 | 10 | √ | 0 | 待汇报数量 |
| 26 | finwarmin | 入库下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 入库下限基本数量 |
| 27 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0.0000000000 | 已领套数 |
| 28 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量 |
| 29 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 30 | fplansuretime | 计划确认时间 | timestamp | 0 |  |  | null | 计划确认时间 |
| 31 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 32 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 33 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 34 | fwaitcheckqty | 待检品入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 待检品入库数量 |
| 35 | fxkinwarmin | 入库下限数量 | numeric | 23 | 10 | √ | 0 | 入库下限数量 |
| 36 | frptbsqty | 关联汇报基本数量 | numeric | 23 | 10 | √ | 0 | 关联汇报基本数量 |
| 37 | fheadbillno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 38 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 39 | ffirstinspectioncontrol | 首检控制方式 | bpchar | 1 |  | √ | 'A' | 首检控制方式,枚举: A :严格控制 B :非严格控制 |
| 40 | fscrapbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 41 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废数量 |
| 42 | fisgenprocessplan | 已生成工序计划 | bpchar | 1 |  | √ | '0' | 已生成工序计划 |
| 43 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 44 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 45 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 46 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 47 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修数量 |
| 48 | fxkinwarmax | 入库上限数量 | numeric | 23 | 10 | √ | 0 | 入库上限数量 |
| 49 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 50 | ftotalsplitqty | 已拆分数量 | numeric | 23 | 10 | √ | 0 | 已拆分数量 |
| 51 | ffirstinspectionstatus | 首检状态 | bpchar | 1 |  | √ | 'N' | 首检状态,枚举: N :空 A :待首检 B :首检中 C :首检完成 |
| 52 | ftotalsplitbaseqty | 已拆分基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分基本数量 |
| 53 | fnotreportbsqty | 待汇报基本数量 | numeric | 23 | 10 | √ | 0 | 待汇报基本数量 |
| 54 | fisinspection | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 55 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 56 | frptqty | 关联汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联汇报数量 |
| 57 | frootdemandentity | 根需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 58 | foutwaqty | 退库基本数量 | numeric | 23 | 10 | √ | 0 | 退库基本数量 |
| 59 | frcvinhighlimit | 入库上限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 入库上限允差（%） |
| 60 | ffirstinspection | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 61 | fisconreportqty | 控制汇报数量 | bpchar | 1 |  | √ | '0' | 控制汇报数量 |
| 62 | fxkdemanddate | 订单需求日期 | timestamp | 0 |  |  | null | 订单需求日期 |
| 63 | freworkorderqty | 关联返工工单数量 | numeric | 23 | 10 | √ | 0 | 关联返工工单数量 |
| 64 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 65 | freportbsqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0 | 汇报基本数量 |
| 66 | frepmaxqty | 汇报上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限数量 |
| 67 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 68 | fxkoutwaqty | 退库数量 | numeric | 23 | 10 | √ | 0 | 退库数量 |
| 69 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 70 | ftransmittime | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 71 | frepmaxrate | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限允差（%） |
| 72 | fqualifiedbsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 73 | frootdemandbillno | 根需求单号 | varchar | 120 |  | √ | ' ' | 根需求单号 |
| 74 | frepmaxbsqty | 汇报上限基本数量 | numeric | 23 | 10 | √ | 0 | 汇报上限基本数量 |
| 75 | frepairbsqty | 返修基本数量 | numeric | 23 | 10 | √ | 0 | 返修基本数量 |
| 76 | frepinwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工品入库数量 |
| 77 | frcvinlowlimit | 入库下限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 入库下限允差（%） |
| 78 | finwarmax | 入库上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 入库上限基本数量 |
| 79 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 80 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 81 | fislastproceplanend | 末道工序完工 | bpchar | 1 |  | √ | '1' | 末道工序完工 |
| 82 | fbrokenqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 83 | fmanuseq | 生产顺序 | int8 | 64 |  | √ | 0 | 生产顺序 |
| 84 | fsettletime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 85 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 86 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 87 | facceptbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 88 | foutputoperation | 产出工序112 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 89 | fendworktime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 90 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 91 | fmtlcostbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_mftorderentry_e_pkey |  | fentryid |
| 2 | idx_pom_mftorderentry_e_fk |  | fid |

---

## 产品明细-子表 t_pom_mftorderentry

- **表名称：** 产品明细-子表
- **表名：** t_pom_mftorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | 拆分前数量 | numeric | 23 | 10 | √ | 0 | 拆分前数量 |
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fclosetype | 关闭类型 | varchar | 10 |  | √ | ' ' | 关闭类型,枚举: A :自动关闭 B :手工关闭 C :拆分关闭 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0.0000000000 | 成品率% |
| 7 | fbaseunitexpoutqty | 基本单位预计产出数量 | numeric | 23 | 10 | √ | 0 | 基本单位预计产出数量 |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | froutereplace | 工艺路线替代号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_routereplace](../mpdm_files/mpdm_routereplace.md) |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 13 | fxkdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 14 | finvkittingqty | 库存齐套数量 | numeric | 23 | 10 | √ | 0 | 库存齐套数量 |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 17 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 18 | fmanftechstatus | 工序计划状态 | varchar | 30 |  | √ | ' ' | 工序计划状态,枚举: T :存在工序计划 F :不存在工序计划 |
| 19 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 21 | fkittingsupplydate | 预计齐套日期 | timestamp | 0 |  |  | null | 预计齐套日期 |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fisreserved | 是否已预留 | bpchar | 1 |  | √ | '0' | 是否已预留 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fsrcorderentryid | 源工单分录id | int8 | 64 |  | √ | 0 | 源工单分录id |
| 26 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 27 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 28 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 29 | fbeginbookdate | 投产记账日期 | timestamp | 0 |  |  | null | 投产记账日期 |
| 30 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 31 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 32 | fmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 33 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 37 | fkittingid | 齐套分析ID | int8 | 64 |  | √ | 0 | 齐套分析ID |
| 38 | fexpoutqty | 预计产出数量 | numeric | 23 | 10 | √ | 0 | 预计产出数量 |
| 39 | fexpkittingqty | 预计齐套数量 | numeric | 23 | 10 | √ | 0 | 预计齐套数量 |
| 40 | fk_bj73_qtyfield | 入库辅助数量 | numeric | 23 | 10 |  | null | 入库辅助数量 |
| 41 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 42 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 44 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 45 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 46 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 47 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 48 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 49 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 50 | fsrcsplitbillnumber | 来源拆分工单编码 | varchar | 50 |  | √ | ' ' | 来源拆分工单编码 |
| 51 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 52 | fkittingsign | 齐套状况 | varchar | 5 |  | √ | ' ' | 齐套状况,枚举: A :库存齐套 B :预计齐套 C :不齐套 D :暂收齐套 E :在途齐套 F :采购申请齐套 G :计划订单齐套 |
| 53 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 54 | fexpkittingbaseqty | 预计齐套基本数量 | numeric | 23 | 10 | √ | 0 | 预计齐套基本数量 |
| 55 | fprodline | 产线 | int8 | 64 |  | √ | 0 | [产线日产能F7 mrp_prodline_f7](../mrp_files/mrp_prodline_f7.md) |
| 56 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 57 | festscrapqty | 预计报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预计报废数量 |
| 58 | fkittingtime | 齐套分析时间 | timestamp | 0 |  |  | null | 齐套分析时间 |
| 59 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 60 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 61 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 63 | fplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 64 | fpurqty | 下推采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推采购数量 |
| 65 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 66 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 67 | foprentryid | 工序计划分录id | int8 | 64 |  | √ | 0 | 工序计划分录id |
| 68 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 69 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 70 | finvkittingbaseqty | 库存齐套基本数量 | numeric | 23 | 10 | √ | 0 | 库存齐套基本数量 |
| 71 | fplanbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 72 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 73 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 74 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orderen_fconfiguredcode |  | fconfiguredcodeid |
| 2 | idx_pom_mftorderentry_fk |  | fid |
| 3 | idx_pom_moe_fplanstatus |  | fplanstatus |
| 4 | idx_orderen_mid |  | fmaterielmasterid |
| 5 | t_pom_mftorderentry_pkey |  | fentryid |
| 6 | idx_orderen_ftracknumber |  | ftracknumberid |
| 7 | idx_orderen_mftid |  | fmaterial |
