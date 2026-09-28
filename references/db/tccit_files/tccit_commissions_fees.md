# 佣金手续费台账-tccit_commissions_fees

## 佣金手续费台账-主表 t_tccit_commissions_fees

- **表名称：** 佣金手续费台账-主表
- **表名：** t_tccit_commissions_fees

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fnonallowed | 不允许扣除金额 | numeric | 23 | 10 | √ | 0 | 不允许扣除金额 |
| 9 | fdeductlimit | 扣除限额 | numeric | 23 | 10 | √ | 0 | 扣除限额 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fssje | 税收金额 | numeric | 23 | 10 | √ | 0 | 税收金额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftype | 佣金手续费类型 | varchar | 50 |  | √ | ' ' | 佣金手续费类型,枚举: 1 :一般企业佣金手续费 2 :房地产委外销售佣金手续费 |
| 16 | frate | 税收规定扣除率 | numeric | 23 | 10 | √ | 0 | 税收规定扣除率 |
| 17 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0 | 账载金额 |
| 19 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: import :数据引入 hand :手工新增 |
| 20 | fbillno | 业务编码 | varchar | 30 |  | √ | ' ' | 业务编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_commissions_fees |  | fid |
| 2 | t_fbillno_idx |  | fbillno |
