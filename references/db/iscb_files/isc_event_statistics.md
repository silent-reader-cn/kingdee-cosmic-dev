# 事件触发统计-isc_event_statistics

## 事件触发统计-主表 t_isc_event_statistics

- **表名称：** 事件触发统计-主表
- **表名：** t_isc_event_statistics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferror | 错误原因 | varchar | 2000 |  |  | ' ' | 错误原因 |
| 3 | ferror_tag | 错误原因_详情 | text | 0 |  |  | ' ' | 错误原因_详情 |
| 4 | fmodify_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdatabase_type | 连接类型 | varchar | 20 |  | √ | ' ' | 连接类型,枚举: eas :EAS系统 self :当前账套 db_proxy :数据库代理 ierp :金蝶云苍穹 |
| 6 | ffail_total | 失败总数 | int4 | 32 |  | √ | 0 | 失败总数 |
| 7 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdblink | 连接配置 | int8 | 64 |  | √ | 0 | 连接配置 |
| 9 | fdate_range | 日期范围 | varchar | 10 |  | √ | ' ' | 日期范围,枚举: 1 :近36小时 7 :近7天 30 :近30天 100 :全部 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_event_statistics_d |  | fdblink |
| 2 | pk_t_isc_event_statistics |  | fid |
