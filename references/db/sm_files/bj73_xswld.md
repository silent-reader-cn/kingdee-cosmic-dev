# 销售物流单-bj73_xswld

## 关联子实体-子表 tk_bj73_xswldbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** tk_bj73_xswldbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_xswldbillentry_lk |  | fpkid |
| 2 | idx__bj73_xswldbillentry_lk_fk |  | fentryid |

---

## 单据体-子表 tk_bj73_xswldbillentry

- **表名称：** 单据体-子表
- **表名：** tk_bj73_xswldbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 |  | null | 关联基本数量 |
| 3 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 4 | fk_bj73_basedatafield | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 2 |  | null | 税率(%) |
| 6 | fdiscountrate | 单位折扣(率) | numeric | 23 | 6 |  | null | 单位折扣(率) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  |  | null | 来源单据分录序号 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fparentproduct | 父项产品 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fmainbillid | 核心单据ID | int8 | 64 |  |  | null | 核心单据ID |
| 15 | fcuramount | 金额(本位币) | numeric | 23 | 10 |  | null | 金额(本位币) |
| 16 | fentrysettleorgid | 结算组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fpriceandtax | 含税单价 | numeric | 23 | 10 |  | null | 含税单价 |
| 21 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  | √ | ' ' | 尾差调整日志 |
| 22 | fqty | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 |  | null | 税额 |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 25 | fprojectid | 项目编码 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  |  | null | 来源单据ID |
| 27 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 28 | funitid | 销售单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fmaterialmasterid | 物料 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fownerid | 货主 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 33 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 |  | null | 辅助数量(2) |
| 34 | fparentrowid | 父项行ID | int8 | 64 |  |  | null | 父项行ID |
| 35 | flotid | 批号主档 | int8 | 64 |  |  | null | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 36 | fauxqty | 辅助数量 | numeric | 23 | 10 |  | null | 辅助数量 |
| 37 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 |  | null | 价税合计(本位币) |
| 38 | fmaterialinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 39 | fsalesorgid | 销售组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 |  | null | 基本单位用量：分母 |
| 41 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 43 | flinetypeid | 行类型 | int8 | 64 |  |  | null | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 44 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 45 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 46 | frowclosestatus | 行关闭状态 | varchar | 50 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 47 | fconbillid | 合同ID | int8 | 64 |  |  | null | 合同ID |
| 48 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 |  | null | 基本单位用量：分子 |
| 49 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  |  | null | 核心单据分录序号 |
| 50 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 51 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 52 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 53 | fdiscountamount | 折扣额 | numeric | 23 | 10 |  | null | 折扣额 |
| 54 | fconbillentryid | 合同行ID | int8 | 64 |  |  | null | 合同行ID |
| 55 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 56 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  |  | null | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 57 | fk_bj73_textfield2 | fk_bj73_textfield2 | varchar | 50 |  | √ | ' ' |  |
| 58 | fprice | 单价 | numeric | 23 | 10 |  | null | 单价 |
| 59 | fk_bj73_textfield3 | fk_bj73_textfield3 | varchar | 50 |  | √ | ' ' |  |
| 60 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 61 | fauxunitid | 辅助单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 62 | ftaxrateid | 税率 | int8 | 64 |  |  | null | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  |  | null | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 64 | fbomentryid | BOM分录ID | int8 | 64 |  |  | null | BOM分录ID |
| 65 | fauxunit2id | 辅助单位(2) | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 66 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 67 | fconbillentryseq | 合同分录序号 | int8 | 64 |  |  | null | 合同分录序号 |
| 68 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 69 | fsuitepricepercent | 套件价格拆分比例% | numeric | 15 | 2 |  | null | 套件价格拆分比例% |
| 70 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 71 | famountandtax | 价税合计 | numeric | 23 | 10 |  | null | 价税合计 |
| 72 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 73 | fassociatedqty | 关联数量 | numeric | 23 | 10 |  | null | 关联数量 |
| 74 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  |  | null | 来源单据行ID |
| 75 | frowterminatestatus | 行终止状态 | varchar | 50 |  | √ | ' ' | 行终止状态,枚举: |
| 76 | flocationid | 仓位 | int8 | 64 |  |  | null | [仓位 bd_location](../sbd_files/bd_location.md) |
| 77 | fmainbillentryid | 核心单据行ID | int8 | 64 |  |  | null | 核心单据行ID |
| 78 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 |  | null | 税额(本位币) |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 |  | null | 基本数量 |
| 80 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__bj73_xswldbillentry_fk |  | fid |
| 2 | pk__bj73_xswldbillentry |  | fentryid |

---

## 销售物流单-关联追踪表 tk_bj73_xswld_tc

- **表名称：** 销售物流单-关联追踪表
- **表名：** tk_bj73_xswld_tc

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
| 1 | idx_tk_bj73_xswld_tc_tbill |  | ftbillid |
| 2 | pk__bj73_xswld_tc |  | fid |
| 3 | idx_tk_bj73_xswld_tc_tid |  | ftid |

---

## 销售物流单-主表 tk_bj73_xswld

- **表名称：** 销售物流单-主表
- **表名：** tk_bj73_xswld

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | faddress | 客户联系地址 | varchar | 300 |  | √ | ' ' | 客户联系地址 |
| 3 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 销售组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fk_bj73_printcountfield | 打印次数 | int8 | 64 |  | √ | '0' | 打印次数 |
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
| 21 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 22 | flinkmanid | 联系人 | int8 | 64 |  |  | null | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 23 | fsettleorgid | 结算组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | flinkaddressf7 | 客户联系地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 25 | fsettlecurrencyid | 结算币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | ftotaltaxamount | 税额 | numeric | 23 | 10 |  | null | 税额 |
| 27 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  |  | null | 单据类型 bos_billtype |
| 29 | fcustomerid | 订货客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 30 | foperatorid | 销售员 | int8 | 64 |  |  | null | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 31 | freclinkmanid | 收货联系人 | int8 | 64 |  |  | null | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 32 | fbiztime | 业务日期(封存) | timestamp | 0 |  |  | null | 业务日期(封存) |
| 33 | fk_bj73_textfield1 | 收货地址 | varchar | 200 |  | √ | ' ' | 收货地址 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fpayingcustomerid | 付款客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 36 | fbiztypeid | 业务类型 | int8 | 64 |  |  | null | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 37 | frecconditionid | 收款条件 | int8 | 64 |  |  | null | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 38 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 39 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | foperatorgroupid | 销售组 | int8 | 64 |  |  | null | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 43 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 |  | null | 价税合计(本位币) |
| 44 | flastupdateuserid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 45 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 46 | fclosestatus | 关闭状态 | varchar | 50 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 47 | fsettletypeid | 结算方式 | int8 | 64 |  |  | null | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 48 | fpaymode | 付款方式 | varchar | 50 |  | √ | ' ' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 49 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 50 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 51 | fk_bj73_textfield | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 52 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 53 | fsettlecustomerid | 结算客户 | int8 | 64 |  |  | null | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 54 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 55 | fcurrencyid | 本位币 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 56 | ftotalallamount | 价税合计 | numeric | 23 | 10 |  | null | 价税合计 |
| 57 | freceiveaddress | 收货地址 | varchar | 300 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_xswld |  | fid |

---

## 销售物流单-反写记录表 tk_bj73_xswld_wb

- **表名称：** 销售物流单-反写记录表
- **表名：** tk_bj73_xswld_wb

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
| 1 | pk__bj73_xswld_wb |  | fentryid |
| 2 | idx__bj73_xswld_wb_fk |  | fid |

---

## 销售物流单-多语言表 tk_bj73_xswld_l

- **表名称：** 销售物流单-多语言表
- **表名：** tk_bj73_xswld_l

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
| 1 | pk__bj73_xswld_l |  | fpkid |
| 2 | idx__bj73_xswld_l_0 |  | fid,flocaleid |
