# 计划成本计算日志-sco_plancostcalclog

## 计划成本计算日志-主表 t_sco_plancostcalclog

- **表名称：** 计划成本计算日志-主表
- **表名：** t_sco_plancostcalclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | freleasedate | 下达/变更日期 | timestamp | 0 |  |  | null | 下达/变更日期 |
| 5 | forderno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 6 | foperdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | forderentryid | 工单分录id | int8 | 64 |  | √ | 0 | 工单分录id |
| 8 | ftrytimes | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 9 | fstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 00 :未执行 01 :运行中 02 :成功 03 :失败 |
| 10 | faccountcosttypeid | 核算标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 11 | flastexecdate | 上一次执行时间 | timestamp | 0 |  |  | null | 上一次执行时间 |
| 12 | fsyncdate | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 13 | fplancosttypeid | 计划标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 14 | forderentryseq | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |
| 15 | fexeclog | 执行日志 | varchar | 2000 |  | √ | ' ' | 执行日志 |
| 16 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: pom_mftorder :生产工单 om_mftorder :委外工单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_plancostcalclog |  | fid |
| 2 | idx_plancostcalclog_syncdate |  | fsyncdate |
