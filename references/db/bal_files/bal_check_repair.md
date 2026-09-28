# 余额巡检重算-bal_check_repair

## 余额巡检重算-主表 t_bal_check_repair

- **表名称：** 余额巡检重算-主表
- **表名：** t_bal_check_repair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | ferrorinfo | 异常信息 | varchar | 100 |  | √ | ' ' | 异常信息 |
| 3 | fupdaterule | 余额规则 | varchar | 36 |  | √ | ' ' | [余额更新规则列表 bal_balanceupdaterule](../bal_files/bal_balanceupdaterule.md) |
| 4 | ftraceid | Traceid | varchar | 30 |  | √ | ' ' | Traceid |
| 5 | ftasktype | 任务类型 | bpchar | 1 |  | √ | ' ' | 任务类型,枚举: B :检查单据生成快照 C :检查快照合计余额 D :检查单据删除 J :检查规则禁用 E :清除已回滚的快照 A :检查KEYCOL F :直接修复KEYCOL G :直接修复单据生成快照 H :直接修复快照合计余额 I :直接修复单据删除 |
| 6 | fbill | 单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | foprange | 操作范围 | bpchar | 1 |  | √ | ' ' | 操作范围,枚举: A :增量操作 B :全量操作 C :按单据条件操作 D :按余额条件操作 |
| 8 | fbal | 余额表实体 | varchar | 36 |  | √ | ' ' | [余额表 bal_balanceinfo](../bal_files/bal_balanceinfo.md) |
| 9 | fopresult | 操作结果 | bpchar | 1 |  | √ | ' ' | 操作结果,枚举: A :待发布 B :发布成功 C :发布失败 D :手工终止 |
| 10 | fbillfsinfo | 单据条件信息 | varchar | 100 |  | √ | ' ' | 单据条件信息 |
| 11 | freason | 操作原因 | varchar | 255 |  | √ | ' ' | 操作原因 |
| 12 | fbalfsinfo_tag | 余额条件信息_详情 | text | 0 |  |  | null | 余额条件信息_详情 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | ftaskno | 任务编号 | varchar | 50 |  | √ | ' ' | 任务编号 |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | '0' | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillfsinfo_tag | 单据条件信息_详情 | text | 0 |  |  | null | 单据条件信息_详情 |
| 17 | fbalfsinfo | 余额条件信息 | varchar | 100 |  | √ | ' ' | 余额条件信息 |
| 18 | ferrorinfo_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_check_repair |  | fid |
| 2 | idx_bal_cr_ct |  | fcreatedate |
| 3 | idx_bal_cr_no |  | ftaskno |
