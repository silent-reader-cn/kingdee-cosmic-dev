# 订单到现金天数-sm_datasrc_ordertorec

## 订单到现金天数-主表 t_sm_data_ordertorec

- **表名称：** 订单到现金天数-主表
- **表名：** t_sm_data_ordertorec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdeptnumber | 销售部门编码 | varchar | 100 |  | √ | ' ' | 销售部门编码 |
| 4 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 5 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 6 | foperatorname | 销售员名称 | varchar | 255 |  | √ | ' ' | 销售员名称 |
| 7 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 8 | foperatorgroupname | 销售组名称 | varchar | 255 |  | √ | ' ' | 销售组名称 |
| 9 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 10 | frecdate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 11 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 13 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 14 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 16 | foperatorgroupnumber | 销售组编码 | varchar | 100 |  | √ | ' ' | 销售组编码 |
| 17 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 18 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 19 | fdeptname | 销售部门名称 | varchar | 255 |  | √ | ' ' | 销售部门名称 |
| 20 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 21 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 22 | frecdays | 订单到收款天数 | int8 | 64 |  | √ | 0 | 订单到收款天数 |
| 23 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 24 | foperatornumber | 销售员编码 | varchar | 100 |  | √ | ' ' | 销售员编码 |
| 25 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_d_ordtorec_date |  | fbizdate |
| 2 | pk_sm_data_ordertorec |  | ftpl_pkid |
| 3 | idx_sm_d_ordtorec_org |  | forgid,fcustomerid |
