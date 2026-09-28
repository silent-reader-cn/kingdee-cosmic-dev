# 其他存货核算记录-cal_other_record

## 其他存货核算记录-主表 t_cal_otherrecord

- **表名称：** 其他存货核算记录-主表
- **表名：** t_cal_otherrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillformid | 单据类型ID | varchar | 36 |  | √ | ' ' | 单据类型ID |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fcostrecordentryid | 核算成本记录单据分录ID | int8 | 64 |  | √ | 0 | 核算成本记录单据分录ID |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ffee | 费用 | numeric | 23 | 10 | √ | 0 | 费用 |
| 11 | fcalentryid | 核算单分录ID | int8 | 64 |  | √ | 0 | 核算单分录ID |
| 12 | fweightsource | 权重来源 | varchar | 10 |  | √ | ' ' | 权重来源,枚举: 1 :手工维护 2 :库存单据（默认） 3 :成本取价配置 |
| 13 | fweight | 权重 | numeric | 23 | 10 | √ | 0 | 权重 |
| 14 | fcostrecordid | 核算成本记录单据ID | int8 | 64 |  | √ | 0 | 核算成本记录单据ID |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 18 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 19 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | funitfee | 单位费用 | numeric | 23 | 10 | √ | 0 | 单位费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_otherrecord |  | fid |
| 2 | idx_cal_otherrecord_calentryid |  | fcalentryid |
| 3 | idx_cal_otherrecord_cost |  | fcostrecordentryid |
| 4 | idx_cal_otherrecord_cp |  | fcostaccountid,fperiodid |
