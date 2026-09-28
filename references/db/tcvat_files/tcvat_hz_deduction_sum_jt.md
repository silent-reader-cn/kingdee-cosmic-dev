# 总机构进项税额抵扣台账单据-tcvat_hz_deduction_sum_jt

## 总机构进项税额抵扣台账单据-主表 t_tcvat_hz_deduct_sum_jt

- **表名称：** 总机构进项税额抵扣台账单据-主表
- **表名：** t_tcvat_hz_deduct_sum_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 5 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsuborgname | fsuborgname | varchar | 50 |  | √ | ' ' |  |
| 9 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fdescription | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 12 | fdeductiontypebase | 抵扣类型 | int8 | 64 |  | √ | 0 | 业务定义 tpo_tcvat_bizdef |
| 13 | finputtaxamount | 即征即退进项税额 | numeric | 23 | 10 | √ | 0 | 即征即退进项税额 |
| 14 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 15 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: generic :一般计税项目 jzjt :即征即退计税项目 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 19 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 21 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 22 | fdeductiontype | 抵扣类型(废弃) | varchar | 50 |  | √ | ' ' | 抵扣类型(废弃),枚举: 1 :增值税专用发票 1-export :用于出口业务 1-jzjt :用于即征即退业务 2 :通行费发票 2-export :用于出口业务 2-jzjt :用于即征即退业务 3 :海关进口增值税专用缴款书 3-export :用于出口业务 3-jzjt :用于即征即退业务 4 :农产品收购发票或者销售发票 4-export :用于出口业务 4-jzjt :用于即征即退业务 5 :代扣代缴税收缴款凭证 5-export :用于出口业务 5-jzjt :用于即征即退业务 6 :加计扣除农产品进项税额 6-export :用于出口业务 6-jzjt :用于即征即退业务 7 :旅客运输服务扣税凭证 7-export :用于出口业务 7-jzjt :用于即征即退业务 |
| 23 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 24 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_hz_deduct_sum_jt |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_hz_deduct_sum_jt |  | fid |
