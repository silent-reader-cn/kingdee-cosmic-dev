# 差异分摊计算结果-sca_diffcalcresult

## 差异分摊计算结果-主表 t_sca_diffcalcresult

- **表名称：** 差异分摊计算结果-主表
- **表名：** t_sca_diffcalcresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrqtys | 本期数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期数量 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcalcreportid | 期末计算报告 | int8 | 64 |  | √ | 0 | 期末计算报告 |
| 5 | fbizstatus | 结算状态 | varchar | 30 |  | √ | ' ' | 结算状态,枚举: A :未结算 B :已结算 |
| 6 | fendqtys | 期末数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期末数量 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 10 | fstartqtys | 期初数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量 |
| 11 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 14 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fentryproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 21 | fcompqtys | 本期完工数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期完工数量 |
| 22 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 23 | ftotalqtys | 累计数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计数量 |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_diffcalcresult |  | fid |

---

## 差异分摊计算分项明细-分表 t_sca_diffcalcresultentry_m

- **表名称：** 差异分摊计算分项明细-分表
- **表名：** t_sca_diffcalcresultentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 3 | fstartfeediff | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 4 | fendmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 5 | fstartfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | ftotalfeediff | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 8 | fcompmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 9 | fendotherdiff | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 10 | fcompfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 11 | fcompinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 12 | fendfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 13 | fendinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 15 | fcompotherdiff | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 16 | fstartinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 17 | ftotalotherdiff | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 18 | fendmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 19 | fstartmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 20 | fcurrfalldiff | 跌价价差 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价价差 |
| 21 | ftotalfalldiff | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 22 | fcurrmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 23 | fcurrmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 24 | fcurrinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 25 | fcurrotherdiff | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 26 | ftotalmadediff | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 27 | fcurrfeediff | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 28 | ftotalinvoicediff | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 29 | fcompmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 30 | ftotalmadeupamt | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fcompfeediff | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 33 | fstartotherdiff | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 34 | fendfeediff | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_diffcalcresultentry_m |  | fentryid |
| 2 | idx_sca_diffcalcresultentry_m |  | fid |

---

## 差异分摊计算分项明细-子表 t_sca_diffcalcresultentry

- **表名称：** 差异分摊计算分项明细-子表
- **表名：** t_sca_diffcalcresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fcurrstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 4 | fsrcbillno | fsrcbillno | varchar | 60 |  | √ | ' ' |  |
| 5 | ftotalqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fcurractcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fendunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 11 | ftotaldiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 12 | fcurrdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 13 | fstartamt | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 14 | fendactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 15 | ftotalunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 16 | fsrcseq | fsrcseq | int8 | 64 |  | √ | 0 |  |
| 17 | fstartstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 18 | fmatversionid | 版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 19 | fcurramt | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 20 | fendorddiff | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 21 | fcomporddiff | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 22 | ftotalorddiff | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 23 | ftotalactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 24 | fcurrunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 25 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 26 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fcurrorddiff | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 28 | fcompdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 29 | fstartunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 30 | fendamt | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 31 | fcompactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 32 | fenddiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 33 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 34 | fcompstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 35 | fcompunjoindiffamt | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 36 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 37 | fcompamt | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 38 | fstartorddiff | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 39 | ftotalamt | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 40 | fendqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 41 | fstartdiffqty | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 42 | fendstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 43 | ftotalstdcostupamt | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 44 | fstartactcostupamt | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 45 | fstartqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | fcurrqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 48 | fcompqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_diffcalcresultentry |  | fid,fseq |
| 2 | pk_t_sca_diffcalcresultentry |  | fentryid |

---

## 差异分摊计算综合明细-分表 t_sca_comdiffresultentry_v

- **表名称：** 差异分摊计算综合明细-分表
- **表名：** t_sca_comdiffresultentry_v

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 3 | ftotalfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 4 | ftotaldiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 5 | fcomporddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 6 | fcompactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 7 | fendqty1 | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fendunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 10 | fendorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 11 | fcompunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 12 | ftotalfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 13 | ftotalotherdiff1 | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 14 | fcompamt1 | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 15 | fcompfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 16 | fcompstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 17 | fendfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 18 | fcompinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 19 | fcompmadeupamt1 | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 20 | fcurrfalldiff1 | 跌价价差 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价价差 |
| 21 | fcompfeediff1 | fcompfeediff1 | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fenddiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 23 | fendactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 24 | fstartfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 25 | fcompotherdiff1 | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 26 | ftotalamt1 | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 27 | fendfalldiff1 | 跌价差异 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价差异 |
| 28 | ftotalunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 29 | ftotalmadeupamt1 | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 30 | fendotherdiff1 | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 31 | fendamt1 | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 32 | ftotalinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 33 | fendmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 34 | ftotalactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 35 | fendinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 36 | ftotalmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 37 | ftotalstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 38 | fendmadeupamt1 | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 39 | fcompqty1 | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | fendstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 42 | fcompdiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 43 | ftotalqty1 | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 44 | ftotalorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_comdiffresultentry_v |  | fid |
| 2 | pk_t_sca_comdiffresultentry_v |  | fentryid |

---

## 差异分摊计算综合明细-子表 t_sca_comdiffresultentry

- **表名称：** 差异分摊计算综合明细-子表
- **表名：** t_sca_comdiffresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeycol1id | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 3 | fstartactcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 4 | fcurrinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 5 | frelacostobjectid1 | 所属成本对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 6 | fcurrqty1 | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 7 | fcurrdiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fcurrmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 10 | fcurrunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 11 | fkeycol1 | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |
| 12 | fstartotherdiff1 | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |
| 13 | fsrcbillid1 | fsrcbillid1 | int8 | 64 |  | √ | 0 |  |
| 14 | fcurramt1 | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 15 | fstartmadediff1 | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 16 | fstartorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 17 | fstartqty1 | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 18 | felementid1 | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 19 | fmaterialid1 | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fstartmadeupamt1 | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 21 | fstartinvoicediff1 | 发票价差 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价差 |
| 22 | fsubelementid1 | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 23 | fstartdiffqty1 | 材料耗用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料耗用差异 |
| 24 | fstartstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 25 | fcompfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 26 | fsrcseq1 | fsrcseq1 | int8 | 64 |  | √ | 0 |  |
| 27 | fstartunjoindiffamt1 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 28 | fcurrfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 29 | fcurrstdcostupamt1 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本变更差异 |
| 30 | fstartfeediff1 | 费用价差 | numeric | 23 | 10 | √ | 0.0000000000 | 费用价差 |
| 31 | fcurrmadeupamt1 | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 32 | fcurractcostupamt1 | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 33 | fbaseunitid1 | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fsrcbillno1 | fsrcbillno1 | varchar | 60 |  | √ | ' ' |  |
| 35 | ftype1 | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :明细行 5 :综合行 |
| 36 | fmatversionid1 | 版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 37 | fcurrorddiff1 | 订单价差 | numeric | 23 | 10 | √ | 0.0000000000 | 订单价差 |
| 38 | fstartamt1 | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fauxptyid1 | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 41 | fcurrotherdiff1 | 其他差异 | numeric | 23 | 10 | √ | 0.0000000000 | 其他差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_comdiffresultentry |  | fid |
| 2 | pk_t_sca_comdiffresultentry |  | fentryid |

---

## 单据体-子表 t_sca_subdiffresultentry

- **表名称：** 单据体-子表
- **表名：** t_sca_subdiffresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 3 | fendstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 4 | fkeycol2id | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 5 | ftotaldiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 6 | fcurrdiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcurrunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 9 | fendunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 10 | fstartotherdiff2 | 其他差异 | numeric | 23 | 10 | √ | 0 | 其他差异 |
| 11 | fcurramt2 | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 12 | fendorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 13 | felementid2 | 成本要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 14 | ftotalfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 15 | ftotalotherdiff2 | 其他差异 | numeric | 23 | 10 | √ | 0 | 其他差异 |
| 16 | fstartinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 17 | fcompfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 18 | fstartmadeupamt2 | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 19 | fcompmadeupamt2 | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 20 | fstartdiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 21 | fcompinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 22 | fstartstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 23 | fcompfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 24 | ftotalmadeupamt2 | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 25 | fcurrfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 26 | fendotherdiff2 | 其他差异 | numeric | 23 | 10 | √ | 0 | 其他差异 |
| 27 | ftotalmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 28 | ftotalunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 29 | fendinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 30 | ftotalstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 31 | fcurrstdcost2 | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fcompdiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 34 | ftotalorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 35 | fcurrorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 36 | fcurrotherdiff2 | 其他差异 | numeric | 23 | 10 | √ | 0 | 其他差异 |
| 37 | fauxptyid2 | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 38 | fcurrqty2 | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 39 | frelacostobjectid2 | 所属成本对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 40 | ftotalfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 41 | fcomporddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 42 | fkeycol2 | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |
| 43 | fcurrinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 44 | fcompunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 45 | fstartmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 46 | fendfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 47 | fmaterialid2 | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 48 | fsubelementid2 | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 49 | fstartorddiff2 | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 50 | fcurrfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 51 | fcompstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 52 | fcompotherdiff2 | 其他差异 | numeric | 23 | 10 | √ | 0 | 其他差异 |
| 53 | fstartfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 54 | fenddiffqty2 | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 55 | fendfalldiff2 | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 56 | fstartunjoindiffamt2 | 未吸收费用差异 | numeric | 23 | 10 | √ | 0 | 未吸收费用差异 |
| 57 | fcurrstdcostupamt2 | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 58 | fcurrmadeupamt2 | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 59 | ftotalinvoicediff2 | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 60 | fstartfeediff2 | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 61 | fendmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 62 | fbaseunitid2 | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 63 | fcurractcostupamt2 | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 64 | fcurrmadediff2 | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 65 | fmatversionid2 | 版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 66 | fendmadeupamt2 | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_subdiffresultentry |  | fentryid |
| 2 | idx_sca_subdiffresultentry |  | fid |
