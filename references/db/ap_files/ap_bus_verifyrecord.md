# 暂估应付勾稽记录-ap_bus_verifyrecord

## 单据体-子表 t_ap_busverifyrecordentry

- **表名称：** 单据体-子表
- **表名：** t_ap_busverifyrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbackwfop | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 3 | fbillqty | 数量-主 | numeric | 23 | 10 | √ | 0 | 数量-主 |
| 4 | fasstcurrency | 币别-辅 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fassbillid | 单据ID-辅 | int8 | 64 |  | √ | 0 | 单据ID-辅 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fasstwoffbillid | 冲回单ID-辅 | int8 | 64 |  | √ | 0 | 冲回单ID-辅 |
| 8 | fbaseunit | 基本单位-主 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fverifyvalue | 本次核销字段值-主（隐藏） | numeric | 23 | 10 | √ | 0 | 本次核销字段值-主（隐藏） |
| 10 | fwoffbillentryid | 冲回单分录ID-主 | int8 | 64 |  | √ | 0 | 冲回单分录ID-主 |
| 11 | fmainwfinfo_tag | 核销详情-主_详情 | text | 0 |  |  | null | 核销详情-主_详情 |
| 12 | fbillno | 单据编号-主 | varchar | 50 |  | √ | ' ' | 单据编号-主 |
| 13 | fexpenseitemid | 费用项目-主 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | fassbillentryid | 单据分录ID-辅 | int8 | 64 |  | √ | 0 | 单据分录ID-辅 |
| 15 | fmainwfinfo | 核销详情-主 | varchar | 255 |  | √ | ' ' | 核销详情-主 |
| 16 | fasstbasecurrency | 本位币-辅 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fasstasstacttype | 往来类型-辅 | varchar | 30 |  | √ | ' ' | 往来类型-辅,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 18 | fasstbillbaseqty | 基本数量-辅 | numeric | 23 | 10 | √ | 0 | 基本数量-辅 |
| 19 | fasstmaterial | 物料编码-辅 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 20 | fbillid | 单据ID-主 | int8 | 64 |  | √ | 0 | 单据ID-主 |
| 21 | fasswfinfo | 核销详情-辅 | varchar | 255 |  | √ | ' ' | 核销详情-辅 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fpricetaxtotal | 应付金额-主 | numeric | 23 | 10 | √ | 0 | 应付金额-主 |
| 24 | funit | 计量单位-主 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fasstasstact | 往来单位-辅 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 26 | fasstpricetaxtotal | 应付金额-辅 | numeric | 23 | 10 | √ | 0 | 应付金额-辅 |
| 27 | fasstwoffbillentryid | 冲回单分录ID-辅 | int8 | 64 |  | √ | 0 | 冲回单分录ID-辅 |
| 28 | fasstbizdate | 业务日期-辅 | timestamp | 0 |  |  | null | 业务日期-辅 |
| 29 | fasstact | 往来单位-主 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | fmaterialid | 物料编码-主 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 31 | fbillbaseqty | 基本数量-主 | numeric | 23 | 10 | √ | 0 | 基本数量-主 |
| 32 | fasstexpenseitem | 费用项目-辅 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 33 | famount | 本次勾稽金额-主 | numeric | 23 | 10 | √ | 0 | 本次勾稽金额-主 |
| 34 | fasstbaseqty | 本次勾稽基本数量-辅 | numeric | 23 | 10 | √ | 0 | 本次勾稽基本数量-辅 |
| 35 | fasstactype | 往来类型-主 | varchar | 30 |  | √ | ' ' | 往来类型-主,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 36 | fassbillqty | 数量-辅 | numeric | 23 | 10 | √ | 0 | 数量-辅 |
| 37 | fverifyqty | 本次勾稽数量-主 | numeric | 23 | 10 | √ | 0 | 本次勾稽数量-主 |
| 38 | fassbillno | 单据编号-辅 | varchar | 50 |  | √ | ' ' | 单据编号-辅 |
| 39 | fassbilltype | 单据类型-辅 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 40 | fasstlocalamount | 本次勾稽金额(本位币)-辅 | numeric | 23 | 10 | √ | 0 | 本次勾稽金额(本位币)-辅 |
| 41 | flocalamount | 本次勾稽金额(本位币)-主 | numeric | 23 | 10 | √ | 0 | 本次勾稽金额(本位币)-主 |
| 42 | fassunit | 计量单位-辅 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 43 | fasswfinfo_tag | 核销详情-辅_详情 | text | 0 |  |  | null | 核销详情-辅_详情 |
| 44 | fcurrency | 币别-主 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 45 | fassverifyvalue | 本次核销字段值-辅（隐藏） | numeric | 23 | 10 | √ | 0 | 本次核销字段值-辅（隐藏） |
| 46 | fbasecurrency | 本位币-主 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 47 | fbillentryid | 单据分录ID-主 | int8 | 64 |  | √ | 0 | 单据分录ID-主 |
| 48 | fasstamount | 本次勾稽金额-辅 | numeric | 23 | 10 | √ | 0 | 本次勾稽金额-辅 |
| 49 | fbizdate | 业务日期-主 | timestamp | 0 |  |  | null | 业务日期-主 |
| 50 | fwoffbillid | 冲回单ID-主 | int8 | 64 |  | √ | 0 | 冲回单ID-主 |
| 51 | fbaseqty | 本次勾稽基本数量-主 | numeric | 23 | 10 | √ | 0 | 本次勾稽基本数量-主 |
| 52 | fasstverifyqty | 本次勾稽数量-辅 | numeric | 23 | 10 | √ | 0 | 本次勾稽数量-辅 |
| 53 | fasstbaseunit | 基本单位-辅 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 54 | fbilltype | 单据类型-主 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_apbus_vr_fid |  | fid |
| 2 | pk_t_ap_busverifyrecordentry |  | fentryid |

---

## 暂估应付勾稽记录-主表 t_ap_busverifyrecord

- **表名称：** 暂估应付勾稽记录-主表
- **表名：** t_ap_busverifyrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 核销批号 | varchar | 50 |  | √ | ' ' | 核销批号 |
| 3 | fverifytype | 勾稽类型 | varchar | 30 |  | √ | ' ' | 勾稽类型,枚举: auto :自动勾稽 manual :手工勾稽 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fwriteofftypeid | 核销类别ID | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 11 | fheadwfinfo | 核销详情 | varchar | 255 |  | √ | ' ' | 核销详情 |
| 12 | fwfnumber | 核销编码 | varchar | 30 |  | √ | ' ' | 核销编码 |
| 13 | fheadwfinfo_tag | 核销详情_详情 | text | 0 |  |  | null | 核销详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_busvr_fnumber |  | fwfnumber |
| 2 | pk_t_ap_busverifyrecord |  | fid |
