# 材料耗用分配-sco_matalloc

## 材料耗用分配-主表 t_sco_matalloc

- **表名称：** 材料耗用分配-主表
- **表名：** t_sco_matalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatcostinfoid | 物料成本信息ID | int8 | 64 |  | √ | 0 | 物料成本信息ID |
| 3 | fproductnum | 生产编码 | varchar | 255 |  | √ | ' ' | 生产编码 |
| 4 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本核算 aca :实际成本核算 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | fmatusesrcbillentryid | 材料耗用归集单源单分录id | int8 | 64 |  | √ | 0 | 材料耗用归集单源单分录id |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 14 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 sco_costdriver |
| 15 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 16 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 19 | fcostrecordentryid | 核算成本记录分录id | int8 | 64 |  | √ | 0 | 核算成本记录分录id |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | falloctorid | 分配人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 24 | fsrcauxptyid | 源单辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 25 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手动分配 |
| 28 | fproductid | 产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 29 | fuseamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 30 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 31 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 32 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 33 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 34 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |
| 35 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fmatcollectid | 材料归集单分录ID | int8 | 64 |  | √ | 0 | 材料归集单分录ID |
| 37 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 38 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 39 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 40 | fbiztype | 业务类型（旧） | varchar | 30 |  | √ | 'PRODUCTMATGET' | 业务类型（旧）,枚举: PRODUCTMATGET :生产领料 PRODUCTMATFALLBACK :生产领料退回 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fuseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 43 | fallocdim | fallocdim | varchar | 255 |  | √ | ' ' |  |
| 44 | fnsrcauditdate | 源单审核日期 | timestamp | 0 |  |  | null | 源单审核日期 |
| 45 | fisreturnitem | 返工 | varchar | 30 |  | √ | '0' | 返工 |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 sco_keycol |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fentrysrc | 分录数据来源 | varchar | 30 |  | √ | ' ' | 分录数据来源,枚举: calcres :卷算结果或物料成本信息 calrec :核实成本记录 |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | fusetype | 耗用类型 | varchar | 30 |  | √ | ' ' | 耗用类型,枚举: 1 :共耗 2 :直接 |
| 52 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 53 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 54 | fcollconfigid | fcollconfigid | int8 | 64 |  | √ | 0 |  |
| 55 | fallocatedate | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 56 | flotcoderuleid | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 57 | fsrcbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 58 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_matalloc2 |  | fcostaccountid,forgid,fperiodid |
| 2 | idx_sco_matalloc_kc |  | fkeycol |
| 3 | idx_sco_matalloc_matc |  | fmatcollectid |
| 4 | index_sco_matalloc |  | forgid,fcostcenterid |
| 5 | pk_sco_matalloc |  | fid |
| 6 | idx_sco_matalloc_co |  | fcostobjectid |

---

## 单据体-子表 t_sco_matallocentry

- **表名称：** 单据体-子表
- **表名：** t_sco_matallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 分配数量 | numeric | 23 | 10 | √ | 0 | 分配数量 |
| 3 | felemententryid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 4 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsubelemententryid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 7 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 8 | famount | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fprice | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_matallocentry |  | fentryid |
| 2 | idx_sco_matallocentry2 |  | fid |
| 3 | index_sco_matallocentry |  | fcostobjectid,fsubelemententryid |

---

## 子单据体-子表 t_sco_matallocsubentry

- **表名称：** 子单据体-子表
- **表名：** t_sco_matallocsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstandardamt | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fsubmatverisonid | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 4 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 7 | fsubqty | 子项耗用量 | numeric | 23 | 10 | √ | 0 | 子项耗用量 |
| 8 | fsubentrykeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |
| 9 | fcalcbasis | 计算依据 | varchar | 80 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 10 | fstandardcost | 标准单价 | numeric | 23 | 10 | √ | 0 | 标准单价 |
| 11 | fsubentrykeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 12 | fsubmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fsubauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_matallocsubentry2 |  | fentryid |
| 2 | pk_sco_matallocsubentry |  | fdetailid |
| 3 | index_sco_matalcsubentry |  | fsubelementid,fsubmaterialid |
