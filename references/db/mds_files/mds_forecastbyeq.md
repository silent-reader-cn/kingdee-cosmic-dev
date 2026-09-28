# 基于未来设备的预测-mds_forecastbyeq

## 章节号-多选基础资料表 t_mds_forecastbyeq_ata

- **表名称：** 章节号-多选基础资料表
- **表名：** t_mds_forecastbyeq_ata

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
| 1 | idx_mds_forecastbyeq_ata |  | fid |
| 2 | pk_mds_forecastbyeq_ata |  | fpkid |

---

## 基于未来设备的预测-主表 t_mds_forecastbyeq

- **表名称：** 基于未来设备的预测-主表
- **表名：** t_mds_forecastbyeq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factualintime | 预计进场时间 | timestamp | 0 |  |  | null | 预计进场时间 |
| 3 | freqtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | faccount | 总架数 | numeric | 23 | 10 | √ | 0 | 总架数 |
| 6 | flogid | 通用备货运算号 | int8 | 64 |  | √ | 0 | [通用备货运算日志 mds_generallog](../mds_files/mds_generallog.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | [检修级别 mpdm_checktype](../mpdm_files/mpdm_checktype.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | feqcountm3 | 未来第三个月设备数量 | numeric | 23 | 10 | √ | 0 | 未来第三个月设备数量 |
| 12 | fforecastqty | 预测未来用量 | numeric | 23 | 10 | √ | 0 | 预测未来用量 |
| 13 | feqcountm2 | 未来第二个月设备数量 | numeric | 23 | 10 | √ | 0 | 未来第二个月设备数量 |
| 14 | factualleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | feqcountm1 | 未来第一个月设备数量 | numeric | 23 | 10 | √ | 0 | 未来第一个月设备数量 |
| 17 | fqty | 总用量 | numeric | 23 | 10 | √ | 0 | 总用量 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 20 | faverageqty | 平均用量 | numeric | 23 | 10 | √ | 0 | 平均用量 |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fstockfactor | 设备库存系数 | numeric | 23 | 10 | √ | 0 | 设备库存系数 |
| 24 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fshelflife | 是否保质期 | bpchar | 1 |  | √ | '0' | 是否保质期 |
| 27 | fisgeneral | 是否通用清单件 | bpchar | 1 |  | √ | '0' | 是否通用清单件 |
| 28 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 29 | fuseaccount | 有用量架数 | numeric | 23 | 10 | √ | 0 | 有用量架数 |
| 30 | feqcount | 设备数量 | numeric | 23 | 10 | √ | 0 | 设备数量 |
| 31 | fmaterialchange | 是否物料转换 | bpchar | 1 |  | √ | '0' | 是否物料转换 |
| 32 | fuseprobability | 使用概率 | numeric | 23 | 10 | √ | 0 | 使用概率 |
| 33 | fislongcyclemater | 是否长周期物料 | bpchar | 1 |  | √ | '0' | 是否长周期物料 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_forecastbyeq |  | fid |
| 2 | idx_mds_forecastbyeq_log |  | flogid |
