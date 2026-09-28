# 生产汇报单-pom_mftorderreport

## 生产汇报单-主表 t_pom_mftorderreport

- **表名称：** 生产汇报单-主表
- **表名：** t_pom_mftorderreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | freportdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 8 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :检修工单手工创建 B :收工操作创建 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fstaffreport | 人员汇报 | varchar | 30 |  | √ | ' ' | 人员汇报,枚举: qty :按数量 cooportion :按比例 hours :按工时 |
| 13 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 17 | fbilltypeid | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 10020 :工序汇报单 10030 :生产汇报单 |
| 18 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorderreport_fbillno |  | fbillno |
| 2 | pk_pom_mftorderreport |  | fid |

---

## 数量汇报-多语言表 t_pom_mftreportsummary_l

- **表名称：** 数量汇报-多语言表
- **表名：** t_pom_mftreportsummary_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | fremark | varchar | 50 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftreportsummary_l_0 |  | fentryid,flocaleid |
| 2 | pk_pom_mftreportsummary_l |  | fpkid |

---

## 生产汇报单-反写记录表 t_pom_mftorderreport_wb

- **表名称：** 生产汇报单-反写记录表
- **表名：** t_pom_mftorderreport_wb

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
| 1 | pk_pom_mftorderreport_wb |  | fentryid |
| 2 | idx_pom_mftorderreport_wb_fk |  | fid |

---

## 数量汇报-分表 t_pom_mftreportsummary_a

- **表名称：** 数量汇报-分表
- **表名：** t_pom_mftreportsummary_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funqualifyrelwarebaseqty | 不合格品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品关联入库基本数量 |
| 3 | fpushcheckbillqty | 关联检验数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联检验数量 |
| 4 | flocation | 入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 5 | ffirstinspection | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 6 | fqualifyrelwareqty | 合格品关联入库数量 | numeric | 23 | 10 | √ | 0 | 合格品关联入库数量 |
| 7 | fconcesionbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收基本数量 |
| 8 | fbrokenbsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 9 | fscrappedrelwareqty | 报废品关联入库数量 | numeric | 23 | 10 | √ | 0 | 报废品关联入库数量 |
| 10 | frepairbsqty | 返修基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修基本数量 |
| 11 | fmaterielinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 12 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 14 | fqualifyrelwarebaseqty | 合格品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品关联入库基本数量 |
| 15 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修数量 |
| 16 | fbrokenqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 17 | fconcesionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 18 | fpushdownwareqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联入库基本数量 |
| 19 | fscrappedrelwarebaseqty | 报废品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品关联入库基本数量 |
| 20 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 21 | fischeckmaterial | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 22 | funqualifyrelwareqty | 不合格品关联入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品关联入库数量 |
| 23 | fisurgent | 是否加急 | bpchar | 1 |  | √ | '0' | 是否加急 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fpushdownwareprdqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 26 | fcheckenddate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 27 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mftreportsummary_a |  | fentryid |
| 2 | idx_pom_mftreportsummary_a_fid |  | fid |

---

## 生产汇报单-多语言表 t_pom_mftorderreport_l

- **表名称：** 生产汇报单-多语言表
- **表名：** t_pom_mftorderreport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorderreport_l_0 |  | fid,flocaleid |
| 2 | pk_pom_mftorderreport_l |  | fpkid |

---

## 子单据体汇报人员-子表 t_pom_mftreporter

- **表名称：** 子单据体汇报人员-子表
- **表名：** t_pom_mftreporter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fclosetime | 收工时间 | timestamp | 0 |  |  | null | 收工时间 |
| 2 | fuserno | 操作人员工号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 3 | frepworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fopactivity | 业务活动 | varchar | 50 |  | √ | ' ' | 业务活动,枚举: A :维修 B :检验 |
| 5 | froleid | 项目角色 | int8 | 64 |  | √ | 0 | 项目角色 fmm_projectrole |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | factconsumedhours | 实际消耗工时 | numeric | 23 | 10 | √ | 0 | 实际消耗工时 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fproportion | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |
| 11 | fqtyfield | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 12 | fstarttime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftreporter_fentryid |  | fentryid |
| 2 | pk_pom_mftreporter |  | fdetailid |

---

## WBS-多选基础资料表 t_pom_mroreportwbs

- **表名称：** WBS-多选基础资料表
- **表名：** t_pom_mroreportwbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | WBS pmts_wbs |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroreportwbs_fk |  | fentryid |
| 2 | pk_pom_mroreportwbs |  | fpkid |

---

## 项目任务-多选基础资料表 t_pom_mroreporttask

- **表名称：** 项目任务-多选基础资料表
- **表名：** t_pom_mroreporttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroreporttask_fk |  | fentryid |
| 2 | pk_pom_mroreporttask |  | fpkid |

---

## 数量汇报-子表 t_pom_mftreportsummary

- **表名称：** 数量汇报-子表
- **表名：** t_pom_mftreportsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fstaworhours | 单位标准工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 单位标准工时(工时汇报) |
| 4 | forgfield | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | fmanufacturebillrow | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | flabworprehours | 人工准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工准备工时(工时汇报) |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fcheckedqty | 检验数量 | numeric | 23 | 10 | √ | 0.0000000000 | 检验数量 |
| 12 | facttotprohours | 实际生产总工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 实际生产总工时(工时汇报) |
| 13 | fplanconsumedhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 14 | freporttype | 汇报类型 | varchar | 30 |  | √ | ' ' | 汇报类型,枚举: 10080 :有效工时 10090 :无效工时 10100 :中性工时 |
| 15 | fisautowarehouse | 是否自动入库 | bpchar | 1 |  | √ | '0' | 是否自动入库 |
| 16 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工基本数量 |
| 17 | ftotalworkhours | 预计生产总工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 预计生产总工时(工时汇报) |
| 18 | fmanufacturebill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 19 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 20 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 21 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fqualifywareprdqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 23 | fscrapqty | 料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废数量 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 26 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废基本数量 |
| 27 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 28 | fscrappedwareprdqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 29 | fscrapbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废基本数量 |
| 30 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废数量 |
| 31 | fcompletqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 32 | fmachprehours | 机器准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器准备工时(工时汇报) |
| 33 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 34 | foprunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | ftimestop | 结束时间(工时汇报) | timestamp | 0 |  |  | null | 结束时间(工时汇报) |
| 36 | ftimeunit | 时间单位(工时汇报) | varchar | 30 |  | √ | ' ' | 时间单位(工时汇报),枚举: hour :小时 minute :分钟 second :秒 |
| 37 | fmacworhours | 机器实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器实作工时(工时汇报) |
| 38 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | ftotalconsumedhours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 41 | funqualifywareprdqty | 不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库数量 |
| 42 | fmanufactureentryid | fmanufactureentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fteamsgroups | 班组(工时汇报) | int8 | 64 |  | √ | 0 | 班组 mpdm_classgroup |
| 44 | fmatertype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 45 | fqualifywareqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 46 | ftotalinspectionhours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 47 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 48 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 49 | fcheckqty | 待检数量 | numeric | 23 | 10 | √ | 0.0000000000 | 待检数量 |
| 50 | fmftentryid | 生产工单分录id | varchar | 50 |  | √ | ' ' | 生产工单分录id |
| 51 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 52 | fscrappedwareqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 53 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 54 | fcompletbsqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报基本数量 |
| 55 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 56 | fmaterialcode | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 57 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 58 | fscrappedbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废基本数量 |
| 59 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 60 | fbackflishflag | 倒冲标识 | varchar | 30 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 61 | fpersonnel | 人员(工时汇报) | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 62 | fqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 63 | funqualifywareqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 64 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 65 | fhourconsumptionrate | 工时消耗率（%） | numeric | 23 | 10 | √ | 0 | 工时消耗率（%） |
| 66 | ftimeon | 开始时间(工时汇报) | timestamp | 0 |  |  | null | 开始时间(工时汇报) |
| 67 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 68 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 69 | fqualifybsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格基本数量 |
| 70 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 71 | fscrappedqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 72 | flabworkhours | 人工实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工实作工时(工时汇报) |
| 73 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mftreportsummary |  | fentryid |
| 2 | idx_portentry_ftracknumber |  | ftracknumberid |
| 3 | idx_pom_mftreportsummary_fid |  | fid |
| 4 | idx_portentry_fconfiguredcode |  | fconfiguredcodeid |

---

## 生产汇报单-关联追踪表 t_pom_mftorderreport_tc

- **表名称：** 生产汇报单-关联追踪表
- **表名：** t_pom_mftorderreport_tc

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
| 1 | idx_pom_mftorderreport_tc_tid |  | ftid |
| 2 | idx_pom_mftorderreport_tc_tbill |  | ftbillid |
| 3 | pk_pom_mftorderreport_tc |  | fid |

---

## 子单据体活动-子表 t_pom_mftreportactivity

- **表名称：** 子单据体活动-子表
- **表名：** t_pom_mftreportactivity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factihours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 2 | frepactualqty | 实际总量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际总量 |
| 3 | factstandardformulaid | 活动公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frepbaseqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 6 | factchours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 7 | frepactualfinishtime | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 8 | frepactivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 9 | frepresources | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 10 | frepactualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 11 | frepactivityunitid | 活动单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mftreportactivity |  | fdetailid |
| 2 | idx_pom_mftreportactivity_feid |  | fentryid |

---

## 关联子实体-子表 t_pom_mftreportsummary_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mftreportsummary_lk

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
| 1 | idx_pom_mftreportsummary_lk_fk |  | fentryid |
| 2 | pk_pom_mftreportsummary_lk |  | fpkid |
