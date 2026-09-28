# 工序计划生成日志-sfc_processplanlog

## 工序计划生成日志-主表 t_sfc_proplanlog

- **表名称：** 工序计划生成日志-主表
- **表名：** t_sfc_proplanlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | flogmessage | 日志信息 | varchar | 255 |  | √ | ' ' | 日志信息 |
| 4 | fproplanbillno | 工序计划号 | varchar | 100 |  | √ | ' ' | 工序计划号 |
| 5 | fbatchno | 批次 | varchar | 50 |  | √ | ' ' | 批次 |
| 6 | flogmessage_tag | 日志信息_详情 | text | 0 |  |  | null | 日志信息_详情 |
| 7 | fworkn | 工单号 | varchar | 80 |  | √ | ' ' | 工单号 |
| 8 | flogtype | 日志类型 | bpchar | 1 |  | √ | ' ' | 日志类型,枚举: A :入参校验不通过 B :下推条件不满足 C :保存校验不通过 D :信息记录 F :下达校验不通过 |
| 9 | fworkrown | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_proplanlog |  | fid |
| 2 | idx_sfclog_date |  | fcreatedate |
