# 资审结果F7-src_aptituderesultf7

## 资审结果F7-主表 t_src_aptituderesult

- **表名称：** 资审结果F7-主表
- **表名：** t_src_aptituderesult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | finputscore | finputscore | numeric | 23 | 10 | √ | 0 |  |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fnote | fnote | varchar | 100 |  | √ | ' ' |  |
| 5 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fscoretaskid | 评标任务单号 | int8 | 64 |  | √ | 0 | 评标任务F7 src_scoretaskf7 |
| 8 | fisaptitude | 资审通过否 | bpchar | 1 |  | √ | '1' | 资审通过否,枚举: 0 :未资审 1 :资审通过 2 :资审不通过 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_aptituderesult_fid |  | fid |
| 2 | idx_src_aptituderesult_fsid |  | fscoretaskid |
| 3 | pk_src_aptituderesult |  | fentryid |
