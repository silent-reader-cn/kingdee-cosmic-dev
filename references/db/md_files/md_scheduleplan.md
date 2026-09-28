# 调度计划-md_scheduleplan

## 调度计划-主表 t_md_scheduleplan

- **表名称：** 调度计划-主表
- **表名：** t_md_scheduleplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fscheduletime | 调度时间 | timestamp | 0 |  |  | null | 调度时间 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | ftradebillid | 所属交易单据 | int8 | 64 |  | √ | 0 | 交易录入F7 tm_trade_f77 |
| 10 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 11 | fitemdataid | fitemdataid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fschedulestatus | 调度状态 | varchar | 30 |  | √ | ' ' | 调度状态,枚举: no_start :未开始 processing :进行中 finish :完成 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fdatatype | fdatatype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_scheduleplan |  | fid |
| 2 | idx_md_schedule_b |  | fdatatype,fitemdataid,ftradebillid,fscheduletime,fschedulestatus |
