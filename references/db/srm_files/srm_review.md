# 评估报告初审-srm_review

## 评估报告初审-主表 t_pur_score

- **表名称：** 评估报告初审-主表
- **表名：** t_pur_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fbizstatus | 评估状态 | bpchar | 1 |  | √ | ' ' | 评估状态,枚举: A :未启动 B :待评分 C :部分评分 D :已评分 E :初审通过 F :初审不通过 G :核准通过 H :核准不通过 Z :已终止 |
| 6 | fbilldate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 7 | fbizbillno | fbizbillno | varchar | 80 |  | √ | ' ' |  |
| 8 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fdatetimeto | fdatetimeto | timestamp | 0 |  |  | null |  |
| 10 | fplandate | fplandate | timestamp | 0 |  |  | null |  |
| 11 | ftaskbillno | 计划编号 | varchar | 80 |  | √ | ' ' | 计划编号 |
| 12 | fdatefrom | fdatefrom | timestamp | 0 |  |  | null |  |
| 13 | fauditgradeid | fauditgradeid | int8 | 64 |  | √ | 0 |  |
| 14 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 15 | fsupgradeid | 初审等级 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 16 | fbillno | 评估单号 | varchar | 80 |  | √ | ' ' | 评估单号 |
| 17 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 18 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 19 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 20 | ftrialresult | 初审结果 | bpchar | 1 |  | √ | ' ' | 初审结果,枚举: A :待初审 B :同意 C :驳回 |
| 21 | fgradeid | fgradeid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 23 | fauditresult | fauditresult | bpchar | 1 |  | √ | ' ' |  |
| 24 | ftaskbillid | 计划单ID | int8 | 64 |  | √ | 0 | 计划单ID |
| 25 | fevatypeid | fevatypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fcalgradeid | 评估等级 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 27 | fsumscore | 评估得分 | numeric | 19 | 6 | √ | 0.000000 | 评估得分 |
| 28 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 29 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 30 | fsupplierid | 评估对象 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 32 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 33 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 34 | fdatetimefrom | fdatetimefrom | timestamp | 0 |  |  | null |  |
| 35 | fbizbilltypeid | fbizbilltypeid | varchar | 80 |  | √ | ' ' |  |
| 36 | fperiod | fperiod | bpchar | 1 |  | √ | ' ' |  |
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

## 评估报告初审-分表 t_pur_score_a

- **表名称：** 评估报告初审-分表
- **表名：** t_pur_score_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fapprover | fapprover | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fterminatedate | fterminatedate | timestamp | 0 |  |  | null |  |
| 7 | fsuggestion | 初审意见 | varchar | 510 |  | √ | ' ' | 初审意见 |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 10 | fauditopinion | fauditopinion | varchar | 510 |  | √ | ' ' |  |
| 11 | freviewdate | 初审时间 | timestamp | 0 |  |  | null | 初审时间 |
| 12 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 15 | ffeedback | ffeedback | varchar | 510 |  | √ | ' ' |  |
| 16 | ftermination | ftermination | varchar | 510 |  | √ | ' ' |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | fterminaterid | fterminaterid | int8 | 64 |  | √ | 0 |  |
| 19 | freviewer | 初审人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_score_a_pkey |  | fid |
| 2 | idx_pur_score_a_fcreatetime |  | fcreatetime |
