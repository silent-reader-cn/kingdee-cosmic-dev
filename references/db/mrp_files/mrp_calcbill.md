# MRP运算单据-mrp_calcbill

## MRP运算单据-主表 t_mrp_computebill

- **表名称：** MRP运算单据-主表
- **表名：** t_mrp_computebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | planorgid | planorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fplanorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fmtlexpandtype | 选料展开方式 | bpchar | 1 |  | √ | '1' | 选料展开方式,枚举: 1 :本层 2 :向下展开 3 :向上展开 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fisallowdateinpast | 允许计划建议开始日期在过去 | bpchar | 1 |  | √ | '0' | 允许计划建议开始日期在过去 |
| 9 | fenddate | 计划结束日期 | timestamp | 0 |  |  | null | 计划结束日期 |
| 10 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fmasterid | fmasterid | int8 | 64 |  |  | null |  |
| 13 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 14 | fisplansimulate | 计划模拟 | bpchar | 1 |  | √ | '0' | 计划模拟 |
| 15 | fplangramid | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案 mrp_planscheme](../msplan_files/mrp_planscheme.md) |
| 16 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 17 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 18 | falgoregisterid | MRP业务方案配置 | int8 | 64 |  | √ | 0 | [业务方案配置 mrp_businessplan](../msplan_files/mrp_businessplan.md) |
| 19 | fcomputedate | 运算日期 | timestamp | 0 |  |  | null | 运算日期 |
| 20 | fmrprunlogid | MRP日志内码 | int8 | 64 |  | √ | 0 | MRP日志内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_computebill |  | fid |
| 2 | idx_mrp_computebill_logid |  | fmrprunlogid |
