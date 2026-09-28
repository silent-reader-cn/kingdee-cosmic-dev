# 编码规则区间段划分-bos_coderuleseqsegment

## 编码规则区间段划分-主表 t_cr_seqsegment

- **表名称：** 编码规则区间段划分-主表
- **表名：** t_cr_seqsegment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fcoderuleid | 编码规则内码 | varchar | 36 |  | √ | ' ' | 编码规则内码 |
| 3 | fattrnumber | 属性编码id | varchar | 100 |  | √ | ' ' | 属性编码id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cr_seqsegment_pkey |  | fid |
| 2 | idx_t_cr_seqsegment_fcrid |  | fcoderuleid |

---

## 单据体-子表 t_cr_seqsegmententry

- **表名称：** 单据体-子表
- **表名：** t_cr_seqsegmententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fendnum | 终止编号 | int8 | 64 |  | √ | 0 | 终止编号 |
| 3 | fbeginnum | 起始编号 | int8 | 64 |  | √ | 0 | 起始编号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 6 | fattributeid | 属性值ID | int8 | 64 |  | √ | 0 | 属性值ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_seqsegmententry_fid |  | fid |
| 2 | t_cr_seqsegmententry_pkey |  | fentryid |
