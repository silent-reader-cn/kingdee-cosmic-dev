# 自动巡检重算-bal_auto_repair

## 自动巡检重算-主表 t_bal_auto_repair

- **表名称：** 自动巡检重算-主表
- **表名：** t_bal_auto_repair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fstatus | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fschedule | 调度计划 | varchar | 36 |  | √ | ' ' | 调度计划 sch_schedule |
| 5 | fbal | 余额表 | varchar | 36 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 7 | fcheckitem | 检查修复项 | varchar | 80 |  | √ | ' ' | 检查修复项,枚举: A :单据生成快照 B :快照合计余额 C :单据删除 D :KEYCOL |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_auto_bal |  | fbal |
| 2 | pk_bal_auto_repair |  | fid |
