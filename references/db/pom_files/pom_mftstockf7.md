# 生产组件清单f7-pom_mftstockf7

## 生产组件清单f7-主表 t_pom_mftorderentry_s

- **表名称：** 生产组件清单f7-主表
- **表名：** t_pom_mftorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillauxqty | fbillauxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | fauxpropertynew | fauxpropertynew | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 7 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 8 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 9 | forderentryid | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单分录f7 pom_mftorder_f7 |
| 10 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fomversion | fomversion | varchar | 50 |  | √ | ' ' |  |
| 13 | fauxproperty | fauxproperty | varchar | 50 |  | √ | ' ' |  |
| 14 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 15 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 16 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 17 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 18 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 19 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 23 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 24 | fischanged | fischanged | bpchar | 1 |  | √ | '0' |  |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fproductmasterid | fproductmasterid | int8 | 64 |  | √ | 0 |  |
| 29 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 30 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | forderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 32 | fprocessroute | fprocessroute | int8 | 64 |  | √ | 0 |  |
| 33 | fmftinqty | fmftinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 35 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fbillauxunit | fbillauxunit | int8 | 64 |  | √ | 0 |  |
| 38 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 39 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

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
