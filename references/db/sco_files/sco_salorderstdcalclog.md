# 跟踪号成本卷算日志-sco_salorderstdcalclog

## 跟踪号成本卷算日志-主表 t_sco_salorderstdcalclog

- **表名称：** 跟踪号成本卷算日志-主表
- **表名：** t_sco_salorderstdcalclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsalorderno | 订单编号 | varchar | 50 |  | √ | ' ' | 订单编号 |
| 4 | fsalorderseq | 订单行号 | int8 | 64 |  | √ | 0 | 订单行号 |
| 5 | fsalorderentryid | 订单分录id | int8 | 64 |  | √ | 0 | 订单分录id |
| 6 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | fsrcbill | 来源单据 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | foperdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 13 | fstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 00 :未执行 01 :运行中 02 :成功 03 :失败 04 :业务失败 05 :取消 |
| 14 | foperationtype | 执行操作 | varchar | 10 |  | √ | ' ' | 执行操作,枚举: 1 :卷算 2 :更新 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | ftransmittime | 首次工单下达时间 | timestamp | 0 |  |  | null | 首次工单下达时间 |
| 17 | ftargetcosttypeid | 目标标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 18 | fupdatestatu | 更新状态 | varchar | 30 |  | √ | ' ' | 更新状态,枚举: S :成功 F :失败 |
| 19 | fupdatelog | 更新日志 | varchar | 2000 |  | √ | ' ' | 更新日志 |
| 20 | fcalctaskid | 卷算任务id | int8 | 64 |  | √ | 0 | 卷算任务id |
| 21 | fupdatetaskid | 更新任务id | int8 | 64 |  | √ | 0 | 更新任务id |
| 22 | ftrytimes | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 23 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 24 | flastexecdate | 上一次执行时间 | timestamp | 0 |  |  | null | 上一次执行时间 |
| 25 | fsalorderaudittime | 订单审核时间 | timestamp | 0 |  |  | null | 订单审核时间 |
| 26 | fsyncdate | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 27 | fexeclog | 执行日志 | varchar | 2000 |  | √ | ' ' | 执行日志 |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_salorderstdcalclog |  | fid |
| 2 | idx_stdcostcalclog_syncdate |  | fsyncdate |
