# 条码盘点表-barcm_invcountbill

## 条码盘点表-主表 t_barcm_invcb

- **表名称：** 条码盘点表-主表
- **表名：** t_barcm_invcb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvcountbillno | 盘点表编号 | varchar | 80 |  | √ | ' ' | 盘点表编号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | finvcountbillid | 盘点表单据ID | int8 | 64 |  | √ | 0 | 盘点表单据ID |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

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
| 4 | fcheckqtyunit2nd | 复盘辅助数量 | numeric | 23 | 10 | √ | 0 | 复盘辅助数量 |
| 5 | fgainqty3rd | 盘盈辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘盈辅助数量(2) |
| 6 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 7 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fgainqty2nd | 盘盈辅助数量 | numeric | 23 | 10 | √ | 0 | 盘盈辅助数量 |
| 10 | fqty2ndacc | 帐存辅助数量 | numeric | 23 | 10 | √ | 0 | 帐存辅助数量 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | fcheckqty | 复盘数量 | numeric | 23 | 10 | √ | 0 | 复盘数量 |
| 14 | fbaselossqty | 盘亏基本数量 | numeric | 23 | 10 | √ | 0 | 盘亏基本数量 |
| 15 | fbaseqtyacc | 帐存基本数量 | numeric | 23 | 10 | √ | 0 | 帐存基本数量 |
| 16 | fcheckqty3rd | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 17 | fqtyacc | 帐存数量 | numeric | 23 | 10 | √ | 0 | 帐存数量 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fqty | 盘点数量 | numeric | 23 | 10 | √ | 0 | 盘点数量 |
| 20 | fbasegainqty | 盘盈基本数量 | numeric | 23 | 10 | √ | 0 | 盘盈基本数量 |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fcheckbaseqty | 复盘基本数量 | numeric | 23 | 10 | √ | 0 | 复盘基本数量 |
| 23 | fgainqty | 盘盈数量 | numeric | 23 | 10 | √ | 0 | 盘盈数量 |
| 24 | fbarcodemainfileid | 条码主档ID | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 25 | flossqty3rd | 盘亏辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘亏辅助数量(2) |
| 26 | fqtyunit2nd | 盘点辅助数量 | numeric | 23 | 10 | √ | 0 | 盘点辅助数量 |
| 27 | flossqty2nd | 盘亏辅助数量 | numeric | 23 | 10 | √ | 0 | 盘亏辅助数量 |
| 28 | fqtyunit3rd | 盘点辅助数量(2) | numeric | 23 | 10 | √ | 0 | 盘点辅助数量(2) |
| 29 | fbarcodevalue | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 30 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fbaseqty | 盘点基本数量 | numeric | 23 | 10 | √ | 0 | 盘点基本数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_invcbentry |  | fentryid |
| 2 | idx_barcm_icbe_bcvalue |  | fbarcodevalue |
