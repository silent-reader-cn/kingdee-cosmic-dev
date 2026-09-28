# 风险历史纪录-mpm_airiskhistory

## 单据体-子表 t_mpm_airiskhistorycard

- **表名称：** 单据体-子表
- **表名：** t_mpm_airiskhistorycard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 风险标题 | varchar | 80 |  | √ | ' ' | 风险标题 |
| 3 | flevel | 风险等级 | int4 | 32 |  | √ | 0 | 风险等级 |
| 4 | fprocessorid | 应对人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdetail | 风险详情 | varchar | 255 |  | √ | ' ' | 风险详情 |
| 6 | ftype | 风险类型 | varchar | 10 |  | √ | ' ' | 风险类型,枚举: new :新增风险 change :风险变动 finish :风险完结 |
| 7 | fcreated | 是否创建 | bpchar | 1 |  | √ | '0' | 是否创建 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fisignore | 是否忽略 | bpchar | 1 |  | √ | '0' | 是否忽略 |
| 10 | frisktypeid | 风险类型id | int8 | 64 |  | √ | 0 | 风险类型id |
| 11 | ftaskid | 关联任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_airiskhistorycard |  | fentryid |
| 2 | idx_mpm_airiskhistorycard_fid |  | fid |

---

## 风险历史纪录-主表 t_mpm_airiskhistory

- **表名称：** 风险历史纪录-主表
- **表名：** t_mpm_airiskhistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 3 | fcreatedate | 生成时间 | timestamp | 0 |  |  | null | 生成时间 |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 |
| 5 | frenametitle | 重命名标题 | varchar | 80 |  | √ | ' ' | 重命名标题 |
| 6 | ferrormsg | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 7 | fisfinish | 是否结束 | bpchar | 1 |  | √ | '0' | 是否结束 |
| 8 | fresulttext | 结果统计 | varchar | 255 |  | √ | ' ' | 结果统计 |
| 9 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 10 | fhistorytitle | 标题 | varchar | 80 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_airiskhistory |  | fid |
| 2 | idx_mpm_airiskhistory_upid |  | fuserid,fprojectid |
