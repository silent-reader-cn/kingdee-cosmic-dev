# 风险处理列表-tctrc_handle_list

## 风险处理列表-主表 t_tctrc_risk_run_result

- **表名称：** 风险处理列表-主表
- **表名：** t_tctrc_risk_run_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | fjson | varchar | 255 |  | √ | ' ' |  |
| 3 | fresult | 风险结果 | varchar | 100 |  | √ | ' ' | 风险结果 |
| 4 | fhandleid | 最新处理结果id | int8 | 64 |  | √ | 0 | 最新处理结果id |
| 5 | ftransmit | 转交后的处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcollect | 收藏 | varchar | 50 |  | √ | ' ' | 收藏 |
| 7 | fcaltype | 计算周期 | varchar | 30 |  | √ | ' ' | 计算周期,枚举: 1 :月度 2 :季度 3 :年度 |
| 8 | friskdesc | 风险说明 | varchar | 2000 |  | √ | ' ' | 风险说明 |
| 9 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fstatus | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: 0 :待处理 1 :已处理 2 :转交中 |
| 11 | frisklevel | 风险等级(弃用) | varchar | 30 |  | √ | ' ' | 风险等级(弃用),枚举: 1 :高 2 :中 3 :低 |
| 12 | fmodifydate | 处理日期 | timestamp | 0 |  |  | null | 处理日期 |
| 13 | fdatestring | 所属期 | varchar | 100 |  | √ | ' ' | 所属期 |
| 14 | fisemptyfield | 字段是否为空 | bpchar | 1 |  | √ | ' ' | 字段是否为空 |
| 15 | fruntime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |
| 16 | frlevel | 风险等级 | int8 | 64 |  | √ | 0 | 风险等级 tctrc_risk_level |
| 17 | fdealresult | 处理结果 | varchar | 30 |  | √ | ' ' | 处理结果,枚举: 1 :- 2 :正常 3 :风险 |
| 18 | friskscore | 风险得分 | varchar | 50 |  | √ | ' ' | 风险得分 |
| 19 | frisk | 风险 | int8 | 64 |  | √ | 0 | 风险设置 tctrc_risk_definition |
| 20 | fmodifier | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fplannumber | 方案号 | varchar | 100 |  | √ | ' ' | 方案号 |
| 22 | fisdenominatorzero | fisdenominatorzero | bpchar | 1 |  | √ | ' ' |  |
| 23 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | frunorg | 运行组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fjson_tag | fjson_tag | text | 0 |  |  | null |  |
| 26 | fassignorg | 分配组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | flastupdateby | 最近运行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_run_result |  | frisk,fassignorg,frunorg,fdatestring |
| 2 | t_tctrc_risk_run_result_pkey |  | fid |
