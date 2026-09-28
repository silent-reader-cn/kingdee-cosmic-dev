# 验收申请处理-pur_accept_apply

## 验收申请分录-子表 t_pur_saloutstockentry

- **表名称：** 验收申请分录-子表
- **表名：** t_pur_saloutstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | frowlogstatus | 行物流状态 | bpchar | 1 |  | √ | ' ' | 行物流状态,枚举: C :待收货 D :部分收货 E :已收货 F :部分入库 G :已入库 H :已拒收 |
| 9 | frcvpersonname | 收货人 | varchar | 200 |  | √ | ' ' | 收货人 |
| 10 | fautorecbillno | 验收单号 | varchar | 80 |  | √ | ' ' | 验收单号 |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 12 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 13 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 14 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 19 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 20 | frejectreason | 不合格原因 | varchar | 255 |  | √ | ' ' | 不合格原因 |
| 21 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 23 | frcvpersontel | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 24 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 25 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 26 | flot1 | flot1 | varchar | 50 |  | √ | ' ' |  |
| 27 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 28 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 29 | ftraceno | ftraceno | int8 | 64 |  | √ | 0 |  |
| 30 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 31 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 |
| 37 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 38 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 39 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 40 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 41 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 42 | fdeliaddr | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |
| 43 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmaterialinventory | fmaterialinventory | int8 | 64 |  | √ | 0 |  |
| 45 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 46 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 C :折扣额 |
| 47 | fdsbillno | fdsbillno | varchar | 80 |  | √ | ' ' |  |
| 48 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 50 | frejectqty | 不合格数量 | numeric | 23 | 10 | √ | 0.000000 | 不合格数量 |
| 51 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 52 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | ' ' | 对账状态,枚举: A :正常 B :已关闭 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_salout_fid_fseq |  | fid,fseq |
| 2 | t_pur_saloutstockentry_pkey |  | fentryid |
| 3 | idx_pur_salout_fmaterialid |  | fmaterialid |

---

## 附件-附件表 t_pur_salrejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_salrejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_salrejectreasonatt |  | fpkid |
| 2 | idx_salrejectatt_fbasedataid |  | fbasedataid |

---

## 验收申请处理-分表 t_pur_saloutstock_a

- **表名称：** 验收申请处理-分表
- **表名：** t_pur_saloutstock_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisinitial | fisinitial | bpchar | 1 |  | √ | ' ' |  |
| 6 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | frejectreson | 打回原因 | varchar | 512 |  | √ | ' ' | 打回原因 |
| 10 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 15 | fsrcbilltype | fsrcbilltype | bpchar | 1 |  | √ | ' ' |  |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_saloutstock_a_ftime |  | fcreatetime |
| 2 | t_pur_saloutstock_a_pkey |  | fid |

---

## 验收申请处理-多语言表 t_pur_saloutstock_l

- **表名称：** 验收申请处理-多语言表
- **表名：** t_pur_saloutstock_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_saloutstock_l_fid |  | fid,flocaleid |
| 2 | t_pur_saloutstock_l_pkey |  | fpkid |

---

## 验收申请分录-分表 t_pur_saloutstockentry_a

- **表名称：** 验收申请分录-分表
- **表名：** t_pur_saloutstockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 23 | 10 | √ | 0.000000 | 关联对账数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fdsbillid | fdsbillid | varchar | 80 |  | √ | ' ' |  |
| 9 | fsumreceiptqty | 关联收货数量 | numeric | 23 | 10 | √ | 0.000000 | 关联收货数量 |
| 10 | fsumaccepttaxamount | 已验收金额 | numeric | 23 | 10 | √ | 0 | 已验收金额 |
| 11 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 13 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 14 | fsumreceiptbaseqty | fsumreceiptbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 16 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 17 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 18 | fsuminstockbaseqty | fsuminstockbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 20 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 21 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 22 | fdsentryid | fdsentryid | varchar | 80 |  | √ | ' ' |  |
| 23 | fsuminstockqty | 关联入库数量 | numeric | 23 | 10 | √ | 0.000000 | 关联入库数量 |
| 24 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 金额(本位币) |
| 25 | fsumcheckamt | 关联对账金额 | numeric | 23 | 10 | √ | 0.000000 | 关联对账金额 |
| 26 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 29 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_saloutentry_a_fid |  | fid |
| 2 | idx_pur_saloutentry_a_fpoid |  | fpoentryid |
| 3 | t_pur_saloutstockentry_a_pkey |  | fentryid |
| 4 | idx_pur_soentry_a_srcentryid |  | fsrcentryid |
| 5 | idx_pur_soentry_a_srcbilid |  | fsrcbillid |

---

## 验收申请处理-主表 t_pur_saloutstock

- **表名称：** 验收申请处理-主表
- **表名：** t_pur_saloutstock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 期望验收日期 | timestamp | 0 |  |  | null | 期望验收日期 |
| 3 | freqorgid | 验收组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | foperatorid | 联系人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 6 | forgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | ftarbilltype | 本单类型 | bpchar | 1 |  | √ | '1' | 本单类型,枚举: 1 :发货单 2 :验收申请 |
| 10 | fpayeesupid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 12 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 13 | fdeliaddr | 发货地址 | varchar | 255 |  | √ | ' ' | 发货地址 |
| 14 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 21 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: C :待收货 D :部分收货 E :已收货 F :部分入库 G :已入库 H :已拒收 |
| 22 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 23 | finvoicesupid | 开票供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 24 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fdelisupid | 送货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 32 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 33 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 34 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 35 | fsumtaxamount | 申请金额 | numeric | 23 | 10 | √ | 0.000000 | 申请金额 |
| 36 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 38 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 39 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |
| 40 | fqcodeurl | fqcodeurl | varchar | 255 |  | √ | ' ' |  |
| 41 | fcontacterid | 业务员 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 42 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_saloutstock_pkey |  | fid |
| 2 | idx_pur_saloutstock_fbillno |  | fbillno |
| 3 | idx_pur_saloutstock_fbizid |  | fbizpartnerid |
| 4 | idx_pur_saloutstock_fbilldate |  | fbilldate,fbizpartnerid |
