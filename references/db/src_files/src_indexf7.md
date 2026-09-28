# 评分指标F7-src_indexf7

## 评分指标F7-主表 t_src_schemeindex

- **表名称：** 评分指标F7-主表
- **表名：** t_src_schemeindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 评标方案ID | int8 | 64 |  | √ | 0 | 评标方案ID |
| 2 | findexdimension | 评标维度 | varchar | 255 |  | √ | ' ' | 评标维度 |
| 3 | fsrcentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 4 | fhightvalue | 提醒值(>=) | numeric | 23 | 10 | √ | 0 | 提醒值(>=) |
| 5 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fisformula | 计算公式 | bpchar | 1 |  | √ | '0' | 计算公式 |
| 9 | fsrcindexlibid | 原始指标库ID | int8 | 64 |  | √ | 0 | 原始指标库ID |
| 10 | fisveto | 一票否决 | bpchar | 1 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 11 | fsrcindexid | 原始指标ID | int8 | 64 |  | √ | 0 | 原始指标ID |
| 12 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :手工评分 2 :自动评分 |
| 13 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 14 | fschemescore | 方案总分 | numeric | 23 | 10 | √ | 0 | 方案总分 |
| 15 | flowvalue | 提醒值(<=) | numeric | 23 | 10 | √ | 0 | 提醒值(<=) |
| 16 | fisopinion | 是否选择项 | bpchar | 1 |  | √ | '0' | 是否选择项 |
| 17 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 18 | findex | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 19 | fproperty | 指标性质 | bpchar | 1 |  | √ | ' ' | 指标性质,枚举: 1 :定量指标 2 :定性指标 3 :门槛指标 |
| 20 | fisfitted | 是否符合项 | bpchar | 1 |  | √ | '0' | 是否符合项 |
| 21 | findexlibid | 指标库ID | int8 | 64 |  | √ | 0 | 指标库 src_index |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | fisthreshold | 门槛值 | bpchar | 1 |  | √ | '0' | 门槛值 |
| 24 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 25 | fscoremethod | 评分方法 | bpchar | 1 |  | √ | '1' | 评分方法,枚举: 1 :百分制(每个指标按百分制评分，方案=100分) 2 :实际值(每个指标按实际值评分，方案=100分) 3 :最终值(每个指标按最终值评分，方案<100分) |
| 26 | fisdeduct | 扣分指标 | bpchar | 1 |  | √ | '0' | 扣分指标 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fscore | 标准分值(权重) | numeric | 19 | 6 | √ | 0 | 标准分值(权重) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_schemeindex_fsrcid |  | fsrcindexid |
| 2 | idx_src_schemeindex_findex |  | findex |
| 3 | idx_src_schemeindex_flibid |  | findexlibid |
| 4 | idx_src_schemeindex_fsrclibid |  | fsrcindexlibid |
| 5 | pk_src_schemeindex |  | fentryid |
| 6 | idx_src_schemeindex_fid |  | fid |
| 7 | idx_src_schemeindex_fsid |  | fsupplierid |
