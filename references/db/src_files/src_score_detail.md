# 评分任务评委分录-src_score_detail

## 评分任务评委分录-主表 t_src_scoredetail

- **表名称：** 评分任务评委分录-主表
- **表名：** t_src_scoredetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcentryid | 源单分录id(评标设置分录ID) | int8 | 64 |  | √ | 0 | 源单分录id(评标设置分录ID) |
| 4 | fveto | 一票否决 | varchar | 30 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 9 :非否决项 |
| 5 | fisoverthreshold | fisoverthreshold | bpchar | 1 |  | √ | '0' |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | findexid | findexid | int8 | 64 |  | √ | 0 |  |
| 10 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 11 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 12 | fisveto | fisveto | varchar | 30 |  | √ | '0' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | finvalid | finvalid | bpchar | 1 |  | √ | '0' |  |
| 15 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 16 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 17 | fisautoscore | fisautoscore | bpchar | 1 |  | √ | '0' |  |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | findexscore | findexscore | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | faverage | faverage | numeric | 23 | 10 | √ | 0 |  |
| 22 | fparentid | 评标任务 | int8 | 64 |  | √ | 0 | [评标任务F7 src_scoretaskf7](../src_files/src_scoretaskf7.md) |
| 23 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 24 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 25 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 28 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 29 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 30 | fscorerscore | 权重得分 | numeric | 23 | 10 | √ | 0 | 权重得分 |
| 31 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_scoredetail |  | fdetailid |
| 2 | idx_src_scoredetail_supid |  | fsupplierid |
| 3 | idx_src_scoredetail_parentid |  | fparentid |
| 4 | idx_src_scoredetail_agentid |  | fagentid |
| 5 | idx_src_scoredetail_scorerid |  | fscorerid |
| 6 | idx_src_scoredetail_entryid |  | fentryid |
| 7 | idx_src_scoredetail_pid |  | fprojectid |
