# 完工成本结转单-aca_finishcosttranfer

## 成本结转明细（综合）-子表 t_aca_finishcost_sonentry

- **表名称：** 成本结转明细（综合）-子表
- **表名：** t_aca_finishcost_sonentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fsubcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fsubbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsubmaterialid | fsubmaterialid | int8 | 64 |  | √ | 0 |  |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fsubunitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | finvoutsourcetype | 委外成本类型 | varchar | 30 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 D :物料 |
| 12 | fsubactualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_finishcost_sonentry |  | fdetailid |
| 2 | idx_aca_finishcostsonentry |  | fentryid |

---

## 完工成本结转单-主表 t_aca_finishcosttranfer

- **表名称：** 完工成本结转单-主表
- **表名：** t_aca_finishcosttranfer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fsourcecalid | 来源核算id(核算成本记录) | int8 | 64 |  | √ | 0 | 来源核算id(核算成本记录) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcalbilltype | 核算单类型 | varchar | 30 |  | √ | ' ' | 核算单类型,枚举: OUT :出库 IN :入库 |
| 8 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 9 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 11 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 17 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 19 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 20 | fsourcevoucher | 源单是否生成凭证 | bpchar | 1 |  | √ | '0' | 源单是否生成凭证 |
| 21 | fcreatvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_finishcost_cpv |  | fperiodid,fcostaccountid,fvouchernum |
| 2 | pk_t_aca_finishcosttranfer |  | fid |

---

## 物料明细-子表 t_aca_finishcost_entry

- **表名称：** 物料明细-子表
- **表名：** t_aca_finishcost_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 5 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 cal_bd_caldimension |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 10 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 11 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 14 | finvoutsourcetype | finvoutsourcetype | varchar | 30 |  | √ | ' ' |  |
| 15 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 16 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 18 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 19 | faccounttype | 计价方法 | varchar | 30 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 C :实时移动加权平均法 D :标准成本法 E :先进先出计价法 |
| 20 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 21 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 23 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_finishcost_entry |  | fentryid |
| 2 | idx_aca_finishcostentry_fid |  | fid |
