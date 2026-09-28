# 指标分录及评委子分录-src_evaluatetask_detail

## 指标分录及评委子分录-主表 t_src_evaluateentry

- **表名称：** 指标分录及评委子分录-主表
- **表名：** t_src_evaluateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 考评记录ID | int8 | 64 |  | √ | 0 | 评标任务F7 src_scoretaskf7 |
| 2 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 3 | ffinalscore | 最终得分 | numeric | 19 | 6 | √ | 0 | 最终得分 |
| 4 | findexdimension | 评标维度 | varchar | 255 |  | √ | ' ' | 评标维度 |
| 5 | fmanscore | 评委评分 | numeric | 19 | 6 | √ | 0 | 评委评分 |
| 6 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 7 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 8 | findexid | 评分指标 | int8 | 64 |  | √ | 0 | 评分指标F7 src_indexf7 |
| 9 | findexlibid | 指标库 | int8 | 64 |  | √ | 0 | 指标库 src_index |
| 10 | fisveto | fisveto | bpchar | 1 |  | √ | '0' |  |
| 11 | fisthreshold | 是否门槛 | bpchar | 1 |  | √ | '0' | 是否门槛 |
| 12 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 13 | fsysscore | 系统评分 | numeric | 19 | 6 | √ | 0 | 系统评分 |
| 14 | fscored | 指标已评分 | bpchar | 1 |  | √ | ' ' | 指标已评分 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

---

## 评委分录-子表 t_src_evaluatedetail

- **表名称：** 评委分录-子表
- **表名：** t_src_evaluatedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fsrcentryid | 评标设置分录ID | int8 | 64 |  | √ | 0 | 评标设置分录ID |
| 3 | fveto | fveto | varchar | 30 |  | √ | ' ' |  |
| 4 | fisoverthreshold | fisoverthreshold | bpchar | 1 |  | √ | '0' |  |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 8 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | 评分指标F7 src_indexf7 |
| 9 | fscorerweight | 权重% | numeric | 23 | 10 | √ | 0 | 权重% |
| 10 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 标的ID |
| 11 | fisveto | fisveto | varchar | 30 |  | √ | '0' |  |
| 12 | finvalid | finvalid | bpchar | 1 |  | √ | '0' |  |
| 13 | fpackageid | 标段ID | int8 | 64 |  | √ | 0 | 标段ID |
| 14 | fscored | fscored | bpchar | 1 |  | √ | '0' |  |
| 15 | fisautoscore | fisautoscore | bpchar | 1 |  | √ | '0' |  |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | findexscore | 标准分值(权重) | numeric | 23 | 10 | √ | 0 | 标准分值(权重) |
| 18 | fprojectid | 项目ID | int8 | 64 |  | √ | 0 | 项目ID |
| 19 | faverage | faverage | numeric | 23 | 10 | √ | 0 |  |
| 20 | fparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 21 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 22 | fisfitted | fisfitted | bpchar | 1 |  | √ | '0' |  |
| 23 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 26 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 27 | fscorerscore | 评委得分 | numeric | 23 | 10 | √ | 0 | 评委得分 |
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
