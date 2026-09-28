# 完工产量归集-cad_factnedoutputbill

## 成本核算对象信息-子表 t_cad_factnedoutputentry

- **表名称：** 成本核算对象信息-子表
- **表名：** t_cad_factnedoutputentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 3 | flastqty | 上一次数量 | numeric | 23 | 10 | √ | 0.0000000000 | 上一次数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 6 | fplannedoutputid | 计划生产数量归集 | int8 | 64 |  | √ | 0 | 计划生产数量归集f7 cad_plannedoutputbillf7 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_finish_costobj |  | fcostobjectid |
| 2 | index_cad_factoutputentry |  | fid,fseq |
| 3 | t_cad_factnedoutputentry_pkey |  | fentryid |

---

## 成本信息-子表 t_cad_factnedoutcost

- **表名称：** 成本信息-子表
- **表名：** t_cad_factnedoutcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fsrcsyncdate | 源单同步日期 | timestamp | 0 |  |  | null | 源单同步日期 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fstdprice | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_factnedoutcost |  | fid,fentryid |
| 2 | idx_finishc_cotypesube |  | fcosttypeid,fsubelementid |
| 3 | pk_cad_factnedoutcost |  | fentryid |

---

## 完工产量归集-主表 t_cad_factnedoutputbill

- **表名称：** 完工产量归集-主表
- **表名：** t_cad_factnedoutputbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fcompletetype | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: EXCEL :模板引入 API :API接口 MANUAL :手工录入 WIPCOMPELETE :完工入库单 WIPCOMPELETEBACK :完工入库退回 PRODUCTCOMPELETE :生产入库单 PRODUCTCOMPELETEBACK :生产入库退回 WWGRK :委外完工入库单 CONFIG :按配置方案引入 |
| 7 | fqualitystatus | 质量状态 | varchar | 30 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不格品 C :待检品 D :报废品 |
| 8 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fsrcauditdate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 13 | fgradeprodgroupid | 等级品产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fnsrcauditdate | 来源单据审核日期 | timestamp | 0 |  |  | null | 来源单据审核日期 |
| 16 | fwareinorgid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 18 | fbatchid | 批次 | varchar | 60 |  | √ | ' ' | 批次 |
| 19 | fbillno | 单据编号 | varchar | 225 |  | √ | ' ' | 单据编号 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fsourcebillentryid | 来源单据单据体ID | int8 | 64 |  | √ | 0 | 来源单据单据体ID |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fversionid | 版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 27 | fsrcauxptyid | 源单辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 31 | fcompleteqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 32 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 33 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 34 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 35 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | 成本归集配置单 cad_costcollectconfig |
| 36 | fsourcebiztime | 来源单据业务日期 | timestamp | 0 |  |  | null | 来源单据业务日期 |
| 37 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 38 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fkeycol | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_finish_bookdate |  | fbookdate |
| 2 | idx_finish_costc |  | fcostcenterid |
| 3 | t_cad_factnedoutputbill_pkey |  | fid |
| 4 | index_cad_factnedoutputbill |  | forgid,fcostcenterid,fmaterialid |
| 5 | idx_finish_mat |  | fmaterialid |
