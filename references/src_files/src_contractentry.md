# 签约分录(采购清单)-src_contractentry

## 签约分录(采购清单)-分表 t_src_contractentry_a

- **表名称：** 签约分录(采购清单)-分表
- **表名：** t_src_contractentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fsalorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 5 | fpreresult | 预定标结果 | bpchar | 1 |  | √ | ' ' | 预定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 |
| 6 | fprecfmqty | fprecfmqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fsourceentryid | 上游源单分录ID | varchar | 50 |  | √ | ' ' | 上游源单分录ID |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fcontractbaseqty | 已签合同基本数量 | numeric | 23 | 10 | √ | 0 | 已签合同基本数量 |
| 10 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fminipackqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 12 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 13 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fcostdetail | 成本明细 | bpchar | 1 |  | √ | '0' | 成本明细,枚举: |
| 15 | fpurorderno | fpurorderno | varchar | 80 |  | √ | ' ' |  |
| 16 | fcfmbaseqty | 定标基本数量 | numeric | 23 | 10 | √ | 0 | 定标基本数量 |
| 17 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fpreorderratio | fpreorderratio | numeric | 23 | 10 | √ | 0 |  |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fisnew | 新增标的 | bpchar | 1 |  | √ | '0' | 新增标的 |
| 21 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 22 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbdsupplierid | 供应商库(bd_supplier) | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fprice5 | 定标价税合计 | numeric | 23 | 10 | √ | 0 | 定标价税合计 |
| 25 | fprice6 | 本币定标未税金额 | numeric | 23 | 10 | √ | 0 | 本币定标未税金额 |
| 26 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | fprice4 | 定标未税金额 | numeric | 23 | 10 | √ | 0 | 定标未税金额 |
| 28 | fprice7 | 本币定标价税合计 | numeric | 23 | 10 | √ | 0 | 本币定标价税合计 |
| 29 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0 | 已订货基本数量 |
| 30 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 31 | fprotocolqty | 关联协议数量 | numeric | 23 | 10 | √ | 0 | 关联协议数量 |
| 32 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 33 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 34 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 37 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

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

## 签约分录(采购清单)-主表 t_src_contractentry

- **表名称：** 签约分录(采购清单)-主表
- **表名：** t_src_contractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 签约单F7 src_contractf7 |
| 2 | fsuppliernumber | 供应商ID | varchar | 50 |  | √ | ' ' | 供应商ID |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0 | 税率(%) |
| 4 | floccurrid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | frebate | 返点(%) | numeric | 19 | 6 | √ | 0 | 返点(%) |
| 7 | fseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 8 | flocprice | 未税单价(本位币) | numeric | 23 | 10 | √ | 0 | 未税单价(本位币) |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fcontractqty | 关联合同数量 | numeric | 23 | 10 | √ | 0 | 关联合同数量 |
| 11 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 |
| 13 | fexchtypeid | 汇率(废弃) | int8 | 64 |  | √ | 0 | 汇率 bd_exrate_tree |
| 14 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 15 | fpricelistno | 价目表编号 | varchar | 50 |  | √ | ' ' | 价目表编号 |
| 16 | fcfmqty | 定标数量 | numeric | 23 | 10 | √ | 0 | 定标数量 |
| 17 | fsourcelistid | 货源清单分录ID | varchar | 50 |  | √ | ' ' | 货源清单分录ID |
| 18 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 19 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 20 | fqtyfrom | 阶梯数量(从) | numeric | 23 | 10 | √ | 0 | 阶梯数量(从) |
| 21 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 24 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0 | 折扣率(%) |
| 25 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 28 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 29 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 30 | fsysresult | 系统推荐 | bpchar | 1 |  | √ | ' ' | 系统推荐,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 |
| 31 | factprice | 实际未税单价 | numeric | 23 | 10 | √ | 0 | 实际未税单价 |
| 32 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 33 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 34 | fcontracttaxamt | 关联合同价税合计 | numeric | 23 | 10 | √ | 0 | 关联合同价税合计 |
| 35 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 38 | frank | 排名 | int4 | 32 |  | √ | 0 | 排名 |
| 39 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 40 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 41 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 42 | fmaxtaxprice | 起标价(含税) | numeric | 23 | 10 | √ | 0 | 起标价(含税) |
| 43 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 44 | fmaterialgroupid | 寻源标的分类 | int8 | 64 |  | √ | 0 | 标的分类 src_materialgroup |
| 45 | fsourcelistno | 货源清单编号 | varchar | 50 |  | √ | ' ' | 货源清单编号 |
| 46 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 47 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 48 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 49 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 50 | fmaxprice | 起标价(不含税) | numeric | 23 | 10 | √ | 0 | 起标价(不含税) |
| 51 | feffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 52 | ftranscost | 运费 | numeric | 23 | 10 | √ | 0 | 运费 |
| 53 | freqsource | 需求来源 | bpchar | 1 |  | √ | '3' | 需求来源,枚举: 1 :寻源申请 2 :采购申请 3 :项目立项新增 4 :项目启动新增 |
| 54 | fbidmaterialid | 原始需求名称 | int8 | 64 |  | √ | 0 | 项目立项分录F7 src_demandf7two |
| 55 | ffeerate | 费率(%) | numeric | 19 | 6 | √ | 0 | 费率(%) |
| 56 | fpricelistid | 价目表分录ID | varchar | 50 |  | √ | ' ' | 价目表分录ID |
| 57 | fpkgamount | 标段未税金额 | numeric | 23 | 10 | √ | 0 | 标段未税金额 |
| 58 | fdistrictid | 片区 | int8 | 64 |  | √ | 0 | 片区与地区 pds_areadistrict |
| 59 | fpkgtaxamount | 标段价税合计 | numeric | 23 | 10 | √ | 0 | 标段价税合计 |
| 60 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 61 | forderqty | 关联订单数量 | numeric | 23 | 10 | √ | 0 | 关联订单数量 |
| 62 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 63 | fordertaxamt | 关联订单价税合计 | numeric | 23 | 10 | √ | 0 | 关联订单价税合计 |
| 64 | forderratio | 份额(%) | numeric | 19 | 6 | √ | 0 | 份额(%) |
| 65 | fprice_uom | 价格单位 | int4 | 32 |  | √ | 0 | 价格单位 |
| 66 | floctaxprice | 含税单价(本位币) | numeric | 23 | 10 | √ | 0 | 含税单价(本位币) |
| 67 | flgortid | 仓库代码 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 68 | fcontractamt | 关联合同未税金额 | numeric | 23 | 10 | √ | 0 | 关联合同未税金额 |
| 69 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 70 | fduedate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 71 | fdecrease | 降幅(%) | numeric | 19 | 6 | √ | 0 | 降幅(%) |
| 72 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 73 | flocamount | 未税金额(本位币) | numeric | 23 | 10 | √ | 0 | 未税金额(本位币) |
| 74 | fqtyto | 阶梯数量(至) | numeric | 23 | 10 | √ | 0 | 阶梯数量(至) |
| 75 | forderamt | 关联订单未税金额 | numeric | 23 | 10 | √ | 0 | 关联订单未税金额 |
| 76 | fsourcebillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 77 | fareaid | 地区 | int8 | 64 |  | √ | 0 | 片区与地区 pds_areadistrict |
| 78 | fexchrate | 汇率值(废弃) | numeric | 19 | 6 | √ | 0 | 汇率值(废弃) |
| 79 | fbuyernote | fbuyernote | varchar | 512 |  | √ | ' ' |  |
| 80 | fcurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 81 | fvieamount | 竞价金额 | numeric | 23 | 10 | √ | 0 | 竞价金额 |
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
