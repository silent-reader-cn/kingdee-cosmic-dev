# 基于时间的预测-mds_forecastbytime

## 章节号-多选基础资料表 t_mds_forecastbytime_ata

- **表名称：** 章节号-多选基础资料表
- **表名：** t_mds_forecastbytime_ata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [ATA章节号 mpdm_atachapterno](../mpdm_files/mpdm_atachapterno.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_forecastbytime_ata |  | fpkid |
| 2 | idx_mds_forecast_ata_id |  | fid |

---

## 基于时间的预测-主表 t_mds_forecastbytime

- **表名称：** 基于时间的预测-主表
- **表名：** t_mds_forecastbytime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factualintime | 预计进场时间 | timestamp | 0 |  |  | null | 预计进场时间 |
| 3 | freqtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 4 | favgdelivery | 平均交期 | numeric | 23 | 10 | √ | 0 | 平均交期 |
| 5 | flogid | 通用备货运算号 | int8 | 64 |  | √ | 0 | [通用备货运算日志 mds_generallog](../mds_files/mds_generallog.md) |
| 6 | fqcode | 季度代码 | varchar | 50 |  | √ | ' ' | 季度代码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fservicefactor | 服务系数 | numeric | 23 | 10 | √ | 0 | 服务系数 |
| 9 | fdelstandadev | 交期标准偏差 | numeric | 23 | 10 | √ | 0 | 交期标准偏差 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fusemonthcount | 使用频率 | int8 | 64 |  | √ | 0 | 使用频率 |
| 13 | frop | 再订货点(ROP) | numeric | 23 | 10 | √ | 0 | 再订货点(ROP) |
| 14 | factualleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | froq | 再订货量(ROQ) | numeric | 23 | 10 | √ | 0 | 再订货量(ROQ) |
| 17 | ftargetstock | 目标库存水平 | numeric | 23 | 10 | √ | 0 | 目标库存水平 |
| 18 | fqty | 总用量 | numeric | 23 | 10 | √ | 0 | 总用量 |
| 19 | favgactdelivery | 平均实际交期 | numeric | 23 | 10 | √ | 0 | 平均实际交期 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fquarterfactor | 季度系数 | numeric | 23 | 10 | √ | 0 | 季度系数 |
| 22 | faverageqty | 平均月用量 | numeric | 23 | 10 | √ | 0 | 平均月用量 |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fstockfactor | 库存系数 | numeric | 23 | 10 | √ | 0 | 库存系数 |
| 26 | fdaystandadev | 日标准用量偏差 | numeric | 23 | 10 |  | 0 | 日标准用量偏差 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fshelflife | 是否保质期 | bpchar | 1 |  | √ | '0' | 是否保质期 |
| 29 | fdeliveryfactor | 交期系数 | numeric | 23 | 10 | √ | 0 | 交期系数 |
| 30 | fisgeneral | 是否通用清单件 | bpchar | 1 |  | √ | '0' | 是否通用清单件 |
| 31 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 32 | fsafestock | 安全库存水平 | numeric | 23 | 10 | √ | 0 | 安全库存水平 |
| 33 | favgplandelivery | 平均计划交期 | numeric | 23 | 10 | √ | 0 | 平均计划交期 |
| 34 | faveragedayqty | 平均日用量 | numeric | 23 | 10 | √ | 0 | 平均日用量 |
| 35 | fislongcyclemater | 是否长周期物料 | bpchar | 1 |  | √ | '0' | 是否长周期物料 |
| 36 | fordercountall | 总打单次数 | int8 | 64 |  | √ | 0 | 总打单次数 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_forecast_log |  | flogid |
| 2 | pk_mds_forecastbytime |  | fid |
