# 总机构减税项目台账单据-tcvat_hz_taxreduce_sum

## 总机构减税项目台账单据-主表 t_tcvat_hz_taxreduce_sum

- **表名称：** 总机构减税项目台账单据-主表
- **表名：** t_tcvat_hz_taxreduce_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 2 :汇总 3 :被汇总 |
| 7 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 8 | fdescription | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 9 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 10 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 14 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 15 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 16 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 17 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 18 | ftaxreductiontype | 减税项目类型 | varchar | 30 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 19 | fsuborg | 汇总方案组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |
| 21 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_taxreduce_sum |  | fid |
| 2 | idx_tcvat_hz_taxreduce_sum |  | forgid,fstartdate,fenddate |
