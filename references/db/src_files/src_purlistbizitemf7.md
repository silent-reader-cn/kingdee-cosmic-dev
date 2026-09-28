# 商务条款分析-src_purlistbizitemf7

## 商务条款分析-多语言表 t_src_purlistentry_l

- **表名称：** 商务条款分析-多语言表
- **表名：** t_src_purlistentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_l_feid |  | fentryid,flocaleid |
| 2 | pk_src_purlistentry_l |  | fpkid |

---

## 商务条款分析-分表 t_src_purlistentry_f

- **表名称：** 商务条款分析-分表
- **表名：** t_src_purlistentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliernumber | fsuppliernumber | varchar | 50 |  | √ | ' ' |  |
| 3 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | ffirstprice | ffirstprice | numeric | 23 | 10 | √ | 0 |  |
| 6 | flocprice | flocprice | numeric | 23 | 10 | √ | 0 |  |
| 7 | fentryrcvorgid | fentryrcvorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fdeliverdate | fdeliverdate | timestamp | 0 |  |  | null |  |
| 10 | fsitecode | fsitecode | varchar | 50 |  | √ | ' ' |  |
| 11 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 12 | fpreamount | fpreamount | numeric | 23 | 10 | √ | 0 |  |
| 13 | fentrystatus2 | fentrystatus2 | bpchar | 1 |  | √ | 'A' |  |
| 14 | fpricerate | fpricerate | numeric | 23 | 10 | √ | 0 |  |
| 15 | fmaxtaxamount | fmaxtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | fclarifytaxprice | fclarifytaxprice | numeric | 23 | 10 | √ | 0 |  |
| 17 | fispresent | fispresent | bpchar | 1 |  | √ | '0' |  |
| 18 | faward | faward | bpchar | 1 |  | √ | '0' |  |
| 19 | fclarifyprice | fclarifyprice | numeric | 23 | 10 | √ | 0 |  |
| 20 | fincreaseprice | fincreaseprice | numeric | 23 | 10 | √ | 0 |  |
| 21 | fclarifytaxamount | fclarifytaxamount | numeric | 23 | 10 | √ | 0 |  |
| 22 | fbestprice | fbestprice | numeric | 23 | 10 | √ | 0 |  |
| 23 | fclarifyamount | fclarifyamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | ffirsttaxprice | ffirsttaxprice | numeric | 23 | 10 | √ | 0 |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | frowtypeid | frowtypeid | int8 | 64 |  | √ | 0 |  |
| 27 | fpricediff | fpricediff | numeric | 23 | 10 | √ | 0 |  |
| 28 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 29 | fmaxtaxprice | fmaxtaxprice | numeric | 23 | 10 | √ | 0 |  |
| 30 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 31 | fmaxprice | fmaxprice | numeric | 23 | 10 | √ | 0 |  |
| 32 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 33 | freqsource | freqsource | bpchar | 1 |  | √ | '3' |  |
| 34 | fcfmbaseqty | fcfmbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | ffirstamount | ffirstamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fhistorytaxprice | fhistorytaxprice | numeric | 23 | 10 | √ | 0 |  |
| 37 | ffirsttaxamount | ffirsttaxamount | numeric | 23 | 10 | √ | 0 |  |
| 38 | floctaxamount | floctaxamount | numeric | 23 | 10 | √ | 0 |  |
| 39 | fpretaxamount | fpretaxamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fquotedate | 供应商报价时间 | timestamp | 0 |  |  | null | 供应商报价时间 |
| 41 | fbdprojectid | fbdprojectid | int8 | 64 |  | √ | 0 |  |
| 42 | floctaxprice | floctaxprice | numeric | 23 | 10 | √ | 0 |  |
| 43 | fduedate | fduedate | timestamp | 0 |  |  | null |  |
| 44 | flocamount | flocamount | numeric | 23 | 10 | √ | 0 |  |
| 45 | fusdprice | fusdprice | numeric | 23 | 10 | √ | 0 |  |
| 46 | fsourcebillid | fsourcebillid | varchar | 50 |  | √ | ' ' |  |
| 47 | fbuyernote | fbuyernote | varchar | 512 |  | √ | ' ' |  |
| 48 | fexchrate | fexchrate | numeric | 23 | 10 | √ | 0 |  |
| 49 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsuppliernote | fsuppliernote | varchar | 512 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_purlistentry_f |  | fentryid |
| 2 | idx_src_purlistentry_f_fid |  | fid |

---

## 商务条款分析-分表 t_src_purlistentry_a

- **表名称：** 商务条款分析-分表
- **表名：** t_src_purlistentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizitemld | 商务条款编码 | int8 | 64 |  | √ | 0 | [寻源商务条款 src_bizitem](../src_files/src_bizitem.md) |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | freply | 供应商回复 | varchar | 510 |  | √ | ' ' | 供应商回复 |
| 5 | fitemtype | 商务条款类型 | varchar | 50 |  | √ | ' ' | 商务条款类型 |
| 6 | fdemand | 采购方要求 | varchar | 510 |  | √ | ' ' | 采购方要求 |
| 7 | freplyvalue | 供应商回复值 | varchar | 510 |  | √ | ' ' | 供应商回复值 |
| 8 | fdemandvalue | 采购方要求值 | varchar | 510 |  | √ | ' ' | 采购方要求值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | frequest | 商务条款名称 | varchar | 510 |  | √ | ' ' | 商务条款名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_a_fid |  | fid |
| 2 | pk_src_purlistentry_a |  | fentryid |

---

## 供应商附件-附件表 t_src_purlistentry_supfj

- **表名称：** 供应商附件-附件表
- **表名：** t_src_purlistentry_supfj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_purlistentry_supfj |  | fpkid |
| 2 | idx_src_purlistentry_supfj_fid |  | fentryid |
| 3 | idx_src_purlistentry_supfj_bid |  | fbasedataid |

---

## 商务条款分析-主表 t_src_purlistentry

- **表名称：** 商务条款分析-主表
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
| 9 | fnote | fnote | varchar | 512 |  | √ | ' ' |  |
| 10 | fresult | fresult | bpchar | 1 |  | √ | ' ' |  |
| 11 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 12 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fcfmqty | fcfmqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fmaterialnane | fmaterialnane | varchar | 255 |  | √ | ' ' |  |
| 15 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 16 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 17 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 18 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 19 | fqtyfrom | fqtyfrom | numeric | 23 | 10 | √ | 0 |  |
| 20 | fpreorderratio | fpreorderratio | numeric | 23 | 10 | √ | 0 |  |
| 21 | fisnew | fisnew | bpchar | 1 |  | √ | '0' |  |
| 22 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 23 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 24 | fmaterialmodel | fmaterialmodel | varchar | 1024 |  | √ | ' ' |  |
| 25 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fdctrate | fdctrate | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 29 | fisbizitem | 是否商务条款 | bpchar | 1 |  | √ | '0' | 是否商务条款 |
| 30 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 31 | fpackagename | fpackagename | varchar | 50 |  | √ | ' ' |  |
| 32 | fdescription | fdescription | varchar | 1024 |  | √ | ' ' |  |
| 33 | fhistoryprice | fhistoryprice | numeric | 23 | 10 | √ | 0 |  |
| 34 | fsysresult | fsysresult | bpchar | 1 |  | √ | ' ' |  |
| 35 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 36 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别 |
| 37 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 40 | frank | frank | int8 | 64 |  | √ | 0 |  |
| 41 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 42 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 43 | fpreresult | fpreresult | bpchar | 1 |  | √ | ' ' |  |
| 44 | fprecfmqty | fprecfmqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
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
| 57 | fturns | fturns | varchar | 2 |  | √ | ' ' |  |
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
