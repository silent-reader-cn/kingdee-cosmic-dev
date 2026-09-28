# 自动完工结算日志-sca_autofinish_calclog

## 自动完工结算日志-主表 t_sca_autofinish_calclog

- **表名称：** 自动完工结算日志-主表
- **表名：** t_sca_autofinish_calclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsrcentryid | 工单分录ID | int8 | 64 |  | √ | 0 | 工单分录ID |
| 4 | ftraceid | 日志轨迹ID | varchar | 1000 |  | √ | ' ' | 日志轨迹ID |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fsrcbillno | 工单编码 | varchar | 60 |  | √ | ' ' | 工单编码 |
| 7 | fbillstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :失败 B :成功 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fsrcentryseq | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |
| 12 | fmodifytime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 15 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 16 | flogtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: 0 :互斥锁 1 :执行异常 2 :正常 3 :材料耗用分配 |
| 17 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | flogdetail | 日志详情 | varchar | 2000 |  | √ | ' ' | 日志详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_autofinish_calclog |  | fbillno,forgid,fcostobjectid,fcostaccountid,fperiodid |
| 2 | pk_t_sca_autofinish_calclog |  | fid |
