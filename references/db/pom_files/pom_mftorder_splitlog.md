# 生产工单拆分日志-pom_mftorder_splitlog

## 生产工单拆分日志-主表 t_pom_splitlog

- **表名称：** 生产工单拆分日志-主表
- **表名：** t_pom_splitlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanqty | 计划数量(弃用) | numeric | 23 | 10 | √ | 0 | 计划数量(弃用) |
| 3 | fbefsplitqty | 拆分前数量 | numeric | 23 | 10 | √ | 0 | 拆分前数量 |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forderid | 生产工单id | int8 | 64 |  | √ | 0 | 生产工单id |
| 6 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | forderentryid | 生产工单行号f7 | int8 | 64 |  | √ | 0 | 生产工单分录f7 pom_mftorder_f7 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 拆分人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | faftauxptyqty | 拆分后辅助数量 | numeric | 23 | 10 | √ | 0 | 拆分后辅助数量 |
| 12 | forderstatus | 生产工单单据状态 | varchar | 50 |  | √ | ' ' | 生产工单单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbefauxptyqty | 拆分前辅助数量 | numeric | 23 | 10 | √ | 0 | 拆分前辅助数量 |
| 14 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fbefauxptyqty2 | 拆分前辅助数量(2) | numeric | 23 | 10 | √ | 0 | 拆分前辅助数量(2) |
| 19 | fcreatetime | 拆分时间 | timestamp | 0 |  |  | null | 拆分时间 |
| 20 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | faftsplitbaseqty | 拆分后基本数量 | numeric | 23 | 10 | √ | 0 | 拆分后基本数量 |
| 22 | faftauxptyqty2 | 拆分后辅助数量(2) | numeric | 23 | 10 | √ | 0 | 拆分后辅助数量(2) |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | forderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 25 | fmaterialmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 26 | fplanbaseqty | 计划基本数量(弃用) | numeric | 23 | 10 | √ | 0 | 计划基本数量(弃用) |
| 27 | fbefsplitbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 28 | faftsplitqty | 拆分后数量 | numeric | 23 | 10 | √ | 0 | 拆分后数量 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fproductname | fproductname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_splitlog |  | fid |
| 2 | idx_pom_splitlog_forderentryid |  | forderentryid |
| 3 | idx_pom_splitlog_forderid |  | forderid |

---

## 单据体-子表 t_pom_splitentry

- **表名称：** 单据体-子表
- **表名：** t_pom_splitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsplitreason | 拆分原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | ftorderid | 目标工单id | int8 | 64 |  | √ | 0 | 目标工单id |
| 4 | fsplitbaseqty | 拆分基本数量 | numeric | 23 | 10 | √ | 0 | 拆分基本数量 |
| 5 | ftordertype | 目标工单类型 | varchar | 30 |  | √ | 'pom_mftorder' | 目标工单类型,枚举: pom_mftorder :生产工单 om_mftorder :委外工单 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsplitqty | 拆分数量 | numeric | 23 | 10 | √ | 0 | 拆分数量 |
| 8 | fsplitauxptyqty2 | 拆分辅助数量(2) | numeric | 23 | 10 | √ | 0 | 拆分辅助数量(2) |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbeginbookdate | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 11 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fsplitauxptyqty | 拆分辅助数量 | numeric | 23 | 10 | √ | 0 | 拆分辅助数量 |
| 13 | ftorderno | 目标工单编号 | varchar | 50 |  | √ | ' ' | 目标工单编号 |
| 14 | ftorderentryid | 目标工单行号f7 | int8 | 64 |  | √ | 0 | 生产工单分录f7 pom_mftorder_f7 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_splitentry_ftorderid |  | ftorderid |
| 2 | pk_pom_splitentry |  | fentryid |
| 3 | idx_pom_splitentry_fid |  | fid |
| 4 | idx_pom_splitentry_ftentryid |  | ftorderentryid |
