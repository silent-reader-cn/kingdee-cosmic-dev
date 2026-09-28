# 退货通知-scp_request

## 退货通知分录-子表 t_pur_requestentry

- **表名称：** 退货通知分录-子表
- **表名：** t_pur_requestentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretdate | 退货日期 | timestamp | 0 |  |  | null | 退货日期 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | flotnumber | flotnumber | varchar | 80 |  | √ | ' ' |  |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 12 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 14 | fpurtypeid | fpurtypeid | int8 | 64 |  | √ | 0 |  |
| 15 | fretreason | 退货原因 | varchar | 255 |  | √ | ' ' | 退货原因 |
| 16 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | fqty | 退货数量 | numeric | 19 | 6 | √ | 0.000000 | 退货数量 |
| 19 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 20 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 21 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 23 | fmaterialnewid | 补货物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 24 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 28 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | finvorgid | 退货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 33 | flotid | 批号 | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 34 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 35 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 36 | freplenishqty | 补货数量 | numeric | 19 | 6 | √ | 0.000000 | 补货数量 |
| 37 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 38 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 39 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
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

## 退货通知分录-分表 t_pur_requestentry_a

- **表名称：** 退货通知分录-分表
- **表名：** t_pur_requestentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 5 | fecorder | fecorder | int8 | 64 |  | √ | 0 |  |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fpickwaretype | fpickwaretype | varchar | 10 |  | √ | ' ' |  |
| 9 | fsumreturnqty | 关联退货数量 | numeric | 19 | 6 | √ | 0.000000 | 关联退货数量 |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 13 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 14 | fjdchildorderid | fjdchildorderid | varchar | 50 |  | √ | ' ' |  |
| 15 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 16 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 17 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 18 | fretreasoncode | fretreasoncode | varchar | 10 |  | √ | ' ' |  |
| 19 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 20 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 21 | freturntype | freturntype | varchar | 10 |  | √ | ' ' |  |
| 22 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 23 | fservicetime | fservicetime | varchar | 50 |  | √ | ' ' |  |
| 24 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 27 | fshoprettype | fshoprettype | varchar | 10 |  | √ | ' ' |  |
| 28 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

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

## 退货通知-主表 t_pur_request

- **表名称：** 退货通知-主表
- **表名：** t_pur_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 取件地址 | varchar | 80 |  | √ | ' ' | 取件地址 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | frettype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :库存退货 2 :暂收退货 |
| 6 | forgid | 退货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 8 | freplenishtype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货需补 2 :新补货订单 3 :退货不补 |
| 9 | fpurorderno | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 10 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fphone | 联系电话（手机） | varchar | 80 |  | √ | ' ' | 联系电话（手机） |
| 13 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 15 | femail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 16 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 17 | fsupplierid | 销售方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 19 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 21 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 22 | flinkman | 退货联系人 | varchar | 80 |  | √ | ' ' | 退货联系人 |
| 23 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 24 | fcardnumber | fcardnumber | varchar | 80 |  | √ | ' ' |  |
| 25 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fmalorderno | fmalorderno | varchar | 80 |  | √ | ' ' |  |
| 27 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 28 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 29 | fpickwaretype | 取件方式 | bpchar | 10 |  | √ | ' ' | 取件方式,枚举: 4 :上门取件 7 :客户送货 40 :客户发货 |
| 30 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 32 | fplatform | 单据来源 | bpchar | 1 |  | √ | ' ' | 单据来源,枚举: 0 :协同 1 :自建商城 2 :京东商城 3 :苏宁商城 5 :西域商城 6 :晨光商城 4 :得力商城 7 :京东工业品 8 :鑫方盛商城 |
| 33 | fadmindivision | fadmindivision | varchar | 50 |  | √ | ' ' |  |
| 34 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 35 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 37 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fcardusername | fcardusername | varchar | 80 |  | √ | ' ' |  |
| 39 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 40 | fbank | fbank | varchar | 80 |  | √ | ' ' |  |
| 41 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 43 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 45 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 46 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 47 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 48 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 F :完成 G :自动确认 |
| 49 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 50 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 51 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |

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

## 退货通知-分表 t_pur_request_a

- **表名称：** 退货通知-分表
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
| 8 | fecsource | fecsource | varchar | 80 |  | √ | ' ' |  |
| 9 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsupaddr | 销售方地址 | varchar | 255 |  | √ | ' ' | 销售方地址 |
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

## 退货通知-多语言表 t_pur_request_l

- **表名称：** 退货通知-多语言表
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
