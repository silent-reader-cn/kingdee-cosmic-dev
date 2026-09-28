# GST明细-销售-gtcp_gstledger_sales

## GST明细-销售-主表 t_gtcp_gstledger_sales

- **表名称：** GST明细-销售-主表
- **表名：** t_gtcp_gstledger_sales

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 800 |  | √ | ' ' | 描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcustomer | 客户名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsourcename | 来源 | varchar | 200 |  | √ | ' ' | 来源 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 12 | fsourcebill | 来源单据实体对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 16 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 17 | fsourcebillid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 18 | fbillno | 单据编号 | varchar | 200 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtcp_gstsales_org |  | forgid |
| 2 | pk_gtcp_gstledger_sales |  | fid |
