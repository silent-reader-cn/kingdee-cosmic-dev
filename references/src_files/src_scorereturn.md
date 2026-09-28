# 退回重评日志-src_scorereturn

## 退回重评日志-主表 t_src_scorereturn

- **表名称：** 退回重评日志-主表
- **表名：** t_src_scorereturn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsrcentryid | 评标设置分录ID | int8 | 64 |  | √ | 0 | 评标设置分录ID |
| 4 | fveto | fveto | varchar | 30 |  | √ | ' ' |  |
| 5 | fisoverthreshold | 未满足门槛值 | bpchar | 1 |  | √ | '0' | 未满足门槛值 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | 评分指标F7 src_indexf7 |
| 10 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 11 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fisveto | fisveto | bpchar | 1 |  | √ | '0' |  |
| 13 | fcreatorid | 退回人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | finvalid | 评分异常否 | bpchar | 1 |  | √ | '0' | 评分异常否,枚举: 0 :正常 1 :偏差过大 2 :去掉最低分 3 :去掉最高分 |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 16 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 17 | fisautoscore | 系统自动评分 | bpchar | 1 |  | √ | '0' | 系统自动评分 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | findexscore | 标准分值(权重) | numeric | 23 | 10 | √ | 0 | 标准分值(权重) |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 21 | faverage | 平均分 | numeric | 23 | 10 | √ | 0 | 平均分 |
| 22 | fparentid | 评标任务 | int8 | 64 |  | √ | 0 | 评标任务F7 src_scoretaskf7 |
| 23 | fcreatetime | 退回时间 | timestamp | 0 |  |  | null | 退回时间 |
| 24 | fsuppliername | 供应商(列表显示) | varchar | 255 |  | √ | ' ' | 供应商(列表显示) |
| 25 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 26 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 27 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 28 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 29 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 30 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 31 | fscorerscore | 评委得分 | numeric | 23 | 10 | √ | 0 | 评委得分 |
| 32 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fentryid | 评标任务指标分录 | int8 | 64 |  | √ | 0 | 评标任务指标分录F7 src_scoretask_indexf7 |
| 34 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_scorereturn_entryid |  | fentryid |
| 2 | idx_src_scorereturn_parentid |  | fparentid |
| 3 | idx_src_scorereturn_scorerid |  | fscorerid |
| 4 | idx_src_scorereturn_agentid |  | fagentid |
| 5 | idx_src_scorereturn_supid |  | fsupplierid |
| 6 | pk_src_scorereturn |  | fdetailid |
| 7 | idx_src_scorereturn_pid |  | fprojectid |
