# 替代日志-mrp_replace_log

## 替代物料-子表 t_mrp_rep_log_r_entry

- **表名称：** 替代物料-子表
- **表名：** t_mrp_rep_log_r_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryqty | 替代数量 | numeric | 23 | 10 | √ | 0 | 替代数量 |
| 3 | fentrymaterial | 替代物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fentryauxpty | 替代物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryunit | 替代计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_rep_log_r_entry |  | fentryid |
| 2 | idx_mrp_rep_log_r_entry |  | fid |

---

## 主物料-子表 t_mrp_rep_log_m_entry

- **表名称：** 主物料-子表
- **表名：** t_mrp_rep_log_m_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 3 | fentrymaterial | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fentryauxpty | 主物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_rep_log_m_entry |  | fentryid |
| 2 | idx_mrp_rep_log_m_entry |  | fid |

---

## 替代日志-主表 t_mrp_replace_log

- **表名称：** 替代日志-主表
- **表名：** t_mrp_replace_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 3 | frepmaterial | 替代物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | freplacestra | 替代策略 | varchar | 30 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 5 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 6 | frepauxpty | 替代物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fbillentryid | 需求分录ID | varchar | 50 |  | √ | ' ' | 需求分录ID |
| 8 | frunlog | 计划运算号 | int8 | 64 |  | √ | 0 | 运算日志 mrp_caculate_log |
| 9 | frepqty | 替代数量 | numeric | 23 | 10 | √ | 0 | 替代数量 |
| 10 | fbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 11 | fsourceno | 需求来源号 | varchar | 512 |  | √ | ' ' | 需求来源号 |
| 12 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | freplacemethod | 替代方式 | varchar | 30 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 14 | frequnit | 替代计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | freplace | 替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 16 | fbomnumber | BOM编码 | varchar | 100 |  | √ | ' ' | BOM编码 |
| 17 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | frunlogno | 运算日志编码 | varchar | 100 |  | √ | ' ' | 运算日志编码 |
| 19 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mrp_replace_log_fnumber |  | frunlog |
| 2 | pk_mrp_replace_log |  | fid |
