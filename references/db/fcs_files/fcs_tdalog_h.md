# 决策分析日志_归档-fcs_tdalog_h

## 决策分析日志_归档-主表 t_fcs_tdalog_h

- **表名称：** 决策分析日志_归档-主表
- **表名：** t_fcs_tdalog_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftraceid | traceid | varchar | 80 |  | √ | ' ' | traceid |
| 4 | fcosttime | 耗时(ms) | int4 | 32 |  | √ | 0 | 耗时(ms) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | freportid | 报表 | varchar | 80 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 8 | fexception_tag | 异常信息_详情 | text | 0 |  |  | ' ' | 异常信息_详情 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fscheduleid | 快照调度 | int8 | 64 |  | √ | 0 | [调度任务 fcs_snapschedule](../fcs_files/fcs_snapschedule.md) |
| 14 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: querydata :报表数据查询 snapschedule :快照调度 |
| 15 | forgviewid | 组织视图 | int8 | 64 |  | √ | 0 | [资金管理组织视图 fbd_companysysviewsch](../fbd_files/fbd_companysysviewsch.md) |
| 16 | fsnapitem | 快照版本 | varchar | 80 |  | √ | ' ' | 快照版本 |
| 17 | fexception | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 18 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_tdalog_h |  | forgviewid,forg |
| 2 | pk_t_fcs_tdalog_h |  | fid |
