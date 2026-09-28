# 扫描日志-rsa_exelog

## 扫描日志-主表 t_rsa_exelog

- **表名称：** 扫描日志-主表
- **表名：** t_rsa_exelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffailmessage_tag | 失败信息_详情 | text | 0 |  |  | null | 失败信息_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 分析期间 pa_analysisperiod |
| 5 | ftaskkey | 任务编号 | varchar | 30 |  | √ | ' ' | 任务编号 |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | friskitemid | 风险检查项 | int8 | 64 |  | √ | 0 | [风险检查项 rsa_riskitem](../rsa_files/rsa_riskitem.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fresult | 执行结果 | bpchar | 1 |  | √ | ' ' | 执行结果,枚举: 1 :执行中 2 :失败 3 :成功 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | ftimetype | 时间类型 | varchar | 50 |  | √ | ' ' | 时间类型,枚举: pa_analysisperiod :分析期间 bd_period :会计期间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ffailmessage | 失败信息 | varchar | 100 |  | √ | ' ' | 失败信息 |
| 16 | feventcount | 风险事件 | int4 | 32 |  | √ | 0 | 风险事件 |
| 17 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 18 | fbillno | 检查批次号 | varchar | 30 |  | √ | ' ' | 检查批次号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rsa_exelog_search |  | fbillno |
| 2 | idx_rsa_exelog_taskkey |  | ftaskkey |
| 3 | pk_t_rsa_exelog |  | fid |

---

## 单据体-子表 t_rsa_exelogentry

- **表名称：** 单据体-子表
- **表名：** t_rsa_exelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventid | 风险事件id | varchar | 30 |  | √ | ' ' | 风险事件id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rsa_exelogentry |  | fentryid |
| 2 | idx_rsa_exelogentry |  | fid |
