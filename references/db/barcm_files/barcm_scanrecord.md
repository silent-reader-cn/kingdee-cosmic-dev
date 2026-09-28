# 条码扫描记录-barcm_scanrecord

## 扫描信息-子表 t_barcm_scanentry

- **表名称：** 扫描信息-子表
- **表名：** t_barcm_scanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsalorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsaldeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbarcode | 条码 | varchar | 512 |  | √ | ' ' | 条码 |
| 8 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 9 | finkeepertype | 入库保管者类型 | varchar | 80 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | fdamageqtyety | 采购损耗库存数量 | numeric | 23 | 10 | √ | 0 | 采购损耗库存数量 |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | finownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fpuroperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 14 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 20 | fsaloperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 21 | fauxqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 22 | fmaterialinvid | 物料编号(库存) | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 23 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 26 | fininvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 27 | fcustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 28 | frequserid | 领用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fprdorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | foutkeepertype | 出库保管者类型 | varchar | 80 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 32 | fprddeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | finwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fsaloprgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 35 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fdamagebaseqtyety | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 37 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | finkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | finlotnumbertext | 入库批号文本 | varchar | 255 |  | √ | ' ' | 入库批号文本 |
| 40 | finlotnumberid | 入库批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 41 | foutlocationid | 出库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 42 | foutownertype | 出库货主类型 | varchar | 80 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 43 | fininvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 44 | finlocationid | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 45 | fprdqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 46 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | foutwarehouseid | 出库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 48 | fpuroprgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 49 | fmtrlinputway | 主条码录入方式 | bpchar | 1 |  | √ | ' ' | 主条码录入方式,枚举: A :记录 B :扫描 |
| 50 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 51 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 52 | finownertype | 入库货主类型 | varchar | 80 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanentry |  | fentryid |
| 2 | idx_barcm_scanentry_fid |  | fid |

---

## 容器条码清单（作废，改成单据体）-子表 t_barcm_conbclist

- **表名称：** 容器条码清单（作废，改成单据体）-子表
- **表名：** t_barcm_conbclist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconbarcodesub | 容器条码 | varchar | 255 |  | √ | ' ' | 容器条码 |
| 2 | fconbcmainfilesubid | 容器条码主档 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fscaninfoentryid | 扫描信息行ID | int8 | 64 |  | √ | 0 | 扫描信息行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_conbclist |  | fdetailid |
| 2 | idx_barcm_conbclist_fid |  | fdetailid |

---

## 条码扫描记录-主表 t_barcm_scanrecord

- **表名称：** 条码扫描记录-主表
- **表名：** t_barcm_scanrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbuildstate | 目标单处理状态 | bpchar | 1 |  | √ | ' ' | 目标单处理状态,枚举: A :未生成 B :已生成 C :已验收 D :已盘点 |
| 7 | ftargetbillno | 目标单据编号 | varchar | 80 |  | √ | ' ' | 目标单据编号 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fisredfield | 是否红字 | bpchar | 1 |  | √ | '0' | 是否红字 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fscanmodelid | 扫描模型 | int8 | 64 |  | √ | 0 | [条码扫描模型 barcm_scanningmodel](../barcm_files/barcm_scanningmodel.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanrecord |  | fid |
| 2 | idx_barcm_scanrec_billno |  | fbillno |

---

## 源单信息-子表 t_barcm_scanrecsrcentry

- **表名称：** 源单信息-子表
- **表名：** t_barcm_scanrecsrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 3 | fbizobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fsrcentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 5 | fsrcbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fsrcauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fsrcmaterielid | 物料编号 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsrcentryseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanrecsrcentry |  | fentryid |
| 2 | idx_barcm_scansrcentry_fid |  | fid |

---

## 容器条码明细-多语言表 t_barcm_containerbcinfo_l

- **表名称：** 容器条码明细-多语言表
- **表名：** t_barcm_containerbcinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsncommentetysub | 序列号备注 | varchar | 255 |  | √ | ' ' | 序列号备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_containerbcinfo_l |  | fpkid |
| 2 | idx_barcm_contbci_fdtlid |  | fdetailid |

---

## 单据体-子表 t_barcm_scanrecexcentry

- **表名称：** 单据体-子表
- **表名：** t_barcm_scanrecexcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexctype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :跨组织创建主档 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fexcdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fexcinfo | 异常信息 | varchar | 512 |  | √ | ' ' | 异常信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanrecexcentry |  | fentryid |
| 2 | idx_barcm_scanrecexc_fid |  | fid |

---

## 容器条码清单-子表 t_barcm_conbclistety

- **表名称：** 容器条码清单-子表
- **表名：** t_barcm_conbclistety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconbarcode | 容器条码 | varchar | 512 |  | √ | ' ' | 容器条码 |
| 3 | ftopconbarcode | 顶层容器条码 | varchar | 512 |  | √ | ' ' | 顶层容器条码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconbcmainfileid | 容器条码主档 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_conbcliste_fid |  | fid |
| 2 | pk_t_barcm_conbclistety |  | fentryid |

---

## 容器条码明细-子表 t_barcm_containerbcinfo

- **表名称：** 容器条码明细-子表
- **表名：** t_barcm_containerbcinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fauxqty2etysub | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 2 | fprdunitidetysubid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | finlotnumberetysubid | 入库批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 4 | fbcmainfilesubid | 条码主档 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 5 | fcheckqtyetysub | 复盘数量 | numeric | 23 | 10 | √ | null | 复盘数量 |
| 6 | fauxunitetysubid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | finvmaterialsubid | 物料编码(库存) | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 8 | fsncommentetysub | 序列号备注 | varchar | 255 |  | √ | ' ' | 序列号备注 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fauxunit2etysubid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | finlotnumbertextetysub | 入库批号文本 | varchar | 255 |  | √ | ' ' | 入库批号文本 |
| 12 | foutlotnumberetysubid | 出库批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 13 | fproducedateetysub | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 14 | finvunitetysubid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | finvqtyetysub | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fauxqtyetysub | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 17 | foutlotnumbertextetysub | 出库批号文本 | varchar | 255 |  | √ | ' ' | 出库批号文本 |
| 18 | fscandatetimeetysub | 录入日期 | timestamp | 0 |  |  | null | 录入日期 |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | foutlocationetysubid | 出库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 21 | fcheckqtyunit2nd2etysub | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 22 | fsnnumberetysub | 序列号 | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 23 | fcheckbaseqtyetysub | 复盘基本数量 | numeric | 23 | 10 | √ | 0 | 复盘基本数量 |
| 24 | fexpirydateetysub | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 25 | fbaseqtyetysub | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 26 | fcheckqtyunit2ndetysub | 复盘辅助数量 | numeric | 23 | 10 | √ | 0 | 复盘辅助数量 |
| 27 | fconunitsubid | 容器明细单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fprdqtyetysub | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 29 | fmversionsubid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 30 | fbaseunitetysubid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fbarcodesub | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 32 | fauxptyetysubid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 33 | fsnnumbertextetysub | 序列号文本 | varchar | 80 |  | √ | ' ' | 序列号文本 |
| 34 | foutwarehouseetysubid | 出库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 35 | finwarehouseetysubid | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 36 | finlocationetysubid | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 37 | fbcrulesubid | 条码规则 | int8 | 64 |  | √ | 0 | [条码规则 barcm_barcoderule](../barcm_files/barcm_barcoderule.md) |
| 38 | fconaccountsub | 容器明细数量 | numeric | 23 | 10 | √ | 0 | 容器明细数量 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_containerbcinfo_fid |  | fdetailid |
| 2 | pk_barcm_containerbcinfo |  | fdetailid |

---

## 匹配记录-子表 t_barcm_scanmatchentry

- **表名称：** 匹配记录-子表
- **表名：** t_barcm_scanmatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmatchqty | 匹配库存单位数量 | numeric | 23 | 10 | √ | 0 | 匹配库存单位数量 |
| 2 | fcopyentryid | 目标单复制分录ID | int8 | 64 |  | √ | 0 | 目标单复制分录ID |
| 3 | finitialentryid | 目标单原始分录ID | int8 | 64 |  | √ | 0 | 目标单原始分录ID |
| 4 | fmatchbaseqty | 匹配基本单位数量 | numeric | 23 | 10 | √ | 0 | 匹配基本单位数量 |
| 5 | fmatchauxqty | 匹配辅助单位数量 | numeric | 23 | 10 | √ | 0 | 匹配辅助单位数量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmatchauxqty2 | 匹配辅助单位(2)数量 | numeric | 23 | 10 | √ | 0 | 匹配辅助单位(2)数量 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fmatchprdqty | 匹配生产单位数量 | numeric | 23 | 10 | √ | 0 | 匹配生产单位数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanmatchentry |  | fdetailid |
| 2 | idx_barcm_scanmatch_entryid |  | fentryid |

---

## 扫描信息-分表 t_barcm_scanentry_a

- **表名称：** 扫描信息-分表
- **表名：** t_barcm_scanentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finprojectid | 入库项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | foutmpmtasknoetyid | 出库项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 4 | frecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | foutlotnumbertext | 出库批号文本 | varchar | 255 |  | √ | ' ' | 出库批号文本 |
| 6 | foutlotnumberid | 出库批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 7 | fcfmanubill | fcfmanubill | varchar | 50 |  | √ | ' ' |  |
| 8 | finlicenseno | 入库许可证 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 9 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 10 | fcheckbaseqtyety | 复盘基本数量 | numeric | 23 | 10 | √ | 0 | 复盘基本数量 |
| 11 | frecoperatorid | 收料员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 12 | fispresent | 是否赠品 | bpchar | 1 |  | √ | ' ' | 是否赠品 |
| 13 | foutinvoprgroupid | 出库库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 14 | ftransit | 在途归属 | bpchar | 1 |  | √ | ' ' | 在途归属,枚举: A :调出货主 B :调入货主 |
| 15 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 |
| 16 | freturnmaterialtype | 生产退料类型 | bpchar | 1 |  | √ | ' ' | 生产退料类型,枚举: A :良品退料 B :来料不良退料 C :作业不良退料 |
| 17 | ftranstype | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 18 | fscanuserid | 录入人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | frecoprgroupid | 收料组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 20 | fpriceety | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 21 | foutinvoperatorid | 出库库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 22 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fsettlecurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fscandatetime | 录入日期 | timestamp | 0 |  |  | null | 录入日期 |
| 26 | fcflineinfo | fcflineinfo | int8 | 64 |  | √ | 0 |  |
| 27 | fqualitystatus | 质量状态 | bpchar | 1 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不合格品 C :待检品 D :报废品 |
| 28 | foutinvdeptid | 出库库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 30 | fprocessplanety | 工序计划编号 | varchar | 50 |  | √ | ' ' | 工序计划编号 |
| 31 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 32 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 33 | fbcruleid | 条码规则 | int8 | 64 |  | √ | 0 | [条码规则 barcm_barcoderule](../barcm_files/barcm_barcoderule.md) |
| 34 | fmversionetyid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 35 | fcheckqtyunit2ndety | 复盘辅助数量 | numeric | 23 | 10 | √ | 0 | 复盘辅助数量 |
| 36 | ftransininvorgid | 调入库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fininvdeptid | 入库库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fprocessplanentryf7idety | 工序计划分录F7 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 39 | fcheckqtyety | 复盘数量 | numeric | 23 | 10 | √ | 0 | 复盘数量 |
| 40 | fbcmainfileid | 条码主档 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 41 | fmanuentry | 生产工单行号 | varchar | 80 |  | √ | ' ' | 生产工单行号 |
| 42 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 43 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 44 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 45 | fchecker2ndid | 复盘人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 46 | fcommentety | 行备注 | varchar | 512 |  | √ | ' ' | 行备注 |
| 47 | fcheckerid | 盘点人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 48 | ftransoutinvorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fininvoperatorid | 入库库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 50 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: A :联产品 B :副产品 C :主产品 |
| 51 | freceiveprojectetyid | 领用项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 52 | fprocessplanf7idety | 工序计划F7 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 53 | foutlicenseno | 出库许可证 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 54 | fpurreturnmtrltype | 采购退料类型 | bpchar | 1 |  | √ | ' ' | 采购退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 55 | fmanubill | 生产工单编号 | varchar | 80 |  | √ | ' ' | 生产工单编号 |
| 56 | famountety | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 57 | finmpmtasknoetyid | 入库项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 58 | fininvoprgroupid | 入库库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 59 | foutprojectid | 出库项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanentry_a |  | fentryid |
| 2 | idx_barcm_scanentrya_fid |  | fid |

---

## 扫描信息-分表 t_barcm_scanentry_b

- **表名称：** 扫描信息-分表
- **表名：** t_barcm_scanentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fneedtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 3 | ffreturntype | 受托退料类型 | bpchar | 1 |  | √ | ' ' | 受托退料类型,枚举: A :退料 B :退补料 |
| 4 | freplenishmentreasonid | 补料原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 5 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fconsumingorgid | 领用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fcusmaterialidety | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 9 | fscrappedbsqtyety | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 10 | fisoutdeductmqty | 出库扣减主档数量 | bpchar | 1 |  | √ | '0' | 出库扣减主档数量 |
| 11 | ftransitownertype | 在途货主类型 | varchar | 80 |  | √ | ' ' | 在途货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | fsupplyownerid | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcontainerbarcode | 容器条码 | bpchar | 1 |  | √ | '0' | 容器条码 |
| 14 | fauxqty2 | 辅助单位数量(2) | numeric | 23 | 10 | √ | 0 | 辅助单位数量(2) |
| 15 | ftransitownerid | 在途货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fcheckqtyunit2ndety2 | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 17 | ftopconbcmainfileid | 顶层容器条码 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 18 | fisovertrans | 调拨完成 | bpchar | 1 |  | √ | ' ' | 调拨完成 |
| 19 | fscrappedqtyety | 报废库存数量 | numeric | 23 | 10 | √ | 0 | 报废库存数量 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fsupplyownertype | 供应货主类型 | varchar | 80 |  | √ | ' ' | 供应货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 22 | fmtrlcontiscan | 物料连续扫描 | bpchar | 1 |  | √ | '0' | 物料连续扫描 |
| 23 | ffacard | 资产卡片id | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanentry_b |  | fentryid |
| 2 | idx_barcm_scanentryb_fid |  | fid |

---

## 单据体-多语言表 t_barcm_scanrecexcentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_barcm_scanrecexcentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexcinfo | 异常信息 | varchar | 512 |  | √ | ' ' | 异常信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_scanrecexcentry_l |  | fpkid |
| 2 | idx_barcm_screcexcl_fidflcid |  | fentryid,flocaleid |

---

## 目标单信息-子表 t_barcm_targenfoent

- **表名称：** 目标单信息-子表
- **表名：** t_barcm_targenfoent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaroribaseqty | 初始基本单位数量 | numeric | 23 | 10 | √ | 0 | 初始基本单位数量 |
| 3 | fsrcentryids | 原单分录ID | varchar | 255 |  | √ | ' ' | 原单分录ID |
| 4 | ftaroriauxunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | ftaroribaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | foriauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | ftaroriauxqty | 初始辅助单位数量 | numeric | 23 | 10 | √ | 0 | 初始辅助单位数量 |
| 8 | ftaroriauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fremainauxqty2 | 剩余辅助单位(2)数量 | numeric | 23 | 10 | √ | 0 | 剩余辅助单位(2)数量 |
| 11 | ftaroriprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | ftaroriqty | 初始库存单位数量 | numeric | 23 | 10 | √ | 0 | 初始库存单位数量 |
| 13 | ftaroriunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fremainauxqty | 剩余辅助单位数量 | numeric | 23 | 10 | √ | 0 | 剩余辅助单位数量 |
| 15 | fremainbaseqty | 剩余基本单位数量 | numeric | 23 | 10 | √ | 0 | 剩余基本单位数量 |
| 16 | ftarorientryid | 目标单原始分录ID | int8 | 64 |  | √ | 0 | 目标单原始分录ID |
| 17 | fsrcids | 原单ID | varchar | 255 |  | √ | ' ' | 原单ID |
| 18 | forimversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 19 | ftarorimaterialid | 物料编号 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 20 | ftaroriauxqty2 | 初始辅助单位(2)数量 | numeric | 23 | 10 | √ | 0 | 初始辅助单位(2)数量 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fremainprdqty | 剩余生产单位数量 | numeric | 23 | 10 | √ | 0 | 剩余生产单位数量 |
| 23 | ftaroriprdqty | 初始生产单位数量 | numeric | 23 | 10 | √ | 0 | 初始生产单位数量 |
| 24 | fremainqty | 剩余库存单位数量 | numeric | 23 | 10 | √ | 0 | 剩余库存单位数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_targenfoent |  | fentryid |
| 2 | idx_barcm_targen_fid |  | fid |
