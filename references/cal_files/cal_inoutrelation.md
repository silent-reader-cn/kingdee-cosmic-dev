# 出入库关系表-cal_inoutrelation

## 出入库关系表-主表 t_cal_inoutrelation

- **表名称：** 出入库关系表-主表
- **表名：** t_cal_inoutrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 3 | finbillnunber | 入库单编码 | varchar | 80 |  | √ | ' ' | 入库单编码 |
| 4 | finbilldate | 入库记账日期 | timestamp | 0 |  |  | null | 入库记账日期 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | finbillentryid | 入库单分录id | int8 | 64 |  | √ | 0 | 入库单分录id |
| 7 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 8 | finbillid | 入库单单据id | int8 | 64 |  | √ | 0 | 入库单单据id |
| 9 | fsumoutqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_iorelation_cim |  | fcostaccountid,finbilldate,fmaterialid |
| 2 | idx_cal_iorelation_inbilleid |  | finbillentryid |
| 3 | pk_cal_inoutrelation |  | fid |

---

## 单据体-子表 t_cal_inoutrelationentry

- **表名称：** 单据体-子表
- **表名：** t_cal_inoutrelationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutqty | 出库数量 | numeric | 23 | 10 | √ | 0 | 出库数量 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | foutbillid | 出库单单据id | int8 | 64 |  | √ | 0 | 出库单单据id |
| 5 | foutbillentryid | 出库单分录id | int8 | 64 |  | √ | 0 | 出库单分录id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | foutbillnumber | 出库单编码 | varchar | 80 |  | √ | ' ' | 出库单编码 |
| 8 | foutbilldate | 出库记账日期 | timestamp | 0 |  |  | null | 出库记账日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_iorelatione_id |  | fid |
| 2 | idx_cal_iorelatione_outbilldate |  | foutbilldate |
| 3 | pk_cal_inoutrelationentry |  | fentryid |
| 4 | idx_cal_iorelatione_outbilleid |  | foutbillentryid |
