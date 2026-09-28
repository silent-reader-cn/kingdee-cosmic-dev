# API调用统计汇总-open_rest_api_stat_sum

## API调用统计汇总-主表 t_open_rest_api_stat_sum

- **表名称：** API调用统计汇总-主表
- **表名：** t_open_rest_api_stat_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 日期 | timestamp | 0 |  |  | null | 日期 |
| 3 | fserver_error_count | 5xx失败次数 | int8 | 64 |  | √ | 0 | 5xx失败次数 |
| 4 | fclient_error_count | 4xx失败次数 | int8 | 64 |  | √ | 0 | 4xx失败次数 |
| 5 | ftotal_cost | 总耗时（ms） | int8 | 64 |  | √ | 0 | 总耗时（ms） |
| 6 | ftype | 统计类型 | varchar | 20 |  | √ | ' ' | 统计类型,枚举: hour_detail :小时明细 day_detail :天明细 hour_sum :小时汇总 day_sum :天汇总 |
| 7 | fsuccess_count | 成功次数 | int8 | 64 |  | √ | 0 | 成功次数 |
| 8 | fthird_app | 第三方应用 | int8 | 64 |  | √ | 0 | [第三方应用 third_app](../open_files/third_app.md) |
| 9 | ftotal_count | 调用总次数 | int8 | 64 |  | √ | 0 | 调用总次数 |
| 10 | frest_api | RESTful API | int8 | 64 |  | √ | 0 | RESTful API（基础模型） open_rest_api |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_api_stat_m |  | ftype,ftime,frest_api,fthird_app |
| 2 | pk_open_rest_api_stat_sum |  | fid |
