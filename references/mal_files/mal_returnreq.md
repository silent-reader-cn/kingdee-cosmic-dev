# 售后申请单-mal_returnreq

## 商品详情分录-子表 t_pur_requestentry

- **表名称：** 商品详情分录-子表
- **表名：** t_pur_requestentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretdate | 退货日期 | timestamp | 0 |  |  | null | 退货日期 |
| 3 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fproddate | fproddate | timestamp | 0 |  |  | null |  |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | flotnumber | flotnumber | varchar | 80 |  | √ | ' ' |  |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | fnote | varchar | 512 |  | √ | ' ' |  |
| 11 | ftaxprice | 商品价格 | numeric | 23 | 10 | √ | 0.0000000000 | 商品价格 |
| 12 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 14 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 15 | fretreason | 退货原因 | varchar | 255 |  | √ | ' ' | 退货原因 |
| 16 | fdctamount | fdctamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 19 | ftaxamount | 商品金额 | numeric | 19 | 6 | √ | 0.000000 | 商品金额 |
| 20 | fdctrate | fdctrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 21 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 22 | ftraceid | ftraceid | int8 | 64 |  | √ | 0 |  |
| 23 | fmaterialnewid | fmaterialnewid | int8 | 64 |  | √ | 0 |  |
| 24 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 25 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | 'NULL' |  |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fpcbillno | fpcbillno | varchar | 80 |  | √ | ' ' |  |
| 28 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 29 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 30 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 31 | finvorgid | finvorgid | int8 | 64 |  | √ | 0 |  |
| 32 | fduedate | fduedate | timestamp | 0 |  |  | null |  |
| 33 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 34 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 35 | fsuplot | fsuplot | varchar | 80 |  | √ | ' ' |  |
| 36 | freplenishqty | 补货数量 | numeric | 19 | 6 | √ | 0.000000 | 补货数量 |
| 37 | fmaterialnametext | fmaterialnametext | varchar | 255 |  | √ | ' ' |  |
| 38 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 39 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fmaterialdesc | fmaterialdesc | varchar | 255 |  | √ | ' ' |  |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 43 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_requestentry_fmatid |  | fmaterialid |
| 2 | idx_pur_requestentry_fid_fseq |  | fid,fseq |
| 3 | t_pur_requestentry_pkey |  | fentryid |

---

## 售后申请单-分表 t_pur_request_a

- **表名称：** 售后申请单-分表
- **表名：** t_pur_request_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmalorderno | fmalorderno | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fjdserviceid | 京东服务单号 | varchar | 50 |  | √ | ' ' | 京东服务单号 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fecsource | 电商平台类型 | varchar | 80 |  | √ | ' ' | 电商平台类型,枚举: pbd_jdorder :京东订单 pbd_order_sn :苏宁易购 pbd_order_xy :电商订单_西域 pbd_order_cg :电商订单_晨光 pbd_order_dl :电商订单_得力 pbd_order_xfs :电商订单_鑫方盛 |
| 9 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_request_a_pkey |  | fid |
| 2 | idx_pur_request_a_fcreatetime |  | fcreatetime |

---

## 售后申请单-反写记录表 t_pur_request_wb

- **表名称：** 售后申请单-反写记录表
- **表名：** t_pur_request_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_request_wb_pkey |  | fentryid |

---

## 售后申请单-多语言表 t_pur_request_l

- **表名称：** 售后申请单-多语言表
- **表名：** t_pur_request_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_request_l_fid |  | fid,flocaleid |
| 2 | t_pur_request_l_pkey |  | fpkid |

---

## 售后申请单-主表 t_pur_request

- **表名称：** 售后申请单-主表
- **表名：** t_pur_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 取件地址 | varchar | 80 |  | √ | ' ' | 取件地址 |
| 3 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 4 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 5 | frettype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :入库退货 2 :收货退货 |
| 6 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 8 | freplenishtype | 补货方式 | bpchar | 1 |  | √ | ' ' | 补货方式,枚举: 1 :按源单补货 2 :新补货订单 3 :不再补货 |
| 9 | fpurorderno | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 10 | fsumamount | fsumamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fphone | 联系电话（手机） | varchar | 80 |  | √ | ' ' | 联系电话（手机） |
| 13 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 15 | femail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 16 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 17 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | fpersonid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsettleorgid | 核算公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 21 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 22 | flinkman | 退货联系人 | varchar | 80 |  | √ | ' ' | 退货联系人 |
| 23 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 24 | fcardnumber | 银行卡号 | varchar | 80 |  | √ | ' ' | 银行卡号 |
| 25 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fmalorderno | 商城订单号 | varchar | 80 |  | √ | ' ' | 商城订单号 |
| 27 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 28 | fbilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 29 | fpickwaretype | fpickwaretype | bpchar | 10 |  | √ | ' ' |  |
| 30 | fpayeesupid | fpayeesupid | int8 | 64 |  | √ | 0 |  |
| 31 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 32 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 5 :西域商城 6 :晨光商城 4 :得力商城 7 :京东工业品 8 :鑫方盛 |
| 33 | fadmindivision | 取件区 | varchar | 50 |  | √ | ' ' | 取件区 |
| 34 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 35 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 37 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fcardusername | 持卡人姓名 | varchar | 80 |  | √ | ' ' | 持卡人姓名 |
| 39 | finvoicesupid | finvoicesupid | int8 | 64 |  | √ | 0 |  |
| 40 | fbank | 银行 | varchar | 80 |  | √ | ' ' | 银行,枚举: 01 :中国银行 02 :工商银行 03 :建设银行 04 :交通银行 05 :华夏银行 06 :招商银行 07 :光大银行 08 :农业银行 09 :民生银行 10 :兴业银行 12 :北京银行 13 :浦发银行 14 :上海银行 15 :平安银行 16 :邮政储蓄银行 |
| 41 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fdelisupid | fdelisupid | int8 | 64 |  | √ | 0 |  |
| 43 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 44 | fsumqty | fsumqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 45 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 46 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 47 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 48 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 E :取消 F :完成 G :自动确认 |
| 49 | fsumtaxamount | fsumtaxamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 50 | fsumtax | fsumtax | numeric | 19 | 6 | √ | 0.000000 |  |
| 51 | fexchrate | fexchrate | numeric | 19 | 6 | √ | 1.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_request_pkey |  | fid |
| 2 | idx_pur_request_fbillno |  | fbillno |
| 3 | idx_pur_request_fbizpartnerid |  | fbizpartnerid |
| 4 | idx_pur_request_fbilldate |  | fbilldate |

---

## 关联子实体-子表 t_pur_request_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_request_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_request_lk_fk |  | fid |
| 2 | t_pur_request_lk_pkey |  | fpkid |

---

## 售后申请单-关联追踪表 t_pur_request_tc

- **表名称：** 售后申请单-关联追踪表
- **表名：** t_pur_request_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_request_tc_pkey |  | fid |
| 2 | idx_pur_request_tc_tbill |  | ftbillid |
| 3 | idx_pur_request_tc_tid |  | ftid |

---

## 电商服务分录-子表 t_pur_requestasentry

- **表名称：** 电商服务分录-子表
- **表名：** t_pur_requestasentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fafservicebillid | 服务单 | int8 | 64 |  | √ | 0 | 电商售后服务单 pbd_eafservicebill |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | inx_pur_requestasentry |  | fid |
| 2 | t_pur_requestasentry_pkey |  | fentryid |

---

## 商品详情分录-分表 t_pur_requestentry_a

- **表名称：** 商品详情分录-分表
- **表名：** t_pur_requestentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | floctax | numeric | 19 | 6 | √ | 0.000000 |  |
| 3 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品管理 pmm_prodmanage |
| 5 | fecorder | 电商订单 | int8 | 64 |  | √ | 0 | 京东订单 pbd_jdorder |
| 6 | fbasicqty | fbasicqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fasstunitid | fasstunitid | int8 | 64 |  | √ | 0 |  |
| 8 | fpickwaretype | 取件方式 | varchar | 10 |  | √ | ' ' | 取件方式,枚举: 4 :上门取件 7 :客户送货 40 :客户发货 1 :客户自发 61 :晨光上门取件 62 :晨光第三方物流 10 :上门取货 20 :客户邮寄 |
| 9 | fsumreturnqty | 关联退货数量 | numeric | 19 | 6 | √ | 0.000000 | 关联退货数量 |
| 10 | fbasicunitid | fbasicunitid | int8 | 64 |  | √ | 0 |  |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | floctaxamount | floctaxamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fasstqty | fasstqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 14 | fjdchildorderid | 京东子订单号 | varchar | 50 |  | √ | ' ' | 京东子订单号 |
| 15 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 16 | facttaxprice | facttaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 18 | fretreasoncode | 退货原因项 | varchar | 10 |  | √ | ' ' | 退货原因项,枚举: 0301 :无理由退货 0101 :商品质量问题 0103 :成套商品部分少发 0105 :商品过期/接近有效期 0106 :商品名称一致，但与网页介绍不符 0201 :未按约定时间上门 0202 :服务态度差 0203 :商品发错 0204 :对收费价格不满 0205 :安装/维修技能差 0401 :价格波动 10 :商品质量问题 70 :多买/买错不想要了 80 :到货物流破损 90 :发票问题 100 :未按约定时间送货 110 :其它原因 120 :收到商品与网站展示不符 130 :客户原因无理由退货 140 :资质问题 |
| 19 | factprice | factprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 21 | freturntype | 售后类型 | varchar | 10 |  | √ | ' ' | 售后类型,枚举: 1 :退货 2 :换货 3 :维修 10 :退货 20 :换货 30 :维修 4 :退货 5 :换货 |
| 22 | flocamount | flocamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | fservicetime | 服务时间 | varchar | 50 |  | √ | ' ' | 服务时间 |
| 24 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fpcbillid | fpcbillid | varchar | 50 |  | √ | ' ' |  |
| 27 | fshoprettype | 补货方式 | varchar | 10 |  | √ | ' ' | 补货方式,枚举: 1 :不再补货 |
| 28 | fpcentryid | fpcentryid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_requestentry_a_fpoid |  | fpoentryid |
| 2 | t_pur_requestentry_a_pkey |  | fentryid |
| 3 | idx_pur_requestentry_a_fid |  | fid |

---

## 关联子实体-子表 t_pur_requestentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_requestentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | fqty_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_requestentry_lk_pkey |  | fpkid |
