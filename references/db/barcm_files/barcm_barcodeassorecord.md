# 条码关联记录-barcm_barcodeassorecord

## 单据体-子表 t_barcm_bcodeassordety

- **表名称：** 单据体-子表
- **表名：** t_barcm_bcodeassordety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fauxunitid2 | 辅助单位2 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | funitetyid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fsubbarcodeid | 子条码 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fauxqty2 | 辅助数量2 | numeric | 23 | 10 | √ | 0 | 辅助数量2 |
| 10 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcar_id |  | fid |
| 2 | pk_barcm_bcodeassordety |  | fentryid |

---

## 条码关联记录-多语言表 t_barcm_bcodeassorecord_l

- **表名称：** 条码关联记录-多语言表
- **表名：** t_barcm_bcodeassorecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcodeassorecord_l |  | fpkid |
| 2 | idx_barcm_bcar_idlc |  | fid,flocaleid |

---

## 条码关联记录-主表 t_barcm_bcodeassorecord

- **表名称：** 条码关联记录-主表
- **表名：** t_barcm_bcodeassorecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsplitoriqty | 拆分前原始数量 | numeric | 23 | 10 | √ | 0 | 拆分前原始数量 |
| 7 | fsplittotalnum | 拆出条码总个数 | int4 | 32 |  | √ | 0 | 拆出条码总个数 |
| 8 | fprinttemplateid | 条码打印模板 | int8 | 64 |  | √ | 0 | [维护打印模板 bos_manageprinttpl](../cts_files/bos_manageprinttpl.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsplitbcqty | 指定拆出单条码数量 | numeric | 23 | 10 | √ | 0 | 指定拆出单条码数量 |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fparentbarcodeid | 父条码 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 18 | fmemo | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fsplitbcnum | 指定拆出条码个数 | int4 | 32 |  | √ | 0 | 指定拆出条码个数 |
| 20 | fmaterialinvid | 物料编号 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 21 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 22 | fparentbcnum | 父条码个数 | int4 | 32 |  | √ | 0 | 父条码个数 |
| 23 | fsplitavaqty | 拆分前可用数量 | numeric | 23 | 10 | √ | 0 | 拆分前可用数量 |
| 24 | fassociationtype | 关联类型 | bpchar | 1 |  | √ | ' ' | 关联类型,枚举: A :按个数拆分 B :按包装规格拆分 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcodeassorecord |  | fid |
| 2 | idx_barcm_bcar_billno |  | fbillno |
