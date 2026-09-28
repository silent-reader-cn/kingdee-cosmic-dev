# 通用备货建议-mds_generalsuggest

## 通用备货建议-主表 t_mds_generalsuggest

- **表名称：** 通用备货建议-主表
- **表名：** t_mds_generalsuggest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | flogid | 通用备货运算号 | int8 | 64 |  | √ | 0 | [通用备货运算日志 mds_generallog](../mds_files/mds_generallog.md) |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_generalsuggest |  | fid |
| 2 | idx_mds_generalsuggest_log |  | flogid |

---

## 章节号-多选基础资料表 t_mds_generalsuggest_ata

- **表名称：** 章节号-多选基础资料表
- **表名：** t_mds_generalsuggest_ata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [ATA章节号 mpdm_atachapterno](../mpdm_files/mpdm_atachapterno.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_generalsug_ata_eid |  | fentryid |
| 2 | pk_mds_generalsuggest_ata |  | fpkid |

---

## 单据体-子表 t_mds_generalsug_entry

- **表名称：** 单据体-子表
- **表名：** t_mds_generalsug_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factualintime | 预计进场时间 | timestamp | 0 |  |  | null | 预计进场时间 |
| 3 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fentrymodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | freqtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 6 | fadjreasonflag | 调整原因是否有值 | bpchar | 1 |  | √ | '0' | 调整原因是否有值 |
| 7 | fadjreason | 调整原因 | varchar | 255 |  | √ | ' ' | 调整原因 |
| 8 | fstockupmode | 备货方式 | varchar | 5 |  | √ | ' ' | 备货方式,枚举: A :按BOM备货（工卡） B :按BOM备货（项目） C :按历史用量备货（工卡） D :按历史用量备货（项目） E :按客户需求量备货（工卡） F :按客户需求量备货（项目） G :通用备货 |
| 9 | fspecialreq | 特殊备货需求 | numeric | 23 | 10 | √ | 0 | 特殊备货需求 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 12 | fcalstocklevel | 计算库存水平 | numeric | 23 | 10 | √ | 0 | 计算库存水平 |
| 13 | fconfirmedqty | 确认备货数量 | numeric | 23 | 10 | √ | 0 | 确认备货数量 |
| 14 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | flastadjreason | 最近一次调整原因 | varchar | 255 |  | √ | ' ' | 最近一次调整原因 |
| 16 | fcalmethod | 计算方法 | varchar | 5 |  | √ | ' ' | 计算方法,枚举: 1 :At Least（最低库存量） 2 :At Most（最高库存量） 3 :Additional（数量累加） 4 :Average（取平均值） 5 :空 |
| 17 | fsuggestqty | 建议备货数量 | numeric | 23 | 10 | √ | 0 | 建议备货数量 |
| 18 | fislongcyclemater | 是否长周期物料 | bpchar | 1 |  | √ | '0' | 是否长周期物料 |
| 19 | fforecastqty | 预测未来用量 | numeric | 23 | 10 | √ | 0 | 预测未来用量 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | factualleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 22 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | ftargetstock | 目标库存水平 | numeric | 23 | 10 | √ | 0 | 目标库存水平 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_generalsug_entry_id |  | fid |
| 2 | pk_mds_generalsug_entry |  | fentryid |
