# 自动结算日志-sco_autocalclog

## 自动结算日志-主表 t_sco_autocalclog

- **表名称：** 自动结算日志-主表
- **表名：** t_sco_autocalclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcalcreportid | 计算报告id | int8 | 64 |  | √ | 0 | 计算报告id |
| 6 | foperdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | forderno | 工单编号 | varchar | 255 |  | √ | ' ' | 工单编号 |
| 8 | forderentryid | 工单分录id | int8 | 64 |  | √ | 0 | 工单分录id |
| 9 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 10 | ftrytimes | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 11 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 12 | fstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 00 :未执行 01 :运行中 02 :成功 03 :系统失败 04 :业务失败 06 :警告 |
| 13 | fbiztype | 业务类型 | varchar | 80 |  | √ | ' ' | 业务类型,枚举: 01 :自动完工结算 |
| 14 | flastexecdate | 上一次执行时间 | timestamp | 0 |  |  | null | 上一次执行时间 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fsyncdate | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 17 | fexeclog | 执行日志 | varchar | 2000 |  | √ | ' ' | 执行日志 |
| 18 | forderentryseq | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_autocalclog |  | forgid,fcostaccountid |
| 2 | pk_sco_autocalclog |  | fid |
| 3 | idx_sco_autocalclog_st |  | fsyncdate |
