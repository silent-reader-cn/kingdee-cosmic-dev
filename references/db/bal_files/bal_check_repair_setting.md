# 余额巡检重算条件-bal_check_repair_setting

## 规则信息-子表 t_bal_check_repair_st_e

- **表名称：** 规则信息-子表
- **表名：** t_bal_check_repair_st_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' |  |
| 2 | frule | 余额规则编码 | varchar | 36 |  | √ | ' ' | [余额更新规则列表 bal_balanceupdaterule](../bal_files/bal_balanceupdaterule.md) |
| 3 | fbillfs_tag | 重算条件_详情 | text | 0 |  |  | null | 重算条件_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillfs | 重算条件 | varchar | 100 |  | √ | ' ' | 重算条件 |
| 6 | fhasfilter | 条件设置 | bpchar | 1 |  | √ | ' ' | 条件设置,枚举: A :自定义 B :无条件 C :默认单据状态为已审核 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | '0' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_crste_fid |  | fid |
| 2 | pk_bal_check_repair_st_e |  | fentryid |
| 3 | idx_bal_crste_rule |  | frule |

---

## 余额巡检重算条件-主表 t_bal_check_repair_st

- **表名称：** 余额巡检重算条件-主表
- **表名：** t_bal_check_repair_st

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fno | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 4 | fbal | 余额表 | varchar | 36 |  | √ | ' ' | [余额表 bal_balanceinfo](../bal_files/bal_balanceinfo.md) |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_check_repair_st |  | fid |
| 2 | idx_bal_crst_bal |  | fbal |
