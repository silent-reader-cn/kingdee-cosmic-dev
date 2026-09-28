# 年度目标-occbo_yeargoals

## 年度目标-主表 t_occbo_chlgoals_entry

- **表名称：** 年度目标-主表
- **表名：** t_occbo_chlgoals_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 渠道目标 | int8 | 64 |  | √ | 0 | 渠道目标 occbo_channelgoals |
| 2 | fgoalsnum12 | 目标值12 | numeric | 23 | 10 | √ | 0 | 目标值12 |
| 3 | fgoalsnum11 | 目标值11 | numeric | 23 | 10 | √ | 0 | 目标值11 |
| 4 | fgoalsnum14 | 目标值14 | numeric | 23 | 10 | √ | 0 | 目标值14 |
| 5 | fgoalsnum13 | 目标值13 | numeric | 23 | 10 | √ | 0 | 目标值13 |
| 6 | fgoalsnum10 | 目标值10 | numeric | 23 | 10 | √ | 0 | 目标值10 |
| 7 | factualnum1 | factualnum1 | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 10 | fchannelid | 经销商 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fgoalsnum16 | 目标值16 | numeric | 23 | 10 | √ | 0 | 目标值16 |
| 12 | fgoalsnum15 | 目标值15 | numeric | 23 | 10 | √ | 0 | 目标值15 |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | fentrytotalnum | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 15 | factualnum9 | factualnum9 | numeric | 23 | 10 | √ | 0 |  |
| 16 | factualnum8 | factualnum8 | numeric | 23 | 10 | √ | 0 |  |
| 17 | fgoalsnum8 | 目标值8 | numeric | 23 | 10 | √ | 0 | 目标值8 |
| 18 | factualnum7 | factualnum7 | numeric | 23 | 10 | √ | 0 |  |
| 19 | fgoalsnum9 | 目标值9 | numeric | 23 | 10 | √ | 0 | 目标值9 |
| 20 | factualnum6 | factualnum6 | numeric | 23 | 10 | √ | 0 |  |
| 21 | fgoalsnum6 | 目标值6 | numeric | 23 | 10 | √ | 0 | 目标值6 |
| 22 | factualnum5 | factualnum5 | numeric | 23 | 10 | √ | 0 |  |
| 23 | fgoalsnum7 | 目标值7 | numeric | 23 | 10 | √ | 0 | 目标值7 |
| 24 | factualnum4 | factualnum4 | numeric | 23 | 10 | √ | 0 |  |
| 25 | fgoalsnum4 | 目标值4 | numeric | 23 | 10 | √ | 0 | 目标值4 |
| 26 | factualnum3 | factualnum3 | numeric | 23 | 10 | √ | 0 |  |
| 27 | fgoalsnum5 | 目标值5 | numeric | 23 | 10 | √ | 0 | 目标值5 |
| 28 | factualnum2 | factualnum2 | numeric | 23 | 10 | √ | 0 |  |
| 29 | fgoalsnum2 | 目标值2 | numeric | 23 | 10 | √ | 0 | 目标值2 |
| 30 | factualnum15 | factualnum15 | numeric | 23 | 10 | √ | 0 |  |
| 31 | fgoalsnum3 | 目标值3 | numeric | 23 | 10 | √ | 0 | 目标值3 |
| 32 | factualnum16 | factualnum16 | numeric | 23 | 10 | √ | 0 |  |
| 33 | factualnum13 | factualnum13 | numeric | 23 | 10 | √ | 0 |  |
| 34 | fgoalsnum1 | 目标值1 | numeric | 23 | 10 | √ | 0 | 目标值1 |
| 35 | factualnum14 | factualnum14 | numeric | 23 | 10 | √ | 0 |  |
| 36 | factualnum11 | factualnum11 | numeric | 23 | 10 | √ | 0 |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | factualnum12 | factualnum12 | numeric | 23 | 10 | √ | 0 |  |
| 39 | factualnum10 | factualnum10 | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_entry |  | fchannelid |
| 2 | pk_occbo_chlgoals_entry |  | fentryid |
