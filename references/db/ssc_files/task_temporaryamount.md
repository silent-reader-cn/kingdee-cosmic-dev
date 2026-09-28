# 核减金额数据表-task_temporaryamount

## 核减金额数据表-主表 t_tk_temporaryamount

- **表名称：** 核减金额数据表-主表
- **表名：** t_tk_temporaryamount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauditperson | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fformnumber | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | frequestperson | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fssccenter | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | floccur | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 9 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 10 | fbillno | 单据号 | varchar | 50 |  | √ | ' ' | 单据号 |
| 11 | fbilltype | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |
| 12 | fcompletetime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 13 | frecordtime | 记录时间 | timestamp | 0 |  |  | null | 记录时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_temporaryamount |  | fbilltype |
| 2 | t_tk_temporaryamount_pkey |  | fid |
| 3 | ssc_tempamot_taskid_idx |  | ftaskid |
| 4 | ssc_tempamot_billid_idx |  | fbillid |

---

## 单据体-子表 t_tk_temporaryamountentry

- **表名称：** 单据体-子表
- **表名：** t_tk_temporaryamountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountcount | 报销总额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销总额 |
| 3 | freductionamount | 核减金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核减金额 |
| 4 | fapprovedcount | 核定总额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定总额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fexpensetype | 费用类型 | int8 | 64 |  | √ | 0 | 费用类型 task_expensetype |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_temporaryamountentry_pkey |  | fentryid |
| 2 | inx_ssc_tmprryamtent_fid |  | fid |
