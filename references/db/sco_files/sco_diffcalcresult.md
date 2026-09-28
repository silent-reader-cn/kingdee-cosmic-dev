# 差异分摊计算结果-sco_diffcalcresult

## 差异分摊计算综合明细-子表 t_sco_comdiffresultentry

- **表名称：** 差异分摊计算综合明细-子表
- **表名：** t_sco_comdiffresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeycol1id | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 3 | fstartactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 4 | fcurrinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 5 | frelacostobjectid1 | 所属成本对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 6 | fcurrqty1 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 7 | fstartreservediffx1 | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 8 | fcurrdiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fcurrmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 11 | fcurrunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 12 | fkeycol1 | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |
| 13 | fcurrreservediffw1 | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 14 | fstartotherdiff1 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 15 | fcurrreservediffy1 | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 16 | fsrcbillid1 | fsrcbillid1 | int8 | 64 |  | √ | 0 |  |
| 17 | fcurramt1 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 18 | fstartmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 19 | fstartorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 20 | fstartqty1 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | felementid1 | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 22 | fmaterialid1 | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 23 | fstartmadeupamt1 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 24 | fstartinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 25 | fsubelementid1 | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 26 | fstartdiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 27 | fstartstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 28 | fcompfeediff1 | fcompfeediff1 | numeric | 23 | 10 | √ | 0 |  |
| 29 | fsrcseq1 | fsrcseq1 | int8 | 64 |  | √ | 0 |  |
| 30 | fstartreservediffy1 | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 31 | fstartreservediffw1 | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 32 | fstartunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 33 | fcurrfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 34 | fcurrstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 35 | fcurrreservediffx1 | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 36 | fstartfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 37 | fcurrmadeupamt1 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 38 | fcurractcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 39 | fbaseunitid1 | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | fsrcbillno1 | fsrcbillno1 | varchar | 80 |  | √ | ' ' |  |
| 41 | ftype1 | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :明细行 5 :综合行 |
| 42 | fmatversionid1 | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 43 | fcurrorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 44 | fstartamt1 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fauxptyid1 | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 47 | fcurrotherdiff1 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_comdiffresultentry |  | fid |
| 2 | idx_sco_comdiffresultery_mat |  | fmaterialid1 |
| 3 | pk_sco_comdiffresultentry |  | fentryid |
| 4 | idx_sco_comdiffresulte_obj |  | frelacostobjectid1 |
| 5 | idx_sco_comdiffresulte_tp |  | ftype1 |

---

## 差异分摊计算结果-主表 t_sco_diffcalcresult

- **表名称：** 差异分摊计算结果-主表
- **表名：** t_sco_diffcalcresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrqtys | 本期数量 | numeric | 23 | 10 | √ | 0 | 本期数量 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcalcreportid | 期末计算报告 | int8 | 64 |  | √ | 0 | 期末计算报告 |
| 5 | fbizstatus | 结算状态 | varchar | 30 |  | √ | ' ' | 结算状态,枚举: A :未结算 B :已结算 |
| 6 | fendqtys | 期末数量 | numeric | 23 | 10 | √ | 0 | 期末数量 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 10 | fstartqtys | 期初数量 | numeric | 23 | 10 | √ | 0 | 期初数量 |
| 11 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 14 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 18 | fisunallocdiff | 是否未分摊差异 | bpchar | 1 |  | √ | '0' | 是否未分摊差异 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fentryproductid | 产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 21 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 22 | fcompqtys | 本期完工数量 | numeric | 23 | 10 | √ | 0 | 本期完工数量 |
| 23 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 24 | ftotalqtys | 累计数量 | numeric | 23 | 10 | √ | 0 | 累计数量 |
| 25 | fcurrencyid | 账簿币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_diffcalcresult |  | fid |
| 2 | idx_sco_diffcalcresult |  | forgid,fcostaccountid |
| 3 | idx_sco_diffcalcresult_cosb |  | fcostobjectid |

---

## 下阶差异-子表 t_sco_subdiffresultentry

- **表名称：** 下阶差异-子表
- **表名：** t_sco_subdiffresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 3 | fendstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 4 | fkeycol2id | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 5 | ftotaldiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 6 | fcurrdiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 7 | fconfiguredcodeid2 | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | ftracknumberid2 | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fendqty2 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 11 | fcurrunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 12 | fendunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 13 | fstartactcostupamt2 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 14 | fstartotherdiff2 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 15 | fcurramt2 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 16 | fendorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 17 | fprojectid2 | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | felementid2 | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 19 | ftotalfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 20 | ftotalotherdiff2 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 21 | fstartinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 22 | fcompfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 23 | fstartmadeupamt2 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 24 | fstartqty2 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 25 | fcompmadeupamt2 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 26 | fstartdiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 27 | fcompinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 28 | fstartstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 29 | fcompfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 30 | fstartstdcost2 | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 31 | ftotalmadeupamt2 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 32 | fcurrfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 33 | fendotherdiff2 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 34 | ftotalmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 35 | ftotalunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 36 | fendinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 37 | flot2 | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 38 | ftotalstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 39 | fcurrstdcost2 | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 40 | fcompqty2 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 41 | ftype2 | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :明细行 5 :综合行 |
| 42 | fcompstdcost2 | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fcompdiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 45 | ftotalorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 46 | fcurrorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 47 | fcurrotherdiff2 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 48 | fauxptyid2 | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 49 | fcurrqty2 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 50 | frelacostobjectid2 | 所属成本对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 51 | ftotalfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 52 | fcompactcostupamt2 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 53 | fcomporddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 54 | fkeycol2 | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |
| 55 | fcurrinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 56 | fcompunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 57 | fstartmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 58 | fendfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 59 | fmaterialid2 | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 60 | fcompamt2 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 61 | fsubelementid2 | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 62 | fstartorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 63 | fcurrfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 64 | fcompstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 65 | fcompotherdiff2 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 66 | fstartfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 67 | fenddiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 68 | fendfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 69 | fstartunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 70 | fcurrstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 71 | fcurrmadeupamt2 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 72 | ftotalinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 73 | fstartfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 74 | fendmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 75 | fbaseunitid2 | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 76 | fcurractcostupamt2 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 77 | fcurrmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 78 | fmatversionid2 | 版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 79 | fendmadeupamt2 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 80 | fstartamt2 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_subdiffresulte_obj |  | frelacostobjectid2 |
| 2 | idx_sco_subdiffresulte_tp |  | ftype2 |
| 3 | idx_sco_subdiffresultentry |  | fid |
| 4 | pk_sco_subdiffresultentry |  | fentryid |

---

## 差异分摊计算综合明细-分表 t_sco_comdiffresultentry_v

- **表名称：** 差异分摊计算综合明细-分表
- **表名：** t_sco_comdiffresultentry_v

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 3 | ftotaldiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 4 | fendreservediffw1 | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 5 | fendqty1 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fendunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 8 | fendorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 9 | ftotalreservediffx1 | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 10 | ftotalfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 11 | ftotalotherdiff1 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 12 | fcompreservediffw1 | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 13 | fcompfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 14 | fcompinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 15 | fcompmadeupamt1 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 16 | fcompfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 17 | fendactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 18 | fendreservediffx1 | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 19 | ftotalunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 20 | ftotalmadeupamt1 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |
| 21 | fendotherdiff1 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 22 | ftotalactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 23 | fendinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 24 | ftotalmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 25 | ftotalreservediffy1 | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 26 | ftotalstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 27 | fcompreservediffx1 | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 28 | fcompqty1 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fendstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 31 | fcompdiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 32 | ftotalqty1 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 33 | ftotalorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 34 | ftotalfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 35 | fendreservediffy1 | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 36 | fcomporddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 37 | fcompactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 38 | fcompunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 39 | fcompamt1 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 40 | fcompreservediffy1 | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 41 | fcompstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 42 | fendfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 43 | fcurrfalldiff1 | 跌价价差 | numeric | 23 | 10 | √ | 0 | 跌价价差 |
| 44 | fenddiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 45 | fstartfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 46 | fcompotherdiff1 | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 47 | ftotalamt1 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 48 | fendfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 49 | fendamt1 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 50 | ftotalinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 51 | ftotalreservediffw1 | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 52 | fendmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 53 | fendmadeupamt1 | 在制品更新差异 | numeric | 23 | 10 | √ | 0 | 在制品更新差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_comdiffresultentry_v |  | fid |
| 2 | pk_sco_comdiffresultentry_v |  | fentryid |

---

## 差异分摊计算分项明细-子表 t_sco_diffcalcresultentry

- **表名称：** 差异分摊计算分项明细-子表
- **表名：** t_sco_diffcalcresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fcurrstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 4 | fsrcbillno | fsrcbillno | varchar | 80 |  | √ | ' ' |  |
| 5 | ftotalqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fcurractcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性定义 bd_auxproperty |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fendunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 11 | ftotaldiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 12 | fcurrdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 13 | fstartamt | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 14 | fendactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 15 | ftotalunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 16 | fsrcseq | fsrcseq | int8 | 64 |  | √ | 0 |  |
| 17 | fstartstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 18 | fmatversionid | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 19 | fcurramt | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 20 | fendorddiff | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 21 | fcomporddiff | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 22 | ftotalorddiff | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 23 | ftotalactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 24 | fcurrunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 25 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 26 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fcurrorddiff | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 28 | fcompdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 29 | fstartunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 30 | fendamt | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 31 | fcompactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 32 | fenddiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 33 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 34 | fcompstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 35 | fcompunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 36 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 37 | fcompamt | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 38 | fstartorddiff | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 39 | ftotalamt | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 40 | fendqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 41 | fstartdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 42 | fendstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 43 | ftotalstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 44 | fstartactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 45 | fstartqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | fcurrqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 48 | fcompqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_diffcalcresultentry |  | fid,fseq |
| 2 | pk_sco_diffcalcresultentry |  | fentryid |

---

## 差异分摊计算分项明细-分表 t_sco_diffcalcresultentry_m

- **表名称：** 差异分摊计算分项明细-分表
- **表名：** t_sco_diffcalcresultentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 3 | fstartfeediff | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 4 | fendmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 5 | fstartfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | ftotalfeediff | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 8 | fcompmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 9 | fendotherdiff | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 10 | fcompfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 11 | fcompinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 12 | fendfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 13 | fendinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 15 | fcompotherdiff | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 16 | fstartinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 17 | ftotalotherdiff | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 18 | fendmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 19 | fstartmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 20 | fcurrfalldiff | 跌价价差 | numeric | 23 | 10 | √ | 0 | 跌价价差 |
| 21 | ftotalfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 22 | fcurrmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 23 | fcurrmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 24 | fcurrinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 25 | fcurrotherdiff | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 26 | ftotalmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 27 | fcurrfeediff | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 28 | ftotalinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 29 | fcompmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 30 | ftotalmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fcompfeediff | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 33 | fstartotherdiff | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 34 | fendfeediff | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_diffcalcresultentry_m |  | fentryid |
| 2 | idx_sco_diffcalcresultentry_m |  | fid |
