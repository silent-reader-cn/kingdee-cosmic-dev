# 一般纳税人计提进项税额抵扣台账单据-tcvat_deduction_sum_sjjt

## 一般纳税人计提进项税额抵扣台账单据-主表 t_tcvat_deduction_sum_jt

- **表名称：** 一般纳税人计提进项税额抵扣台账单据-主表
- **表名：** t_tcvat_deduction_sum_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 6 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fdescription | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 11 | finputtaxamount | 即征即退进项税额 | numeric | 23 | 10 | √ | 0 | 即征即退进项税额 |
| 12 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: generic :一般计税项目 jzjt :即征即退计税项目 |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 16 | fdeductiontype | 抵扣类型 | varchar | 50 |  | √ | ' ' | 抵扣类型,枚举: 1 :增值税专用发票 1-export :用于出口业务 1-jzjt :用于即征即退业务 2 :通行费发票 2-export :用于出口业务 2-jzjt :用于即征即退业务 3 :海关进口增值税专用缴款书 3-export :用于出口业务 3-jzjt :用于即征即退业务 4 :农产品收购发票或者销售发票 4-export :用于出口业务 4-jzjt :用于即征即退业务 5 :代扣代缴税收缴款凭证 5-export :用于出口业务 5-jzjt :用于即征即退业务 6 :加计扣除农产品进项税额 6-export :用于出口业务 6-jzjt :用于即征即退业务 7 :旅客运输服务扣税凭证 7-export :用于出口业务 7-jzjt :用于即征即退业务 10 :本期用于购建不动产的扣税凭证 |
| 17 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_deduction_sum_serialno |  | forgid,ftaxperiod |
| 2 | pk_tcvat_deduction_sum_jt |  | fid |
