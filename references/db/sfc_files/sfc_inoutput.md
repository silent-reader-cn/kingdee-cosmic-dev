# 车间投入产出-sfc_inoutput

## 车间投入产出-主表 t_sfc_inoutput

- **表名称：** 车间投入产出-主表
- **表名：** t_sfc_inoutput

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproplanid | 工序计划号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fworkid | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 14 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fworkrowid | 工单行id | int8 | 64 |  | √ | 0 | 工单行id |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_inoutput_caid |  | fcostaccountid |
| 2 | pk_sfc_inoutput |  | fid |
| 3 | idx_sfc_inoutput_capoid |  | fperiodid,fcostaccountid |

---

## 工序明细-子表 t_sfc_inoutputentry

- **表名称：** 工序明细-子表
- **表名：** t_sfc_inoutputentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquabaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 3 | finqty | 转入数量 | numeric | 23 | 10 | √ | 0 | 转入数量 |
| 4 | foutqty | 转出数量 | numeric | 23 | 10 | √ | 0 | 转出数量 |
| 5 | foutprodqty | 转出生产数量 | numeric | 23 | 10 | √ | 0 | 转出生产数量 |
| 6 | fdamageproqty | 损耗生产数量 | numeric | 23 | 10 | √ | 0 | 损耗生产数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fwastbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 9 | fperiodbeginnotoutbaseqty | 期初未转出基本数量 | numeric | 23 | 10 | √ | 0 | 期初未转出基本数量 |
| 10 | fwastqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 11 | fdamagebaseqty | 损耗基本数量 | numeric | 23 | 10 | √ | 0 | 损耗基本数量 |
| 12 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 13 | finbaseqty | 转入基本数量 | numeric | 23 | 10 | √ | 0 | 转入基本数量 |
| 14 | fperiodendnotoutbaseqty | 期末未转出基本数量 | numeric | 23 | 10 | √ | 0 | 期末未转出基本数量 |
| 15 | fperiodbeginnotoutprodqty | 期初未转出生产数量 | numeric | 23 | 10 | √ | 0 | 期初未转出生产数量 |
| 16 | fperiodendnotoutqty | 期末未转出数量 | numeric | 23 | 10 | √ | 0 | 期末未转出数量 |
| 17 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 18 | foutbaseqty | 转出基本数量 | numeric | 23 | 10 | √ | 0 | 转出基本数量 |
| 19 | fquaproduceqty | 合格生产数量 | numeric | 23 | 10 | √ | 0 | 合格生产数量 |
| 20 | fwastprodqty | 报废生产数量 | numeric | 23 | 10 | √ | 0 | 报废生产数量 |
| 21 | fperiodbeginnotoutqty | 期初未转出数量 | numeric | 23 | 10 | √ | 0 | 期初未转出数量 |
| 22 | finprodqty | 转入生产数量 | numeric | 23 | 10 | √ | 0 | 转入生产数量 |
| 23 | fdamageqty | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fperiodendnotoutprodqty | 期末未转出生产数量 | numeric | 23 | 10 | √ | 0 | 期末未转出生产数量 |
| 26 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_inoutputentry |  | fentryid |
| 2 | idx_sfc_inoutputentry_fid |  | fid |
