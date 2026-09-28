# 销售处理单-bj73_xscld

## 销售处理单-主表 tk_bj73_xscld

- **表名称：** 销售处理单-主表
- **表名：** tk_bj73_xscld

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | faddress | 客户联系地址 | varchar | 300 |  | √ | ' ' | 客户联系地址 |
| 3 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  |  | null |  |
| 4 | forgid | 销售组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fcancelstatus | fcancelstatus | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 |  | null | 汇率 |
| 11 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 |  | null | 金额(本位币) |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  |  | null | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fcloserid | 关闭人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | freccustomerid | 收货客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 15 | fdeliveraddressf7 | 收货地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fdeptid | 销售部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 21 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 22 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 23 | flinkmanid | 联系人 | int8 | 64 |  |  | null | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 24 | fsettleorgid | 结算组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fk_bj73_currencyfield | fk_bj73_currencyfield | int8 | 64 |  |  | null |  |
| 26 | flinkaddressf7 | 客户联系地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 27 | fsettlecurrencyid | 结算币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | ftotaltaxamount | 税额 | numeric | 23 | 10 |  | null | 税额 |
| 29 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  |  | null | 单据类型 bos_billtype |
| 31 | fcustomerid | 订货客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 32 | foperatorid | 销售员 | int8 | 64 |  |  | null | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 33 | freclinkmanid | 收货联系人 | int8 | 64 |  |  | null | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 34 | fbiztime | 业务日期(封存) | timestamp | 0 |  |  | null | 业务日期(封存) |
| 35 | fcancelerid | fcancelerid | int8 | 64 |  |  | null |  |
| 36 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fpayingcustomerid | 付款客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 38 | fbiztypeid | 业务类型 | int8 | 64 |  |  | null | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 39 | frecconditionid | 收款条件 | int8 | 64 |  |  | null | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 40 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | foperatorgroupid | 销售组 | int8 | 64 |  |  | null | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 45 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 |  | null | 价税合计(本位币) |
| 46 | fbizuserid | fbizuserid | int8 | 64 |  |  | null |  |
| 47 | flastupdateuserid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 48 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 49 | fk_bj73_settletype | fk_bj73_settletype | int8 | 64 |  |  | null |  |
| 50 | fclosestatus | 关闭状态 | varchar | 50 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 51 | fsettletypeid | 结算方式 | int8 | 64 |  |  | null | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 52 | fpaymode | 付款方式 | varchar | 50 |  | √ | ' ' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 53 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 54 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 55 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 56 | fsettlecustomerid | 结算客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 57 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 58 | fcurrencyid | 本位币 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 59 | ftotalallamount | 价税合计 | numeric | 23 | 10 |  | null | 价税合计 |
| 60 | freceiveaddress | 收货地址 | varchar | 300 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_xscld |  | fid |

---

## 销售处理单-多语言表 tk_bj73_xscld_l

- **表名称：** 销售处理单-多语言表
- **表名：** tk_bj73_xscld_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_xscld_l |  | fpkid |
| 2 | idx__bj73_xscld_l_0 |  | fid,flocaleid |

---

## 单据体-子表 tk_bj73_xscldbillentry

- **表名称：** 单据体-子表
- **表名：** tk_bj73_xscldbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 |  | null | 关联基本数量 |
| 3 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 4 | fentrymodifytime | fentrymodifytime | timestamp | 0 |  |  | null |  |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 2 |  | null | 税率(%) |
| 6 | fdiscountrate | 单位折扣(率) | numeric | 23 | 6 |  | null | 单位折扣(率) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentrycreatorid | fentrycreatorid | int8 | 64 |  |  | null |  |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  |  | null | 来源单据分录序号 |
| 12 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | fparentproduct | 父项产品 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  |  | null | 核心单据ID |
| 16 | fcuramount | 金额(本位币) | numeric | 23 | 10 |  | null | 金额(本位币) |
| 17 | fentrysettleorgid | 结算组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fentrymodifierid | fentrymodifierid | int8 | 64 |  |  | null |  |
| 19 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 20 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fpriceandtax | 含税单价 | numeric | 23 | 10 |  | null | 含税单价 |
| 23 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  | √ | ' ' | 尾差调整日志 |
| 24 | fqty | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 25 | ftaxamount | 税额 | numeric | 23 | 10 |  | null | 税额 |
| 26 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 27 | fprojectid | 项目编码 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fsrcbillid | 来源单据ID | int8 | 64 |  |  | null | 来源单据ID |
| 29 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 30 | funitid | 销售单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fauxunitid2 | fauxunitid2 | int8 | 64 |  |  | null |  |
| 32 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 33 | fwarehouseid | 仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fmaterialmasterid | 物料 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 35 | fentrycreatetime | fentrycreatetime | timestamp | 0 |  |  | null |  |
| 36 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 |  | null | 辅助数量(2) |
| 37 | fownerid | 货主 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 38 | fparentrowid | 父项行ID | int8 | 64 |  |  | null | 父项行ID |
| 39 | fauxqty | 辅助数量 | numeric | 23 | 10 |  | null | 辅助数量 |
| 40 | flotid | 批号主档 | int8 | 64 |  |  | null | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 41 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 |  | null | 价税合计(本位币) |
| 42 | fmaterialinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 43 | fsalesorgid | 销售组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 |  | null | 基本单位用量：分母 |
| 45 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 47 | flinetypeid | 行类型 | int8 | 64 |  |  | null | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 48 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 49 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 50 | frowclosestatus | 行关闭状态 | varchar | 50 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 51 | fconbillid | 合同ID | int8 | 64 |  |  | null | 合同ID |
| 52 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 |  | null | 基本单位用量：分子 |
| 53 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  |  | null | 核心单据分录序号 |
| 54 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 55 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 56 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 57 | fdiscountamount | 折扣额 | numeric | 23 | 10 |  | null | 折扣额 |
| 58 | fconbillentryid | 合同行ID | int8 | 64 |  |  | null | 合同行ID |
| 59 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 60 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  |  | null | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 61 | fprice | 单价 | numeric | 23 | 10 |  | null | 单价 |
| 62 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 63 | fauxunitid | 辅助单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 64 | ftaxrateid | 税率 | int8 | 64 |  |  | null | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 65 | ftracknumberid | 跟踪号 | int8 | 64 |  |  | null | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 66 | fbomentryid | BOM分录ID | int8 | 64 |  |  | null | BOM分录ID |
| 67 | fauxunit2id | 辅助单位(2) | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 68 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 69 | fconbillentryseq | 合同分录序号 | int8 | 64 |  |  | null | 合同分录序号 |
| 70 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 71 | fsuitepricepercent | 套件价格拆分比例% | numeric | 15 | 2 |  | null | 套件价格拆分比例% |
| 72 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 73 | famountandtax | 价税合计 | numeric | 23 | 10 |  | null | 价税合计 |
| 74 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 75 | fassociatedqty | 关联数量 | numeric | 23 | 10 |  | null | 关联数量 |
| 76 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  |  | null | 来源单据行ID |
| 77 | frowterminatestatus | 行终止状态 | varchar | 50 |  | √ | ' ' | 行终止状态,枚举: |
| 78 | flocationid | 仓位 | int8 | 64 |  |  | null | [仓位 bd_location](../sbd_files/bd_location.md) |
| 79 | fmainbillentryid | 核心单据行ID | int8 | 64 |  |  | null | 核心单据行ID |
| 80 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 |  | null | 税额(本位币) |
| 81 | fentrycomment | fentrycomment | varchar | 512 |  | √ | ' ' |  |
| 82 | fbaseqty | 基本数量 | numeric | 23 | 10 |  | null | 基本数量 |
| 83 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_xscldbillentry |  | fentryid |
| 2 | idx__bj73_xscldbillentry_fk |  | fid |
