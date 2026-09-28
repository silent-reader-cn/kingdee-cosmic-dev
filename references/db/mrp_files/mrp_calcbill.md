# MRP运算单据-mrp_calcbill

## MRP运算单据-主表 t_mrp_computebill

- **表名称：** MRP运算单据-主表
- **表名：** t_mrp_computebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisallowdateinpast | 允许计划建议开始日期在过去 | bpchar | 1 |  | √ | '0' | 允许计划建议开始日期在过去 |
| 3 | fenddate | 计划结束日期 | timestamp | 0 |  |  | null | 计划结束日期 |
| 4 | planorgid | planorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 6 | fplangramid | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案 mrp_planscheme |
| 7 | falgoregisterid | MRP算法 | int8 | 64 |  | √ | 0 | 算法注册配置 mrp_algoregister |
| 8 | fcomputedate | 运算日期 | timestamp | 0 |  |  | null | 运算日期 |
| 9 | fmrprunlogid | MRP日志内码 | int8 | 64 |  | √ | 0 | MRP日志内码 |
| 10 | fmtlexpandtype | 选料展开方式 | bpchar | 1 |  | √ | '1' | 选料展开方式,枚举: 1 :本层 2 :向下展开 3 :向上展开 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_computebill |  | fid |
| 2 | idx_mrp_computebill_logid |  | fmrprunlogid |
