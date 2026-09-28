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
| 6 | fmaterialgroupid | 寻源标的分类 | int8 | 64 |  | √ | 0 | 标的分类 src_materialgroup |
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
| 3 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 4 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fmaxtaxprice | 含税起标单价 | numeric | 23 | 10 | √ | 0 | 含税起标单价 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ffirstprice | 首轮未税单价 | numeric | 23 | 10 | √ | 0 | 首轮未税单价 |
| 8 | flocprice | 本币未税单价 | numeric | 23 | 10 | √ | 0 | 本币未税单价 |
| 9 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fexchtypeid | 汇率 | int8 | 64 |  | √ | 0 | 汇率 bd_exrate_tree |
| 11 | fmaxprice | 未税起标单价 | numeric | 23 | 10 | √ | 0 | 未税起标单价 |
| 12 | feffectdate | 价格生效时间 | timestamp | 0 |  |  | null | 价格生效时间 |
| 13 | freqsource | freqsource | bpchar | 1 |  | √ | '3' |  |
| 14 | fdeliverdate | fdeliverdate | timestamp | 0 |  |  | null |  |
| 15 | fsitecode | site编码 | varchar | 50 |  | √ | ' ' | site编码 |
| 16 | fcfmbaseqty | fcfmbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | ffirstamount | 首轮未税金额 | numeric | 23 | 10 | √ | 0 | 首轮未税金额 |
| 18 | fhistorytaxprice | 上轮含税报价 | numeric | 23 | 10 | √ | 0 | 上轮含税报价 |
| 19 | ffirsttaxamount | 首轮价税合计 | numeric | 23 | 10 | √ | 0 | 首轮价税合计 |
| 20 | floctaxamount | 本币含税金额 | numeric | 23 | 10 | √ | 0 | 本币含税金额 |
| 21 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 22 | fpreamount | 上轮未税金额 | numeric | 23 | 10 | √ | 0 | 上轮未税金额 |
| 23 | fpretaxamount | 上轮价税合计 | numeric | 23 | 10 | √ | 0 | 上轮价税合计 |
| 24 | fentrystatus2 | fentrystatus2 | bpchar | 1 |  | √ | 'A' |  |
| 25 | fquotedate | 供应商报价时间 | timestamp | 0 |  |  | null | 供应商报价时间 |
| 26 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | floctaxprice | 本币含税单价 | numeric | 23 | 10 | √ | 0 | 本币含税单价 |
| 28 | fclarifytaxprice | 澄清含税单价 | numeric | 23 | 10 | √ | 0 | 澄清含税单价 |
| 29 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 30 | faward | 裁决 | bpchar | 1 |  | √ | '0' | 裁决 |
| 31 | fclarifyprice | 澄清未税单价 | numeric | 23 | 10 | √ | 0 | 澄清未税单价 |
| 32 | fincreaseprice | 价格涨幅 | numeric | 23 | 10 | √ | 0 | 价格涨幅 |
| 33 | fduedate | 价格失效时间 | timestamp | 0 |  |  | null | 价格失效时间 |
| 34 | fclarifytaxamount | 澄清价税合计 | numeric | 23 | 10 | √ | 0 | 澄清价税合计 |
| 35 | fbestprice | 项目最优未税单价 | numeric | 23 | 10 | √ | 0 | 项目最优未税单价 |
| 36 | flocamount | 本币未税金额 | numeric | 23 | 10 | √ | 0 | 本币未税金额 |
| 37 | fusdprice | 项目最优含税单价 | numeric | 23 | 10 | √ | 0 | 项目最优含税单价 |
| 38 | fsourcebillid | fsourcebillid | varchar | 50 |  | √ | ' ' |  |
| 39 | fclarifyamount | 澄清未税金额 | numeric | 23 | 10 | √ | 0 | 澄清未税金额 |
| 40 | ffirsttaxprice | 首轮含税单价 | numeric | 23 | 10 | √ | 0 | 首轮含税单价 |
| 41 | fbuyernote | 采购方备注 | varchar | 512 |  | √ | ' ' | 采购方备注 |
| 42 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 43 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 45 | frowtypeid | frowtypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fsuppliernote | 供应商备注 | varchar | 512 |  | √ | ' ' | 供应商备注 |

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
| 10 | fcompkey | 采购清单 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
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
| 10 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :门槛未达标 7 :资审未通过 9 :预中标 0 :流标 |
| 11 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 14 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 15 | fisdiscardbid | 允许弃标的 | bpchar | 1 |  | √ | '0' | 允许弃标的 |
| 16 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 17 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 19 | fqtyfrom | fqtyfrom | numeric | 23 | 10 | √ | 0 |  |
| 20 | fpreorderratio | 预定标份额(%) | numeric | 23 | 10 | √ | 0 | 预定标份额(%) |
| 21 | fisnew | fisnew | bpchar | 1 |  | √ | '0' |  |
| 22 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 27 | fdctrate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 28 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 31 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 32 | fhistoryprice | 上轮未税报价 | numeric | 23 | 10 | √ | 0 | 上轮未税报价 |
| 33 | fsysresult | 推荐结果 | bpchar | 1 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :门槛未达标 7 :资审未通过 9 :预中标 |
| 34 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 35 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 36 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 37 | fentryid | 明细分录ID | int8 | 64 |  | √ | 0 | 明细分录ID |
| 38 | fisdiscarded | 确定弃标的 | bpchar | 1 |  | √ | '0' | 确定弃标的 |
| 39 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 40 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | fbizamount | 系统计算的商务价格 | numeric | 23 | 10 | √ | 0 | 系统计算的商务价格 |
| 42 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 |
| 43 | fprecfmqty | 预定标数量 | numeric | 23 | 10 | √ | 0 | 预定标数量 |
| 44 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标的 I :已废标 J :已终止 |
| 45 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 46 | fsuppliercode | fsuppliercode | bpchar | 50 |  | √ | ' ' |  |
| 47 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 48 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 49 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 50 | ffeerate | 费率(%) | numeric | 23 | 10 | √ | 0 | 费率(%) |
| 51 | fbidmaterialid | 寻源标的 | int8 | 64 |  | √ | 0 | 标的档案 src_material |
| 52 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 53 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: 0 :待处理 1 :已处理 |
| 54 | fpkgamount | 标段金额 | numeric | 23 | 10 | √ | 0 | 标段金额 |
| 55 | fdistrictid | 片区 | int8 | 64 |  | √ | 0 | 片区与地区 pds_areadistrict |
| 56 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) A :补价(1) B :补价(2) C :补价(3) |
| 57 | fpkgtaxamount | fpkgtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 58 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 59 | fisdecision | 分批定标否 | bpchar | 1 |  | √ | '0' | 分批定标否 |
| 60 | forderratio | 定标份额(%) | numeric | 23 | 10 | √ | 0 | 定标份额(%) |
| 61 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 62 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 63 | fdecrease | 降幅(%) | numeric | 23 | 10 | √ | 0 | 降幅(%) |
| 64 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 65 | fqtyto | fqtyto | numeric | 23 | 10 | √ | 0 |  |
| 66 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 67 | fareaid | 供货地区 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 68 | fcurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 69 | fvieamount | 竞价金额 | numeric | 23 | 10 | √ | 0 | 竞价金额 |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
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
