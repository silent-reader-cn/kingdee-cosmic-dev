# 新增投资资产基础资料-tccit_new_invest_asset_bs

## 新增投资资产基础资料-主表 t_tccit_new_invest_asset

- **表名称：** 新增投资资产基础资料-主表
- **表名：** t_tccit_new_invest_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 投资标的名称 | varchar | 50 |  | √ | ' ' | 投资标的名称 |
| 4 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fljjysf | fljjysf | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fljjsjc | fljjsjc | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | finvesttype | 投资性质 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 10 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | ftaxpayerid | ftaxpayerid | varchar | 50 |  | √ | ' ' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fassettype | 资产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 15 | fljtzcbrzje | fljtzcbrzje | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 17 | fbillno | 资产编号 | varchar | 30 |  | √ | ' ' | 资产编号 |
| 18 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 19 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: 0 :持有 1 :处置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_new_invest_asset |  | fid |
| 2 | idx_tccit_new_invest_asset |  | fbillno |
