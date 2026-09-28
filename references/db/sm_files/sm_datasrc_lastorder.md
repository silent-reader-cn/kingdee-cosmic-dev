# 最近订货信息-sm_datasrc_lastorder

## 最近订货信息-主表 t_sm_data_lastorder

- **表名称：** 最近订货信息-主表
- **表名：** t_sm_data_lastorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryamount | 单据分录金额(本位币) | numeric | 28 | 10 | √ | 0 | 单据分录金额(本位币) |
| 2 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdeptnumber | 销售部门编码 | varchar | 100 |  | √ | ' ' | 销售部门编码 |
| 6 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 7 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 8 | foperatorname | 销售员名称 | varchar | 255 |  | √ | ' ' | 销售员名称 |
| 9 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 10 | foperatorgroupname | 销售组名称 | varchar | 255 |  | √ | ' ' | 销售组名称 |
| 11 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |
| 12 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 13 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 15 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 16 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 18 | foperatorgroupnumber | 销售组编码 | varchar | 100 |  | √ | ' ' | 销售组编码 |
| 19 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 20 | fbillamount | 单据金额(本位币) | numeric | 28 | 10 | √ | 0 | 单据金额(本位币) |
| 21 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 22 | fdeptname | 销售部门名称 | varchar | 255 |  | √ | ' ' | 销售部门名称 |
| 23 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 24 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 25 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 26 | foperatornumber | 销售员编码 | varchar | 100 |  | √ | ' ' | 销售员编码 |
| 27 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 28 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_data_lastorder |  | ftpl_pkid |
| 2 | idx_sm_data_lstord_org |  | forgid,fcustomerid |
| 3 | idx_sm_data_lstord_date |  | fbizdate |
