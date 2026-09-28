# 自动执行日志-sca_schemelog

## 单据体-子表 t_sca_schemelogentry

- **表名称：** 单据体-子表
- **表名：** t_sca_schemelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | fcostcenterid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fopername | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作 |
| 6 | fsourcesys | fsourcesys | int8 | 64 |  | √ | 0 |  |
| 7 | fdetail | 执行详情 | varchar | 1000 |  | √ | ' ' | 执行详情 |
| 8 | fbusinessname | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 9 | fcostaccountid | fcostaccountid | int8 | 64 |  | √ | 0 |  |
| 10 | fsourceentity | fsourceentity | varchar | 30 |  | √ | ' ' |  |
| 11 | ftimecost | 耗时 | varchar | 10 |  | √ | ' ' | 耗时 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsourcebillno | fsourcebillno | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_schemelogentry |  | fid |
| 2 | t_sca_schemelogentry_pkey |  | fentryid |

---

## 自动执行日志-主表 t_sca_schemelog

- **表名称：** 自动执行日志-主表
- **表名：** t_sca_schemelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecuteresult | 执行结果 | bpchar | 1 |  | √ | '1' | 执行结果,枚举: 1 :成功 2 :失败 |
| 3 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | [自动执行方案 sca_autoexecsheme](../aca_files/sca_autoexecsheme.md) |
| 4 | fexecutetime | 执行时长 | varchar | 30 |  | √ | ' ' | 执行时长 |
| 5 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用 |
| 7 | fexecutetype | 执行类型 | varchar | 60 |  | √ | ' ' | 执行类型,枚举: task :调度触发 manual :手工执行 |
| 8 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_schemelog_schemeid |  | fschemeid |
| 2 | t_sca_schemelog_pkey |  | fid |

---

## 子单据体-子表 t_sca_schemelogsubentry

- **表名称：** 子单据体-子表
- **表名：** t_sca_schemelogsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fsuccessqty | 成功单据数量 | int4 | 32 |  | √ | 0 | 成功单据数量 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_schemelogsubentry |  | fdetailid |
| 2 | idx_sca_schemelogsubentry |  | fentryid,forgid |
