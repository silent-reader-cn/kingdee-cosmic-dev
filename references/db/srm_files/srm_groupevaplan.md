# 集团评估计划-srm_groupevaplan

## 集团评估计划-反写记录表 t_srm_groupevaplan_wb

- **表名称：** 集团评估计划-反写记录表
- **表名：** t_srm_groupevaplan_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_groupevaplan_wb_fk |  | fid |
| 2 | pk_srm_groupevaplan_wb |  | fentryid |

---

## 指标分录-子表 t_srm_groupevaplanindex

- **表名称：** 指标分录-子表
- **表名：** t_srm_groupevaplanindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | findexid | 评估指标 | int8 | 64 |  | √ | 0 | [评估指标 srm_index](../srm_files/srm_index.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_gevaplanindex_index |  | findexid |
| 2 | pk_srm_groupevaplanindex |  | fentryid |
| 3 | idx_srm_gevaplanindex_idseq |  | fid,fseq |

---

## 集团评估计划-关联追踪表 t_srm_groupevaplan_tc

- **表名称：** 集团评估计划-关联追踪表
- **表名：** t_srm_groupevaplan_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_groupevaplan_tc_tbill |  | ftbillid |
| 2 | pk_srm_groupevaplan_tc |  | fid |
| 3 | idx_srm_groupevaplan_tc_tid |  | ftid |

---

## 供应商分录-子表 t_srm_groupevaplanentry

- **表名称：** 供应商分录-子表
- **表名：** t_srm_groupevaplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_groupevaplanentry |  | fentryid |
| 2 | idx_srm_gevaplansup_fsupid |  | fsupplierid |
| 3 | idx_srm_gevaplansup_fid |  | fid |

---

## 评估对象分录-子表 t_srm_groupevasupentry

- **表名称：** 评估对象分录-子表
- **表名：** t_srm_groupevasupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevasupnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fevacategoryid | 评估品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | fevamaterialid | 评估物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fevagradeid | 分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 8 | fweightstrategy | 评委权重策略 | varchar | 1 |  | √ | ' ' | 评委权重策略,枚举: A :权重平均计算 B :自定义权重 |
| 9 | fevasupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fevaschemeid | 评估方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_gplansupentry_fsupid |  | fevasupplierid |
| 2 | pk_srm_groupevasupentry |  | fentryid |
| 3 | idx_srm_gplansupentry_fid |  | fid |

---

## 评估物料-子表 t_srm_groupevasubentry

- **表名称：** 评估物料-子表
- **表名：** t_srm_groupevasubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 评估物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_srm_gevasub_entryid |  | fentryid |
| 2 | pk_srm_groupevasubentry |  | fdetailid |

---

## 集团评估计划-主表 t_srm_groupevaplan

- **表名称：** 集团评估计划-主表
- **表名：** t_srm_groupevaplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fistypescorer | 按一级指标类型设置评委 | bpchar | 1 |  | √ | ' ' | 按一级指标类型设置评委 |
| 3 | fevamethod | 评估方式 | bpchar | 1 |  | √ | 'A' | 评估方式,枚举: A :供应商 B :物料+供应商 D :品类+供应商 |
| 4 | forgid | 集团 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcansumcalculate | 可汇总计算 | bpchar | 1 |  | √ | ' ' | 可汇总计算 |
| 6 | fterminatecaltype | 评估组织权重动态调配方案 | bpchar | 1 |  | √ | ' ' | 评估组织权重动态调配方案,枚举: 1 :按权重比例动态调配 2 :平均分配至其他权重 3 :按设置比例直接计算 |
| 7 | fschemeid | 评估方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |
| 8 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbilldate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 10 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 11 | favgcal | 平均计算 | bpchar | 1 |  | √ | '1' | 平均计算 |
| 12 | fdatetimeto | 分级有效日期至 | timestamp | 0 |  |  | null | 分级有效日期至 |
| 13 | fcategoryid | 评估品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 14 | fdatefrom | 评估期间从 | timestamp | 0 |  |  | null | 评估期间从 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 17 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 18 | fcompsumcalculate | 已汇总计算 | bpchar | 1 |  | √ | ' ' | 已汇总计算 |
| 19 | fgroupgradeid | 集团分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 20 | fdateto | 评估期间至 | timestamp | 0 |  |  | null | 评估期间至 |
| 21 | fgradeid | 分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 X :已终止 |
| 23 | fevatypeid | 评估类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 24 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 25 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 26 | ffinishdate | 要求完成日期 | timestamp | 0 |  |  | null | 要求完成日期 |
| 27 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 28 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 29 | ftype | 下发类型 | bpchar | 1 |  | √ | ' ' | 下发类型,枚举: 1 :评估计划（保存） 2 :评估计划（已审核并下达） 3 :绩效评估计划（保存） 4 :绩效评估计划（已审核并下达） |
| 30 | fdatetimefrom | 分级有效日期从 | timestamp | 0 |  |  | null | 分级有效日期从 |
| 31 | fperiod | 评估周期 | bpchar | 1 |  | √ | ' ' | 评估周期,枚举: 1 :年度 2 :半年 3 :季度 4 :月度 5 :按需 |
| 32 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_gevaplan_fbilldate |  | fbilldate |
| 2 | idx_srm_gevaplan_fbillno |  | fbillno |
| 3 | pk_srm_groupevaplan |  | fid |

---

## 评委明细-子表 t_srm_groupevaplandetail

- **表名称：** 评委明细-子表
- **表名：** t_srm_groupevaplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 评委权重% | numeric | 19 | 6 | √ | 0 | 评委权重% |
| 3 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_gevadetail_scorer |  | fscorerid |
| 2 | pk_srm_groupevaplandetail |  | fdetailid |
| 3 | idx_srm_gevadetail_idseq |  | fentryid,fseq |

---

## 集团评估计划-分表 t_srm_groupevaplan_a

- **表名称：** 集团评估计划-分表
- **表名：** t_srm_groupevaplan_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fterminatedate | 终止时间 | timestamp | 0 |  |  | null | 终止时间 |
| 6 | fcfmopinion | fcfmopinion | varchar | 255 |  | √ | ' ' |  |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftermination | 终止意见 | varchar | 255 |  | √ | ' ' | 终止意见 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fterminaterid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_groupevaplan_a |  | fid |
| 2 | idx_srm_groupevaplan_a_ftime |  | fcreatetime |

---

## 集团评估计划-多语言表 t_srm_groupevaplan_l

- **表名称：** 集团评估计划-多语言表
- **表名：** t_srm_groupevaplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_groupevaplan_l |  | fpkid |
| 2 | idx_srm_gevaplan_l_idlocale |  | fid,flocaleid |

---

## 评委信息分录-子表 t_srm_groupscorerentry

- **表名称：** 评委信息分录-子表
- **表名：** t_srm_groupscorerentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fevaindexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类 srm_indexclass](../srm_files/srm_indexclass.md) |
| 2 | fevascorernote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fevascorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fevascorerweight | 评委权重 | numeric | 23 | 10 | √ | 0 | 评委权重 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_srm_gplanscorer_entryid |  | fentryid |
| 2 | pk_srm_groupscorerentry |  | fdetailid |

---

## 评估组织分录-子表 t_srm_evaorgentry

- **表名称：** 评估组织分录-子表
- **表名：** t_srm_evaorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fevaorgid | 评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fevapersonid | 评估负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | forgweight | 权重（%） | numeric | 23 | 10 | √ | 0 | 权重（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_evaorgentry |  | fentryid |
| 2 | idx_srm_evaorgentry_fevaorgid |  | fevaorgid |
| 3 | idx_srm_evaorgentry_fid |  | fid |

---

## 评委分录-子表 t_srm_groupevaplanscorer

- **表名称：** 评委分录-子表
- **表名：** t_srm_groupevaplanscorer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 评委权重(%) | numeric | 19 | 6 | √ | 0 | 评委权重(%) |
| 3 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类 srm_indexclass](../srm_files/srm_indexclass.md) |
| 4 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_gevaplanscorer_idseq |  | fid,fseq |
| 2 | pk_srm_groupevaplanscorer |  | fentryid |

---

## 关联子实体-子表 t_srm_groupevaplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_srm_groupevaplan_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_groupevaplan_lk_fk |  | fid |
| 2 | pk_srm_groupevaplan_lk |  | fpkid |
