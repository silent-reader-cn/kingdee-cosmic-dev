# 生产用料清单f7-pom_mftstockf7

## 生产用料清单f7-主表 t_pom_mftorderentry_s

- **表名称：** 生产用料清单f7-主表
- **表名：** t_pom_mftorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillauxqty | fbillauxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fauxpropertynew | fauxpropertynew | int8 | 64 |  | √ | 0 |  |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 8 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 9 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 10 | fmftorderid | fmftorderid | int8 | 64 |  | √ | 0 |  |
| 11 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 12 | forderentryid | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单分录f7 pom_mftorder_f7 |
| 13 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fomversion | fomversion | varchar | 50 |  | √ | ' ' |  |
| 16 | fauxproperty | fauxproperty | varchar | 50 |  | √ | ' ' |  |
| 17 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 18 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 20 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 21 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 22 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 26 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 27 | fischanged | fischanged | bpchar | 1 |  | √ | '0' |  |
| 28 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 30 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fproductmasterid | fproductmasterid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 33 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | forderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 35 | fprocessroute | fprocessroute | int8 | 64 |  | √ | 0 |  |
| 36 | fmftinqty | fmftinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 38 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fbillauxunit | fbillauxunit | int8 | 64 |  | √ | 0 |  |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 42 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_moes_fbillno |  | fbillno |
| 2 | t_pom_mftorderentry_s_pkey |  | fentryid |
| 3 | idx_stock_ftracknumber |  | ftracknumberid |
| 4 | idx_mftorderentry_s_orgfid |  | forgid,fentryid |
| 5 | idx_pom_moes_forderid |  | forderid,forderentryid,fsourcebillid,forderno |
| 6 | idx_mftstock_mftid |  | fmaterialid,fproductmasterid |
| 7 | idx_pom_moes_fcreatetime |  | fcreatetime |
| 8 | idx_stock_fconfiguredcode |  | fconfiguredcodeid |
