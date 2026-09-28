# 派工单-sfc_sendwork

## 派工单-主表 t_sfc_sendwork

- **表名称：** 派工单-主表
- **表名：** t_sfc_sendwork

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsendworktype | 派工对象类型 | bpchar | 1 |  | √ | ' ' | 派工对象类型,枚举: A :设备 B :人员 C :团队 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fprocessorgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_sendwork |  | fid |
| 2 | idx_sfc_sendwork_billno |  | fbillno |

---

## 派工明细-分表 t_sfc_sendworkentry_a

- **表名称：** 派工明细-分表
- **表名：** t_sfc_sendworkentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumworkwastbaseqty | 累计工废基本数量 | numeric | 23 | 10 | √ | 0 | 累计工废基本数量 |
| 3 | fdamageproqty | 损耗生产数量 | numeric | 23 | 10 | √ | 0 | 损耗生产数量 |
| 4 | fsampledestoryproqty | 样本破坏生产数量 | numeric | 23 | 10 | √ | 0 | 样本破坏生产数量 |
| 5 | freportsbqty | 关联汇报数量 | numeric | 23 | 10 | √ | 0 | 关联汇报数量 |
| 6 | ftobereworkedbaseqty | 待返工基本数量 | numeric | 23 | 10 | √ | 0 | 待返工基本数量 |
| 7 | fdamagebaseqty | 损耗基本数量 | numeric | 23 | 10 | √ | 0 | 损耗基本数量 |
| 8 | fsumworkwastproqty | 累计工废生产数量 | numeric | 23 | 10 | √ | 0 | 累计工废生产数量 |
| 9 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 10 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 11 | ftobeinspectproqty | 待检生产数量 | numeric | 23 | 10 | √ | 0 | 待检生产数量 |
| 12 | fsumquabaseqyt | 累计合格基本数量 | numeric | 23 | 10 | √ | 0 | 累计合格基本数量 |
| 13 | freworkdrawqty | 关联返工数量 | numeric | 23 | 10 | √ | 0 | 关联返工数量 |
| 14 | fsumworkwastqty | 累计工废数量 | numeric | 23 | 10 | √ | 0 | 累计工废数量 |
| 15 | fsumstockwastproqty | 累计料废生产数量 | numeric | 23 | 10 | √ | 0 | 累计料废生产数量 |
| 16 | ftobereworkedqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 17 | ftobereworkedproqty | 待返工生产数量 | numeric | 23 | 10 | √ | 0 | 待返工生产数量 |
| 18 | ftobeinspectqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 19 | fcompletebaseqty | 完工基本单位数量 | numeric | 23 | 10 | √ | 0 | 完工基本单位数量 |
| 20 | ftobeinsbaseqty | 待检基本数量 | numeric | 23 | 10 | √ | 0 | 待检基本数量 |
| 21 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 22 | fcompleteproqty | 完工生产数量 | numeric | 23 | 10 | √ | 0 | 完工生产数量 |
| 23 | fsumstockwastbaseqty | 累计料废基本数量 | numeric | 23 | 10 | √ | 0 | 累计料废基本数量 |
| 24 | fsampledestorybaseqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 25 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 26 | fsumquaproqyt | 累计合格生产数量 | numeric | 23 | 10 | √ | 0 | 累计合格生产数量 |
| 27 | fsumquaqyt | 累计合格数量 | numeric | 23 | 10 | √ | 0 | 累计合格数量 |
| 28 | fdamageqty | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 29 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 31 | fsumstockwastqty | 累计料废数量 | numeric | 23 | 10 | √ | 0 | 累计料废数量 |
| 32 | fyetreworkedqty | 已返工数量 | numeric | 23 | 10 | √ | 0 | 已返工数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_sendworkentry_a |  | fentryid |
| 2 | idx_sfc_sendworkentry_a_id |  | fid |

---

## 派工明细-分表 t_sfc_sendworkentry_b

- **表名称：** 派工明细-分表
- **表名：** t_sfc_sendworkentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 3 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 4 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 5 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 6 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 7 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 8 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 10 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 11 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 12 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_sendworkentry_b_id |  | fid |
| 2 | pk_sfc_sendworkentry_b |  | fentryid |

---

## 派工单-反写记录表 t_sfc_sendwork_wb

- **表名称：** 派工单-反写记录表
- **表名：** t_sfc_sendwork_wb

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
| 1 | pk_sfc_sendwork_wb |  | fentryid |
| 2 | idx_sfc_sendwork_wb_fk |  | fid |

---

## 关联子实体-子表 t_sfc_sendworkentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_sendworkentry_lk

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
| 1 | pk_sfc_sendworkentry_lk |  | fpkid |
| 2 | idx_sfc_sendworkentry_lk_fk |  | fentryid |

---

## 派工单-关联追踪表 t_sfc_sendwork_tc

- **表名称：** 派工单-关联追踪表
- **表名：** t_sfc_sendwork_tc

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
| 1 | idx_sfc_sendwork_tc_tid |  | ftid |
| 2 | pk_sfc_sendwork_tc |  | fid |
| 3 | idx_sfc_sendwork_tc_tbill |  | ftbillid |

---

## 团队成员-子表 t_sfc_sendworkedetail

- **表名称：** 团队成员-子表
- **表名：** t_sfc_sendworkedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcgleader | 负责人 | bpchar | 1 |  | √ | ' ' | 负责人 |
| 2 | fworkratio | 工作量比例 | numeric | 23 | 10 | √ | 0 | 工作量比例 |
| 3 | fpersonid | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fproportion | 百分比 | numeric | 23 | 10 | √ | 0 | 百分比 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_sendworkedetail |  | fdetailid |
| 2 | idx_sfc_sendworkedetail |  | fentryid |

---

## 派工明细-子表 t_sfc_sendworkentry

- **表名称：** 派工明细-子表
- **表名：** t_sfc_sendworkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproplanid | 工序计划 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 3 | fpushsendworkqty | fpushsendworkqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 7 | fsendworkprodqty | 派工生产数量 | numeric | 23 | 10 | √ | 0 | 派工生产数量 |
| 8 | fentrycode | 派工明细条码 | varchar | 50 |  | √ | ' ' | 派工明细条码 |
| 9 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 10 | fequipmentid | 设备 | int8 | 64 |  | √ | 0 | [设备 sfc_equipment](../mpdm_files/sfc_equipment.md) |
| 11 | fworkid | 生产工单 | int8 | 64 |  | √ | 0 | 生产工单 pom_mftorder |
| 12 | fprojno | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fworkrowid | 工单分录id | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 15 | fmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 16 | fsendworkqty | 派工数量 | numeric | 23 | 10 | √ | 0 | 派工数量 |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 18 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 19 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | ftaskpreclosestatus | 任务关闭前状态 | bpchar | 1 |  | √ | ' ' | 任务关闭前状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 21 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 24 | fsendworkbaseqty | 派工基本数量 | numeric | 23 | 10 | √ | 0 | 派工基本数量 |
| 25 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 27 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 28 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 29 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 30 | fproduceteamid | 制造团队 | int8 | 64 |  | √ | 0 | [制造团队 mpdm_mftteam](../mpdm_files/mpdm_mftteam.md) |
| 31 | fproplanentryactid | 工序计划分录_活动 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 32 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 33 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 36 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_sendworkentry |  | fentryid |
| 2 | idx_sfc_sendworkentry_fid |  | fid |
