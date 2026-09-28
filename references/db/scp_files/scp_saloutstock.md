# 发货处理-scp_saloutstock

## 销售发货分录-子表 t_pur_saloutstockentry

- **表名称：** 销售发货分录-子表
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
| 10 | fautorecbillno | 自动生成收货单号 | varchar | 80 |  | √ | ' ' | 自动生成收货单号 |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 12 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 13 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 14 | fpurorgid | 客户 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 19 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 20 | frejectreason | 不合格原因 | varchar | 255 |  | √ | ' ' | 不合格原因 |
| 21 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 23 | frcvpersontel | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 24 | flotid | 批号(废弃) | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 25 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 26 | flot1 | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 27 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 28 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 29 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 30 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 31 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 37 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 38 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 39 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 40 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 41 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 42 | fdeliaddr | 收货地址 | varchar | 255 |  | √ | ' ' | 收货地址 |
| 43 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmaterialinventory | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 45 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 46 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 C :折扣额 |
| 47 | fdsbillno | 交货计划号 | varchar | 80 |  | √ | ' ' | 交货计划号 |
| 48 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
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
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 2 | ftaxamount | ftaxamount | numeric | 23 | 10 |  | null |  |
| 3 | ftaxamount_old | ftaxamount_old | numeric | 23 | 10 |  | null |  |
| 4 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 7 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |
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

## 发货处理-反写记录表 t_pur_saloutstock_wb

- **表名称：** 发货处理-反写记录表
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

## 发货处理-分表 t_pur_saloutstock_a

- **表名称：** 发货处理-分表
- **表名：** t_pur_saloutstock_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisinitial | 期初发货单 | bpchar | 1 |  | √ | ' ' | 期初发货单 |
| 6 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | frejectreson | 打回原因 | varchar | 512 |  | √ | ' ' | 打回原因 |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 15 | fsrcbilltype | 下推源单类型 | bpchar | 1 |  | √ | ' ' | 下推源单类型,枚举: 1 :订单查询 2 :送货通知 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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

## 发货处理-多语言表 t_pur_saloutstock_l

- **表名称：** 发货处理-多语言表
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

## 发货处理-关联追踪表 t_pur_saloutstock_tc

- **表名称：** 发货处理-关联追踪表
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

## 用料信息-子表 t_pur_saloutstockentry_s

- **表名称：** 用料信息-子表
- **表名：** t_pur_saloutstockentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 2 | fconsumesubbaseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 3 | fconsumesubqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 4 | fsubbaseqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsubunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fsubsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 8 | fsubqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 9 | fsubsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 10 | fsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fsubconfiguredcodeid | 用料配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 12 | fsubsrcbillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 13 | fcurconsumesubqty | 本次消耗数量 | numeric | 23 | 10 | √ | 0 | 本次消耗数量 |
| 14 | fsubmaterialid | 用料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fisbackflushnew | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fcurconsumesubbaseqty | 本次消耗基本数量 | numeric | 23 | 10 | √ | 0 | 本次消耗基本数量 |
| 19 | fsubsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 20 | fsubmaterialnametext | 用料名称 | varchar | 255 |  | √ | ' ' | 用料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_saloutstockentry_s_fid |  | fentryid,fseq |
| 2 | pk_t_pur_saloutstockentry_s |  | fdetailid |

---

## 销售发货分录-分表 t_pur_saloutstockentry_o

- **表名称：** 销售发货分录-分表
- **表名：** t_pur_saloutstockentry_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foproperation | 工序编码 | varchar | 80 |  | √ | ' ' | 工序编码 |
| 3 | fmftorderid | 委外工单ID | varchar | 50 |  | √ | ' ' | 委外工单ID |
| 4 | fmftsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 5 | fmftorderentryid | 委外工单行ID | varchar | 50 |  | √ | ' ' | 委外工单行ID |
| 6 | foprdescription | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 8 | fpayentrychangetype | fpayentrychangetype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fmftdirect | 委外直送 | bpchar | 1 |  | √ | '0' | 委外直送 |
| 10 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 11 | foproperationname | 工序名称 | varchar | 100 |  | √ | ' ' | 工序名称 |
| 12 | foprentryid | 工序计划工序号ID | varchar | 50 |  | √ | ' ' | 工序计划工序号ID |
| 13 | ftechno | 工序计划编码 | varchar | 80 |  | √ | ' ' | 工序计划编码 |
| 14 | foproperationid | 工序ID | varchar | 50 |  | √ | ' ' | 工序ID |
| 15 | foprentryseq | 工序计划工序号 | varchar | 20 |  | √ | ' ' | 工序计划工序号 |
| 16 | fmftorderentryseq | 委外工单分录序号 | varchar | 20 |  | √ | ' ' | 委外工单分录序号 |
| 17 | ftechid | 工序计划ID | varchar | 50 |  | √ | ' ' | 工序计划ID |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 20 | fprocessseq | 工序计划序列号 | varchar | 50 |  | √ | ' ' | 工序计划序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_saloutsentry_o_fid |  | fid |
| 2 | pk_pur_saloutstockentry_o |  | fentryid |

---

## 销售发货分录-分表 t_pur_saloutstockentry_a

- **表名称：** 销售发货分录-分表
- **表名：** t_pur_saloutstockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 23 | 10 | √ | 0.000000 | 关联对账数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fdsbillid | 交货计划单据ID | varchar | 80 |  | √ | ' ' | 交货计划单据ID |
| 9 | fsumreceiptqty | 关联收货数量 | numeric | 23 | 10 | √ | 0.000000 | 关联收货数量 |
| 10 | fsumaccepttaxamount | fsumaccepttaxamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 13 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 14 | fsumreceiptbaseqty | 关联基本收货数量 | numeric | 23 | 10 | √ | 0 | 关联基本收货数量 |
| 15 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 16 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 17 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 18 | fsuminstockbaseqty | 关联基本入库数量 | numeric | 23 | 10 | √ | 0 | 关联基本入库数量 |
| 19 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 20 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 21 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 22 | fdsentryid | 交货计划分录ID | varchar | 80 |  | √ | ' ' | 交货计划分录ID |
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
| 8 | fsupplierid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 pur_logsupplier](../pbd_files/pur_logsupplier.md) |
| 9 | frecphone | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |

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

## 发货处理-主表 t_pur_saloutstock

- **表名称：** 发货处理-主表
- **表名：** t_pur_saloutstock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 预计到货日期 | timestamp | 0 |  |  | null | 预计到货日期 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 6 | forgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | ftarbilltype | 本单类型 | bpchar | 1 |  | √ | '1' | 本单类型,枚举: 1 :发货单 2 :验收申请 |
| 10 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 12 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 13 | fdeliaddr | 详细收货地址 | varchar | 255 |  | √ | ' ' | 详细收货地址 |
| 14 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 17 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :草稿 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 21 | flogstatus | 物流状态 | bpchar | 1 |  | √ | ' ' | 物流状态,枚举: C :待收货 D :部分收货 E :已收货 F :部分入库 G :已入库 H :已拒收 |
| 22 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 23 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 24 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fdelisupid | 发货方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 32 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 33 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 34 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 35 | fsumtaxamount | 应收金额 | numeric | 23 | 10 | √ | 0.000000 | 应收金额 |
| 36 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 38 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 39 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |
| 40 | fqcodeurl | 二维码URL | varchar | 255 |  | √ | ' ' | 二维码URL |
| 41 | fcontacterid | 供应商业务员 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
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
