# API调用统计快照-open_rest_api_stat_snap

## API调用统计快照-主表 t_open_rest_api_stat_snap

- **表名称：** API调用统计快照-主表
- **表名：** t_open_rest_api_stat_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserver_error_count | 5xx失败次数 | int4 | 32 |  | √ | 0 | 5xx失败次数 |
| 3 | ftotal_cost | 总耗时（ms） | int8 | 64 |  | √ | 0 | 总耗时（ms） |
| 4 | fclient_error_count | 4xx失败次数 | int4 | 32 |  | √ | 0 | 4xx失败次数 |
| 5 | finstance_id | 实例ID | varchar | 100 |  | √ | ' ' | 实例ID |
| 6 | fsuccess_count | 成功次数 | int4 | 32 |  | √ | 0 | 成功次数 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftotal_count | 调用总次数 | int4 | 32 |  | √ | 0 | 调用总次数 |
| 9 | frest_api | RESTful API | int8 | 64 |  | √ | 0 | RESTful API |
| 10 | fappid | 第三方应用 | int8 | 64 |  | √ | 0 | 第三方应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_stat_snap_api |  | frest_api |
| 2 | idx_open_stat_snap_appid |  | fappid |
| 3 | idx_open_stat_snap_t |  | fcreatetime |
| 4 | pk_t_open_rest_api_stat_snap |  | fid |
