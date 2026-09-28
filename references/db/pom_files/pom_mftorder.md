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
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 8 | fasyncstatussfc | 工序计划异步状态 | varchar | 50 |  | √ | ' ' | 工序计划异步状态,枚举: A :处理中 B :已完成 C :已失败 |
| 9 | fasyncstatuspom | 组件清单异步状态 | varchar | 50 |  | √ | ' ' | 组件清单异步状态,枚举: A :处理中 B :已完成 C :已失败 |
| 10 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 11 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 17 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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

## 产品明细-分表 t_pom_mftorderentry_e

- **表名称：** 产品明细-分表
- **表名：** t_pom_mftorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 3 | fxkunquainwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 4 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 5 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | frepminbsqty | 汇报下限基本数量 | numeric | 23 | 10 | √ | 0 | 汇报下限基本数量 |
| 7 | fiscontrolqty | 控制入库数量 | bpchar | 1 |  | √ | '0' | 控制入库数量 |
| 8 | flocation | 入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 9 | fmtlcostqty | 料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废数量 |
| 10 | fxkstockqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 11 | fstockqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推入库基本数量 |
| 12 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 13 | fxkquainwaqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 14 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fendcasetime | 齐套时间 | timestamp | 0 |  |  | null | 齐套时间 |
| 16 | fbrokenbsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 17 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 18 | frepminqty | 汇报下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限数量 |
| 19 | frepminrate | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限允差（%） |
| 20 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 21 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 22 | fnotreportqty | 待汇报数量 | numeric | 23 | 10 | √ | 0 | 待汇报数量 |
| 23 | finwarmin | 入库下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 入库下限基本数量 |
| 24 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0.0000000000 | 已领套数 |
| 25 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量 |
| 26 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 27 | fplansuretime | 计划确认时间 | timestamp | 0 |  |  | null | 计划确认时间 |
| 28 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 29 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 30 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fwaitcheckqty | 待检品入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 待检品入库数量 |
| 32 | fxkinwarmin | 入库下限数量 | numeric | 23 | 10 | √ | 0 | 入库下限数量 |
| 33 | frptbsqty | 关联汇报基本数量 | numeric | 23 | 10 | √ | 0 | 关联汇报基本数量 |
| 34 | fheadbillno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 35 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 36 | ffirstinspectioncontrol | 首检控制方式 | bpchar | 1 |  | √ | 'A' | 首检控制方式,枚举: A :严格控制 B :非严格控制 |
| 37 | fscrapbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 38 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废数量 |
| 39 | fisgenprocessplan | 已生成工序计划 | bpchar | 1 |  | √ | '0' | 已生成工序计划 |
| 40 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 41 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 42 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 43 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修数量 |
| 44 | fxkinwarmax | 入库上限数量 | numeric | 23 | 10 | √ | 0 | 入库上限数量 |
| 45 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 46 | ftotalsplitqty | 已拆分数量 | numeric | 23 | 10 | √ | 0 | 已拆分数量 |
| 47 | ffirstinspectionstatus | 首检状态 | bpchar | 1 |  | √ | 'N' | 首检状态,枚举: N :空 A :待首检 B :首检中 C :首检完成 |
| 48 | ftotalsplitbaseqty | 已拆分基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分基本数量 |
| 49 | fnotreportbsqty | 待汇报基本数量 | numeric | 23 | 10 | √ | 0 | 待汇报基本数量 |
| 50 | fisinspection | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 51 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 52 | frptqty | 关联汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联汇报数量 |
| 53 | foutwaqty | 退库基本数量 | numeric | 23 | 10 | √ | 0 | 退库基本数量 |
| 54 | frcvinhighlimit | 入库上限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 入库上限允差（%） |
| 55 | ffirstinspection | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 56 | fisconreportqty | 控制汇报数量 | bpchar | 1 |  | √ | '0' | 控制汇报数量 |
| 57 | fxkdemanddate | 订单需求日期 | timestamp | 0 |  |  | null | 订单需求日期 |
| 58 | freworkorderqty | 关联返工工单数量 | numeric | 23 | 10 | √ | 0 | 关联返工工单数量 |
| 59 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 60 | freportbsqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0 | 汇报基本数量 |
| 61 | frepmaxqty | 汇报上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限数量 |
| 62 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 63 | fxkoutwaqty | 退库数量 | numeric | 23 | 10 | √ | 0 | 退库数量 |
| 64 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 65 | ftransmittime | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 66 | frepmaxrate | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限允差（%） |
| 67 | fqualifiedbsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 68 | frepmaxbsqty | 汇报上限基本数量 | numeric | 23 | 10 | √ | 0 | 汇报上限基本数量 |
| 69 | frepairbsqty | 返修基本数量 | numeric | 23 | 10 | √ | 0 | 返修基本数量 |
| 70 | frepinwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工品入库数量 |
| 71 | frcvinlowlimit | 入库下限允差（%） | numeric | 23 | 10 | √ | 0.0000000000 | 入库下限允差（%） |
| 72 | finwarmax | 入库上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 入库上限基本数量 |
| 73 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 74 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 75 | fislastproceplanend | 末道工序完工 | bpchar | 1 |  | √ | '1' | 末道工序完工 |
| 76 | fbrokenqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 77 | fmanuseq | 生产顺序 | int8 | 64 |  | √ | 0 | 生产顺序 |
| 78 | fsettletime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 79 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 80 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 81 | facceptbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 82 | foutputoperation | 产出工序112 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 83 | fendworktime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 84 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 85 | fmtlcostbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |

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
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | fclosetype | 关闭类型 | varchar | 10 |  | √ | ' ' | 关闭类型,枚举: A :自动关闭 B :手工关闭 C :拆分关闭 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0.0000000000 | 成品率% |
| 7 | fbaseunitexpoutqty | 基本单位预计产出数量 | numeric | 23 | 10 | √ | 0 | 基本单位预计产出数量 |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | froutereplace | 工艺路线替代号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_routereplace |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 12 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 13 | fxkdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 15 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 16 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 17 | fmanftechstatus | 工序计划状态 | varchar | 30 |  | √ | ' ' | 工序计划状态,枚举: T :存在工序计划 F :不存在工序计划 |
| 18 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fsrcorderentryid | 源工单分录id | int8 | 64 |  | √ | 0 | 源工单分录id |
| 23 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 24 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 25 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线 mpdm_sfcprocessroute |
| 26 | fbeginbookdate | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 27 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 29 | fmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | 生产版本 pdm_manuversion |
| 30 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 34 | fexpoutqty | 预计产出数量 | numeric | 23 | 10 | √ | 0 | 预计产出数量 |
| 35 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 36 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 38 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 39 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 40 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 41 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 42 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 43 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 44 | fsrcsplitbillnumber | 来源拆分工单编码 | varchar | 50 |  | √ | ' ' | 来源拆分工单编码 |
| 45 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | 生产工单分录f7 pom_mftorder_f7 |
| 48 | festscrapqty | 预计报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预计报废数量 |
| 49 | fkittingtime | 齐套分析时间 | timestamp | 0 |  |  | null | 齐套分析时间 |
| 50 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 52 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 53 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 54 | fplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 55 | fpurqty | 下推采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推采购数量 |
| 56 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 57 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 58 | foprentryid | 工序计划分录id | int8 | 64 |  | √ | 0 | 工序计划分录id |
| 59 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 60 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 61 | fplanbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 62 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 63 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 64 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |

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
