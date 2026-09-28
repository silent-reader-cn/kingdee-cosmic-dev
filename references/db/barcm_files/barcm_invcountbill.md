# 条码盘点表-barcm_invcountbill

## 盘点扫描明细-子表 t_barcm_invcbdetentry

- **表名称：** 盘点扫描明细-子表
- **表名：** t_barcm_invcbdetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscanrecordid | 扫描记录id | int8 | 64 |  | √ | 0 | 扫描记录id |
| 3 | fscandatetime | 录入日期 | timestamp | 0 |  |  | null | 录入日期 |
| 4 | fscanrecordentryid | 扫描记录分录id | int8 | 64 |  | √ | 0 | 扫描记录分录id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbarcode | 条码 | varchar | 512 |  | √ | ' ' | 条码 |
| 7 | finvcountqty | 折算后数量 | numeric | 23 | 10 | √ | 0 | 折算后数量 |
| 8 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fmversionetyid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | finvqtyety | 扫描数量 | numeric | 23 | 10 | √ | 0 | 扫描数量 |
| 11 | fbcmainfileid | 条码主档 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 12 | finvunitety | 扫描计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fbaseunitety | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fscanrecord | fscanrecord | varchar | 80 |  | √ | ' ' |  |
| 16 | fauxqty2 | 辅助单位数量(2) | numeric | 23 | 10 | √ | 0 | 辅助单位数量(2) |
| 17 | fauxqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 18 | ftype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: A :初盘 B :复盘 |
| 19 | fauxptyety | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | finvcentryid | 盘点表分录id | int8 | 64 |  | √ | 0 | 盘点表分录id |
| 21 | fmaterialinvid | 物料编号 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 22 | fscanuserid | 录入人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | finvcountunit | 盘点表计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fbaseqtyety | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 26 | fscanrecordno | 条码扫描记录编号 | varchar | 80 |  | √ | ' ' | 条码扫描记录编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_invcbdetentry_fid |  | fid |
| 2 | pk_barcm_invcbdetentry |  | fentryid |

---

## 盘点扫描汇总-子表 t_barcm_invcbtoentry

- **表名称：** 盘点扫描汇总-子表
- **表名：** t_barcm_invcbtoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvctotalentryid | 盘点表分录id | int8 | 64 |  | √ | 0 | 盘点表分录id |
| 3 | fcountbaseqty | 盘点基本数量 | numeric | 23 | 10 | √ | 0 | 盘点基本数量 |
| 4 | fisopenserial | 启用序列号 | bpchar | 1 |  | √ | '0' | 启用序列号 |
| 5 | fcountbaseqtyacc | 账存基本数量 | numeric | 23 | 10 | √ | 0 | 账存基本数量 |
| 6 | fcountbaselossqty | 盘亏基本数量 | numeric | 23 | 10 | √ | 0 | 盘亏基本数量 |
| 7 | fcountqtyunit3rd | 盘点辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘点辅助数量(2) |
| 8 | fcountqtyunit2nd | 盘点辅助数量 | numeric | 23 | 10 | √ | 0 | 盘点辅助数量 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | finvcounttotqty | 折算后数量 | numeric | 23 | 10 | √ | 0 | 折算后数量 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | finvcounttype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: A :初盘 B :复盘 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_invcbtoentry |  | fentryid |

---

## 条码盘点表-主表 t_barcm_invcb

- **表名称：** 条码盘点表-主表
- **表名：** t_barcm_invcb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvcountbillno | 盘点表编号 | varchar | 80 |  | √ | ' ' | 盘点表编号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finvcountuserid | 盘点人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 8 | finvcountbillid | 盘点表单据ID | int8 | 64 |  | √ | 0 | 盘点表单据ID |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fismultiperinv | 支持多人盘点 | bpchar | 1 |  | √ | '0' | 支持多人盘点 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fisallinvcount | 盘点完成 | bpchar | 1 |  | √ | '0' | 盘点完成 |
| 14 | finvcountdate | 盘点完成时间 | timestamp | 0 |  |  | null | 盘点完成时间 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_invcb_fbillno |  | fbillno |
| 2 | pk_barcm_invcb |  | fid |

---

## 物料明细-子表 t_barcm_invcbentry

- **表名称：** 物料明细-子表
- **表名：** t_barcm_invcbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flossqty | 盘亏数量 | numeric | 23 | 10 | √ | 0 | 盘亏数量 |
| 3 | fqty3rdacc | 账存辅助数量(2) | numeric | 23 | 10 | √ | 0 | 账存辅助数量(2) |
| 4 | fsnnumbertext | 序列号文本 | varchar | 80 |  | √ | ' ' | 序列号文本 |
| 5 | fcheckqtyunit2nd | 复盘辅助数量 | numeric | 23 | 10 | √ | 0 | 复盘辅助数量 |
| 6 | fgainqty3rd | 盘盈辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘盈辅助数量(2) |
| 7 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 8 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fgainqty2nd | 盘盈辅助数量 | numeric | 23 | 10 | √ | 0 | 盘盈辅助数量 |
| 11 | fqty2ndacc | 账存辅助数量 | numeric | 23 | 10 | √ | 0 | 账存辅助数量 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fcheckqty | 复盘数量 | numeric | 23 | 10 | √ | 0 | 复盘数量 |
| 15 | fbaselossqty | 盘亏基本数量 | numeric | 23 | 10 | √ | 0 | 盘亏基本数量 |
| 16 | fismanualinvloss | 手工盘亏 | bpchar | 1 |  | √ | '0' | 手工盘亏 |
| 17 | finvlossuserid | 盘亏人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbaseqtyacc | 账存基本数量 | numeric | 23 | 10 | √ | 0 | 账存基本数量 |
| 19 | fcheckqty3rd | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 20 | fqtyacc | 账存数量 | numeric | 23 | 10 | √ | 0 | 账存数量 |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fqty | 盘点数量 | numeric | 23 | 10 | √ | 0 | 盘点数量 |
| 23 | fbasegainqty | 盘盈基本数量 | numeric | 23 | 10 | √ | 0 | 盘盈基本数量 |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | finvcountentryid | 盘点表分录id | int8 | 64 |  | √ | 0 | 盘点表分录id |
| 26 | fcheckbaseqty | 复盘基本数量 | numeric | 23 | 10 | √ | 0 | 复盘基本数量 |
| 27 | fgainqty | 盘盈数量 | numeric | 23 | 10 | √ | 0 | 盘盈数量 |
| 28 | fbarcodemainfileid | 条码主档ID | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 29 | flossqty3rd | 盘亏辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘亏辅助数量(2) |
| 30 | fqtyunit2nd | 盘点辅助数量 | numeric | 23 | 10 | √ | 0 | 盘点辅助数量 |
| 31 | flossqty2nd | 盘亏辅助数量 | numeric | 23 | 10 | √ | 0 | 盘亏辅助数量 |
| 32 | fqtyunit3rd | 盘点辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘点辅助数量(2) |
| 33 | fbarcodevalue | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 34 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fbaseqty | 盘点基本数量 | numeric | 23 | 10 | √ | 0 | 盘点基本数量 |
| 36 | fisreinventoryloss | 复盘盘亏 | bpchar | 1 |  | √ | '0' | 复盘盘亏 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_invcbentry |  | fentryid |
| 2 | idx_barcm_icbe_bcvalue |  | fbarcodevalue |
