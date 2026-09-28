# 扩展字段映射-ap_billfieldmapping

## 扩展字段映射-主表 t_ap_billfieldmapping

- **表名称：** 扩展字段映射-主表
- **表名：** t_ap_billfieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetbillentity | 目标单标识 | varchar | 50 |  | √ | ' ' | 目标单标识,枚举: ap_adjexchbill :应付调汇单 ar_adjustexchbill :应收调汇单 |
| 3 | fsrcbillentity | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识,枚举: ap_busbill :暂估应付单 ap_finapbill :财务应付单 ap_paidbill :期初预付单 cas_paybill :付款处理 ar_busbill :暂估应收单 ar_finarbill :财务应收单 ar_receivedbill :预收单 cas_recbill :收款处理 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_mapping_entity |  | fsrcbillentity,ftargetbillentity |
| 2 | pk_t_ap_billfieldmapping |  | fid |

---

## 单据体-子表 t_ap_fieldmappingentry

- **表名称：** 单据体-子表
- **表名：** t_ap_fieldmappingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcfieldsite | 源单字段位置 | varchar | 50 |  | √ | ' ' | 源单字段位置 |
| 3 | ftargetfieldsite | 目标单字段位置 | varchar | 50 |  | √ | ' ' | 目标单字段位置 |
| 4 | ftargetfield | 目标单字段 | varchar | 50 |  | √ | ' ' | 目标单字段,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcfield | 源单字段 | varchar | 50 |  | √ | ' ' | 源单字段,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_fieldmappingentry_fid |  | fid |
| 2 | pk_t_ap_fieldmappingentry |  | fentryid |
