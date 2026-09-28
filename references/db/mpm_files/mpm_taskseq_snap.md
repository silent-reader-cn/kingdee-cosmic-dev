# 项目任务顺序关系快照-mpm_taskseq_snap

## 下级-子表 t_mpm_taskseqentry_snap

- **表名称：** 下级-子表
- **表名：** t_mpm_taskseqentry_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fchildtaskid | 任务编码 | int8 | 64 |  | √ | 0 | [项目任务快照F7 mpm_task_snap_f7](../mpm_files/mpm_task_snap_f7.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpmc_taskseqentry_id |  | fid |
| 2 | pk_t_mpm_taskseqentry_snap |  | fentryid |

---

## 项目任务顺序关系快照-主表 t_mpm_taskseq_snap

- **表名称：** 项目任务顺序关系快照-主表
- **表名：** t_mpm_taskseq_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | ftaskid | 项目任务 | int8 | 64 |  | √ | 0 | [项目任务快照F7 mpm_task_snap_f7](../mpm_files/mpm_task_snap_f7.md) |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fplanversionid | 计划版本id | int8 | 64 |  | √ | 0 | 计划版本id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_taskseq_snap |  | fid |
| 2 | idx_mpmc_taskseq_planver |  | fplanversionid |
