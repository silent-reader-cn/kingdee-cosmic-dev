# 评估报告-srm_scorerpt

## 评估报告-关联追踪表 t_pur_score_tc

- **表名称：** 评估报告-关联追踪表
- **表名：** t_pur_score_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_score_tc_tbill |  | ftbillid |
| 2 | t_pur_score_tc_pkey |  | fid |
| 3 | idx_pur_score_tc_tid |  | ftid |

---

## 评估报告-反写记录表 t_pur_score_wb

- **表名称：** 评估报告-反写记录表
- **表名：** t_pur_score_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_score_wb_pkey |  | fentryid |

---

## 评估报告-主表 t_pur_score

- **表名称：** 评估报告-主表
- **表名：** t_pur_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 评估物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fschemeid | 评估方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |
| 5 | fbizstatus | 评估状态 | bpchar | 1 |  | √ | ' ' | 评估状态,枚举: D :已评分 E :初审通过 F :初审不通过 G :核准通过 H :核准不通过 Z :已终止 |
| 6 | fbilldate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 7 | fbizbillno | 业务单据号 | varchar | 80 |  | √ | ' ' | 业务单据号 |
| 8 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :资质审查 2 :现场考察 3 :样品试用 4 :资格认证 5 :绩效评估 |
| 9 | fdatetimeto | 分级有效日期至 | timestamp | 0 |  |  | null | 分级有效日期至 |
| 10 | fplandate | 预计完成日期 | timestamp | 0 |  |  | null | 预计完成日期 |
| 11 | ftaskbillno | 计划编号 | varchar | 80 |  | √ | ' ' | 计划编号 |
| 12 | fdatefrom | 评估期间从 | timestamp | 0 |  |  | null | 评估期间从 |
| 13 | fauditgradeid | 核准等级 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 14 | fcategoryid | 评估品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 15 | fsupgradeid | 初审等级 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 18 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 19 | fdateto | 评估期间至 | timestamp | 0 |  |  | null | 评估期间至 |
| 20 | ftrialresult | 初审结果 | bpchar | 1 |  | √ | ' ' | 初审结果,枚举: A :待初审 B :同意 C :驳回 |
| 21 | fgradeid | 分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 23 | fauditresult | 核准结果 | bpchar | 1 |  | √ | ' ' | 核准结果,枚举: A :待核准 B :同意 C :驳回 |
| 24 | ftaskbillid | 计划单ID | int8 | 64 |  | √ | 0 | 计划单ID |
| 25 | fevatypeid | 评估类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 26 | fcalgradeid | 评估等级 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 27 | fsumscore | 评估得分 | numeric | 19 | 6 | √ | 0.000000 | 评估得分 |
| 28 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | fsupplierid | 评估对象 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | ffinishdate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 32 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 33 | fcfmstatus | 初审反馈结果 | bpchar | 1 |  | √ | ' ' | 初审反馈结果,枚举: A :未反馈 B :已同意 C :已申诉 Z :已终止 |
| 34 | fdatetimefrom | 分级有效日期从 | timestamp | 0 |  |  | null | 分级有效日期从 |
| 35 | fbizbilltypeid | 业务单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 36 | fperiod | 评估周期 | bpchar | 1 |  | √ | ' ' | 评估周期,枚举: 1 :年度 2 :半年 3 :季度 4 :月度 5 :按需 |
| 37 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_score_fbilldate |  | fbilldate |
| 2 | idx_pur_score_taskno |  | ftaskbillno |
| 3 | idx_pur_score_fbillno |  | fbillno |
| 4 | t_pur_score_pkey |  | fid |

---

## 评估报告-多语言表 t_pur_score_l

- **表名称：** 评估报告-多语言表
- **表名：** t_pur_score_l

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
| 1 | t_pur_score_l_pkey |  | fpkid |
| 2 | idx_pur_score_l_fid_flocaleid |  | fid,flocaleid |

---

## 评估报告-分表 t_pur_score_a

- **表名称：** 评估报告-分表
- **表名：** t_pur_score_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovedate | 核准时间 | timestamp | 0 |  |  | null | 核准时间 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fapprover | 核准人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fterminatedate | fterminatedate | timestamp | 0 |  |  | null |  |
| 7 | fsuggestion | 初审意见 | varchar | 510 |  | √ | ' ' | 初审意见 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fcfmdate | 反馈时间 | timestamp | 0 |  |  | null | 反馈时间 |
| 10 | fauditopinion | 核准意见 | varchar | 510 |  | √ | ' ' | 核准意见 |
| 11 | freviewdate | 初审时间 | timestamp | 0 |  |  | null | 初审时间 |
| 12 | fcfmid | 反馈人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 15 | ffeedback | 反馈意见 | varchar | 510 |  | √ | ' ' | 反馈意见 |
| 16 | ftermination | ftermination | varchar | 510 |  | √ | ' ' |  |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fterminaterid | fterminaterid | int8 | 64 |  | √ | 0 |  |
| 19 | freviewer | 初审人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_score_a_pkey |  | fid |
| 2 | idx_pur_score_a_fcreatetime |  | fcreatetime |

---

## 关联子实体-子表 t_pur_score_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_score_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_score_lk_pkey |  | fpkid |
