# 计算过程-sco_alloccalcreport

## 分配标准值计算明细-子表 t_sco_alloccreportentry

- **表名称：** 分配标准值计算明细-子表
- **表名：** t_sco_alloccreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillnumber | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 3 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 4 | fcalcresult | 公式运算结果 | varchar | 255 |  | √ | ' ' | 公式运算结果 |
| 5 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 6 | fbilltypenum | 业务单据类型编码 | varchar | 80 |  | √ | ' ' | 业务单据类型编码 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 11 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_alloccreportentry_cid |  | fcostobjectid |
| 2 | pk_sco_alloccreportentry |  | fentryid |
| 3 | idx_sco_alloccreportentry_fid |  | fid |

---

## 计算过程-主表 t_sco_alloccalcreport

- **表名称：** 计算过程-主表
- **表名：** t_sco_alloccalcreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fiscalcdata | 是否计算过程记录数据 | bpchar | 1 |  | √ | '0' | 是否计算过程记录数据 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 8 | falloctime | 分配日期 | timestamp | 0 |  |  | null | 分配日期 |
| 9 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fallocbillno | 分配单编号 | varchar | 80 |  | √ | ' ' | 分配单编号 |
| 12 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_alloccalcreport_ocp |  | forgid,fcostaccountid,fperiodid |
| 2 | pk_sco_alloccalcreport |  | fid |
