# 考评记录评委分录-src_evaluate_detail

## 考评记录评委分录-主表 t_src_evaluatedetail

- **表名称：** 考评记录评委分录-主表
- **表名：** t_src_evaluatedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fagentid | fagentid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 源单分录id(考评设置分录ID) | int8 | 64 |  | √ | 0 | 源单分录id(考评设置分录ID) |
| 3 | fveto | 一票否决 | varchar | 30 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 9 :非否决项 |
| 4 | fisoverthreshold | fisoverthreshold | bpchar | 1 |  | √ | '0' |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | findexid | findexid | int8 | 64 |  | √ | 0 |  |
| 9 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 10 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 11 | fisveto | fisveto | varchar | 30 |  | √ | '0' |  |
| 12 | finvalid | finvalid | bpchar | 1 |  | √ | '0' |  |
| 13 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 14 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 15 | fisautoscore | fisautoscore | bpchar | 1 |  | √ | '0' |  |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | findexscore | findexscore | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 19 | faverage | faverage | numeric | 23 | 10 | √ | 0 |  |
| 20 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 21 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 22 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 23 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 26 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 27 | fscorerscore | 权重得分 | numeric | 23 | 10 | √ | 0 | 权重得分 |
| 28 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evadetail_parentid |  | fparentid |
| 2 | idx_src_evaetail_scorerid |  | fscorerid |
| 3 | idx_src_evadetail_pid |  | fprojectid |
| 4 | idx_src_evaetail_eid |  | fentryid |
| 5 | pk_src_evaluatedetail |  | fdetailid |
| 6 | idx_src_evaetail_agentid |  | fagentid |
