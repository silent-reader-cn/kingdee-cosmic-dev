# 定时核销监控-ar_rpa_settlelog

## 定时核销监控-主表 t_ar_rpasettlelog

- **表名称：** 定时核销监控-主表
- **表名：** t_ar_rpasettlelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemenumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fasstentrycount | 辅方分录数量 | int4 | 32 |  | √ | 0 | 辅方分录数量 |
| 5 | fmainbillentity | 主方单据标识 | varchar | 50 |  | √ | ' ' | 主方单据标识 |
| 6 | fschemeid | 核销方案id | int8 | 64 |  | √ | 0 | 核销方案id |
| 7 | fschemeruleid | 核销执行规则id | int8 | 64 |  | √ | 0 | 核销执行规则id |
| 8 | fmainentrycount | 主方分录数量 | int4 | 32 |  | √ | 0 | 主方分录数量 |
| 9 | fasstsettleamt | 辅方执行金额 | numeric | 23 | 10 | √ | 0 | 辅方执行金额 |
| 10 | fsettlerecordcount | 核销记录数 | int4 | 32 |  | √ | 0 | 核销记录数 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fasstbillentity | 辅方单据标识 | varchar | 50 |  | √ | ' ' | 辅方单据标识 |
| 13 | fmainsettleamt | 主方执行金额 | numeric | 23 | 10 | √ | 0 | 主方执行金额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmaincount | 主方单据数量 | int4 | 32 |  | √ | 0 | 主方单据数量 |
| 16 | fexecuteprocess | 执行进度 | varchar | 50 |  | √ | ' ' | 执行进度 |
| 17 | fasstexecutedcount | 辅方已执行单数 | int4 | 32 |  | √ | 0 | 辅方已执行单数 |
| 18 | fusetime | 用时 | int8 | 64 |  | √ | 0 | 用时 |
| 19 | ferrordesc | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 20 | fbillno | 日志编码 | varchar | 80 |  | √ | ' ' | 日志编码 |
| 21 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fisstop | 已中止 | bpchar | 1 |  | √ | ' ' | 已中止 |
| 24 | fsettlerelation | 核销关系 | varchar | 50 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 recself :收款红蓝对冲 arself :应收红蓝对冲 arapsettle :应收冲应付 recpaysettle :收款冲退款 arpaymentsettle :应收退款核销 arliqsettle :应收清理 recclearing :收款清理 |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fasstcount | 辅方单据数量 | int4 | 32 |  | √ | 0 | 辅方单据数量 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fexecutestate | 执行状态 | varchar | 5 |  | √ | ' ' | 执行状态,枚举: 0 :成功 1 :执行中 2 :失败 |
| 30 | fmainexecutedcount | 主方已执行单数 | int4 | 32 |  | √ | 0 | 主方已执行单数 |
| 31 | fstarttime | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 32 | fschemename | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 33 | ferrordesc_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 34 | fendtime | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 35 | fexecutetype | 执行类型 | varchar | 5 |  | √ | ' ' | 执行类型,枚举: 0 :自动执行 1 :手动执行 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_rpa_fnumber |  | fbillno |
| 2 | pk_t_ar_rpasettlelog |  | fid |
| 3 | idx_ar_rpa_dateorg |  | fstarttime,forgid |
