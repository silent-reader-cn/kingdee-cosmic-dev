# 工序汇报单(废弃)-sfc_processreportbill

## 工序汇报单(废弃)-主表 t_sfc_processreport

- **表名称：** 工序汇报单(废弃)-主表
- **表名：** t_sfc_processreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fischargeoffed | fischargeoffed | bpchar | 1 |  | √ | '0' |  |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | freportdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 9 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :检修工序计划手工创建 B :收工操作创建 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fstaffreport | 人员汇报 | varchar | 30 |  | √ | ' ' | 人员汇报,枚举: qty :按数量 cooportion :按比例 hours :按工时 |
| 14 | fbasedatafield | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 15 | freporttype | freporttype | varchar | 30 |  | √ | ' ' |  |
| 16 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fchekcoopration | 协作工序 | bpchar | 1 |  | √ | '0' | 协作工序 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 21 | fbilltypeid | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 10020 :工序汇报单 10030 :工单汇报单 |
| 22 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processreport |  | fid |
| 2 | idx_sfc_processreport_fk |  | fbillno |

---

## 活动-子表 t_sfc_subreportactivity

- **表名称：** 活动-子表
- **表名：** t_sfc_subreportactivity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factihours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 2 | frepactivityunit | 活动单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | frepactualqty | 实际总量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际总量 |
| 4 | fsourceid | 源单分录id | varchar | 50 |  | √ | ' ' | 源单分录id |
| 5 | factstandardformulaid | 活动公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frepbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 8 | factchours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 9 | frepactualfinishtime | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 10 | frepactivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 11 | frepresources | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 12 | frepactualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_subreportactivity_fk |  | fentryid |
| 2 | pk_sfc_subreportactivity |  | fdetailid |

---

## 工序汇报单(废弃)-关联追踪表 t_mpdm_processreport_tc

- **表名称：** 工序汇报单(废弃)-关联追踪表
- **表名：** t_mpdm_processreport_tc

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
| 1 | pk_mpdm_processreport_tc |  | fid |
| 2 | idx_mpdm_processreport_tc_tbill |  | ftbillid |
| 3 | idx_mpdm_processreport_tc_tid |  | ftid |

---

## 关联子实体-子表 t_mpdm_processreport_s_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_processreport_s_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freworkqty_old | 返工数量_原始携带值 | numeric | 23 | 10 |  | null | 返工数量_原始携带值 |
| 2 | ftotalcompletqty_old | 累计汇报数量_原始携带值 | numeric | 23 | 10 |  | null | 累计汇报数量_原始携带值 |
| 3 | ftotalreworkqty | 累计返工数量_确认携带值 | numeric | 23 | 10 |  | null | 累计返工数量_确认携带值 |
| 4 | fscrapqty | 料废数量_确认携带值 | numeric | 23 | 10 |  | null | 料废数量_确认携带值 |
| 5 | fcompletqty_old | 汇报数量_原始携带值 | numeric | 23 | 10 |  | null | 汇报数量_原始携带值 |
| 6 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fqualifyqty | 合格数量_确认携带值 | numeric | 23 | 10 |  | null | 合格数量_确认携带值 |
| 9 | fworkwasteqty | 工废数量_确认携带值 | numeric | 23 | 10 |  | null | 工废数量_确认携带值 |
| 10 | ftotalscrapqty_old | 累计废料数量_原始携带值 | numeric | 23 | 10 |  | null | 累计废料数量_原始携带值 |
| 11 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 12 | fcompletqty | 汇报数量_确认携带值 | numeric | 23 | 10 |  | null | 汇报数量_确认携带值 |
| 13 | fqualifyqty_old | 合格数量_原始携带值 | numeric | 23 | 10 |  | null | 合格数量_原始携带值 |
| 14 | fscrapqty_old | 料废数量_原始携带值 | numeric | 23 | 10 |  | null | 料废数量_原始携带值 |
| 15 | ftotalcompletqty | 累计汇报数量_确认携带值 | numeric | 23 | 10 |  | null | 累计汇报数量_确认携带值 |
| 16 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 17 | freworkqty | 返工数量_确认携带值 | numeric | 23 | 10 |  | null | 返工数量_确认携带值 |
| 18 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 19 | ftotalscrapqty | 累计废料数量_确认携带值 | numeric | 23 | 10 |  | null | 累计废料数量_确认携带值 |
| 20 | fworkwasteqty_old | 工废数量_原始携带值 | numeric | 23 | 10 |  | null | 工废数量_原始携带值 |
| 21 | ftotalreworkqty_old | 累计返工数量_原始携带值 | numeric | 23 | 10 |  | null | 累计返工数量_原始携带值 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_processreport_s_lk |  | fpkid |
| 2 | idx_mpdm_processreport_s_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_mpdm_processreport_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_processreport_lk

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
| 1 | pk_mpdm_processreport_lk |  | fpkid |
| 2 | idx_mpdm_processreport_lk_fk |  | fid |

---

## 完工入库-子表 t_sfc_subinstorage

- **表名称：** 完工入库-子表
- **表名：** t_sfc_subinstorage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmatertype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 2 | fbadconformityqty | 不合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格数量 |
| 3 | fqualifiedinqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftotalwarehouseqty | 累计入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计入库数量 |
| 6 | forderentryid | 生产工单分录ID | varchar | 50 |  | √ | ' ' | 生产工单分录ID |
| 7 | fmanufacturerow | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 8 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | ftotalqualifystorageqty | 累计合格入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计合格入库数量 |
| 11 | finwarehouseorg | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fscrapinqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 13 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | fposition | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 15 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fmanufacturenun | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 18 | fbadqualifiedinqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 19 | fpushwarehouseqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推入库基本数量 |
| 20 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废基本数量 |
| 21 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | fproduceunitid | 生产计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fqualifyqty | 合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格基本数量 |
| 24 | funitfield | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | ftotalscrapstorageqty | 累计报废入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计报废入库数量 |
| 27 | fconformityqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 28 | fdiscardqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 29 | fbadqualifyqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格基本数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_subinstorage |  | fdetailid |
| 2 | idx_sfc_subinstorage_fentryid |  | fentryid |

---

## 子单据体汇报人员-子表 t_sfc_subrepoperator

- **表名称：** 子单据体汇报人员-子表
- **表名：** t_sfc_subrepoperator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frepworkunit | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 2 | foperator | 操作人员工号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 3 | fopactivity | 业务活动 | varchar | 50 |  | √ | ' ' | 业务活动,枚举: A :维修 B :检验 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | factconsumedhours | 实际消耗工时 | numeric | 23 | 10 | √ | 0 | 实际消耗工时 |
| 6 | fqtyfield | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 7 | fstarttime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 8 | fclosetime | 收工时间 | timestamp | 0 |  |  | null | 收工时间 |
| 9 | fpersonnelindustry | 人员行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 10 | fuserno | 操作人员工号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 11 | fprojectroles | 项目角色 | int8 | 64 |  | √ | 0 | 项目角色 fmm_projectrole |
| 12 | factivehours | 有效工时（小时） | numeric | 23 | 10 | √ | 0 | 有效工时（小时） |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fproportion | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_subrepoperator |  | fdetailid |
| 2 | idx_sfc_subrepoperator_fentry |  | fentryid |

---

## 单据体汇报人员-子表 t_sfc_repoperator

- **表名称：** 单据体汇报人员-子表
- **表名：** t_sfc_repoperator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusernoid | 操作人员工号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fproportion | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |
| 6 | fqtyfield | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_repoperator |  | fentryid |
| 2 | idx_sfc_repoperator_fid |  | fid |

---

## 汇总-子表 t_sfc_processrptent

- **表名称：** 汇总-子表
- **表名：** t_sfc_processrptent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalreworkqty | 累计返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计返工数量 |
| 3 | fwarehousepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 4 | fworkwastebaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 5 | fmanufacturebillrow | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcheckreworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 8 | freceivebaseqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 9 | freporttype | 汇报类型 | varchar | 30 |  | √ | ' ' | 汇报类型,枚举: 10080 :有效工时 10090 :无效工时 10100 :中性工时 |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fcompletbaseqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0 | 汇报基本数量 |
| 12 | fcheckreworkbaseqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 13 | fmanufacturebill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 14 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 15 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 16 | fscrapqty | 料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废数量 |
| 17 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 18 | freworkmethod | 返工方式 | varchar | 30 |  | √ | ' ' | 返工方式,枚举: 1 :直接返工 2 :返工工作台 |
| 19 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废数量 |
| 20 | fdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 21 | fcompletqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 22 | fconfirmoprstatus | 确认工序状态 | varchar | 30 |  | √ | ' ' | 确认工序状态,枚举: 10060 :手动完工 10070 :自动判断 10080 :最终汇报 |
| 23 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 24 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修数量 |
| 25 | ftotalcompletqty | 累计汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计汇报数量 |
| 26 | foprunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | finspectiontype | 检验方式 | varchar | 30 |  | √ | '1011' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 28 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 29 | ftotalscrapqty | 累计废料数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计废料数量 |
| 30 | fisreworkreport | 返工汇报 | bpchar | 1 |  | √ | '0' | 返工汇报 |
| 31 | fjunkqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fmanufactureentryid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录F7 sfc_mftorder_f7 |
| 34 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 35 | fmatertype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 36 | fqualifybaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 37 | freceiveqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 38 | frepairbaseqty | 返修基本数量 | numeric | 23 | 10 | √ | 0 | 返修基本数量 |
| 39 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 40 | ffirstinspection | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 41 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 42 | fsequnit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 43 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 44 | ftotalworkwasteqty | 累计工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计工废数量 |
| 45 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | 'sfc_manftech' | 来源单据实体 |
| 48 | fmanuinbillentryid | 完工入库分录ID | varchar | 50 |  | √ | ' ' | 完工入库分录ID |
| 49 | ftotalqualifyqty | 累计合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计合格数量 |
| 50 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 51 | fopra | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 52 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 53 | fqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 54 | fjunkbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 55 | fseqreportctrl | 汇报顺序控制 | varchar | 30 |  | √ | ' ' | 汇报顺序控制,枚举: 1005 :顺序汇报 1006 :告警 1007 :不控制 |
| 56 | fmfttechnics | 工序计划编号 | varchar | 50 |  | √ | ' ' | 工序计划编号 |
| 57 | foprentryid | 工序计划工序分录ID | varchar | 50 |  | √ | ' ' | 工序计划工序分录ID |
| 58 | fmanufactureid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 59 | finspectionbaseqty | 检验基本数量 | numeric | 23 | 10 | √ | 0 | 检验基本数量 |
| 60 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 61 | fpushinspectionbaseqty | 下推检验基本数量 | numeric | 23 | 10 | √ | 0 | 下推检验基本数量 |
| 62 | fscrapbaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_processrptent_fid |  | fid |
| 2 | idx_repentry_forderid |  | fmanufactureid |
| 3 | idx_repentry_foprentryid |  | foprentryid |
| 4 | pk_sfc_processrptent |  | fentryid |
| 5 | idx_repentry_forderentryid |  | fmanufactureentryid |
| 6 | idx_repentry_ftracknumber |  | ftracknumberid |
| 7 | idx_repentry_fconfiguredcode |  | fconfiguredcodeid |

---

## 联副产品-子表 t_sfc_otherproductrpt

- **表名称：** 联副产品-子表
- **表名：** t_sfc_otherproductrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foutputtype | 产出类型 | varchar | 30 |  | √ | ' ' | 产出类型,枚举: A :联产品 B :副产品 |
| 2 | freceiveqty | 让步接收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 让步接收数量 |
| 3 | fscrapqty | 料废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 料废数量 |
| 4 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fproduceunitid | 生产计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fsrcorderentryid | 工单分录ID | varchar | 50 |  | √ | ' ' | 工单分录ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格数量 |
| 9 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工废数量 |
| 10 | fcompletqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 11 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返修数量 |
| 14 | finwarehouseorg | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 返工数量 |
| 16 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 17 | fposition | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 18 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | fjunkqty | 报废数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废数量 |
| 21 | fsrcorderid | 工单ID | varchar | 50 |  | √ | ' ' | 工单ID |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_otherproductrpt |  | fdetailid |
| 2 | idx_sfc_otherproductrpt_fk |  | fentryid |

---

## 工序汇报单(废弃)-反写记录表 t_mpdm_processreport_wb

- **表名称：** 工序汇报单(废弃)-反写记录表
- **表名：** t_mpdm_processreport_wb

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
| 1 | idx_mpdm_processreport_wb_fk |  | fid |
| 2 | pk_mpdm_processreport_wb |  | fentryid |

---

## 工序汇报单(废弃)-多语言表 t_sfc_processreport_l

- **表名称：** 工序汇报单(废弃)-多语言表
- **表名：** t_sfc_processreport_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_processreport_fid |  | fid,flocaleid |
| 2 | pk_sfc_processreport_l |  | fpkid |

---

## 联副产品-多语言表 t_sfc_otherproductrpt_l

- **表名称：** 联副产品-多语言表
- **表名：** t_sfc_otherproductrpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremarks | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_otherproductrpt_l |  | fpkid |
| 2 | idx_sfc_otherproductrpt_l_0 |  | fdetailid,flocaleid |

---

## 汇总-分表 t_sfc_processrptent_m

- **表名称：** 汇总-分表
- **表名：** t_sfc_processrptent_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 3 | fworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | ftotalinspectionhours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 5 | feffectivehours | 有效工时 | numeric | 23 | 10 | √ | 0 | 有效工时 |
| 6 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 7 | factualstarttime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 8 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: D :下达 E :开工 F :完工 |
| 9 | fwbsid | WBS | int8 | 64 |  | √ | 0 | WBS pmts_wbs |
| 10 | fplanconsumedhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 11 | fmroorderentryid | 检修工单分录ID | int8 | 64 |  | √ | 0 | 检修工单分录F7(废弃) sfc_mroorder_f7 |
| 12 | fhourconsumptionrate | 工时消耗率（%） | numeric | 23 | 2 | √ | 0 | 工时消耗率（%） |
| 13 | foperationgroupid | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 14 | fstandardhours | 标准工时 | numeric | 23 | 10 | √ | 0 | 标准工时 |
| 15 | factualcompletiontime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 16 | ftaskid | 任务编码 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | ftotalconsumedhours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_processrptent_m |  | fentryid |
| 2 | idx_sfcprocessrptent_m_fid |  | fid |
| 3 | idx_sfcprorptent_m_fmroordert |  | fmroorderentryid |

---

## 汇总-多语言表 t_sfc_processrptent_l

- **表名称：** 汇总-多语言表
- **表名：** t_sfc_processrptent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremarks | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | '0' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processrptent_l |  | fpkid |
| 2 | idx_sfc_processrptent_fentry |  | fentryid,flocaleid |
