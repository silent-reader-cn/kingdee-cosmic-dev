# 质检附件-task_qcattachment

## 质检附件-主表 t_tk_qcattachment

- **表名称：** 质检附件-主表
- **表名：** t_tk_qcattachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpointid | 质检点Id | int8 | 64 |  | √ | 0 | 质检点Id |
| 3 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_qcattachment_pkey |  | fid |
| 2 | idx_som_taskid |  | ftaskid |

---

## 单据体-子表 t_tk_qcattachmententry

- **表名称：** 单据体-子表
- **表名：** t_tk_qcattachmententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户 |
| 5 | ftaskformid | 表单标识 | varchar | 100 |  | √ | ' ' | 表单标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fattachmentid | 附件Id | int8 | 64 |  | √ | 0 | 附件Id |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_qcattachmententry_pkey |  | fentryid |
| 2 | idx_som_attrid |  | fattachmentid |
