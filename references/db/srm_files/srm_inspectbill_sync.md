# 来料检验同步-srm_inspectbill_sync

## 单据体-子表 t_srm_inspectentity

- **表名称：** 单据体-子表
- **表名：** t_srm_inspectentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | funqualifiedqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | fbasequaliqty | 基本单位合格数 | numeric | 23 | 10 | √ | 0 | 基本单位合格数 |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fbaseunqlyqty | 基本单位不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位不合格数 |
| 12 | fqualifiedqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_inspectentity |  | fentryid |
| 2 | idx_srm_inspectentity_fsupid |  | fsupplierid |
| 3 | idx_srm_inspectentity_fmatid |  | fmaterialid |
| 4 | idx_srm_inspectentity_fid_fseq |  | fid,fseq |

---

## 来料检验同步-主表 t_srm_inspectbill

- **表名称：** 来料检验同步-主表
- **表名：** t_srm_inspectbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finspeenddate | 检验完成时间 | timestamp | 0 |  |  | null | 检验完成时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_inbillsync_fbillno |  | fbillno |
| 2 | idx_srm_inbillsync_findate |  | finspeenddate |
| 3 | pk_srm_inspectbill |  | fid |
| 4 | idx_srm_inbillsync_forgid |  | forgid |
