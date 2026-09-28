# 风险运行清单-tctrc_risk_run_list

## 风险运行清单-主表 t_tctrc_risk_run_list

- **表名称：** 风险运行清单-主表
- **表名：** t_tctrc_risk_run_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanid | 方案ID | int8 | 64 |  | √ | 0 | 方案ID |
| 3 | flastruntime | 最后运行时间 | timestamp | 0 |  |  | null | 最后运行时间 |
| 4 | frisk | 风险 | int8 | 64 |  | √ | 0 | 风险设置 tctrc_risk_definition |
| 5 | frunorg | 运行组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmonth | 定时运行月份 | varchar | 100 |  | √ | ' ' | 定时运行月份 |
| 7 | fday | 定时运行日 | varchar | 100 |  | √ | ' ' | 定时运行日 |
| 8 | fsharingid | 风险分配主键 | int8 | 64 |  | √ | 0 | 风险分配主键 |
| 9 | fruntime | 运行时间 | varchar | 100 |  | √ | ' ' | 运行时间 |
| 10 | fcollect | 收藏 | varchar | 50 |  | √ | ' ' | 收藏 |
| 11 | fassignorg | 分配组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fplannumber | 方案号 | varchar | 100 |  | √ | ' ' | 方案号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_run_sharingid |  | fsharingid |
| 2 | idx_tctrc_risk_run_list |  | frisk,fassignorg,frunorg,fplanid |
| 3 | t_tctrc_risk_run_list_pkey |  | fid |
