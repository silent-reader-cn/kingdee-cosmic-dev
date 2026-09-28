# 专家考评结果F7-src_evaluateresultf7

## 专家考评结果F7-主表 t_src_evaluateresult

- **表名称：** 专家考评结果F7-主表
- **表名：** t_src_evaluateresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fgradeid | 考评等级 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | finputscore | 考评得分(线下) | numeric | 23 | 10 | √ | 0 | 考评得分(线下) |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 6 | faptitudenote | 考评意见 | varchar | 255 |  | √ | ' ' | 考评意见 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fscoretaskid | 考评任务单号 | int8 | 64 |  | √ | 0 | [考评记录F7 src_evaluatetaskf7](../src_files/src_evaluatetaskf7.md) |
| 9 | fisaptitude | 考评通过否 | bpchar | 1 |  | √ | '1' | 考评通过否,枚举: 0 :未考评 1 :考评通过 2 :考评不通过 |
| 10 | fentryparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_src_evaluateresult |  | fentryid |
| 2 | idx_src_evaluateresult_sid |  | fscoretaskid |
| 3 | idx_src_evaluateresult_fid |  | fid |
| 4 | idx_src_evaluateresult_pid |  | fentryparentid |
