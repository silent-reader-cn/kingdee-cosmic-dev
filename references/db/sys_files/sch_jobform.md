# 后台大任务-sch_jobform

## 后台大任务-主表 t_sch_jobform

- **表名称：** 后台大任务-主表
- **表名：** t_sch_jobform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :创建 1 :确认 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftaskid | taskid | varchar | 36 |  | √ | ' ' | taskid |
| 6 | fdata | data | text | 0 |  |  | null | data |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_jobform_fcreatorid |  | fcreatorid |
| 2 | pk_t_sch_jobform |  | fid |
| 3 | idx_sch_jobform_ftaskid |  | ftaskid |
| 4 | idx_sch_jobform_fcreatetime |  | fcreatetime |
