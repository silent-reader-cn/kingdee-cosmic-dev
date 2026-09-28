# 分配报告检查明细-sco_allocreportdetail

## 单据体-子表 t_sco_alloreptdetailentry

- **表名称：** 单据体-子表
- **表名：** t_sco_alloreptdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubcostcenternum | 成本中心编码 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fcheckdetail | 检查明细 | varchar | 255 |  | √ | ' ' | 检查明细 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_alloreptdetailentry |  | fentryid |
| 2 | idx_sco_alloreptdetailentry |  | fid,fseq |

---

## 分配报告检查明细-主表 t_sco_allocreportdetail

- **表名称：** 分配报告检查明细-主表
- **表名：** t_sco_allocreportdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fcheckitemdesc | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 8 | fstarttime | 分配日期 | timestamp | 0 |  |  | null | 分配日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_allocreportdetail |  | fid |
| 2 | idx_sco_allocreportdetail |  | forgid,fmanuorgid,fcostaccountid |
