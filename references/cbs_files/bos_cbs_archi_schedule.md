# 归档调度计划（旧）-bos_cbs_archi_schedule

## 归档调度计划（旧）-主表 t_cbs_archi_schedule

- **表名称：** 归档调度计划（旧）-主表
- **表名：** t_cbs_archi_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcycleinfo | 周期信息 | text | 0 |  |  | null | 周期信息 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用,枚举: 0 :否 1 :是 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fdescription | 调度说明 | varchar | 512 |  | √ | ' ' | 调度说明 |
| 9 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 11 | fcronexpr | 设置周期 | varchar | 255 |  | √ | ' ' | 设置周期 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_schedule_enable |  | fenable |
| 2 | pk_cbs_archi_schedule |  | fid |
| 3 | idx_cbs_archi_schedule |  | fnumber |

---

## 单据体-子表 t_cbs_archi_scheduleentry

- **表名称：** 单据体-子表
- **表名：** t_cbs_archi_scheduleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfigid | 归档规则 | int8 | 64 |  | √ | 0 | 单据归档规则 bos_cbs_archi_config |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_sch_ety_cid |  | fconfigid |
| 2 | idx_cbs_archi_sch_ety_fk |  | fid |
| 3 | pk_cbs_archi_scheduleentry |  | fentryid |
