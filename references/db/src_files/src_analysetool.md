# 报价分析-src_analysetool

## 报价分析-多语言表 t_src_purlistentry_l

- **表名称：** 报价分析-多语言表
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

## 报价分析-分表 t_src_purlistentry_e

- **表名称：** 报价分析-分表
- **表名：** t_src_purlistentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplatformerea | fplatformerea | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterialtypeid | fmaterialtypeid | int8 | 64 |  | √ | 0 |  |
| 4 | felectrictype | felectrictype | varchar | 30 |  | √ | ' ' |  |
| 5 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 6 | fmaterialgroupid | 标的分类 | int8 | 64 |  | √ | 0 | [标的分类 src_materialgroup](../src_files/src_materialgroup.md) |
| 7 | fhigth | fhigth | numeric | 23 | 10 | √ | 0 |  |
| 8 | fpower | fpower | int8 | 64 |  | √ | 0 |  |
| 9 | fspeed | fspeed | numeric | 23 | 10 | √ | 0 |  |
| 10 | famoutratio | famoutratio | numeric | 23 | 10 | √ | 0 |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fisreuse | fisreuse | bpchar | 1 |  | √ | '0' |  |
| 13 | fwidt | fwidt | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_e_fid |  | fid |
| 2 | pk_src_purlistentry_e |  | fentryid |

---

## 报价分析-分表 t_src_purlistentry_f

- **表名称：** 报价分析-分表
- **表名：** t_src_purlistentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliernumber | 供应商编码 | varchar | 50 |  | √ | ' ' | 供应商编码 |
| 3 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ffirstprice | 首轮未税单价 | numeric | 23 | 10 | √ | 0 | 首轮未税单价 |
| 6 | flocprice | 本币未税单价 | numeric | 23 | 10 | √ | 0 | 本币未税单价 |
| 7 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fexchtypeid | 汇率 | int8 | 64 |  | √ | 0 | [汇率 bd_exrate_tree](../base_files/bd_exrate_tree.md) |
| 9 | fdeliverdate | fdeliverdate | timestamp | 0 |  |  | null |  |
| 10 | fsitecode | site编码 | varchar | 50 |  | √ | ' ' | site编码 |
| 11 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 12 | fpreamount | 上轮未税金额 | numeric | 23 | 10 | √ | 0 | 上轮未税金额 |
| 13 | fentrystatus2 | fentrystatus2 | bpchar | 1 |  | √ | 'A' |  |
| 14 | fpricerate | 价差率(%) | numeric | 23 | 10 | √ | 0 | 价差率(%) |
| 15 | fmaxtaxamount | 含税起标金额 | numeric | 23 | 10 | √ | 0 | 含税起标金额 |
| 16 | fclarifytaxprice | 澄清含税单价 | numeric | 23 | 10 | √ | 0 | 澄清含税单价 |
| 17 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 18 | faward | 裁决 | bpchar | 1 |  | √ | '0' | 裁决 |
| 19 | fclarifyprice | 澄清未税单价 | numeric | 23 | 10 | √ | 0 | 澄清未税单价 |
| 20 | fincreaseprice | 价格涨幅 | numeric | 23 | 10 | √ | 0 | 价格涨幅 |
| 21 | fclarifytaxamount | 澄清价税合计 | numeric | 23 | 10 | √ | 0 | 澄清价税合计 |
| 22 | fbestprice | 项目最优未税单价 | numeric | 23 | 10 | √ | 0 | 项目最优未税单价 |
| 23 | fclarifyamount | 澄清未税金额 | numeric | 23 | 10 | √ | 0 | 澄清未税金额 |
| 24 | ffirsttaxprice | 首轮含税单价 | numeric | 23 | 10 | √ | 0 | 首轮含税单价 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | frowtypeid | frowtypeid | int8 | 64 |  | √ | 0 |  |
| 27 | fpricediff | 价差 | numeric | 23 | 10 | √ | 0 | 价差 |
| 28 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 29 | fmaxtaxprice | 含税起标单价 | numeric | 23 | 10 | √ | 0 | 含税起标单价 |
| 30 | fmaxamount | 未税起标金额 | numeric | 23 | 10 | √ | 0 | 未税起标金额 |
| 31 | fmaxprice | 未税起标单价 | numeric | 23 | 10 | √ | 0 | 未税起标单价 |
| 32 | feffectdate | 价格生效时间 | timestamp | 0 |  |  | null | 价格生效时间 |
| 33 | freqsource | freqsource | bpchar | 1 |  | √ | '3' |  |
| 34 | fcfmbaseqty | fcfmbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | ffirstamount | 首轮未税金额 | numeric | 23 | 10 | √ | 0 | 首轮未税金额 |
| 36 | fhistorytaxprice | 上轮含税报价 | numeric | 23 | 10 | √ | 0 | 上轮含税报价 |
| 37 | ffirsttaxamount | 首轮价税合计 | numeric | 23 | 10 | √ | 0 | 首轮价税合计 |
| 38 | floctaxamount | 本币含税金额 | numeric | 23 | 10 | √ | 0 | 本币含税金额 |
| 39 | fpretaxamount | 上轮价税合计 | numeric | 23 | 10 | √ | 0 | 上轮价税合计 |
| 40 | fquotedate | 供应商报价时间 | timestamp | 0 |  |  | null | 供应商报价时间 |
| 41 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 42 | floctaxprice | 本币含税单价 | numeric | 23 | 10 | √ | 0 | 本币含税单价 |
| 43 | fduedate | 价格失效时间 | timestamp | 0 |  |  | null | 价格失效时间 |
| 44 | flocamount | 本币未税金额 | numeric | 23 | 10 | √ | 0 | 本币未税金额 |
| 45 | fusdprice | 项目最优含税单价 | numeric | 23 | 10 | √ | 0 | 项目最优含税单价 |
| 46 | fsourcebillid | fsourcebillid | varchar | 50 |  | √ | ' ' |  |
| 47 | fbuyernote | 采购方备注 | varchar | 512 |  | √ | ' ' | 采购方备注 |
| 48 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 49 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsuppliernote | 供应商备注 | varchar | 512 |  | √ | ' ' | 供应商备注 |

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

## 报价分析-分表 t_src_purlistentry_z

- **表名称：** 报价分析-分表
- **表名：** t_src_purlistentry_z

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftendersideld | ftendersideld | int8 | 64 |  | √ | 0 |  |
| 3 | fcontract | fcontract | int8 | 64 |  | √ | 0 |  |
| 4 | fareaprice | fareaprice | numeric | 23 | 10 | √ | 0 |  |
| 5 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 6 | ffirstrank | 首轮排名 | int8 | 64 |  | √ | 0 | 首轮排名 |
| 7 | fnote1 | 备注1 | varchar | 500 |  | √ | ' ' | 备注1 |
| 8 | fnote2 | 备注2 | varchar | 50 |  | √ | ' ' | 备注2 |
| 9 | fnote3 | 备注3 | varchar | 50 |  | √ | ' ' | 备注3 |
| 10 | fcompkey | 采购清单 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fnumber1 | fnumber1 | int8 | 64 |  | √ | 0 |  |
| 12 | fnumber2 | fnumber2 | int8 | 64 |  | √ | 0 |  |
| 13 | fpurdate | fpurdate | timestamp | 0 |  |  | null |  |
| 14 | fprice5 | 定标价税合计 | numeric | 23 | 10 | √ | 0 | 定标价税合计 |
| 15 | fprice6 | 本币定标未税金额 | numeric | 23 | 10 | √ | 0 | 本币定标未税金额 |
| 16 | fprice3 | 最近含税交易单价 | numeric | 23 | 10 | √ | 0 | 最近含税交易单价 |
| 17 | fprice4 | 定标未税金额 | numeric | 23 | 10 | √ | 0 | 定标未税金额 |
| 18 | fprice9 | 竞价价差 | numeric | 23 | 10 | √ | 0 | 竞价价差 |
| 19 | fprice7 | 本币定标价税合计 | numeric | 23 | 10 | √ | 0 | 本币定标价税合计 |
| 20 | fprice8 | 竞价比例(%) | numeric | 23 | 10 | √ | 0 | 竞价比例(%) |
| 21 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 22 | factprice | 实际未税单价 | numeric | 23 | 10 | √ | 0 | 实际未税单价 |
| 23 | freqfrequency | freqfrequency | bpchar | 1 |  | √ | ' ' |  |
| 24 | fminiorderqty | fminiorderqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | farea | farea | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprice1 | 未税单价1 | numeric | 23 | 10 | √ | 0 | 未税单价1 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fprice2 | 最近未税交易单价 | numeric | 23 | 10 | √ | 0 | 最近未税交易单价 |
| 29 | facreage | facreage | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 31 | fisclone | fisclone | bpchar | 1 |  | √ | '0' |  |
| 32 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 33 | fminipackqty | fminipackqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fweight | 计算的权重 | numeric | 23 | 10 | √ | 0 | 计算的权重 |
| 35 | fcalcvalue | 自定义计算值 | numeric | 23 | 10 | √ | 0 | 自定义计算值 |
| 36 | fprice_uom | 价格单位 | int8 | 64 |  | √ | 0 | 价格单位 |
| 37 | flgortid | flgortid | int8 | 64 |  | √ | 0 |  |
| 38 | fratio | 计算的配比 | numeric | 23 | 10 | √ | 0 | 计算的配比 |
| 39 | fwidth | fwidth | numeric | 23 | 10 | √ | 0 |  |
| 40 | fprice10 | 竞价区间从(>) | numeric | 23 | 10 | √ | 0 | 竞价区间从(>) |
| 41 | fprice11 | 竞价区间至(<) | numeric | 23 | 10 | √ | 0 | 竞价区间至(<) |
| 42 | fprice12 | 上次定标未税单价 | numeric | 23 | 10 | √ | 0 | 上次定标未税单价 |
| 43 | fprice13 | 上次定标含税单价 | numeric | 23 | 10 | √ | 0 | 上次定标含税单价 |
| 44 | fprice14 | 历史最优未税单价 | numeric | 23 | 10 | √ | 0 | 历史最优未税单价 |
| 45 | fprice15 | 历史最优含税单价 | numeric | 23 | 10 | √ | 0 | 历史最优含税单价 |
| 46 | freqdepart | freqdepart | int8 | 64 |  | √ | 0 |  |
| 47 | fheight | fheight | numeric | 23 | 10 | √ | 0 |  |
| 48 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 1 :采购清单 2 :供应商报价单 3 :线上议价单 4 :线下议价单 |
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

## 报价分析-主表 t_src_purlistentry

- **表名称：** 报价分析-主表
- **表名：** t_src_purlistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '1' |  |
| 5 | fsourceentryid | fsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 6 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 7 | frebate | 返点(%) | numeric | 23 | 10 | √ | 0 | 返点(%) |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 0 :流标 |
| 11 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 14 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 15 | fisdiscardbid | 允许弃标的 | bpchar | 1 |  | √ | '0' | 允许弃标的 |
| 16 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 17 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 19 | fqtyfrom | fqtyfrom | numeric | 23 | 10 | √ | 0 |  |
| 20 | fpreorderratio | 预定标份额(%) | numeric | 23 | 10 | √ | 0 | 预定标份额(%) |
| 21 | fisnew | fisnew | bpchar | 1 |  | √ | '0' |  |
| 22 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 27 | fdctrate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 28 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 29 | fisbizitem | 是否商务条款 | bpchar | 1 |  | √ | '0' | 是否商务条款 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 32 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 33 | fhistoryprice | 上轮未税报价 | numeric | 23 | 10 | √ | 0 | 上轮未税报价 |
| 34 | fsysresult | 推荐结果 | bpchar | 1 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :评标/资审不合格 9 :预中标 |
| 35 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 36 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 37 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 38 | fentryid | 明细分录ID | int8 | 64 |  | √ | 0 | 明细分录ID |
| 39 | fisdiscarded | 确定弃标的 | bpchar | 1 |  | √ | '0' | 确定弃标的 |
| 40 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 41 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 42 | fbizamount | 系统计算的商务价格 | numeric | 23 | 10 | √ | 0 | 系统计算的商务价格 |
| 43 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/资审未达标 9 :预中标 |
| 44 | fprecfmqty | 预定标数量 | numeric | 23 | 10 | √ | 0 | 预定标数量 |
| 45 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标的 I :已废标 J :已终止 |
| 46 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 47 | fsuppliercode | fsuppliercode | bpchar | 50 |  | √ | ' ' |  |
| 48 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 49 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 50 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 51 | ffeerate | 费率(%) | numeric | 23 | 10 | √ | 0 | 费率(%) |
| 52 | fbidmaterialid | 标的档案 | int8 | 64 |  | √ | 0 | [标的档案 src_material](../src_files/src_material.md) |
| 53 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 54 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: 0 :待处理 1 :已处理 |
| 55 | fpkgamount | 标段金额 | numeric | 23 | 10 | √ | 0 | 标段金额 |
| 56 | fdistrictid | 片区 | int8 | 64 |  | √ | 0 | [片区与地区 pds_areadistrict](../pds_files/pds_areadistrict.md) |
| 57 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) A :补价(1) B :补价(2) C :补价(3) |
| 58 | fpkgtaxamount | fpkgtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 59 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 60 | fisdecision | 分批定标否 | bpchar | 1 |  | √ | '0' | 分批定标否 |
| 61 | forderratio | 定标份额(%) | numeric | 23 | 10 | √ | 0 | 定标份额(%) |
| 62 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 63 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 64 | fdecrease | 降幅(%) | numeric | 23 | 10 | √ | 0 | 降幅(%) |
| 65 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 66 | fqtyto | fqtyto | numeric | 23 | 10 | √ | 0 |  |
| 67 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 68 | fareaid | 供货地区 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 69 | fcurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 70 | fvieamount | 竞价金额 | numeric | 23 | 10 | √ | 0 | 竞价金额 |

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

---

## 附件-附件表 t_src_purlistentry_fj

- **表名称：** 附件-附件表
- **表名：** t_src_purlistentry_fj

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
| 1 | idx_src_purlistentry_fj_bid |  | fbasedataid |
| 2 | pk_src_purlistentry_fj |  | fpkid |
| 3 | idx_src_purlistentry_fj_fid |  | fentryid |
