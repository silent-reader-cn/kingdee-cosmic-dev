# 计算结果单-sca_calcresult

## 单据体-子表 t_sca_unabsorbentry

- **表名称：** 单据体-子表
- **表名：** t_sca_unabsorbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fpddiffqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 4 | fsourceinfo | 源单信息 | varchar | 2000 |  | √ | ' ' | 源单信息 |
| 5 | fmfgobjid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 6 | fpdcurramt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ftotaldiffqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 9 | fmfgprotype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 10 | fpdendamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 12 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :明细行 5 :汇总行 |
| 13 | fpdstartqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fpdstartamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 15 | fpdendqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fpddiffamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fpdcurrqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | ftotaldiffamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_unabsorbentry |  | fentryid |
| 2 | idx_sca_unabsorbentry |  | fid |

---

## 计算结果单-主表 t_sca_calcresult

- **表名称：** 计算结果单-主表
- **表名：** t_sca_calcresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbizstatus | 业务状态 | varchar | 30 |  | √ | 'A' | 业务状态,枚举: A :未结算 B :已结算 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsrcbilid | fsrcbilid | int8 | 64 |  | √ | 0 |  |
| 14 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_calcresult_pkey |  | fid |
| 2 | index_sca_calcresult |  | forgid,fcostobjectid,fcostcenterid,fperiodid,fcostaccountid |

---

## 单据体-子表 t_sca_calcresultentry

- **表名称：** 单据体-子表
- **表名：** t_sca_calcresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpdcurrtqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fcostupdatediffamt | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 5 | ftotalqty | 实际用量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际用量 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | ftotalamount | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 8 | fsourceinfo | 源单信息 | text | 0 |  |  | null | 源单信息 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fdiffqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 11 | fcalcbasis | 计算依据 | varchar | 30 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 12 | fcaltype | 计算类型 | varchar | 30 |  | √ | ' ' | 计算类型,枚举: 1 :期末材料 2 :期末制造费用 3 :完工材料 4 :完工制造费用 5 :最终结果 |
| 13 | fmatversionid | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 14 | fpdcurramount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 15 | fcostupdatediff | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fstdqty | 标准用量 | numeric | 23 | 10 | √ | 0.0000000000 | 标准用量 |
| 17 | fpdstartqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 18 | fpdendqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 19 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 20 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 21 | fstdamount | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 22 | fdiff | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 23 | fpdendamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 24 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 25 | fcostlevel | 工费阶级 | varchar | 30 |  | √ | ' ' | 工费阶级,枚举: 2 :本阶 3 :下阶 |
| 26 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 27 | fdifftype | 差异类型 | varchar | 30 |  | √ | ' ' | 差异类型,枚举: 1 :材料差异 2 :制造费用差异 3 :成本更新差异 |
| 28 | fpdstartamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 29 | fpdcompanount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 30 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性定义 bd_auxproperty |
| 33 | fpdcompqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 34 | fkeycol | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |
| 35 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: 1 :综合 2 :分项 3 :制造费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sca_calcresultentry |  | felementid,fsubelementid,fmaterialid |
| 2 | t_sca_calcresultentry_pkey |  | fentryid |
| 3 | idx_sca_calcresultentry2 |  | fid |

---

## 实际价差单据-子表 t_sca_calcresultprice

- **表名称：** 实际价差单据-子表
- **表名：** t_sca_calcresultprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpstdamount | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 3 | fppdcompamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 4 | fpmatversion | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 5 | fppdendqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 6 | fppdcompqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 7 | fptotalamount | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fpdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: 1 :综合 2 :分项 |
| 10 | fppdstartamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 11 | freceiptdiff | 发票差异 | numeric | 23 | 10 | √ | 0.0000000000 | 发票差异 |
| 12 | fcostupdatediff | 成本更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 成本更新差异 |
| 13 | fppdcurrqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 14 | fmfgfeediff | 制造费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 制造费用差异 |
| 15 | fpelement | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 16 | fpauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性定义 bd_auxproperty |
| 17 | forderdiff | 订单差异 | numeric | 23 | 10 | √ | 0.0000000000 | 订单差异 |
| 18 | fppdendamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 19 | ffactcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 20 | fmatdiff | 材料差异 | numeric | 23 | 10 | √ | 0.0000000000 | 材料差异 |
| 21 | ffeediff | 费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 费用差异 |
| 22 | funabsorbfeediff | 未吸收费用差异 | numeric | 23 | 10 | √ | 0.0000000000 | 未吸收费用差异 |
| 23 | fpsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 24 | fpmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 25 | fperiodtype | 差异期间类型 | varchar | 30 |  | √ | ' ' | 差异期间类型,枚举: 1 :完工差异 2 :累计差异 |
| 26 | fptotalqty | 实际用量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际用量 |
| 27 | fppdcurramount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fppdstartqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 30 | fpstdqty | 标准用量 | numeric | 23 | 10 | √ | 0.0000000000 | 标准用量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_calcresultprice_pkey |  | fentryid |
| 2 | idx_sca_calcresultprice |  | fpelement,fpsubelement |
