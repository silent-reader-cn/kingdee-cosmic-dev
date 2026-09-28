# 销售计划协议F7-amccsa_custschdorder_f7

## 销售计划协议F7-分表 t_amccsa_custschdorder_c

- **表名称：** 销售计划协议F7-分表
- **表名：** t_amccsa_custschdorder_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiptplace | freceiptplace | int8 | 64 |  | √ | 0 |  |
| 3 | fpaidbyid | fpaidbyid | int8 | 64 |  | √ | 0 |  |
| 4 | fshippingaddress | fshippingaddress | varchar | 300 |  |  | null |  |
| 5 | fexchangemethod | fexchangemethod | varchar | 8 |  | √ | ' ' |  |
| 6 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 7 | fsettlementmethodid | fsettlementmethodid | int8 | 64 |  | √ | 0 |  |
| 8 | fsoldtoid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 9 | fcollectiontermid | fcollectiontermid | int8 | 64 |  | √ | 0 |  |
| 10 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 11 | fcontactid | fcontactid | int8 | 64 |  | √ | 0 |  |
| 12 | fshiptoid | fshiptoid | int8 | 64 |  | √ | 0 |  |
| 13 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 14 | fpaymentmethod | fpaymentmethod | varchar | 8 |  | √ | ' ' |  |
| 15 | fconsigneeid | fconsigneeid | int8 | 64 |  | √ | 0 |  |
| 16 | fbilltoid | fbilltoid | int8 | 64 |  | √ | 0 |  |
| 17 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 18 | fincludetax | fincludetax | bpchar | 1 |  | √ | ' ' |  |
| 19 | fcontactaddress | fcontactaddress | varchar | 300 |  |  | null |  |
| 20 | fdeliverytype | fdeliverytype | int8 | 64 |  | √ | 0 |  |
| 21 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 22 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_amccsa_custschdorder_c |  | fid |
| 2 | idx_t_amccsa_csorder_c_shp |  | fshiptoid |

---

## 销售计划协议F7-主表 t_amccsa_custschdorder

- **表名称：** 销售计划协议F7-主表
- **表名：** t_amccsa_custschdorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fdeliverycalendar | fdeliverycalendar | varchar | 8 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 8 | fenddate | 订单截止日期 | timestamp | 0 |  |  | null | 订单截止日期 |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fsdpedigroup | fsdpedigroup | varchar | 8 |  | √ | ' ' |  |
| 11 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 12 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 13 | fdefaultqtymethod | fdefaultqtymethod | varchar | 8 |  | √ | ' ' |  |
| 14 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 17 | fremark | fremark | varchar | 510 |  |  | null |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 22 | fisinitbill | fisinitbill | bpchar | 1 |  | √ | ' ' |  |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 25 | fsubversion | fsubversion | varchar | 50 |  | √ | ' ' |  |
| 26 | fstartdate | 订单起始日期 | timestamp | 0 |  |  | null | 订单起始日期 |
| 27 | fisaccumulation | fisaccumulation | bpchar | 1 |  | √ | '0' |  |
| 28 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 29 | fplandatetype | fplandatetype | varchar | 8 |  | √ | ' ' |  |
| 30 | fdaysdelivery | fdaysdelivery | int4 | 32 |  | √ | 0 |  |
| 31 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_custschdorder_org |  | forgid |
| 2 | pk_t_amccsa_custschdorder |  | fid |
