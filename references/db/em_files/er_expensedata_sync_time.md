# 费用明细同步时间-er_expensedata_sync_time

## 费用明细同步时间-主表 t_er_expensedata_synctime

- **表名称：** 费用明细同步时间-主表
- **表名：** t_er_expensedata_synctime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :正在同步 B :已同步完成 |
| 3 | flastsynctime | 上次同步时间 | timestamp | 0 |  |  | null | 上次同步时间 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsyncing | 已同步数量 | int8 | 64 |  | √ | 0 | 已同步数量 |
| 6 | ftotal | 数据总量 | int8 | 64 |  | √ | 0 | 数据总量 |
| 7 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: er_tripreimbursebill :差旅报销单 er_publicreimbursebill :对公报销单 er_dailyreimbursebill :费用报销单 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_expensedata_synctime |  | fid |
| 2 | idx_er_datasynctime_fbilltype |  | fbilltype |
