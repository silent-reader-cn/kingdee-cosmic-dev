# 核算凭证信息-cal_voucher

## 核算凭证信息-主表 t_cal_voucher

- **表名称：** 核算凭证信息-主表
- **表名：** t_cal_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 3 | fvouchertype | 凭证类型 | varchar | 5 |  | √ | ' ' | 凭证类型,枚举: A :正式凭证 B :暂估凭证 C :冲回凭证 D :结转凭证 E :费用凭证 |
| 4 | fcreatemode | 创建方式(暂估冲回凭证记录为1) | int8 | 64 |  | √ | 0 | 创建方式(暂估冲回凭证记录为1) |
| 5 | fperiodid | 期间id(取凭证的期间) | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fvouchernum | 凭证编码 | varchar | 80 |  | √ | ' ' | 凭证编码 |
| 9 | fdischargetype | 冲回方式 | varchar | 5 |  | √ | ' ' | 冲回方式,枚举: A :单到冲回 B :月初一次冲回 C :差额调整 |
| 10 | fcostrecordid | 成本记录（暂估凭证）ID | int8 | 64 |  | √ | 0 | 成本记录（暂估凭证）ID |
| 11 | fvouchersource | 凭证来源 | varchar | 5 |  | √ | ' ' | 凭证来源,枚举: A :成本记录生成 B :系统自动生成 C :应付反写生成 D :携带生成 |
| 12 | fapbillid | 应付单ID | int8 | 64 |  | √ | 0 | 应付单ID |
| 13 | fyear | 年度 | int8 | 64 |  | √ | 0 | 年度 |
| 14 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_vouc_crid |  | fcostrecordid |
| 2 | idx_cal_voucher_id |  | fvoucherid |
| 3 | t_cal_voucher_pkey |  | fid |
