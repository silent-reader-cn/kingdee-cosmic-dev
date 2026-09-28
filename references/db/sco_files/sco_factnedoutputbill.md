# 完工产量归集-sco_factnedoutputbill

## 成本信息-子表 t_sco_factnedoutcost

- **表名称：** 成本信息-子表
- **表名：** t_sco_factnedoutcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fentrykeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fstdprice | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 9 | fentrykeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 sco_keycol](../sco_files/sco_keycol.md) |
| 10 | fmatcostid | 物料成本信息id | int8 | 64 |  | √ | 0 | 物料成本信息id |
| 11 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | fsrcsyncdate | 源单同步日期 | timestamp | 0 |  |  | null | 源单同步日期 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_factnedoutcost |  | fid,fentryid |
| 2 | pk_sco_factnedoutcost |  | fentryid |
| 3 | idx_finishc_keycol |  | fentrykeycol |
| 4 | idx_finishc_matcostid |  | fmatcostid |

---

## 成本核算对象信息-子表 t_sco_factnedoutputentry

- **表名称：** 成本核算对象信息-子表
- **表名：** t_sco_factnedoutputentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 3 | flastqty | 上一次数量 | numeric | 23 | 10 | √ | 0 | 上一次数量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fplannedoutputid | 计划生产数量归集 | int8 | 64 |  | √ | 0 | [计划生产数量归集f7 sco_plannedoutputbillf7](../sco_files/sco_plannedoutputbillf7.md) |
| 6 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_factoutputentry |  | fid,fseq |
| 2 | pk_sco_factnedoutputentry |  | fentryid |

---

## 完工产量归集-主表 t_sco_factnedoutputbill

- **表名称：** 完工产量归集-主表
- **表名：** t_sco_factnedoutputbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证/冲销 | varchar | 50 |  | √ | ' ' | 凭证/冲销,枚举: 1 :凭证 -1 :冲销 |
| 3 | forgid | 核算组织(废弃-20240329多核算体系改造) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fcompletetype | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: EXCEL :模板导入 API :API接口 MANUAL :手工录入 WIPCOMPELETE :完工入库单 WIPCOMPELETEBACK :完工入库退回 PRODUCTCOMPELETE :生产入库单 PRODUCTCOMPELETEBACK :生产入库退回 WWGRK :委外完工入库单 CONFIG :按配置方案导入 |
| 6 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fgradeprodgroupid | 等级品产品组 | int8 | 64 |  | √ | 0 | [产品组 sco_productweight](../sco_files/sco_productweight.md) |
| 10 | fdevcost | 研发费用 | bpchar | 1 |  |  | '0' | 研发费用,枚举: 0 :否 1 :是 |
| 11 | fwareinorgid | 入库货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fownertype | 入库货主类型 | varchar | 255 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 15 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 16 | fsourcebillentryid | 来源单据单据体ID | int8 | 64 |  | √ | 0 | 来源单据单据体ID |
| 17 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fversionid | 版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 21 | fsrcauxptyid | 源单辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | foutinvstatus | foutinvstatus | int8 | 64 |  | √ | 0 |  |
| 26 | fsourcebiztime | 来源单据业务日期 | timestamp | 0 |  |  | null | 来源单据业务日期 |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |
| 31 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 32 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 34 | fqualitystatus | 质量状态 | varchar | 30 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不格品 C :待检品 D :报废品 |
| 35 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 36 | fsrcauditdate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 37 | fbonded | 保税 | bpchar | 1 |  |  | '0' | 保税 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fnsrcauditdate | 来源单据审核时间 | timestamp | 0 |  |  | null | 来源单据审核时间 |
| 40 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 41 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 sco_keycol](../sco_files/sco_keycol.md) |
| 42 | fbatchid | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fproducttype | 产品类型(废弃) | varchar | 30 |  | √ | ' ' | 产品类型(废弃),枚举: C :主产品 A :联产品 B :副产品 |
| 47 | fowner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fcompleteqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 49 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 50 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 51 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 52 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | [成本归集配置单 cad_costcollectconfig](../aca_files/cad_costcollectconfig.md) |
| 53 | finvstatus | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_finish_keycol |  | fkeycol |
| 2 | pk_sco_factnedoutputbill |  | fid |
| 3 | index_sco_factnedoutputbill |  | forgid,fcostcenterid,fmaterialid |
