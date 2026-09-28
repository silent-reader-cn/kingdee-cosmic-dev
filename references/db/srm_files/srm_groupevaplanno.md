# 集团评估计划单号-srm_groupevaplanno

## 集团评估计划单号-主表 t_srm_groupevaplan

- **表名称：** 集团评估计划单号-主表
- **表名：** t_srm_groupevaplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fistypescorer | fistypescorer | bpchar | 1 |  | √ | ' ' |  |
| 3 | fevamethod | fevamethod | bpchar | 1 |  | √ | 'A' |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fcansumcalculate | fcansumcalculate | bpchar | 1 |  | √ | ' ' |  |
| 6 | fterminatecaltype | fterminatecaltype | bpchar | 1 |  | √ | ' ' |  |
| 7 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 8 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 11 | favgcal | favgcal | bpchar | 1 |  | √ | '1' |  |
| 12 | fdatetimeto | fdatetimeto | timestamp | 0 |  |  | null |  |
| 13 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 14 | fdatefrom | fdatefrom | timestamp | 0 |  |  | null |  |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fcompsumcalculate | fcompsumcalculate | bpchar | 1 |  | √ | ' ' |  |
| 19 | fgroupgradeid | fgroupgradeid | int8 | 64 |  | √ | 0 |  |
| 20 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 21 | fgradeid | fgradeid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 23 | fevatypeid | fevatypeid | int8 | 64 |  | √ | 0 |  |
| 24 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 25 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 26 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 27 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 28 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 29 | ftype | 下发类型 | bpchar | 1 |  | √ | ' ' | 下发类型,枚举: |
| 30 | fdatetimefrom | fdatetimefrom | timestamp | 0 |  |  | null |  |
| 31 | fperiod | fperiod | bpchar | 1 |  | √ | ' ' |  |
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
