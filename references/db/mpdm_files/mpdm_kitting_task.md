# 任务-mpdm_kitting_task

## 任务-分表 t_mpdm_kittingtask_m

- **表名称：** 任务-分表
- **表名：** t_mpdm_kittingtask_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 3 | fsrcbillno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fbizstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 8 | fentryseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 9 | fplanstatus | 计划状态 | varchar | 5 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 10 | fplanmaterialid | 物料（计划） | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 11 | fplanbegingtime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 12 | fmasterid | 物料（主数据） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | ftaskstatus | 任务状态 | varchar | 5 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 15 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 16 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 |
| 19 | forderbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kittingtask_m |  | fid |

---

## 任务-主表 t_mpdm_kittingtask

- **表名称：** 任务-主表
- **表名：** t_mpdm_kittingtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkittingid | 齐套ID | int8 | 64 |  | √ | 0 | 齐套ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 9 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kittingtask |  | fid |
| 2 | idx_kitting_t_kittingid |  | fkittingid |
| 3 | idx_kitting_t_srcid |  | fsrcbillid,fsrcbillentryid |
