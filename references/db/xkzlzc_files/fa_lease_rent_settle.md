# 摊销与计息-fa_lease_rent_settle

## 摊销与计息-主表 t_fa_lease_rent_settle

- **表名称：** 摊销与计息-主表
- **表名：** t_fa_lease_rent_settle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterestdays | 计息天数 | int4 | 32 |  | √ | 0 | 计息天数 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fnextsettledate | 下次结算日期（弃用） | timestamp | 0 |  |  | null | 下次结算日期（弃用） |
| 5 | fsrcid | 源ID | int8 | 64 |  | √ | 0 | 源ID |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fnextsettledatemonth | 下次结算月份 | int8 | 64 |  | √ | 0 | 下次结算月份 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fprincipal | 本金（弃用） | numeric | 19 | 4 | √ | 0.0000 | 本金（弃用） |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | firr | 实际日利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 实际日利率(%) |
| 13 | frent | 租金 | numeric | 19 | 4 | √ | 0.0000 | 租金 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fsettledatemonth | 本次结算月份 | int8 | 64 |  | √ | 0 | 本次结算月份 |
| 16 | fendleaseliab | 期末租赁负债 | numeric | 19 | 4 | √ | 0.0000 | 期末租赁负债 |
| 17 | finterest | 利息费用 | numeric | 19 | 4 | √ | 0.0000 | 利息费用 |
| 18 | fleasecontractid | 合同号 | int8 | 64 |  | √ | 0 | 租赁合同 fa_lease_contract |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | 'A' | 来源类型,枚举: A :新增 B :冲销 |
| 21 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | fsettledate | 摊销日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 摊销日期 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_rentsettle_org_date |  | forgid,fsettledate |
| 2 | idx_fa_rentsettle_contractid |  | fleasecontractid |
| 3 | t_fa_lease_rent_settle_pkey |  | fid |
