# 天气贴士天气数据-er_tripweather

## 天气贴士天气数据-主表 t_er_tripweather

- **表名称：** 天气贴士天气数据-主表
- **表名：** t_er_tripweather

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnow | 当前日期 | timestamp | 0 |  |  | null | 当前日期 |
| 3 | fcityname | 城市 | varchar | 30 |  | √ | ' ' | 城市 |
| 4 | frealtem | 实时天气 | varchar | 30 |  | √ | ' ' | 实时天气 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trwe_fcityname |  | fcityname |
| 2 | t_er_tripweather_pkey |  | fid |

---

## 未来七天天气-子表 t_er_futureweather

- **表名称：** 未来七天天气-子表
- **表名：** t_er_futureweather

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 天气类型 | varchar | 30 |  | √ | ' ' | 天气类型 |
| 3 | fmaxtem | 最高温度 | varchar | 30 |  | √ | ' ' | 最高温度 |
| 4 | fmintem | 最低温度 | varchar | 30 |  | √ | ' ' | 最低温度 |
| 5 | fdate | 天气日期 | timestamp | 0 |  |  | null | 天气日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fwind | 风速 | varchar | 30 |  | √ | ' ' | 风速 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_fuwe_fseq |  | fid,fseq |
| 2 | t_er_futureweather_pkey |  | fentryid |
