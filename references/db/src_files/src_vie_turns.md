# 竞价轮次F7-src_vie_turns

## 竞价轮次F7-主表 t_src_vie_turns

- **表名称：** 竞价轮次F7-主表
- **表名：** t_src_vie_turns

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: A :报名中 B :准备竞价 C :竞价中 D :评标中 E :已定标 F :已执行 G :已废弃 H :已暂停 |
| 3 | fseq | 轮次序号 | int4 | 32 |  | √ | 0 | 轮次序号 |
| 4 | fbidtimes | 竞价时长(分钟) | int4 | 32 |  | √ | 0 | 竞价时长(分钟) |
| 5 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 6 | freducepct | freducepct | numeric | 23 | 10 | √ | 0 |  |
| 7 | fbidtime | fbidtime | timestamp | 0 |  |  | null |  |
| 8 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) |
| 9 | fopen4 | fopen4 | bpchar | 1 |  | √ | '0' |  |
| 10 | flasttime | flasttime | int4 | 32 |  | √ | 0 |  |
| 11 | fopen2 | fopen2 | bpchar | 1 |  | √ | '0' |  |
| 12 | fsubmittype | fsubmittype | bpchar | 1 |  | √ | ' ' |  |
| 13 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fautoconfirm | fautoconfirm | bpchar | 1 |  | √ | '0' |  |
| 15 | fopen1 | fopen1 | bpchar | 1 |  | √ | '0' |  |
| 16 | fvie_purlist | fvie_purlist | bpchar | 1 |  | √ | ' ' |  |
| 17 | fopendate | 竞价开始时间 | timestamp | 0 |  |  | null | 竞价开始时间 |
| 18 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 19 | ftendency | ftendency | bpchar | 1 |  | √ | ' ' |  |
| 20 | fwinerqty | fwinerqty | int4 | 32 |  | √ | 0 |  |
| 21 | faddtimenum | faddtimenum | int4 | 32 |  | √ | 0 |  |
| 22 | freducetype | freducetype | bpchar | 1 |  | √ | ' ' |  |
| 23 | fdelaytime | fdelaytime | int4 | 32 |  | √ | 0 |  |
| 24 | fbidnumber | fbidnumber | int4 | 32 |  | √ | 0 |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_vie_turns_fid |  | fid |
| 2 | idx_src_vie_turns_turn |  | fturns |
| 3 | idx_src_vie_turns_vietrurn |  | fvieturns |
| 4 | pk_src_vie_turns |  | fentryid |
