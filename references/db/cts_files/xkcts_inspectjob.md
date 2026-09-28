# 巡检任务-xkcts_inspectjob

## 检查项分录-子表 t_xkinsp_jobentry

- **表名称：** 检查项分录-子表
- **表名：** t_xkinsp_jobentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwarmlevel | 控制级别 | varchar | 50 |  | √ | ' ' | 控制级别,枚举: 200 :告警 300 :错误 |
| 3 | fissystem | 是否预设检查项 | bpchar | 1 |  | √ | '0' | 是否预设检查项 |
| 4 | feffective | 生效状态 | varchar | 1 |  | √ | '0' | 生效状态 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemid | 编码 | int8 | 64 |  | √ | 0 | [巡检检查项 xkcts_inspectitem](../cts_files/xkcts_inspectitem.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkinsp_jobentry_fid |  | fid,fseq |
| 2 | pk_xkinsp_jobentry |  | fentryid |

---

## 巡检任务-主表 t_xkinsp_job

- **表名称：** 巡检任务-主表
- **表名：** t_xkinsp_job

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemtypeid | 巡检分类 | int8 | 64 |  | √ | 0 | [巡检业务分类 xkcts_inspectitemtype](../cts_files/xkcts_inspectitemtype.md) |
| 3 | fname | 任务名称 | varchar | 200 |  | √ | ' ' | 任务名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 7 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ftype | 任务类型 | varchar | 1 |  | √ | ' ' | 任务类型,枚举: 1 :日常巡检 2 :期末巡检 3 :审计巡检 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 14 | fenable | 任务状态 | bpchar | 1 |  | √ | '0' | 任务状态,枚举: 0 :禁用 1 :启用 |
| 15 | fnumber | 任务编码 | varchar | 30 |  | √ | ' ' | 任务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_job |  | fid |
| 2 | idx_xkinsp_job_type |  | fitemtypeid |

---

## 巡检任务-多语言表 t_xkinsp_job_l

- **表名称：** 巡检任务-多语言表
- **表名：** t_xkinsp_job_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 任务名称 | varchar | 200 |  | √ | ' ' | 任务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkinsp_job_l |  | fid,flocaleid |
| 2 | pk_xkinsp_job_l |  | fpkid |
