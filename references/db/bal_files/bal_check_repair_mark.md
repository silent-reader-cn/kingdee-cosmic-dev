# 余额巡检重算增量标记-bal_check_repair_mark

## 余额巡检重算增量标记-主表 t_bal_check_repair_mark

- **表名称：** 余额巡检重算增量标记-主表
- **表名：** t_bal_check_repair_mark

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftasktype | 任务类型 | bpchar | 1 |  | √ | ' ' | 任务类型,枚举: A :检查 或 直接修复KEYCOL B :检查 或 直接修复单据生成快照 C :检查 或 直接修复快照合计余额 D :检查 或 直接修复单据删除 E :检查 或 直接修复规则禁用 |
| 4 | fpointinfo | 增量信息 | varchar | 80 |  | √ | ' ' | 增量信息 |
| 5 | fpointkey | 增量标识 | varchar | 80 |  | √ | ' ' | 增量标识 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_crmk_key |  | fpointkey |
| 2 | pk_bal_check_repair_mark |  | fid |
| 3 | idx_bal_crmk_mt |  | fmodifydate |
