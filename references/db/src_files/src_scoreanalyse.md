# 评标分析-src_scoreanalyse

## 评标分析-主表 t_src_scoredetail

- **表名称：** 评标分析-主表
- **表名：** t_src_scoredetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcentryid | 评标设置分录ID | int8 | 64 |  | √ | 0 | 评标设置分录ID |
| 4 | fveto | 一票否决 | varchar | 30 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 9 :非否决项 |
| 5 | fisoverthreshold | 未满足门槛值 | bpchar | 1 |  | √ | '0' | 未满足门槛值 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 10 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 11 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fisveto | fisveto | varchar | 30 |  | √ | '0' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | finvalid | 评分异常否 | bpchar | 1 |  | √ | '0' | 评分异常否,枚举: 0 :正常 1 :偏差过大 2 :去掉最低分 3 :去掉最高分 |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 16 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 17 | fisautoscore | 系统自动评分 | bpchar | 1 |  | √ | '0' | 系统自动评分 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | findexscore | 标准分值(权重) | numeric | 23 | 10 | √ | 0 | 标准分值(权重) |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | faverage | 平均分 | numeric | 23 | 10 | √ | 0 | 平均分 |
| 22 | fparentid | 评标任务 | int8 | 64 |  | √ | 0 | [评标任务F7 src_scoretaskf7](../src_files/src_scoretaskf7.md) |
| 23 | fsuppliername | 供应商(列表显示) | varchar | 100 |  | √ | ' ' | 供应商(列表显示) |
| 24 | fisfitted | 是否符合 | bpchar | 1 |  | √ | '0' | 是否符合 |
| 25 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 28 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 29 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 30 | fscorerscore | 评委得分 | numeric | 23 | 10 | √ | 0 | 评委得分 |
| 31 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fentryid | 评标任务指标分录 | int8 | 64 |  | √ | 0 | [评标任务指标分录F7 src_scoretask_indexf7](../src_files/src_scoretask_indexf7.md) |
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
