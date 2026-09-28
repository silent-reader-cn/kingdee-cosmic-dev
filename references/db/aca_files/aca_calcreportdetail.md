# 未通过明细-aca_calcreportdetail

## 单据体-子表 t_aca_calcdetailentry

- **表名称：** 单据体-子表
- **表名：** t_aca_calcdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckdetail_tag | 检查明细_详情 | text | 0 |  |  | null | 检查明细_详情 |
| 3 | fentrycostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fcheckdetail | 检查明细 | varchar | 255 |  | √ | ' ' | 检查明细 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_calcdetailentry |  | fentryid |
| 2 | idx_aca_calcdetailentry |  | fid,fentrycostcenterid,fcheckdetail |

---

## 未通过明细-主表 t_aca_calcreportdetail

- **表名称：** 未通过明细-主表
- **表名：** t_aca_calcreportdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckitemdesc | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fcalcdate | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 7 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | 任务 |
| 8 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | 检查项 |
| 10 | fcheckdesc | fcheckdesc | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_calcreportdetail |  | fid |
| 2 | idx_aca_calcreportdetail |  | fcostaccountid,fcheckdesc |
