# 计划订单投放-psw_firmplanorder

## 计划订单-子表 t_psw_firmorderdet

- **表名称：** 计划订单-子表
- **表名：** t_psw_firmorderdet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffirmedorder | 本次投放关联工单 | varchar | 50 |  |  | null | 本次投放关联工单 |
| 3 | fsupplyorg | 供应组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fvaliddatetime | 计划订单修改时间 | timestamp | 0 |  |  | null | 计划订单修改时间 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 8 | fbomid | BOM编码 | int8 | 64 |  |  | null | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 9 | ffirmdatetime | 上次投放时间 | timestamp | 0 |  |  | null | 上次投放时间 |
| 10 | ffirmstatus | 投放状态 | varchar | 50 |  |  | null | 投放状态,枚举: A :未投放 B :投放中 C :部分投放 D :已投放 E :投放失败 |
| 11 | forderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  |  | null | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fqtytofirm | 本次投放基本数量 | numeric | 23 | 10 | √ | 0 | 本次投放基本数量 |
| 15 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fplanoperatenum | 计划运算号 | varchar | 50 |  |  | null | 计划运算号 |
| 18 | firmedqty | 已投放基本数量 | numeric | 23 | 10 | √ | 0 | 已投放基本数量 |
| 19 | ffirmordertype | 订单类型 | varchar | 50 |  | √ | ' ' | 订单类型,枚举: 10030 :自制 10050 :委外 10040 :外购 10060 :内协 10070 :返工自制 10080 :返工委外 |
| 20 | fmftunitid | fmftunitid | int8 | 64 |  |  | null |  |
| 21 | fbizunitid | 计量单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | freqorg | 需求组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | forderbaseqty | 订单基本数量 | numeric | 23 | 10 | √ | 0 | 订单基本数量 |
| 26 | fplanner | 计划员 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 29 | fduedate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 30 | fyieldpercent | 成品率% | numeric | 23 | 10 |  | null | 成品率% |
| 31 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 32 | fplanorderid | 计划订单编号 | int8 | 64 |  |  | null | 计划订单 mrp_planorder |
| 33 | fbomcode | fbomcode | int8 | 64 |  |  | null |  |
| 34 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 35 | fmaterialmftid | 物料生产 | int8 | 64 |  |  | null | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_fmd_union |  | fentryid |
| 2 | pk_t_psw_firmorderdet |  | fentryid |

---

## 计划订单投放-主表 t_psw_firmorder

- **表名称：** 计划订单投放-主表
- **表名：** t_psw_firmorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 30 |  |  | null | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_firmorder |  | fid |
| 2 | idx_t_psw_fm_union |  | forgid |
