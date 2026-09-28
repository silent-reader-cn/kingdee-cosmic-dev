# 目标件清单明细-mds_targetmaterial

## 目标件清单明细-主表 t_mds_targetmaterial

- **表名称：** 目标件清单明细-主表
- **表名：** t_mds_targetmaterial

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
| 10 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | [检修级别 mpdm_checktype](../mpdm_files/mpdm_checktype.md) |
| 11 | fquarter1 | Q1 | bpchar | 1 |  | √ | '0' | Q1 |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fbeforematerialnumber | 转换前物料编码 | varchar | 2000 |  | √ | ' ' | 转换前物料编码 |
| 15 | fqty | 总用量 | numeric | 23 | 10 | √ | 0 | 总用量 |
| 16 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fconmtypename | 合同类型名称 | varchar | 2000 |  | √ | ' ' | 合同类型名称 |
| 19 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 20 | fdaystandadev12m | 12个月日标准用量偏差 | numeric | 23 | 10 |  | 0 | 12个月日标准用量偏差 |
| 21 | fordercount2 | 打单次数（M2） | int8 | 64 |  | √ | 0 | 打单次数（M2） |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fordercount1 | 打单次数（M1） | int8 | 64 |  | √ | 0 | 打单次数（M1） |
| 24 | fordercount4 | 打单次数（M4） | int8 | 64 |  | √ | 0 | 打单次数（M4） |
| 25 | fordercount3 | 打单次数（M3） | int8 | 64 |  | √ | 0 | 打单次数（M3） |
| 26 | fordercount6 | 打单次数（M6） | int8 | 64 |  | √ | 0 | 打单次数（M6） |
| 27 | fordercount5 | 打单次数（M5） | int8 | 64 |  | √ | 0 | 打单次数（M5） |
| 28 | fordercount8 | 打单次数（M8） | int8 | 64 |  | √ | 0 | 打单次数（M8） |
| 29 | fbeforeunitname | 转换前计量单位 | varchar | 2000 |  | √ | ' ' | 转换前计量单位 |
| 30 | faverageyearqty | 365日平均用量 | numeric | 23 | 10 | √ | 0 | 365日平均用量 |
| 31 | fordercount7 | 打单次数（M7） | int8 | 64 |  | √ | 0 | 打单次数（M7） |
| 32 | faverageqty12m | 12个月平均用量 | numeric | 23 | 10 | √ | 0 | 12个月平均用量 |
| 33 | fordercount9 | 打单次数（M9） | int8 | 64 |  | √ | 0 | 打单次数（M9） |
| 34 | faveragedayqty | 平均日用量 | numeric | 23 | 10 | √ | 0 | 平均日用量 |
| 35 | fmaterialchange | 是否物料转换 | bpchar | 1 |  | √ | '0' | 是否物料转换 |
| 36 | fislongcyclemater | 是否长周期物料 | bpchar | 1 |  | √ | '0' | 是否长周期物料 |
| 37 | fordercountall | 总打单次数 | int8 | 64 |  | √ | 0 | 总打单次数 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | fmqty2 | 月用量（M2） | numeric | 23 | 10 | √ | 0 | 月用量（M2） |
| 41 | fmqty1 | 月用量（M1） | numeric | 23 | 10 | √ | 0 | 月用量（M1） |
| 42 | freqtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 43 | fmqty6 | 月用量（M6） | numeric | 23 | 10 | √ | 0 | 月用量（M6） |
| 44 | fmqty10 | 月用量（M10） | numeric | 23 | 10 | √ | 0 | 月用量（M10） |
| 45 | fmqty5 | 月用量（M5） | numeric | 23 | 10 | √ | 0 | 月用量（M5） |
| 46 | fmqty11 | 月用量（M11） | numeric | 23 | 10 | √ | 0 | 月用量（M11） |
| 47 | fmqty4 | 月用量（M4） | numeric | 23 | 10 | √ | 0 | 月用量（M4） |
| 48 | fmqty3 | 月用量（M3） | numeric | 23 | 10 | √ | 0 | 月用量（M3） |
| 49 | favgdelivery | 三年平均交期 | numeric | 23 | 10 | √ | 0 | 三年平均交期 |
| 50 | fmqty9 | 月用量（M9） | numeric | 23 | 10 | √ | 0 | 月用量（M9） |
| 51 | fmqty8 | 月用量（M8） | numeric | 23 | 10 | √ | 0 | 月用量（M8） |
| 52 | fmqty7 | 月用量（M7） | numeric | 23 | 10 | √ | 0 | 月用量（M7） |
| 53 | ftargetflag | 标识 | bpchar | 1 |  | √ | '0' | 标识 |
| 54 | fqcode | 季度代码 | varchar | 50 |  | √ | ' ' | 季度代码 |
| 55 | fstandadev12m | 12个月标准用量偏差 | numeric | 23 | 10 |  | 0 | 12个月标准用量偏差 |
| 56 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 57 | fconmtypenumber | 合同类型编码 | varchar | 2000 |  | √ | ' ' | 合同类型编码 |
| 58 | fcustosupplyqty | 客户供应用量 | numeric | 23 | 10 | √ | 0 | 客户供应用量 |
| 59 | fmqty12 | 月用量（M12） | numeric | 23 | 10 | √ | 0 | 月用量（M12） |
| 60 | fusemonthcount | 使用频率 | int8 | 64 |  | √ | 0 | 使用频率 |
| 61 | factualleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 62 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 63 | faverageqty | 平均月用量 | numeric | 23 | 10 | √ | 0 | 平均月用量 |
| 64 | flongcycle | 长周期 | numeric | 23 | 10 | √ | 0 | 长周期 |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fordercount10 | 打单次数（M10） | int8 | 64 |  | √ | 0 | 打单次数（M10） |
| 67 | fordercount11 | 打单次数（M11） | int8 | 64 |  | √ | 0 | 打单次数（M11） |
| 68 | fordercount12 | 打单次数（M12） | int8 | 64 |  | √ | 0 | 打单次数（M12） |
| 69 | fdaystandadev | 日标准用量偏差 | numeric | 23 | 10 |  | 0 | 日标准用量偏差 |
| 70 | fshelflife | 是否保质期 | bpchar | 1 |  | √ | '0' | 是否保质期 |
| 71 | fisgeneral | 是否通用清单件 | bpchar | 1 |  | √ | '0' | 是否通用清单件 |
| 72 | fconmtypeid | 合同类型ID | varchar | 2000 |  | √ | ' ' | 合同类型ID |
| 73 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 74 | fsupplyresp | 供货责任 | varchar | 5 |  | √ | ' ' | 供货责任,枚举: 0 :库存组织 1 :客户 2 :VMI供应商 3 :非VMI供应商 |
| 75 | finsupplyqty | 内部供应用量 | numeric | 23 | 10 | √ | 0 | 内部供应用量 |
| 76 | fbeforematerial | 转换前物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 77 | fqty12m | 12个月总用量 | numeric | 23 | 10 | √ | 0 | 12个月总用量 |
| 78 | fbeforematerialname | 转换前物料名称 | varchar | 2000 |  | √ | ' ' | 转换前物料名称 |
| 79 | fbeforeunit | 转换前计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_targetmaterial_log |  | flogid |
| 2 | pk_mds_targetmaterial |  | fid |

---

## 章节号-多选基础资料表 t_mds_targetmaterial_ata

- **表名称：** 章节号-多选基础资料表
- **表名：** t_mds_targetmaterial_ata

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
| 1 | pk_mds_targetmaterial_ata |  | fpkid |
| 2 | idx_mds_target_ata_id |  | fid |
