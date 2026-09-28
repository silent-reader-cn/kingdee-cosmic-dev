# 项目任务审批单-mpm_task_process

## 单据体-多语言表 t_mpm_taskprocessentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mpm_taskprocessentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessdescription | 审批描述 | varchar | 255 |  | √ | ' ' | 审批描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskprocessentry_l |  | fpkid |
| 2 | idx_mpm_taskprocessentry_l |  | fentryid,flocaleid |

---

## 单据体-子表 t_mpm_taskprocessentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_taskprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessdescription | 审批描述 | varchar | 255 |  | √ | ' ' | 审批描述 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskprocessentry |  | fentryid |
| 2 | idx_mpm_taskprocessentry_task |  | ftaskid |
| 3 | idx_mpm_taskprocessentry_fid |  | fid |

---

## 项目任务审批单-主表 t_mpm_taskprocess

- **表名称：** 项目任务审批单-主表
- **表名：** t_mpm_taskprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftaskstatusruleid | 任务状态规则 | int8 | 64 |  | √ | 0 | 任务状态规则基础资料 mpm_taskstatusrule |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已作废 E :已终止 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcanceluserid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskprocess |  | fid |
| 2 | idx_mpm_taskprocess_billno |  | fbillno |
