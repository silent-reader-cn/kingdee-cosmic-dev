# 渠道月度目标达成-occbo_monthgoals_complete

## 渠道月度目标达成-主表 t_occbo_chlgoals_entry

- **表名称：** 渠道月度目标达成-主表
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
| 7 | factualnum1 | 实际值1 | numeric | 23 | 10 | √ | 0 | 实际值1 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 10 | fchannelid | 经销商 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fgoalsnum16 | 目标值16 | numeric | 23 | 10 | √ | 0 | 目标值16 |
| 12 | fgoalsnum15 | 目标值15 | numeric | 23 | 10 | √ | 0 | 目标值15 |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | fentrytotalnum | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 15 | factualnum9 | 实际值9 | numeric | 23 | 10 | √ | 0 | 实际值9 |
| 16 | factualnum8 | 实际值8 | numeric | 23 | 10 | √ | 0 | 实际值8 |
| 17 | fgoalsnum8 | 目标值8 | numeric | 23 | 10 | √ | 0 | 目标值8 |
| 18 | factualnum7 | 实际值7 | numeric | 23 | 10 | √ | 0 | 实际值7 |
| 19 | fgoalsnum9 | 目标值9 | numeric | 23 | 10 | √ | 0 | 目标值9 |
| 20 | factualnum6 | 实际值6 | numeric | 23 | 10 | √ | 0 | 实际值6 |
| 21 | fgoalsnum6 | 目标值6 | numeric | 23 | 10 | √ | 0 | 目标值6 |
| 22 | factualnum5 | 实际值5 | numeric | 23 | 10 | √ | 0 | 实际值5 |
| 23 | fgoalsnum7 | 目标值7 | numeric | 23 | 10 | √ | 0 | 目标值7 |
| 24 | factualnum4 | 实际值4 | numeric | 23 | 10 | √ | 0 | 实际值4 |
| 25 | fgoalsnum4 | 目标值4 | numeric | 23 | 10 | √ | 0 | 目标值4 |
| 26 | factualnum3 | 实际值3 | numeric | 23 | 10 | √ | 0 | 实际值3 |
| 27 | fgoalsnum5 | 目标值5 | numeric | 23 | 10 | √ | 0 | 目标值5 |
| 28 | factualnum2 | 实际值2 | numeric | 23 | 10 | √ | 0 | 实际值2 |
| 29 | fgoalsnum2 | 目标值2 | numeric | 23 | 10 | √ | 0 | 目标值2 |
| 30 | factualnum15 | 实际值15 | numeric | 23 | 10 | √ | 0 | 实际值15 |
| 31 | fgoalsnum3 | 目标值3 | numeric | 23 | 10 | √ | 0 | 目标值3 |
| 32 | factualnum16 | 实际值16 | numeric | 23 | 10 | √ | 0 | 实际值16 |
| 33 | factualnum13 | 实际值13 | numeric | 23 | 10 | √ | 0 | 实际值13 |
| 34 | fgoalsnum1 | 目标值1 | numeric | 23 | 10 | √ | 0 | 目标值1 |
| 35 | factualnum14 | 实际值14 | numeric | 23 | 10 | √ | 0 | 实际值14 |
| 36 | factualnum11 | 实际值11 | numeric | 23 | 10 | √ | 0 | 实际值11 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | factualnum12 | 实际值12 | numeric | 23 | 10 | √ | 0 | 实际值12 |
| 39 | factualnum10 | 实际值10 | numeric | 23 | 10 | √ | 0 | 实际值10 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_entry |  | fchannelid |
| 2 | pk_occbo_chlgoals_entry |  | fentryid |

---

## 渠道月度目标达成-分表 t_occbo_chlgoals_entry_a

- **表名称：** 渠道月度目标达成-分表
- **表名：** t_occbo_chlgoals_entry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompletionrate6 | 完成率6 | varchar | 50 |  | √ | ' ' | 完成率6 |
| 3 | fcompletionrate15 | 完成率15 | varchar | 50 |  | √ | ' ' | 完成率15 |
| 4 | fcompletionrate7 | 完成率7 | varchar | 50 |  | √ | ' ' | 完成率7 |
| 5 | fcompletionrate16 | 完成率16 | varchar | 50 |  | √ | ' ' | 完成率16 |
| 6 | fcompletionrate8 | 完成率8 | varchar | 50 |  | √ | ' ' | 完成率8 |
| 7 | fcompletionrate13 | 完成率13 | varchar | 50 |  | √ | ' ' | 完成率13 |
| 8 | fcompletionrate9 | 完成率9 | varchar | 50 |  | √ | ' ' | 完成率9 |
| 9 | fcompletionrate14 | 完成率14 | varchar | 50 |  | √ | ' ' | 完成率14 |
| 10 | fcompletionrate2 | 完成率2 | varchar | 50 |  | √ | ' ' | 完成率2 |
| 11 | fcompletionrate11 | 完成率11 | varchar | 50 |  | √ | ' ' | 完成率11 |
| 12 | fcompletionrate3 | 完成率3 | varchar | 50 |  | √ | ' ' | 完成率3 |
| 13 | fcompletionrate12 | 完成率12 | varchar | 50 |  | √ | ' ' | 完成率12 |
| 14 | fcompletionrate4 | 完成率4 | varchar | 50 |  | √ | ' ' | 完成率4 |
| 15 | fcompletionrate5 | 完成率5 | varchar | 50 |  | √ | ' ' | 完成率5 |
| 16 | fcompletionrate10 | 完成率10 | varchar | 50 |  | √ | ' ' | 完成率10 |
| 17 | fcompletionrate1 | 完成率1 | varchar | 50 |  | √ | ' ' | 完成率1 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_entry_a |  | fid |
| 2 | pk_occbo_chlgoals_entry_a |  | fentryid |
