# 成本还原结果表-sco_costrecovry

## 单据体-子表 t_sco_costrecovryentry

- **表名称：** 单据体-子表
- **表名：** t_sco_costrecovryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fisleaf | 完工结构叶子节点 | bpchar | 1 |  | √ | ' ' | 完工结构叶子节点 |
| 4 | fsourceinfo | 源单信息 | varchar | 2000 |  | √ | ' ' | 源单信息 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpreqty | 期初数量 | numeric | 23 | 10 | √ | 0 | 期初数量 |
| 7 | famount | 本期完工金额 | numeric | 23 | 10 | √ | 0 | 本期完工金额 |
| 8 | factamount | 实际金额 | numeric | 23 | 10 | √ | 0 | 实际金额 |
| 9 | ftreepath | 树长路径 | varchar | 2000 |  | √ | ' ' | 树长路径 |
| 10 | fsubmaterialid | 子物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | fpursleaf | 采购结构叶子节点 | bpchar | 1 |  | √ | '0' | 采购结构叶子节点 |
| 12 | fpreamount | 期初金额 | numeric | 23 | 10 | √ | 0 | 期初金额 |
| 13 | fqty | 本期完工数量 | numeric | 23 | 10 | √ | 0 | 本期完工数量 |
| 14 | factqty | 实际数量 | numeric | 23 | 10 | √ | 0 | 实际数量 |
| 15 | fisunabsorb | 来源未吸收 | varchar | 2 |  | √ | ' ' | 来源未吸收,枚举: B :是 A :否 |
| 16 | fpuramount | 本期采购金额 | numeric | 23 | 10 | √ | 0 | 本期采购金额 |
| 17 | ftransleaf | 调拨结构叶子节点 | bpchar | 1 |  | √ | '0' | 调拨结构叶子节点 |
| 18 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 19 | ftransinamount | 本期调入金额 | numeric | 23 | 10 | √ | 0 | 本期调入金额 |
| 20 | fpurqty | 本期采购数量 | numeric | 23 | 10 | √ | 0 | 本期采购数量 |
| 21 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 22 | fsubmaterialauxpropid | 子物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 23 | ftransinqty | 本期调入数量 | numeric | 23 | 10 | √ | 0 | 本期调入数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fsubmaterialverid | 子物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_costrecovryentry |  | fid,fentryid |
| 2 | pk_sco_costrecovryentry |  | fentryid |

---

## 子单据体-子表 t_sco_costrecsubentry

- **表名称：** 子单据体-子表
- **表名：** t_sco_costrecsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubtranstype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :调拨入 B :采购入 |
| 2 | fsubperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | fsubtransorgid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsubtransqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | fsubpriceradio | 加价比 | numeric | 23 | 10 | √ | 0 | 加价比 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsubtransamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costrecsubentry |  | fdetailid |
| 2 | idx_sco_costrecsubentry |  | fentryid |

---

## 成本还原结果表-主表 t_sco_costrecovry

- **表名称：** 成本还原结果表-主表
- **表名：** t_sco_costrecovry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fheadpreamt | 期初金额 | numeric | 23 | 10 | √ | 0 | 期初金额 |
| 4 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcalcreportid | 成本还原计算报告 | int8 | 64 |  | √ | 0 | 成本还原计算报告 |
| 8 | fheadtotalamt | 实际金额 | numeric | 23 | 10 | √ | 0 | 实际金额 |
| 9 | fmaterialverid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fheadtransinqty | 本期调入数量 | numeric | 23 | 10 | √ | 0 | 本期调入数量 |
| 15 | fcaltime | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 16 | fheadpuramt | 本期采购金额 | numeric | 23 | 10 | √ | 0 | 本期采购金额 |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fbatchno | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fheadamount | 本期完工金额 | numeric | 23 | 10 | √ | 0 | 本期完工金额 |
| 25 | fheadqty | 本期完工数量 | numeric | 23 | 10 | √ | 0 | 本期完工数量 |
| 26 | fheadpreqty | 期初数量 | numeric | 23 | 10 | √ | 0 | 期初数量 |
| 27 | fheadtransinamt | 本期调入金额 | numeric | 23 | 10 | √ | 0 | 本期调入金额 |
| 28 | fheadpurqty | 本期采购数量 | numeric | 23 | 10 | √ | 0 | 本期采购数量 |
| 29 | fheadtotalqty | 实际数量 | numeric | 23 | 10 | √ | 0 | 实际数量 |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costrecovry |  | fid |
| 2 | idx_sco_costrecovrymat |  | fmaterialid,fmaterialverid,fauxpropid |
| 3 | idx_sco_costrecovry |  | fcostaccountid,fperiodid |
