# 任务完成确认单据-plm_ipd_taskconfirmlist

## 抄送人-多选基础资料表 t_plm_ipd_taskcomnotifier

- **表名称：** 抄送人-多选基础资料表
- **表名：** t_plm_ipd_taskcomnotifier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_taskcomnotifier_fk |  | fid |
| 2 | pk_plm_ipd_taskcomnotifier |  | fpkid |

---

## 任务完成确认单据-主表 t_plm_ipd_taskconfirm

- **表名称：** 任务完成确认单据-主表
- **表名：** t_plm_ipd_taskconfirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fselfevalue | 自评等级 | varchar | 50 |  | √ | ' ' | 自评等级,枚举: 0 :卓越 1 :优秀 2 :良好 |
| 3 | ftask | 任务 | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 4 | freportuser | 汇报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fapprovaluser | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | feportdate | 汇报日期 | timestamp | 0 |  |  | null | 汇报日期 |
| 7 | fdelayreason | 延期原因 | varchar | 255 |  | √ | ' ' | 延期原因 |
| 8 | fdatatype | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :未确认 1 :同意 2 :驳回 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_taskconfirm |  | fid |
| 2 | idx_plm_ipd_taskconfirm_m0 |  | fapprovaluser |
