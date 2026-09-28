# 预算需求计划单-xkbm_mrprequireplanbill

## 预算需求明细-子表 t_xkbm_requireplandetail

- **表名称：** 预算需求明细-子表
- **表名：** t_xkbm_requireplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fauxqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 5 | fmodeltype | 模型类型 | varchar | 10 |  | √ | ' ' | 模型类型,枚举: 1 :供应 2 :需求 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 8 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_requireplandetail |  | fentryid |
| 2 | pk_xkbm_requireplandetail |  | fdetailid |

---

## 预算需求计划单-主表 t_xkbm_mrprequireplanbill

- **表名称：** 预算需求计划单-主表
- **表名：** t_xkbm_mrprequireplanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmrpbizscheme | 业务流方案 | int8 | 64 |  | √ | 0 | [预算MRP业务流方案 xkbm_mrpbizscheme](../xkbm_files/xkbm_mrpbizscheme.md) |
| 10 | fincludeauxpty | 考虑物料的辅助属性 | bpchar | 1 |  | √ | ' ' | 考虑物料的辅助属性 |
| 11 | fsource | 来源类型 | varchar | 10 |  | √ | ' ' | 来源类型,枚举: 0 :预算报表 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 15 | fscheme | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 16 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 17 | fdate | 预算日期 | timestamp | 0 |  |  | null | 预算日期 |
| 18 | fcycle | 周期类型 | varchar | 10 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrprequireplanbill |  | fcycle,fyear,fperiod |
| 2 | pk_xkbm_mrprequireplanbill |  | fid |

---

## 预算来源-子表 t_xkbm_requireplansource

- **表名称：** 预算来源-子表
- **表名：** t_xkbm_requireplansource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fsheetname | 表页名 | varchar | 570 |  | √ | ' ' | 表页名 |
| 4 | freportid | 报表编码 | varchar | 36 |  | √ | ' ' | [预算报表 xkbm_report](../xkbm_files/xkbm_report.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_requireplansource |  | fentryid |
| 2 | idx_xkbm_requireplansource_fid |  | fid |
