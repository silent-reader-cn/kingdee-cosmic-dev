# 委外用料清单f7-om_mftstock_headf7

## 委外用料清单f7-主表 t_om_mftorderentry_s

- **表名称：** 委外用料清单f7-主表
- **表名：** t_om_mftorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillauxqty | fbillauxqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 6 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 7 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 8 | fmftorderid | fmftorderid | int8 | 64 |  | √ | 0 |  |
| 9 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 10 | forderentryid | 委外工单行号 | int8 | 64 |  | √ | 0 | 委外工单分录F7 om_mftorder_f7 |
| 11 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fomversion | fomversion | varchar | 50 |  | √ | ' ' |  |
| 14 | fauxproperty | fauxproperty | int8 | 64 |  | √ | 0 |  |
| 15 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 16 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 19 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 20 | fentrustorg | fentrustorg | int8 | 64 |  | √ | 0 |  |
| 21 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 22 | fplanpreparetime | fplanpreparetime | timestamp | 0 |  |  | null |  |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 27 | fischanged | fischanged | bpchar | 1 |  | √ | '0' |  |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 30 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fproductmasterid | fproductmasterid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 33 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | forderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 35 | fprocessroute | fprocessroute | int8 | 64 |  | √ | 0 |  |
| 36 | fmftinqty | fmftinqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 38 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
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
| 1 | idx_om_moes_fcreatetime |  | fcreatetime |
| 2 | idx_om_moes_forderid |  | forderid |
| 3 | pk_om_mftorderentry_s |  | fentryid |
| 4 | idx_om_moes_forgideid |  | forgid,fentryid |
| 5 | idx_om_mes_fproductmasterid |  | fproductmasterid |
| 6 | idx_om_mes_orderno |  | fbillno,forderno |
| 7 | idx_om_moes_forderentryid |  | forderentryid |
