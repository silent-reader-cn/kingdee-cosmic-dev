# 排程明细表-mrp_pls_detail

## 单据体-子表 t_mrp_pls_detail_entry

- **表名称：** 单据体-子表
- **表名：** t_mrp_pls_detail_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterielcode | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fordercalculateqty | 订单计算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单计算数量 |
| 4 | fwctimeconsuming | 工作中心耗时 | numeric | 23 | 10 | √ | 0.0000000000 | 工作中心耗时 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fyieldrate | 成品率 | numeric | 23 | 10 | √ | 0.0000000000 | 成品率 |
| 7 | fprocessroutebillno | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 8 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 9 | fsourceorderbillno | 来源单据编号 | varchar | 30 |  | √ | ' ' | 来源单据编号 |
| 10 | fworkremainingqty | 班次余量 | numeric | 23 | 10 | √ | 0.0000000000 | 班次余量 |
| 11 | forderinitialqty | 订单初始数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单初始数量 |
| 12 | fworkendtime | 结束时间 | int8 | 64 |  | √ | 0 | 结束时间 |
| 13 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 14 | fplantagsid | 计划标识 | int8 | 64 |  | √ | 0 | [计划标识 mpdm_plantag](../mpdm_files/mpdm_plantag.md) |
| 15 | fsourceordertype | 来源单据类型编码 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fworkplsqty | 班次排产量 | numeric | 23 | 10 | √ | 0.0000000000 | 班次排产量 |
| 17 | forderremainingqty | 订单余量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单余量 |
| 18 | fmaterialplanid | 物料计划信息 | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 19 | fworkstarttime | 开始时间 | int8 | 64 |  | √ | 0 | 开始时间 |
| 20 | fworkshiftid | 班次 | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 21 | fworkpowerqty | 班次能力数量 | numeric | 23 | 10 | √ | 0.0000000000 | 班次能力数量 |
| 22 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 23 | fworkcentre | 工作中心编码 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 24 | fyieldqty | 成品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 成品数量 |
| 25 | fbom | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 26 | fproductionorder | 生产顺序 | int8 | 64 |  | √ | 0 | 生产顺序 |
| 27 | fdateunit | 时长单位 | varchar | 36 |  | √ | ' ' | 时长单位,枚举: A :秒 B :分 C :时 D :天 |
| 28 | fplanpreparedate | 计划准备日期 | timestamp | 0 |  |  | null | 计划准备日期 |
| 29 | fplsplannerid | 排产计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fproductionorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fproductionversion | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | ftimeconsuming | ftimeconsuming | int8 | 64 |  | √ | 0 |  |
| 34 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fplsdate | 计划生产日期 | timestamp | 0 |  |  | null | 计划生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_pls_detail_entrya |  | fid,fseq |
| 2 | pk_t_mrp_pls_detail_entry |  | fentryid |
| 3 | idx_mrp_pls_detail_entry |  | fid,fsourceorderbillno |

---

## 排程明细表-主表 t_mrp_pls_detail

- **表名称：** 排程明细表-主表
- **表名：** t_mrp_pls_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplsoperationno | 排程运算号 | varchar | 50 |  | √ | ' ' | 排程运算号 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fplsscheme | 排程方案编码 | int8 | 64 |  | √ | 0 | [排程方案定义 mrp_pls_scheme](../mrp_files/mrp_pls_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_pls_detail |  | fplsoperationno |
| 2 | idx_mrp_pls_detaila |  | fplsoperationno,fcreatetime |
| 3 | pk_t_mrp_pls_detail |  | fid |
