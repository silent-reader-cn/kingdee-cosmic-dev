# 应收结算清单-ism_arsettlebill

## 单据体-分表 t_ism_arsettlebillentry_b

- **表名称：** 单据体-分表
- **表名：** t_ism_arsettlebillentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmidid | 取价策略取价分录ID | int8 | 64 |  | √ | 0 | 取价策略取价分录ID |
| 3 | finnerbillno | 内部交易单据编号 | varchar | 50 |  | √ | ' ' | 内部交易单据编号 |
| 4 | funiqueid | 唯一标识（应收应付匹配） | varchar | 100 |  | √ | ' ' | 唯一标识（应收应付匹配） |
| 5 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 6 | finnerbillentryid | 内部交易单据分录ID | int8 | 64 |  | √ | 0 | 内部交易单据分录ID |
| 7 | fbizbillno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 8 | fcorebillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 9 | finnerbillentityid | 内部交易单据名称 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 10 | finnerbilltypeid | 内部交易单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 11 | finnerbillid | 内部交易单据ID | int8 | 64 |  | √ | 0 | 内部交易单据ID |
| 12 | fcorebillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 13 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 14 | fbizbillentityid | 业务单据名称 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 15 | fcorebillrowseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 16 | fbizbilltypeid | 业务单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 17 | fbizbillseq | 业务单据行号 | int8 | 64 |  | √ | 0 | 业务单据行号 |
| 18 | fbizbilldate | 业务单据日期 | timestamp | 0 |  |  | null | 业务单据日期 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 21 | fcorebillrowid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_arsettlebillentry_b |  | fentryid |
| 2 | idx_ism_arsetety_bizdate |  | fbizbilldate |
| 3 | idx_ism_arsettlebillety_b |  | fid |
| 4 | idx_ism_arsetety_bizid |  | fbizbillentityid,fbizbillid |

---

## 单据体-子表 t_ism_arsettlebillentry

- **表名称：** 单据体-子表
- **表名：** t_ism_arsettlebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | frelatebaseqty | 应收基本数量 | numeric | 23 | 10 | √ | 0 | 应收基本数量 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fbizcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 7 | fseq | 分录行号 | numeric | 23 | 10 | √ | 0 | 分录行号 |
| 8 | ftotalcost | 总成本本位币 | numeric | 23 | 10 | √ | 0 | 总成本本位币 |
| 9 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | ' ' | 含税 |
| 12 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fcuramount | 金额本位币 | numeric | 23 | 10 | √ | 0 | 金额本位币 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | finownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fresidueqty | 剩余应收数量 | numeric | 23 | 10 | √ | 0 | 剩余应收数量 |
| 19 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 23 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 25 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fbizsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 29 | fcuramountandtax | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 30 | fresiduebaseqty | 剩余应收基本数量 | numeric | 23 | 10 | √ | 0 | 剩余应收基本数量 |
| 31 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 34 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 36 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 37 | fhasarbusbill | 是否生成暂估应收单 | bpchar | 1 |  | √ | ' ' | 是否生成暂估应收单 |
| 38 | famount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 39 | fsettledirection | 结算方向 | varchar | 50 |  | √ | ' ' | 结算方向,枚举: 0 :普通 1 :退货 |
| 40 | fprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |
| 41 | finnerbilldate | 内部交易单据日期 | timestamp | 0 |  |  | null | 内部交易单据日期 |
| 42 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 43 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 44 | fpricelist | 结算价目表 | int8 | 64 |  | √ | 0 | 组织间结算价目表 ism_settlepricelist |
| 45 | frelateqty | 应收数量 | numeric | 23 | 10 | √ | 0 | 应收数量 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | foutownertype | 调出货主类型 | varchar | 50 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 48 | fsettlesource | 取价来源 | varchar | 50 |  | √ | ' ' | 取价来源,枚举: 2 :来源业务单据价格 3 :来源订单价格 6 :指定固定价格 7 :实际成本价 8 :结算价目表 9 :结算取价策略 5 :自定义插件 |
| 49 | fismanualprice | 手工改价 | bpchar | 1 |  | √ | '0' | 手工改价 |
| 50 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 51 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 52 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 53 | fbizmainorgid | 单据主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 54 | fcurtaxamount | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 55 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 56 | finnerbiztype | 内部交易单据业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 57 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 58 | fconfirmrectiming | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 59 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 60 | finownertype | 调入货主类型 | varchar | 50 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_arsettlebillentry |  | fentryid |
| 2 | idx_ism_arsettlebillentry |  | fid |

---

## 应收结算清单-主表 t_ism_arsettlebill

- **表名称：** 应收结算清单-主表
- **表名：** t_ism_arsettlebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 4 | faraptype | 应收应付类型 | varchar | 50 |  | √ | ' ' | 应收应付类型,枚举: ar :应收 ap :应付 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fbizenddate | 业务截止日期 | timestamp | 0 |  |  | null | 业务截止日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fhasapbusbill | fhasapbusbill | bpchar | 1 |  | √ | ' ' |  |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fisdefaultaccsys | 是否默认核算体系 | bpchar | 1 |  | √ | ' ' | 是否默认核算体系 |
| 12 | fsupplierid | 对应供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsessionid | 创建线程ID | varchar | 50 |  | √ | ' ' | 创建线程ID |
| 16 | fmaporgid | 需求方核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmapsettleorgid | 需求方结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcustomerid | 对应客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_arsettlebill |  | fid |
| 2 | idx_ism_arsetbill_edate |  | fbizenddate |
| 3 | idx_ism_arsettlebill |  | forgid |
