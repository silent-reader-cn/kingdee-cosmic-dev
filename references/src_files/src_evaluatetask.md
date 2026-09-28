# 考评记录-src_evaluatetask

## 考评记录-主表 t_src_evaluatetask

- **表名称：** 考评记录-主表
- **表名：** t_src_evaluatetask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 考评设置分录ID | int8 | 64 |  | √ | 0 | 考评设置分录ID |
| 3 | fgradeschemeid | 分级方案 | int8 | 64 |  | √ | 0 | 考评分级方案 src_expertgrade |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbasetype | 基本类型 | bpchar | 1 |  | √ | '1' | 基本类型,枚举: 8 :专家考评类 |
| 6 | fbizstatus | 评分状态 | bpchar | 1 |  | √ | ' ' | 评分状态,枚举: B :待评分 C :部分评分 D :已评分 E :已作废 |
| 7 | fschemeid | 评分方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 8 | fbilldate | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 9 | fsuppliercode | 专家代码 | varchar | 50 |  | √ | ' ' | 专家代码 |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fisaptitude | 是否资质审查 | bpchar | 1 |  | √ | '0' | 是否资质审查 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :线上评分 2 :线下评分 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 16 | fbillno | 记录编号 | varchar | 30 |  | √ | ' ' | 记录编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fisaptitude2 | 是否资质后审 | bpchar | 1 |  | √ | '0' | 是否资质后审 |
| 19 | fprojectid | 考评单号 | int8 | 64 |  | √ | 0 | 专家考评F7 src_evaluatef7 |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fgradeid | 考评等级 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fsumscore | 评估得分 | numeric | 23 | 10 | √ | 0 | 评估得分 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fexperttype | 专家类别 | varchar | 30 |  | √ | ' ' | 专家类别,枚举: src_expert :评标专家 |
| 27 | fsupplierid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 28 | ffinishdate | 评分完成时间 | timestamp | 0 |  |  | null | 评分完成时间 |
| 29 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 30 | fminvalue | 合格最低分 | numeric | 23 | 10 | √ | 0 | 合格最低分 |
| 31 | fbillindexscore | 指标占比(%) | numeric | 23 | 10 | √ | 0 | 指标占比(%) |
| 32 | finputscore | 手工录入评分 | numeric | 23 | 10 | √ | 0 | 手工录入评分 |
| 33 | fbizstatus2 | 评分状态(历史) | bpchar | 1 |  | √ | ' ' | 评分状态(历史),枚举: A :未启动 B :待评分 C :部分评分 D :已评分 E :已废标 |
| 34 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluatetask_supid |  | fsupplierid |
| 2 | pk_src_evaluatetask |  | fid |
| 3 | idx_src_evaluatetask_projectid |  | fprojectid |
| 4 | idx_src_evaluatetask_fbillno |  | fbillno |

---

## 指标分录-子表 t_src_evaluateentry

- **表名称：** 指标分录-子表
- **表名：** t_src_evaluateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 3 | ffinalscore | 最终得分 | numeric | 19 | 6 | √ | 0 | 最终得分 |
| 4 | findexdimension | 评分维度 | varchar | 255 |  | √ | ' ' | 评分维度 |
| 5 | fmanscore | 评委评分 | numeric | 19 | 6 | √ | 0 | 评委评分 |
| 6 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | findexid | 评分指标 | int8 | 64 |  | √ | 0 | 评分指标F7 src_indexf7 |
| 9 | findexlibid | findexlibid | int8 | 64 |  | √ | 0 |  |
| 10 | fisveto | 一票否决 | bpchar | 1 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 11 | fisthreshold | 是否门槛值 | bpchar | 1 |  | √ | '0' | 是否门槛值 |
| 12 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 13 | fsysscore | 系统评分 | numeric | 19 | 6 | √ | 0 | 系统评分 |
| 14 | fscored | 指标已评分 | bpchar | 1 |  | √ | ' ' | 指标已评分 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_evaluateentry |  | fentryid |
| 2 | idx_src_evaluateentry_fid |  | fid |
| 3 | idx_src_evaluateentry_indexid |  | findexid |

---

## 评委分录-子表 t_src_evaluatedetail

- **表名称：** 评委分录-子表
- **表名：** t_src_evaluatedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fveto | fveto | varchar | 30 |  | √ | ' ' |  |
| 4 | fisoverthreshold | fisoverthreshold | bpchar | 1 |  | √ | '0' |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | findexid | 评分指标ID | int8 | 64 |  | √ | 0 | 评分指标ID |
| 9 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 10 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 11 | fisveto | 一票否决 | varchar | 30 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 12 | finvalid | 评分异常否 | bpchar | 1 |  | √ | '0' | 评分异常否,枚举: 0 :正常 1 :偏差过大 2 :去掉最低分 3 :去掉最高分 |
| 13 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 14 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 15 | fisautoscore | 系统自动评分 | bpchar | 1 |  | √ | '0' | 系统自动评分 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | findexscore | findexscore | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 19 | faverage | faverage | numeric | 23 | 10 | √ | 0 |  |
| 20 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 21 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 22 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 23 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 26 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 27 | fscorerscore | 评委评分 | numeric | 23 | 10 | √ | 0 | 评委评分 |
| 28 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evadetail_parentid |  | fparentid |
| 2 | idx_src_evaetail_scorerid |  | fscorerid |
| 3 | idx_src_evadetail_pid |  | fprojectid |
| 4 | idx_src_evaetail_eid |  | fentryid |
| 5 | pk_src_evaluatedetail |  | fdetailid |
| 6 | idx_src_evaetail_agentid |  | fagentid |
