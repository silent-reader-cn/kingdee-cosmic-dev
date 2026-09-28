# 评标任务指标分录F7-src_scoretask_indexf7

## 供应商回复附件-附件表 t_src_aptitudereply_fj

- **表名称：** 供应商回复附件-附件表
- **表名：** t_src_aptitudereply_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_aptitudereply_fj_bid |  | fbasedataid |
| 2 | pk_src_aptitudereply_fj |  | fpkid |
| 3 | idx_src_aptitudereply_fj_fid |  | fentryid |

---

## 评标任务指标分录F7-主表 t_src_scoreentry

- **表名称：** 评标任务指标分录F7-主表
- **表名：** t_src_scoreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 评标任务 | int8 | 64 |  | √ | 0 | [评标任务F7 src_scoretaskf7](../src_files/src_scoretaskf7.md) |
| 2 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 3 | faptitudereplyvalue | 供应商回复值 | varchar | 512 |  | √ | ' ' | 供应商回复值 |
| 4 | ffinalscore | 最终得分 | numeric | 19 | 6 | √ | 0 | 最终得分 |
| 5 | findexdimension | 评标维度 | varchar | 255 |  | √ | ' ' | 评标维度 |
| 6 | fmanscore | 评委评分 | numeric | 19 | 6 | √ | 0 | 评委评分 |
| 7 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 8 | fentrystatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :待回复 B :已提交 C :已回复 |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 11 | findexlibid | 指标库ID | int8 | 64 |  | √ | 0 | [指标库 src_index](../src_files/src_index.md) |
| 12 | fisveto | fisveto | bpchar | 1 |  | √ | '0' |  |
| 13 | fisthreshold | 是否门槛值 | bpchar | 1 |  | √ | '0' | 是否门槛值 |
| 14 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 15 | fsysscore | 系统评分 | numeric | 19 | 6 | √ | 0 | 系统评分 |
| 16 | fscored | 指标已评分 | bpchar | 1 |  | √ | ' ' | 指标已评分 |
| 17 | faptitudereply | 供应商回复内容 | varchar | 512 |  | √ | ' ' | 供应商回复内容 |
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
