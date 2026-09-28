# 库存周转数据集-im_inv_ito_anal

## 库存周转数据集-主表 t_im_inv_ito_anal

- **表名称：** 库存周转数据集-主表
- **表名：** t_im_inv_ito_anal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty_bal | 结余数量 | numeric | 23 | 10 | √ | 0 | 结余数量 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcountdate | 统计期间 | timestamp | 0 |  |  | null | 统计期间 |
| 6 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 7 | fversiontime | 版本同步日期 | timestamp | 0 |  |  | null | 版本同步日期 |
| 8 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 9 | fmonth | 月份 | int4 | 32 |  | √ | 0 | 月份 |
| 10 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fitoratio | 库存周转率 | numeric | 23 | 10 | √ | 0 | 库存周转率 |
| 13 | fqty_in | 收入数量 | numeric | 23 | 10 | √ | 0 | 收入数量 |
| 14 | fqty | 期初数量 | numeric | 23 | 10 | √ | 0 | 期初数量 |
| 15 | fendperiod | 结束期间 | int4 | 32 |  | √ | 0 | 结束期间 |
| 16 | fitodaytype | 周转天数分布类型 | varchar | 50 |  | √ | ' ' | 周转天数分布类型,枚举: |
| 17 | fitoday | 周转天数 | int4 | 32 |  | √ | 0 | 周转天数 |
| 18 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 19 | fitodaytypename | 库存周转天数类型名称 | varchar | 50 |  | √ | ' ' | 库存周转天数类型名称 |
| 20 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fitoratiotype | 库存周转率类型 | varchar | 50 |  | √ | ' ' | 库存周转率类型,枚举: 6 :低 8 :高 |
| 24 | fperioddays | 期间天数 | int4 | 32 |  | √ | 0 | 期间天数 |
| 25 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fyear | 年份 | int4 | 32 |  | √ | 0 | 年份 |
| 27 | fqty_bal_sameterm | 同期结余数量 | numeric | 23 | 10 | √ | 0 | 同期结余数量 |
| 28 | fperiod | 开始期间 | int4 | 32 |  | √ | 0 | 开始期间 |
| 29 | fitoratiotypename | 库存周转率类型名称 | varchar | 50 |  | √ | ' ' | 库存周转率类型名称 |
| 30 | fkeycol | Keycol | varchar | 50 |  | √ | ' ' | Keycol |
| 31 | fqty_out | 发出数量 | numeric | 23 | 10 | √ | 0 | 发出数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_inv_ito_anal |  | fid |
| 2 | idx_im_inv_ito_anal_fkey |  | fkeycol |
