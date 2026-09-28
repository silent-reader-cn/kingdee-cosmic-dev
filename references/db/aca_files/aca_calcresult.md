# 成本计算结果单-aca_calcresult

## 单据体-子表 t_aca_calcresultinventry

- **表名称：** 单据体-子表
- **表名：** t_aca_calcresultinventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finventoryamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 3 | fsourcebillentryid | 生产入库单分录ID | int8 | 64 |  | √ | 0 | 生产入库单分录ID |
| 4 | finvcostobjectid | 入库成本对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 5 | finvproducttype | 产品类型 | varchar | 2 |  | √ | 'C' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finventoryqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 8 | finvoutsourcetype | 委外成本类型 | varchar | 30 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 D :物料 |
| 9 | fgroupfield | 分组字段 | varchar | 60 |  | √ | ' ' | 分组字段,枚举: bd_auxproperty :辅助属性 bd_invtype :库存类型 |
| 10 | fgroupcategoryid | 分组类型ID | int8 | 64 |  | √ | 0 | 分组类型ID |
| 11 | finventorysubeleid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 12 | fsourcebillid | 生产入库单ID | int8 | 64 |  | √ | 0 | 生产入库单ID |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_resultinventry_fid |  | fid |
| 2 | idx_aca_calcresultinventry |  | fid,finventorysubeleid |
| 3 | pk_t_aca_calcresultinventry |  | fentryid |

---

## 成本计算结果单-主表 t_aca_calcresult

- **表名称：** 成本计算结果单-主表
- **表名：** t_aca_calcresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcalcreportid | 期末计算报告 | int8 | 64 |  | √ | 0 | 期末计算报告 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 14 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 15 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_calcresult_center |  | fcostcenterid |
| 2 | pk_t_aca_calcresult |  | fid |
| 3 | idx_aca_calcresult |  | fcreatetime,fcostaccountid |
| 4 | idx_aca_calcresult_cob |  | fcostobjectid |
| 5 | idx_aca_calcresult_o_c_p |  | forgid,fcostaccountid,fperiodid |

---

## 单据体-子表 t_aca_calcresultconventry

- **表名称：** 单据体-子表
- **表名：** t_aca_calcresultconventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fconvsrcbillentryid | 生产入库单分录ID | int8 | 64 |  | √ | 0 | 生产入库单分录ID |
| 5 | fconvgroupcategoryid | 分组类型ID | int8 | 64 |  | √ | 0 | 分组类型ID |
| 6 | fconvsubmatid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fconvoutsourcetype | 委外成本类型 | varchar | 50 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 D :物料 |
| 9 | fconvsubmatverid | 子项物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 10 | fconvcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 11 | fconvqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fconvproqty | 产品入库数量 | numeric | 23 | 10 | √ | 0 | 产品入库数量 |
| 13 | fconvsubauxptyid | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fconvproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 15 | fconvgroupfield | 分组字段 | varchar | 60 |  | √ | ' ' | 分组字段,枚举: bd_auxproperty :辅助属性 bd_invtype :库存类型 |
| 16 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fconvsrcbillid | 生产入库单ID | int8 | 64 |  | √ | 0 | 生产入库单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_calcresultconventry |  | fentryid |
| 2 | idx_aca_calcresconvet_costo |  | fconvcostobjectid |
| 3 | idx_aca_calcresultconventry_fk |  | fid |

---

## 单据体-子表 t_aca_calcresultentry

- **表名称：** 单据体-子表
- **表名：** t_aca_calcresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fyearsumcomuse | 单耗 | numeric | 23 | 10 | √ | 0 | 单耗 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fsubmatversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性定义 bd_auxproperty |
| 7 | ffeetype | 费用类型 | varchar | 30 |  | √ | ' ' | 费用类型,枚举: mfgFee :制造费用 materialFee :材料耗用费用 |
| 8 | fendadjqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fsumcomqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 11 | frelaproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 12 | fyearpdsumamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 13 | fmatversionid | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 14 | fpdcurramount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 15 | fpdstartqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fyearsumcomamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 17 | fpdendqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 18 | fsumcomunitcost | 单位成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位成本 |
| 19 | frelacostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 20 | fsubmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 21 | fendadjamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 22 | fcurrcomamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 23 | fstartadjqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | fyearpdsumqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 25 | fpdsumamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 26 | fcurrcomuse | 单耗 | numeric | 23 | 10 | √ | 0.0000000000 | 单耗 |
| 27 | fpdendamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 28 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 29 | fcurrcomunitcost | 单位成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位成本 |
| 30 | fyearsumcomqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 31 | foutsourcetype | 委外成本类型 | varchar | 30 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 D :物料 |
| 32 | fsumcomamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 33 | ftype | 汇总类型 | varchar | 30 |  | √ | ' ' | 汇总类型,枚举: finalResult :最终结果 detail :明细 |
| 34 | fyearsumcomunitcost | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 35 | fcurrcomqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 36 | fstartadjamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 37 | fsubauxpty | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 38 | fpdstartamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 39 | fsumcomuse | 单耗 | numeric | 23 | 10 | √ | 0.0000000000 | 单耗 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fpdsumqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 42 | fpdcurrqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_calcresultentry |  | fentryid |
| 2 | idx_aca_calcresultentry |  | fsubelementid,fmaterialid |
| 3 | idx_aca_calcresultentry_fid |  | fid |
