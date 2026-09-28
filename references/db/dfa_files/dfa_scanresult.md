# 扫描结果-dfa_scanresult

## 风险清单-子表 t_dfa_scan_abnormalentry

- **表名称：** 风险清单-子表
- **表名：** t_dfa_scan_abnormalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctorgname | 核算组织名称 | varchar | 255 |  | √ | ' ' | 核算组织名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | flowerval | 低数值 | numeric | 23 | 10 |  | null | 低数值 |
| 5 | fval | 数值 | numeric | 23 | 10 |  | null | 数值 |
| 6 | fupperval | 高数值 | numeric | 23 | 10 |  | null | 高数值 |
| 7 | fsheettype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型 |
| 8 | facctorgcode | 核算组织编码 | varchar | 100 |  | √ | ' ' | 核算组织编码 |
| 9 | fitemname | 报表项目名称 | varchar | 255 |  | √ | ' ' | 报表项目名称 |
| 10 | fitemdatatypecode | 项目数据类型编码 | varchar | 100 |  | √ | ' ' | 项目数据类型编码 |
| 11 | fitemcode | 报表项目编码 | varchar | 100 |  | √ | ' ' | 报表项目编码 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fitemdatatypename | 项目数据类型名称 | varchar | 255 |  | √ | ' ' | 项目数据类型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_abnormalentry_fid |  | fid |
| 2 | pk_dfa_scan_abnormalentry |  | fentryid |

---

## 扫描结果-主表 t_dfa_scanresult

- **表名称：** 扫描结果-主表
- **表名：** t_dfa_scanresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscansetting | 扫描设置 | int8 | 64 |  | √ | 0 | 风险扫描设置 dfa_risk_scanning_setting |
| 3 | forgsnum | 总组织数量 | int4 | 32 |  | √ | 0 | 总组织数量 |
| 4 | ftenant_datacenter | 数据中心 | int8 | 64 |  | √ | 0 | [租户数据中心 dfa_tenant_datacenter](../dfa_files/dfa_tenant_datacenter.md) |
| 5 | fabnormalorgnum | 异常项组织数量 | int4 | 32 |  | √ | 0 | 异常项组织数量 |
| 6 | fscantime | 扫描日期 | timestamp | 0 |  |  | null | 扫描日期 |
| 7 | fabnormalnum | 异常项数量 | int4 | 32 |  | √ | 0 | 异常项数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_scanresult |  | fid |
| 2 | idx_dfa_scanresult_datacenter |  | ftenant_datacenter |
