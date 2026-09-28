# 工序投入产出归集-aca_sfcinoutput

## 工序投入产出归集-分表 t_aca_sfcinoutput_q

- **表名称：** 工序投入产出归集-分表
- **表名：** t_aca_sfcinoutput_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frptqty | 工序汇报数量 | numeric | 23 | 10 | √ | 0 | 工序汇报数量 |
| 3 | fbeginsfcwipqty | 期初工序在制数量 | numeric | 23 | 10 | √ | 0 | 期初工序在制数量 |
| 4 | fcompleteqty | 本期完工数量 | numeric | 23 | 10 | √ | 0 | 本期完工数量 |
| 5 | fendrptwipqty | 期末汇报在制数量 | numeric | 23 | 10 | √ | 0 | 期末汇报在制数量 |
| 6 | fendsfcwipqty | 期末工序在制数量 | numeric | 23 | 10 | √ | 0 | 期末工序在制数量 |
| 7 | fdiffqty | 工序盘盈（亏） | numeric | 23 | 10 | √ | 0 | 工序盘盈（亏） |
| 8 | fbeginrptwipqty | 期初汇报在制数量 | numeric | 23 | 10 | √ | 0 | 期初汇报在制数量 |
| 9 | ftransferinqty | 工序转入数量 | numeric | 23 | 10 | √ | 0 | 工序转入数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aca_sfcinoutput_q |  | fid |
| 2 | idx_sfcinoutput_q |  | fdiffqty |

---

## 工序投入产出归集-主表 t_aca_sfcinoutput

- **表名称：** 工序投入产出归集-主表
- **表名：** t_aca_sfcinoutput

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproplanid | 工序计划号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 3 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmaterialid | 所属产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fissysauto | 盘点来源 | bpchar | 1 |  | √ | '0' | 盘点来源,枚举: 0 :- 1 :自动盘零 2 :外部引入 |
| 12 | fproplanentryid | 工序计划分录内码 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 16 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 17 | fbillno | 单据编号 | varchar | 510 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfcinoutput_costcenter |  | fcostcenterid |
| 2 | pk_aca_sfcinoutput |  | fid |
| 3 | idx_sfcinoutput_costobject |  | fcostobjectid |
| 4 | idx_sfcinoutput_proplan |  | fproplanid,fproplanentryid |
