# 条码扫描记录-barcm_scanrecord

## 扫描信息-子表 t_barcm_scanentry

- **表名称：** 扫描信息-子表
- **表名：** t_barcm_scanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsalorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsaldeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbarcode | 条码 | varchar | 512 |  | √ | ' ' | 条码 |
| 8 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 9 | finkeepertype | 入库保管者类型 | varchar | 80 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | finownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fpuroperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 13 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 19 | fsaloperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 20 | fauxqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 21 | fmaterialinvid | 物料编号(库存) | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 22 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 25 | fininvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 26 | fcustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 27 | frequserid | 领用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fprdorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | foutkeepertype | 出库保管者类型 | varchar | 80 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 31 | fprddeptid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | finwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 33 | fsaloprgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 34 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | finkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | finlotnumbertext | 入库批号文本 | varchar | 255 |  | √ | ' ' | 入库批号文本 |
| 38 | finlotnumberid | 入库批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 39 | foutlocationid | 出库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 40 | foutownertype | 出库货主类型 | varchar | 80 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 41 | fininvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 42 | finlocationid | 入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 43 | fprdqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 44 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | foutwarehouseid | 出库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 46 | fpuroprgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 47 | fmtrlinputway | 主条码录入方式 | bpchar | 1 |  | √ | ' ' | 主条码录入方式,枚举: A :记录 B :扫描 |
| 48 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 49 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 50 | finownertype | 入库货主类型 | varchar | 80 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |

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
| 2 | fconbcmainfilesubid | 容器条码主档 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbuildstate | 目标单处理状态 | bpchar | 1 |  | √ | ' ' | 目标单处理状态,枚举: A :未生成 B :已生成 C :已验收 D :已盘点 |
| 7 | ftargetbillno | 目标单据编号 | varchar | 80 |  | √ | ' ' | 目标单据编号 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fisredfield | 是否红字 | bpchar | 1 |  | √ | '0' | 是否红字 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fscanmodelid | 扫描模型 | int8 | 64 |  | √ | 0 | 条码扫描模型 barcm_scanningmodel |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 3 | fbizobjectid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 4 | fsrcentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 5 | fsrcbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fsrcauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fsrcmaterielid | 物料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
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
| 5 | fconbcmainfileid | 容器条码主档 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
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
| 2 | fprdunitidetysubid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | finlotnumberetysubid | 入库批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 4 | fbcmainfilesubid | 条码主档 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 5 | fcheckqtyetysub | 复盘数量 | numeric | 23 | 10 | √ | null | 复盘数量 |
| 6 | fauxunitetysubid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | finvmaterialsubid | 物料编码(库存) | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 8 | fsncommentetysub | 序列号备注 | varchar | 255 |  | √ | ' ' | 序列号备注 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fauxunit2etysubid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | finlotnumbertextetysub | 入库批号文本 | varchar | 255 |  | √ | ' ' | 入库批号文本 |
| 12 | foutlotnumberetysubid | 出库批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 13 | fproducedateetysub | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 14 | finvunitetysubid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | finvqtyetysub | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fauxqtyetysub | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 17 | foutlotnumbertextetysub | 出库批号文本 | varchar | 255 |  | √ | ' ' | 出库批号文本 |
| 18 | fscandatetimeetysub | 录入日期 | timestamp | 0 |  |  | null | 录入日期 |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | fcheckqtyunit2nd2etysub | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 21 | fsnnumberetysub | 序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 22 | fcheckbaseqtyetysub | 复盘基本数量 | numeric | 23 | 10 | √ | 0 | 复盘基本数量 |
| 23 | fexpirydateetysub | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 24 | fbaseqtyetysub | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 25 | fcheckqtyunit2ndetysub | 复盘辅助数量 | numeric | 23 | 10 | √ | 0 | 复盘辅助数量 |
| 26 | fconunitsubid | 容器明细单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fprdqtyetysub | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 28 | fmversionsubid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 29 | fbaseunitetysubid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fbarcodesub | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 31 | fauxptyetysubid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 32 | fsnnumbertextetysub | 序列号文本 | varchar | 80 |  | √ | ' ' | 序列号文本 |
| 33 | fbcrulesubid | 条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 34 | fconaccountsub | 容器明细数量 | numeric | 23 | 10 | √ | 0 | 容器明细数量 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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
| 2 | finprojectid | 入库项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 3 | fscandatetime | 录入日期 | timestamp | 0 |  |  | null | 录入日期 |
| 4 | fqualitystatus | 质量状态 | bpchar | 1 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不合格品 C :待检品 D :报废品 |
| 5 | foutinvdeptid | 出库库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | frecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | foutlotnumbertext | 出库批号文本 | varchar | 255 |  | √ | ' ' | 出库批号文本 |
| 10 | foutlotnumberid | 出库批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 11 | fbcruleid | 条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 12 | fmversionetyid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | fcheckqtyunit2ndety | 复盘辅助数量 | numeric | 23 | 10 | √ | 0 | 复盘辅助数量 |
| 14 | ftransininvorgid | 调入库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fininvdeptid | 入库库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fcheckqtyety | 复盘数量 | numeric | 23 | 10 | √ | 0 | 复盘数量 |
| 17 | fbcmainfileid | 条码主档 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 18 | fmanuentry | 生产工单行号 | varchar | 80 |  | √ | ' ' | 生产工单行号 |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 21 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | 班次 mpdm_workshifts |
| 22 | fcheckbaseqtyety | 复盘基本数量 | numeric | 23 | 10 | √ | 0 | 复盘基本数量 |
| 23 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fchecker2ndid | 复盘人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 25 | fcommentety | 行备注 | varchar | 255 |  | √ | ' ' | 行备注 |
| 26 | fcheckerid | 盘点人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 27 | frecoperatorid | 收料员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 28 | fispresent | 是否赠品 | bpchar | 1 |  | √ | ' ' | 是否赠品 |
| 29 | ftransoutinvorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fininvoperatorid | 入库库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 31 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: A :联产品 B :副产品 C :主产品 |
| 32 | foutinvoprgroupid | 出库库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 33 | ftransit | 在途归属 | bpchar | 1 |  | √ | ' ' | 在途归属,枚举: A :调出货主 B :调入货主 |
| 34 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 |
| 35 | freturnmaterialtype | 生产退料类型 | bpchar | 1 |  | √ | ' ' | 生产退料类型,枚举: A :良品退料 B :来料不良退料 C :作业不良退料 |
| 36 | ftranstype | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 37 | fscanuserid | 录入人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fpurreturnmtrltype | 采购退料类型 | bpchar | 1 |  | √ | ' ' | 采购退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 39 | frecoprgroupid | 收料组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 40 | fpriceety | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 41 | foutinvoperatorid | 出库库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 42 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fmanubill | 生产工单编号 | varchar | 80 |  | √ | ' ' | 生产工单编号 |
| 44 | famountety | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 46 | fininvoprgroupid | 入库库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 47 | fsettlecurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 48 | foutprojectid | 出库项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |

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
| 4 | freplenishmentreasonid | 补料原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 5 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fconsumingorgid | 领用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fcusmaterialidety | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 9 | fscrappedbsqtyety | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 10 | fisoutdeductmqty | 出库扣减主档数量 | bpchar | 1 |  | √ | '0' | 出库扣减主档数量 |
| 11 | ftransitownertype | 在途货主类型 | varchar | 80 |  | √ | ' ' | 在途货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | fsupplyownerid | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcontainerbarcode | 容器条码 | bpchar | 1 |  | √ | '0' | 容器条码 |
| 14 | fauxqty2 | 辅助单位数量(2) | numeric | 23 | 10 | √ | 0 | 辅助单位数量(2) |
| 15 | ftransitownerid | 在途货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fcheckqtyunit2ndety2 | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 17 | ftopconbcmainfileid | 顶层容器条码 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 18 | fisovertrans | 调拨完成 | bpchar | 1 |  | √ | ' ' | 调拨完成 |
| 19 | fscrappedqtyety | 报废库存数量 | numeric | 23 | 10 | √ | 0 | 报废库存数量 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fsupplyownertype | 供应货主类型 | varchar | 80 |  | √ | ' ' | 供应货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 22 | ffacard | 资产卡片id | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |

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
| 4 | ftaroriauxunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | ftaroribaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | foriauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | ftaroriauxqty | 初始辅助单位数量 | numeric | 23 | 10 | √ | 0 | 初始辅助单位数量 |
| 8 | ftaroriauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fremainauxqty2 | 剩余辅助单位(2)数量 | numeric | 23 | 10 | √ | 0 | 剩余辅助单位(2)数量 |
| 11 | ftaroriprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | ftaroriqty | 初始库存单位数量 | numeric | 23 | 10 | √ | 0 | 初始库存单位数量 |
| 13 | ftaroriunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fremainauxqty | 剩余辅助单位数量 | numeric | 23 | 10 | √ | 0 | 剩余辅助单位数量 |
| 15 | fremainbaseqty | 剩余基本单位数量 | numeric | 23 | 10 | √ | 0 | 剩余基本单位数量 |
| 16 | ftarorientryid | 目标单原始分录ID | int8 | 64 |  | √ | 0 | 目标单原始分录ID |
| 17 | fsrcids | 原单ID | varchar | 255 |  | √ | ' ' | 原单ID |
| 18 | forimversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | ftarorimaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
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
