# 退回重评日志-src_evaluatereturn

## 退回重评日志-主表 t_src_evaluatereturn

- **表名称：** 退回重评日志-主表
- **表名：** t_src_evaluatereturn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fsrcentryid | 考评设置分录ID | int8 | 64 |  | √ | 0 | 考评设置分录ID |
| 3 | fveto | fveto | varchar | 30 |  | √ | ' ' |  |
| 4 | fisoverthreshold | 未满足门槛值 | bpchar | 1 |  | √ | '0' | 未满足门槛值 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 9 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fisveto | fisveto | bpchar | 1 |  | √ | '0' |  |
| 12 | fcreatorid | 退回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | finvalid | 评分异常否 | bpchar | 1 |  | √ | '0' | 评分异常否,枚举: 0 :正常 1 :偏差过大 2 :去掉最低分 3 :去掉最高分 |
| 14 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 15 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 16 | fisautoscore | 系统自动评分 | bpchar | 1 |  | √ | '0' | 系统自动评分 |
| 17 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 18 | findexscore | 标准分值(权重) | numeric | 23 | 10 | √ | 0 | 标准分值(权重) |
| 19 | fprojectid | 考评单号 | int8 | 64 |  | √ | 0 | [专家考评F7 src_evaluatef7](../src_files/src_evaluatef7.md) |
| 20 | faverage | 平均分 | numeric | 23 | 10 | √ | 0 | 平均分 |
| 21 | fparentid | 考评任务 | int8 | 64 |  | √ | 0 | [考评记录F7 src_evaluatetaskf7](../src_files/src_evaluatetaskf7.md) |
| 22 | fcreatetime | 退回时间 | timestamp | 0 |  |  | null | 退回时间 |
| 23 | fsuppliername | 专家(列表显示) | varchar | 255 |  | √ | ' ' | 专家(列表显示) |
| 24 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 25 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fscorerscore | 评委得分 | numeric | 23 | 10 | √ | 0 | 评委得分 |
| 30 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fentryid | 考评任务指标分录 | int8 | 64 |  | √ | 0 | [考评记录指标分录F7 src_evaluatetask_indexf7](../src_files/src_evaluatetask_indexf7.md) |
| 32 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_evaluatereturn |  | fdetailid |
| 2 | idx_src_evaluatereturn_aid |  | fagentid |
| 3 | idx_src_evaluatereturn_prid |  | fprojectid |
| 4 | idx_src_evaluatereturnl_sid |  | fscorerid |
| 5 | idx_src_evaluatereturn_eid |  | fentryid |
| 6 | idx_src_evaluatereturn_paid |  | fparentid |
