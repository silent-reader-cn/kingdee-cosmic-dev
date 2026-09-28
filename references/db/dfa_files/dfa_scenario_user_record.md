# 场景-用户历史-dfa_scenario_user_record

## 场景-用户历史-主表 t_dfa_scenario_user_recor

- **表名称：** 场景-用户历史-主表
- **表名：** t_dfa_scenario_user_recor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fupdate_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | finput_info | finput_info | varchar | 255 |  | √ | ' ' |  |
| 5 | freport_url | 报告链接 | varchar | 200 |  | √ | ' ' | 报告链接 |
| 6 | fuserid | 用户ID | varchar | 50 |  | √ | ' ' | 用户ID |
| 7 | freport_type | 报告类型 | varchar | 50 |  | √ | ' ' | 报告类型 |
| 8 | fio_contextid | IO上下文ID | varchar | 50 |  | √ | ' ' | IO上下文ID |
| 9 | fchatsessionid | 会话ID | int8 | 64 |  | √ | 0 | 会话ID |
| 10 | fscenario_type | 场景类型 | varchar | 50 |  | √ | ' ' | 场景类型,枚举: fin_report_analysis :财报分析 fin_report_pk :财报对比 metric_pk :指标对比 |
| 11 | fio_status | IO状态 | varchar | 50 |  | √ | ' ' | IO状态,枚举: process :处理中 completed :已完成 fail :失败 stop :已停止 |
| 12 | fscenario_condition | 场景条件json | varchar | 255 |  | √ | ' ' | 场景条件json |
| 13 | freport_title | 报告标题 | varchar | 255 |  | √ | ' ' | 报告标题 |
| 14 | fdelete | 是否删除 | bpchar | 1 |  | √ | '0' | 是否删除 |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fscenario_condition_tag | 场景条件json_详情 | text | 0 |  |  | null | 场景条件json_详情 |
| 17 | finput_info_tag | finput_info_tag | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_scenario_user_recor |  | fid |
| 2 | idx_dfa_scenario_user_recor |  | fscenario_type |
