# 评分任务明细-srm_score_detail

## 评分任务明细-主表 t_pur_scoredetail

- **表名称：** 评分任务明细-主表
- **表名：** t_pur_scoredetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fveto | 一票否决 | bpchar | 1 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 9 :非否决项 |
| 2 | fabstain | 放弃评分 | bpchar | 1 |  | √ | '0' | 放弃评分 |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fvalue | 评估结果 | numeric | 19 | 6 | √ | 0.000000 | 评估结果 |
| 6 | fscorersave | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 7 | fweight | 评委权重% | numeric | 19 | 6 | √ | 0.000000 | 评委权重% |
| 8 | fscorerscore | 权重得分 | numeric | 19 | 6 | √ | 0.000000 | 权重得分 |
| 9 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fscored | 评委已评分 | bpchar | 1 |  | √ | ' ' | 评委已评分 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | faccordance | 符合项判断 | varchar | 50 |  | √ | ' ' | 符合项判断 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fscore | 得分 | numeric | 19 | 6 | √ | 0.000000 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_scoredetail_eidseq |  | fentryid,fseq |
| 2 | idx_pur_scoredetail_scorer |  | fscorerid |
| 3 | t_pur_scoredetail_pkey |  | fdetailid |

---

## 附件-附件表 t_pur_srmscoreatt

- **表名称：** 附件-附件表
- **表名：** t_pur_srmscoreatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_srmscoreatt |  | fpkid |
| 2 | idx_pur_srmscoreatt_fbdid |  | fbasedataid |
