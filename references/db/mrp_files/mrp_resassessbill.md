# 资源评估表-mrp_resassessbill

## 单据体-子表 t_mrp_resassessbillentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_resassessbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupetime | 供应完成时间 | timestamp | 0 |  |  | null | 供应完成时间 |
| 3 | freqetime | 需求完成时间 | timestamp | 0 |  |  | null | 需求完成时间 |
| 4 | fissame | 是否匹配 | bpchar | 1 |  | √ | '0' | 是否匹配 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | freqbilltagname | 需求单据类型 | varchar | 80 |  | √ | ' ' | 需求单据类型 |
| 7 | fsupusetime | 供应时长 | numeric | 23 | 10 | √ | 0 | 供应时长 |
| 8 | fsupbilltag | 供应单据标识 | varchar | 80 |  | √ | ' ' | 供应单据标识 |
| 9 | fsupqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 10 | fsupstime | 供应开始时间 | timestamp | 0 |  |  | null | 供应开始时间 |
| 11 | freqbilltag | 需求单据标识 | varchar | 80 |  | √ | ' ' | 需求单据标识 |
| 12 | fmaterial | 工具资源 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fallowanceqty | 容差 | numeric | 23 | 10 | √ | 0 | 容差 |
| 14 | freqorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fcardid | 工卡 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 16 | freqbillno | 需求单据编号 | varchar | 200 |  | √ | ' ' | 需求单据编号 |
| 17 | frequsetime | 历史使用时长(小时) | numeric | 23 | 10 | √ | 0 | 历史使用时长(小时) |
| 18 | fsupbillno | 供应单据编号 | varchar | 200 |  | √ | ' ' | 供应单据编号 |
| 19 | fptype | 供需类型 | varchar | 5 |  | √ | ' ' | 供需类型,枚举: A :库存工具 B :采购 C :租借 D :需求 E :供应 |
| 20 | fshortageqty | 短缺 | numeric | 23 | 10 | √ | 0 | 短缺 |
| 21 | freqstime | 需求开始时间 | timestamp | 0 |  |  | null | 需求开始时间 |
| 22 | freqqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 23 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fsupbilltagname | 供应单据类型 | varchar | 80 |  | √ | ' ' | 供应单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_resassessbillentry |  | fentryid |
| 2 | idx_mrp_resassessbillentry |  | fid |

---

## 资源评估表-主表 t_mrp_resassessbill

- **表名称：** 资源评估表-主表
- **表名：** t_mrp_resassessbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fscheme | 计划方案编码 | int8 | 64 |  | √ | 0 | [资源计划方案 mrp_res_scheme](../mrp_files/mrp_res_scheme.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 评估单据编号 | varchar | 80 |  | √ | ' ' | 评估单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | flog | 计划运算号 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_resassessbill |  | fid |
| 2 | idx_mrp_resassessbill_id |  | forgid |
