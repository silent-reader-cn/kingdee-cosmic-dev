# 评估报告单号-srm_scorerptbaseno

## 评估报告单号-主表 t_pur_score

- **表名称：** 评估报告单号-主表
- **表名：** t_pur_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fbizbillno | fbizbillno | varchar | 80 |  | √ | ' ' |  |
| 8 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fdatetimeto | fdatetimeto | timestamp | 0 |  |  | null |  |
| 10 | fplandate | fplandate | timestamp | 0 |  |  | null |  |
| 11 | ftaskbillno | ftaskbillno | varchar | 80 |  | √ | ' ' |  |
| 12 | fdatefrom | fdatefrom | timestamp | 0 |  |  | null |  |
| 13 | fauditgradeid | 核准等级 | int8 | 64 |  | √ | 0 | 评估等级 bd_evagrade |
| 14 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 15 | fsupgradeid | fsupgradeid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 18 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 19 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 20 | ftrialresult | ftrialresult | bpchar | 1 |  | √ | ' ' |  |
| 21 | fgradeid | fgradeid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 23 | fauditresult | fauditresult | bpchar | 1 |  | √ | ' ' |  |
| 24 | ftaskbillid | ftaskbillid | int8 | 64 |  | √ | 0 |  |
| 25 | fevatypeid | fevatypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fcalgradeid | 评估等级 | int8 | 64 |  | √ | 0 | 评估等级 bd_evagrade |
| 27 | fsumscore | 评估得分 | numeric | 19 | 6 | √ | 0.000000 | 评估得分 |
| 28 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 29 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 30 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
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
