# 招标价格库-src_pricelib

## 招标价格库-分表 t_src_contractentry_a

- **表名称：** 招标价格库-分表
- **表名：** t_src_contractentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | fsalorgid | fsalorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '1' |  |
| 5 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 |
| 6 | fprecfmqty | 预定标数量 | numeric | 23 | 10 | √ | 0 | 预定标数量 |
| 7 | fsourceentryid | fsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 8 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 9 | fcontractbaseqty | fcontractbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fminipackqty | fminipackqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fdeliverdate | fdeliverdate | timestamp | 0 |  |  | null |  |
| 13 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 14 | fcostdetail | fcostdetail | bpchar | 1 |  | √ | '0' |  |
| 15 | fpurorderno | fpurorderno | varchar | 80 |  | √ | ' ' |  |
| 16 | fcfmbaseqty | fcfmbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fpreorderratio | 预定标份额(%) | numeric | 23 | 10 | √ | 0 | 预定标份额(%) |
| 19 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 20 | fisnew | fisnew | bpchar | 1 |  | √ | '0' |  |
| 21 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 22 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbdsupplierid | fbdsupplierid | int8 | 64 |  | √ | 0 |  |
| 24 | fprice5 | fprice5 | numeric | 23 | 10 | √ | 0 |  |
| 25 | fprice6 | fprice6 | numeric | 23 | 10 | √ | 0 |  |
| 26 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | fprice4 | fprice4 | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprice7 | fprice7 | numeric | 23 | 10 | √ | 0 |  |
| 29 | forderbaseqty | forderbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | fispresent | fispresent | bpchar | 1 |  | √ | '0' |  |
| 31 | fprotocolqty | fprotocolqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fminiorderqty | fminiorderqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 34 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | frowtypeid | frowtypeid | int8 | 64 |  | √ | 0 |  |
| 37 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractentry_a_fid |  | fid |
| 2 | pk_src_contractentry_a |  | fentryid |

---

## 招标价格库-多语言表 t_src_contractentry_l

- **表名称：** 招标价格库-多语言表
- **表名：** t_src_contractentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_contractentry_l |  | fpkid |
| 2 | idx_src_apply_l_fid |  | fid |

---

## 招标价格库-主表 t_src_contractentry

- **表名称：** 招标价格库-主表
- **表名：** t_src_contractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | fsuppliernumber | fsuppliernumber | varchar | 50 |  | √ | ' ' |  |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0 | 税率(%) |
| 4 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | frebate | 返点(%) | numeric | 19 | 6 | √ | 0 | 返点(%) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | flocprice | flocprice | numeric | 23 | 10 | √ | 0 |  |
| 9 | fnote | fnote | varchar | 512 |  | √ | ' ' |  |
| 10 | fcontractqty | fcontractqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fentryrcvorgid | fentryrcvorgid | int8 | 64 |  | √ | 0 |  |
| 12 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 |
| 13 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fpurlistid | 标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 15 | fpricelistno | fpricelistno | varchar | 50 |  | √ | ' ' |  |
| 16 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 17 | fsourcelistid | fsourcelistid | varchar | 50 |  | √ | ' ' |  |
| 18 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 19 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 20 | fqtyfrom | fqtyfrom | numeric | 23 | 10 | √ | 0 |  |
| 21 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 22 | fqty | 招标数量 | numeric | 23 | 10 | √ | 0 | 招标数量 |
| 23 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0 | 折扣率(%) |
| 25 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 定标F7 src_decisionf7 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | facttaxprice | facttaxprice | numeric | 23 | 10 | √ | 0 |  |
| 28 | fpackagename | fpackagename | varchar | 50 |  | √ | ' ' |  |
| 29 | fdescription | 标的描述 | varchar | 1024 |  | √ | ' ' | 标的描述 |
| 30 | fsysresult | fsysresult | bpchar | 1 |  | √ | ' ' |  |
| 31 | factprice | factprice | numeric | 23 | 10 | √ | 0 |  |
| 32 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 33 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: bd_supplier :供应商 |
| 34 | fcontracttaxamt | fcontracttaxamt | numeric | 23 | 10 | √ | 0 |  |
| 35 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 38 | frank | frank | int4 | 32 |  | √ | 0 |  |
| 39 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 40 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 41 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 42 | fmaxtaxprice | fmaxtaxprice | numeric | 23 | 10 | √ | 0 |  |
| 43 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 44 | fmaterialgroupid | fmaterialgroupid | int8 | 64 |  | √ | 0 |  |
| 45 | fsourcelistno | fsourcelistno | varchar | 50 |  | √ | ' ' |  |
| 46 | fbrand | fbrand | varchar | 50 |  | √ | ' ' |  |
| 47 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 48 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 50 | fmaxprice | fmaxprice | numeric | 23 | 10 | √ | 0 |  |
| 51 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 52 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 53 | freqsource | freqsource | bpchar | 1 |  | √ | '3' |  |
| 54 | fbidmaterialid | fbidmaterialid | int8 | 64 |  | √ | 0 |  |
| 55 | ffeerate | 费率(%) | numeric | 19 | 6 | √ | 0 | 费率(%) |
| 56 | fpricelistid | fpricelistid | varchar | 50 |  | √ | ' ' |  |
| 57 | fpkgamount | fpkgamount | numeric | 23 | 10 | √ | 0 |  |
| 58 | fdistrictid | fdistrictid | int8 | 64 |  | √ | 0 |  |
| 59 | fpkgtaxamount | fpkgtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | fdctamount | fdctamount | numeric | 23 | 10 | √ | 0 |  |
| 61 | forderqty | forderqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | floctaxamount | floctaxamount | numeric | 23 | 10 | √ | 0 |  |
| 63 | fordertaxamt | fordertaxamt | numeric | 23 | 10 | √ | 0 |  |
| 64 | forderratio | 份额(%) | numeric | 19 | 6 | √ | 0 | 份额(%) |
| 65 | fprice_uom | fprice_uom | int4 | 32 |  | √ | 0 |  |
| 66 | floctaxprice | floctaxprice | numeric | 23 | 10 | √ | 0 |  |
| 67 | flgortid | flgortid | int8 | 64 |  | √ | 0 |  |
| 68 | fcontractamt | fcontractamt | numeric | 23 | 10 | √ | 0 |  |
| 69 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 70 | fduedate | fduedate | timestamp | 0 |  |  | null |  |
| 71 | fdecrease | 降幅(%) | numeric | 19 | 6 | √ | 0 | 降幅(%) |
| 72 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 73 | flocamount | flocamount | numeric | 23 | 10 | √ | 0 |  |
| 74 | fqtyto | fqtyto | numeric | 23 | 10 | √ | 0 |  |
| 75 | forderamt | forderamt | numeric | 23 | 10 | √ | 0 |  |
| 76 | fsourcebillid | fsourcebillid | varchar | 50 |  | √ | ' ' |  |
| 77 | fareaid | fareaid | int8 | 64 |  | √ | 0 |  |
| 78 | fexchrate | fexchrate | numeric | 19 | 6 | √ | 0 |  |
| 79 | fbuyernote | fbuyernote | varchar | 512 |  | √ | ' ' |  |
| 80 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 81 | fvieamount | fvieamount | numeric | 23 | 10 | √ | 0 |  |
| 82 | fsuppliernote | fsuppliernote | varchar | 512 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractentry_eid |  | fentrystatus |
| 2 | idx_src_contractentry_fid |  | fid |
| 3 | idx_src_contractentry_proid |  | fprojectid |
| 4 | idx_src_contractentry_sid |  | fsupplierid,fsuppliertype |
| 5 | pk_src_contractentry |  | fentryid |
| 6 | idx_src_contractentry_fpakid |  | fpackageid |
| 7 | idx_src_contractentry_pid |  | fpurlistid |
