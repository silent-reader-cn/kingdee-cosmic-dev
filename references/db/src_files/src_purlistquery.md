# 采购清单查询-src_purlistquery

## 采购清单查询-分表 t_src_purlistentry_e

- **表名称：** 采购清单查询-分表
- **表名：** t_src_purlistentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplatformerea | fplatformerea | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterialtypeid | fmaterialtypeid | int8 | 64 |  | √ | 0 |  |
| 4 | felectrictype | felectrictype | varchar | 30 |  | √ | ' ' |  |
| 5 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 6 | fmaterialgroupid | 寻源标的分类 | int8 | 64 |  | √ | 0 | [标的分类 src_materialgroup](../src_files/src_materialgroup.md) |
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

## 采购清单查询-分表 t_src_purlistentry_f

- **表名称：** 采购清单查询-分表
- **表名：** t_src_purlistentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliernumber | fsuppliernumber | varchar | 50 |  | √ | ' ' |  |
| 3 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ffirstprice | 首轮未税单价 | numeric | 23 | 10 | √ | 0 | 首轮未税单价 |
| 6 | flocprice | 本币未税单价 | numeric | 23 | 10 | √ | 0 | 本币未税单价 |
| 7 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fexchtypeid | 汇率(废弃) | int8 | 64 |  | √ | 0 | [汇率 bd_exrate_tree](../base_files/bd_exrate_tree.md) |
| 9 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 10 | fsitecode | fsitecode | varchar | 50 |  | √ | ' ' |  |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fpreamount | 上轮未税金额 | numeric | 23 | 10 | √ | 0 | 上轮未税金额 |
| 13 | fentrystatus2 | 标的流标状态 | bpchar | 1 |  | √ | 'A' | 标的流标状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 14 | fpricerate | 价差率(%) | numeric | 23 | 10 | √ | 0 | 价差率(%) |
| 15 | fmaxtaxamount | 含税起标金额 | numeric | 23 | 10 | √ | 0 | 含税起标金额 |
| 16 | fclarifytaxprice | 澄清含税单价 | numeric | 23 | 10 | √ | 0 | 澄清含税单价 |
| 17 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 18 | faward | 核价同意否 | bpchar | 1 |  | √ | '0' | 核价同意否 |
| 19 | fclarifyprice | 澄清未税单价 | numeric | 23 | 10 | √ | 0 | 澄清未税单价 |
| 20 | fincreaseprice | 竞价调价幅度 | numeric | 23 | 10 | √ | 0 | 竞价调价幅度 |
| 21 | fclarifytaxamount | 澄清价税合计 | numeric | 23 | 10 | √ | 0 | 澄清价税合计 |
| 22 | fbestprice | 项目最优未税单价 | numeric | 23 | 10 | √ | 0 | 项目最优未税单价 |
| 23 | fclarifyamount | 澄清未税金额 | numeric | 23 | 10 | √ | 0 | 澄清未税金额 |
| 24 | ffirsttaxprice | 首轮含税单价 | numeric | 23 | 10 | √ | 0 | 首轮含税单价 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 27 | fpricediff | 价差 | numeric | 23 | 10 | √ | 0 | 价差 |
| 28 | fsrcbillno | 上游源单单号 | varchar | 50 |  | √ | ' ' | 上游源单单号 |
| 29 | fmaxtaxprice | 含税起标单价 | numeric | 23 | 10 | √ | 0 | 含税起标单价 |
| 30 | fmaxamount | 未税起标金额 | numeric | 23 | 10 | √ | 0 | 未税起标金额 |
| 31 | fmaxprice | 未税起标单价 | numeric | 23 | 10 | √ | 0 | 未税起标单价 |
| 32 | feffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 33 | freqsource | 需求来源 | bpchar | 1 |  | √ | '3' | 需求来源,枚举: 1 :寻源申请 2 :采购申请 3 :项目立项新增 4 :项目启动新增 |
| 34 | fcfmbaseqty | 定标基本数量 | numeric | 23 | 10 | √ | 0 | 定标基本数量 |
| 35 | ffirstamount | 首轮未税金额 | numeric | 23 | 10 | √ | 0 | 首轮未税金额 |
| 36 | fhistorytaxprice | 上轮含税报价 | numeric | 23 | 10 | √ | 0 | 上轮含税报价 |
| 37 | ffirsttaxamount | 首轮价税合计 | numeric | 23 | 10 | √ | 0 | 首轮价税合计 |
| 38 | floctaxamount | 本币价税合计 | numeric | 23 | 10 | √ | 0 | 本币价税合计 |
| 39 | fpretaxamount | 上轮价税合计 | numeric | 23 | 10 | √ | 0 | 上轮价税合计 |
| 40 | fquotedate | 供应商报价时间 | timestamp | 0 |  |  | null | 供应商报价时间 |
| 41 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 42 | floctaxprice | 本币含税单价 | numeric | 23 | 10 | √ | 0 | 本币含税单价 |
| 43 | fduedate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 44 | flocamount | 本币未税金额 | numeric | 23 | 10 | √ | 0 | 本币未税金额 |
| 45 | fusdprice | 项目最优含税单价 | numeric | 23 | 10 | √ | 0 | 项目最优含税单价 |
| 46 | fsourcebillid | 上游源单ID | varchar | 50 |  | √ | ' ' | 上游源单ID |
| 47 | fbuyernote | fbuyernote | varchar | 512 |  | √ | ' ' |  |
| 48 | fexchrate | 汇率(废弃) | numeric | 23 | 10 | √ | 0 | 汇率(废弃) |
| 49 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
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

## 采购清单查询-分表 t_src_purlistentry_a

- **表名称：** 采购清单查询-分表
- **表名：** t_src_purlistentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizitemld | 商务条款编码 | int8 | 64 |  | √ | 0 | [寻源商务条款 src_bizitem](../src_files/src_bizitem.md) |
| 3 | fremark | 商务条款备注 | varchar | 255 |  | √ | ' ' | 商务条款备注 |
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

## 采购清单查询-分表 t_src_purlistentry_z

- **表名称：** 采购清单查询-分表
- **表名：** t_src_purlistentry_z

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftendersideld | 招标方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcontract | fcontract | int8 | 64 |  | √ | 0 |  |
| 4 | fareaprice | fareaprice | numeric | 23 | 10 | √ | 0 |  |
| 5 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 6 | ffirstrank | 首轮排名 | int8 | 64 |  | √ | 0 | 首轮排名 |
| 7 | fnote1 | note1 | varchar | 500 |  | √ | ' ' | note1 |
| 8 | fnote2 | fnote2 | varchar | 50 |  | √ | ' ' |  |
| 9 | fnote3 | fnote3 | varchar | 50 |  | √ | ' ' |  |
| 10 | fcompkey | 组件名称 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fnumber1 | fnumber1 | int8 | 64 |  | √ | 0 |  |
| 12 | fnumber2 | fnumber2 | int8 | 64 |  | √ | 0 |  |
| 13 | fpurdate | 实际采购日期 | timestamp | 0 |  |  | null | 实际采购日期 |
| 14 | fprice5 | 定标价税合计 | numeric | 23 | 10 | √ | 0 | 定标价税合计 |
| 15 | fprice6 | 本币定标未税金额 | numeric | 23 | 10 | √ | 0 | 本币定标未税金额 |
| 16 | fprice3 | 最近含税交易单价 | numeric | 23 | 10 | √ | 0 | 最近含税交易单价 |
| 17 | fprice4 | 定标未税金额 | numeric | 23 | 10 | √ | 0 | 定标未税金额 |
| 18 | fprice9 | 竞价价差 | numeric | 23 | 10 | √ | 0 | 竞价价差 |
| 19 | fprice7 | 本币定标价税合计 | numeric | 23 | 10 | √ | 0 | 本币定标价税合计 |
| 20 | fprice8 | 竞价比例(%) | numeric | 23 | 10 | √ | 0 | 竞价比例(%) |
| 21 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 22 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 23 | freqfrequency | 需求频次 | bpchar | 1 |  | √ | ' ' | 需求频次,枚举: 1 :一次性需求 2 :持续性需求 |
| 24 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 25 | farea | farea | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprice1 | 单价1 | numeric | 23 | 10 | √ | 0 | 单价1 |
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
| 37 | flgortid | 仓库代码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 38 | fratio | 计算的配比 | numeric | 23 | 10 | √ | 0 | 计算的配比 |
| 39 | fwidth | fwidth | numeric | 23 | 10 | √ | 0 |  |
| 40 | fprice10 | 竞价区间从(>) | numeric | 23 | 10 | √ | 0 | 竞价区间从(>) |
| 41 | fprice11 | 竞价区间至(<) | numeric | 23 | 10 | √ | 0 | 竞价区间至(<) |
| 42 | fprice12 | 上次定标未税单价 | numeric | 23 | 10 | √ | 0 | 上次定标未税单价 |
| 43 | fprice13 | 上次定标含税单价 | numeric | 23 | 10 | √ | 0 | 上次定标含税单价 |
| 44 | fprice14 | 历史最优未税单价 | numeric | 23 | 10 | √ | 0 | 历史最优未税单价 |
| 45 | fprice15 | 历史最优含税单价 | numeric | 23 | 10 | √ | 0 | 历史最优含税单价 |
| 46 | freqdepart | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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

## 采购清单查询-主表 t_src_purlistentry

- **表名称：** 采购清单查询-主表
- **表名：** t_src_purlistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 5 | fsourceentryid | 上游源单分录ID | varchar | 50 |  | √ | ' ' | 上游源单分录ID |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | frebate | 返点(%) | numeric | 23 | 10 | √ | 0 | 返点(%) |
| 8 | fseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 |
| 11 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 14 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 15 | fisdiscardbid | 采购方允许弃标的 | bpchar | 1 |  | √ | '0' | 采购方允许弃标的 |
| 16 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 17 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 19 | fqtyfrom | 阶梯数量从(>) | numeric | 23 | 10 | √ | 0 | 阶梯数量从(>) |
| 20 | fpreorderratio | 预定标份额(%) | numeric | 23 | 10 | √ | 0 | 预定标份额(%) |
| 21 | fisnew | 新增标的 | bpchar | 1 |  | √ | '0' | 新增标的 |
| 22 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 27 | fdctrate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 28 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 29 | fisbizitem | 是否商务条款 | bpchar | 1 |  | √ | '0' | 是否商务条款 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 32 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 33 | fhistoryprice | 上轮未税报价 | numeric | 23 | 10 | √ | 0 | 上轮未税报价 |
| 34 | fsysresult | 系统推荐 | bpchar | 1 |  | √ | ' ' | 系统推荐,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 0 :流标 |
| 35 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 36 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 37 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 38 | fentryid | 明细分录ID | int8 | 64 |  | √ | 0 | 明细分录ID |
| 39 | fisdiscarded | 供应商确定弃标的 | bpchar | 1 |  | √ | '0' | 供应商确定弃标的 |
| 40 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 41 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 42 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 43 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 9 :预中标 |
| 44 | fprecfmqty | 预定标数量 | numeric | 23 | 10 | √ | 0 | 预定标数量 |
| 45 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 46 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 47 | fsuppliercode | 供应商代码 | bpchar | 50 |  | √ | ' ' | 供应商代码 |
| 48 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 49 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 50 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 51 | ffeerate | 费率(%) | numeric | 23 | 10 | √ | 0 | 费率(%) |
| 52 | fbidmaterialid | 原始需求名称 | int8 | 64 |  | √ | 0 | [项目立项分录F7 src_demandf7two](../src_files/src_demandf7two.md) |
| 53 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 54 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: 0 :待处理 1 :已处理 |
| 55 | fpkgamount | 标段未税金额(废弃) | numeric | 23 | 10 | √ | 0 | 标段未税金额(废弃) |
| 56 | fdistrictid | 片区 | int8 | 64 |  | √ | 0 | [片区与地区 pds_areadistrict](../pds_files/pds_areadistrict.md) |
| 57 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) |
| 58 | fpkgtaxamount | 标段价税合计(废弃) | numeric | 23 | 10 | √ | 0 | 标段价税合计(废弃) |
| 59 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 60 | fisdecision | 分批定标否 | bpchar | 1 |  | √ | '0' | 分批定标否 |
| 61 | forderratio | 定标份额(%) | numeric | 23 | 10 | √ | 0 | 定标份额(%) |
| 62 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 63 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 64 | fdecrease | 降幅(%) | numeric | 23 | 10 | √ | 0 | 降幅(%) |
| 65 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 66 | fqtyto | 阶梯数量至(≤) | numeric | 23 | 10 | √ | 0 | 阶梯数量至(≤) |
| 67 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 68 | fareaid | 地区 | int8 | 64 |  | √ | 0 | [片区与地区 pds_areadistrict](../pds_files/pds_areadistrict.md) |
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

## 采购方附件-附件表 t_src_purlistentry_fj

- **表名称：** 采购方附件-附件表
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
