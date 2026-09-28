# 检查任务-cal_datacheck_task

## 检查任务-主表 t_cal_datacheck_task

- **表名称：** 检查任务-主表
- **表名：** t_cal_datacheck_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpurpose | 用途 | varchar | 5 |  | √ | ' ' | 用途,枚举: A :日常巡检 B :结账 C :关账 D :出库核算前 E :出库核算后 F :成本计算前 G :成本计算后 |
| 6 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_datacheck_task_pkey |  | fid |
| 2 | idx_cal_chtask_no |  | fnumber |

---

## 检查任务-多语言表 t_cal_datacheck_task_l

- **表名称：** 检查任务-多语言表
- **表名：** t_cal_datacheck_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_chtask_l_fid |  | fid |
| 2 | t_cal_datacheck_task_l_pkey |  | fpkid |

---

## 检查项-子表 t_cal_datacheck_taskentry

- **表名称：** 检查项-子表
- **表名：** t_cal_datacheck_taskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 告警级别 | bpchar | 1 |  | √ | ' ' | 告警级别,枚举: A :警告 B :错误 |
| 3 | fisenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 4 | fischange | 允许修改 | bpchar | 1 |  | √ | '0' | 允许修改 |
| 5 | fispreitem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 cal_datacheck_item](../cal_files/cal_datacheck_item.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_chtaskentry_fid |  | fid |
| 2 | t_cal_datacheck_taskentry_pkey |  | fentryid |
