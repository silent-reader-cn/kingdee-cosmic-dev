# 工序计划(废弃)-sfc_manftech

## 工序序列-子表 t_pom_manftprocessentry

- **表名称：** 工序序列-子表
- **表名：** t_pom_manftprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 | id |
| 3 | fprocessplanbegintime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 4 | fprocessplanouttime | 计划转出时间 | timestamp | 0 |  |  | null | 计划转出时间 |
| 5 | fprocessseqtype | 序列类型 | varchar | 30 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 6 | fprocessrelation | 并行关系 | varchar | 50 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :开始-结束 C :结束-开始 D :结束-结束 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fprocessoutput | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 10 | fprocessinput | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 11 | fprocessplanendtime | 计划结束时间 | timestamp | 0 |  |  | null | 计划结束时间 |
| 12 | fprocessseqqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 13 | fprocessremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fprocessinputdesc | 转入工序说明 | varchar | 50 |  | √ | ' ' | 转入工序说明 |
| 15 | fprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 16 | fprocessreference | 参照序列 | varchar | 50 |  | √ | ' ' | 参照序列 |
| 17 | fsourceseqid | 来源工序工序列ID | varchar | 50 |  | √ | ' ' | 来源工序工序列ID |
| 18 | fprocessoutputdesc | 转出工序说明 | varchar | 50 |  | √ | ' ' | 转出工序说明 |
| 19 | fprocessplanintime | 计划转入时间 | timestamp | 0 |  |  | null | 计划转入时间 |
| 20 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftprocessentry |  | fprocessentryid |
| 2 | idx_pom_manftprocessentry_fid |  | fid |

---

## 工序计划(废弃)-反写记录表 t_pom_mftorderentry_m_wb

- **表名称：** 工序计划(废弃)-反写记录表
- **表名：** t_pom_mftorderentry_m_wb

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
| 1 | idx_pom_mftorderentry_m_wb_fk |  | fid |
| 2 | pk_pom_mftorderentry_m_wb |  | fentryid |

---

## 工序计划(废弃)-关联追踪表 t_pom_mftorderentry_m_tc

- **表名称：** 工序计划(废弃)-关联追踪表
- **表名：** t_pom_mftorderentry_m_tc

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
| 1 | pk_pom_mftorderentry_m_tc |  | fid |
| 2 | idx_pom_mftorderentry_m_tc_tid |  | ftid |
| 3 | idx_pom_mftorderentry_m_tc_tbill |  | ftbillid |

---

## 工序计划(废弃)-主表 t_pom_mftorderentry_m

- **表名称：** 工序计划(废弃)-主表
- **表名：** t_pom_mftorderentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 3 | fproductionworkshopid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 5 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fparentplanid | 父工序计划ID | varchar | 50 |  | √ | ' ' | 父工序计划ID |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 14 | fmanufactureorder | 生产工单编号（废弃） | varchar | 50 |  | √ | ' ' | 生产工单编号（废弃） |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | ftransactiontypeid | 事务类型 | int8 | 64 |  | √ | 0 | [生产事务类型 mpdm_transactproduct](../mpdm_files/mpdm_transactproduct.md) |
| 17 | fmftentryseq | 生产工单行号 | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fplanfinishtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 24 | fparentseqid | 父工序序列ID | varchar | 50 |  | √ | ' ' | 父工序序列ID |
| 25 | fmanufactureorderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 26 | fplantype | 计划类型 | varchar | 30 |  | √ | ' ' | 计划类型,枚举: A :主计划 B :拆卡-首序 C :拆卡-中间工序 D :拆卡-选中序 |
| 27 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 28 | fplanstarttime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fschedulplanid | 排程方案 | int8 | 64 |  | √ | 0 | [生产事务类型 mpdm_transactproduct](../mpdm_files/mpdm_transactproduct.md) |
| 31 | fauxptyqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助单位数量 |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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

## 工序排程资源-子表 t_pom_manftschsubentry

- **表名称：** 工序排程资源-子表
- **表名：** t_pom_manftschsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fschresourceid | 资源编码 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 6 | fsourceresid | 来源工序活动计划ID | varchar | 50 |  | √ | ' ' | 来源工序活动计划ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftschsubentry |  | fdetailid |
| 2 | idx_pom_mftschsubent_fsubentid |  | fprocessentryid |

---

## 工序活动计划-子表 t_pom_manftactsubentry

- **表名称：** 工序活动计划-子表
- **表名：** t_pom_manftactsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 2 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 3 | factminformula1 | 最小值公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 4 | factactivityid | 活动编码 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 5 | factplanbegintime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | factstandardformulaid | 标准公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fprocessstage | 工序阶段 | varchar | 30 |  | √ | ' ' | 工序阶段,枚举: A :排队阶段 B :准备阶段 C :加工阶段 D :拆卸阶段 E :等待阶段 F :转移阶段 |
| 11 | factplantotalqty | 计划总量 | numeric | 23 | 10 | √ | 0.0000000000 | 计划总量 |
| 12 | factminformulaid | 最小值公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 13 | factresources | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 14 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: A :生产 B :成本 C :工资 |
| 15 | factplanfinishtime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fsourceactid | 来源工序活动计划ID | varchar | 50 |  | √ | ' ' | 来源工序活动计划ID |
| 18 | factstandardformula1id | 标准公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftactsubentry |  | fdetailid |
| 2 | idx_pom_mftactsubeny_fsubentid |  | fprocessentryid |

---

## 关联子实体-子表 t_pom_manftechentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_manftechentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | null |  |
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
| 1 | pk_pom_manftechentry_lk |  | fpkid |
| 2 | idx_pom_manftechentry_lk_fk |  | fprocessentryid |

---

## 工序活动汇报-子表 t_pom_manftrepsubentry

- **表名称：** 工序活动汇报-子表
- **表名：** t_pom_manftrepsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frepactualfinishtime | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 2 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fsrcentryid | 来源分录id | varchar | 50 |  | √ | ' ' | 来源分录id |
| 4 | frepactualqty | 实际总量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际总量 |
| 5 | frepactivityid | 活动编码 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 6 | frepresources | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 7 | frepactualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | frepbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftrepsubentry |  | fdetailid |
| 2 | idx_pom_mftrepsubent_fsubentid |  | fprocessentryid |

---

## 序列关系-子表 t_pom_manftrelationentry

- **表名称：** 序列关系-子表
- **表名：** t_pom_manftrelationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 | id |
| 3 | ftransferprocessname | 转入工序名称 | varchar | 50 |  | √ | ' ' | 转入工序名称 |
| 4 | frelationseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 5 | fplanturnouttime | 计划转出时间 | timestamp | 0 |  |  | null | 计划转出时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fturnoutprocessname | 转出工序名称 | varchar | 50 |  | √ | ' ' | 转出工序名称 |
| 9 | frelationparseq | 并行序列号 | varchar | 50 |  | √ | ' ' | 并行序列号 |
| 10 | frelationparseqname | 并行序列名称 | varchar | 50 |  | √ | ' ' | 并行序列名称 |
| 11 | ftransferprocessno | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 12 | fsourcerelid | 来源序列关系分录ID | varchar | 50 |  | √ | ' ' | 来源序列关系分录ID |
| 13 | fparallelration | 并行关系 | varchar | 30 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :结束-开始 C :结束-结束 D :开始-结束 |
| 14 | fplantransfertime | 计划转入时间 | timestamp | 0 |  |  | null | 计划转入时间 |
| 15 | fturnoutprocessno | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 16 | frelationname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fprocessentryid | fprocessentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manftrelationentry |  | fprocessentryid |
| 2 | idx_pom_manftrelationentry_fid |  | fid |

---

## 工序-分表 t_pom_manftechentry_f

- **表名称：** 工序-分表
- **表名：** t_pom_manftechentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprtotalunqualifiedqty | 已不合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已不合格数量 |
| 3 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 4 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | [采购业务组(封存) bd_pmoperatorgroup](../sbd_files/bd_pmoperatorgroup.md) |
| 6 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 7 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 8 | fpushoproutorderbaseqty | 下推工序委外订单基本数量 | numeric | 23 | 10 | √ | 0 | 下推工序委外订单基本数量 |
| 9 | fpushoproutorderqty | 下推工序委外订单数量 | numeric | 23 | 10 | √ | 0 | 下推工序委外订单数量 |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fmachiningtype | 加工类型 | varchar | 30 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 12 | ffloorratio | 汇报下限比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限比例(%) |
| 13 | fpurordernumber | 采购订单选单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 采购订单选单数量 |
| 14 | fentrymaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fentrustrinqty | 受托工单合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 受托工单合格品入库基本数量 |
| 16 | ftotaldownqty | 已采购申请数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购申请数量 |
| 17 | fentrustorderqty | 下推受托工单基本数量 | numeric | 23 | 10 | √ | 0 | 下推受托工单基本数量 |
| 18 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fsettlementcoefficient | 结算系数 | numeric | 23 | 10 | √ | 0.0000000000 | 结算系数 |
| 20 | fpurapplynumber | 采购申请选单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 采购申请选单数量 |
| 21 | ftotaloproutorderqty | 已工序委外订单数量 | numeric | 23 | 10 | √ | 0 | 已工序委外订单数量 |
| 22 | fpurchasepersonid | 采购员(暂时不用) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fentrustedorderqty | 已受托工单基本数量 | numeric | 23 | 10 | √ | 0 | 已受托工单基本数量 |
| 24 | ftotaloproutorderbaseqty | 已工序委外订单基本数量 | numeric | 23 | 10 | √ | 0 | 已工序委外订单基本数量 |
| 25 | flockqty | 锁定数量 | numeric | 23 | 10 | √ | 0.0000000000 | 锁定数量 |
| 26 | fentrustdinqty | 受托工单报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 受托工单报废品入库基本数量 |
| 27 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 29 | fentrustfinqty | 受托工单不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 受托工单不合格品入库基本数量 |
| 30 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fsettlementunitid | 结算单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

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

## 工序-分表 t_pom_manftechentry_e

- **表名称：** 工序-分表
- **表名：** t_pom_manftechentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscripprice | 废料单价 | numeric | 23 | 10 | √ | 0.0000000000 | 废料单价 |
| 3 | foprtotalqualifiedbaseqty | 已合格基本数量 | numeric | 23 | 10 | √ | 0 | 已合格基本数量 |
| 4 | foprtotalreportbaseqty | 已普通汇报基本数量 | numeric | 23 | 10 | √ | 0 | 已普通汇报基本数量 |
| 5 | fstoragepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 6 | ffloorqty | 汇报下限数量 | numeric | 23 | 10 | √ | 0 | 汇报下限数量 |
| 7 | foprrepairedbaseqty | 已返修基本数量 | numeric | 23 | 10 | √ | 0 | 已返修基本数量 |
| 8 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 9 | ffirstinspection | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 10 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工序数量 |
| 11 | foprtotalreceivebaseqty | 已让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 已让步接收基本数量 |
| 12 | fpushpurbillqty | 下推采购申请/订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推采购申请/订单数量 |
| 13 | foprtotalreworkqty | 已返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已返工数量 |
| 14 | foprtotaljunkqty | 已报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已报废数量 |
| 15 | fschedulingcalendar | 排程工厂日历 | int8 | 64 |  | √ | 0 | [生产日历 mpdm_calendar](../mpdm_files/mpdm_calendar.md) |
| 16 | foprtotalwastebaseqty | 已工废基本数量 | numeric | 23 | 10 | √ | 0 | 已工废基本数量 |
| 17 | fpushreportbaseqty | 下推普通汇报基本数量 | numeric | 23 | 10 | √ | 0 | 下推普通汇报基本数量 |
| 18 | fpushreworkreportqty | 下推返工汇报数量 | numeric | 23 | 10 | √ | 0 | 下推返工汇报数量 |
| 19 | foprtotaljunkbaseqty | 已报废基本数量 | numeric | 23 | 10 | √ | 0 | 已报废基本数量 |
| 20 | fscriptaxprice | 废料含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 废料含税单价 |
| 21 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 |  |
| 22 | freworkreportqty | 已返工汇报数量 | numeric | 23 | 10 | √ | 0 | 已返工汇报数量 |
| 23 | ffirstinspectioncontrol | 首检控制方式 | varchar | 30 |  | √ | ' ' | 首检控制方式,枚举: A :严格控制 B :非严格控制 |
| 24 | fpushreportqty | 下推普通汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推普通汇报数量 |
| 25 | foprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 26 | freworkreportbaseqty | 已返工汇报基本数量 | numeric | 23 | 10 | √ | 0 | 已返工汇报基本数量 |
| 27 | foperationunitid | 工序单位（弃用） | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | foprtotaloutbaseqty | 已转出基本数量 | numeric | 23 | 10 | √ | 0 | 已转出基本数量 |
| 29 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0.0000000000 | 表头数量 |
| 30 | foprtotalreceiveqty | 已让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已让步接收数量 |
| 31 | fwastetaxprice | 工废含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 工废含税单价 |
| 32 | fwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0.0000000000 | 工废单价 |
| 33 | fupperqty | 汇报上限数量 | numeric | 23 | 10 | √ | 0 | 汇报上限数量 |
| 34 | foprtotalmaterialbaseqty | 已料废基本数量 | numeric | 23 | 10 | √ | 0 | 已料废基本数量 |
| 35 | finspectiontype | 检验方式 | varchar | 30 |  | √ | '1011' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 36 | foprtotalinbaseqty | 已转入基本数量 | numeric | 23 | 10 | √ | 0 | 已转入基本数量 |
| 37 | fpushreworkreportbaseqty | 下推返工汇报基本数量 | numeric | 23 | 10 | √ | 0 | 下推返工汇报基本数量 |
| 38 | fupperratio | 汇报上限比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限比例(%) |
| 39 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | foprtotalreworkbaseqty | 已返工基本数量 | numeric | 23 | 10 | √ | 0 | 已返工基本数量 |
| 41 | ffirstinspectionstatus | 首检状态 | varchar | 30 |  | √ | ' ' | 首检状态,枚举: A :待首检 C :首检完成 N :不通过 |
| 42 | fcollaborative | 协作工序 | bpchar | 1 |  | √ | '0' | 协作工序 |
| 43 | fworkstationid | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 44 | freworkedreworkqty | 返工汇报已返工数量 | numeric | 23 | 10 | √ | 0 | 返工汇报已返工数量 |

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

## 关联子实体-子表 t_pom_mftorderentry_m_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mftorderentry_m_lk

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
| 1 | pk_pom_mftorderentry_m_lk |  | fpkid |
| 2 | idx_pom_mftorderentry_m_lk_fk |  | fid |

---

## 工序-子表 t_pom_manftechentry

- **表名称：** 工序-子表
- **表名：** t_pom_manftechentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprplanbegintime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 3 | foprtotaloutqty | 已转出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已转出数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsubentryid | fsubentryid | int8 | 64 |  | √ | 0 |  |
| 6 | foprtotalqualifiedqty | 已合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已合格数量 |
| 7 | foproverlapqty | 重叠批量 | numeric | 23 | 10 | √ | 0.0000000000 | 重叠批量 |
| 8 | foprproductionqty | 生产单位工序数量 | numeric | 23 | 10 | √ | 0.0000000000 | 生产单位工序数量 |
| 9 | foprrepairedqty | 已返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已返修数量 |
| 10 | foprnonum | 工序号（数字） | int8 | 64 |  | √ | 0 | 工序号（数字） |
| 11 | fbasebatchqty | 基本批量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本批量 |
| 12 | foprworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 13 | foprworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 14 | foprtimeunit | 加工时间单位 | varchar | 30 |  | √ | ' ' | 加工时间单位,枚举: A :分钟 B :秒 |
| 15 | foprparentnum | 工序序列（数字） | int8 | 64 |  | √ | 0 | 工序序列（数字） |
| 16 | foproperationid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 17 | foprtotalmaterialqty | 已料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已料废数量 |
| 18 | foprsuggestsplitqty | 建议拆分数 | numeric | 23 | 10 | √ | 0.0000000000 | 建议拆分数 |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | foprissplit | 是否拆分排程 | bpchar | 1 |  | √ | '0' | 是否拆分排程 |
| 21 | foprsourcetype | 工序来源类型 | varchar | 30 |  | √ | ' ' | 工序来源类型,枚举: A :工艺路线 B :人工新增 |
| 22 | foprorgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | foprunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | foprtotalsplitbaseqty | 已拆分/改制基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分/改制基本数量 |
| 25 | ftotalsplitqty | 已拆分/改制数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已拆分/改制数量 |
| 26 | foprtotalreportqty | 已普通汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已普通汇报数量 |
| 27 | foproverlaptimeunit | 重叠时间单位 | varchar | 30 |  | √ | ' ' | 重叠时间单位,枚举: A :分钟 B :秒 |
| 28 | foprtotalconcessionqty | 已让步数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已让步数量 |
| 29 | foprearliestfinishtime | 最早完工时间 | timestamp | 0 |  |  | null | 最早完工时间 |
| 30 | foprtotalinqty | 已转入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已转入数量 |
| 31 | foprisprocessoverlap | 是否工序重叠 | bpchar | 1 |  | √ | '0' | 是否工序重叠 |
| 32 | foprminworktime | 最小加工时间 | numeric | 23 | 10 | √ | 0.0000000000 | 最小加工时间 |
| 33 | foprstandardqty | 工序标准数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工序标准数量 |
| 34 | foprqty | 工序计划数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工序计划数量 |
| 35 | foverlapunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | foprparent | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 37 | fopractualsplitqty | 实际拆分数 | numeric | 23 | 10 | √ | 0.0000000000 | 实际拆分数 |
| 38 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 39 | foprtotalwasteqty | 已工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已工废数量 |
| 40 | fparentoprid | 父工序工序ID | varchar | 50 |  | √ | ' ' | 父工序工序ID |
| 41 | foprsourceentryid | 工艺路线工序ID | varchar | 50 |  | √ | ' ' | 工艺路线工序ID |
| 42 | fprocessentryid | fprocessentryid | int8 | 64 |  | √ | 0 | id |
| 43 | foprlatestfinishtime | 最晚完工时间 | timestamp | 0 |  |  | null | 最晚完工时间 |
| 44 | foprminoverlaptime | 重叠最小时间 | numeric | 23 | 10 | √ | 0.0000000000 | 重叠最小时间 |
| 45 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | [工序控制策略(废弃) mpdm_proctrlstrategy](../mpdm_files/mpdm_proctrlstrategy.md) |
| 46 | foprinvalid | 作废 | bpchar | 1 |  | √ | '0' | 作废 |
| 47 | foprtotalscrapqty | 已报废数量(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 已报废数量(废弃) |
| 48 | foprplanfinishtime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 49 | foprstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :创建 B :计划 C :计划确认 D :下达 E :开工 F :完工 G :关闭 |
| 50 | foprearliestbegintime | 最早开始时间 | timestamp | 0 |  |  | null | 最早开始时间 |
| 51 | foprlatestbegintime | 最晚开始时间 | timestamp | 0 |  |  | null | 最晚开始时间 |

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
