# 结算中间结果数据-ism_settlemiddledata

## 结算中间结果数据-分表 t_ism_settlemiddledata_s

- **表名称：** 结算中间结果数据-分表
- **表名：** t_ism_settlemiddledata_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fesupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 |
| 3 | ferelationentryid | 匹配的结算路径分录ID | int8 | 64 |  | √ | 0 | 匹配的结算路径分录ID |
| 4 | fearsettleentryid | 应收结算清单分录ID | int8 | 64 |  | √ | 0 | 应收结算清单分录ID |
| 5 | feinownerid | 调入货主 | int8 | 64 |  | √ | 0 | 调入货主 |
| 6 | fearsettleuniqueid | 应收结算清单唯一键 | varchar | 50 |  | √ | ' ' | 应收结算清单唯一键 |
| 7 | feinstockorgid | 调入库存组织 | int8 | 64 |  | √ | 0 | 调入库存组织 |
| 8 | fearacctorgid | 供货方核算组织 | int8 | 64 |  | √ | 0 | 供货方核算组织 |
| 9 | fematchkey | 匹配KEY值 | varchar | 255 |  | √ | ' ' | 匹配KEY值 |
| 10 | feapsettleuniqueid | 应付结算清单唯一键 | varchar | 50 |  | √ | ' ' | 应付结算清单唯一键 |
| 11 | feapsettleentryid | 应付结算清单分录ID | int8 | 64 |  | √ | 0 | 应付结算清单分录ID |
| 12 | feapmaterialmasterid | 应付物料MASTERID | int8 | 64 |  | √ | 0 | 应付物料MASTERID |
| 13 | feapsettleorgid | 需求方结算组织 | int8 | 64 |  | √ | 0 | 需求方结算组织 |
| 14 | feoutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 调出货主 |
| 15 | feacctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 会计核算体系 |
| 16 | fepriceruleid | 取价规则 | int8 | 64 |  | √ | 0 | 取价规则 |
| 17 | feoutstockorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | 调出库存组织 |
| 18 | fecustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 |
| 19 | feapacctorgid | 需求方核算组织 | int8 | 64 |  | √ | 0 | 需求方核算组织 |
| 20 | fearsettleorgid | 供货方结算组织 | int8 | 64 |  | √ | 0 | 供货方结算组织 |
| 21 | fematerialmasterid | 物料MASTERID | int8 | 64 |  | √ | 0 | 物料MASTERID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_settlemdata_s_mkey |  | fematchkey |
| 2 | pk_ism_settlemiddledata_s |  | fid |

---

## 结算中间结果数据-分表 t_ism_settlemiddledata_n

- **表名称：** 结算中间结果数据-分表
- **表名：** t_ism_settlemiddledata_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fedemtargetbilldate | 需求方内部交易单据日期 | timestamp | 0 |  |  | null | 需求方内部交易单据日期 |
| 3 | fesuptargetbilldate | 供方内部交易单据日期 | timestamp | 0 |  |  | null | 供方内部交易单据日期 |
| 4 | fedemtargetbilltype | 需求方内部交易单据类型 | int8 | 64 |  | √ | 0 | 需求方内部交易单据类型 |
| 5 | fedemtargetentitykey | 需方内部交易单据实体 | varchar | 50 |  | √ | ' ' | 需方内部交易单据实体 |
| 6 | fesuptargetentitykey | 供方内部交易单据实体 | varchar | 50 |  | √ | ' ' | 供方内部交易单据实体 |
| 7 | fesuptargetbotpid | 供方单据转换规则 | int8 | 64 |  | √ | 0 | 供方单据转换规则 |
| 8 | fedemtargetentryid | 需求方内部交易单据分录ID | int8 | 64 |  | √ | 0 | 需求方内部交易单据分录ID |
| 9 | fesuptargetentryid | 供方内部交易单据分录ID | int8 | 64 |  | √ | 0 | 供方内部交易单据分录ID |
| 10 | fesuptargetbillno | 供应方内部交易单据编号 | varchar | 100 |  | √ | ' ' | 供应方内部交易单据编号 |
| 11 | fedemtargetbotpid | 需方单据转换规则 | int8 | 64 |  | √ | 0 | 需方单据转换规则 |
| 12 | fedemtargetbiztype | 需方内部交易单据业务类型 | int8 | 64 |  | √ | 0 | 需方内部交易单据业务类型 |
| 13 | fedemtargetbillno | 需求方内部交易单据编号 | varchar | 100 |  | √ | ' ' | 需求方内部交易单据编号 |
| 14 | fesuptargetbillid | 供方内部交易单据ID | int8 | 64 |  | √ | 0 | 供方内部交易单据ID |
| 15 | fedemtargetbillid | 需求方内部交易单据ID | int8 | 64 |  | √ | 0 | 需求方内部交易单据ID |
| 16 | fesuptargetbiztype | 供方内部交易单据业务类型 | int8 | 64 |  | √ | 0 | 供方内部交易单据业务类型 |
| 17 | fesuptargetbilltype | 供方内部交易单据类型 | int8 | 64 |  | √ | 0 | 供方内部交易单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlemiddledata_n |  | fid |
| 2 | idx_ism_settlemdata_n_sid |  | fesuptargetbillid |

---

## 结算中间结果数据-分表 t_ism_settlemiddledata_p

- **表名称：** 结算中间结果数据-分表
- **表名：** t_ism_settlemiddledata_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fecuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 3 | feexratedate | 取价后的汇率日期 | timestamp | 0 |  |  | null | 取价后的汇率日期 |
| 4 | feapcurtaxamount | 应付税额（本位币） | numeric | 23 | 10 | √ | 0 | 应付税额（本位币） |
| 5 | feexratetable | 取价汇率表 | int8 | 64 |  | √ | 0 | 取价汇率表 |
| 6 | fearexrate | 取价后获取的供应方汇率 | numeric | 23 | 10 | √ | 0 | 取价后获取的供应方汇率 |
| 7 | feapcuramountandtax | 应付价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 应付价税合计（本位币） |
| 8 | fepriceqty | 计价单位数量 | numeric | 23 | 10 | √ | 0 | 计价单位数量 |
| 9 | feamount | 取价后计算的金额 | numeric | 23 | 10 | √ | 0 | 取价后计算的金额 |
| 10 | fetaxprice | 取价的含税单价 | numeric | 23 | 10 | √ | 0 | 取价的含税单价 |
| 11 | fepricematchtype | 取价匹配方式 | varchar | 50 |  | √ | ' ' | 取价匹配方式 |
| 12 | feapexratetable | 取价后需求方的汇率表 | int8 | 64 |  | √ | 0 | 取价后需求方的汇率表 |
| 13 | fepricesource | 取价来源 | varchar | 50 |  | √ | ' ' | 取价来源 |
| 14 | fecuramountandtax | 价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 价税合计（本位币） |
| 15 | feprice | 取价的单价 | numeric | 23 | 10 | √ | 0 | 取价的单价 |
| 16 | feapcuramount | 应付金额(本位币) | numeric | 23 | 10 | √ | 0 | 应付金额(本位币) |
| 17 | fesettlecurrencyid | 取价的币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fepriceunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | feisgift | 取价后是否赠品 | bpchar | 1 |  | √ | ' ' | 取价后是否赠品 |
| 20 | feapbasecurrencyid | 取价后的需求方本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fetaxrate | 取价的税率（%） | numeric | 23 | 10 | √ | 0 | 取价的税率（%） |
| 22 | fetaxrateid | 取价的税率ID | int8 | 64 |  | √ | 0 | 取价的税率ID |
| 23 | fepricequotation | 汇率换算方式 | varchar | 50 |  | √ | ' ' | 汇率换算方式 |
| 24 | fearbasecurrencyid | 取价后的供应方本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | feistax | 取价后是否含税 | bpchar | 1 |  | √ | ' ' | 取价后是否含税 |
| 26 | fegetsettleprice | 是否取了结算清单的价格 | bpchar | 1 |  | √ | ' ' | 是否取了结算清单的价格 |
| 27 | fecurtaxamount | 税额（本位币） | numeric | 23 | 10 | √ | 0 | 税额（本位币） |
| 28 | fetaxamount | 取价后计算的税额 | numeric | 23 | 10 | √ | 0 | 取价后计算的税额 |
| 29 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 30 | feapexrate | 取价后获取的需求方汇率 | numeric | 23 | 10 | √ | 0 | 取价后获取的需求方汇率 |
| 31 | feamountandtax | 取价后计算的价税合计 | numeric | 23 | 10 | √ | 0 | 取价后计算的价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlemiddledata_p |  | fid |
| 2 | idx_ism_settlemdata_p_psrc |  | fepricesource |

---

## 结算中间结果数据-主表 t_ism_settlemiddledata

- **表名称：** 结算中间结果数据-主表
- **表名：** t_ism_settlemiddledata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 |
| 4 | fneedar | 需要生成应收结算清单 | bpchar | 1 |  | √ | ' ' | 需要生成应收结算清单 |
| 5 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 6 | fdiscountrate | 折扣率 | numeric | 23 | 10 | √ | 0 | 折扣率 |
| 7 | fneedap | 需要生成应付结算清单 | bpchar | 1 |  | √ | ' ' | 需要生成应付结算清单 |
| 8 | fbizsupplierorg | 供应方组织 | int8 | 64 |  | √ | 0 | 供应方组织 |
| 9 | fmainbizorg | 单据主组织 | int8 | 64 |  | √ | 0 | 单据主组织 |
| 10 | fmainbillentity | 核心单据实体标识 | varchar | 50 |  | √ | ' ' | 核心单据实体标识 |
| 11 | fsuiteinnersettletype | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: |
| 12 | flocation | 仓位 | int8 | 64 |  | √ | 0 | 仓位 |
| 13 | fbizsettlejudgeid | 结算判定 | int8 | 64 |  | √ | 0 | 结算判定 |
| 14 | fbillentryseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 15 | fcorrespondbillid | 调拨对方单据ID | int8 | 64 |  | √ | 0 | 调拨对方单据ID |
| 16 | fbaseunit | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fdemandproject | 需求方项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fparentmaterialid | 父项产品 | int8 | 64 |  | √ | 0 | 父项产品 |
| 19 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 20 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 21 | fistax | 含税 | bpchar | 1 |  | √ | ' ' | 含税 |
| 22 | fcorrespondentitykey | 调拨对方单据实体标识 | varchar | 50 |  | √ | ' ' | 调拨对方单据实体标识 |
| 23 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 24 | fbizdirection | 业务方向 | varchar | 50 |  | √ | ' ' | 业务方向 |
| 25 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 |
| 26 | fparentmaterialmasterid | 父项产品MASTERID | int8 | 64 |  | √ | 0 | 父项产品MASTERID |
| 27 | fbizsettlerelation | 结算路径 | int8 | 64 |  | √ | 0 | 结算路径 |
| 28 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 |
| 29 | flot | 批号 | int8 | 64 |  | √ | 0 | 批号 |
| 30 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 采购组织 |
| 31 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 |
| 32 | fbillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 33 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 34 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 35 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 36 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 37 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 |
| 38 | fprocessplanid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划 |
| 39 | fprocessplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录 |
| 40 | fbizcustomerorg | 需求方组织 | int8 | 64 |  | √ | 0 | 需求方组织 |
| 41 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 42 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 43 | finvscheme | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 |
| 44 | froaddamageowner | 途损归属 | varchar | 50 |  | √ | ' ' | 途损归属,枚举: OutOwner :调出货主 InOwner :调入货主 |
| 45 | froaddamageqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 46 | fbizsettlejudgeprior | 结算判定优先级 | int8 | 64 |  | √ | 0 | 结算判定优先级 |
| 47 | fauditdate | 单据审核日期 | timestamp | 0 |  |  | null | 单据审核日期 |
| 48 | fisgift | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 49 | fmaterialmasterid | 物料主ID | int8 | 64 |  | √ | 0 | 物料主ID |
| 50 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 |
| 51 | fsettlecy | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 53 | freturntype | 退货类型 | varchar | 50 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 3 :仅退款不退货 |
| 54 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 55 | fbillid | 单据主键 | int8 | 64 |  | √ | 0 | 单据主键 |
| 56 | flinetype | 行类型 | int8 | 64 |  | √ | 0 | 行类型 |
| 57 | froaddamagebaseqty | 途损基本数量 | numeric | 23 | 10 | √ | 0 | 途损基本数量 |
| 58 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 59 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 60 | fmainbillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 61 | flotnumber | 批号文本 | varchar | 100 |  | √ | ' ' | 批号文本 |
| 62 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 63 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 |
| 64 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 65 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 66 | fbiztime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 67 | fstatus | 单据状态 | varchar | 20 |  | √ | ' ' | 单据状态 |
| 68 | fbiztype | 单据业务类型 | int8 | 64 |  | √ | 0 | 单据业务类型 |
| 69 | fquotation | 汇率换算方式 | int8 | 64 |  | √ | 0 | 汇率换算方式 |
| 70 | fisvirtualbill | 是否虚单 | bpchar | 1 |  | √ | ' ' | 是否虚单 |
| 71 | fcorrespondentryid | 调拨对方单据分录ID | int8 | 64 |  | √ | 0 | 调拨对方单据分录ID |
| 72 | ftaxrateid | 税率ID | int8 | 64 |  | √ | 0 | 税率ID |
| 73 | fsaleorg | 销售组织 | int8 | 64 |  | √ | 0 | 销售组织 |
| 74 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 75 | frevconfirmnodebill | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点 |
| 76 | fdiscounttype | 折扣类型 | varchar | 50 |  | √ | ' ' | 折扣类型 |
| 77 | fcreatetime | 单据创建日期 | timestamp | 0 |  |  | null | 单据创建日期 |
| 78 | fepricelist | 结算价目表 | int8 | 64 |  | √ | 0 | [组织间结算价目表 ism_settlepricelist](../ism_files/ism_settlepricelist.md) |
| 79 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 80 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: |
| 81 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 82 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 83 | fmidcreatetime | 中间结果的创建时间 | timestamp | 0 |  |  | null | 中间结果的创建时间 |
| 84 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 85 | frevconfirmnode | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点 |
| 86 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 87 | fmainbillentryid | 核心单据分录ID | int8 | 64 |  | √ | 0 | 核心单据分录ID |
| 88 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 89 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 90 | fbillentitykey | 单据实体标识 | varchar | 50 |  | √ | ' ' | 单据实体标识 |
| 91 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 92 | fbizbillbiztypeid | fbizbillbiztypeid | int8 | 64 |  | √ | 0 |  |
| 93 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性 |
| 94 | fbillkey | 唯一键 | varchar | 255 |  | √ | ' ' | 唯一键 |
| 95 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlemiddledata |  | fid |
| 2 | idx_ism_settlemiddledata |  | fsessionid |
