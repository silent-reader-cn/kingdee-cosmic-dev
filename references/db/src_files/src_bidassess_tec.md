# 评标汇总分录(后台元数据)-src_bidassess_tec

## 评标汇总分录(后台元数据)-主表 t_src_assesssum

- **表名称：** 评标汇总分录(后台元数据)-主表
- **表名：** t_src_assesssum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 5 | faptitudenote | 评标意见 | varchar | 255 |  | √ | ' ' | 评标意见 |
| 6 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 7 | fisaptitude | 评标通过否 | varchar | 2 |  | √ | ' ' | 评标通过否,枚举: 0 :未评标 1 :评标合格 2 :评标不合格 |
| 8 | findextypeid | findextypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 10 | finputscore | 评估得分(线下) | numeric | 19 | 6 | √ | 0 | 评估得分(线下) |
| 11 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fscoretaskid | 评标任务单号 | int8 | 64 |  | √ | 0 | [评标任务F7 src_scoretaskf7](../src_files/src_scoretaskf7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_assesssum_packid |  | fpackageid |
| 2 | idx_src_assesssum_fid |  | fid |
| 3 | pk_src_assesssum |  | fentryid |
| 4 | idx_src_assesssum_supid |  | fsupplierid |
| 5 | idx_src_assesssum_proid |  | fprojectid |
| 6 | idx_src_assesssum_taskid |  | fscoretaskid |
