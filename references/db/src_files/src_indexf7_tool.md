# 评分指标F7(工具)-src_indexf7_tool

## 评分指标F7(工具)-主表 t_src_schemeindex

- **表名称：** 评分指标F7(工具)-主表
- **表名：** t_src_schemeindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 评标方案ID | int8 | 64 |  | √ | 0 | 评标方案ID |
| 2 | fisscoretask | 下达评标任务 | bpchar | 1 |  | √ | '1' | 下达评标任务 |
| 3 | findexdimension | 评标维度 | varchar | 255 |  | √ | ' ' | 评标维度 |
| 4 | fsrcentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 5 | fhightvalue | 提醒值(>=) | numeric | 23 | 10 | √ | 0 | 提醒值(>=) |
| 6 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 7 | fseq | 指标分录序号 | int8 | 64 |  | √ | 0 | 指标分录序号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fisformula | 计算公式 | bpchar | 1 |  | √ | '0' | 计算公式 |
| 10 | fsrcindexlibid | 原始指标库ID | int8 | 64 |  | √ | 0 | 原始指标库ID |
| 11 | fisveto | 一票否决 | bpchar | 1 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 12 | fsrcindexid | 原始指标ID | int8 | 64 |  | √ | 0 | 原始指标ID |
| 13 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :手工评分 2 :自动评分 |
| 14 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 15 | fschemescore | 方案总分 | numeric | 23 | 10 | √ | 0 | 方案总分 |
| 16 | flowvalue | 提醒值(<=) | numeric | 23 | 10 | √ | 0 | 提醒值(<=) |
| 17 | fisopinion | 是否选择项 | bpchar | 1 |  | √ | '0' | 是否选择项 |
| 18 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 19 | fvaluebizobject | 关联的业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 20 | findex | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 21 | ffieldname | 关联的业务对象字段 | varchar | 50 |  | √ | ' ' | 关联的业务对象字段,枚举: |
| 22 | fproperty | 指标性质 | bpchar | 1 |  | √ | ' ' | 指标性质,枚举: 1 :定量指标 2 :定性指标 3 :门槛指标 |
| 23 | fisfitted | 是否符合项 | bpchar | 1 |  | √ | '0' | 是否符合项 |
| 24 | fvaluetype | 指标值类型 | bpchar | 1 |  | √ | '0' | 指标值类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉列表 |
| 25 | findexlibid | 指标库ID | int8 | 64 |  | √ | 0 | [指标库 src_index](../src_files/src_index.md) |
| 26 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fisthreshold | 是否门槛项 | bpchar | 1 |  | √ | '0' | 是否门槛项 |
| 28 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 29 | fitemtype | 指标可编辑性 | bpchar | 1 |  | √ | '1' | 指标可编辑性,枚举: 1 :采供双方均可编辑 2 :供应商可编辑，采购方可见不可编辑 3 :采购方可编辑，供应商可见不可编辑 4 :采购方可编辑，供应商不可见 |
| 30 | fscoremethod | 评分方法 | bpchar | 1 |  | √ | '1' | 评分方法,枚举: 1 :百分制(每个指标按百分制评分，方案=100分) 2 :实际值(每个指标按实际值评分，方案=100分) 3 :最终值(每个指标按最终值评分，方案<100分) |
| 31 | fisdeduct | 是否扣分指标 | bpchar | 1 |  | √ | '0' | 是否扣分指标 |
| 32 | fentryid | 指标分录ID | int8 | 64 |  | √ | 0 | 指标分录ID |
| 33 | fscore | 标准分值(权重) | numeric | 19 | 6 | √ | 0 | 标准分值(权重) |

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

---

## 评分指标F7(工具)-多语言表 t_src_schemeindex_l

- **表名称：** 评分指标F7(工具)-多语言表
- **表名：** t_src_schemeindex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | findexdimension | 评标维度 | varchar | 500 |  | √ | ' ' | 评标维度 |
| 2 | findex | 指标名称 | varchar | 500 |  | √ | ' ' | 指标名称 |
| 3 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 4 | fnote | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_schemeindex_l |  | fpkid |
| 2 | idx_src_schemeindex_l_fid |  | fentryid,flocaleid |
