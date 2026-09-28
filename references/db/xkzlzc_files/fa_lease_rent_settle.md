# 摊销与计息-fa_lease_rent_settle

## 摊销与计息-主表 t_fa_lease_rent_settle

- **表名称：** 摊销与计息-主表
- **表名：** t_fa_lease_rent_settle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcid | 源ID | int8 | 64 |  | √ | 0 | 源ID |
| 3 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fprincipal | 本金（弃用） | numeric | 19 | 4 | √ | 0.0000 | 本金（弃用） |
| 5 | fleaseexp | 租赁费用 | numeric | 19 | 6 | √ | 0 | 租赁费用 |
| 6 | frent | 租金 | numeric | 19 | 4 | √ | 0.0000 | 租金 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fendleaseliab | 期末租赁负债 | numeric | 19 | 4 | √ | 0.0000 | 期末租赁负债 |
| 9 | finterest | 利息费用 | numeric | 19 | 4 | √ | 0.0000 | 利息费用 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fleaseexpbak | fleaseexpbak | numeric | 19 | 6 | √ | 0 |  |
| 12 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | 'A' | 来源类型,枚举: A :新增 B :冲销 |
| 13 | fbillno | 单据编号 | varchar | 40 |  | √ | ' ' | 单据编号 |
| 14 | fsettledate | 摊销日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 摊销日期 |
| 15 | finterestdays | 计息天数 | int4 | 32 |  | √ | 0 | 计息天数 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fnextsettledate | 下次结算日期（弃用） | timestamp | 0 |  |  | null | 下次结算日期（弃用） |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :废弃 |
| 19 | fnextsettledatemonth | 下次结算月份 | int8 | 64 |  | √ | 0 | 下次结算月份 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | firr | 实际日利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 实际日利率(%) |
| 23 | fsettledatemonth | 本次结算月份 | int8 | 64 |  | √ | 0 | 本次结算月份 |
| 24 | fleasecontractid | 合同号 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
