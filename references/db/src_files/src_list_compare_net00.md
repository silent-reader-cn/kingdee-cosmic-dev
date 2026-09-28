# 网购比价清单要求-src_list_compare_net00

## 阶梯报价分录-子表 t_src_purlistentrysub

- **表名称：** 阶梯报价分录-子表
- **表名：** t_src_purlistentrysub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftieredqtyfrom | 阶梯数量从(>) | numeric | 23 | 10 | √ | 0 | 阶梯数量从(>) |
| 2 | ftieredtaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 3 | ftieredprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 4 | ftieredunitid | 阶梯计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftieredprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 7 | ftierednote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | ftieredcurrid | 阶梯报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | ftieredqtyto | 阶梯数量至(≤) | numeric | 23 | 10 | √ | 0 | 阶梯数量至(≤) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_purlistentrysub |  | fdetailid |
| 2 | idx_src_purlistentrysub_eid |  | fentryid |

---

## 网购比价清单要求-反写记录表 t_src_purlist_wb

- **表名称：** 网购比价清单要求-反写记录表
- **表名：** t_src_purlist_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_purlist_wb |  | fentryid |
| 2 | idx_src_purlist_wb_fk |  | fid |

---

## 标的分录-分表 t_src_purlistentry_f

- **表名称：** 标的分录-分表
- **表名：** t_src_purlistentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliernumber | 供应商编码 | varchar | 50 |  | √ | ' ' | 供应商编码 |
| 3 | fsrcbillno | 上游源单单号 | varchar | 50 |  | √ | ' ' | 上游源单单号 |
| 4 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fmaxtaxprice | 含税起标单价 | numeric | 23 | 10 | √ | 0 | 含税起标单价 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ffirstprice | 首轮未税单价 | numeric | 23 | 10 | √ | 0 | 首轮未税单价 |
| 8 | flocprice | 本币未税单价 | numeric | 23 | 10 | √ | 0 | 本币未税单价 |
| 9 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fexchtypeid | 汇率(废弃) | int8 | 64 |  | √ | 0 | 汇率 bd_exrate_tree |
| 11 | fmaxprice | 未税起标单价 | numeric | 23 | 10 | √ | 0 | 未税起标单价 |
| 12 | feffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 13 | freqsource | 需求来源 | bpchar | 1 |  | √ | '3' | 需求来源,枚举: 1 :寻源申请 2 :采购申请 3 :项目立项 4 :项目启动 5 :采购共享 |
| 14 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 15 | fsitecode | site编码 | varchar | 50 |  | √ | ' ' | site编码 |
| 16 | fcfmbaseqty | 定标基本数量 | numeric | 23 | 10 | √ | 0 | 定标基本数量 |
| 17 | ffirstamount | 首轮未税金额 | numeric | 23 | 10 | √ | 0 | 首轮未税金额 |
| 18 | fhistorytaxprice | 上轮含税报价 | numeric | 23 | 10 | √ | 0 | 上轮含税报价 |
| 19 | ffirsttaxamount | 首轮价税合计 | numeric | 23 | 10 | √ | 0 | 首轮价税合计 |
| 20 | floctaxamount | 本币价税合计 | numeric | 23 | 10 | √ | 0 | 本币价税合计 |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fpreamount | 上轮未税金额 | numeric | 23 | 10 | √ | 0 | 上轮未税金额 |
| 23 | fpretaxamount | 上轮价税合计 | numeric | 23 | 10 | √ | 0 | 上轮价税合计 |
| 24 | fentrystatus2 | fentrystatus2 | bpchar | 1 |  | √ | 'A' |  |
| 25 | fquotedate | 供应商报价时间 | timestamp | 0 |  |  | null | 供应商报价时间 |
| 26 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | floctaxprice | 本币含税单价 | numeric | 23 | 10 | √ | 0 | 本币含税单价 |
| 28 | fclarifytaxprice | 澄清含税单价 | numeric | 23 | 10 | √ | 0 | 澄清含税单价 |
| 29 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 30 | faward | 核价同意否 | bpchar | 1 |  | √ | '0' | 核价同意否 |
| 31 | fclarifyprice | 澄清未税单价 | numeric | 23 | 10 | √ | 0 | 澄清未税单价 |
| 32 | fincreaseprice | 竞价调价幅度 | numeric | 23 | 10 | √ | 0 | 竞价调价幅度 |
| 33 | fduedate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 34 | fclarifytaxamount | 澄清价税合计 | numeric | 23 | 10 | √ | 0 | 澄清价税合计 |
| 35 | fbestprice | 项目最优未税单价 | numeric | 23 | 10 | √ | 0 | 项目最优未税单价 |
| 36 | flocamount | 本币未税金额 | numeric | 23 | 10 | √ | 0 | 本币未税金额 |
| 37 | fusdprice | 项目最优含税单价 | numeric | 23 | 10 | √ | 0 | 项目最优含税单价 |
| 38 | fsourcebillid | 上游源单ID | varchar | 50 |  | √ | ' ' | 上游源单ID |
| 39 | fclarifyamount | 澄清未税金额 | numeric | 23 | 10 | √ | 0 | 澄清未税金额 |
| 40 | ffirsttaxprice | 首轮含税单价 | numeric | 23 | 10 | √ | 0 | 首轮含税单价 |
| 41 | fbuyernote | 采购方备注 | varchar | 512 |  | √ | ' ' | 采购方备注 |
| 42 | fexchrate | 汇率(废弃) | numeric | 23 | 10 | √ | 0 | 汇率(废弃) |
| 43 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 45 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
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

## 标的分录-分表 t_src_purlistentry_z

- **表名称：** 标的分录-分表
- **表名：** t_src_purlistentry_z

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftendersideld | ftendersideld | int8 | 64 |  | √ | 0 |  |
| 3 | fcontract | fcontract | int8 | 64 |  | √ | 0 |  |
| 4 | fareaprice | fareaprice | numeric | 23 | 10 | √ | 0 |  |
| 5 | flength | 长(米) | numeric | 23 | 10 | √ | 0 | 长(米) |
| 6 | ffirstrank | 首轮排名 | int8 | 64 |  | √ | 0 | 首轮排名 |
| 7 | fnote1 | 备注1 | varchar | 500 |  | √ | ' ' | 备注1 |
| 8 | fnote2 | 备注2 | varchar | 50 |  | √ | ' ' | 备注2 |
| 9 | fnote3 | 备注3 | varchar | 50 |  | √ | ' ' | 备注3 |
| 10 | fcompkey | 组件名称 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fnumber1 | 编码1 | int8 | 64 |  | √ | 0 | 编码1 |
| 12 | fnumber2 | 编码2 | int8 | 64 |  | √ | 0 | 编码2 |
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
| 24 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 25 | farea | farea | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprice1 | 分项单价1 | numeric | 23 | 10 | √ | 0 | 分项单价1 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fprice2 | 最近未税交易单价 | numeric | 23 | 10 | √ | 0 | 最近未税交易单价 |
| 29 | facreage | facreage | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 31 | fisclone | 是否克隆 | bpchar | 1 |  | √ | '0' | 是否克隆 |
| 32 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 33 | fminipackqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 34 | fweight | 计算的权重 | numeric | 23 | 10 | √ | 0 | 计算的权重 |
| 35 | fcalcvalue | 自定义计算值 | numeric | 23 | 10 | √ | 0 | 自定义计算值 |
| 36 | fprice_uom | 价格单位 | int8 | 64 |  | √ | 0 | 价格单位 |
| 37 | flgortid | 仓库代码 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 38 | fratio | 计算的配比 | numeric | 23 | 10 | √ | 0 | 计算的配比 |
| 39 | fwidth | 宽(米) | numeric | 23 | 10 | √ | 0 | 宽(米) |
| 40 | fprice10 | 竞价区间从(>) | numeric | 23 | 10 | √ | 0 | 竞价区间从(>) |
| 41 | fprice11 | 竞价区间至(<) | numeric | 23 | 10 | √ | 0 | 竞价区间至(<) |
| 42 | fprice12 | 上次定标未税单价 | numeric | 23 | 10 | √ | 0 | 上次定标未税单价 |
| 43 | fprice13 | 上次定标含税单价 | numeric | 23 | 10 | √ | 0 | 上次定标含税单价 |
| 44 | fprice14 | 历史最优未税)单价 | numeric | 23 | 10 | √ | 0 | 历史最优未税)单价 |
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

## 网购比价清单要求-关联追踪表 t_src_purlist_tc

- **表名称：** 网购比价清单要求-关联追踪表
- **表名：** t_src_purlist_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlist_tc_tid |  | ftid |
| 2 | pk_src_purlist_tc |  | fid |
| 3 | idx_src_purlist_tc_tbill |  | ftbillid |

---

## 网购比价清单要求-主表 t_src_purlist

- **表名称：** 网购比价清单要求-主表
- **表名：** t_src_purlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 4 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 5 | fmaintainclause | 维修条款 | varchar | 50 |  | √ | ' ' | 维修条款 |
| 6 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 7 | fchgsrcbillid | fchgsrcbillid | int8 | 64 |  | √ | 0 |  |
| 8 | fsumamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 9 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 10 | fispurlistcomp | 是否采购清单组件 | bpchar | 1 |  | √ | '1' | 是否采购清单组件 |
| 11 | fcondition | fcondition | varchar | 2000 |  | √ | ' ' |  |
| 12 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 13 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 14 | fparentid | 父单据ID | varchar | 30 |  | √ | ' ' | 父单据ID |
| 15 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 16 | fentitykey | 组件标识 | varchar | 30 |  | √ | ' ' | 组件标识 |
| 17 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 18 | fsumqty | 合计数量 | numeric | 23 | 10 | √ | 0 | 合计数量 |
| 19 | fbidchangeid | fbidchangeid | int8 | 64 |  | √ | 0 |  |
| 20 | fcosttypeid | fcosttypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fpurtype | fpurtype | varchar | 30 |  | √ | ' ' |  |
| 22 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 24 | fsumtax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 25 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 26 | fcompbillno | fcompbillno | varchar | 30 |  | √ | ' ' |  |
| 27 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlist_fentitykey |  | fentitykey |
| 2 | idx_src_purlist_fparentid |  | fparentid |
| 3 | pk_src_purlist |  | fid |

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

## 标的分录-子表 t_src_purlistentry

- **表名称：** 标的分录-子表
- **表名：** t_src_purlistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 5 | fsourceentryid | 上游源单分录ID | varchar | 50 |  | √ | ' ' | 上游源单分录ID |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | frebate | 返点(%) | numeric | 23 | 10 | √ | 0 | 返点(%) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/未达标 7 :资审/评标不合格 9 :预中标 0 :流标 |
| 11 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 14 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 15 | fisdiscardbid | 允许弃标的 | bpchar | 1 |  | √ | '0' | 允许弃标的 |
| 16 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 17 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 19 | fqtyfrom | 阶梯数量从(>) | numeric | 23 | 10 | √ | 0 | 阶梯数量从(>) |
| 20 | fpreorderratio | 预定标份额(%) | numeric | 23 | 10 | √ | 0 | 预定标份额(%) |
| 21 | fisnew | 新增标的 | bpchar | 1 |  | √ | '0' | 新增标的 |
| 22 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 27 | fdctrate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 28 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 31 | fdescription | 标的描述 | varchar | 1024 |  | √ | ' ' | 标的描述 |
| 32 | fhistoryprice | 上轮未税报价 | numeric | 23 | 10 | √ | 0 | 上轮未税报价 |
| 33 | fsysresult | 推荐结果 | bpchar | 1 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/未达标 7 :资审/评标不合格 9 :预中标 |
| 34 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 35 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 36 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fisdiscarded | 确定弃标的 | bpchar | 1 |  | √ | '0' | 确定弃标的 |
| 39 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 40 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 42 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/未达标 7 :资审不合格 9 :预中标 0 :流标 |
| 43 | fprecfmqty | 预定标数量 | numeric | 23 | 10 | √ | 0 | 预定标数量 |
| 44 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标的 I :已废标 J :已终止 |
| 45 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 46 | fsuppliercode | 供应商代码 | bpchar | 50 |  | √ | ' ' | 供应商代码 |
| 47 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 48 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 49 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 50 | ffeerate | 费率(%) | numeric | 23 | 10 | √ | 0 | 费率(%) |
| 51 | fbidmaterialid | 项目标的 | int8 | 64 |  | √ | 0 | 项目立项分录F7 src_demandf7two |
| 52 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 53 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: 0 :待处理 1 :已处理 |
| 54 | fpkgamount | 标段未税金额 | numeric | 23 | 10 | √ | 0 | 标段未税金额 |
| 55 | fdistrictid | 片区 | int8 | 64 |  | √ | 0 | 片区与地区 pds_areadistrict |
| 56 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 30 :补价(1) 31 :补价(2) 32 :补价(3) |
| 57 | fpkgtaxamount | 标段价税合计 | numeric | 23 | 10 | √ | 0 | 标段价税合计 |
| 58 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 59 | fisdecision | 分批定标否 | bpchar | 1 |  | √ | '0' | 分批定标否 |
| 60 | forderratio | 定标份额(%) | numeric | 23 | 10 | √ | 0 | 定标份额(%) |
| 61 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 62 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 63 | fdecrease | 降幅(%) | numeric | 23 | 10 | √ | 0 | 降幅(%) |
| 64 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 65 | fqtyto | 阶梯数量至(≤) | numeric | 23 | 10 | √ | 0 | 阶梯数量至(≤) |
| 66 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 67 | fareaid | 地区 | int8 | 64 |  | √ | 0 | 片区与地区 pds_areadistrict |
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

## 采购方附件-附件表 t_src_purlistentry_fj

- **表名称：** 采购方附件-附件表
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

---

## 关联子实体-子表 t_src_purlistentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_purlistentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_purlistentry_lk |  | fpkid |
| 2 | idx_src_purlistentry_lk_fk |  | fentryid |
