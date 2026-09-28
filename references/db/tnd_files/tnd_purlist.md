# 标的信息-tnd_purlist

## 标的信息-主表 t_src_purlistentry

- **表名称：** 标的信息-主表
- **表名：** t_src_purlistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '1' |  |
| 5 | fsourceentryid | fsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 6 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 7 | frebate | frebate | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fnote | fnote | varchar | 512 |  | √ | ' ' |  |
| 10 | fresult | fresult | bpchar | 1 |  | √ | ' ' |  |
| 11 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fcfmqty | fcfmqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 15 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 16 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 17 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 19 | fqtyfrom | fqtyfrom | numeric | 23 | 10 | √ | 0 |  |
| 20 | fpreorderratio | fpreorderratio | numeric | 23 | 10 | √ | 0 |  |
| 21 | fisnew | fisnew | bpchar | 1 |  | √ | '0' |  |
| 22 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 23 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fdctrate | fdctrate | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 29 | fisbizitem | fisbizitem | bpchar | 1 |  | √ | '0' |  |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 32 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 33 | fhistoryprice | fhistoryprice | numeric | 23 | 10 | √ | 0 |  |
| 34 | fsysresult | fsysresult | bpchar | 1 |  | √ | ' ' |  |
| 35 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 36 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 37 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 38 | fentryid | 明细分录ID | int8 | 64 |  | √ | 0 | 明细分录ID |
| 39 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 40 | frank | frank | int8 | 64 |  | √ | 0 |  |
| 41 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 42 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 43 | fpreresult | fpreresult | bpchar | 1 |  | √ | ' ' |  |
| 44 | fprecfmqty | fprecfmqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 46 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsuppliercode | fsuppliercode | bpchar | 50 |  | √ | ' ' |  |
| 48 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 50 | ftranscost | ftranscost | numeric | 23 | 10 | √ | 0 |  |
| 51 | ffeerate | ffeerate | numeric | 23 | 10 | √ | 0 |  |
| 52 | fbidmaterialid | fbidmaterialid | int8 | 64 |  | √ | 0 |  |
| 53 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 54 | fcostdetail | fcostdetail | bpchar | 1 |  | √ | '0' |  |
| 55 | fpkgamount | fpkgamount | numeric | 23 | 10 | √ | 0 |  |
| 56 | fdistrictid | fdistrictid | int8 | 64 |  | √ | 0 |  |
| 57 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) |
| 58 | fpkgtaxamount | fpkgtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 59 | fdctamount | fdctamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | fisdecision | fisdecision | bpchar | 1 |  | √ | '0' |  |
| 61 | forderratio | forderratio | numeric | 23 | 10 | √ | 0 |  |
| 62 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 63 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 64 | fdecrease | fdecrease | numeric | 23 | 10 | √ | 0 |  |
| 65 | ftaxitemid | ftaxitemid | int8 | 64 |  | √ | 0 |  |
| 66 | fqtyto | fqtyto | numeric | 23 | 10 | √ | 0 |  |
| 67 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 68 | fareaid | fareaid | int8 | 64 |  | √ | 0 |  |
| 69 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 70 | fvieamount | fvieamount | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_fsupid |  | fsupplierid |
| 2 | idx_src_purlistentry_pid |  | fparentid |
| 3 | idx_src_purlistentry_fid |  | fid |
| 4 | idx_src_purlistentry_fpackid |  | fpackageid |
| 5 | idx_src_purlistentry_fpurid |  | fpurlistid |
| 6 | pk_src_purlistentry |  | fentryid |
| 7 | idx_src_purlistentry_fproid |  | fprojectid |
| 8 | idx_src_purlistentry_status |  | fentrystatus |
