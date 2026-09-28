# 目标件清单-按时间-mds_targetmaterial_time

## 章节号-多选基础资料表 t_mds_targetm_time_ata

- **表名称：** 章节号-多选基础资料表
- **表名：** t_mds_targetm_time_ata

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
| 1 | pk_mds_targetm_time_ata |  | fpkid |
| 2 | idx_mds_targetm_ata_id |  | fid |

---

## 目标件清单-按时间-主表 t_mds_targetmaterial_time

- **表名称：** 目标件清单-按时间-主表
- **表名：** t_mds_targetmaterial_time

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factualintime | 预计进场时间 | timestamp | 0 |  |  | null | 预计进场时间 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fquarter2 | Q2 | bpchar | 1 |  | √ | '0' | Q2 |
| 5 | fquarter3 | Q3 | bpchar | 1 |  | √ | '0' | Q3 |
| 6 | fquarter4 | Q4 | bpchar | 1 |  | √ | '0' | Q4 |
| 7 | fmonthstandadev | 月标准用量偏差 | numeric | 23 | 10 |  | 0 | 月标准用量偏差 |
| 8 | flogid | 通用备货运算号 | int8 | 64 |  | √ | 0 | [通用备货运算日志 mds_generallog](../mds_files/mds_generallog.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fquarter1 | Q1 | bpchar | 1 |  | √ | '0' | Q1 |
| 11 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fbeforematerialnumber | 转换前物料编码 | varchar | 2000 |  | √ | ' ' | 转换前物料编码 |
| 14 | fqty | 总用量 | numeric | 23 | 10 | √ | 0 | 总用量 |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fconmtypename | 合同类型名称 | varchar | 2000 |  | √ | ' ' | 合同类型名称 |
| 17 | fdaystandadev12m | 12个月日标准用量偏差 | numeric | 23 | 10 |  | 0 | 12个月日标准用量偏差 |
| 18 | fordercount2 | 打单次数（M2） | int8 | 64 |  | √ | 0 | 打单次数（M2） |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fordercount1 | 打单次数（M1） | int8 | 64 |  | √ | 0 | 打单次数（M1） |
| 21 | fordercount4 | 打单次数（M4） | int8 | 64 |  | √ | 0 | 打单次数（M4） |
| 22 | fordercount3 | 打单次数（M3） | int8 | 64 |  | √ | 0 | 打单次数（M3） |
| 23 | fordercount6 | 打单次数（M6） | int8 | 64 |  | √ | 0 | 打单次数（M6） |
| 24 | fordercount5 | 打单次数（M5） | int8 | 64 |  | √ | 0 | 打单次数（M5） |
| 25 | fordercount8 | 打单次数（M8） | int8 | 64 |  | √ | 0 | 打单次数（M8） |
| 26 | fbeforeunitname | 转换前计量单位 | varchar | 2000 |  | √ | ' ' | 转换前计量单位 |
| 27 | faverageyearqty | 365日平均用量 | numeric | 23 | 10 | √ | 0 | 365日平均用量 |
| 28 | fordercount7 | 打单次数（M7） | int8 | 64 |  | √ | 0 | 打单次数（M7） |
| 29 | faverageqty12m | 12个月平均用量 | numeric | 23 | 10 | √ | 0 | 12个月平均用量 |
| 30 | fordercount9 | 打单次数（M9） | int8 | 64 |  | √ | 0 | 打单次数（M9） |
| 31 | faveragedayqty | 平均日用量 | numeric | 23 | 10 | √ | 0 | 平均日用量 |
| 32 | fmaterialchange | 是否物料转换 | bpchar | 1 |  | √ | '0' | 是否物料转换 |
| 33 | fislongcyclemater | 是否长周期物料 | bpchar | 1 |  | √ | '0' | 是否长周期物料 |
| 34 | fordercountall | 总打单次数 | int8 | 64 |  | √ | 0 | 总打单次数 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fmqty2 | 月用量（M2） | numeric | 23 | 10 | √ | 0 | 月用量（M2） |
| 38 | fmqty1 | 月用量（M1） | numeric | 23 | 10 | √ | 0 | 月用量（M1） |
| 39 | freqtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 40 | fmqty6 | 月用量（M6） | numeric | 23 | 10 | √ | 0 | 月用量（M6） |
| 41 | fmqty10 | 月用量（M10） | numeric | 23 | 10 | √ | 0 | 月用量（M10） |
| 42 | fmqty5 | 月用量（M5） | numeric | 23 | 10 | √ | 0 | 月用量（M5） |
| 43 | fmqty11 | 月用量（M11） | numeric | 23 | 10 | √ | 0 | 月用量（M11） |
| 44 | fmqty4 | 月用量（M4） | numeric | 23 | 10 | √ | 0 | 月用量（M4） |
| 45 | fmqty3 | 月用量（M3） | numeric | 23 | 10 | √ | 0 | 月用量（M3） |
| 46 | favgdelivery | 三年平均交期 | numeric | 23 | 10 | √ | 0 | 三年平均交期 |
| 47 | fmqty9 | 月用量（M9） | numeric | 23 | 10 | √ | 0 | 月用量（M9） |
| 48 | fmqty8 | 月用量（M8） | numeric | 23 | 10 | √ | 0 | 月用量（M8） |
| 49 | fmqty7 | 月用量（M7） | numeric | 23 | 10 | √ | 0 | 月用量（M7） |
| 50 | ftargetflag | 标识 | bpchar | 1 |  | √ | '0' | 标识 |
| 51 | fqcode | 季度代码 | varchar | 50 |  | √ | ' ' | 季度代码 |
| 52 | fstandadev12m | 12个月标准用量偏差 | numeric | 23 | 10 |  | 0 | 12个月标准用量偏差 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fconmtypenumber | 合同类型编码 | varchar | 2000 |  | √ | ' ' | 合同类型编码 |
| 55 | fcustosupplyqty | 客户供应用量 | numeric | 23 | 10 | √ | 0 | 客户供应用量 |
| 56 | fmqty12 | 月用量（M12） | numeric | 23 | 10 | √ | 0 | 月用量（M12） |
| 57 | fusemonthcount | 使用频率 | int8 | 64 |  | √ | 0 | 使用频率 |
| 58 | factualleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 59 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 60 | faverageqty | 平均月用量 | numeric | 23 | 10 | √ | 0 | 平均月用量 |
| 61 | flongcycle | 长周期 | numeric | 23 | 10 | √ | 0 | 长周期 |
| 62 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 63 | fordercount10 | 打单次数（M10） | int8 | 64 |  | √ | 0 | 打单次数（M10） |
| 64 | fordercount11 | 打单次数（M11） | int8 | 64 |  | √ | 0 | 打单次数（M11） |
| 65 | fordercount12 | 打单次数（M12） | int8 | 64 |  | √ | 0 | 打单次数（M12） |
| 66 | fdaystandadev | 日标准用量偏差 | numeric | 23 | 10 |  | 0 | 日标准用量偏差 |
| 67 | fshelflife | 是否保质期 | bpchar | 1 |  | √ | '0' | 是否保质期 |
| 68 | fisgeneral | 是否通用清单件 | bpchar | 1 |  | √ | '0' | 是否通用清单件 |
| 69 | fconmtypeid | 合同类型ID | varchar | 2000 |  | √ | ' ' | 合同类型ID |
| 70 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 71 | fsupplyresp | 供货责任 | varchar | 5 |  | √ | ' ' | 供货责任,枚举: 0 :库存组织 1 :客户 2 :VMI供应商 3 :非VMI供应商 |
| 72 | finsupplyqty | 内部供应用量 | numeric | 23 | 10 | √ | 0 | 内部供应用量 |
| 73 | fbeforematerial | 转换前物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 74 | fqty12m | 12个月总用量 | numeric | 23 | 10 | √ | 0 | 12个月总用量 |
| 75 | fbeforematerialname | 转换前物料名称 | varchar | 2000 |  | √ | ' ' | 转换前物料名称 |
| 76 | fbeforeunit | 转换前计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_target_time_log |  | flogid |
| 2 | pk_mds_targetmaterial_time |  | fid |
