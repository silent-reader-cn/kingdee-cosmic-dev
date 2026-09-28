# 退货信息-sm_datasrc_returninfo

## 退货信息-主表 t_sm_data_returninfo

- **表名称：** 退货信息-主表
- **表名：** t_sm_data_returninfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdeptnumber | 销售部门编码 | varchar | 100 |  | √ | ' ' | 销售部门编码 |
| 5 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 6 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 7 | foperatorname | 销售员名称 | varchar | 255 |  | √ | ' ' | 销售员名称 |
| 8 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 9 | foperatorgroupname | 销售组名称 | varchar | 255 |  | √ | ' ' | 销售组名称 |
| 10 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |
| 11 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 13 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 14 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 16 | freturnamount | 累计退货总额 | numeric | 28 | 10 | √ | 0 | 累计退货总额 |
| 17 | foperatorgroupnumber | 销售组编码 | varchar | 100 |  | √ | ' ' | 销售组编码 |
| 18 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 19 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 20 | fdeptname | 销售部门名称 | varchar | 255 |  | √ | ' ' | 销售部门名称 |
| 21 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 22 | forderamount | 订单总额 | numeric | 28 | 10 | √ | 0 | 订单总额 |
| 23 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 24 | foperatornumber | 销售员编码 | varchar | 100 |  | √ | ' ' | 销售员编码 |
| 25 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 26 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 27 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_data_returninfo |  | ftpl_pkid |
| 2 | idx_sm_data_ret_org |  | forgid,fcustomerid |
| 3 | idx_sm_data_ret_date |  | fbizdate |
