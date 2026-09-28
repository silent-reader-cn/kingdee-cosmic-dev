# 标的信息-src_purlistedit

## 标的信息-分表 t_src_purlistentry_z

- **表名称：** 标的信息-分表
- **表名：** t_src_purlistentry_z

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftendersideld | ftendersideld | int8 | 64 |  | √ | 0 |  |
| 3 | fcontract | fcontract | int8 | 64 |  | √ | 0 |  |
| 4 | fareaprice | fareaprice | numeric | 23 | 10 | √ | 0 |  |
| 5 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 6 | ffirstrank | ffirstrank | int8 | 64 |  | √ | 0 |  |
| 7 | fnote1 | fnote1 | varchar | 500 |  | √ | ' ' |  |
| 8 | fnote2 | fnote2 | varchar | 50 |  | √ | ' ' |  |
| 9 | fnote3 | fnote3 | varchar | 50 |  | √ | ' ' |  |
| 10 | fcompkey | fcompkey | varchar | 50 |  | √ | ' ' |  |
| 11 | fnumber1 | fnumber1 | int8 | 64 |  | √ | 0 |  |
| 12 | fnumber2 | fnumber2 | int8 | 64 |  | √ | 0 |  |
| 13 | fpurdate | fpurdate | timestamp | 0 |  |  | null |  |
| 14 | fprice5 | fprice5 | numeric | 23 | 10 | √ | 0 |  |
| 15 | fprice6 | fprice6 | numeric | 23 | 10 | √ | 0 |  |
| 16 | fprice3 | fprice3 | numeric | 23 | 10 | √ | 0 |  |
| 17 | fprice4 | fprice4 | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprice9 | fprice9 | numeric | 23 | 10 | √ | 0 |  |
| 19 | fprice7 | fprice7 | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprice8 | fprice8 | numeric | 23 | 10 | √ | 0 |  |
| 21 | facttaxprice | facttaxprice | numeric | 23 | 10 | √ | 0 |  |
| 22 | factprice | factprice | numeric | 23 | 10 | √ | 0 |  |
| 23 | freqfrequency | freqfrequency | bpchar | 1 |  | √ | ' ' |  |
| 24 | fminiorderqty | fminiorderqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | farea | farea | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprice1 | fprice1 | numeric | 23 | 10 | √ | 0 |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fprice2 | fprice2 | numeric | 23 | 10 | √ | 0 |  |
| 29 | facreage | facreage | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 31 | fisclone | fisclone | bpchar | 1 |  | √ | '0' |  |
| 32 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 33 | fminipackqty | fminipackqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fweight | fweight | numeric | 23 | 10 | √ | 0 |  |
| 35 | fcalcvalue | fcalcvalue | numeric | 23 | 10 | √ | 0 |  |
| 36 | fprice_uom | fprice_uom | int8 | 64 |  | √ | 0 |  |
| 37 | flgortid | flgortid | int8 | 64 |  | √ | 0 |  |
| 38 | fratio | fratio | numeric | 23 | 10 | √ | 0 |  |
| 39 | fwidth | fwidth | numeric | 23 | 10 | √ | 0 |  |
| 40 | fprice10 | fprice10 | numeric | 23 | 10 | √ | 0 |  |
| 41 | fprice11 | fprice11 | numeric | 23 | 10 | √ | 0 |  |
| 42 | fprice12 | fprice12 | numeric | 23 | 10 | √ | 0 |  |
| 43 | fprice13 | fprice13 | numeric | 23 | 10 | √ | 0 |  |
| 44 | fprice14 | fprice14 | numeric | 23 | 10 | √ | 0 |  |
| 45 | fprice15 | fprice15 | numeric | 23 | 10 | √ | 0 |  |
| 46 | freqdepart | freqdepart | int8 | 64 |  | √ | 0 |  |
| 47 | fheight | fheight | numeric | 23 | 10 | √ | 0 |  |
| 48 | fbilltype | fbilltype | varchar | 30 |  | √ | ' ' |  |
| 49 | fpaymethod | fpaymethod | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_z_fid |  | fid |
| 2 | pk_src_purlistentry_z |  | fentryid |

---

## 标的信息-主表 t_src_purlistentry

- **表名称：** 标的信息-主表
- **表名：** t_src_purlistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '1' |  |
| 5 | fsourceentryid | fsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 6 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 7 | frebate | frebate | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fresult | fresult | bpchar | 1 |  | √ | ' ' |  |
| 11 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 12 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fcfmqty | fcfmqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 15 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 16 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 17 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 18 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 19 | fqtyfrom | fqtyfrom | numeric | 23 | 10 | √ | 0 |  |
| 20 | fpreorderratio | fpreorderratio | numeric | 23 | 10 | √ | 0 |  |
| 21 | fisnew | 是否供应商新增标的 | bpchar | 1 |  | √ | '0' | 是否供应商新增标的 |
| 22 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 23 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fdctrate | fdctrate | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 29 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 30 | fpackagename | fpackagename | varchar | 50 |  | √ | ' ' |  |
| 31 | fdescription | 标的描述 | varchar | 1024 |  | √ | ' ' | 标的描述 |
| 32 | fhistoryprice | fhistoryprice | numeric | 23 | 10 | √ | 0 |  |
| 33 | fsysresult | fsysresult | bpchar | 1 |  | √ | ' ' |  |
| 34 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 35 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 36 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 39 | frank | frank | int8 | 64 |  | √ | 0 |  |
| 40 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fpreresult | fpreresult | bpchar | 1 |  | √ | ' ' |  |
| 43 | fprecfmqty | fprecfmqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fentrystatus | 当前状态 | bpchar | 1 |  | √ | ' ' | 当前状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标的 I :已废标 J :已终止 |
| 45 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0 |  |
| 46 | fsuppliercode | fsuppliercode | bpchar | 50 |  | √ | ' ' |  |
| 47 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 48 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 49 | ftranscost | ftranscost | numeric | 23 | 10 | √ | 0 |  |
| 50 | ffeerate | ffeerate | numeric | 23 | 10 | √ | 0 |  |
| 51 | fbidmaterialid | fbidmaterialid | int8 | 64 |  | √ | 0 |  |
| 52 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 53 | fcostdetail | fcostdetail | bpchar | 1 |  | √ | '0' |  |
| 54 | fpkgamount | fpkgamount | numeric | 23 | 10 | √ | 0 |  |
| 55 | fdistrictid | fdistrictid | int8 | 64 |  | √ | 0 |  |
| 56 | fturns | fturns | varchar | 2 |  | √ | ' ' |  |
| 57 | fpkgtaxamount | fpkgtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 58 | fdctamount | fdctamount | numeric | 23 | 10 | √ | 0 |  |
| 59 | fisdecision | fisdecision | bpchar | 1 |  | √ | '0' |  |
| 60 | forderratio | forderratio | numeric | 23 | 10 | √ | 0 |  |
| 61 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 62 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 63 | fdecrease | fdecrease | numeric | 23 | 10 | √ | 0 |  |
| 64 | ftaxitemid | ftaxitemid | int8 | 64 |  | √ | 0 |  |
| 65 | fqtyto | fqtyto | numeric | 23 | 10 | √ | 0 |  |
| 66 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 67 | fareaid | fareaid | int8 | 64 |  | √ | 0 |  |
| 68 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 69 | fvieamount | fvieamount | numeric | 23 | 10 | √ | 0 |  |

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
