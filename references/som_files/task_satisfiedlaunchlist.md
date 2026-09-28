# 满意度问卷投放名单-task_satisfiedlaunchlist

## 满意度问卷投放名单-主表 t_tk_satisfiedlaunchlist

- **表名称：** 满意度问卷投放名单-主表
- **表名：** t_tk_satisfiedlaunchlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 满意度问卷 | int8 | 64 |  | √ | 0 | 满意度设置 task_satisfiedquestion |
| 2 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdeliverurl | 问卷链接 | varchar | 500 |  | √ | ' ' | 问卷链接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_satisfiedqid |  | fid |
| 2 | pk_t_tk_satisfiedlaunchlist |  | fentryid |
