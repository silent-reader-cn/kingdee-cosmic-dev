# 考评记录指标分录F7-src_evaluatetask_indexf7

## 考评记录指标分录F7-主表 t_src_evaluateentry

- **表名称：** 考评记录指标分录F7-主表
- **表名：** t_src_evaluateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 考评记录ID | int8 | 64 |  | √ | 0 | [考评记录F7 src_evaluatetaskf7](../src_files/src_evaluatetaskf7.md) |
| 2 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 3 | ffinalscore | 最终得分 | numeric | 19 | 6 | √ | 0 | 最终得分 |
| 4 | findexdimension | 评标维度 | varchar | 255 |  | √ | ' ' | 评标维度 |
| 5 | fmanscore | 评委评分 | numeric | 19 | 6 | √ | 0 | 评委评分 |
| 6 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 7 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | 'A' |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 10 | findexlibid | 指标库ID | int8 | 64 |  | √ | 0 | [指标库 src_index](../src_files/src_index.md) |
| 11 | fisveto | fisveto | bpchar | 1 |  | √ | '0' |  |
| 12 | fisthreshold | 是否门槛值 | bpchar | 1 |  | √ | '0' | 是否门槛值 |
| 13 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 14 | fsysscore | 系统评分 | numeric | 19 | 6 | √ | 0 | 系统评分 |
| 15 | fscored | 指标已评分 | bpchar | 1 |  | √ | ' ' | 指标已评分 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_evaluateentry |  | fentryid |
| 2 | idx_src_evaluateentry_fid |  | fid |
| 3 | idx_src_evaluateentry_indexid |  | findexid |
