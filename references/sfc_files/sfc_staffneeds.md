# 人员需求(废弃)-sfc_staffneeds

## 单据体-子表 t_sfc_staffentry

- **表名称：** 单据体-子表
- **表名：** t_sfc_staffentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 人员类型 | int8 | 64 |  | √ | 0 | 行政类别 mpdm_category |
| 3 | freqenddate | 需求结束时间 | timestamp | 0 |  |  | null | 需求结束时间 |
| 4 | fneedsnum | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 5 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fstaffpoolamount | 人员池数量 | int8 | 64 |  | √ | 0 | 人员池数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freqstartdate | 需求开始时间 | timestamp | 0 |  |  | null | 需求开始时间 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fneedsamount | 需求数量 | int8 | 64 |  | √ | 0 | 需求数量 |
| 11 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fstaffpoolnum | 人员池数量 | numeric | 23 | 10 | √ | 0 | 人员池数量 |
| 13 | fstaffdispatch | 人员调拨数量 | numeric | 23 | 10 | √ | 0 | 人员调拨数量 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_staffentry_fk |  | fid |
| 2 | pk_sfc_staffentry |  | fentryid |

---

## 人员需求(废弃)-主表 t_sfc_staffneeds

- **表名称：** 人员需求(废弃)-主表
- **表名：** t_sfc_staffneeds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fworkhours | 工时量 | numeric | 23 | 10 | √ | 0 | 工时量 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 11 | fdispatchstatus | 调度状态 | varchar | 50 |  | √ | ' ' | 调度状态,枚举: D :待调度 Y :已调度 |
| 12 | fbizdata | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_staffneeds_billno |  | fbillno |
| 2 | pk_sfc_staffneeds |  | fid |
