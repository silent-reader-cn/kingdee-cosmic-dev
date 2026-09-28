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
| 3 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库基本数量 |
| 4 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 5 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 6 | fexecutedamountandtax | 已执行价税合计 | numeric | 23 | 10 | √ | 0 | 已执行价税合计 |
| 7 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货基本数量 |
| 8 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 9 | forderqty | 已订货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已订货数量 |
| 10 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 11 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 12 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 13 | favinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 14 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 15 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 18 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已订货基本数量 |
| 19 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 20 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 21 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 22 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 23 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 24 | fjoinpushamountandtax | 关联下推价税合计 | numeric | 23 | 10 | √ | 0 | 关联下推价税合计 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 27 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |

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
| 4 | fassortbillno | 配套单据信息 | varchar | 2000 |  | √ | ' ' | 配套单据信息 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fisredordermate | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 10 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fpurdate | 建议采购日期 | timestamp | 0 |  |  | null | 建议采购日期 |
| 16 | fbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 17 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 18 | fqty | 核准数量 | numeric | 23 | 10 | √ | 0.0000000000 | 核准数量 |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 24 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fentrypurogid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fentrypurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 31 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 33 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 34 | fpurleadday | 采购提前期 | int4 | 32 |  | √ | 0 | 采购提前期 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 37 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 38 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 39 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 42 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 43 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 44 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 45 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 46 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 47 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 48 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 50 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 51 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 52 | fpurmethod | 采购方式 | varchar | 5 |  | √ | ' ' | 采购方式,枚举: order :订单 mall :商城 sourc :寻源 |
| 53 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 54 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 55 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 57 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 58 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 59 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 60 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 61 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 62 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

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
| 3 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 6 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 10 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 17 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbizuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 29 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 30 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 31 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | finquirystatus | 询价状态 | varchar | 5 |  | √ | ' ' | 询价状态,枚举: A :询价中 B :已询价 |
| 33 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 34 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 35 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
