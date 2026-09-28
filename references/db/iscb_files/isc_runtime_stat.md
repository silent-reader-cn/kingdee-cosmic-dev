# 集成云运行时统计信息-isc_runtime_stat

## 集成云运行时统计信息-主表 t_iscb_runtime_stat

- **表名称：** 集成云运行时统计信息-主表
- **表名：** t_iscb_runtime_stat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdcr_failed_count | 数据集成读取失败行数 | int8 | 64 |  | √ | 0 | 数据集成读取失败行数 |
| 3 | fperiod_week | 统计期间（周） | int8 | 64 |  | √ | 0 | 统计期间（周） |
| 4 | fdct_failed_count | 数据集成转换失败行数 | int8 | 64 |  | √ | 0 | 数据集成转换失败行数 |
| 5 | fperiod_year | 统计期间（年） | int8 | 64 |  | √ | 0 | 统计期间（年） |
| 6 | fperiod_day | 统计期间（天） | int8 | 64 |  | √ | 0 | 统计期间（天） |
| 7 | fdcw_failed_count | 数据集成加载失败行数 | int8 | 64 |  | √ | 0 | 数据集成加载失败行数 |
| 8 | fdf_execute_count | 数据流执行总次数 | int8 | 64 |  | √ | 0 | 数据流执行总次数 |
| 9 | fmq_published_bytes | MQ发布流量（字节） | int8 | 64 |  | √ | 0 | MQ发布流量（字节） |
| 10 | fperiod_quarter | 统计期间（季度） | int8 | 64 |  | √ | 0 | 统计期间（季度） |
| 11 | fdcr_total_count | 数据集成读取行数 | int8 | 64 |  | √ | 0 | 数据集成读取行数 |
| 12 | fdct_total_count | 数据集成转换行数 | int8 | 64 |  | √ | 0 | 数据集成转换行数 |
| 13 | fserver | 执行服务器 | varchar | 100 |  | √ | ' ' | 执行服务器 |
| 14 | fdf_stream_count | 数据流数量 | int8 | 64 |  | √ | 0 | 数据流数量 |
| 15 | fdf_execute_failed | 数据流执行失败次数 | int8 | 64 |  | √ | 0 | 数据流执行失败次数 |
| 16 | fdcw_total_count | 数据集成加载行数 | int8 | 64 |  | √ | 0 | 数据集成加载行数 |
| 17 | fdf_fiber_complete | 数据线完成数量 | int8 | 64 |  | √ | 0 | 数据线完成数量 |
| 18 | fdf_fiber_count | 数据线发起数量 | int8 | 64 |  | √ | 0 | 数据线发起数量 |
| 19 | fperiod_month | 统计期间（月） | int8 | 64 |  | √ | 0 | 统计期间（月） |
| 20 | fmq_consumed_count | MQ消费次数 | int8 | 64 |  | √ | 0 | MQ消费次数 |
| 21 | fapi_total_count | API调用总次数 | int8 | 64 |  | √ | 0 | API调用总次数 |
| 22 | fsf_total_count | 服务流程发起次数 | int8 | 64 |  | √ | 0 | 服务流程发起次数 |
| 23 | fcreated_time | 记录时间 | timestamp | 0 |  |  | null | 记录时间 |
| 24 | fmq_consumed_bytes | MQ消费流量（字节） | int8 | 64 |  | √ | 0 | MQ消费流量（字节） |
| 25 | fperiod_hour | 统计期间（小时） | int8 | 64 |  | √ | 0 | 统计期间（小时） |
| 26 | fmq_pubished_count | MQ发布次数 | int8 | 64 |  | √ | 0 | MQ发布次数 |
| 27 | fsf_failed_count | 服务流程失败次数 | int8 | 64 |  | √ | 0 | 服务流程失败次数 |
| 28 | fapi_failed_count | API调用失败次数 | int8 | 64 |  | √ | 0 | API调用失败次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_runtime_stat_c |  | fcreated_time |
| 2 | t_iscb_runtime_stat_pkey |  | fid |
