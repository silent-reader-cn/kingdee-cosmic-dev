# 采购申请单-pm_purapplybill

## 采购申请单-反写记录表 t_pm_purapplybill_wb

- **表名称：** 采购申请单-反写记录表
- **表名：** t_pm_purapplybill_wb

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
| 1 | idx_pm_purapplybill_wb_fk |  | fid |
| 2 | t_pm_purapplybill_wb_pkey |  | fentryid |

---

## 物料明细-分表 t_pm_purapplybillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_pm_purapplybillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货数量 |
| 3 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 4 | fjointracesourceqty | 关联寻源数量 | numeric | 23 | 10 | √ | 0 | 关联寻源数量 |
| 5 | ftracesourcetype | 寻源方式 | varchar | 50 |  | √ | ' ' | 寻源方式,枚举: INQUIRY :询价 BIDDING :竞价 INVITE_BIDS :招标 |
| 6 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库基本数量 |
| 7 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 8 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fconbillnumber | 合同编号 | varchar | 100 |  | √ | ' ' | 合同编号 |
| 11 | fexecutedamountandtax | 已执行价税合计 | numeric | 23 | 10 | √ | 0 | 已执行价税合计 |
| 12 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货基本数量 |
| 13 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 14 | forderqty | 已订货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已订货数量 |
| 15 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 17 | fconbillentryseq | 合同分录序号 | varchar | 50 |  | √ | ' ' | 合同分录序号 |
| 18 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 19 | favinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 20 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 21 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 24 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已订货基本数量 |
| 25 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 26 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 27 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 28 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 29 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 30 | ftracesourcestatus | 寻源状态 | varchar | 50 |  | √ | ' ' | 寻源状态,枚举: TRACING :寻源中 TRACED :已寻源 |
| 31 | fjoinpushamountandtax | 关联下推价税合计 | numeric | 23 | 10 | √ | 0 | 关联下推价税合计 |
| 32 | fjointracesourcebaseqty | 关联寻源基本数量 | numeric | 23 | 10 | √ | 0 | 关联寻源基本数量 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 34 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 35 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_pabillentry_r |  | fid |
| 2 | t_pm_purapplybillentry_r_pkey |  | fentryid |

---

## 物料明细-子表 t_pm_purapplybillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_purapplybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 5 | fassortbillno | 配套单据信息 | varchar | 2000 |  | √ | ' ' | 配套单据信息 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fisredordermate | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | frootdemandentryseq | 根需求单据分录行号 | int4 | 32 |  | √ | 0 | 根需求单据分录行号 |
| 10 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fpurdate | 建议采购日期 | timestamp | 0 |  |  | null | 建议采购日期 |
| 18 | fbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 19 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 20 | fqty | 核准数量 | numeric | 23 | 10 | √ | 0.0000000000 | 核准数量 |
| 21 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fentrymanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 26 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 27 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | fentrypurogid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fentrypurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 34 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 35 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 36 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 38 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 39 | fpurleadday | 采购提前期 | int4 | 32 |  | √ | 0 | 采购提前期 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 42 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 43 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 44 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 47 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 48 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 49 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 50 | frootdemandentity | 根需求单据实体 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 51 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 52 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 53 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 54 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 55 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 56 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 57 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 58 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 59 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 60 | frootdemandbillno | 根需求单据编码 | varchar | 120 |  | √ | ' ' | 根需求单据编码 |
| 61 | fpurmethod | 采购方式 | varchar | 5 |  | √ | ' ' | 采购方式,枚举: order :订单 mall :商城 sourc :寻源 |
| 62 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 63 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 64 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 65 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 66 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 67 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 68 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 69 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 70 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 71 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 72 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purapplybillentry |  | fid |
| 2 | idx_pm_prentry_matid |  | fmaterialid,fid |
| 3 | t_pm_purapplybillentry_pkey |  | fentryid |
| 4 | idx_pm_prentry_matastertid |  | fmaterialmasterid,fid |

---

## 采购申请单-主表 t_pm_purapplybill

- **表名称：** 采购申请单-主表
- **表名：** t_pm_purapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidstatus | 竞价状态 | varchar | 5 |  | √ | ' ' | 竞价状态,枚举: A :竞价中 B :已竞价 |
| 3 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 6 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 10 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 17 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |
| 18 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fbizuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 31 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 32 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 33 | fmanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 34 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | finquirystatus | 寻源状态 | varchar | 5 |  | √ | ' ' | 寻源状态,枚举: A :寻源中 B :已寻源 |
| 36 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 37 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 38 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purapplybilll_org |  | forgid,fbiztime,fbillno,fid |
| 2 | idx_pm_purapplybill_org |  | forgid,fbiztime,fbillno,fid |
| 3 | idx_pm_purapply_billno_org |  | fbillno,forgid |
| 4 | idx_pm_purapplybill_biztime |  | fbiztime |
| 5 | t_pm_purapplybill_pkey |  | fid |

---

## 采购申请单-多语言表 t_pm_purapplybill_l

- **表名称：** 采购申请单-多语言表
- **表名：** t_pm_purapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purapplybill_l |  | fid,flocaleid |
| 2 | t_pm_purapplybill_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_pm_purapplybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purapplybillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fapplyqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 9 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 10 | fapplyqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purapplybillentry_lk_pkey |  | fpkid |
| 2 | idx_pm_purapplybillentry_lk_fk |  | fentryid |

---

## 采购申请单-关联追踪表 t_pm_purapplybill_tc

- **表名称：** 采购申请单-关联追踪表
- **表名：** t_pm_purapplybill_tc

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
| 1 | t_pm_purapplybill_tc_pkey |  | fid |
| 2 | idx_pm_purapplybill_tc_tid |  | ftid |
| 3 | idx_pm_purapplybill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_pm_purapplybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purapplybill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purapplybill_lk_pkey |  | fpkid |
| 2 | idx_pm_purapplybill_lk_fk |  | fid |
