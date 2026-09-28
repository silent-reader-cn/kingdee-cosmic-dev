# 评估计划-srm_evaplan

## 评估物料-子表 t_pur_evaplanscorersub

- **表名称：** 评估物料-子表
- **表名：** t_pur_evaplanscorersub

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
| 1 | pk_pur_evaplanscorersub |  | fdetailid |
| 2 | index_pur_evasub_id |  | fentryid |

---

## 关联子实体-子表 t_pur_evaplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_evaplan_lk

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
| 1 | pk_pur_evaplan_lk |  | fpkid |
| 2 | idx_pur_evaplan_lk_fk |  | fid |

---

## 评委分录-子表 t_pur_evaplanscorer

- **表名称：** 评委分录-子表
- **表名：** t_pur_evaplanscorer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 评委权重(%) | numeric | 19 | 6 | √ | 0.000000 | 评委权重(%) |
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
| 1 | t_pur_evaplanscorer_pkey |  | fentryid |
| 2 | idx_pur_evaplanscorer_fid |  | fid,fseq |

---

## 评估计划-反写记录表 t_pur_evaplan_wb

- **表名称：** 评估计划-反写记录表
- **表名：** t_pur_evaplan_wb

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
| 1 | pk_pur_evaplan_wb |  | fentryid |
| 2 | idx_pur_evaplan_wb_fk |  | fid |

---

## 评估计划-关联追踪表 t_pur_evaplan_tc

- **表名称：** 评估计划-关联追踪表
- **表名：** t_pur_evaplan_tc

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
| 1 | pk_pur_evaplan_tc |  | fid |
| 2 | idx_pur_evaplan_tc_tid |  | ftid |
| 3 | idx_pur_evaplan_tc_tbill |  | ftbillid |

---

## 指标分录-子表 t_pur_evaplanindex

- **表名称：** 指标分录-子表
- **表名：** t_pur_evaplanindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0.000000 | 指标权重% |
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
| 1 | idx_pur_evaplanindex_idseq |  | fid,fseq |
| 2 | t_pur_evaplanindex_pkey |  | fentryid |
| 3 | idx_pur_evaplanindex_index |  | findexid |

---

## 评估计划-主表 t_pur_evaplan

- **表名称：** 评估计划-主表
- **表名：** t_pur_evaplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fistypescorer | 按一级指标类型设置评委 | bpchar | 1 |  | √ | ' ' | 按一级指标类型设置评委 |
| 3 | fevamethod | 评估方式 | bpchar | 1 |  | √ | 'A' | 评估方式,枚举: A :按供应商维度评估 B :按物料维度评估 C :按单据评估 |
| 4 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fschemeid | 评估方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |
| 6 | fbizstatus | 计划状态 | bpchar | 1 |  | √ | ' ' | 计划状态,枚举: A :未启动 B :待下达 C :待评分 D :已评分 E :已初审 F :已核准 Z :已终止 |
| 7 | fbilldate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 8 | fbiztype | 评估类型 | bpchar | 1 |  | √ | ' ' | 评估类型,枚举: 1 :资质审查 2 :现场考察 3 :样品确认 4 :物料试用 5 :绩效评估 6 :招标资审 |
| 9 | fdatetimeto | 分级有效日期至 | timestamp | 0 |  |  | null | 分级有效日期至 |
| 10 | fcategoryid | 评估品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 11 | fdatefrom | 评估期间从 | timestamp | 0 |  |  | null | 评估期间从 |
| 12 | fgroupevaplannoid | 集团评估计划单号 | int8 | 64 |  | √ | 0 | [集团评估计划单号 srm_groupevaplanno](../srm_files/srm_groupevaplanno.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 15 | fname | 计划名称 | varchar | 100 |  | √ | ' ' | 计划名称 |
| 16 | fdateto | 评估期间至 | timestamp | 0 |  |  | null | 评估期间至 |
| 17 | fgradeid | 分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 19 | fevatypeid | 评估类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 22 | ffinishdate | 预计完成日期 | timestamp | 0 |  |  | null | 预计完成日期 |
| 23 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 25 | fdatetimefrom | 分级有效日期从 | timestamp | 0 |  |  | null | 分级有效日期从 |
| 26 | fperiod | 评估周期 | bpchar | 1 |  | √ | ' ' | 评估周期,枚举: 1 :年度 2 :半年 3 :季度 4 :月度 5 :按需 |
| 27 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_evaplan_fbillno |  | fbillno |
| 2 | idx_pur_evaplan_fbilldate |  | fbilldate |
| 3 | t_pur_evaplan_pkey |  | fid |

---

## 供应商分录-子表 t_pur_evaplanentry

- **表名称：** 供应商分录-子表
- **表名：** t_pur_evaplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizbilltypeid | 业务单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fbizbillno | 业务单据号 | varchar | 80 |  | √ | ' ' | 业务单据号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_evaplansup_fid |  | fid |
| 2 | idx_pur_evaplansup_fsupplierid |  | fsupplierid |
| 3 | t_pur_evaplanentry_pkey |  | fentryid |

---

## 评委明细-子表 t_pur_evaplandetail

- **表名称：** 评委明细-子表
- **表名：** t_pur_evaplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fweight | 评委权重% | numeric | 19 | 6 | √ | 0.000000 | 评委权重% |
| 2 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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

---

## 评估计划-分表 t_pur_evaplan_a

- **表名称：** 评估计划-分表
- **表名：** t_pur_evaplan_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 6 | fterminatedate | 终止时间 | timestamp | 0 |  |  | null | 终止时间 |
| 7 | fpushnotice | 是否下推公告 | bpchar | 1 |  | √ | '0' | 是否下推公告,枚举: 0 :否 1 :是 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | ftermination | 终止意见 | varchar | 255 |  | √ | ' ' | 终止意见 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fterminaterid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpushscore | 是否下达评估任务 | bpchar | 1 |  | √ | '0' | 是否下达评估任务,枚举: 0 :否 1 :是 |
| 17 | fsrcbilltype | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_evaplan_a_pkey |  | fid |
| 2 | idx_pur_evaplan_a_ftime |  | fcreatetime |

---

## 评估计划-多语言表 t_pur_evaplan_l

- **表名称：** 评估计划-多语言表
- **表名：** t_pur_evaplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fname | 计划名称 | varchar | 100 |  | √ | ' ' | 计划名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_evaplan_l_pkey |  | fpkid |
| 2 | idx_pur_evaplan_l_fid |  | fid,flocaleid |
