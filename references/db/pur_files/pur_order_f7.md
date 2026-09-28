# 采购订单F7-pur_order_f7

## 采购订单F7-主表 t_pur_order

- **表名称：** 采购订单F7-主表
- **表名：** t_pur_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fdelidate | fdelidate | timestamp | 0 |  |  | null |  |
| 3 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 4 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 7 | fsumpayableamt | fsumpayableamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 8 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 9 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0.000000 |  |
| 10 | fsumpayamt | fsumpayamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 E :变更中 |
| 14 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 15 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 16 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 17 | fissyn | fissyn | bpchar | 1 |  | √ | ' ' |  |
| 18 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 19 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 20 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 21 | fcontacterid | fcontacterid | int8 | 64 |  | √ | 0 |  |
| 22 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fprepayrate | fprepayrate | numeric | 23 | 6 | √ | 0.00 |  |
| 24 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 25 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 26 | fpayeesupid | fpayeesupid | int8 | 64 |  | √ | 0 |  |
| 27 | fpaystatus | fpaystatus | bpchar | 1 |  | √ | ' ' |  |
| 28 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 29 | fcentersettle | fcentersettle | bpchar | 1 |  | √ | ' ' |  |
| 30 | fsupgroupid | fsupgroupid | int8 | 64 |  | √ | 0 |  |
| 31 | fplatform | fplatform | bpchar | 1 |  | √ | ' ' |  |
| 32 | fdeliaddr | fdeliaddr | varchar | 255 |  | √ | ' ' |  |
| 33 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 34 | fsuminvoiceamt | fsuminvoiceamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 35 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 37 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 38 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 39 | finvoicesupid | finvoicesupid | int8 | 64 |  | √ | 0 |  |
| 40 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 41 | fdelisupid | fdelisupid | int8 | 64 |  | √ | 0 |  |
| 42 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0.000000 |  |
| 44 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 45 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 46 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 47 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 E :自动确认 |
| 48 | fsumprepayamt | fsumprepayamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 49 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0.000000 |  |
| 50 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0.000000 |  |
| 51 | fexchrate | fexchrate | numeric | 23 | 10 | √ | 1.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_order_pkey |  | fid |
| 2 | idx_pur_order_fbillno |  | fbillno |
| 3 | idx_pur_order_frcvorgid |  | frcvorgid |
| 4 | idx_pur_order_fsupplierid |  | fsupplierid |
| 5 | idx_pur_order_fbizpartnerid |  | fbilldate,fbizpartnerid |
