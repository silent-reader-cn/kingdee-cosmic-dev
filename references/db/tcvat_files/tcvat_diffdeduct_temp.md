# 差额扣除模板-tcvat_diffdeduct_temp

## 差额扣除模板-主表 t_tcvat_diffdeduct

- **表名称：** 差额扣除模板-主表
- **表名：** t_tcvat_diffdeduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 5 | fdifftypeid | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 6 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fdeductproject | 扣除项目 | varchar | 50 |  | √ | ' ' | 扣除项目,枚举: bqfse :本期发生额 bqsjkce :本期实际扣除额 fseandkce :本期发生额和实际扣除额 |
| 10 | fjzjtdeductamount | 即征即退实际扣除额 | numeric | 23 | 10 | √ | 0 | 即征即退实际扣除额 |
| 11 | fdeductamount | 本期实际扣除额 | numeric | 23 | 10 | √ | 0 | 本期实际扣除额 |
| 12 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 13 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 14 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 15 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 16 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 17 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 18 | fproject | 项目 | varchar | 100 |  | √ | ' ' | 项目 |
| 19 | frowno | 行号 | varchar | 100 |  | √ | ' ' | 行号 |
| 20 | fdeductiontype | 免税性质代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 21 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_diffdeduct_id |  | forgid,ftaxperiod |
| 2 | t_tcvat_diffdeduct_pkey |  | fid |
