# 进项税额抵扣台账单据-tcvat_deduction_summary

## 进项税额抵扣台账单据-主表 t_tcvat_deduction_summary

- **表名称：** 进项税额抵扣台账单据-主表
- **表名：** t_tcvat_deduction_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 4 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 7 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 8 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 9 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 13 | fdescription | 业务名称 | varchar | 300 |  | √ | ' ' | 业务名称 |
| 14 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 15 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 16 | finputtaxamount | 即征即退进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退进项税额 |
| 17 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 18 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: generic :一般计税项目 jzjt :即征即退计税项目 |
| 19 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 20 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 21 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 22 | fdeductiontype | 抵扣类型 | varchar | 30 |  | √ | ' ' | 抵扣类型,枚举: 1 :增值税专用发票 1-export :用于出口业务 1-jzjt :用于即征即退业务 2 :通行费发票 2-export :用于出口业务 2-jzjt :用于即征即退业务 3 :海关进口增值税专用缴款书 3-export :用于出口业务 3-jzjt :用于即征即退业务 4 :农产品收购发票或者销售发票 4-export :用于出口业务 4-jzjt :用于即征即退业务 5 :代扣代缴税收缴款凭证 5-export :用于出口业务 5-jzjt :用于即征即退业务 6 :加计扣除农产品进项税额 6-export :用于出口业务 6-jzjt :用于即征即退业务 7 :旅客运输服务扣税凭证 7-export :用于出口业务 7-jzjt :用于即征即退业务 10 :本期用于购建不动产的扣税凭证 |
| 23 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_deduction_summary_pkey |  | fid |
| 2 | idx_t_tcvat_deduction_summary |  | forgid,ftaxperiod |
