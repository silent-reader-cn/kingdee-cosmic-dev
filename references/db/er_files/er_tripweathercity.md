# 天气贴士城市天气链接-er_tripweathercity

## 天气贴士城市天气链接-主表 t_er_weathercitycode

- **表名称：** 天气贴士城市天气链接-主表
- **表名：** t_er_weathercitycode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftianqi | 天气网 | varchar | 100 |  | √ | ' ' | 天气网 |
| 3 | fnmcid | 中央天气城市编码 | varchar | 30 |  | √ | ' ' | 中央天气城市编码 |
| 4 | fmoji | 墨迹天气 | varchar | 100 |  | √ | ' ' | 墨迹天气 |
| 5 | fcityname | 城市名称 | varchar | 30 |  | √ | ' ' | 城市名称 |
| 6 | fnmcurl | 中央天气城市链接 | varchar | 100 |  | √ | ' ' | 中央天气城市链接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_weathercitycode_pkey |  | fid |
| 2 | idx_er_wecc_fcityname |  | fcityname |
