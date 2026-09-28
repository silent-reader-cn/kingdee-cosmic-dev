# 排程结果表数据-mrp_pls_result

## 排程结果表数据-主表 t_mrp_pls_result

- **表名称：** 排程结果表数据-主表
- **表名：** t_mrp_pls_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterielcode | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fordercalculateqty | 订单计算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单计算数量 |
| 4 | fyieldrate | 成品率 | numeric | 23 | 10 | √ | 0.0000000000 | 成品率 |
| 5 | fprocessroutebillno | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 6 | fbillorder | 单据优先级 | int8 | 64 |  | √ | 0 | 单据优先级 |
| 7 | fstatus | 推单状态 | varchar | 50 |  | √ | ' ' | 推单状态,枚举: A :未推单 B :已推单 |
| 8 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 9 | fsourceorderbillno | 来源单据编号 | varchar | 30 |  | √ | ' ' | 来源单据编号 |
| 10 | fworkremainingqty | 班次余量 | numeric | 23 | 10 | √ | 0.0000000000 | 班次余量 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | forderinitialqty | 订单初始数量 | numeric | 23 | 10 | √ | 0.0000000000 | 订单初始数量 |
| 14 | fworkendtime | 结束时间 | int8 | 64 |  | √ | 0 | 结束时间 |
| 15 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 16 | fplantagsid | 计划标识 | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 17 | fsourceordertype | 来源单据类型编码 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 18 | fworkplsqty | 班次排产量 | numeric | 23 | 10 | √ | 0.0000000000 | 班次排产量 |
| 19 | forderremainingqty | 订单余量 | numeric | 23 | 10 | √ | 0 | 订单余量 |
| 20 | fmaterialplanid | 物料计划信息 | int8 | 64 |  | √ | 0 | 物料计划信息 mpdm_materialplan |
| 21 | fworkstarttime | 开始时间 | int8 | 64 |  | √ | 0 | 开始时间 |
| 22 | fworkshiftid | 班次编码 | int8 | 64 |  | √ | 0 | 班次 mpdm_workshifts |
| 23 | fworkpowerqty | 班次能力数量 | numeric | 23 | 10 | √ | 0.0000000000 | 班次能力数量 |
| 24 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 25 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 26 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fplsschemeid | 排程方案编码 | int8 | 64 |  | √ | 0 | 排程方案定义 mrp_pls_scheme |
| 28 | fworkcentre | 工作中心编码 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 29 | fplsoperationno | 排程运算号 | varchar | 50 |  | √ | ' ' | 排程运算号 |
| 30 | fyieldqty | 成品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 成品数量 |
| 31 | fbom | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 32 | fproductionorder | 生产顺序 | int8 | 64 |  | √ | 0 | 生产顺序 |
| 33 | fdateunit | 时长单位 | varchar | 36 |  | √ | ' ' | 时长单位,枚举: A :秒 B :分 C :时 D :天 |
| 34 | fplanpreparedate | 计划准备日期 | timestamp | 0 |  |  | null | 计划准备日期 |
| 35 | fplsplannerid | 排产计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fproductionorgid | 生产组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fproductionversion | 生产版本 | int8 | 64 |  | √ | 0 | 生产版本 pdm_manuversion |
| 38 | ftimeconsuming | 工作中心耗时 | int8 | 64 |  | √ | 0 | 工作中心耗时 |
| 39 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | fplsdate | 计划生产日期 | timestamp | 0 |  |  | null | 计划生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_pls_result |  | fplsschemeid,fplsoperationno,fsourceorderbillno |
| 2 | pk_t_mrp_pls_result |  | fid |
