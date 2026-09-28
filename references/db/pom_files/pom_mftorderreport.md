# 生产汇报单-pom_mftorderreport

## 生产汇报单-主表 t_pom_mftorderreport

- **表名称：** 生产汇报单-主表
- **表名：** t_pom_mftorderreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_bj73_basedatafield | 汇报人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 9 :迁移生成 |
| 9 | freportdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 10 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :检修工单手工创建 B :收工操作创建 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fstaffreport | 人员汇报 | varchar | 30 |  | √ | ' ' | 人员汇报,枚举: qty :按数量 cooportion :按比例 hours :按工时 |
| 15 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 19 | fbilltypeid | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 10020 :工序汇报单 10030 :生产汇报单 |
| 20 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |

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
| 4 | flocation | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 5 | ffirstinspection | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 6 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 7 | fqualifyrelwareqty | 合格品关联入库数量 | numeric | 23 | 10 | √ | 0 | 合格品关联入库数量 |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fconcesionbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收基本数量 |
| 10 | fbrokenbsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 11 | fscrappedrelwareqty | 报废品关联入库数量 | numeric | 23 | 10 | √ | 0 | 报废品关联入库数量 |
| 12 | flinkinbaseqty | 关联检验基本数量 | numeric | 23 | 10 | √ | 0 | 关联检验基本数量 |
| 13 | frepairbsqty | 返修基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修基本数量 |
| 14 | fmaterielinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 15 | fcheckedbaseqty | 检验基本数量 | numeric | 23 | 10 | √ | 0 | 检验基本数量 |
| 16 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 18 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 19 | fqualifyrelwarebaseqty | 合格品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品关联入库基本数量 |
| 20 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修数量 |
| 21 | fbrokenqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 22 | fconcesionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 23 | fpushdownwareqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联入库基本数量 |
| 24 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 25 | fscrappedrelwarebaseqty | 报废品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品关联入库基本数量 |
| 26 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 27 | fischeckmaterial | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 28 | funqualifyrelwareqty | 不合格品关联入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品关联入库数量 |
| 29 | fisurgent | 是否加急 | bpchar | 1 |  | √ | '0' | 是否加急 |
| 30 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fpushdownwareprdqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 33 | fcheckenddate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 34 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 35 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

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
| 2 | fuserno | 操作人员工号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_manuperson](../mpdm_files/mpdm_manuperson.md) |
| 3 | frepworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fopactivity | 业务活动 | varchar | 50 |  | √ | ' ' | 业务活动,枚举: A :维修 B :检验 |
| 5 | froleid | 项目角色 | int8 | 64 |  | √ | 0 | [项目角色 fmm_projectrole](../mpdm_files/fmm_projectrole.md) |
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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [WBS pmts_wbs](../fmm_files/pmts_wbs.md) |
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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目任务清单 pmts_task](../fmm_files/pmts_task.md) |
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
| 2 | fworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fstaworhours | 单位标准工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 单位标准工时(工时汇报) |
| 4 | forgfield | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | fmanufacturebillrow | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 7 | forderid | 生产工单F7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | flabworprehours | 人工准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工准备工时(工时汇报) |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fcheckedqty | 检验数量 | numeric | 23 | 10 | √ | 0.0000000000 | 检验数量 |
| 13 | facttotprohours | 实际生产总工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 实际生产总工时(工时汇报) |
| 14 | fplanconsumedhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 15 | freporttype | 汇报类型 | varchar | 30 |  | √ | ' ' | 汇报类型,枚举: 10080 :有效工时 10090 :无效工时 10100 :中性工时 |
| 16 | fisautowarehouse | 是否自动入库 | bpchar | 1 |  | √ | '0' | 是否自动入库 |
| 17 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工基本数量 |
| 18 | ftotalworkhours | 预计生产总工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 预计生产总工时(工时汇报) |
| 19 | fisadd | 来源类型 | bpchar | 1 |  | √ | '0' | 来源类型,枚举: 0 :普通 1 :新增行 |
| 20 | fmanufacturebill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 21 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 22 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 23 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 24 | fqualifywareprdqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 25 | freportway | 汇报方式 | varchar | 5 |  | √ | 'A' | 汇报方式,枚举: A :入库汇报 B :生产汇报 |
| 26 | fscrapqty | 料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废数量 |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 29 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废基本数量 |
| 30 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 31 | fscrappedwareprdqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 32 | fscrapbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废基本数量 |
| 33 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废数量 |
| 34 | fcompletqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 35 | fmachprehours | 机器准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器准备工时(工时汇报) |
| 36 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 37 | foprunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | ftimestop | 结束时间(工时汇报) | timestamp | 0 |  |  | null | 结束时间(工时汇报) |
| 39 | ftimeunit | 时间单位(工时汇报) | varchar | 30 |  | √ | ' ' | 时间单位(工时汇报),枚举: hour :小时 minute :分钟 second :秒 |
| 40 | fmacworhours | 机器实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器实作工时(工时汇报) |
| 41 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | ftotalconsumedhours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 44 | funqualifywareprdqty | 不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库数量 |
| 45 | fmanufactureentryid | fmanufactureentryid | int8 | 64 |  | √ | 0 |  |
| 46 | fteamsgroups | 班组(工时汇报) | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 47 | fmatertype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 48 | fqualifywareqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 49 | ftotalinspectionhours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 50 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 51 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fcheckqty | 待检数量 | numeric | 23 | 10 | √ | 0.0000000000 | 待检数量 |
| 53 | fmftentryid | 生产工单分录id | varchar | 50 |  | √ | ' ' | 生产工单分录id |
| 54 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 55 | forderentryid | 生产工单分录F7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 56 | fscrappedwareqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 57 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 58 | fcompletbsqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报基本数量 |
| 59 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 60 | fmaterialcode | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 61 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 62 | fscrappedbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废基本数量 |
| 63 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 64 | fbackflishflag | 倒冲标识 | varchar | 30 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 65 | fpersonnel | 人员(工时汇报) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | fqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 67 | funqualifywareqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 68 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 69 | fk_bj73_basedatafield1 | fk_bj73_basedatafield1 | int8 | 64 |  | √ | 0 |  |
| 70 | fk_bj73_pricefield | 前处理 | numeric | 23 | 10 |  | null | 前处理 |
| 71 | fhourconsumptionrate | 工时消耗率（%） | numeric | 23 | 10 | √ | 0 | 工时消耗率（%） |
| 72 | ftimeon | 开始时间(工时汇报) | timestamp | 0 |  |  | null | 开始时间(工时汇报) |
| 73 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 74 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 75 | fqualifybsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格基本数量 |
| 76 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 77 | fscrappedqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 78 | flabworkhours | 人工实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工实作工时(工时汇报) |
| 79 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

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
| 3 | factstandardformulaid | 活动公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frepbaseqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 6 | factchours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 7 | frepactualfinishtime | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 8 | frepactivityid | 活动编码 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 9 | frepresources | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 10 | frepactualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 11 | frepactivityunitid | 活动单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
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
