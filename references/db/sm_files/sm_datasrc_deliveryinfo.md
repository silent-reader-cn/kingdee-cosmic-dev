# 发货及时情况数据-sm_datasrc_deliveryinfo

## 发货及时情况数据-主表 t_sm_data_deliveryinfo

- **表名称：** 发货及时情况数据-主表
- **表名：** t_sm_data_deliveryinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 6 | foverrows | 逾期发货批数 | numeric | 23 | 10 | √ | 0 | 逾期发货批数 |
| 7 | fdeliverydate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 8 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 9 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 10 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 11 | frealrows | 订单发货及时批数 | numeric | 23 | 10 | √ | 0 | 订单发货及时批数 |
| 12 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 13 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 14 | forderrows | 订单到期批数 | numeric | 23 | 10 | √ | 0 | 订单到期批数 |
| 15 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 16 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |
| 17 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 18 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 19 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_data_deinfo_date |  | fdeliverydate |
| 2 | pk_sm_data_deliveryinfo |  | ftpl_pkid |
| 3 | idx_sm_data_deinfo_org |  | forgid,fcustomerid |
