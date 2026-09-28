# 报表自动方案执行队列-xkbm_autoscheme_exe_queue

## 报表自动方案执行队列-主表 t_xkbm_autorpt_exe_queue

- **表名称：** 报表自动方案执行队列-主表
- **表名：** t_xkbm_autorpt_exe_queue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fselectdate | 选择日期 | timestamp | 0 |  |  | null | 选择日期 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fautolock | 执行锁 | bpchar | 1 |  | √ | ' ' | 执行锁 |
| 11 | fstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 0 :待执行 1 :执行中 2 :完成 3 :执行异常 |
| 12 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcreatetype | 方案类型 | varchar | 10 |  | √ | '10' | 方案类型,枚举: 10 :预算报表 20 :实际数报表 30 :预算调整表 |
| 14 | fautorptscheme | 自动报表方案 | int8 | 64 |  | √ | 0 | [报表自动创建方案 xkbm_baserptscheme](../xkbm_files/xkbm_baserptscheme.md) |
| 15 | fexecutetype | 执行方式 | varchar | 10 |  | √ | '10' | 执行方式,枚举: 20 :自动 10 :手动 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_queue_status |  | fstatus |
| 2 | idx_xkbm_queue_scheme |  | fautorptscheme |
| 3 | pk_t_xkbm_autorpt_exe_queue |  | fid |
