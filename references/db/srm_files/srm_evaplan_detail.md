# 评估计划明细-srm_evaplan_detail

## 评估计划明细-主表 t_pur_evaplanindex

- **表名称：** 评估计划明细-主表
- **表名：** t_pur_evaplanindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fweight | 权重% | numeric | 19 | 6 | √ | 0.000000 | 权重% |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | 评估指标 srm_index |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_evaplanindex_idseq |  | fid,fseq |
| 2 | t_pur_evaplanindex_pkey |  | fentryid |
| 3 | idx_pur_evaplanindex_index |  | findexid |

---

## 评委分录-子表 t_pur_evaplandetail

- **表名称：** 评委分录-子表
- **表名：** t_pur_evaplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fweight | 权重% | numeric | 19 | 6 | √ | 0.000000 | 权重% |
| 2 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_evadetail_scorer |  | fscorerid |
| 2 | t_pur_evaplandetail_pkey |  | fdetailid |
| 3 | idx_pur_evadetail_eidseq |  | fentryid,fseq |
