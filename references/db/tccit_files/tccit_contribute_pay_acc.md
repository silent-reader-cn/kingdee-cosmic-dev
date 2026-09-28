# 捐赠支出台账-tccit_contribute_pay_acc

## 捐赠支出台账-主表 t_tccit_contribute_pay

- **表名称：** 捐赠支出台账-主表
- **表名：** t_tccit_contribute_pay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | factualpayamount | 实际支出金额 | numeric | 23 | 10 | √ | 0 | 实际支出金额 |
| 5 | fpayee | 收款单位 | varchar | 1000 |  | √ | ' ' | 收款单位 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fzhangzaiamount | 账载金额 | numeric | 23 | 10 | √ | 0 | 账载金额 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fcontributetype | 捐赠类型 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fbusinessdsummary | 业务摘要 | varchar | 2000 |  | √ | ' ' | 业务摘要 |
| 15 | fbillno | 业务编码 | varchar | 30 |  | √ | ' ' | 业务编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_contribute_pay |  | fid |
| 2 | idx_tccit_contribute_fbillno |  | fbillno |
| 3 | idx_tccit_contribute_forgid |  | forgid,fcontributetype,fbusinessdate |
