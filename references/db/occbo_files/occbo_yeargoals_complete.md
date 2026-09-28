# 渠道年度目标达成-occbo_yeargoals_complete

## 渠道年度目标达成-主表 t_occbo_chlgoals_entry

- **表名称：** 渠道年度目标达成-主表
- **表名：** t_occbo_chlgoals_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 渠道目标 | int8 | 64 |  | √ | 0 | [渠道目标 occbo_channelgoals](../occbo_files/occbo_channelgoals.md) |
| 2 | fgoalsnum12 | fgoalsnum12 | numeric | 23 | 10 | √ | 0 |  |
| 3 | fgoalsnum11 | fgoalsnum11 | numeric | 23 | 10 | √ | 0 |  |
| 4 | fgoalsnum14 | fgoalsnum14 | numeric | 23 | 10 | √ | 0 |  |
| 5 | fgoalsnum13 | fgoalsnum13 | numeric | 23 | 10 | √ | 0 |  |
| 6 | fgoalsnum10 | fgoalsnum10 | numeric | 23 | 10 | √ | 0 |  |
| 7 | factualnum1 | 实际值1 | numeric | 23 | 10 | √ | 0 | 实际值1 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 10 | fchannelid | 经销商 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 11 | fgoalsnum16 | fgoalsnum16 | numeric | 23 | 10 | √ | 0 |  |
| 12 | fgoalsnum15 | fgoalsnum15 | numeric | 23 | 10 | √ | 0 |  |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | fentrytotalnum | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 15 | factualnum9 | factualnum9 | numeric | 23 | 10 | √ | 0 |  |
| 16 | factualnum8 | factualnum8 | numeric | 23 | 10 | √ | 0 |  |
| 17 | fgoalsnum8 | fgoalsnum8 | numeric | 23 | 10 | √ | 0 |  |
| 18 | factualnum7 | factualnum7 | numeric | 23 | 10 | √ | 0 |  |
| 19 | fgoalsnum9 | fgoalsnum9 | numeric | 23 | 10 | √ | 0 |  |
| 20 | factualnum6 | factualnum6 | numeric | 23 | 10 | √ | 0 |  |
| 21 | fgoalsnum6 | fgoalsnum6 | numeric | 23 | 10 | √ | 0 |  |
| 22 | factualnum5 | factualnum5 | numeric | 23 | 10 | √ | 0 |  |
| 23 | fgoalsnum7 | fgoalsnum7 | numeric | 23 | 10 | √ | 0 |  |
| 24 | factualnum4 | factualnum4 | numeric | 23 | 10 | √ | 0 |  |
| 25 | fgoalsnum4 | fgoalsnum4 | numeric | 23 | 10 | √ | 0 |  |
| 26 | factualnum3 | factualnum3 | numeric | 23 | 10 | √ | 0 |  |
| 27 | fgoalsnum5 | fgoalsnum5 | numeric | 23 | 10 | √ | 0 |  |
| 28 | factualnum2 | factualnum2 | numeric | 23 | 10 | √ | 0 |  |
| 29 | fgoalsnum2 | fgoalsnum2 | numeric | 23 | 10 | √ | 0 |  |
| 30 | factualnum15 | factualnum15 | numeric | 23 | 10 | √ | 0 |  |
| 31 | fgoalsnum3 | fgoalsnum3 | numeric | 23 | 10 | √ | 0 |  |
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

---

## 渠道年度目标达成-分表 t_occbo_chlgoals_entry_a

- **表名称：** 渠道年度目标达成-分表
- **表名：** t_occbo_chlgoals_entry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompletionrate6 | fcompletionrate6 | varchar | 50 |  | √ | ' ' |  |
| 3 | fcompletionrate15 | fcompletionrate15 | varchar | 50 |  | √ | ' ' |  |
| 4 | fcompletionrate7 | fcompletionrate7 | varchar | 50 |  | √ | ' ' |  |
| 5 | fcompletionrate16 | fcompletionrate16 | varchar | 50 |  | √ | ' ' |  |
| 6 | fcompletionrate8 | fcompletionrate8 | varchar | 50 |  | √ | ' ' |  |
| 7 | fcompletionrate13 | fcompletionrate13 | varchar | 50 |  | √ | ' ' |  |
| 8 | fcompletionrate9 | fcompletionrate9 | varchar | 50 |  | √ | ' ' |  |
| 9 | fcompletionrate14 | fcompletionrate14 | varchar | 50 |  | √ | ' ' |  |
| 10 | fcompletionrate2 | fcompletionrate2 | varchar | 50 |  | √ | ' ' |  |
| 11 | fcompletionrate11 | fcompletionrate11 | varchar | 50 |  | √ | ' ' |  |
| 12 | fcompletionrate3 | fcompletionrate3 | varchar | 50 |  | √ | ' ' |  |
| 13 | fcompletionrate12 | fcompletionrate12 | varchar | 50 |  | √ | ' ' |  |
| 14 | fcompletionrate4 | fcompletionrate4 | varchar | 50 |  | √ | ' ' |  |
| 15 | fcompletionrate5 | fcompletionrate5 | varchar | 50 |  | √ | ' ' |  |
| 16 | fcompletionrate10 | fcompletionrate10 | varchar | 50 |  | √ | ' ' |  |
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
