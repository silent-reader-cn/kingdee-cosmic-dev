# 方案执行记录-xkcr_smartmerge_log

## 方案执行记录-主表 t_xkcr_smart_merge_log

- **表名称：** 方案执行记录-主表
- **表名：** t_xkcr_smart_merge_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemsetarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | fremark | 异常信息 | varchar | 1000 |  |  | ' ' | 异常信息 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fqueueid | 执行队列id | varchar | 30 |  | √ | '0' | 执行队列id |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fremark_tag | fremark_tag | text | 0 |  |  | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 执行状态 | varchar | 50 |  | √ | '0' | 执行状态,枚举: 0 :未执行 1 :执行中 2 :部分成功 3 :成功 4 :失败 5 :执行完成 |
| 11 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsmartmergeplan | 自动合并方案 | int8 | 64 |  | √ | 0 | [自动合并方案 xkcr_smart_merge_plan](../xkcr_files/xkcr_smart_merge_plan.md) |
| 13 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 14 | fschemeendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fcreatetype | 执行方式 | bpchar | 1 |  | √ | '0' | 执行方式,枚举: 0 :自动 1 :手动 |
| 16 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 17 | fbillno | 执行编号 | varchar | 30 |  | √ | ' ' | 执行编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_smart_merge_log_sch |  | fsmartmergeplan,fbillno |
| 2 | pk_xkcr_smart_merge_log |  | fid |
