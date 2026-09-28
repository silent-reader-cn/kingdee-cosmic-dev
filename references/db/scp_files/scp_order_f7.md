# 采购订单F7-scp_order_f7

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
| 5 | fprepayrate | fprepayrate | numeric | 19 | 2 | √ | 0.00 |  |
| 6 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | 订货客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fsumpayableamt | fsumpayableamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 11 | fpayeesupid | fpayeesupid | int8 | 64 |  | √ | 0 |  |
| 12 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 13 | fpaystatus | fpaystatus | bpchar | 1 |  | √ | ' ' |  |
| 14 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 15 | fcentersettle | fcentersettle | bpchar | 1 |  | √ | ' ' |  |
| 16 | fsumamount | fsumamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | fsupgroupid | fsupgroupid | int8 | 64 |  | √ | 0 |  |
| 18 | fdeliaddr | fdeliaddr | varchar | 255 |  | √ | ' ' |  |
| 19 | fsumpayamt | fsumpayamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 22 | fsuminvoiceamt | fsuminvoiceamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 25 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 E :变更中 |
| 27 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 28 | finvoicesupid | finvoicesupid | int8 | 64 |  | √ | 0 |  |
| 29 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fdelisupid | fdelisupid | int8 | 64 |  | √ | 0 |  |
| 32 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 33 | fsumqty | fsumqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 34 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 35 | fsupplierid | 销售公司 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 37 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 38 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 E :自动确认 |
| 39 | fissyn | fissyn | bpchar | 1 |  | √ | ' ' |  |
| 40 | fpersonid | fpersonid | int8 | 64 |  | √ | 0 |  |
| 41 | fsumprepayamt | fsumprepayamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 42 | fsumtaxamount | fsumtaxamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 43 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 44 | fsumtax | fsumtax | numeric | 19 | 6 | √ | 0.000000 |  |
| 45 | fbusinesstypeid | fbusinesstypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fexchrate | fexchrate | numeric | 19 | 6 | √ | 1.000000 |  |
| 47 | fcontacterid | fcontacterid | int8 | 64 |  | √ | 0 |  |
| 48 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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

---

## 采购订单F7-分表 t_pur_order_a

- **表名称：** 采购订单F7-分表
- **表名：** t_pur_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumsaloutamount | fsumsaloutamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 3 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 4 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 5 | fbillversion | fbillversion | varchar | 50 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 8 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | ' ' |  |
| 11 | frejectdate | frejectdate | timestamp | 0 |  |  | null |  |
| 12 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 15 | fsuggestion | fsuggestion | varchar | 255 |  | √ | ' ' |  |
| 16 | frejectreason | frejectreason | varchar | 512 |  |  | ' ' |  |
| 17 | frejecterid | frejecterid | int8 | 64 |  | √ | 0 |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 20 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 21 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | ' ' |  |
| 22 | fcloseid | fcloseid | int8 | 64 |  | √ | 0 |  |
| 23 | fsumdiffamount | fsumdiffamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 24 | fsrcbilltype | fsrcbilltype | bpchar | 1 |  | √ | ' ' |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fsumsettleamount | fsumsettleamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 27 | fcheckstatus | fcheckstatus | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_order_a_pkey |  | fid |
| 2 | idx_pur_order_a_fcreatetime |  | fcreatetime |
