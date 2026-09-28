# 评标任务明细分录-src_scoretask_detail

## 评标任务明细分录-主表 t_src_scoreentry

- **表名称：** 评标任务明细分录-主表
- **表名：** t_src_scoreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 评标任务 | int8 | 64 |  | √ | 0 | [评标任务F7 src_scoretaskf7](../src_files/src_scoretaskf7.md) |
| 2 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 3 | faptitudereplyvalue | faptitudereplyvalue | varchar | 512 |  | √ | ' ' |  |
| 4 | ffinalscore | 最终得分 | numeric | 19 | 6 | √ | 0 | 最终得分 |
| 5 | findexdimension | 评标维度 | varchar | 255 |  | √ | ' ' | 评标维度 |
| 6 | fmanscore | 评委评分 | numeric | 19 | 6 | √ | 0 | 评委评分 |
| 7 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 8 | fentrystatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :待回复 B :已提交 C :已回复 |
| 9 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 10 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 11 | findexlibid | 指标库 | int8 | 64 |  | √ | 0 | [指标库 src_index](../src_files/src_index.md) |
| 12 | fisveto | fisveto | bpchar | 1 |  | √ | '0' |  |
| 13 | fisthreshold | 是否门槛 | bpchar | 1 |  | √ | '0' | 是否门槛 |
| 14 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 15 | fsysscore | 系统评分 | numeric | 19 | 6 | √ | 0 | 系统评分 |
| 16 | fscored | 指标已评分 | bpchar | 1 |  | √ | ' ' | 指标已评分 |
| 17 | faptitudereply | faptitudereply | varchar | 512 |  | √ | ' ' |  |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_scoreentry_indexid |  | findexid |
| 2 | pk_src_scoreentry |  | fentryid |
| 3 | idx_src_scoreentry_fid |  | fid |

---

## 评委分录-子表 t_src_scoredetail

- **表名称：** 评委分录-子表
- **表名：** t_src_scoredetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcentryid | 评标设置分录ID | int8 | 64 |  | √ | 0 | 评标设置分录ID |
| 4 | fveto | fveto | varchar | 30 |  | √ | ' ' |  |
| 5 | fisoverthreshold | fisoverthreshold | bpchar | 1 |  | √ | '0' |  |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 10 | fscorerweight | 权重% | numeric | 23 | 10 | √ | 0 | 权重% |
| 11 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 标的ID |
| 12 | fisveto | fisveto | varchar | 30 |  | √ | '0' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | finvalid | finvalid | bpchar | 1 |  | √ | '0' |  |
| 15 | fpackageid | 标段ID | int8 | 64 |  | √ | 0 | 标段ID |
| 16 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 17 | fisautoscore | fisautoscore | bpchar | 1 |  | √ | '0' |  |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | findexscore | 标准分值(权重) | numeric | 23 | 10 | √ | 0 | 标准分值(权重) |
| 20 | fprojectid | 项目ID | int8 | 64 |  | √ | 0 | 项目ID |
| 21 | faverage | faverage | numeric | 23 | 10 | √ | 0 |  |
| 22 | fparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 23 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 24 | fisfitted | fisfitted | bpchar | 1 |  | √ | '0' |  |
| 25 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 28 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 29 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 30 | fscorerscore | 评委得分 | numeric | 23 | 10 | √ | 0 | 评委得分 |
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
