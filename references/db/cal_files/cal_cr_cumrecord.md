# 存货消耗记录-cal_cr_cumrecord

## 单据体-子表 t_cal_cr_cumrecordentry

- **表名称：** 单据体-子表
- **表名：** t_cal_cr_cumrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fincalentryid | 来源核算单分录ID | int8 | 64 |  | √ | 0 | 来源核算单分录ID |
| 4 | finbillentryid | 来源单据分录行ID | int8 | 64 |  | √ | 0 | 来源单据分录行ID |
| 5 | fcalbilltype | 核算单类型 | varchar | 50 |  | √ | ' ' | 核算单类型,枚举: OUT :出库 IN :入库 |
| 6 | foutbizentityobjectid | 目标单业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foutbillid | 目标单据行ID | int8 | 64 |  | √ | 0 | 目标单据行ID |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fbaseunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | finbillid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 12 | foutbillno | 目标编码 | varchar | 50 |  | √ | ' ' | 目标编码 |
| 13 | finbillno | 来源编码 | varchar | 50 |  | √ | ' ' | 来源编码 |
| 14 | foutcalentryid | 目标核算单分录ID | int8 | 64 |  | √ | 0 | 目标核算单分录ID |
| 15 | finbizentityobjectid | 来源业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fsourcetype | 数据来源类型 | varchar | 50 |  | √ | ' ' | 数据来源类型,枚举: 0 :余额表 1 :核算成本记录 |
| 17 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | foutbillentryid | 目标单据分录行ID | int8 | 64 |  | √ | 0 | 目标单据分录行ID |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fbaseqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cr_cumrecordentry_fk |  | fid |
| 2 | pk_cal_cr_cumrecordentry |  | fentryid |

---

## 存货消耗记录-主表 t_cal_cr_cumrecord

- **表名称：** 存货消耗记录-主表
- **表名：** t_cal_cr_cumrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdividebasiskeystr | 划分依据值 | varchar | 255 |  | √ | ' ' | 划分依据值 |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 9 | fcaldimensionkey | 核算维度值key | varchar | 255 |  | √ | ' ' | 核算维度值key |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | frtpplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 14 | fcaldimensionkeystr | 核算维度值 | varchar | 255 |  | √ | ' ' | 核算维度值 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdividebasiskey | 划分依据值key | varchar | 255 |  | √ | ' ' | 划分依据值key |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_cr_cumrecord |  | fid |
| 2 | idx_cal_cr_cumrecord_cp |  | fcostaccountid,fperiodid |
