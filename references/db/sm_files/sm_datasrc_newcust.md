# 新增客户数-sm_datasrc_newcust

## 新增客户数-主表 t_sm_data_newcust

- **表名称：** 新增客户数-主表
- **表名：** t_sm_data_newcust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fcustomername | 订货客户名称 | varchar | 255 |  | √ | ' ' | 订货客户名称 |
| 4 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 5 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgnumber | 销售组织编码 | varchar | 100 |  | √ | ' ' | 销售组织编码 |
| 8 | foperatorgroupnumber | 销售组编码 | varchar | 100 |  | √ | ' ' | 销售组编码 |
| 9 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 10 | fdeptnumber | 销售部门编码 | varchar | 100 |  | √ | ' ' | 销售部门编码 |
| 11 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 12 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 13 | foperatorname | 销售员名称 | varchar | 255 |  | √ | ' ' | 销售员名称 |
| 14 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 15 | fdeptname | 销售部门名称 | varchar | 255 |  | √ | ' ' | 销售部门名称 |
| 16 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 17 | fbizdate | 最早客户创建日期 | timestamp | 0 |  |  | null | 最早客户创建日期 |
| 18 | foperatorgroupname | 销售组名称 | varchar | 255 |  | √ | ' ' | 销售组名称 |
| 19 | forgname | 销售组织名称 | varchar | 255 |  | √ | ' ' | 销售组织名称 |
| 20 | foperatornumber | 销售员编码 | varchar | 100 |  | √ | ' ' | 销售员编码 |
| 21 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fcustomernumber | 订货客户编码 | varchar | 100 |  | √ | ' ' | 订货客户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_data_newcust_org |  | forgid,fcustomerid |
| 2 | pk_sm_data_newcust |  | ftpl_pkid |
