# 发货通知单-sm_delivernotice

## 发货通知单-关联追踪表 t_sm_delivernotice_tc

- **表名称：** 发货通知单-关联追踪表
- **表名：** t_sm_delivernotice_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delivernotice_tc_tid |  | ftid |
| 2 | t_sm_delivernotice_tc_pkey |  | fid |
| 3 | idx_sm_delivernotice_tc_tbill |  | ftbillid |

---

## 物料明细-子表 t_sm_delivernoticeentry

- **表名称：** 物料明细-子表
- **表名：** t_sm_delivernoticeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货超发比率(%) |
| 3 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 4 | fexpectqtydate | 获取可发量日期 | timestamp | 0 |  |  | null | 获取可发量日期 |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 6 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 7 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fdeliverratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货欠发比率(%) |
| 11 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 12 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fdeliverbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限基本数量 |
| 14 | frowstatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 15 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 18 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fexpectqty | 预计可发量 | numeric | 23 | 10 | √ | 0 | 预计可发量 |
| 23 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 24 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  | √ | ' ' | 尾差调整日志 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 29 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fqtyunit2nd | 主辅数量 | numeric | 23 | 10 | √ | 0.0000000000 | 主辅数量 |
| 36 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 38 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 39 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 40 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 41 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 42 | fmaterialinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 43 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 45 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 46 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 47 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 49 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 50 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 51 | fmaterialname | 物料名称(历史) | varchar | 800 |  | √ | ' ' | 物料名称(历史) |
| 52 | frowclosemanual | 行手工关闭 | bpchar | 1 |  | √ | '0' | 行手工关闭 |
| 53 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 55 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 56 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 57 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 58 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 59 | funit2ndid | 主辅单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 60 | funit2ndrate | 换算率(主辅单位) | numeric | 23 | 10 | √ | 0.0000000000 | 换算率(主辅单位) |
| 61 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 62 | fk_bj73_qtyfield | 关联物流数量 | numeric | 23 | 10 |  | null | 关联物流数量 |
| 63 | fdeliverqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限数量 |
| 64 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 65 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 66 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 67 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 68 | frowclosemanualever | 是否手工行关闭过 | bpchar | 1 |  | √ | '0' | 是否手工行关闭过 |
| 69 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 70 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 71 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 72 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 73 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 74 | fdeliverbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限基本数量 |
| 75 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 76 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 77 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 78 | fcloseupdatesaleorder | 手工关闭更新订单 | bpchar | 1 |  | √ | '0' | 手工关闭更新订单 |
| 79 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 80 | fdeliverydate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 81 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 82 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 83 | fk_bj73_checkboxfield | fk_bj73_checkboxfield | bpchar | 1 |  | √ | '0' |  |
| 84 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 85 | fdeliverqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限数量 |
| 86 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 87 | fk_bj73_pricefield | 销售参考价 | numeric | 23 | 10 |  | null | 销售参考价 |
| 88 | fdeliverinspect | 发货检验 | bpchar | 1 |  | √ | '0' | 发货检验 |
| 89 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 90 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 91 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 92 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delientry_fownerid |  | fownerid |
| 2 | idx_sm_delientry_matid |  | fmaterialid,fid |
| 3 | t_sm_delivernoticeentry_pkey |  | fentryid |
| 4 | idx_sm_delientry_matmasterid |  | fmaterialmasterid,fid |
| 5 | idx_sm_delientry_fid |  | fid |

---

## 物料明细-分表 t_sm_delivernoticeentry_r

- **表名称：** 物料明细-分表
- **表名：** t_sm_delivernoticeentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvfailqty | 关联不合格出库数量 | numeric | 23 | 10 | √ | 0 | 关联不合格出库数量 |
| 3 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 4 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 5 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 6 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 7 | fk_bj73_textfield5 | 物流状态 | varchar | 50 |  | √ | ' ' | 物流状态 |
| 8 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | ffailqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 10 | finvbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库基本数量 |
| 11 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 12 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 13 | fremaininvqty | fremaininvqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 15 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 16 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 17 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 18 | fassoinvinspectbaseqty | 关联请检基本数量 | numeric | 23 | 10 | √ | 0 | 关联请检基本数量 |
| 19 | ffailsaleableqty | 不合格可销售数量 | numeric | 23 | 10 | √ | 0 | 不合格可销售数量 |
| 20 | fpassbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 21 | ftransportbaseqty | 已运输基本数量 | numeric | 23 | 10 | √ | 0 | 已运输基本数量 |
| 22 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 23 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 24 | fpassqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 25 | ftransportqty | 已运输数量 | numeric | 23 | 10 | √ | 0 | 已运输数量 |
| 26 | fconbillentryseq | 合同分录序号 | int8 | 64 |  | √ | 0 | 合同分录序号 |
| 27 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 28 | finvpassqty | 关联合格出库数量 | numeric | 23 | 10 | √ | 0 | 关联合格出库数量 |
| 29 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 30 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 31 | finvqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 32 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 33 | fremaininvbaseqty | fremaininvbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 35 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 36 | finvpassbaseqty | 关联合格出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联合格出库基本数量 |
| 37 | fassotransportqty | 关联运输数量 | numeric | 23 | 10 | √ | 0 | 关联运输数量 |
| 38 | fsrcsysbillentryid | 来源系统单据分录id | varchar | 100 |  | √ | ' ' | 来源系统单据分录id |
| 39 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 40 | fassotransportbaseqty | 关联运输基本数量 | numeric | 23 | 10 | √ | 0 | 关联运输基本数量 |
| 41 | fassoinvinspectqty | 关联请检数量 | numeric | 23 | 10 | √ | 0 | 关联请检数量 |
| 42 | ffailbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0 | 不合格基本数量 |
| 43 | ffailsaleablebaseqty | 不合格可销售基本数量 | numeric | 23 | 10 | √ | 0 | 不合格可销售基本数量 |
| 44 | fscrapbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 46 | fsrcsysbillid | 来源系统单据id | varchar | 100 |  | √ | ' ' | 来源系统单据id |
| 47 | finvfailbaseqty | 关联不合格出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联不合格出库基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_delivernoticeentry_r_pkey |  | fentryid |
| 2 | idx_sm_delientry_r_fid |  | fid |

---

## 关联子实体-子表 t_sm_delivernoticeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_delivernoticeentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delivernoticeentry_lk_fk |  | fentryid |
| 2 | t_sm_delivernoticeentry_lk_pkey |  | fpkid |

---

## 发货通知单-主表 t_sm_delivernotice

- **表名称：** 发货通知单-主表
- **表名：** t_sm_delivernotice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 客户联系地址 | varchar | 512 |  |  | ' ' | 客户联系地址 |
| 3 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 8 | fk_bj73_printcountfield | 打印次数 | int8 | 64 |  | √ | '0' | 打印次数 |
| 9 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 10 | fgtmpacked | 已生成装箱单 | bpchar | 1 |  | √ | '0' | 已生成装箱单 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fconsigngencrossorg | 委托代销生成跨组织发出 | bpchar | 1 |  | √ | '0' | 委托代销生成跨组织发出 |
| 15 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :正常 B :已终止 |
| 16 | fcominvoiced | 已生成商业发票 | bpchar | 1 |  | √ | '0' | 已生成商业发票 |
| 17 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 18 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 19 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 20 | fk_bj73_checkboxfield1 | 预发货 | bpchar | 1 |  | √ | '0' | 预发货 |
| 21 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 23 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 24 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 25 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fdeliverpatternid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 30 | ftraderouteid | 贸易路线 | int8 | 64 |  | √ | 0 | [贸易路线 sbs_traderoute](../sbs_files/sbs_traderoute.md) |
| 31 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 32 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 33 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | flinkaddressf7 | 客户联系地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 36 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 40 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 41 | finvgroupid | 库存组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 42 | fk_bj73_textfield4 | 收货地址 | varchar | 200 |  | √ | ' ' | 收货地址 |
| 43 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 44 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 45 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 46 | fk_bj73_textfield2 | 考核省区 | varchar | 50 |  | √ | ' ' | 考核省区 |
| 47 | fk_bj73_textfield3 | 考核大区 | varchar | 50 |  | √ | ' ' | 考核大区 |
| 48 | fendbill | 尾单 | bpchar | 1 |  | √ | '0' | 尾单 |
| 49 | fbiztime | 通知日期 | timestamp | 0 |  |  | null | 通知日期 |
| 50 | fk_bj73_textfield1 | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 51 | fdeliverdeptid | 发货部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 52 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fterminaterid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fisvirtualbill | 是否虚单 | bpchar | 1 |  | √ | '0' | 是否虚单 |
| 56 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 57 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 58 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 59 | fdeliveroperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 60 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 61 | freceiveaddress_bak | 发货明细执行地址(后台用) | varchar | 512 |  | √ | ' ' | 发货明细执行地址(后台用) |
| 62 | fdeclareformed | 已生成报关单 | bpchar | 1 |  | √ | '0' | 已生成报关单 |
| 63 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 64 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 65 | fstep | 当前步骤 | int4 | 32 |  | √ | 0 | 当前步骤 |
| 66 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 67 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 70 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 71 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 72 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 73 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 74 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 75 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 76 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 77 | fclosemanual | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 78 | flogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 79 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 80 | fisexport | 出口 | bpchar | 1 |  | √ | '0' | 出口 |
| 81 | fk_bj73_textfield | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 82 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 83 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 84 | fgtmladed | 已生成提单 | bpchar | 1 |  | √ | '0' | 已生成提单 |
| 85 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 86 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 87 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 88 | freceiveaddress | 收货地址 | varchar | 512 |  |  | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delinotice_fbiztime |  | fbiztime |
| 2 | idx_sm_delinotice_customer |  | fcustomerid |
| 3 | t_sm_delivernotice_pkey |  | fid |
| 4 | idx_uniq_delinotice_billnoorg |  | fbillno,fdeliverorgid |
| 5 | idx_sm_delinotice_forgid |  | forgid,fbiztime,fbillno,fid |

---

## 发货通知单-反写记录表 t_sm_delivernotice_wb

- **表名称：** 发货通知单-反写记录表
- **表名：** t_sm_delivernotice_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delivernotice_wb_fk |  | fid |
| 2 | t_sm_delivernotice_wb_pkey |  | fentryid |

---

## 发货通知单-分表 t_sm_delivernotice_d

- **表名称：** 发货通知单-分表
- **表名：** t_sm_delivernotice_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_bj73_textfield6 | fk_bj73_textfield6 | varchar | 50 |  | √ | ' ' |  |
| 3 | finvgroupid | finvgroupid | int8 | 64 |  | √ | 0 |  |
| 4 | faddress | faddress | varchar | 512 |  |  | ' ' |  |
| 5 | fk_bj73_datetimefield | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 6 | fdeliverpatternid | fdeliverpatternid | int8 | 64 |  | √ | 0 |  |
| 7 | freclinkmanid | freclinkmanid | int8 | 64 |  | √ | 0 |  |
| 8 | fdeliverdeptid | fdeliverdeptid | int8 | 64 |  | √ | 0 |  |
| 9 | fk_bj73_checkboxfield | 第四批单 | bpchar | 1 |  | √ | '0' | 第四批单 |
| 10 | fpayingcustomerid | fpayingcustomerid | int8 | 64 |  | √ | 0 |  |
| 11 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 12 | fdeliverorgid | fdeliverorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fdeliveroperatorid | fdeliveroperatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fsettlecustomerid | fsettlecustomerid | int8 | 64 |  | √ | 0 |  |
| 15 | freccustomerid | freccustomerid | int8 | 64 |  | √ | 0 |  |
| 16 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 17 | freceiveaddress | freceiveaddress | varchar | 512 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delinotice_d_sid |  | fdeliverorgid |
| 2 | idx_sm_delinotice_d_customer |  | fcustomerid |
| 3 | t_sm_delivernotice_d_pkey |  | fid |

---

## 发货通知单-分表 t_sm_delivernotice_f

- **表名称：** 发货通知单-分表
- **表名：** t_sm_delivernotice_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_bj73_textfield6 | 审核备注 | varchar | 50 |  | √ | ' ' | 审核备注 |
| 3 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 4 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 5 | fistax | fistax | bpchar | 1 |  | √ | '0' |  |
| 6 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 8 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 9 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 10 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 11 | frecconditionid | frecconditionid | int8 | 64 |  | √ | 0 |  |
| 12 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 13 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delinotice_f_settid |  | fsettletypeid,fsettleorgid |
| 2 | t_sm_delivernotice_f_pkey |  | fid |

---

## 发货通知单-分表 t_sm_delivernotice_m

- **表名称：** 发货通知单-分表
- **表名：** t_sm_delivernotice_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccmexcessamount | 预估信用超标额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标额度 |
| 3 | fccmexcessdays | 预估信用超标天数 | numeric | 23 | 10 | √ | 0 | 预估信用超标天数 |
| 4 | fccmexcessoveramount | 预估信用超标逾期额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标逾期额度 |
| 5 | fccmexcessbillamount | 预估信用超标单笔限额 | numeric | 23 | 10 | √ | 0 | 预估信用超标单笔限额 |
| 6 | fccmupdatetime | 预估信用超标时点 | timestamp | 0 |  |  | null | 预估信用超标时点 |
| 7 | fccmunsettlecount | 信用未结批数 | int4 | 32 |  | √ | 0 | 信用未结批数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delivernotice_m_t |  | fccmupdatetime |
| 2 | pk_sm_delivernotice_m |  | fid |

---

## 发货通知单-多语言表 t_sm_delivernotice_l

- **表名称：** 发货通知单-多语言表
- **表名：** t_sm_delivernotice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_delivernotice_l_pkey |  | fpkid |
| 2 | idx_sm_delinotice_l_fid |  | fid,flocaleid |
