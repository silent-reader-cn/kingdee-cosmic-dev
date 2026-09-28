# 集团评估报告单号-srm_groupscorerptno

## 集团评估报告单号-主表 t_srm_groupscorerpt

- **表名称：** 集团评估报告单号-主表
- **表名：** t_srm_groupscorerpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fgroupsumscore | fgroupsumscore | numeric | 23 | 10 | √ | 0 |  |
| 3 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 4 | fgroupevagradeid | fgroupevagradeid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 6 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fterminatecaltype | fterminatecaltype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 11 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 12 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 13 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 14 | favgcal | favgcal | bpchar | 1 |  | √ | ' ' |  |
| 15 | fgroupevaplanno | fgroupevaplanno | varchar | 80 |  | √ | ' ' |  |
| 16 | fplandate | fplandate | timestamp | 0 |  |  | null |  |
| 17 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_score_fbilldate |  | fbilldate |
| 2 | idx_srm_score_fbillno |  | fbillno |
| 3 | pk_srm_groupscorerpt |  | fid |
