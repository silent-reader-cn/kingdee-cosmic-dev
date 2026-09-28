# 材料耗用分配-aca_matalloc

## 材料耗用分配-主表 t_sca_matalloc

- **表名称：** 材料耗用分配-主表
- **表名：** t_sca_matalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatcostinfoid | 物料成本信息 | int8 | 64 |  | √ | 0 | 物料成本信息 |
| 3 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmatcollectid | 材料归集单分录ID | int8 | 64 |  | √ | 0 | 材料归集单分录ID |
| 5 | fproductnum | 生产编码 | varchar | 255 |  | √ | ' ' | 生产编码 |
| 6 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 10 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本核算 aca :实际成本核算 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 14 | fbiztype | 业务类型（旧） | varchar | 30 |  | √ | 'PRODUCTMATGET' | 业务类型（旧）,枚举: PRODUCTMATGET :生产领料 PRODUCTMATFALLBACK :生产领料退回 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fuseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 18 | fmatusesrcbillentryid | 材料耗用归集单源单分录id | int8 | 64 |  | √ | 0 | 材料耗用归集单源单分录id |
| 19 | fisreturnitem | 返工 | varchar | 30 |  | √ | '0' | 返工 |
| 20 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 23 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 26 | fentrysrc | 分录数据来源 | varchar | 30 |  | √ | ' ' | 分录数据来源,枚举: calcres :卷算结果或物料成本信息 calrec :核实成本记录 |
| 27 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 28 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | falloctorid | 分配人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fvouchernum | 凭证号 | varchar | 100 |  | √ | ' ' | 凭证号 |
| 33 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 34 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 35 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手动分配 |
| 36 | fusetype | 耗用类型 | varchar | 30 |  | √ | ' ' | 耗用类型,枚举: 1 :共耗 2 :直接 |
| 37 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 38 | fproductid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 39 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 40 | fuseamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 41 | fallocatedate | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 42 | flotcoderuleid | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 43 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 44 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 45 | fsrcbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 46 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 47 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 48 | fkeycol | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_matalloc_co |  | fcostobjectid |
| 2 | idx_cad_matalloc_fkeycol |  | fkeycol |
| 3 | idx_matalloc_mat |  | fmaterialid |
| 4 | index_sca_matalloc |  | forgid,fcostcenterid |
| 5 | idx_sca_matalloc2 |  | fcostaccountid,forgid,fperiodid |
| 6 | idx_sca_matalloc_matc |  | fmatcollectid |
| 7 | idx_matalloc_bookdate |  | fbookdate |
| 8 | t_sca_matalloc_pkey |  | fid |

---

## 单据体-子表 t_sca_matallocentry

- **表名称：** 单据体-子表
- **表名：** t_sca_matallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 分配数量 | numeric | 23 | 10 | √ | 0.0000000000 | 分配数量 |
| 3 | felemententryid | 成本要素-废弃 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 4 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0.0000000000 | 分配标准值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsubelemententryid | 成本子要素-废弃 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 7 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 8 | famount | 分配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配金额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fprice | 单位成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_matallocentry_pkey |  | fentryid |
| 2 | index_sca_matallocentry |  | fcostobjectid,fsubelemententryid |
| 3 | idx_sca_matallocentry2 |  | fid |

---

## 子单据体-子表 t_sca_matallocsubentry

- **表名称：** 子单据体-子表
- **表名：** t_sca_matallocsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstandardamt | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fsubmatverisonid | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 4 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 7 | fsubqty | 子项耗用量 | numeric | 23 | 10 | √ | 0.0000000000 | 子项耗用量 |
| 8 | fcalcbasis | 计算依据 | varchar | 60 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 9 | fstandardcost | 标准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 标准单价 |
| 10 | fsubmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fsubauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_matallocsubentry_pkey |  | fdetailid |
| 2 | idx_sca_matallocsubentry2 |  | fentryid |
| 3 | index_sca_matalcsubentry |  | fsubelementid,fsubmaterialid |

---

## 子单据体-子表 t_sca_elementsubentry

- **表名称：** 子单据体-子表
- **表名：** t_sca_elementsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fismfg | 是否制造费用 | int4 | 32 |  | √ | 0 | 是否制造费用 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | famountforelement | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_elementsubentry |  | fdetailid |
| 2 | idx_sca_elementsubentry |  | fentryid |
