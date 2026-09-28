# 期初发货-scp_saloutstock_initial

## 销售发货分录-子表 t_pur_saloutstockentry

- **表名称：** 销售发货分录-子表
- **表名：** t_pur_saloutstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | frowlogstatus | 行物流状态 | bpchar | 1 |  | √ | ' ' | 行物流状态,枚举: C :待收货 D :部分收货 E :已收货 F :部分入库 G :已入库 H :已拒收 |
| 9 | frcvpersonname | 收货人 | varchar | 200 |  | √ | ' ' | 收货人 |
| 10 | fautorecbillno | 自动生成收货单号 | varchar | 80 |  | √ | ' ' | 自动生成收货单号 |
| 11 | fqty | 期初数量 | numeric | 19 | 6 | √ | 0.000000 | 期初数量 |
| 12 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 13 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 14 | fpurorgid | 客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 16 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 19 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 20 | frejectreason | 不合格原因 | varchar | 255 |  | √ | ' ' | 不合格原因 |
| 21 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 23 | frcvpersontel | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 24 | flotid | 批号 | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 25 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 26 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 27 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 28 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 29 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 33 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 34 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 35 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 36 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 37 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 38 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 39 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 40 | fdeliaddr | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |
| 41 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 43 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 44 | fdsbillno | 交货计划号 | varchar | 80 |  | √ | ' ' | 交货计划号 |
| 45 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 47 | frejectqty | 不合格数量 | numeric | 19 | 6 | √ | 0.000000 | 不合格数量 |
| 48 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 49 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | ' ' | 对账状态,枚举: A :正常 B :已关闭 |

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

## 不合格明细-子表 t_pur_saloutstock_rej

- **表名称：** 不合格明细-子表
- **表名：** t_pur_saloutstock_rej

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 3 | finbillno | 入库或收货单号 | varchar | 255 |  | √ | ' ' | 入库或收货单号 |
| 4 | frejdate | 不合格日期 | timestamp | 0 |  |  | null | 不合格日期 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fpobillid | 采购订单ID | varchar | 50 |  | √ | ' ' | 采购订单ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | frejectreason | 不合格原因 | varchar | 255 |  | √ | ' ' | 不合格原因 |
| 10 | frejectqty | 不合格数量 | numeric | 19 | 6 | √ | 0.000000 | 不合格数量 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fpobillno | 采购订单号 | varchar | 255 |  | √ | ' ' | 采购订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_salout_rej_fid_fseq |  | fid,fseq |
| 2 | pk_t_pur_saloutstock_rej |  | fentryid |

---

## 关联子实体-子表 t_pur_saloutstockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_saloutstockentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 期初数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量_确认携带值 |
| 2 | ftaxamount | ftaxamount | numeric | 23 | 10 |  | null |  |
| 3 | ftaxamount_old | ftaxamount_old | numeric | 23 | 10 |  | null |  |
| 4 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 7 | fqty_old | 期初数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量_原始携带值 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_saloutstockentry_lk_pkey |  | fpkid |
| 2 | idx_pur_salestock_lk_fentryid |  | fentryid |

---

## 期初发货-反写记录表 t_pur_saloutstock_wb

- **表名称：** 期初发货-反写记录表
- **表名：** t_pur_saloutstock_wb

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
| 1 | t_pur_saloutstock_wb_pkey |  | fentryid |
| 2 | idx_pur_salout_wb_fidfseq |  | fid,fseq |

---

## 附件-附件表 t_pur_salrejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_salrejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
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

## 期初发货-分表 t_pur_saloutstock_a

- **表名称：** 期初发货-分表
- **表名：** t_pur_saloutstock_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisinitial | 期初发货单 | bpchar | 1 |  | √ | ' ' | 期初发货单 |
| 6 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | frejectreson | 打回原因 | varchar | 512 |  | √ | ' ' | 打回原因 |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 15 | fsrcbilltype | 下推源单类型 | bpchar | 1 |  | √ | ' ' | 下推源单类型,枚举: 1 :订单查询 2 :送货通知 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_saloutstock_a_pkey |  | fid |
| 2 | idx_pur_saloutstock_a_ftime |  | fcreatetime |

---

## 期初发货-多语言表 t_pur_saloutstock_l

- **表名称：** 期初发货-多语言表
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

## 期初发货-关联追踪表 t_pur_saloutstock_tc

- **表名称：** 期初发货-关联追踪表
- **表名：** t_pur_saloutstock_tc

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
| 1 | idx_pur_saloutstock_tc_tid |  | ftid |
| 2 | t_pur_saloutstock_tc_pkey |  | fid |
| 3 | idx_pur_saloutstock_tc_tbill |  | ftbillid |

---

## 销售发货分录-分表 t_pur_saloutstockentry_a

- **表名称：** 销售发货分录-分表
- **表名：** t_pur_saloutstockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 19 | 6 | √ | 0.000000 | 关联对账数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fdsbillid | 交货计划单据ID | varchar | 80 |  | √ | ' ' | 交货计划单据ID |
| 9 | fsumreceiptqty | 关联收货数量 | numeric | 19 | 6 | √ | 0.000000 | 关联收货数量 |
| 10 | fsumaccepttaxamount | fsumaccepttaxamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 13 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 14 | fsumreceiptbaseqty | 关联基本收货数量 | numeric | 23 | 10 | √ | 0 | 关联基本收货数量 |
| 15 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 16 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 17 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 18 | fsuminstockbaseqty | 关联基本入库数量 | numeric | 23 | 10 | √ | 0 | 关联基本入库数量 |
| 19 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 20 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 21 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 22 | fdsentryid | 交货计划分录ID | varchar | 80 |  | √ | ' ' | 交货计划分录ID |
| 23 | fsuminstockqty | 关联入库数量 | numeric | 19 | 6 | √ | 0.000000 | 关联入库数量 |
| 24 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 25 | fsumcheckamt | 关联对账金额 | numeric | 19 | 6 | √ | 0.000000 | 关联对账金额 |
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

## 物流信息-子表 t_pur_saloutstock_log

- **表名称：** 物流信息-子表
- **表名：** t_pur_saloutstock_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 3 | fdelidate | 预计到货日期 | timestamp | 0 |  |  | null | 预计到货日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flogbillno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 8 | fsupplierid | 物流公司 | int8 | 64 |  | √ | 0 | 物流公司 pur_logsupplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_saloutstock_log_pkey |  | fentryid |
| 2 | idx_pur_salout_log_fid_fseq |  | fid,fseq |
| 3 | idx_pur_salout_log_flogbillno |  | flogbillno |

---

## 期初发货-主表 t_pur_saloutstock

- **表名称：** 期初发货-主表
- **表名：** t_pur_saloutstock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 预计到货日期 | timestamp | 0 |  |  | null | 预计到货日期 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | foperatorid | 联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | forgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | ftarbilltype | 本单类型 | bpchar | 1 |  | √ | '1' | 本单类型,枚举: 1 :发货单 2 :验收申请 |
| 10 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 12 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 13 | fdeliaddr | 详细收货地址 | varchar | 255 |  | √ | ' ' | 详细收货地址 |
| 14 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 17 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :草稿 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 20 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: C :待收货 D :部分收货 E :已收货 F :部分入库 G :已入库 H :已拒收 |
| 21 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fdelisupid | 发货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 27 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 31 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 32 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 33 | fsumtaxamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 34 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 36 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 37 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 38 | fqcodeurl | 二维码URL | varchar | 255 |  | √ | ' ' | 二维码URL |
| 39 | fcontacterid | 业务员 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 40 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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
