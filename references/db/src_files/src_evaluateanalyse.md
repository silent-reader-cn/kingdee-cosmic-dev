# 专家评分明细-src_evaluateanalyse

## 专家评分明细-主表 t_src_evaluatedetail

- **表名称：** 专家评分明细-主表
- **表名：** t_src_evaluatedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fsrcentryid | 考评设置分录ID | int8 | 64 |  | √ | 0 | 考评设置分录ID |
| 3 | fveto | 一票否决 | varchar | 30 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 9 :非否决项 |
| 4 | fisoverthreshold | 未满足门槛值 | bpchar | 1 |  | √ | '0' | 未满足门槛值 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 9 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fisveto | fisveto | varchar | 30 |  | √ | '0' |  |
| 12 | finvalid | 评分异常否 | bpchar | 1 |  | √ | '0' | 评分异常否,枚举: 0 :正常 1 :偏差过大 2 :去掉最低分 3 :去掉最高分 |
| 13 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 14 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 15 | fisautoscore | 系统自动评分 | bpchar | 1 |  | √ | '0' | 系统自动评分 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | findexscore | 标准分值(权重) | numeric | 23 | 10 | √ | 0 | 标准分值(权重) |
| 18 | fprojectid | 考评单号 | int8 | 64 |  | √ | 0 | [专家考评F7 src_evaluatef7](../src_files/src_evaluatef7.md) |
| 19 | faverage | 平均分 | numeric | 23 | 10 | √ | 0 | 平均分 |
| 20 | fparentid | 考评任务 | int8 | 64 |  | √ | 0 | [考评记录F7 src_evaluatetaskf7](../src_files/src_evaluatetaskf7.md) |
| 21 | fsuppliername | 专家(列表显示) | varchar | 100 |  | √ | ' ' | 专家(列表显示) |
| 22 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 23 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 26 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 27 | fscorerscore | 评委得分 | numeric | 23 | 10 | √ | 0 | 评委得分 |
| 28 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fentryid | 考评任务指标分录 | int8 | 64 |  | √ | 0 | [考评记录指标分录F7 src_evaluatetask_indexf7](../src_files/src_evaluatetask_indexf7.md) |
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
