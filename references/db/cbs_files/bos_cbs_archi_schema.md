# 归档调度计划-bos_cbs_archi_schema

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

---

## 归档调度计划-主表 t_cbs_archi_schema

- **表名称：** 归档调度计划-主表
- **表名：** t_cbs_archi_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexecplan | 执行计划 | varchar | 512 |  | √ | ' ' | 执行计划 |
| 6 | fscheduleplanid | 调度计划ID | varchar | 50 |  | √ | ' ' | 调度计划ID |
| 7 | fmovingtype | 转储或清除 | bpchar | 1 |  | √ | ' ' | 转储或清除,枚举: 0 :转储 1 :清除 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 15 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 16 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_schema |  | fnumber |
| 2 | pk_t_cbs_archi_schema |  | fid |

---

## 归档调度计划-多语言表 t_cbs_archi_schema_l

- **表名称：** 归档调度计划-多语言表
- **表名：** t_cbs_archi_schema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_schema_l |  | fid,flocaleid |
| 2 | pk_t_cbs_archi_schema_l |  | fpkid |
