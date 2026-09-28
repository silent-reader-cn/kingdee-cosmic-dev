# 检查结果-cal_datacheck_result

## 异常对象单据体-子表 t_cal_check_resultdetail

- **表名称：** 异常对象单据体-子表
- **表名：** t_cal_check_resultdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fobjtypeid | 对象类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 2 | fdetailinfo | 详情 | varchar | 30 |  | √ | ' ' | 详情 |
| 3 | fisrepaired | 是否已修复 | bpchar | 1 |  | √ | ' ' | 是否已修复 |
| 4 | fobjid | 异常对象id | int8 | 64 |  | √ | 0 | 异常对象id |
| 5 | fextralinfo | 其他信息 | varchar | 500 |  | √ | ' ' | 其他信息 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fobjdes | 对象描述 | varchar | 500 |  | √ | ' ' | 对象描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_check_resultdetail_pkey |  | fdetailid |
| 2 | idx_cal_chresultde_entryid |  | fentryid |

---

## 检查结果-主表 t_cal_datacheck_result

- **表名称：** 检查结果-主表
- **表名：** t_cal_datacheck_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostaccountbaseid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 3 | fcheckplantype | 检查计划类型 | varchar | 30 |  | √ | ' ' | 检查计划类型,枚举: cal_datacheck_plan :巡检计划 cal_task :后台任务 |
| 4 | fcalorg | 核算组织 | varchar | 2000 |  | √ | ' ' | 核算组织 |
| 5 | fuserid | 检查用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fpurpose | 用途 | varchar | 5 |  | √ | ' ' | 用途,枚举: A :日常巡检 B :结账 C :关账 D :出库核算 |
| 7 | fowner | 货主 | varchar | 2000 |  | √ | ' ' | 货主 |
| 8 | fcostaccount | 成本主体 | varchar | 2000 |  | √ | ' ' | 成本主体 |
| 9 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :进行中 B :已完成 |
| 10 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 货主 |
| 11 | fcheckplanid | 检查计划 | int8 | 64 |  | √ | 0 | 巡检计划 cal_datacheck_plan |
| 12 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 13 | fchecktaskid | 检查任务 | int8 | 64 |  | √ | 0 | 检查任务 cal_datacheck_task |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_datacheck_result_pkey |  | fid |
| 2 | idx_cal_chresult_checktime |  | fchecktime |

---

## 检查详情-子表 t_cal_check_resultentry

- **表名称：** 检查详情-子表
- **表名：** t_cal_check_resultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrystatus | 检查结果 | bpchar | 1 |  | √ | ' ' | 检查结果,枚举: A :警告 B :失败 C :异常 D :成功 E :部分修复 F :已修复 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fruningstatus | 运行状态 | bpchar | 1 |  | √ | ' ' | 运行状态,枚举: A :未开始 B :运行中 C :已完成 |
| 5 | fdescription | 描述 | varchar | 225 |  | √ | ' ' | 描述 |
| 6 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | 检查项 cal_datacheck_item |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_check_resultentry_pkey |  | fentryid |
| 2 | idx_cal_chresultentry_fid |  | fid |
