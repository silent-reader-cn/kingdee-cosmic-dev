# 成本还原合法性检查项明细-sco_reductcheckdetail

## 单据体-子表 t_sco_redcheckdetailentry

- **表名称：** 单据体-子表
- **表名：** t_sco_redcheckdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckdetail | 检查明细 | varchar | 1000 |  | √ | ' ' | 检查明细 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryprodorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_redcheckdetailentry |  | fid,fentryid |
| 2 | pk_sco_redcheckdetailentry |  | fentryid |

---

## 成本还原合法性检查项明细-主表 t_sco_reductcheckdetail

- **表名称：** 成本还原合法性检查项明细-主表
- **表名：** t_sco_reductcheckdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprodorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcheckitemdesc | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 7 | fcalcdate | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 8 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | 任务 |
| 9 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | 检查项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_reductcheckdetail |  | forgid,fcostaccountid,fperiodid |
| 2 | pk_sco_reductcheckdetail |  | fid |
