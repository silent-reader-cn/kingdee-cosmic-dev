# 个人设置-er_tripsettingdata

## 个人设置-主表 t_er_tripsettingdata

- **表名称：** 个人设置-主表
- **表名：** t_er_tripsettingdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremaincyc | 提醒周期 | bpchar | 30 |  | √ | ' ' | 提醒周期,枚举: before0 :当天 before1 :前一天 before2 :前两天 |
| 3 | fispartner | 多出差人设置 | bpchar | 1 |  | √ | '0' | 多出差人设置 |
| 4 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fiscalendar | 日历显示 | bpchar | 1 |  | √ | '0' | 日历显示 |
| 6 | fismultireimburser | 多报销人设置 | bpchar | 1 |  | √ | '0' | 多报销人设置 |
| 7 | fdate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fiscurrency | 多币种设置 | bpchar | 1 |  | √ | '0' | 多币种设置 |
| 9 | fispush | 推送 | bpchar | 1 |  | √ | '0' | 推送 |
| 10 | fremaintime | 提醒时间 | bpchar | 30 |  | √ | ' ' | 提醒时间,枚举: one :上午8:00 two :中午12:00 three :下午6:00 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trsda_fuser |  | fuser |
| 2 | t_er_tripsettingdata_pkey |  | fid |
